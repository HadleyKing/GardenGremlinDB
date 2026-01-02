
From a JSON Schema, you can deterministically generate:

Django model

DRF serializer

ViewSet skeleton

Router registration

Migration file

OpenAPI/Swagger visibility

Admin registration (optional)

These are mechanical translations. No judgment required.

Spreadsheet
   → schema_maker.py
       → JSON Schema (authoritative)
           → schema2model.py
               → Django ORM
                   → DRF
                       → Swagger

utilities/
├── schema_maker.py      # TSV → JSON Schema
├── schema2model.py      # JSON Schema → models.py
└── (future) model2api.py
