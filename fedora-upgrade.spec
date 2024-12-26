Name:		fedora-upgrade
Version:	41.3
Release:	1%{?dist}
Summary:	Upgrade Fedora to next version using dnf upgrade (unofficial tool)

License:	GPL-2.0-only
URL:		https://github.com/xsuchy/fedora-upgrade
# Sources can be obtained by
# git clone git://github.com/xsuchy/fedora-upgrade.git
# cd fedora-upgrade
# tito build --tgz
Source0:	%{name}-%{version}.tar.gz
BuildArch:	noarch

%if 0%{?fedora} >= 41
Requires:       dnf5
%else
Requires:	dnf
Requires:	dnf-plugins-core
Recommends:	dnf-plugin-system-upgrade
Requires:   dnf-utils
%endif
Requires:       sudo
Requires:	cpio
Requires:	rpmconf
Requires:	libselinux-utils
Requires:   policycoreutils
Requires:   distribution-gpg-keys >= 1.51
Suggests:   vim-enhanced
Requires:	wget
Requires: remove-retired-packages
BuildRequires: asciidoc
BuildRequires: libxslt

%description
Upgrade Fedora to next version using dnf upgrade.
This is attempt to automatize steps as listed here:
https://fedoraproject.org/wiki/Upgrading_Fedora_using_package_manager

This is an unofficial tool, for official Fedora-supported
upgrades please see:
https://fedoraproject.org/wiki/Upgrading

%package -n remove-retired-packages
Summary: Remove retired distribution's packages
Requires: curl
Requires: python3-dnf

%description -n remove-retired-packages
Script that removes packages removed from
Fedora distribution.

%prep
%setup -q

%build
for i in fedora-remove-old-gpg-keys.8.asciidoc fedora-upgrade.8.asciidoc remove-retired-packages.8.asciidoc; do
  a2x -d manpage -f manpage "$i"
done

%install
mkdir -p %{buildroot}%{_sbindir}
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man8
mkdir -p %{buildroot}%{_datadir}/%{name}
install -m755 fedora-upgrade %{buildroot}%{_sbindir}
install -m644 fedora-upgrade.8 %{buildroot}/%{_mandir}/man8/
install -m755 remove-retired-packages %{buildroot}%{_sbindir}
install -m644 remove-retired-packages.8 %{buildroot}/%{_mandir}/man8/
install -m755 fedora-remove-old-gpg-keys %{buildroot}%{_sbindir}/
install -m644 fedora-remove-old-gpg-keys.8 %{buildroot}/%{_mandir}/man8/
install -m755 rpm-print-name-from-filename.py %{buildroot}%{_bindir}/rpm-print-name-from-filename

%files
%license LICENSE
%doc README.md
%{_sbindir}/fedora-upgrade
%doc %{_mandir}/man8/fedora-upgrade.8*
%{_datadir}/%{name}

%files -n remove-retired-packages
%{_sbindir}/remove-retired-packages
%{_sbindir}/fedora-remove-old-gpg-keys
%{_bindir}/rpm-print-name-from-filename
%doc %{_mandir}/man8/remove-retired-packages.8*
%doc %{_mandir}/man8/fedora-remove-old-gpg-keys.8*
%license LICENSE

%changelog
* Thu Dec 26 2024 Miroslav Suchý <msuchy@redhat.com> 41.3-1
- correctly detect tmux
- requires sudo
- add reverence to `dnf history` in man page
- add old gpg keys
- group minimal install does not exist anymore
- move rawhide version

* Tue Nov 05 2024 Miroslav Suchý <msuchy@redhat.com> 41.2-1
- remove-retired-packages: detect removed subpackages
- no need to check if F41 is prerelease
- add new line to repoquery to make remove-retired-packages work with dnf5

* Sat Aug 17 2024 Miroslav Suchý <msuchy@redhat.com> 41.1-1
- add upgrade to f41

* Sun Mar 24 2024 Miroslav Suchý <msuchy@redhat.com> 40.1-1
- upgrade to F40

* Sun Mar 24 2024 Miroslav Suchý <msuchy@redhat.com> 39.2-1
- add upgrade to F40

* Wed Aug 23 2023 Miroslav Suchý <msuchy@redhat.com> 39.1-1
- remove upgrade to F37
- add upgrade to f39 and remove upgrade to f36
- add f39 to releasers
- Speed up selecting retired installed packages
- Require DNF 5 in Fedora >= 41, not Fedora > 38

* Sun May 28 2023 Miroslav Suchý <msuchy@redhat.com> 38.2-1
- use dnf5 on F39+
- Fix typo in main script

* Thu Mar 16 2023 Miroslav Suchý <msuchy@redhat.com> 38.1-1
- add upgrades to F38
- Use "Fedora Linux" to refer to the distro

* Wed Nov 30 2022 Miroslav Suchý <msuchy@redhat.com> 37.2-1
- do not check if f37 is prerelease
- use spdx license
- 2142229 - reference for log what executed /usr/bin/true
- report reason of the retirement

* Thu Aug 25 2022 Miroslav Suchý <msuchy@redhat.com> 37.1-1
- bump up version

* Thu Aug 25 2022 Miroslav Suchý <msuchy@redhat.com> 36.4-1
- add f37 to releasers
- remove upgrade to f35
- remove upgrade to f34
- check if f37 is prerelease
- UPGRADE_FINISHED=2 is for in-progress-to-rawhide
- Add update to F37
- Set current rawhide version
- Do not ignore user request to skip
- Update remove-retired-packages
- do not stop when you want to skip one package
- fixed one typo

* Sun May 08 2022 Miroslav Suchý <msuchy@redhat.com> 36.3-1
- do not test prerelease for F36
- remove-retired-packages: Normalize grammatical tense in messages
- remove-retired-packages: Rewrite introductory text for better clarity
- remove-retired-packages: Normalize quotation marks in echo commands
- ignore if rpmfusion repos are not present during upgrade to rawhide
- ignore if some gpg keys to be remove are missing
- 2066053 - ask for the GPG key if needed
- remove-retired-packages: Typo

* Fri Mar 18 2022 Miroslav Suchý <msuchy@redhat.com> 36.2-1
- 2065720 - fix path to fedora-remove-old-gpg-keys

* Wed Feb 09 2022 Miroslav Suchý <msuchy@redhat.com> 36.1-1
- add upgrade to Feodora 36
- failure during reset of services preset should not be fatal

* Tue Nov 09 2021 Miroslav Suchý <msuchy@redhat.com> 35.3-1
- do not test prerelease during upgrade to F35
- note fedora-remove-old-gpg-keys in fedora-upgrade man page
- print whole list before asking on individual packages
- add fedora 33 gpg keys to remove
- add fedora 32 gpg keys to remove
- add fedora-remove-old-gpg-key
- fail if something fail, or when user interrupt
- grammar edits
- work on list of removed packages rather than components
- Small changes to reduce dependencies

* Thu Sep 23 2021 Miroslav Suchý <msuchy@redhat.com> 35.2-1
- add remove-retired-packages

* Thu Sep 16 2021 Miroslav Suchý <msuchy@redhat.com> 35.1-1
- remove upgrade to f32
- add upgrade to f35

* Thu Apr 29 2021 Miroslav Suchý <msuchy@redhat.com> 34.3-1
- remove prerelease test for F34

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
