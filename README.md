# SharedPythonUtilities

Reusable Python functions shared by the sports-data repositories.

## Current functions

- `clean_player_name(name)`: applies the player-name standardization rules
  converted from the Excel LAMBDA.

## Import

After installing this repository as a Python dependency:

```python
from shared_python_utilities import clean_player_name

df["Player Name"] = df["Player Name"].map(clean_player_name)
```

Missing values are preserved. Non-missing values passed to
`clean_player_name` must be strings.

## Install from GitHub

For a repository with access to this private GitHub repository:

```text
git+https://github.com/evilwebboy/SharedPythonUtilities.git
```

Private-repository authentication must be configured in the environment
that installs the package (for example, GitHub Actions).
