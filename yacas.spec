%define name yacas
%define version 1.0.55
%define release %mkrel 2

%define major 0
%define libname %mklibname %name %major


Name: %{name}
Summary: Yacas, a computer algebra language
Version: %{version}
Release: %{release}
Source: %{name}-%{version}.tar.bz2
Patch0: %{name}-doc-destdir.patch.bz2
Group: Development/Other
URL: http://www.xs4all.nl/~apinkus/yacas.html 
BuildRoot: %{_tmppath}/%{name}-buildroot
License: GPL

%description
Yacas (Yet Another Computer Algebra System) is a small and highly
flexible computer algebra language. The syntax uses a infix-operator
grammar parser. The distribution contains a small library of
mathematical functions, but its real strength is in the language in
which you can easily write your own symbolic manipulation algorithms.
It supports arbitrary precision arithmetic.

%package -n %libname
Group: Development/Other
Provides: lib%name = %version-%release
Summary: Yacas libraries

%description -n %libname
Library need by Yacas
Yacas (Yet Another Computer Algebra System) is a small and highly
flexible computer algebra language. The syntax uses a infix-operator
grammar parser. The distribution contains a small library of
mathematical functions, but its real strength is in the language in
which you can easily write your own symbolic manipulation algorithms.
It supports arbitrary precision arithmetic.

%package -n %libname-devel
Group: Development/Other
Provides: lib%name-devel = %version-%release
Requires: %libname = %version-%release
Summary: Development files from Yacas

%description -n %libname-devel
This package contains develpment from Yacas.
Yacas (Yet Another Computer Algebra System) is a small and highly
flexible computer algebra language. The syntax uses a infix-operator
grammar parser. The distribution contains a small library of
mathematical functions, but its real strength is in the language in
which you can easily write your own symbolic manipulation algorithms.
It supports arbitrary precision arithmetic.

%prep
rm -rf $RPM_BUILD_ROOT

%setup -q
%patch0 -p0

%build
%configure

%make -k

%install
# # make install prefix=$RPM_BUILD_ROOT/%{_prefix}
%makeinstall_std datadir=$RPM_BUILD_ROOT/%{_datadir}

%post -n %libname -p /sbin/ldconfig

%postun -n %libname -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT 

%files 
%defattr(-,root,root,0755)
%doc docs/*
%dir %{_datadir}/yacas
%{_datadir}/yacas/*
%exclude %{_datadir}/yacas/include
%{_bindir}/*

%files -n %libname
%defattr(-,root,root,0755)
%_libdir/*.so.*

%files -n %libname-devel
%defattr(-,root,root,0755)
%_libdir/*.so
%_libdir/*.a
%_libdir/*.la
%dir %_libdir/%name
%_libdir/%name/*.so.*
%_libdir/%name/*.so
%_libdir/%name/*.a
%_libdir/%name/*.la
%dir %{_datadir}/yacas/include
%{_datadir}/yacas/include/*


