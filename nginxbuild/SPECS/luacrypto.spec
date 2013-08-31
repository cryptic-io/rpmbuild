Name:		luacrypto
Version:	0.3.2
Release:	1%{?dist}.cio
Summary:	OpenSSL wrapper library for lua

License:	MIT
URL:		https://github.com/mkottman/luacrypto/
Source0:	luacrypto-%{version}.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

%description
LuaCrypto is an OpenSSL wrapper library for lua 5.1. This
package is compiled for LuaJIT, which expects its library files
in a different place then the normal lua package for CentOS 6.


%prep
%setup -q


%build
%configure
make %{?_smp_mflags}

%define actuallib %(pkg-config --variable=libdir luajit)

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

mkdir -p %{buildroot}%{actuallib}/lua/5.1
mv %{buildroot}%{actuallib}/crypto.so %{buildroot}%{actuallib}/lua/5.1
rm -f %{buildroot}%{actuallib}/crypto.la

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc COPYING README doc/*
%{_includedir}/luacrypto/lcrypto.h
%{actuallib}/lua/5.1/crypto.so
%{_libdir}/pkgconfig/luacrypto.pc
%{_docdir}/luacrypto/*



%changelog

