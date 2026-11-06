# SharedPythonUtilities

Reusable Python functions shared by the sports-data repositories.

## Available lookup dictionaries

- `PLAYER_EXCEPTIONS_CFB`: maps raw college football player names to their standardized clean names.
- `PLAYER_EXCEPTIONS_MLB`: maps raw Major League Baseball player names to their standardized clean names.
- `PLAYER_EXCEPTIONS_NBA`: maps raw National Basketball Association player names to their standardized clean names.
- `PLAYER_EXCEPTIONS_NFL`: maps raw National Football League player names to their standardized clean names.
- `PLAYER_EXCEPTIONS_NHL`: maps raw National Hockey League player names to their standardized clean names.

- `TEAM_NAMES_CFB`: maps college football team abbreviations and aliases to canonical team names.

## Current functions

- `clean_player_name(name)`: applies the player-name standardization rules
  converted from the Excel LAMBDA.

## Import

After installing this repository as a Python dependency:

```python
from shared_python_utilities import (
    clean_player_name,
    PLAYER_EXCEPTIONS_CFB,
    PLAYER_EXCEPTIONS_MLB,
    PLAYER_EXCEPTIONS_NBA,
    PLAYER_EXCEPTIONS_NFL,
    PLAYER_EXCEPTIONS_NHL,
    TEAM_NAMES_CFB,
)

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
