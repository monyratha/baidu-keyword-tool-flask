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


def fetch_related_terms(keyword, headers, cookies):
    url = f"https://m.baidu.com/s?wd={keyword}"
    try:
        res = requests.get(url, headers=headers, cookies=cookies, timeout=10)
        res.raise_for_status()
        soup = BeautifulSoup(res.text, "html.parser")
        results = set()
        for row in soup.select(
                "div.cos-row.cos-space-pb-xs.font-size-upgrade_2fasj, div.cos-row.font-size-upgrade_2fasj"):
            for col in row.select("div.cos-col"):
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
    results = []
    if request.method == "POST":
        keywords = request.form.get("keywords", "").strip()
        baiduid = request.form.get("baiduid", "").strip()
        bduss = request.form.get("bduss", "").strip()
        bdorz = request.form.get("bdorz", "").strip()

        if not (keywords and baiduid and bduss and bdorz):
            flash("Please fill in all fields.")
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

    return render_template("index.html", results=results)


if __name__ == "__main__":
    app.run(debug=True)
