Summary:	mDNS Service Switch Module
Summary(pl):	Moduł NSS mDNS
Name:		nss_mdns
Version:	0.6
Release:	1
License:	LGPL v2.1
Group:		Base
Source0:	http://0pointer.de/lennart/projects/nss-mdns/nss-mdns-%{version}.tar.gz
# Source0-md5:	46e4e6c200ee9dc4a466be5ff9247fbd
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
nss-mdns to wtyczka dla funkcjonalności NSS (Name Service Switch) w
glibc dająca możliwość rozwiązywania nazw poprzez Multicast DNS (znany
także jako Zeroconf lub Apple Rendezvous), efektywnie umożliwiająca
rozwiązywanie nazw przez popularne programy uniksowe/linuksowe w
doraźnej domenie mDNS .local.

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
