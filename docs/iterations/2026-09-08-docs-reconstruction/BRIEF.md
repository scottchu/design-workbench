# Docs-only reconstruction pilot

The user authorized one small experiment after identifying that the current docs
cannot reconstruct the product. This step follows the product-boundary work in
PR6 and does not depend on merging or deploying it first.

Capture one existing capability as sufficient document source: Playground Host
and Origin request admission. Freeze that document before a fresh, bounded agent
interprets it into AST, ontology and typed composition views and generates a
candidate. That agent receives only the specification, target/output locations
and procedural constraints; no original implementation, tests or chat history.
The shared filesystem is not an enforced isolation boundary, so retain the
agent's reported reads and describe this as procedural independence.

The primary agent may inspect the existing implementation to capture current
behavior and prepare independent acceptance and differential checks. Reconstructed
current behavior is explicitly scoped compatibility source, not automatically a
new design policy for all projects. A separate reviewer assesses specification,
derived models, generated candidate and evidence for omissions or overclaims.

Track generated models/code as designated generic reconstruction fixtures, not
production replacements. Keep test inputs and test harness separate from the
builder's source inputs. Record source/output hashes, tool/runtime identities,
actual checks, gaps and limitations. A typed composition diagram alone does not
prove category laws or a docs-to-product compiler. No runtime operation, package
installation, project asset migration or work in personal/compiler is included.
