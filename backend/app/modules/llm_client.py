import os

from openai import OpenAI

api_key = os.getenv('OPENAI_API_KEY')
client = OpenAI(api_key=api_key) if api_key else None


def llm_generate(prompt: str, model: str = 'gpt-4o-mini', temperature: float = 0.2) -> str:
    if client is None:
        return f"[LLM not configured] {prompt[:240]}..."

    resp = client.responses.create(
        model=model,
        temperature=temperature,
        max_tokens=700,
        input=prompt,
    )

    # openai v1 responses response structure may contain output_text or output[0].content
    if hasattr(resp, 'output_text') and resp.output_text:
        return resp.output_text

    if hasattr(resp, 'output') and resp.output:
        items = []
        for o in resp.output:
            if isinstance(o, dict) and 'content' in o:
                items.append(o['content'])
            elif isinstance(o, str):
                items.append(o)
        return ''.join(items)

    return str(resp)
