.PHONY: start test compile-deps bump-min-ha

start:
	scripts/develop

test:
	pytest -q

compile-deps:
	pip install --quiet pip-tools
	pip-compile tests/requirements.in --output-file tests/requirements.txt --upgrade --strip-extras

# Bump the minimum required HA version across all three places that must stay
# in sync: hacs.json, and the lower bound in tests/requirements.in.
# Also regenerates tests/requirements.txt via compile-deps.
# Usage: make bump-min-ha VERSION=2025.3.0
bump-min-ha:
	@test -n "$(VERSION)" || (echo "Usage: make bump-min-ha VERSION=2025.3.0" && exit 1)
	sed -i.bak 's/"homeassistant": "[^"]*"/"homeassistant": "$(VERSION)"/' hacs.json \
		&& rm hacs.json.bak

	sed -i.bak 's/homeassistant>=[^ ]*/homeassistant>=$(VERSION)/' tests/requirements.in \
		&& rm tests/requirements.in.bak
	$(MAKE) compile-deps
	@echo "Minimum HA version set to $(VERSION)."
	@echo "Commit: hacs.json, tests/requirements.in, tests/requirements.txt"
