---
title: 工具與 MCP
type: concept
sources: [src-05, src-03, src-04, src-01]
updated: 2026-11-17
---

# 工具與 MCP

## 工具是什麼
工具是 agent 可呼叫的函式或 API，讓它取得模型權重裡沒有的資訊或影響外部系統。[src-04]

OpenAI 把工具分成三類：[src-05]
- **資料工具**：取得上下文，例如資料庫查詢、網頁搜尋。
- **行動工具**：改變系統，例如寄信、更新紀錄。
- **編排工具**：讓一個 agent 把另一個 agent 當作工具來呼叫。

## 設計好工具很重要
Anthropic 強調 **agent-computer interface**：工具要有清楚的文件、經過測試、參數設計良好（例如要求使用絕對路徑以避免出錯）。[src-01]

## MCP：讓工具接入變標準
- **MCP（Model Context Protocol）** 是開源標準，把 AI 助理連接到資料所在的地方。[src-03]
- 痛點：每個新資料來源都需要客製整合，難以擴充；MCP 用共通協定取代。[src-03]
- 架構：**MCP server** 公開資料，**MCP client**（AI 應用）連接 server。[src-03]
- 公告日期：2024-11-25；當時已有 Google Drive、Slack、GitHub、Git、Postgres、Puppeteer 等預建 server。[src-03]

## 相關
[agent-components.md](agent-components.md)
