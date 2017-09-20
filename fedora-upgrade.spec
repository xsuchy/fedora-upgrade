Name:		fedora-upgrade
Version:	27.1
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
* Wed Sep 20 2017 Miroslav Suchý <msuchy@redhat.com> 27.1-1
- remove old changelogs
- remove upgrade from f24
- Add support for Fedora 27

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
