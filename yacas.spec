%define name yacas
%define version 1.2.2
%define release %mkrel 3

%define major 0
%define libname %mklibname %name %major


Name: %{name}
Summary: Yacas, a computer algebra language
Version: %{version}
Release: %{release}
Source: %{name}-%{version}.tar.bz2
Group: Development/Other
URL: http://yacas.sourceforge.net/
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildRequires: gsl-devel
License: GPL

%description
Yacas (Yet Another Computer Algebra System) is a small and highly
flexible computer algebra language. The syntax uses a infix-operator
grammar parser. The distribution contains a small library of
mathematical functions, but its real strength is in the language in
which you can easily write your own symbolic manipulation algorithms.
It supports arbitrary precision arithmetic.

%prep
rm -rf $RPM_BUILD_ROOT

%setup -q

%build
%configure

%make

%install
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT 

%files 
%defattr(-,root,root,0755)
%doc docs/*
%{_datadir}/yacas
%{_bindir}/*

