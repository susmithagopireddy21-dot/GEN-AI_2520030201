
from budget import FeatureBudget

budget = FeatureBudget.from_env()

scenarios = [
    ("Original usage", {}),
    ("Double requests per day", {
        "requests_per_day": budget.requests_per_day * 2
    }),
    ("Double input tokens", {
        "avg_input_tokens": budget.avg_input_tokens * 2
    }),
    ("Reduce output tokens by half", {
        "avg_output_tokens": budget.avg_output_tokens // 2
    }),
]

print("\nWHAT-IF ANALYSIS")
print("-" * 50)

for name, changes in scenarios:
    values = budget.__dict__.copy()
    values.update(changes)

    scenario_budget = FeatureBudget(**values)
    result = scenario_budget.calculate()

    print(f"\nScenario: {name}")
    print(f"Daily cost: ${result['daily_cost_usd']:.2f}")
    print(f"Monthly cost: ${result['monthly_cost_usd']:.2f}")
    print(f"Daily budget: {'PASS' if result['daily_budget_ok'] else 'REVIEW'}")
    print(f"Monthly budget: {'PASS' if result['monthly_budget_ok'] else 'REVIEW'}")
