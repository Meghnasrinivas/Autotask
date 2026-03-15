from typing import Dict, List


def summarize(agent_responses: Dict[str, List[str]], query: str) -> str:
    lines = [f"Summary for query: {query}"]
    for agent_id, responses in agent_responses.items():
        lines.append(f"--- {agent_id} ---")
        lines.extend([r for r in responses[-2:]])
    lines.append("Final conclusion: Multi-agent combined insights provided.")
    return "\n".join(lines)
