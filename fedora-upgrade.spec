Name:		fedora-upgrade
Version:	27.0
Release:	1%{?dist}
Summary:	Upgrade Fedora to next version using dnf upgrade (unofficial tool)

Group:		Applications/System
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
Requires:	cpio
Requires:	rpmconf
Requires:	libselinux-utils
Requires:   policycoreutils
Requires:   distribution-gpg-keys
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
* Thu Mar 16 2017 Miroslav Suchý <msuchy@redhat.com> 26.1-1
- add upgrade to F26

* Mon Oct 24 2016 Miroslav Suchý <miroslav@suchy.cz> 25.2-1
- add warning about crashing XWindows

* Mon Oct 24 2016 Miroslav Suchý <miroslav@suchy.cz> 25.1-1
- remove upgrade from F22 and F23
- add upgrade to F25 and use distribution-gpg-keys

* Mon Apr 25 2016 Miroslav Suchý <msuchy@redhat.com> 24.2-1
- do not require yum and yum-utils

* Mon Apr 25 2016 Miroslav Suchý 24.1-1
- dnf does not have clean plugins option
- add example to readme
- fix syntax error

* Mon Apr 25 2016 Miroslav Suchý 23.2-1
- add upgrade to F24
- remove yum and use only DNF
- doc: admit that we can upgrade new releases too
- make clear distance between our and plugin output
- make the weak deps little bit stronger
- pause before rebooting
- dnf download should be quite
- create function install_if_missing
- install dnf-plugin-system-upgrade if not installed
- allow to use official upgrade tool
- more of migration to DNF

* Sun Oct 11 2015 Miroslav Suchý <miroslav@suchy.cz> 23.1-1
- add F23,24 keys
- change note about official tool
- upgrade to F23
- use %%license for LICENSE
- use dnf on F22
- update README.md #15
- do not ask about fedora next when upgrading to F22

* Sat Apr 25 2015 Miroslav Suchý <miroslav@suchy.cz> 22.2-1
- upgrade to F22 was in fact upgrade to F21
- package with rawhide repos was renamed
- restore selinux context after upgrade

* Fri Feb 20 2015 Miroslav Suchý <msuchy@redhat.com> 22.1-1
- bump up version
- import rpmfusion keys only if it exists
- add F22 GPG keys
- add Fedora 22

* Mon Nov 24 2014 Miroslav Suchý <miroslav@suchy.cz> 21.3-1
- 1167079 - fedora-release-standard was renamed to fedora-release-nonproduct
- sync upgrade to rawhide with wiki page

* Thu Oct 02 2014 Miroslav Suchý 21.2-1
- productize Fedora after upgrade

* Wed Jul 16 2014 Miroslav Suchý <miroslav@suchy.cz> 21.1-1
- bump up major version to 21
- remove upgrades from F17,F18 and add upgrade to F21
- delete F18 gpg keys and add F21 gpg keys
- use correct version
- clean up yum cache after upgrade
- "read -t 1" exits greater than 128, which trips over "set -e".
- Upgrade of 19->20 now available.
- Remove out-of-date note saying that only 17->18 is supported.
- put repeated code of welcome banner to separate function
- print exit banner even if there is no problem
- make trap message little precise
- Adding trap for nice exit message
- Clear the stdin buffer before question
- Added installation check as a first step

* Fri Sep 20 2013 Miroslav Suchý <miroslav@suchy.cz> 20.2-1
- add wget require explicit dependency

* Wed Aug 21 2013 Miroslav Suchý <miroslav@suchy.cz> 20.1-1
- bump up version to 20
- add upgrade to Fedora 20
- add rpmfusion 20 gpg keys
- add fedora-20-primary gpg key
- Import rpmfusion-nonfree key if it is potentially required.  Refactor.

* Mon Jul 15 2013 Miroslav Suchý <msuchy@redhat.com> 19.3-1
- 983082 - clarify that fedora-upgrade is not an official upgrade tool
- set up differ for rpmconf
- warn about loosing session (bug 962983)
- update README

* Mon May 13 2013 Miroslav Suchý <msuchy@redhat.com> 19.2-1
- #4 - Enable updates-testing on branched development release

* Wed Mar 20 2013 Miroslav Suchý <msuchy@redhat.com> 19.1-1
- bump up version
- suggest unwanted packages
- add upgrade to Fedora 19
- use gpg keys shipped with fedora-upgrade
- distribute gpg keys with rpm
- add GPG keys
- call "yum upgrade" before upgrade
- fixes #3 - upgrade to latest selinux before upgrading

* Mon Dec 17 2012 Miroslav Suchý <msuchy@redhat.com> 18.5-1
- add fedora-git releaser

* Mon Dec 17 2012 Miroslav Suchý <msuchy@redhat.com> 18.4-1
- make output more friendly by adding more space
- enhance README.md - what works and how it works
- make optional steps during upgrade really optional
- bug 844167 should be fixed, no need to disable selinux now
- add support for upgrading to rawhide

* Tue Dec 11 2012 Miroslav Suchý <msuchy@redhat.com> 18.3-1
- do not set executable flag on man page
- add man page

* Wed Nov 21 2012 Miroslav Suchý 18.2-1
- initial release

