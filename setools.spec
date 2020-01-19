%global setools_maj_ver 3.3
%global setools_min_ver 8
%global gitver f1e5b20

Name: setools
Version: %{setools_maj_ver}.%{setools_min_ver}
Release: 1.1%{?dist}
License: GPLv2
URL: http://oss.tresys.com/projects/setools
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
# Source: http://oss.tresys.com/projects/setools/chrome/site/dists/setools-%{version}/setools-%{version}.tar.bz2
# git clone https://github.com/TresysTechnology/setools3.git
# cd setools3
# gitrev=`git rev-parse --verify --short HEAD`
# git archive --format=tar --prefix=setools-3.3.8/ HEAD | bzip2 > setools-3.3.8-$gitrev.tar.bz2
Source: setools-%{version}-%{gitver}.tar.bz2
Source1: setools.pam
Source2: apol.desktop
Source3: seaudit.desktop
Patch1: 0001-Since-we-do-not-ship-neverallow-rules-all-always-fai.patch
Patch2: 0002-Fix-sepol-calls-to-work-with-latest-libsepol.patch
Patch4: 0004-Apply-selinux_current_policy_path-patch.patch
Patch5: 0005-Apply-seaudit-patch-for-progress.c.patch
Patch6: 0006-Add-support-for-boolean-subs.patch
Patch7: 0007-Setools-noship.patch
Patch8: 0008-Add-alias-support-to-seinfo-t.patch
Patch9: 0009-Fix-help-message-on-sesearch-D.patch
Patch11: 0011-Fix-Wformat-security-issues.patch
# Patch12: 0012-Fix-configure.ac-to-use-SWIG-3.0.0.patch
Patch13: 0013-libqpol-Skip-types-when-building-type-attribute-map.patch

Summary: Policy analysis tools for SELinux
Group: System Environment/Base
Requires: setools-libs = %{version}-%{release} setools-libs-tcl = %{version}-%{release} setools-gui = %{version}-%{release} setools-console = %{version}-%{release}

# external requirements
%define autoconf_ver 2.59
%define bwidget_ver 1.8
%define gtk_ver 2.8
%define sepol_ver 2.5-0
%define selinux_ver 2.5-0
%define sqlite_ver 3.2.0
%define swig_ver 2.0.7-3
%define tcltk_ver 8.4.9

%description
SETools is a collection of graphical tools, command-line tools, and
libraries designed to facilitate SELinux policy analysis.

This meta-package depends upon the main packages necessary to run
SETools.

%package libs
License: LGPLv2
Summary: Policy analysis support libraries for SELinux
Group: System Environment/Libraries
Requires: libselinux >= %{selinux_ver} libsepol >= %{sepol_ver} sqlite >= %{sqlite_ver}
Obsoletes: setools-libs-java
Obsoletes: setools-libs-python < 3.3.7-36
BuildRequires: flex  bison  pkgconfig bzip2-devel
BuildRequires: glibc-devel libstdc++-devel gcc gcc-c++
BuildRequires: libselinux-devel >= %{selinux_ver} libsepol-devel >= %{sepol_ver}
BuildRequires: libsepol-static >= %{sepol_ver}
BuildRequires: sqlite-devel >= %{sqlite_ver} libxml2-devel
BuildRequires: tcl-devel >= %{tcltk_ver}
BuildRequires: autoconf >= %{autoconf_ver} automake

%description libs
SETools is a collection of graphical tools, command-line tools, and
libraries designed to facilitate SELinux policy analysis.

This package includes the following run-time libraries:

  libapol       policy analysis library
  libpoldiff    semantic policy difference library
  libqpol       library that abstracts policy internals
  libseaudit    parse and filter SELinux audit messages in log files
  libsefs       SELinux file contexts library

%package libs-tcl
License: LGPLv2
Summary: Tcl bindings for SELinux policy analysis
Group: Development/Languages
Requires: setools-libs = %{version}-%{release} tcl >= %{tcltk_ver}
BuildRequires: tcl-devel >= %{tcltk_ver} swig >= %{swig_ver}

%description libs-tcl
SETools is a collection of graphical tools, command-line tools, and
libraries designed to facilitate SELinux policy analysis.

This package includes Tcl bindings for the following libraries:

  libapol       policy analysis library
  libpoldiff    semantic policy difference library
  libqpol       library that abstracts policy internals
  libseaudit    parse and filter SELinux audit messages in log files
  libsefs       SELinux file contexts library

%package devel
License: LGPLv2
Summary: Policy analysis development files for SELinux
Group: Development/Libraries
Requires: libselinux-devel >= %{selinux_ver} libsepol-devel >= %{sepol_ver} setools-libs = %{version}-%{release}
BuildRequires: sqlite-devel >= %{sqlite_ver} libxml2-devel

%description devel
SETools is a collection of graphical tools, command-line tools, and
libraries designed to facilitate SELinux policy analysis.

This package includes header files and archives for the following
libraries:

  libapol       policy analysis library
  libpoldiff    semantic policy difference library
  libqpol       library that abstracts policy internals
  libseaudit    parse and filter SELinux audit messages in log files
  libsefs       SELinux file contexts library

%package console
Summary: Policy analysis command-line tools for SELinux
Group: System Environment/Base
License: GPLv2
Requires: setools-libs = %{version}-%{release}
Requires: libselinux >= %{selinux_ver}

%description console
SETools is a collection of graphical tools, command-line tools, and
libraries designed to facilitate SELinux policy analysis.

This package includes the following console tools:

  secmds          command line tools: seinfo, sesearch
  sediff          semantic policy difference tool

%package gui
Summary: Policy analysis graphical tools for SELinux
Group: System Environment/Base
Requires: tcl >= %{tcltk_ver} tk >= %{tcltk_ver} bwidget >= %{bwidget_ver}
Requires: setools-libs = %{version}-%{release} setools-libs-tcl = %{version}-%{release}
Requires: glib2 gtk2 >= %{gtk_ver} usermode
BuildRequires: gtk2-devel >= %{gtk_ver} libglade2-devel libxml2-devel tk-devel >= %{tcltk_ver}
BuildRequires: desktop-file-utils

%description gui
SETools is a collection of graphical tools, command-line tools, and
libraries designed to facilitate SELinux policy analysis.

This package includes the following graphical tools:

  apol          policy analysis tool
  seaudit       audit log analysis tool

%define setoolsdir %{_datadir}/setools-%{setools_maj_ver}
%define tcllibdir %{_libdir}/setools

%prep
%setup -q
%patch1 -p 1 -b .neverallow
%patch2 -p 1 -b .libsepol
%patch4 -p 1 -b .current_policy
%patch5 -p 1 -b .seaudit
%patch6 -p 1 -b .boolean-subs
%patch7 -p 1 -b .noship
%patch8 -p 1 -b .seinfo-t
%patch9 -p 1 -b .sesearch-D
%patch11 -p 1 -b .Wformat-security
# %patch12 -p 1 -b .version
%patch13 -p 1 -b .libqpol

%ifarch sparc sparcv9 sparc64 s390 s390x
    for file in `find . -name Makefile.am`; do
        sed -i -e 's:-fpic:-fPIC:' $file;
    done
%endif
# Fixup expected version of SWIG:
sed -i -e "s|AC_PROG_SWIG(1.3.28)|AC_PROG_SWIG(2.0.0)|g" configure.ac
# and rebuild the autotooled files:
aclocal
autoreconf -if

%build
automake
%configure --libdir=%{_libdir} --disable-bwidget-check --disable-selinux-check \
    --enable-swig-tcl
# work around issue with gcc 4.3 + gnu99 + swig-generated code:
make %{?_smp_mflags}

%install
rm -rf ${RPM_BUILD_ROOT}
make DESTDIR=${RPM_BUILD_ROOT} INSTALL="install -p" install
mkdir -p ${RPM_BUILD_ROOT}%{_datadir}/applications
mkdir -p ${RPM_BUILD_ROOT}%{_datadir}/pixmaps
install -d -m 755 ${RPM_BUILD_ROOT}%{_sysconfdir}/pam.d
install -p -m 644 %{SOURCE1} ${RPM_BUILD_ROOT}%{_sysconfdir}/pam.d/seaudit
install -d -m 755 ${RPM_BUILD_ROOT}%{_sysconfdir}/security/console.apps
install -p -m 644 packages/rpm/seaudit.console ${RPM_BUILD_ROOT}%{_sysconfdir}/security/console.apps/seaudit
install -d -m 755 ${RPM_BUILD_ROOT}%{_datadir}/applications
install -p -m 644 apol/apol.png ${RPM_BUILD_ROOT}%{_datadir}/pixmaps/apol.png
install -p -m 644 seaudit/seaudit.png ${RPM_BUILD_ROOT}%{_datadir}/pixmaps/seaudit.png
desktop-file-install --dir ${RPM_BUILD_ROOT}%{_datadir}/applications %{SOURCE2}
ln -sf consolehelper ${RPM_BUILD_ROOT}/%{_bindir}/seaudit
# remove static libs
rm -f ${RPM_BUILD_ROOT}/%{_libdir}/*.a
# ensure permissions are correct
chmod 0755 ${RPM_BUILD_ROOT}/%{_libdir}/*.so.*
chmod 0755 ${RPM_BUILD_ROOT}/%{_libdir}/%{name}/*/*.so.*
chmod 0644 ${RPM_BUILD_ROOT}/%{tcllibdir}/*/pkgIndex.tcl

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%defattr(-,root,root,-)

%files libs
%defattr(-,root,root,-)
%{!?_licensedir:%global license %%doc}
%license COPYING COPYING.GPL COPYING.LGPL
%doc AUTHORS ChangeLog KNOWN-BUGS NEWS README
%{_libdir}/libqpol.so.*
%{_libdir}/libapol.so.*
%{_libdir}/libpoldiff.so.*
%{_libdir}/libsefs.so.*
%{_libdir}/libseaudit.so.*
%{tcllibdir}/apol_tcl/
%dir %{setoolsdir}

%files libs-tcl
%defattr(-,root,root,-)
%dir %{tcllibdir}
%{tcllibdir}/qpol/
%{tcllibdir}/apol/
%{tcllibdir}/poldiff/
%{tcllibdir}/seaudit/
%{tcllibdir}/sefs/

%files devel
%defattr(-,root,root,-)
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_includedir}/qpol/
%{_includedir}/apol/
%{_includedir}/poldiff/
%{_includedir}/seaudit/
%{_includedir}/sefs/

%files console
%defattr(-,root,root,-)
%{_bindir}/seinfo
%{_bindir}/sesearch
%{_bindir}/sediff
%{_bindir}/findcon
%{_bindir}/sechecker
%{setoolsdir}/sechecker-profiles/
%{setoolsdir}/sechecker_help.txt
%{_mandir}/man1/findcon.1.gz
%{_mandir}/man1/sechecker.1.gz
%{_mandir}/man1/sediff.1.gz
%{_mandir}/man1/seinfo.1.gz
%{_mandir}/man1/sesearch.1.gz

%files gui
%defattr(-,root,root,-)
%{_bindir}/seaudit
%{_bindir}/apol
%{setoolsdir}/apol_help.txt
%{setoolsdir}/domaintrans_help.txt
%{setoolsdir}/file_relabel_help.txt
%{setoolsdir}/infoflow_help.txt
%{setoolsdir}/types_relation_help.txt
%{setoolsdir}/apol_perm_mapping_*
%{setoolsdir}/seaudit_help.txt
%{setoolsdir}/*.glade
%{setoolsdir}/*.png
%{setoolsdir}/apol.gif
%{setoolsdir}/dot_seaudit
%{_mandir}/man1/apol.1.gz
%{_mandir}/man8/seaudit.8.gz
%{_sbindir}/seaudit
%config(noreplace) %{_sysconfdir}/pam.d/seaudit
%config(noreplace) %{_sysconfdir}/security/console.apps/seaudit
%{_datadir}/applications/*
%attr(0644,root,root) %{_datadir}/pixmaps/*.png

%post libs -p /sbin/ldconfig

%postun libs -p /sbin/ldconfig

%post libs-tcl -p /sbin/ldconfig

%postun libs-tcl -p /sbin/ldconfig

%changelog
* Mon May 23 2016 Petr Lautrbach <plautrba@redhat.com> - 3.3.8-1.1
- Rebase to the latest setools3 sources

* Tue Mar 18 2014 Dan Walsh <dwalsh@redhat.com> - 3.3.7-46
- Move apol_tcl to setools-lib package
Resolves: #1076429

* Thu Feb 13 2014 Dan Walsh <dwalsh@redhat.com> - 3.3.7-45
- Fix sesearch --all

* Fri Jan 24 2014 Daniel Mach <dmach@redhat.com> - 3.3.7-44
- Mass rebuild 2014-01-24

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 3.3.7-43
- Mass rebuild 2013-12-27

* Wed Nov 27 2013 Dan Walsh <dwalsh@redhat.com> - 3.3.7-42
- Add back in findcon and sechecker for RHEL customer request
Resolves: 927522

* Mon Sep 16 2013 Dan Walsh <dwalsh@redhat.com> - 3.3.7-41
- Cleanup Destop files.
Resolves: 884174

* Fri Jul 19 2013 Dan Walsh <dwalsh@redhat.com> - 3.3.7-40
- Fix help message on sesearch -D

* Thu May 16 2013 Dan Walsh <dwalsh@redhat.com> - 3.3.7-39
- Remove --default and --audit from sesearch
- Make -D == --dontaudit in sesearch

* Thu Mar 28 2013 Dan Walsh <dwalsh@redhat.com> - 3.3.7-38
- Add alias support to seinfo -t

* Wed Mar 27 2013 Kalev Lember <kalevlember@gmail.com> - 3.3.7-37
- Obsolete the removed setools-libs-python subpackage

* Fri Mar 15 2013 Dan Walsh <dwalsh@redhat.com> - 3.3.7-36
- Drop support for python bindings

* Thu Mar 14 2013 Dan Walsh <dwalsh@redhat.com> - 3.3.7-35
- Add support for substituting bools to sesearch and seinfo

* Wed Jan 30 2013 Dan Walsh <dwalsh@redhat.com> - 3.3.7-34
- Rebuild using pristine source from Tresys

* Tue Jan 29 2013 Dan Walsh <dwalsh@redhat.com> - 3.3.7-33
- Apply swig patch to make apol work again.

* Mon Jan 7 2013 Dan Walsh <dwalsh@redhat.com> - 3.3.7-32
- Rebuild with new tool chain

* Fri Sep 28 2012 Dan Walsh <dwalsh@redhat.com> - 3.3.7-31
- Add filename_trans to python/setools/sesearch bindings

* Fri Sep 28 2012 Dan Walsh <dwalsh@redhat.com> - 3.3.7-30
- Apply Lars Jensen patch to fix seaudit
- Remove java bindings, not supported

* Sun Sep 16 2012 Dan Walsh <dwalsh@redhat.com> - 3.3.7-29
- Remove tools that we do not want to support

* Mon Aug 20 2012 Dan Horák <dan[at]danny.cz> - 3.3.7-28
- use autoreconf to rebuild all autotooled files (FTBFS)

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.7-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jul 11 2012 Dan Walsh <dwalsh@redhat.com> - 3.3.7-26
- mgrepl patch to  Fix swig coding style for structures related to SWIG changes

* Wed Jul 4 2012 Dan Walsh <dwalsh@redhat.com> - 3.3.7-25
- Fix swig coding style for structures related to SWIG changes

* Wed May 2 2012 Dan Walsh <dwalsh@redhat.com> - 3.3.7-24
- Revert setools current patch

- Rebuild to get latest libsepol which fixes the file_name transition problems
- Use selinux_current_policy_path to read by default policy

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.7-22
- Rebuilt for c++ ABI breakage

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.7-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 20 2011 Dan Walsh <dwalsh@redhat.com> - 3.3.7-20
- Rebuild to use latest libsepol

* Wed Oct 26 2011 Dan Walsh <dwalsh@redhat.com> - 3.3.7-19
- Add ftrule*h in apol and qpol 

* Wed Sep 21 2011 Dan Walsh <dwalsh@redhat.com> - 3.3.7-18
- Fix output to match input in policy

* Tue Sep 20 2011 Dan Walsh <dwalsh@redhat.com> - 3.3.7-17
- Fix to build with latest libsepol
- Show filename transition files

* Thu Apr 21 2011 Dan Walsh <dwalsh@redhat.com> - 3.3.7-16
- Rebuild for new sepol

* Fri Apr 15 2011 Dan Walsh <dwalsh@redhat.com> - 3.3.7-15
- Rebuild for new sepol

* Sat Apr 9 2011 Dan Walsh <dwalsh@redhat.com> - 3.3.7-14
- Rebuild for new sepol

* Sun Feb 27 2011 Dennis Gilmore <dennis@ausil.us> - 3.3.7-13
- switch in -fPIC in Makefile.am in prep stage

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.7-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Nov 5 2010 Dan Walsh <dwalsh@redhat.com> 3.3.6-10
- Exit seinfo and sesearch with proper status

* Fri Nov 5 2010 Dan Walsh <dwalsh@redhat.com> 3.3.6-9
- Rebuild for new libxml2

* Thu Oct 14 2010 Dan Walsh <dwalsh@redhat.com> 3.3.6-8
- Return None when no records match python setools.sesearch

* Thu Aug 19 2010 Dan Walsh <dwalsh@redhat.com> 3.3.6-7
- Add range to ports in seinfo python

* Tue Aug 3 2010 Dan Walsh <dwalsh@redhat.com> 3.3.6-6
- Return range with ports

* Tue Aug 3 2010 Dan Walsh <dwalsh@redhat.com> 3.3.6-5
- Add port support to setools python 

* Mon Jul 26 2010 David Malcolm <dmalcolm@redhat.com> - 3.3.7-4
- fixup configure.ac to expect SWIG 2.0.0; bump the python version to 2.7 in
patch 1

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 3.3.7-3
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Wed May 12 2010 Chris PeBenito <cpebenito@tresys.com> 3.3.7-2
- Add missing bzip2 dependencies.

* Wed May 12 2010 Chris PeBenito <cpebenito@tresys.com> 3.3.7-1
- New upstream release.

* Tue Aug 11 2009 Dan Walsh <dwalsh@redhat.com> 3.3.6-4
- Add python bindings for sesearch and seinfo

* Tue Jul 28 2009 Dan Walsh <dwalsh@redhat.com> 3.3.6-3
- Fix qpol install of include files

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul 22 2009 Chris PeBenito <cpebenito@tresys.com> 3.3.6-1
- New upstream release.

* Sun Apr  5 2009 Dan Horák <dan[at]danny.cz> - 3.3.5-8
- don't expect that java-devel resolves as gcj

* Sun Apr  5 2009 Dan Horák <dan[at]danny.cz> - 3.3.5-7
- add support for s390x

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Dec 04 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 3.3.5-5
- Rebuild for Python 2.6

* Mon Dec  1 2008 Michael Schwendt <mschwendt@fedoraproject.org> - 3.3.5-4
- Include %%tcllibdir directory in -libs-tcl package.

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 3.3.5-3
- Rebuild for Python 2.6

* Wed Sep 17 2008 Dennis Gilmore <dennis@ausil.us> 3.3.5-2
- fix building in sparc and s390 arches

* Tue Aug 26 2008 Chris PeBenito <cpebenito@tresys.com> 3.3.5-1
- Update to upstream version 3.3.5.

* Wed Feb 27 2008 Chris PeBenito <cpebenito@tresys.com> 3.3.4-1
- Fixes gcc 4.3, glibc 2.7, tcl 8.5, and libsepol 2.0.20 issues.
- Fix policy loading when policy on disk is higher version than the kernel.

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 3.3.2-3
- Autorebuild for GCC 4.3

* Tue Jan 29 2008 Chris Pebenito <cpebenito@tresys.com> 3.3.2-2.fc9
- Bump to pick up new libsepol and policy 22.

* Wed Nov 28 2007 Chris Pebenito <cpebenito@tresys.com> 3.3.2-1.fc9
- Update for 3.3.2.

* Thu Oct 18 2007 Chris PeBenito <cpebenito@tresys.com> 3.3.1-7.fc8
- Rebuild to fix ppc64 issue.

* Wed Oct 17 2007 Chris PeBenito <cpebenito@tresys.com> 3.3.1-6.fc8
- Update for 3.3.1.

* Tue Aug 28 2007 Fedora Release Engineering <rel-eng at fedoraproject dot org> - 3.2-4
- Rebuild for selinux ppc32 issue.

* Fri Jul 20 2007 Dan Walsh <dwalsh@redhat.com> 3.2-3
- Move to Tresys spec file

* Wed Jun 13 2007 Dan Walsh <dwalsh@redhat.com> 3.2-2
- Bump for rebuild

* Mon Apr 30 2007 Dan Walsh <dwalsh@redhat.com> 3.2-1
- Start shipping the rest of the setools command line apps

* Wed Apr 25 2007 Jason Tang <jtang@tresys.com> 3.2-0
- update to SETools 3.2 release

* Fri Feb 02 2007 Jason Tang <jtang@tresys.com> 3.1-1
- update to SETools 3.1 release

* Mon Oct 30 2006 Dan Walsh <dwalsh@redhat.com> 3.0-2.fc6
- bump for fc6
 
* Thu Oct 26 2006 Dan Walsh <dwalsh@redhat.com> 3.0-2
- Build on rawhide

* Sun Oct 15 2006 Dan Walsh <dwalsh@redhat.com> 3.0-1
- Update to upstream

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - sh: line 0: fg: no job control
- rebuild

* Tue May 23 2006 Dan Walsh <dwalsh@redhat.com> 2.4-2
- Remove sqlite include directory

* Wed May 3 2006 Dan Walsh <dwalsh@redhat.com> 2.4-1
- Update from upstream

* Mon Apr 10 2006 Dan Walsh <dwalsh@redhat.com> 2.3-3
- Fix help
- Add icons

* Tue Mar 21 2006 Dan Walsh <dwalsh@redhat.com> 2.3-2
- Remove console apps for sediff, sediffx and apol

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 2.3-1.2
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 2.3-1.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Tue Jan 31 2006 Dan Walsh <dwalsh@redhat.com> 2.3-1
- Update from upstream
  * apol:
        added new MLS components tab for sensitivities, 
        levels, and categories.
        Changed users tab to support ranges and default 
        levels.
        added range transition tab for searching range
        Transition rules.
        added new tab for network context components.
        added new tab for file system context components.
  * libapol:
        added binpol support for MLS, network contexts, 
        and file system contexts.
  * seinfo:
        added command line options for MLS components.
        added command line options for network contexts
        and file system contexts.
  * sesearch:
        added command line option for searching for rules
        by conditional boolean name.
  * seaudit:
        added new column in the log view for the 'comm' 
        field found in auditd log files.
        added filters for the 'comm' field and 'message'
        field.
  * manpages:
        added manpages for all tools.        



* Fri Dec 16 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt for new gcj

* Wed Dec 14 2005 Dan Walsh <dwalsh@redhat.com> 2.2-4
- Fix dessktop files
- Apply fixes from bkyoung

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Thu Nov 3 2005 Dan Walsh <dwalsh@redhat.com> 2.2-3
- Move more gui files out of base into gui 

* Thu Nov 3 2005 Dan Walsh <dwalsh@redhat.com> 2.2-2
- Move sediff from gui to main package

* Thu Nov 3 2005 Dan Walsh <dwalsh@redhat.com> 2.2-1
- Upgrade to upstream version

* Thu Oct 13 2005 Dan Walsh <dwalsh@redhat.com> 2.1.3-1
- Upgrade to upstream version

* Mon Oct 10 2005 Tomas Mraz <tmraz@redhat.com> 2.1.2-3
- use include instead of pam_stack in pam config

* Thu Sep 1 2005 Dan Walsh <dwalsh@redhat.com> 2.1.2-2
- Fix spec file
 
* Thu Sep 1 2005 Dan Walsh <dwalsh@redhat.com> 2.1.2-1
- Upgrade to upstream version
 
* Thu Aug 18 2005 Florian La Roche <laroche@redhat.com>
- do not package debug files into the -devel package

* Wed Aug 17 2005 Jeremy Katz <katzj@redhat.com> - 2.1.1-3
- rebuild against new cairo

* Wed May 25 2005 Dan Walsh <dwalsh@redhat.com> 2.1.1-0
- Upgrade to upstream version

* Mon May 23 2005 Bill Nottingham <notting@redhat.com> 2.1.0-5
- put libraries in the right place (also puts debuginfo in the right
  package)
- add %%defattr for -devel too

* Thu May 12 2005 Dan Walsh <dwalsh@redhat.com> 2.1.0-4
- Move sepcut to gui apps.

* Fri May 6 2005 Dan Walsh <dwalsh@redhat.com> 2.1.0-3
- Fix Missing return code.

* Wed Apr 20 2005 Dan Walsh <dwalsh@redhat.com> 2.1.0-2
- Fix requires line

* Tue Apr 19 2005 Dan Walsh <dwalsh@redhat.com> 2.1.0-1
- Update to latest from tresys

* Tue Apr 5 2005 Dan Walsh <dwalsh@redhat.com> 2.0.0-2
- Fix buildrequires lines in spec file

* Wed Mar 2 2005 Dan Walsh <dwalsh@redhat.com> 2.0.0-1
- Update to latest from tresys

* Mon Nov 29 2004 Dan Walsh <dwalsh@redhat.com> 1.5.1-6
- add FALLBACK=true to /etc/security/console.apps/apol

* Wed Nov 10 2004 Dan Walsh <dwalsh@redhat.com> 1.5.1-3
- Add badtcl patch from Tresys.

* Mon Nov 8 2004 Dan Walsh <dwalsh@redhat.com> 1.5.1-2
- Apply malloc problem patch provided by  Sami Farin 

* Mon Nov 1 2004 Dan Walsh <dwalsh@redhat.com> 1.5.1-1
- Update to latest from Upstream

* Wed Oct 6 2004 Dan Walsh <dwalsh@redhat.com> 1.4.1-5
- Update tresys patch

* Mon Oct 4 2004 Dan Walsh <dwalsh@redhat.com> 1.4.1-4
- Fix directory ownership

* Thu Jul 8 2004 Dan Walsh <dwalsh@redhat.com> 1.4.1-1
- Latest from Tresys

* Wed Jun 23 2004 Dan Walsh <dwalsh@redhat.com> 1.4-5
- Add build requires libselinux

* Tue Jun 22 2004 Dan Walsh <dwalsh@redhat.com> 1.4-4
- Add support for policy.18

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Thu Jun 10 2004 Dan Walsh <dwalsh@redhat.com> 1.4-2
- Fix install locations of policy_src_dir

* Wed Jun 2 2004 Dan Walsh <dwalsh@redhat.com> 1.4-1
- Update to latest from TRESYS.

* Tue Jun 1 2004 Dan Walsh <dwalsh@redhat.com> 1.3-3
- Make changes to work with targeted/strict policy
* Fri Apr 16 2004 Dan Walsh <dwalsh@redhat.com> 1.3-2
- Take out requirement for policy file

* Fri Apr 16 2004 Dan Walsh <dwalsh@redhat.com> 1.3-1
- Fix doc location

* Fri Apr 16 2004 Dan Walsh <dwalsh@redhat.com> 1.3-1
- Latest from TRESYS

* Tue Apr 13 2004 Dan Walsh <dwalsh@redhat.com> 1.2.1-8
- fix location of policy.conf file

* Tue Apr 6 2004 Dan Walsh <dwalsh@redhat.com> 1.2.1-7
- Obsolete setools-devel
* Tue Apr 6 2004 Dan Walsh <dwalsh@redhat.com> 1.2.1-6
- Fix location of 
* Tue Apr 6 2004 Dan Walsh <dwalsh@redhat.com> 1.2.1-5
- Remove devel libraries
- Fix installdir for lib64

* Sat Apr 3 2004 Dan Walsh <dwalsh@redhat.com> 1.2.1-4
- Add usr_t file read to policy

* Thu Mar 25 2004 Dan Walsh <dwalsh@redhat.com> 1.2.1-3
- Use tcl8.4

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 6 2004 Dan Walsh <dwalsh@redhat.com> 1.2.1-1
- New patch

* Fri Feb 6 2004 Dan Walsh <dwalsh@redhat.com> 1.2-1
- Latest upstream version

* Tue Dec 30 2003 Dan Walsh <dwalsh@redhat.com> 1.1.1-1
- New version from upstream
- Remove seuser.te.  Now in policy file.

* Tue Dec 30 2003 Dan Walsh <dwalsh@redhat.com> 1.1-2
- Add Defattr to devel
- move libs to base kit

* Fri Dec 19 2003 Dan Walsh <dwalsh@redhat.com> 1.1-1
- Update to latest code from tresys
- Break into three separate packages for cmdline, devel and gui
- Incorporate the tcl patch

* Mon Dec 15 2003 Jens Petersen <petersen@redhat.com> - 1.0.1-3
- apply setools-1.0.1-tcltk.patch to build against tcl/tk 8.4
- buildrequire tk-devel

* Thu Nov 20 2003 Dan Walsh <dwalsh@redhat.com> 1.0.1-2
- Add Bwidgets to this RPM

* Tue Nov 4 2003 Dan Walsh <dwalsh@redhat.com> 1.0.1-1
- Upgrade to 1.0.1

* Wed Oct 15 2003 Dan Walsh <dwalsh@redhat.com> 1.0-6
- Clean up build

* Tue Oct 14 2003 Dan Walsh <dwalsh@redhat.com> 1.0-5
- Update with correct seuser.te

* Wed Oct 1 2003 Dan Walsh <dwalsh@redhat.com> 1.0-4
- Update with final release from Tresys

* Mon Jun 2 2003 Dan Walsh <dwalsh@redhat.com> 1.0-1
- Initial version
