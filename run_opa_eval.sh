#!/bin/bash
echo "Running OPA policy checks..."
for policy in opa-policies/*.rego; do
    echo "--------------------------------------------------"
    echo "Checking policy: $policy"
    opa eval --input data/mock_app_config.json --data $policy "data"
done
