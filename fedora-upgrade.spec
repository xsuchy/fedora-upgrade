Name:		fedora-upgrade
Version:	29.1
Release:	1%{?dist}
Summary:	Upgrade Fedora to next version using dnf upgrade (unofficial tool)

License:	GPLv2
URL:		https://github.com/xsuchy/fedora-upgrade
# Sources can be obtained by
# git clone git://github.com/xsuchy/fedora-upgrade.git
# cd fedora-upgrade
# tito build --tgz
Source0:	%{name}-%{version}.tar.gz
BuildArch:	noarch

Requires:	dnf
Requires:	dnf-plugins-core
Recommends:	dnf-plugin-system-upgrade
Requires:   dnf-utils
Requires:	cpio
Requires:	rpmconf
Requires:	libselinux-utils
Requires:   policycoreutils
Requires:   distribution-gpg-keys >= 1.14
Suggests:   vim-enhanced
Requires:	wget
BuildRequires: asciidoc
BuildRequires: libxslt

%description
Upgrade Fedora to next version using dnf upgrade.
This is attempt to automatize steps as listed here:
https://fedoraproject.org/wiki/Upgrading_Fedora_using_package_manager

This is an unofficial tool, for official Fedora-supported
upgrades please see:
https://fedoraproject.org/wiki/Upgrading

%prep
%setup -q

%build
a2x -d manpage -f manpage fedora-upgrade.8.asciidoc

%install
mkdir -p %{buildroot}%{_sbindir}
mkdir -p %{buildroot}%{_mandir}/man8
mkdir -p %{buildroot}%{_datadir}/%{name}
install -m755 fedora-upgrade %{buildroot}%{_sbindir}
install -m644 fedora-upgrade.8 %{buildroot}/%{_mandir}/man8/

%files
%license LICENSE
%doc README.md
%{_sbindir}/fedora-upgrade
%doc %{_mandir}/man8/fedora-upgrade.8*
%{_datadir}/%{name}

%changelog
* Wed Aug 08 2018 Miroslav Suchý <msuchy@redhat.com> 29.1-1
- add upgrade from F28 to F29
- Update release notes URL to point towards the correct target version

* Wed Apr 18 2018 Miroslav Suchý <msuchy@redhat.com> 28.2-1
- remove --distro-sync for dnf system-upgrade
- do not check for dnf-plugins-core, it has been installed by check_dnf_deps()
- be more verbose so we have some progress

* Tue Jan 23 2018 Miroslav Suchý <msuchy@redhat.com> 28.1-1
- clean caches before doing any other task
- list orphans after upgrade
- warn if not run as root
- add upgrade to F28 and remove upgrade to F25
- Remove PackageKit cache
- choose better wording for reset priorities
- reset services priorities the systemd way

* Wed Sep 20 2017 Miroslav Suchý <msuchy@redhat.com> 27.1-1
- remove old changelogs
- remove upgrade from f24
- Add support for Fedora 27

* Thu Mar 16 2017 Miroslav Suchý <msuchy@redhat.com> 26.1-1
- add upgrade to F26
