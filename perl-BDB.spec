%define upstream_name    BDB
%define upstream_version 1.91

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:	3

Summary:    Asynchronous Berkeley DB access

License:    GPL+ or Artistic
Group:      Development/Perl
Url:        https://search.cpan.org/dist/BDB
Source0:    http://search.cpan.org/CPAN/authors/id/M/ML/MLEHMANN/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: db-devel
BuildRequires: perl(common::sense)
BuildRequires: perl-devel


Requires: perl(common::sense)

%description
This is the Asynchronous Berkeley DB access API for Perl and DB 4.6.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%clean

%files
%doc README Changes META.yml
%{_mandir}/man3/*
%{perl_vendorlib}/*



