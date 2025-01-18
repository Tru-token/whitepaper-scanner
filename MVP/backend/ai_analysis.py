
def analyze_whitepaper(text):
    keywords = ["blockchain", "tokenomics", "roadmap", "team"]
    keyword_analysis = {key: text.lower().count(key) for key in keywords}
    return {
        "keyword_analysis": keyword_analysis,
        "length": len(text.split()),
        "contains_roadmap": "roadmap" in text.lower()
    }
