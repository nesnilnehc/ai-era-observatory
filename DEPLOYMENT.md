# 构建与发布

数据源：data/observatory.json。模板：website/。运行 python3 scripts/build.py 生成 dist/ 与问题文档；运行 README 中列出的检查。

Sites 托管只使用 dist/ 和 .openai/hosting.json。GitHub 保留完整内容与构建来源。发布应从已验证的同一源码状态打包，通过 Sites 官方源码 helper 提交、保存版本并部署，记录版本、源码提交和验证结果。不要上传凭据、临时文件或整个工作区。

首版不配置自动采集、定时推送、网站自动部署或自定义域名。后续发布须保持数据与 GitHub 来源一致，并重新核验并发修改。
