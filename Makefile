export WORKSPACE ?= $(abspath $(PWD)/)

datagather:
	touch datagather

# Build documentation
.PHONY: docs
docs:
	$(MAKE) -C docs html

# Run all tests
.PHONY: test
test:
	python3 -m pytest --rootdir=tests

# Clean up build artifacts
.PHONY: clean
clean:
	@rm -f datagather
	@rm -rf docs/_build
