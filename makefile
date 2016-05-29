TESTDIR=tests

all: test

test:
	cd $(TESTDIR) && py.test

.PHONY: all, test
