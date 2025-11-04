1) Which issues were easiest/hardest to fix and why?

The easiest issues to fix were naming style violations and missing blank lines because they involved straightforward renaming of functions to snake_case and adding extra blank lines as per PEP 8. Removing unused imports was also simple. The hardest were logical issues like mutable default arguments and broad except clauses, as these required deeper understanding and careful refactoring to avoid bugs without changing intended behavior.

2) Did you encounter false positives? Provide an example.

Yes, static analysis tools sometimes report false positives. For example, Pylint can incorrectly flag unused imports or variables that are actually used dynamically or in ways it can't analyze reliably, especially with complex code or meta-programming. Another common false positive is the no-member error when analyzing C extensions or dynamically added attributes, which Pylint cannot reliably detect.

3) How would you integrate static analysis tools into your actual software development workflow? (e.g., CI integration, pre-commit hooks)
Run Flake8 and Bandit locally during development or as pre-commit hooks to catch style and security issues early. Integrate Pylint and Bandit checks in continuous integration (CI) pipelines to enforce quality gates automatically and prevent problematic code merges. Use configuration files to customize rules and suppress known false positives, balancing strictness with practicality.

4) What tangible improvements did you observe in the code quality, readability, or potential robustness after applying the fixes?
Fixes improved code quality by enforcing consistent naming and style standards, which enhances readability and maintainability. Replacing mutable defaults and broad excepts reduced potential bugs and improved robustness. Removing eval and addressing Bandit security warnings strengthened code security. Overall, the code is cleaner, safer, and more Pythonic, making future maintenance easier.