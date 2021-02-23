Name:		fedora-upgrade
Version:	34.2
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
Requires:   distribution-gpg-keys >= 1.33
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
* Tue Feb 23 2021 Miroslav Suchý <msuchy@redhat.com> 34.2-1
- fedora-repos-modular does not need to be installed
- handle special case of rdma-core.i686
- print info when checking updates

* Thu Feb 11 2021 Miroslav Suchý <msuchy@redhat.com> 34.1-1
- remove f31
- add f34
- rawhide is f35

* Wed Nov 04 2020 Miroslav Suchý <msuchy@redhat.com> 33.2-1
- do not test if F33 is prerelease

* Tue Aug 25 2020 Miroslav Suchý <msuchy@redhat.com> 33.1-1
- bump up version

* Tue Aug 25 2020 Miroslav Suchý <msuchy@redhat.com> 32.3-1
- do not check prerelease when upgrading to F32
- add Fedora 33

* Wed Mar 04 2020 Miroslav Suchý <msuchy@redhat.com> 32.2-1
- 1767351 - reset modules before the upgrade

* Tue Mar 03 2020 Miroslav Suchý <msuchy@redhat.com> 32.1-1
- add upgrade to f32
- try to restore repos in case of failed upgrade to rawhide
- disable rpmfusion-*-updates when updating to rawhide
- do not upgrade dnf before upgrading to rawhide
- disable updates-modular when updating to rawhide

* Sun Oct 27 2019 Miroslav Suchý <msuchy@redhat.com> 31.3-1
- do not check if F31 is pre-release

* Mon Sep 23 2019 Miroslav Suchý <msuchy@redhat.com> 31.2-1
- 1747408 - reset modules before upgrading
- enable modulare-testing if needed

* Wed Aug 28 2019 Miroslav Suchý <msuchy@redhat.com> 31.1-1
- add migration to Fedora 31
- do not run tracer and needs-restarting plugins

* Thu Apr 11 2019 Miroslav Suchý <msuchy@redhat.com> 30.5-1
- warn when user is not running screen or tmux
- improve exit banner when failure happens
- package fedora-release does not need to be installed, it can be fedora-
  release-common

* Tue Mar 19 2019 Miroslav Suchý <msuchy@redhat.com> 30.4-1
- Fix the offline update path for fedora 30

* Mon Mar 18 2019 Miroslav Suchý <msuchy@redhat.com> 30.3-1
- unmount tmpfs when error occurs
- trap Ctrl+C
- accept "rawhide" as upgrade-to version
- allow to upgrade to specific version
- add link to common bugs
- allow to mount /var/cache/dnf as tmpfs

* Thu Feb 28 2019 Miroslav Suchý <msuchy@redhat.com> 30.2-1
- set module_id during upgrade
- add upgrade F29 to F30
- remove old changelog entries
- remove Group tag from spec

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
