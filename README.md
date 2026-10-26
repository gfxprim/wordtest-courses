# Courses for wordtest

Language courses for the [wordtest](https://github.com/gfxprim/wordtest)
vocabulary test application.

## Courses

| Course | Languages | Directory |
|--------|-----------|-----------|
| Gateway to the World A1+ | English - Czech | `en-cz/gateway-a1plus/` |

### Gateway to the World A1+

English-Czech vocabulary for the Gateway to the World A1+ textbook, split into
lessons by units.

This is not an official vocabulary course, it is not affiliated with or
endorsed by Macmillan Education, the publisher of the Gateway to the World
textbooks. The Czech translations were not taken from the textbook, they were
derived from the free GNU/FDL English-Czech dictionary, see
[Translations](#translations).

## Installation

The courses are installed into `/usr/share/wordtest/`, each into a
`language-pair/course/` directory:

```
make install
```

All courses are packaged together into a `wordtest-courses` rpm
(`wordtest-courses.spec`) and deb (`debian/`) package.

## Adding a course

1. Put the lessons into a `language-pair/course/` directory, the lesson file
   format is described in the wordtest README.
2. Add the directory to `COURSES` in the `Makefile`.
3. Add the course to the package descriptions in `wordtest-courses.spec` and
   `debian/control`, and for a new language pair also the directory to
   `%files` in `wordtest-courses.spec`.

## Translations

The Czech translations in the Gateway to the World A1+ course are taken from
the GNU/FDL English-Czech dictionary (https://www.svobodneslovniky.cz/).
Entries that are not in the dictionary were translated manually.

## License

The courses are available under the GNU Free Documentation License, Version
1.1 or any later version, see `COPYING`. The tools and the packaging are
available under GPL-2.0-or-later.
