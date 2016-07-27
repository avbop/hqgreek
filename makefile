TESTDIR=tests
DOCDIR=docs
WEBDIR=web
JSONDIR=$(WEBDIR)/data
SPHINX_API=sphinx-apidoc --no-toc --force -o $(DOCDIR)/api
TMPDIR=/tmp/hqgreek
ISSUES_FILE=issues.html
GITHUB_REPO=avbop/hqgreek

all: test doc json site
travis: test doc json

test:
	cd $(TESTDIR) && py.test

doc:
	$(SPHINX_API) hqgreek
	$(SPHINX_API) hqvocab
	cd $(DOCDIR) && make html
	cp -r $(DOCDIR)/_build/html $(WEBDIR)/docs

json:
	mkdir -p $(JSONDIR)
	python3 generate_website_data.py $(JSONDIR)

$(WEBDIR)/favicon.png: $(WEBDIR)/favicon.svg
	inkscape -D -e $@ -w 16 -h 16 $<

sitedata: doc json $(WEBDIR)/favicon.png

site: test sitedata
	# Make sure we're on the master branch.
	git branch --no-color | grep "* master"
	mkdir $(TMPDIR)
	cd $(TMPDIR) && git clone -b gh-pages git@github.com:$(GITHUB_REPO).git
	cd $(TMPDIR)/hqgreek && git rm -rf * && git commit -m "Clearing gh-pages via makefile."
	cp -r $(WEBDIR)/. $(TMPDIR)/hqgreek
	cp -r $(DOCDIR)/_build/html $(TMPDIR)/hqgreek/docs
	cd $(TMPDIR)/hqgreek && git add .
	cd $(TMPDIR)/hqgreek && git commit -m "Updating site via makefile."
	cd $(TMPDIR)/hqgreek && git push -u origin gh-pages
	rm -rf $(TMPDIR)
	git pull

server: sitedata
	cd $(WEBDIR) && python3 -m http.server 8080

issues:
	handkerchief -a -o $(ISSUES_FILE) $(GITHUB_REPO)

clean:
	rm -r $(DOCDIR)/api
	rm -r $(DOCDIR)/_build
	rm -r $(JSONDIR)
	rm -r $(WEBDIR)/docs
	rm -r $(WEBDIR)/favicon.png

.PHONY: all, test, doc, clean, travis, json, server, sitedata, issues
.IGNORE: clean
