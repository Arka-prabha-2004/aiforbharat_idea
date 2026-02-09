def mock_bedrock_response(prompt: str):
    return {
        "recommendations": [
            {
                "platform_name": "YouTube",
                "match_score": 88,
                "reasoning": "Long-form educational content performs well and allows deep explanations.",
                "audience_fit": "Students and self-learners",
                "time_investment": "Medium",
                "monetization_potential": "High",
                "content_optimization_tips": [
                    "Use clear titles",
                    "Add chapter timestamps",
                    "Post weekly"
                ]
            },
            {
                "platform_name": "Medium",
                "match_score": 76,
                "reasoning": "Good for structured written explanations and credibility building.",
                "audience_fit": "Academic readers",
                "time_investment": "Low",
                "monetization_potential": "Medium",
                "content_optimization_tips": [
                    "Use diagrams",
                    "Keep posts 5–7 min read"
                ]
            }
        ],
        "overall_strategy": "Batch create content on weekends and schedule 2 posts per week.",
        "next_steps": [
            "Create a consistent posting calendar",
            "Track engagement monthly"
        ]
    }
