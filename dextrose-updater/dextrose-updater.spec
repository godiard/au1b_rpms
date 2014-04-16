Name:	dextrose-updater	
Version:	5
Release:	9.olpcau%{?dist}
Summary:	A yum based updater for sugar-dextrose. Updates the sugar-dextrose related packages automatically and emits dbus messages (for the sugar notification system, if installed)

Group:		Applications/Updating
License:	GPLv3
URL:		http://wiki.sugarlabs.org/go/Dextrose/Updater
Source0:	%{name}-%{version}.tar.gz
Patch0:     change_last_update_flag_file.diff
Patch1:     networkmanager_hook.diff
Patch2:     modify_yum_conf.diff
Patch3:     clean_yum_caches.diff

BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildArch:	noarch

Packager: Gonzalo Odiard <godiard@sugarlabs.org>

%description

A yum based updater for sugar-dextrose. Updates the sugar-dextrose related packages automatically and emits dbus messages (for the sugar notification system, if installed)

%prep
%setup -q
%patch0 -p1 -b .flag_file
%patch1 -p1 -b .networkmanager
%patch2 -p1 -b .proxy
%patch3 -p1 -b .clean_cache

%build

%install
rm -rf $RPM_BUILD_ROOT

make DESTDIR=%{buildroot} REPO="au1b-updates" install
chmod 755 %{buildroot}/etc/NetworkManager/dispatcher.d/dextrose-updater-ifup


%clean
rm -rf $RPM_BUILD_ROOT
rm -rf $RPM_BUILD_DIR/%{name}-%{version}

%files
%defattr(-,root,root,-)
%doc 

/usr/sbin/dextrose-updater
%config(noreplace) /etc/sysconfig/dextrose-updater
/etc/NetworkManager/dispatcher.d/dextrose-updater-ifup

%changelog
* Tue Feb 15 2011 Anish Mangal <anish@sugarlabs.org> 5-1
- Bump version, fix Source0, download url

* Tue Feb 15 2011 Anish Mangal <anish@sugarlabs.org> 4-1
- Interpret check-update exit status correctly (alsroot)
- Remove stampfile at the beginning; touch it only successful exit (alsroot)
- More conveninet installer; install cron task (alsroot)
- Keep all metadata in Makefile

* Mon Feb 14 2011 Anish Mangal <anish@sugarlabs.org> 3-1
- Do not re-create logfile on checking update (alsroot)

* Thu Feb  3 2011 Anish Mangal <anish@sugarlabs.org> 2-1
- Keep trying every hour until yum returns an exit code (alsroot)

* Wed Jan 19 2011 Aleksey Lim <alsroot@member.fsf.org> 1-8
- Check daily updates hourly.

* Mon Jan 10 2011 Anish Mangal <anish@sugarlabs.org> 1-6
- Remove dextrose-py and change path of config file from /etc/default to /etc/sysconfig.

* Mon Jan 03 2011 Anish Mangal <anish@sugarlabs.org> 1-5
- Add dextrose-py to the list of repos to update from.

* Wed Dec 22 2010 Anish Mangal <anish@sugarlabs.org> 1-4
- Remove post, postun sections and handle symlink in install and file sections.

* Wed Dec 22 2010 Anish Mangal <anish@sugarlabs.org> 1-3
- Remove cron job after removing

* Wed Dec 22 2010 Anish Mangal <anish@sugarlabs.org> 1-2
- Add cron job

* Wed Dec 22 2010 Anish Mangal <anish@sugarlabs.org> 1-1
- Initial rpm version
