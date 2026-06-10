.FOLDERS :=
.FOLDERS += animate
.FOLDERS += floats
.FOLDERS += generated_files
.FOLDERS += latexdiff
.FOLDERS += media9
.FOLDERS += multi_output
.FOLDERS += precompiled_preamble
.FOLDERS += standalone

.ALL := $(addsuffix .all,$(.FOLDERS))
.CLEAN := $(addsuffix .clean,$(.FOLDERS))

.PHONY: all clean $(.ALL) $(.CLEAN)

all: $(.ALL)
clean: $(.CLEAN)

$(.ALL): %.all:
	$(MAKE) -C $* all

$(.CLEAN): %.clean:
	$(MAKE) -C $* clean
