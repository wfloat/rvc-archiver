import subprocess
import sys

def run_command(command):
    """Run a shell command and exit if it fails."""
    result = subprocess.run(command, shell=True)
    if result.returncode != 0:
        sys.exit(1)

run_command('''sgqlc-codegen \
    schema \
    --docstrings ../api/src/codegen/generated/schema.json \
    src/graphql/generated/schema.py \
''')

run_command('''sgqlc-codegen \
    operation \
    --schema ../api/src/codegen/generated/schema.json \
    src.graphql.generated.schema \
    src/graphql/generated/operations.py \
    src/graphql/operations.gql \
''')
