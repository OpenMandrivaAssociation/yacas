%define name yacas
%define version 1.3.2
%define release 1

%define major 0
%define libname %mklibname %name %major


Name: %{name}
Summary: Yacas, a computer algebra language
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.gz
Group: Development/Other
URL: http://yacas.sourceforge.net/
BuildRequires: gsl-devel
License: GPLv2

%description
Yacas (Yet Another Computer Algebra System) is a small and highly
flexible computer algebra language. The syntax uses a infix-operator
grammar parser. The distribution contains a small library of
mathematical functions, but its real strength is in the language in
which you can easily write your own symbolic manipulation algorithms.
It supports arbitrary precision arithmetic.

%prep
%setup -q

%build
%configure

%make

%install
%makeinstall_std

%files 
%defattr(-,root,root,0755)
%doc docs/*
%{_datadir}/yacas
%{_bindir}/*

