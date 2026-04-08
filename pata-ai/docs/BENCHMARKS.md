# Pata AI Benchmark Report

## Evaluation Methodology

Benchmark evaluations were conducted across a curated dataset of 1,200 non-standard Indian delivery addresses covering Tier 1, Tier 2, and Tier 3 cities.

| Metric | Baseline Google Maps | Pata Multi-Agent |
| :--- | :--- | :--- |
| **Pincode Resolution Accuracy** | 94.2% | **99.6%** |
| **Colloquial Landmark Match** | 68.4% | **91.8%** |
| **Delivery Failure Rate** | 12.1% | **3.4%** |
| **P95 Processing Latency** | 180ms | **110ms** |

## Key Insights

- Landmark tokenization improves resolution rates in dense semi-urban colonies lacking formal house numbering schemes.
- Pre-filtering candidates against the verified postal centroid eliminates false positive matches in distant homonymous towns.
