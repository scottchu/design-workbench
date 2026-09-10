# Design Workbench

Role: product intent source. Status: accepted direction, 2026-09-08; delivery
status belongs in [PROJECT_STATE](../PROJECT_STATE.md).
Owns: why this product exists, how it helps, and what it delivers.

## Why

Help people and agents produce, inspect and revise designs from project-owned
specifications while preserving intent, consistency, evidence and approval.

A project determines the desired outcome: a CAD mechanism, a set of images, a
sticker pack, or a future design medium. Workbench supplies reusable ways to carry
that intent through iteration. Design choices discovered during the work remain
in the project that owns them.

## How

Use focused skills for independently useful tasks, workflow Markdown to compose
those tasks and their review gates, and executable tools to perform operations.
Select domain procedures from the project's purpose, requirements and evidence
needs. The [composition decision](decisions/0003-composable-skills.md) owns these
roles; the [architecture](architecture.md) owns implementation boundaries.

CAD and image work share the need to identify inputs, preserve agreed invariants,
review candidates and record acceptance. Their checks remain domain-specific:
geometry and written exports require different evidence from visual identity,
style or exact lettering. Shared principles do not make these validators
interchangeable.

The Playground provides interactive inspection of explicitly registered,
project-built pages. Projects own their page logic, models and parameter rules;
Workbench owns the reusable host and its lifecycle. External generation and
printer providers keep their own services and execution responsibilities.

## What

Design Workbench is an installable design workflow plugin that helps agents produce,
inspect and iterate CAD, images and future design outcomes from project
specifications, with a Playground for interactive review.

The plugin is the delivery entry point. It supplies skills, workflow guidance,
shared contracts and the supporting software needed for its declared
capabilities. The Playground is a runtime component of that experience. A future
Workbench MCP will expose bounded operations over owned tools; it is planned,
not implemented today.

Workbench's product outputs are versioned plugin packages and supporting software
builds. A consumer project's outputs are its actual designs, images, exports and
release artifacts. Those outputs, their requirements and their approvals remain
in the consumer project.

## Acceptance expectations

- A declared release identifies its packaged capabilities, required providers,
  runtime prerequisites and source/build identities.
- A task uses identified project inputs and returns an actual outcome, relevant
  evidence and unresolved prerequisites without depending on remembered chat.
- Changes preserve approved invariants or make the affected acceptance explicit;
  successful software checks do not establish design or physical acceptance.
- Package validation, installed-skill invocation and running-system validation
  are separate claims. A release reports which were demonstrated.

The current package includes skill and Playground sources; installation does not
automatically prepare, build or start the runtime. The exact mechanism for a more
self-contained runtime release remains open. See [packaging](../packaging/README.md)
for what is actually assembled and [the roadmap](roadmap.md) for pending work.

## Source sufficiency target

Versioned document source and explicit target parameters should be sufficient
to reconstruct the declared
product outputs. Consequential behavior must not exist only in implementation,
tests or remembered conversations. Required dependencies and external inputs must
be declared; private runtime state is not something product documents can invent.

Interpretation may produce an AST, ontology and typed composition graph before
generation. These are derived views that must preserve source meaning and expose
gaps; their presence alone does not establish a compiler or fill in missing
requirements. [Current verification](verification.md) supports sampled behavior compatibility
for one reconstructed module. Reproducible, byte-identical full
product compilation remains an unimplemented target, with generation and
verification mechanisms still to be established. Existing code remains maintained
source until replacement is supported by explicit evidence.
