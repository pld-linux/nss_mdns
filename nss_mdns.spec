Summary:	mDNS Service Switch Module
Summary(pl):	Modu³ NSS mDNS
Name:		nss_mdns
Version:	0.3
Release:	1
License:	LGPL
Group:		Base
Source0:	http://0pointer.de/lennart/projects/nss-mdns/nss-mdns-%{version}.tar.gz
# Source0-md5:	8fae540908567a96c2c8d71d22ccf210
URL:		http://0pointer.de/lennart/projects/nss-mdns/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libdir		/%{_lib}

%description
nss-mdns is a plugin for the GNU Name Service Switch (NSS)
functionality of the GNU C Library (glibc) providing host name
resolution via Multicast DNS (aka Zeroconf, aka Apple Rendezvous),
effectively allowing name resolution by common Unix/Linux programs in
the ad-hoc mDNS domain .local.

%description -l pl
nss-mdns to wtyczka dla funkcjonalno¶ci NSS (Name Service Switch) w
glibc daj±ca mo¿liwo¶æ rozwi±zywania nazw poprzez Multicast DNS (znany
tak¿e jako Zeroconf lub Apple Rendezvous), efektywnie umo¿liwiaj±ca
rozwi±zywanie nazw przez popularne programy uniksowe/linuksowe w
dora¼nej domenie mDNS .local.

%prep
%setup -q -n nss-mdns-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/*
%attr(755,root,root) %{_libdir}/*.so*
