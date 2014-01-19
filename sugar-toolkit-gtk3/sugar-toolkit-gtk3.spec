%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}

Summary: Sugar toolkit GTK+ 3
Name:    sugar-toolkit-gtk3
Version: 0.100
Release: 4.olpcau
URL:     http://wiki.laptop.org/go/Sugar
Source0: sugar-toolkit-gtk3-0.100.tar

# from sugar-toolkit-gtk3 master, last commit 93437ddedf68a2e1e6fc46bcc23b763e59dcf84a

Source1: macros.sugar
Patch0: 0001-Inhibit-suspend-while-a-activity-is-shared.patch
Patch1: 0001-Keep-updated-CellRendererInvoker-self.path-updated-F.patch

License: LGPLv2+
Group:   System Environment/Libraries

BuildRequires: alsa-lib-devel
BuildRequires: gettext-devel
BuildRequires: GConf2-devel
BuildRequires: gtk3-devel
BuildRequires: gobject-introspection-devel
BuildRequires: intltool
BuildRequires: librsvg2-devel
BuildRequires: libSM-devel
BuildRequires: perl-XML-Parser
BuildRequires: pkgconfig
BuildRequires: python-devel
BuildRequires: pygtk2-codegen
BuildRequires: pygobject2-devel

Requires: dbus-python
Requires: gettext
Requires: pygobject3
Requires: python-dateutil
Requires: sugar-datastore
Requires: unzip
# TEMPORARY disable libwebkit2gtk dependency
#Requires: libwebkit2gtk

%description
Sugar is the core of the OLPC Human Interface. The toolkit provides
a set of widgets to build HIG compliant applications and interfaces
to interact with system services like presence and the datastore.
This is the toolkit depending on GTK3.

%package devel
Summary: Invokation information for accessing SugarExt-1.0
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the invocation information for accessing
the SugarExt-1.0 library through gobject-introspection.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
./autogen.sh
%configure
make %{?_smp_mflags} V=1

%install
make install DESTDIR=%{buildroot}

mkdir -p %{buildroot}/%{_sysconfdir}/rpm/
install -p %{SOURCE1} %{buildroot}/%{_sysconfdir}/rpm/macros.sugar

%find_lang %name

#Remove libtool archives.
find %{buildroot} -name '*.la' -exec rm -f {} ';'

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc COPYING README
%{python_sitelib}/*
%{_bindir}/sugar-activity-web
%{_sysconfdir}/rpm/macros.sugar
%{_libdir}/girepository-1.0/*.typelib
%{_libdir}/lib*.so.*
%{_bindir}/sugar-activity

%files devel
%defattr(-,root,root,-)
%{_libdir}/*.so
%{_datadir}/gir-1.0/*.gir

%changelog
* Sat Aug 10 2013 Daniel Drake <dsd@laptop.org> 0.99.1-2
- Add missing dependency on WebKit2, needed for web activities

* Wed Jul 31 2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.99.1-1
- 0.99.1 devel release

* Sat Jul 13 2013 Daniel Drake <dsd@laptop.org> 0.99.0-2
- Remove dependency on simplejson, no longer required.

* Fri Jun 28 2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.99.0-1
- 0.99.0 devel release

* Thu May 30 2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.98.7-1
- Sugar 0.98.7 stable release

* Fri May 24 2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.98.6-1
- Sugar 0.98.6 stable release

* Sat Feb 16 2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.98.5-1
- Sugar 0.98.5 stable release

* Thu Jan 24 2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.98.4-1
- Sugar 0.98.4 stable release

* Fri Dec 21 2012 Simon Schampijer <simon@laptop.org> - 0.98.3-1
- Sugar 0.98.3 stable release

* Tue Dec 18 2012 Peter Robinson <pbrobinson@fedoraproject.org> 0.98.2-1
- Sugar 0.98.2 stable release

* Mon Dec 10 2012 Peter Robinson <pbrobinson@fedoraproject.org> 0.98.1-1
- Sugar 0.98.1 stable release

* Thu Nov 29 2012 Peter Robinson <pbrobinson@fedoraproject.org> 0.98.0-1
- Sugar 0.98.0 stable release

* Tue Nov 27 2012 Peter Robinson <pbrobinson@fedoraproject.org> 0.97.13-1
- 0.97.13 devel release

* Sat Nov 24 2012 Peter Robinson <pbrobinson@fedoraproject.org> 0.97.12-1
- 0.97.12 devel release 

* Thu Nov 22 2012 Peter Robinson <pbrobinson@fedoraproject.org> 0.97.11-1
- 0.97.11 devel release

* Sat Nov 10 2012 Peter Robinson <pbrobinson@fedoraproject.org> 0.97.10-1
- 0.97.10 devel release

* Wed Nov  7 2012 Peter Robinson <pbrobinson@fedoraproject.org> 0.97.9-1
- 0.97.9 devel release

* Thu Oct 25 2012 Peter Robinson <pbrobinson@fedoraproject.org> 0.97.8-1
- 0.97.8 devel release

* Tue Oct 16 2012 Daniel Drake <dsd@laptop.org> 0.97.7-1
- 0.97.7 devel release

* Thu Oct 11 2012 Peter Robinson <pbrobinson@fedoraproject.org> 0.97.6-1
- 0.97.6 devel release

* Fri Oct  5 2012 Peter Robinson <pbrobinson@fedoraproject.org> 0.97.5-1
- 0.97.5 devel release

* Wed Sep 26 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.97.4-1
- 0.97.4 devel release

* Thu Sep 20 2012 Daniel Drake <dsd@laptop.org> - 0.97.3-1
- New development release

* Thu Sep 13 2012 Daniel Drake <dsd@laptop.org> - 0.97.2-1
- New development release

* Tue Aug 28 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.97.1-1
- 0.97.1 devel release

* Wed Aug 15 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.97.0-1
- 0.97.0 devel release

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.96.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun  6 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.96.4-1
- 0.96.4 stable release

* Tue Jun  5 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.96.3-1
- 0.96.3 stable release

* Sat Jun  2 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.96.2-1
- 0.96.2 stable release

* Sun May 27 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.96.1-2
- Add gettext to Requires

* Sat May  5 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.96.1-1
- 0.96.1 stable release

* Tue Apr 24 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.96.0-1
- 0.96.0 stable release

* Thu Apr 19 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.95.6-1
- devel release 0.95.6

* Fri Mar 23 2012 Simon Schampijer <simon@laptop.org> - 0.95.5-1
- devel release 0.95.5

* Wed Mar 14 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.95.4-1
- devel release 0.95.4

* Mon Feb  6 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.95.3-1
- devel release 0.95.3

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.95.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Dec 24 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 0.95.2-2
- Fix devel dependencies

* Thu Dec 22 2011 Simon Schampijer <simon@laptop.org> - 0.95.2-1
- devel release 0.95.2
- incorporated review comments

* Sun Dec 11 2011 Simon Schampijer <simon@laptop.org> - 0.95.1-1
- devel release 0.95.1
