---
title: Anthropic — Building effective agents
type: source
sources: []
updated: 2026-11-17
---

- **url**：https://www.anthropic.com/engineering/building-effective-agents
- **fetched**：2026-11-17
- **類型**：官方工程文章（Anthropic）

## 重點摘要
- 把「agentic systems」分成兩類：**workflow**（LLM 與工具照預先寫好的程式路徑走）與 **agent**（LLM 自己決定步驟與工具使用，掌控完成任務的方式）。
- 基本建構單元是 **augmented LLM**：LLM 加上檢索、工具與記憶。
- 列出五種 workflow 模式：prompt chaining、routing、parallelization、orchestrator-workers、evaluator-optimizer。
- 建議從最簡單的方案開始，很多時候單次 LLM 呼叫加檢索就夠；只有在確實有幫助時才增加複雜度。
- Agent 適合步驟數無法預先決定的開放式問題；代價是成本較高、錯誤可能累積，需要在沙箱測試並設置護欄。
- 設計原則：保持簡單、讓規劃步驟透明、用心設計 agent-computer interface（工具文件與參數設計）。

## 限制與注意
- 文章自述其工具相關建議寫於 2024 年 12 月，Anthropic 現行做法已有變化。
- 本 Wiki 只引用其概念性內容，不引用特定工具細節。
- 本頁沒有直接引用：擷取到的內容是摘要，無法保證逐字正確，因此全部改寫。
