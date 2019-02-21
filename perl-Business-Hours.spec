#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Business
%define		pnam	Hours
%include	/usr/lib/rpm/macros.perl
Summary:	Business::Hours - Calculate business hours in a time period
Name:		perl-Business-Hours
Version:	0.13
Release:	1
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Business/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	83c7b6af0a373a3bd617e709ced59360
URL:		http://search.cpan.org/dist/Business-Hours/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(Set::IntSpan) >= 1.12
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module is a simple tool for calculating business hours in a time
period. Over time, additional functionality will be added to make it
easy to calculate the number of business hours between arbitrary
dates.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Business/Hours.pm
%{_mandir}/man3/*
