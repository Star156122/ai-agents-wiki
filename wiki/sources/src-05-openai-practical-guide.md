---
title: OpenAI — A practical guide to building agents
type: source
sources: []
updated: 2026-11-17
---

- **url**：https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf
- **fetched**：2026-11-17
- **類型**：官方指南（OpenAI）。發布日期：來源未標示。

## 重點摘要
- 定義：agent 是能代替使用者獨立完成任務的系統；它用 LLM 管理工作流程並做決策，能判斷任務何時完成、必要時自我修正，失敗時把控制權交還給使用者。單輪的聊天機器人不算 agent。
- 適合建 agent 的情境（三個跡象）：需要複雜判斷或例外處理、規則集龐大難以維護、高度依賴非結構化資料。不明顯符合時，確定性的方案可能就夠。
- 三大核心組件：**模型**（推理與決策）、**工具**（資料工具、行動工具、編排工具）、**指示**（清楚的逐步指引，含邊界情況）。
- 編排模式：**單一 agent 迴圈**（建議的起點，迴圈直到達到結束條件，如沒有更多工具呼叫、產出最終結果、錯誤或回合上限）、**manager 模式**（中央 agent 透過工具呼叫指派專家 agent）、**decentralized 模式**（agent 之間互相交棒）。
- **護欄**：建議多層疊加，包含相關性與安全分類器、個資過濾、規則式檢查、工具風險分級、輸出驗證；並在失敗次數過多或高風險、不可逆動作（如大額付款）時由人類介入。

## 限制與注意
- 頁面未標示發布日期，本 Wiki 不推測日期。

> "systems that independently accomplish tasks on your behalf"
