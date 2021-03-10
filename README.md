# e-flask

> 个人使用模版

## Build Setup

```bash
# 确保全局环境有 poetry
pip install poetry

# 安装依赖
poetry install

# 测试
flask run

# 生产测试数据库
flask shell
>>> from config import db
>>> db.create_all()
```