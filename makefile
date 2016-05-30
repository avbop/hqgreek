TESTDIR=tests
DOCDIR=docs

all: doc

test:
	cd $(TESTDIR) && py.test

doc:
	echo blah > $(DOCDIR)/index

.PHONY: all, test, doc
