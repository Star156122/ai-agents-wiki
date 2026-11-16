---
title: Anthropic — Introducing the Model Context Protocol
type: source
sources: []
updated: 2026-11-17
---

- **url**：https://www.anthropic.com/news/model-context-protocol
- **fetched**：2026-11-17
- **類型**：官方公告（Anthropic），發布日期 2024-11-25

## 重點摘要
- **MCP（Model Context Protocol）** 是開源標準，用來把 AI 助理連接到資料所在的地方，如內容庫、商業工具與開發環境。
- 要解決的問題：資料散落在孤立的系統中，每接一個新資料來源就要寫一套客製整合，難以擴充。MCP 用一個共通協定取代這些一次性整合。
- 架構：開發者可以用 **MCP server** 公開自己的資料，或建立 **MCP client**（AI 應用）去連接這些 server。
- 公告當時已有預建 server：Google Drive、Slack、GitHub、Git、Postgres、Puppeteer；早期採用者包含 Block 與 Apollo。

## 限制與注意
- 這是 2024 年底的公告，之後的生態與規格可能已變動；本 Wiki 只採用其「為何需要、基本架構」的概念。
