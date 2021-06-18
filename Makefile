
.PHONY : all html pdf deploy clean

all: html
publish: clean html pdf deploy

html:
	if [ ! -d _book ];then mkdir _book;fi
	cd book; \
	Rscript -e "bookdown::render_book('.', 'bookdown::gitbook')"
	cp -R book/style.css _book;

pdf:
	cd book; \
	Rscript -e "bookdown::render_book('.', 'bookdown::pdf_book')"

# add git worktree
worktree:
	./_helper.bash worktree

deploy:
	./_helper.bash deploy

clean:
	rm -rf _book/* \
	rm book/*.rds \
	rm book/*.md \
	rm -r book/_bookdown_files \
	rm book/Reproducible\ Research\ in\ R.*
