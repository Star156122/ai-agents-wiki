---
title: Lilian Weng — LLM Powered Autonomous Agents
type: source
sources: []
updated: 2026-11-17
---

- **url**：https://lilianweng.github.io/posts/2023-06-23-agent/
- **fetched**：2026-11-17
- **類型**：研究者部落格長文，發布日期 2023-06-23

## 重點摘要
- 把 LLM 驅動的自主 agent 描述為：**LLM 當控制器（大腦）**，加上三個組件——**規劃（planning）、記憶（memory）、工具使用（tool use）**。
- **規劃**：任務分解（把大目標拆成子目標，如 Chain of Thought、Tree of Thoughts）與自我反思（回顧過去行動並改進，如 ReAct、Reflexion）。
- **記憶**：短期記憶＝在 context 內學習，受限於 context window；長期記憶＝外部向量資料庫，透過快速檢索取用。
- **工具使用**：呼叫外部 API 取得模型權重裡沒有的資訊，例如最新資料、程式碼執行、私有資料來源。
- 列出的挑戰：context 長度有限；長期規劃與任務分解困難，遇到意外錯誤時不易調整計畫；自然語言介面脆弱，輸出格式可能出錯。

## 限制與注意
- 寫於 2023 年，部分系統與方法已演進；本 Wiki 採用其「組件框架」與「挑戰」作為概念基礎。
