
# Bonus / Stretch Goals – RFQ Similarity Assessment

## 1. Overview
This notebook contains the bonus/advanced tasks for the RFQ similarity and analysis assessment.
The main goals are:

- Ablation Analysis: Understanding the impact of different feature groups (dimensions, grades, categorical features) on similarity.

- Alternative Similarity Metrics: Using different similarity measures (cosine similarity, weighted cosine, Jaccard) for more robust matching.

- Clustering: Grouping RFQs into families for visualization and interpretation.

All outputs are saved in the folder: bonus_task_output.

## 2. Datasets
- 'rfq.csv' – Original RFQs
- 'reference_properties.tsv' – Reference material/grade properties
- 'rfq_with_clusters.csv' – RFQs annotated with cluster labels
- 'top3_bonus.csv' – Top-3 similar RFQs per RFQ based on combined similarity
- 'pca_coordinates.csv' – PCA coordinates for cluster visualization

## 3. Steps Performed

### 3.1 Data Preparation
- Loaded 'rfq.csv and 'reference_properties.tsv'.
- Normalized grades and parsed numeric ranges (min, max, mid) for dimensions and material properties.
- Joined RFQs with reference properties and flagged missing references.

### 3.2 Ablation Analysis
- Computed cosine similarity for:
    - Dimensions only
    - Grades only
    - Combined (weighted)
- Visualized mean similarity to show the impact of dropping feature groups.

### 3.3 Alternative Metrics
- Used different similarity metrics:
    - Weighted cosine similarity for numeric features
    - Jaccard similarity for categorical features (coating, finish, form, surface type)
- Combined weighted metrics to compute overall similarity.
- Extracted top-3 matches for each RFQ.

### 3.4 Clustering
- Standardized numeric features (dimensions + grades) and encoded categorical features.
- Applied KMeans clustering to group RFQs.
- Visualized clusters using PCA (2D plot).
- Saved RFQs with cluster labels and PCA coordinates.

## 4. How to Use
1. Open 'top3_bonus.csv' to see the top-3 similar RFQs for each RFQ.
2. Open 'rfq_with_clusters.csv' to view cluster assignments.
3. Open 'pca_coordinates.csv' to visualize clusters in a 2D PCA space.
4. Refer to this README for context on the methodology used.

## 5. Notes
- Similarity metrics are weighted; numeric mid-values were used if available, else min-values.
- Ablation analysis helps understand the impact of different feature groups on similarity.
- Clustering provides an overview of RFQ families for quick categorization.

