Summary: Example VMOD for Varnish
Name: vmod-hash
Version: 0.1
Release: 1%{?dist}
License: BSD
Group: System Environment/Daemons
Source0: libvmod-hash.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: varnish > 3.0
BuildRequires: make, python-docutils

%description
Example VMOD

%prep
%setup -n libvmod-hash

%build
# this assumes that VARNISHSRC is defined on the rpmbuild command line, like this:
# rpmbuild -bb --define 'VARNISHSRC /home/user/rpmbuild/BUILD/varnish-3.0.3' redhat/*spec
./configure VARNISHSRC=%{VARNISHSRC} VMODDIR="$(PKG_CONFIG_PATH=%{VARNISHSRC} pkg-config --variable=vmoddir varnishapi)" --prefix=/usr/ --docdir='${datarootdir}/doc/%{name}'
make
make check

%install
make install DESTDIR=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_libdir}/varnish/vmods/
%doc /usr/share/doc/%{name}/*
%{_mandir}/man?/*

%changelog
* Tue Mar 04 2014 Boris Guéry <guery.b@gmail.com> - 0.1-0.20140304
- Initial version.
