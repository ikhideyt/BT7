import json
import os

from decouple import config

# todo: if scope_files is: 500 > 50, 300 > 30 , 100 > 10
MAX_REPO = 20
# todo: the path from https:///github.com/dfinity/ICRC-1
SOURCE_REPO = "scallop-io/sui-lending-protocol"
# todo: the name of the repository
REPO_NAME = "sui-lending-protocol"
run_number = os.environ.get('GITHUB_RUN_NUMBER') or os.environ.get('CI_PIPELINE_IID', '0')


def get_cyclic_index(run_number, max_index=100):
    """Convert run number to a cyclic index between 1 and max_index"""
    return (int(run_number) - 1) % max_index + 1


def load_repository_urls():
    """Load repository URLs from repositories.json."""
    repo_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "repositories.json")
    if not os.path.exists(repo_file):
        return []

    try:
        with open(repo_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except (json.JSONDecodeError, OSError):
        return []

    if not isinstance(data, list):
        return []

    return [url for url in data if isinstance(url, str) and url.strip()]


if run_number == "0":
    BASE_URL = f"https://deepwiki.com/{SOURCE_REPO}"
else:
    repository_urls = load_repository_urls()
    if repository_urls:
        run_index = get_cyclic_index(run_number, len(repository_urls))
        BASE_URL = repository_urls[run_index - 1]
    else:
        BASE_URL = f"https://deepwiki.com/{SOURCE_REPO}"

scope_files = [
    'contracts/libs/coin_decimals_registry/sources/coin_decimals_registry.move',
    'contracts/libs/decimal/sources/decimal.move',
    'contracts/libs/math/sources/fixed_point32.move',
    'contracts/libs/math/sources/u128.move',
    'contracts/libs/math/sources/u256.move',
    'contracts/libs/math/sources/u64.move',
    'contracts/libs/whitelist/sources/whitelist.move',
    'contracts/libs/x/sources/ac_table.move',
    'contracts/libs/x/sources/balance_bag.move',
    'contracts/libs/x/sources/one_time_lock_value.move',
    'contracts/libs/x/sources/ownership.move',
    'contracts/libs/x/sources/supply_bag.move',
    'contracts/libs/x/sources/wit_table.move',
    'contracts/libs/x/sources/witness.move',
    'contracts/protocol/sources/app/app.move',
    'contracts/protocol/sources/error/error.move',
    'contracts/protocol/sources/evaluator/borrow_withdraw_evaluator.move',
    'contracts/protocol/sources/evaluator/collateral_value.move',
    'contracts/protocol/sources/evaluator/debt_value.move',
    'contracts/protocol/sources/evaluator/liquidation_evaluator.move',
    'contracts/protocol/sources/evaluator/price.move',
    'contracts/protocol/sources/evaluator/value_calculator.move',
    'contracts/protocol/sources/market/apm.move',
    'contracts/protocol/sources/market/asset_active_state.move',
    'contracts/protocol/sources/market/borrow_dynamics.move',
    'contracts/protocol/sources/market/collateral_stats.move',
    'contracts/protocol/sources/market/incentive_rewards.move',
    'contracts/protocol/sources/market/interest_model.move',
    'contracts/protocol/sources/market/limiter.move',
    'contracts/protocol/sources/market/market.move',
    'contracts/protocol/sources/market/market_dynamic_keys.move',
    'contracts/protocol/sources/market/reserve.move',
    'contracts/protocol/sources/market/risk_model.move',
    'contracts/protocol/sources/obligation/obligation.move',
    'contracts/protocol/sources/obligation/obligation_access.move',
    'contracts/protocol/sources/obligation/obligation_collaterals.move',
    'contracts/protocol/sources/obligation/obligation_debts.move',
    'contracts/protocol/sources/obligation/obligation_key_display.move',
    'contracts/protocol/sources/referral/borrow_referral.move',
    'contracts/protocol/sources/user/accrue_interest.move',
    'contracts/protocol/sources/user/borrow.move',
    'contracts/protocol/sources/user/deposit_collateral.move',
    'contracts/protocol/sources/user/flash_loan.move',
    'contracts/protocol/sources/user/liquidate.move',
    'contracts/protocol/sources/user/lock_obligation.move',
    'contracts/protocol/sources/user/mint.move',
    'contracts/protocol/sources/user/open_obligation.move',
    'contracts/protocol/sources/user/redeem.move',
    'contracts/protocol/sources/user/repay.move',
    'contracts/protocol/sources/user/withdraw_collateral.move',
    'contracts/protocol/sources/version/current_version.move',
    'contracts/protocol/sources/version/version.move',
    'contracts/protocol_whitelist/sources/protocol_whitelist.move',
    'contracts/query/sources/market_query.move',
    'contracts/query/sources/obligation_query.move',
    'contracts/sui_x_oracle/custom_afsui_rule/sources/oracle_config.move',
    'contracts/sui_x_oracle/custom_afsui_rule/sources/pyth_adaptor.move',
    'contracts/sui_x_oracle/custom_afsui_rule/sources/rule.move',
    'contracts/sui_x_oracle/custom_hasui_rule/sources/oracle_config.move',
    'contracts/sui_x_oracle/custom_hasui_rule/sources/pyth_adaptor.move',
    'contracts/sui_x_oracle/custom_hasui_rule/sources/rule.move',
    'contracts/sui_x_oracle/pyth_rule/sources/pyth_adaptor.move',
    'contracts/sui_x_oracle/pyth_rule/sources/pyth_registry.move',
    'contracts/sui_x_oracle/pyth_rule/sources/rule.move',
    'contracts/sui_x_oracle/supra_rule/sources/rule.move',
    'contracts/sui_x_oracle/supra_rule/sources/supra_adaptor.move',
    'contracts/sui_x_oracle/supra_rule/sources/supra_registry.move',
    'contracts/sui_x_oracle/switchboard_on_demand_rule/sources/rule.move',
    'contracts/sui_x_oracle/switchboard_on_demand_rule/sources/switchboard_adaptor.move',
    'contracts/sui_x_oracle/switchboard_on_demand_rule/sources/switchboard_registry.move',
    'contracts/sui_x_oracle/switchboard_rule/sources/rule.move',
    'contracts/sui_x_oracle/switchboard_rule/sources/switchboard_adaptor.move',
    'contracts/sui_x_oracle/switchboard_rule/sources/switchboard_registry.move',
    'contracts/sui_x_oracle/x_oracle/sources/price_feed.move',
    'contracts/sui_x_oracle/x_oracle/sources/price_update_policy.move',
    'contracts/sui_x_oracle/x_oracle/sources/x_oracle.move',
]

target_scopes = [
    'Critical. Direct theft or loss of user funds, collateral, borrowed assets, supplied liquidity, redeemed assets, liquidated collateral, or flash-loaned funds at rest or in motion, excluding unclaimed yield',
    'Critical. Unauthorized capability, access-control, role, version, whitelist, oracle, market, reserve, limiter, or obligation-state manipulation that causes major protocol damage',
    'High. Theft of unclaimed yield, incentive rewards, reserve revenue, Scallop Treasury funds, or protocol-held fees',
    'Medium. Fee payment bypass, borrow-fee bypass, flash-loan-fee bypass, block stuffing for profit, or bounded value extraction through accounting or rate manipulation',
    'Low. Griefing that causes concrete damage to users or the protocol without relying on public DoS, DDoS, spam, or a profit motive',
]


def question_generator(target_file: str) -> str:
    """
    Generate exploit-focused audit and fuzzing questions for one Scallop Sui Lending Protocol target.

    target_file format:
    "'File Name: contracts/protocol/sources/user/borrow.move -> Scope: Critical. Direct theft or loss of user funds, collateral, borrowed assets, supplied liquidity, redeemed assets, liquidated collateral, or flash-loaned funds at rest or in motion, excluding unclaimed yield'"
    """

    prompt = f"""
    ```

    Generate exploit-focused security audit and fuzzing questions for this exact Scallop Sui Lending Protocol target:

    {target_file}

    Use live context from the project if available: Scallop Sui lending core protocol, Market, reserves, sCoins, obligations, obligation keys, collateral and debt accounting, mint/redeem, borrow/repay, withdraw/deposit collateral, liquidation, flash loans, interest accrual, risk models, interest models, asset active states, APM, supply and borrow limits, outflow limiters, incentive rewards, borrow referrals, version checks, whitelists, coin decimals registry, xOracle price feeds, Pyth/Supra/Switchboard oracle rules, custom afSUI/haSUI oracle rules, query modules, and local math/decimal/container libraries.

    Protocol focus:
    Scallop is a Sui Move lending protocol. Users supply assets to receive sCoins, redeem sCoins for underlying assets, open obligations, deposit collateral, borrow assets, repay debt, withdraw collateral when healthy, and liquidate undercollateralized obligations. The market stores reserves, interest/risk models, fees, limits, rewards, and asset configuration. xOracle aggregates supported price sources. The audit target is production smart contract code in this repository only.

    Core invariants:

    * User, reserve, collateral, borrowed, liquidated, flash-loaned, treasury, fee, and reward funds must never be stolen, lost, over-withdrawn, over-borrowed, under-repaid, over-redeemed, misdirected, double-counted, or permanently trapped by an unprivileged attacker.
    * Only authorized owners, obligation-key holders, protocol capabilities, whitelisted callers, configured markets, valid versions, approved oracle rules, and intended package/module paths may perform privileged or state-changing actions.
    * Reserve cash, sCoin supply, exchange rates, collateral balances, debt principal, borrow indexes, interest accrual, liquidation discounts, close factors, fees, rewards, decimals, price values, limits, and treasury accounting must remain internally consistent across all supported user flows.
    * Oracle price reads, decimal normalization, asset type matching, market dynamic fields, obligation access checks, hot-potato flows, lock keys, whitelist gates, and version gates must not be bypassable, spoofable, stale in a dangerous way, or usable for the wrong asset or market.
    * Liquidation, flash loan, mint/redeem, borrow/repay, collateral withdrawal, incentive reward, referral, revenue, and administrative capability flows must be atomic and must not leave partial state that benefits an attacker.

    Rules:

    * Treat `File Name:` as the exact file/module.
    * Treat `Scope:` as the ONLY impact to target.
    * Assume full repo context is accessible.
    * Do not ask for code or say anything is missing.
    * Attacker may be an unprivileged Sui account, supplier, borrower, collateral depositor, obligation owner, obligation-key holder, liquidator, flash-loan borrower, integrator contract, public entry caller, reward/referral participant, or creator of price/update inputs accepted by in-scope oracle modules.
    * Do not rely on admin/operator/governance/strategist compromise; leaked keys or credentials; privileged-address access; malicious maintainer; social engineering; public-mainnet or public-testnet testing; oracle-provider compromise outside this repo; third-party contract bugs; frontend/browser/website bugs; centralization risk; lack of liquidity; sybil attacks; front-running-only attacks; spam; brute-force DDoS; or breaking the law.
    * Exclude denial of service, public DoS/DDoS, automated traffic abuse, block stuffing without profit, griefing without concrete protocol/user damage, dependency-only issues, imported-contract issues, static-analysis-only findings, gas optimizations, code style, redundant code, best-practice findings, known issues, and purely theoretical issues without a proof or demonstration.
    * Exclude test-only code paths, mocks, examples, docs, configs, generated files, local scripts, package metadata, repo automation, deployment-only choices, and non-default feature-only paths.
    * Generate 10 to 20 high-signal questions.
    * At least 70% must be multi-step flow, invariant, authorization, accounting, oracle, decimal-normalization, type-binding, obligation-access, interest-accrual, liquidation, flash-loan, reward, fee, limit, or cross-module questions.
    * Every question must be testable by a runnable local unit test, Move test, fuzz test, invariant test, model test, differential test, or private-testnet transaction sequence. Do not require public mainnet or public testnet testing.
    * Avoid generic checklist questions and repeated root causes; prefer boundary mutations such as wrong asset type, stale or mismatched price, wrong decimal, reused obligation key, locked obligation edge case, partial state update, duplicate reward claim, incorrect exchange rate, manipulated borrow index, bypassed limit, or failed flash-loan repayment.
    * Each question must target a plausible issue class for the exact file and scope.

    High-value attack surfaces:

    * User flows: `mint`, `redeem`, `open_obligation`, `return_obligation`, `deposit_collateral`, `withdraw_collateral`, `borrow`, `repay`, `liquidate`, `flash_loan`, `accrue_interest`, and `lock_obligation`.
    * Market and reserve flows: reserve creation and lookup, dynamic keys, supply/borrow limits, outflow limiters, APM thresholds, asset active states, risk models, interest models, borrow dynamics, collateral stats, revenue, treasury, fees, and incentive rewards.
    * Obligation flows: obligation-key authorization, hot-potato consumption, locked obligations, collateral/debt add/remove, debt index updates, health calculation, liquidation eligibility, and owner/key binding.
    * Oracle and decimal flows: xOracle price feed selection, price update policies, Pyth/Supra/Switchboard adaptors, custom afSUI/haSUI rules, stale price checks, feed identifier binding, decimal registry entries, decimal math, and asset type matching.
    * Capability and whitelist flows: app initialization, protocol whitelist, generic whitelist libraries, witness/access tables, ownership helpers, one-time lock values, version enforcement, and privileged package capabilities.
    * Accounting consistency: sCoin exchange rates, underlying reserve cash, debt value, collateral value, liquidation repay/withdraw amounts, flash-loan principal plus fee, borrow fees, referral rewards, incentive reward factors, and treasury transfers.

    Impact mapping:

    * Critical: direct theft/loss/freezing of user or protocol funds, or unauthorized capability/access-control manipulation that causes major protocol damage.
    * High: theft of unclaimed yield, incentive rewards, reserve revenue, treasury assets, or protocol-held fees.
    * Medium: fee bypass, block stuffing for profit, or bounded accounting/rate manipulation with extractable value.
    * Low: concrete griefing damage to users or protocol, excluding public DoS/DDoS, spam, and purely theoretical disruption.

    Each question must include:

    1. target function/module;
    2. attacker action;
    3. preconditions;
    4. call sequence;
    5. invariant tested;
    6. scoped impact;
    7. proof idea.

    Output only valid Python. No markdown. No explanations.

    questions = [
    "[File: {target_file}] [Function: symbol_or_module] Can an attacker ACTION under PRECONDITIONS trigger CALL_SEQUENCE, violating INVARIANT, causing scoped impact: SCOPE_IMPACT? Proof idea: fuzz/state-test PARAMETERS and assert EXPECTED_PROPERTY.",
    ]
    """
    return prompt


def audit_format(question: str) -> str:
    """
    Generate a focused Scallop Sui Lending Protocol exploit-question validation prompt.
    """
    return f"""# QUESTION SCAN PROMPT

## Exploit Question
{question}

## Scope Rules
- Audit only production Scallop Sui Lending Protocol smart-contract code listed in `scope_files`.
- Do not ask for repo contents or claim files are missing.
- Ignore tests, docs, mocks, generated files, repo automation scripts, configs, build files, IDE files, package metadata, local deployment choices, examples, local tooling, vendors, and imported contracts.
- Respect the HackenProof Scallop program rules. Do not perform mainnet or public-testnet testing; prefer local tests or private testnets.

## Objective
Decide whether the question leads to a real, reachable Scallop Sui Lending Protocol vulnerability.
The attacker must enter through a supported production path: public Move call, user mint/redeem flow, obligation open/lock/access flow, collateral deposit/withdrawal, borrow/repay, liquidation, flash loan, interest accrual, reward/referral flow, market query, whitelisted integration path, accepted oracle update/read path, or a supported local/private-testnet reproduction of those paths.
The impact must match the provided target scope.
Prefer #NoVulnerability unless the path is concrete, locally testable on unmodified code, and proves one of the impacts in `target_scopes`.

## Method
1. Trace the attacker-controlled entrypoint.
2. Map it to exact production files/functions across protocol, oracle, query, whitelist, and local library modules.
3. Check relevant guards: version checks, capability checks, whitelist checks, obligation-key checks, hot-potato consumption, lock checks, asset active states, supply/borrow limits, outflow limiters, APM thresholds, oracle price freshness, feed/asset binding, decimal normalization, type matching, interest accrual, liquidation thresholds, flash-loan repayment, fee accounting, reward accounting, reserve cash, sCoin supply, debt index updates, treasury accounting, and dynamic-field ownership.
4. Decide whether the questioned invariant can actually break under intended deployment.
5. Prove root cause with file/function/line references.
6. Confirm realistic likelihood and exact scoped impact.
7. Reject if current validation already prevents the exploit.

## Reject Immediately
- Requires admin/operator/governance/strategist compromise, leaked keys or credentials, malicious maintainer, social engineering, privileged-address access, public-mainnet or public-testnet testing, oracle-provider compromise outside this repo, third-party contract bugs, frontend/browser/website bugs, centralization risk, lack of liquidity, sybil assumptions, front-running-only attacks, spam, brute-force DDoS, or breaking the law.
- Only affects tests, docs, configs, scripts, mocks, generated code, local tooling, deployment choices, vendors, imported contracts, or non-default feature-only paths.
- External dependency behavior is the only cause.
- Impact is public DoS/DDoS, unbounded gas/storage consumption, network outage, automated traffic abuse, performance degradation, block stuffing without profit, local misconfiguration, observability noise, logging noise, harmless rejection, stale read with no security impact, code style, redundant code, gas optimization, best practice, or non-security correctness.
- No concrete scoped impact or no realistic exploit path.

## Allowed Impact Scope
Only these impacts are valid:
- Critical. Direct theft or loss of user funds, collateral, borrowed assets, supplied liquidity, redeemed assets, liquidated collateral, or flash-loaned funds at rest or in motion, excluding unclaimed yield.
- Critical. Unauthorized capability, access-control, role, version, whitelist, oracle, market, reserve, limiter, or obligation-state manipulation that causes major protocol damage.
- High. Theft of unclaimed yield, incentive rewards, reserve revenue, Scallop Treasury funds, or protocol-held fees.
- Medium. Fee payment bypass, borrow-fee bypass, flash-loan-fee bypass, block stuffing for profit, or bounded value extraction through accounting or rate manipulation.
- Low. Griefing that causes concrete damage to users or the protocol without relying on public DoS, DDoS, spam, or a profit motive.

## Output
If valid:

### Title
[Clear vulnerability statement] - ([File: file_path])

### Summary
### Finding Description
### Impact Explanation
### Likelihood Explanation
### Recommendation
### Proof of Concept

If invalid, output exactly:
#NoVulnerability found for this question.
"""


def scan_format(report: str) -> str:
    """
    Generate a short cross-project analog scan prompt for Scallop Sui Lending Protocol.
    """
    prompt = f"""# ANALOG SCAN PROMPT

## External Report
{report}

## Access Rules (Strict)
- Treat production Scallop Sui Lending Protocol files in the provided scope as accessible context.
- Do not claim missing/inaccessible files.
- Do not ask for repository contents.
- Do not scan tests, docs, build files, IDE files, configs, generated files, resources, package metadata, repo automation scripts, local tooling, deployment-only choices, vendors, imported contracts, or non-default feature-only paths as audited targets.

## Objective
Use the external report's vulnerability class as a hint to find valid issues based on Scallop Sui Lending Protocol security impact.
Focus on externally reachable issues triggered by an unprivileged Sui account, supplier, borrower, obligation owner/key holder, collateral depositor, liquidator, flash-loan borrower, reward/referral participant, integrator contract, public entry caller, or creator of accepted oracle inputs.
Only report an analog if this repository has its own reachable root cause and the impact matches the provided target scope.

## Method
1. Classify vuln type: direct fund theft/loss, unauthorized capability/action, obligation access bypass, market manipulation, reserve accounting bug, sCoin exchange-rate manipulation, collateral/debt accounting error, liquidation mispricing, interest accrual/index error, flash-loan repayment or fee bypass, treasury/reward/yield theft, oracle price/feed binding flaw, decimal normalization flaw, whitelist/version bypass, limit bypass, or concrete griefing damage.
2. Map to Scallop Sui Lending components and exact production files.
3. Prove root cause with exact file/function/module/line references.
4. Confirm concrete scoped impact and realistic likelihood.
5. Explain the attacker-controlled entry path and why this code is a necessary vulnerable step.
6. Reject if the impact does not match the provided target scope.

## Disqualify Immediately
- No reachable attacker-controlled entry path.
- Requires admin/operator/governance/strategist compromise, leaked keys or credentials, malicious maintainer, social engineering, privileged-address access, public-mainnet or public-testnet testing, oracle-provider compromise outside this repo, third-party contract bugs, frontend/browser/website bugs, centralization risk, lack of liquidity, sybil assumptions, front-running-only attacks, spam, brute-force DDoS, or breaking the law.
- External dependency behavior is the only cause.
- Test/docs/config/build/generated/local-tooling/deployment-only/vendor/imported-contract/non-default-feature issue.
- Theoretical-only issue with no protocol impact.
- Impact is public DoS/DDoS, unbounded gas/storage consumption, network outage, automated traffic abuse, performance degradation, block stuffing without profit, local misconfiguration, observability noise, logging noise, harmless rejection, stale read with no security impact, code style, redundant code, gas optimization, best practice, or non-security correctness.
- Impact or likelihood missing.

## Allowed Impact Scope
Only these impacts are valid:
- Critical. Direct theft or loss of user funds, collateral, borrowed assets, supplied liquidity, redeemed assets, liquidated collateral, or flash-loaned funds at rest or in motion, excluding unclaimed yield.
- Critical. Unauthorized capability, access-control, role, version, whitelist, oracle, market, reserve, limiter, or obligation-state manipulation that causes major protocol damage.
- High. Theft of unclaimed yield, incentive rewards, reserve revenue, Scallop Treasury funds, or protocol-held fees.
- Medium. Fee payment bypass, borrow-fee bypass, flash-loan-fee bypass, block stuffing for profit, or bounded value extraction through accounting or rate manipulation.
- Low. Griefing that causes concrete damage to users or the protocol without relying on public DoS, DDoS, spam, or a profit motive.


## Output (Strict)
If valid analog exists, output:

### Title
[Clear vulnerability statement] - ([File: file_path])

### Summary
### Finding Description
### Impact Explanation
### Likelihood Explanation
### Recommendation
### Proof of Concept

If not, output exactly:
#NoVulnerability found for this question.

No extra text.
"""
    return prompt


def validation_format(report: str) -> str:
    """
    Generate a strict Scallop Sui Lending Protocol validation prompt for security claims.
    """
    prompt = f"""# VALIDATION PROMPT

## Security Claim
{report}

## Rules
- Validate only the submitted claim.
- Check the HackenProof Scallop program rules for scope, exclusions, known issues, and valid impact classes.
- Do not create a new vulnerability if the submitted claim is weak or invalid.
- Do not upgrade severity unless the provided evidence proves the higher impact.
- Reject admin-only, operator-only, governance-only, strategist-only, trusted-maintainer, leaked-key, best-practice, docs/style, redundant-code, gas-only, public-DoS/DDoS, unbounded gas/storage, performance-only, front-running-only, static-analysis-only, dependency-only, imported-contract, lack-of-liquidity, sybil, centralization-risk, and purely theoretical issues.
- Reject if the exploit requires unrealistic assumptions, victim mistakes, missing external context, unsupported protocol behavior, oracle-provider compromise outside this repo, third-party contract bugs, frontend/browser/website bugs, privileged-address access, public-mainnet or public-testnet testing, social engineering, spam, or breaking the law.
- A valid report must be triggerable by an unprivileged external user through public Move calls, mint/redeem, obligation access, collateral deposit/withdrawal, borrow/repay, liquidation, flash loan, interest accrual, reward/referral, market query, whitelisted integration path, accepted oracle update/read path, or a private-testnet reproduction of those paths.
- The final impact must match one of the `target_scopes`, not just a generic code bug.
- Prefer #NoVulnerability over speculative reports.

## Allowed Impact Scope
Only these impacts are valid:
- Critical. Direct theft or loss of user funds, collateral, borrowed assets, supplied liquidity, redeemed assets, liquidated collateral, or flash-loaned funds at rest or in motion, excluding unclaimed yield.
- Critical. Unauthorized capability, access-control, role, version, whitelist, oracle, market, reserve, limiter, or obligation-state manipulation that causes major protocol damage.
- High. Theft of unclaimed yield, incentive rewards, reserve revenue, Scallop Treasury funds, or protocol-held fees.
- Medium. Fee payment bypass, borrow-fee bypass, flash-loan-fee bypass, block stuffing for profit, or bounded value extraction through accounting or rate manipulation.
- Low. Griefing that causes concrete damage to users or the protocol without relying on public DoS, DDoS, spam, or a profit motive.

If the submitted claim does not concretely prove one of the allowed impacts above, it is invalid.

## Required Validation Checks
All must pass:
1. Exact in-scope file, function, and line/code references.
2. Clear root cause and broken lending/security/accounting/oracle assumption.
3. Reachable exploit path: preconditions -> attacker action -> trigger -> bad result.
4. Existing checks/guards reviewed and shown insufficient.
5. Concrete impact that exactly matches one allowed Scallop Sui Lending Protocol impact above, with realistic likelihood.
6. Reproducible proof path: local Move/unit/integration/fuzz/invariant test, private-testnet transaction sequence, contract call sequence, or justified model/differential test when localnet cannot demonstrate the impact.
7. No obvious rejection reason from HackenProof rules, known issues, privileges, imported contracts, or scope exclusions.

## Silent Triage Questions
Before output, internally answer:
- Can a normal supplier, borrower, obligation owner/key holder, collateral depositor, liquidator, flash-loan borrower, reward/referral participant, integrator contract, public caller, or accepted oracle-input creator trigger this?
- Does the code actually behave as claimed?
- Is the impact caused by this repository, not by an external dependency or imported contract alone?
- Is the fund/authorization/accounting/oracle/griefing impact concrete, not hypothetical?
- Would a responsible-disclosure triager accept the proof?
- What exact test would prove it?

## Output
If valid, output exactly:

Audit Report

## Title
[Clear vulnerability statement] - ([File: file_path])

## Summary
[2-3 sentence summary of the bug and impact]

## Finding Description
[Exact code path, root cause, exploit flow, and why existing checks fail]

## Impact Explanation
[Concrete allowed Scallop Sui Lending Protocol impact and severity rationale]

## Likelihood Explanation
[Attacker capability, required conditions, feasibility, repeatability]

## Recommendation
[Specific fix guidance]

## Proof of Concept
[Minimal reproducible steps or fuzz/invariant/model/private-testnet test plan]

If invalid, output exactly:
#NoVulnerability found for this question.

Output only one of the two outcomes above. No extra text.
"""
    return prompt

