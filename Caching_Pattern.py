#What it does: Stores previous LLM responses so you don’t pay or wait again.
# Logic / Steps:
# Check if query exists in cache
# If yes → return cached result
# If no → call LLM → save result in cache
# Memory tip: Think “Check → Use → Save”
import llm_call
cache={}

def cache_llm(prompt):
    if prompt in cache:
        print("⚡ Cache hit")
        return cache[prompt]
    print("❌ Cache miss - querying LLM")

    response = llm_call.llm_call(prompt)
    cache[prompt] = response
    return response