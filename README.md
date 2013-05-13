fedora-upgrade
==============

Upgrade Fedora to next version using yum upgrade.

This is attempt to automatize steps as listed here:

https://fedoraproject.org/wiki/Upgrading_Fedora_using_yum


What works
==========

Please note that fedora-upgrade is NOT officially supported upgrade path.
That means it is not tested by Fedora QA before release and bugs in fedora-upgrade
are not blocker for release.
However I am aiming for official support - see https://fedoraproject.org/wiki/Features/FedoraUpgrade

Currently you can upgrade only to next version. You can upgrade from
* Fedora 17 -> Fedora 18
* Fedora 18 -> Fedora 19
* Fedora 19 -> rawhide

You can *not* upgrade from older releases.
You can *not* skip release - e.g. upgrade from Fedora 16 to Fedora 18.


How it works
============

1. Display link to release notes and ask you if you really want to upgrade.
2. Check if dependencies are installed and install them. This step is needed only if you download script from GitHub. Dependencies are always present if you install fedora-upgrade as rpm package.
3. Resolve old .rpmsave and .rpmnew files using [rpmconf](https://github.com/xsuchy/rpmconf/). This step is optional and can be skipped. But it is better to start upgrade with clean state.
4. Download and install new GPG keys - including rpmfusion if you are using it.
5. Update yum and clean all yum metadata. 
6. Upgrade system using yum. In this or any previous step, you can hit Ctrl + C and interrupt upgrade and repeat it as many times you wish. After this step, you could not return (you can use back up, you created backup before upgrade, did you?).
7. Install packages from group 'Minimal Install'. It may happen that some new essential packages have been introduced to Fedora. This step will install them. You may however skip this step if you want to.
8. Resolve old .rpmsave and .rpmnew files using [rpmconf](https://github.com/xsuchy/rpmconf/). This step is optional and can be skipped. But it is better to finish upgrade with clean state.
9. Reset service priorities - the order of init scripts could have changed from the previous version. This steps is optional and can be skipped. And this does not affect services already migrated to systemD units.
11. Optionally report dead packages (packages that are no present in Fedora any more) and you have them installed from previous version.
12. Report success and suggest you reboot.

If there will be a problem during upgrade, this script will immediately stop and will not continue.
If you hit problem before step 6, you can run fedora-upgrade again after you resolve the problem.
If you hit problem in later stage, you can resolve the issue manually and open fedora-upgrade as it is just bash script. And try to finish manually. But most steps after step 6 are optional, so it should not affect stability of your system.

Note
====

If you are upgrading to branched development version then updates-testing is automatically enabled.

BUGS
====

See https://apps.fedoraproject.org/packages/fedora-upgrade/bugs

If you find bug, please [report](https://bugzilla.redhat.com/enter_bug.cgi?product=Fedora&version=rawhide&component=fedora-upgrade) it.


License
=======

GPLv2
