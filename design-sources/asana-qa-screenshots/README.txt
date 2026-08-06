ARCHIVE MAPPING RULE

Each folder represents one QA page in Asana.

Files inside each folder are numbered according to the exact visible order
of subtasks under that page's QA task.

Example:

Home/1 ... = first Home QA subtask
Home/2 ... = second Home QA subtask
About/1 ... = first About QA subtask

Suffix meanings:

ChromeSafari / SafariChrome = desktop browser reference
mobile = mobile reference
(1), (2) = additional screenshot belonging to the same numbered subtask

Cloud Code must map each numbered file to the corresponding Asana subtask
already stored in ASANA_QA_LEDGER.md.

If one numbered subtask has multiple images, treat all of them as attachments
to the same correction.

Do not map by visual similarity alone.
Use:

1. Page folder
2. Numeric filename prefix
3. Existing Asana subtask order and GID
4. ASANA_QA_LEDGER.md

If any number is missing, duplicated or ambiguous, record it instead of guessing.