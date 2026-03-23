# 📊 Rating Product & Sorting Reviews in Amazon

---

## 🧩 Business Problem

One of the most critical challenges in e-commerce is accurately calculating product ratings based on post-purchase feedback.

Solving this problem leads to:
- Improved **customer satisfaction**
- Better **product visibility** for sellers
- A more **seamless shopping experience** for buyers

Another key challenge is properly **sorting product reviews**. Misleading or low-quality reviews appearing at the top can directly impact product sales, leading to:
- Financial loss
- Loss of customer trust

By addressing these two core problems:
- E-commerce platforms and sellers can **increase sales**
- Customers can complete their purchasing journey **smoothly and confidently**

---

## 📁 Dataset Story

This dataset contains **Amazon product data**, including product categories and various metadata.

It focuses on:
- The **most-reviewed product** in the electronics category
- User ratings and review data

---

## 📌 Variables

| Variable | Description |
|----------|-------------|
| **reviewerID** | User ID |
| **asin** | Product ID |
| **reviewerName** | User Name |
| **helpful** | Helpfulness rating |
| **reviewText** | Review text |
| **overall** | Product rating |
| **summary** | Review summary |
| **unixReviewTime** | Review timestamp |
| **reviewTime** | Raw review time |
| **day_diff** | Number of days since the review |
| **helpful_yes** | Number of helpful votes |
| **total_vote** | Total number of votes |

---

## 🎯 Project Objectives

- Calculate **time-weighted average rating**
- Compare it with the **standard average rating**
- Identify the **top 20 most helpful reviews**
- Apply scoring methods:
  - `score_pos_neg_diff`
  - `score_average_rating`
  - `wilson_lower_bound`

---

## 🛠️ Methodology

- Time-based weighting of ratings
- Review scoring using statistical methods
- Ranking reviews based on **Wilson Lower Bound**

---

## 🚀 Expected Outcome

- More reliable product ratings  
- Better review ranking system  
- Improved user trust and engagement  
