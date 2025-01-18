
def calculate_risk_score(analysis):
    score = 0
    keyword_counts = analysis["keyword_analysis"]
    score += keyword_counts.get("blockchain", 0) * 2
    score += keyword_counts.get("tokenomics", 3)
    score += 10 if analysis.get("contains_roadmap", False) else -5
    return max(0, min(100, score))
