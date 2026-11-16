---
title: ReAct — Synergizing Reasoning and Acting in Language Models
type: source
sources: []
updated: 2026-11-17
---

- **url**：https://arxiv.org/abs/2210.03629
- **fetched**：2026-11-17
- **類型**：學術論文（Yao 等人，ICLR 2023）

## 重點摘要
- 提出 **ReAct**：讓凍結的大型語言模型交錯產生「推理軌跡」與「任務行動」。
- 推理幫助模型規劃、追蹤進度、處理意外；行動讓模型從外部（如 Wikipedia API 或互動環境）取得資訊。
- 要解決的問題：純 chain-of-thought 沒有接地到外部世界，容易幻覺並讓錯誤沿推理鏈累積；純行動則缺乏抽象推理來設定目標與追蹤進度。
- 在 HotpotQA 與 FEVER 上，靠檢索資訊降低幻覺；在 ALFWorld 與 WebShop 上，僅用一到兩個範例的提示，成功率就勝過模仿學習與強化學習方法。

## 限制與注意
- 摘要提到的成功率提升幅度（ALFWorld、WebShop）為論文報告的絕對數字，本 Wiki 不在概念頁重複，避免誤用。
- 只讀取了頁面前段內容，細節以論文本文為準。

> "reasoning traces help the model induce, track, and update action plans"
