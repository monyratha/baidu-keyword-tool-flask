# MIT License
# Copyright (c) 2024 Lucas
# See LICENSE file in the project root for full license text.

from flask import Flask, render_template, request, flash
from bs4 import BeautifulSoup
import requests
import logging

logging.basicConfig(level=logging.INFO)

app = Flask(__name__)
app.secret_key = 'lucas-rules'

LANGUAGES = {
    'en': {
        'title': 'Baidu Keyword Extractor 🤖',
        'keywords_label': 'Keywords (one per line):',
        'configure_login': '🔐 Configure Baidu Login',
        'extract': '🧠 Extract',
        'scraping': 'Scraping Baidu…',
        'results': 'Results:',
        'copy_btn': 'Copy',
        'copied': '✅ Results copied to clipboard!',
        'fill_in': 'Please fill in all fields.'
    },
    'zh': {
        'title': '百度关键词提取工具 🤖',
        'keywords_label': '关键词（每行一个）：',
        'configure_login': '🔐 配置百度登录',
        'extract': '🧠 提取',
        'scraping': '正在抓取百度…',
        'results': '结果：',
        'copy_btn': '复制',
        'copied': '✅ 已复制到剪贴板！',
        'fill_in': '请填写所有字段。'
    }
}


def fetch_related_terms(keyword, headers, cookies):
    url = f"https://m.baidu.com/s?wd={keyword}"
    try:
        res = requests.get(url, headers=headers, cookies=cookies, timeout=10)
        res.raise_for_status()
        soup = BeautifulSoup(res.text, "html.parser")
        results = set()
        for row in soup.select(
                "div.cos-row.cos-gutter.cos-space-pb-xs.font-size-upgrade_2fasj, div.cos-row.font-size-upgrade_2fasj"):
            for col in row.select("div.cos-col-6"):
                for span in col.select("span.content-link_2AXFK.c-fwb"):
                    results.add(span.text.strip())
        return results
    except requests.RequestException as e:
        logging.error("Network error fetching %s: %s", keyword, e)
        return {f"[ERROR] {keyword}"}
    except Exception as e:
        logging.exception("Parsing error for %s", keyword)
        return {f"[ERROR] {keyword}: {e}"}


@app.route("/", methods=["GET", "POST"])
def index():
    lang = request.args.get("lang", "en")
    if lang not in LANGUAGES:
        lang = "en"
    t = LANGUAGES[lang]

    results = []
    if request.method == "POST":
        keywords = request.form.get("keywords", "").strip()
        baiduid = request.form.get("baiduid", "").strip()
        bduss = request.form.get("bduss", "").strip()
        bdorz = request.form.get("bdorz", "").strip()

        if not (keywords and baiduid and bduss and bdorz):
            flash(t['fill_in'])
        else:
            cookies = {
                "BAIDUID": baiduid,
                "BDUSS": bduss,
                "BDORZ": bdorz
            }

            headers = {
                "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) "
                              "AppleWebKit/605.1.15 (KHTML, like Gecko) "
                              "Version/16.6 Mobile/15E148 Safari/604.1"
            }

            seen_keywords = set()

            for kw in keywords.splitlines():
                kw_clean = kw.strip()
                if kw_clean and kw_clean not in seen_keywords:
                    seen_keywords.add(kw_clean)
                    terms = fetch_related_terms(kw_clean, headers, cookies)
                    results.append((kw_clean, sorted(terms)))

    return render_template("index.html", results=results, lang=lang, t=t)


if __name__ == "__main__":
    app.run(debug=True)
