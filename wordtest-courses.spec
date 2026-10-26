#
# WORDTEST-COURSES specfile
#
# (C) Cyril Hrubis metan{at}ucw.cz 2026
#

Summary: Courses for wordtest
Name: wordtest-courses
Version: git
Release: 1
License: GFDL-1.1-or-later
Group: Amusements/Teaching/Language
Url: https://github.com/gfxprim/wordtest-courses
Source: wordtest-courses-%{version}.tar.bz2
BuildArch: noarch
Requires: wordtest

BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot

%description
Language courses for the wordtest vocabulary test application:

- Gateway to the World A1+, English-Czech vocabulary for the Gateway to the
  World A1+ textbook, split into lessons by units.

The Gateway to the World A1+ course is not an official course, it is not
affiliated with or endorsed by Macmillan Education, the publisher of the
Gateway to the World textbooks. The Czech translations were not taken from
the textbook, they were derived from the free GNU/FDL English-Czech
dictionary.

%prep
%setup -n wordtest-courses-%{version}

%build

%install
DESTDIR="$RPM_BUILD_ROOT" make install

%files
%defattr(-,root,root)
%dir %{_datadir}/wordtest/
%{_datadir}/wordtest/en-cz/
%license COPYING DICTIONARY

%changelog
* Mon Oct 26 2026 Cyril Hrubis <metan@ucw.cz>

  Initial version.
