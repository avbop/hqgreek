TESTDIR=tests
DOCDIR=docs

all: doc

test:
	cd $(TESTDIR) && py.test

doc:
	sphinx-apidoc -o $(DOCDIR)/api hqgreek
	sphinx-apidoc -o $(DOCDIR)/api hqvocab
	cd $(DOCDIR) && make html

.PHONY: all, test, doc
