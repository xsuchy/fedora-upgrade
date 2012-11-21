Name:		fedora-upgrade
Version:	18.1
Release:	1%{?dist}
Summary:	Upgrade Fedora to next version using yum upgrade

Group:		Applications/System
License:	GPLv2
URL:		https://github.com/xsuchy/fedora-upgrade
# Sources can be obtained by
# git clone git://github.com/xsuchy/fedora-upgrade.git
# cd fedora-upgrade
# tito build --tgz
Source0:	%{name}-%{version}.tar.gz
BuildArch:	noarch

Requires:	yum
Requires:	yum-utils
Requires:	rpmconf
Requires:	libselinux-utils

%description
Upgrade Fedora to next version using yum upgrade.
This is attempt to automatize steps as listed here:
https://fedoraproject.org/wiki/Upgrading_Fedora_using_yum

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}%{_sbindir}
install -m755 fedora-upgrade %{buildroot}%{_sbindir}

%files
%doc LICENSE README.md
%{_sbindir}/fedora-upgrade


%changelog
