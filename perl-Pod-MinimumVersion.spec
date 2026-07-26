%define upstream_name    Pod-MinimumVersion
Name:		perl-%{upstream_name}
Version:	50
Release:	6

Summary:	Report object from Pod::MinimumVersion
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://user42.tuxfamily.org/pod-minimumversion/index.html
Source0:	https://cpan.metacpan.org/authors/id/K/KR/KRYDE/Pod-MinimumVersion-%{version}.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(IO::String)
BuildRequires:	perl(List::Util)
BuildRequires:	perl(Pod::Parser)
BuildRequires:	perl(Test)
BuildRequires:	perl(version)
BuildArch:	noarch

%description
'Pod::MinimumVersion' parses the POD in a Perl script, module, or document,
and reports what version of Perl is required to process the directives in
it with 'pod2man' etc.

%prep
%setup -q -n %{upstream_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes META.yml
%{_bindir}/pod-minimumversion
%{_mandir}/man3/*
%{_mandir}/man1/pod-minimumversion.1*
%{perl_vendorlib}/*

%changelog
* Wed May 04 2011 Guillaume Rousse <guillomovitch@mandriva.org> 50.0.0-1mdv2011.0
+ Revision: 666352
- import perl-Pod-MinimumVersion

