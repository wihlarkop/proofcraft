# Application Data Modeling

Start from business invariants and ownership.

For each material entity/value, clarify:
- stable identity;
- authoritative owner;
- required vs optional fields;
- cardinality;
- uniqueness;
- lifecycle/deletion semantics;
- references and cascade behavior;
- immutable vs mutable properties.

Prefer database constraints for invariants the database can reliably enforce. Do not mirror an API payload or UI form directly into a persistence model without considering domain ownership.
