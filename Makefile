# SPDX-License-Identifier: GPL-2.0-or-later

PREFIX ?= /usr
COURSES_DIR = $(DESTDIR)$(PREFIX)/share/wordtest

COURSES = en-cz/gateway-a1plus

all:

install:
	for course in $(COURSES); do \
		install -d $(COURSES_DIR)/$$course/; \
		install -m 644 $$course/*.txt $(COURSES_DIR)/$$course/; \
	done

.PHONY: all install
