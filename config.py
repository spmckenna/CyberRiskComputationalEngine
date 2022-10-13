INPUTS = {
    'numberOfMonteCarloRuns': 1000,
    'impactCalcMode': 'mean',  # mean or max
    'riskMode': 'probabilistic',  # certainty or probabilistic
    'timeWindow': 1,  # 1 year
    'baselineProbability': 0.05,
    'confidenceAlpha': 0.05,
    'scoring_lambda': 0.2,
    'scoring_fit': [11.80, -2.95],
    'tac_v_ctrl_coeffs': [0.174147,
                          -0.931719,
                          2.339254,
                          1.097710,
                          -1.370110,
                          -2.272632,
                          -0.315703,
                          -0.931118,
                          1.924220,
                          0.836075]

}
THREAT_ACTOR_CAPACITY_VALUES = {
    'determination': {
        'low': 0.1,
        'medium': 0.5,
        'high': 0.9
    },
    'api_resources': {
        'individual': 0.2,
        'club': 0.4,
        'contest': 0.1,
        'team': 0.5,
        'organization': 0.8,
        'government': 0.95
    },
    'sophistication': {
        'none': 0.1,
        'minimal': 0.28,
        'intermediate': 0.46,
        'advanced': 0.64,
        'expert': 0.82,
        'innovator': 0.82,
        'strategic': 0.95
    }
}
THREAT_ACTOR_CAPACITY_WEIGHTS = {
    'determination': 0.9,
    'sophistication': 1,
    'api_resources': 0.8
}