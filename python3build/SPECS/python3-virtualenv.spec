#
# spec file for package python3-virtualenv
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

%{?!py3_ver: %global py3_ver 3.3}

Name:           python3-virtualenv
Version:        1.10
Release:        1%{dist}.cio
Url:            http://www.virtualenv.org/
Summary:        Virtual Python Environment builder
License:        MIT
Group:          Development/Languages/Python
Source:         https://pypi.python.org/packages/source/v/virtualenv/virtualenv-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  python3-devel
# Documentation requirements
#BuildRequires:  python3-Sphinx
#Requires:       python3-pip
#Requires:       python3-setuptools
BuildArch:      noarch

%description
virtualenv is a tool to create isolated Python environments.
The basic problem being addressed is one of dependencies and versions, and
indirectly permissions. Imagine you have an application that needs version 1
of LibFoo, but another application requires version 2. How can you use both
these applications? If you install everything into
/usr/lib/python2.4/site-packages (or whatever your platforms standard location
is), its easy to end up in a situation where you unintentionally upgrade an
application that shouldnt be upgraded.

Or more generally, what if you want to install an application and leave it be?
If an application works, any change in its libraries or the versions of those
libraries can break the application.

Also, what if you cant install packages into the global site-packages
directory? For instance, on a shared host.

In all these cases, virtualenv can help you. It creates an environment that
has its own installation directories, that doesnt share libraries with other
virtualenv environments (and optionally doesnt use the globally installed
libraries either).

%prep
%setup -q -n virtualenv-%{version}

%build
python3 setup.py build
#python3 setup.py build_sphinx && rm build/sphinx/html/.buildinfo

%install
python3 setup.py install --prefix=%{_prefix} --root=%{buildroot}
ln -s %{_bindir}/virtualenv-%{py3_ver} %{buildroot}/%{_bindir}/virtualenv3
rm -f %{buildroot}/%{_bindir}/virtualenv

#%pre
## Since /usr/bin/virtualenv became ghosted to be used with update-alternatives, we have to
## get rid of the old binary resulting from the non-update-alternativies-ified package:
#[[ ! -L %{_bindir}/virtualenv ]] && rm -f %{_bindir}/virtualenv
#exit 0
#
#%post
#update-alternatives \
#    --install %{_bindir}/virtualenv virtualenv %{_bindir}/virtualenv-%{py3_ver} 30

#%preun
#if [ $1 -eq 0 ] ; then
#    update-alternatives --remove virtualenv %{_bindir}/virtualenv-%{py3_ver}
#fi

%files
%defattr(-,root,root,-)
#%doc LICENSE.txt README.rst build/sphinx/html
%ghost %{_bindir}/virtualenv3
%{_bindir}/virtualenv-%{py3_ver}
%{python3_sitelib}/virtualenv-%{version}-py%{py3_ver}.egg-info
%{python3_sitelib}/virtualenv.py
%{python3_sitelib}/virtualenv_support
%{python3_sitelib}/__pycache__/virtualenv.*

%changelog
* Mon Jul 29 2013 speilicke@suse.com
- Don't drop shipped setuptools / pip, they've been fetched from the
  interwebs previously. It doesn't make sense to use the (currently
  matching) system equivalents, it's meant to be self-contained
* Mon Jul 29 2013 speilicke@suse.com
- Initial version
