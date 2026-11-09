# AI 时代观察站

持续观察 AI 如何改变工作、组织与商业，并基于证据形成可修订的判断。

## 从问题出发

1. 什么正在变得可能，什么仍然做不到？
2. 工作、岗位和组织会怎样重新组合？
3. 价值、控制权和风险流向谁？

这些是观察视角，不是永久边界。研究对象涵盖工作、组织、产品、服务与商业；保留探索线索以发现已有框架之外的变化，不建设泛资讯门户。

## 阅读入口

- [可视化网站](https://ai-era-observatory.nesnilnehc.chatgpt.site)
- [研究方法](RESEARCH_METHOD.md)
- [概念关系](topics/roles-and-delivery.md)
- [Q001：构建能力普及后的分工](questions/Q001.md)
- [Q002：从局部提速到可靠成果](questions/Q002.md)
- [Q003：持续付费与交付风险](questions/Q003.md)
- [判断记录](judgments/README.md)与[情景蓝图](blueprints/README.md)

初版为研究起点：3 个问题、2 条待核探索线索、5 个来源。招聘要求不是效果证据，学习路线不是行业标准，条件情景不是预测。

## 内容与网站同源

`data/observatory.json` 是结构化内容的唯一编辑源。`scripts/build.py` 生成问题文档和 `dist/`；网站模板位于 `website/`。不手改生成文件。

```bash
python3 scripts/build.py
python3 -m unittest discover -s tests -p 'test_*.py'
python3 scripts/build.py --check
node --check website/app.js
git diff --check
```

网站为静态 HTML/CSS/JavaScript，无登录、数据库、追踪或外部脚本。部署配置位于 `.openai/hosting.json`；不自动运行资料采集或定时推送。维护和发布流程见 [DEPLOYMENT.md](DEPLOYMENT.md)。

## 与其他项目的关系

[ai-era-software](https://github.com/nesnilnehc/ai-era-software)聚焦软件研发、工程治理和质量保障。本项目拓展到工作、组织与经营变化，交叉材料优先引用，不修改原项目政策或自动化。

## 版权与贡献

[贡献说明](CONTRIBUTING.md) · [授权说明](RIGHTS.md)。首版原创内容与代码许可尚待维护者确认；公开可读不等于授予开放再利用许可。第三方材料保留其原有权利。本项目不复制第三方全文或私有数据。
