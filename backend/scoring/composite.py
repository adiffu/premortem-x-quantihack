def compute_composite_score(signals):
    """
    Weighted fragility score per company.
    Ref: premortem_architecture.jsx
    """
    weights = {
        "fda": 0.23,      # T1 - most credible
        "reddit": 0.18,   # T1 - live consumer signal
        "wiki": 0.18,     # T1 - quant novelty
        "fred": 0.14,     # T1 - macro context
        "adzuna": 0.11,   # T2 - talent signal
        "edgar": 0.08,    # T2 - legal signal
        "trends": 0.08,   # T2 - search-intent stress signal
    }
    
    score = 0.0
    for key, weight in weights.items():
        val = signals.get(key, 0.0)
        score += val * weight
        
    # Scale to 0-10
    return min(round(score * 10, 2), 10.0)

if __name__ == "__main__":
    test_signals = {"fda": 0.5, "reddit": 0.8, "wiki": 0.3}
    print(compute_composite_score(test_signals))
