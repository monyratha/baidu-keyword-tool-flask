# 百度关键词提取工具 🤖

这是一个基于 Flask 的网络应用程序，用于从百度搜索结果中提取相关关键词。该工具通过抓取百度移动搜索界面，帮助您发现与您的关键词相关的术语和建议。

## 功能特点

- 从百度搜索结果中提取相关关键词
- 支持多个关键词（每行一个）
- 清新现代的用户界面，支持深色模式
- 一键复制结果到剪贴板
- 在浏览器本地存储中安全保存凭据
- 移动端响应式设计

## 系统要求

- Python 3.x
- Flask 2.3.3
- Requests 2.31.0
- BeautifulSoup4 4.12.2

## 安装步骤

1. 克隆此仓库：
```bash
git clone https://github.com/monyratha/baidu-keyword-tool-flask.git
cd baidu-keyword-tool-flask
```

2. 创建并激活虚拟环境：
```bash
python -m venv venv
source venv/bin/activate  # Windows系统使用: venv\Scripts\activate
```

3. 安装所需包：
```bash
pip install -r requirements.txt
```

## 使用方法

1. 启动 Flask 应用：
```bash
python app.py
```

2. 打开网络浏览器并访问 `http://localhost:5000`

3. 配置百度登录凭据：
   - 点击 "🔐 配置百度登录"
   - 输入您百度账号的 BAIDUID、BDUSS 和 BDORZ cookie
   - 这些凭据将保存在浏览器的本地存储中

4. 在文本区域输入关键词（每行一个）

5. 点击 "🧠 提取" 获取每个词的相关关键词

6. 使用 "📋 复制" 按钮将所有结果复制到剪贴板

## 项目结构

```
.
├── app.py              # Flask主应用程序
├── requirements.txt    # Python依赖包
├── static/
│   └── style.css      # CSS样式（嵌入在index.html中）
└── templates/
    └── index.html     # 主HTML模板
```

## 安全说明

此应用程序需要百度登录凭据（cookies）才能正常运行。这些凭据：
- 安全存储在浏览器的本地存储中
- 仅发送到百度的服务器
- 从不存储在应用程序服务器上

## 许可证

本项目采用 [MIT 许可证](./LICENSE) 授权。

> ⚠️ **注意：** 这是一个个人学习项目。  
> 我构建它是为了练习 Python、Flask 和网络爬虫技术。  
> 欢迎探索、学习或改进它。

您可以在 MIT 许可证条款下自由使用、修改和分发此代码。  
详细信息请参见 `LICENSE` 文件。