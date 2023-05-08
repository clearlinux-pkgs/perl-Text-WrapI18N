#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Text-WrapI18N
Version  : 0.06
Release  : 13
URL      : https://cpan.metacpan.org/authors/id/K/KU/KUBOTA/Text-WrapI18N-0.06.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/K/KU/KUBOTA/Text-WrapI18N-0.06.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Artistic-1.0
Requires: perl-Text-WrapI18N-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Text::CharWidth)

%description
Text::WrapI18N version 0.06
===========================
This is a module which intends to substitute Text::Wrap,
which supports internationalized texts including:
- multibyte encodings such as UTF-8, EUC-JP, EUC-KR, GB2312, and Big5,
- fullwidth characters like east Asian characters which appear in
UTF-8, EUC-JP, EUC-KR, GB2312, Big5, and so on,
- combining characters like diacritical marks which appear in UTF-8,
ISO-8859-11 (aka TIS-620), and so on, and
- languages which don't use whitespaces between words, like Chinese
and Japanese.

%package dev
Summary: dev components for the perl-Text-WrapI18N package.
Group: Development
Provides: perl-Text-WrapI18N-devel = %{version}-%{release}
Requires: perl-Text-WrapI18N = %{version}-%{release}

%description dev
dev components for the perl-Text-WrapI18N package.


%package perl
Summary: perl components for the perl-Text-WrapI18N package.
Group: Default
Requires: perl-Text-WrapI18N = %{version}-%{release}

%description perl
perl components for the perl-Text-WrapI18N package.


%prep
%setup -q -n Text-WrapI18N-0.06
cd %{_builddir}/Text-WrapI18N-0.06

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Text::WrapI18N.3

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
