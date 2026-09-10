# Reconstruction capability and evidence

Role: current verification knowledge, not product intent.

## Demonstrated scope

The [request-admission specification](source/playground-access.md) supported one
fresh-agent reconstruction of the Playground's private-origin validation and
Host/Origin admission behavior. Production still uses its original module.

The specification was completed from existing implementation evidence and frozen
before generation. The builder reported reading only that product input, then
its own outputs. It produced an AST, ontology and typed composition view before
the candidate. Access restrictions were procedural on a shared filesystem, not
enforced isolation. There was one source version and one candidate, with no
post-test candidate repair.

Independent expected-value checks and comparison against the original passed:
106 tests, including 5,148 sampled request outcomes. Of those outcomes, 936 use
valid or empty configuration; the remainder repeat configuration-error outcomes
across headers. Counts do not represent distinct semantic paths. Independent
review found no blocking mismatch within string configuration and standard
request-header inputs.

The [technical receipt](../evidence/reconstruction/access/RECEIPT.json) identifies
source, generated outputs, acceptance inputs and execution results. The
[independent review](../evidence/reconstruction/access/REVIEW.md) preserves its
exact acceptance scope. [Experimental fixtures](../fixtures/reconstruction/access/README.md)
provide the candidate, model and executable verification entry point.

## What the result teaches

General product prose was insufficient: reconstruction required exact defaults,
return behavior, failure distinctions, evaluation order, matching rules and input
normalization boundaries. These are now captured in the owning specification.
Captured compatibility behavior is not automatically a policy requirement for
all future products or implementations.

The AST makes declarations inspectable; the ontology separates configuration from
network reachability and errors from rejection; composition exposes ordering and
early termination. These are agent-authored interpretations. The experiment does
not establish that a generator mechanically consumes the model, that the views
improve generation over prose alone, or that category laws have been proved.

## Remaining limits

Evidence supports one sampled behavioral reconstruction, not exhaustive
equivalence, byte-identical generation or complete product reconstruction. A
versioned compiler and exact generation replay have not been established.
HTTP integration, live runtime behavior and inputs outside the declared domain
are not covered by this result.

Other declared product capabilities still need sufficient behavior and delivery
specifications, external input definitions and acceptance conditions. Existing
implementation and tests remain maintained until replacement has adequate
evidence. A future experiment should address a product gap and define what
"the same output" means before choosing a generation method.
