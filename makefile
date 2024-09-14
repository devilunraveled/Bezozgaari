.PHONY: install

# Target to install a library and append it to requirements.txt
install:
	pip install $(lib) && echo $(lib) >> requirements.txt

# To handle library input from the command line
lib := $(word 2, $(MAKECMDGOALS))

# Prevent make from treating the command line arguments as targets
%:
	@:
