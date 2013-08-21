Name:		fedora-upgrade
Version:	20.0
Release:	1%{?dist}
Summary:	Upgrade Fedora to next version using yum upgrade (unofficial tool)

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
Requires:	vim-enhanced
BuildRequires: asciidoc
BuildRequires: libxslt

%description
Upgrade Fedora to next version using yum upgrade.
This is attempt to automatize steps as listed here:
https://fedoraproject.org/wiki/Upgrading_Fedora_using_yum

This is an unofficial tool, for official Fedora-supported
upgrades please see the 'fedup' tool.

%prep
%setup -q

%build
a2x -d manpage -f manpage fedora-upgrade.8.asciidoc

%install
mkdir -p %{buildroot}%{_sbindir}
mkdir -p %{buildroot}%{_mandir}/man8
mkdir -p %{buildroot}%{_datadir}/%{name}/keys
install -m755 fedora-upgrade %{buildroot}%{_sbindir}
install -m644 fedora-upgrade.8 %{buildroot}/%{_mandir}/man8/
cp -a keys/* %{buildroot}%{_datadir}/%{name}/keys

%files
%doc LICENSE README.md
%{_sbindir}/fedora-upgrade
%doc %{_mandir}/man8/fedora-upgrade.8*
%{_datadir}/%{name}

%changelog
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

