%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary:	KDE calendar and scheduling component
Name:		plasma6-korganizer
Version:	24.01.85
Release:	1
Epoch:		3
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://www.kde.org
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/korganizer-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:	pkgconfig(Qt6DBus)
BuildRequires:	pkgconfig(Qt6Gui)
BuildRequires:	pkgconfig(Qt6Widgets)
BuildRequires:	pkgconfig(Qt6Test)
BuildRequires:	pkgconfig(Qt6UiTools)
BuildRequires:	cmake(KPim6AkonadiSearch)
BuildRequires:	cmake(KPim6AkonadiContact)
BuildRequires:	cmake(KF6Codecs)
BuildRequires:	cmake(KF6Completion)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6ConfigWidgets)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6Crash)
BuildRequires:	cmake(KF6DBusAddons)
BuildRequires:	cmake(KF6DocTools)
BuildRequires:	cmake(KF6IconThemes)
BuildRequires:	cmake(KF6ItemViews)
BuildRequires:	cmake(KF6JobWidgets)
BuildRequires:	cmake(KF6KCMUtils)
BuildRequires:	cmake(KF6NewStuff)
BuildRequires:	cmake(KF6Parts)
BuildRequires:	cmake(KF6Service)
BuildRequires:	cmake(KF6WidgetsAddons)
BuildRequires:	cmake(KF6WindowSystem)
BuildRequires:	cmake(KF6XmlGui)
BuildRequires:	cmake(KF6PimTextEdit)
BuildRequires:	cmake(KF6Akonadi)
BuildRequires:	cmake(KF6Contacts)
BuildRequires:	cmake(KF6CalendarCore)
BuildRequires:	cmake(KPim6IdentityManagement)
BuildRequires:	cmake(KPim6MailTransport)
BuildRequires:	cmake(KPim6AkonadiMime)
BuildRequires:	cmake(KPim6CalendarUtils)
BuildRequires:	cmake(KF6Notifications)
BuildRequires:	cmake(KF6Holidays)
BuildRequires:	cmake(KPim6Ldap)
BuildRequires:	cmake(KPim6AkonadiCalendar)
BuildRequires:	cmake(Phonon4Qt6)
BuildRequires:	cmake(KPim6KontactInterface)
BuildRequires:	cmake(KPim6Mime)
BuildRequires:	cmake(KPim6AkonadiNotes)
BuildRequires:	cmake(KPim6PimCommonAkonadi)
BuildRequires:	cmake(KPim6IncidenceEditor)
BuildRequires:	cmake(KPim6CalendarSupport)
BuildRequires:	cmake(KPim6EventViews)
BuildRequires:	cmake(KUserFeedback)
BuildRequires:	cmake(KPim6Libkdepim)
BuildRequires:	boost-devel
BuildRequires:	sasl-devel
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xext)
Requires:	akonadi-calendar-tools
Requires:	kdepim-runtime
Suggests:	kdepim-addons
Conflicts:	kontact < 3:17.04.0

%description
KOrganizer provides management of events and tasks, alarm notification,
web export, network transparent handling of data, group scheduling,
import and export of calendar files and more. It is able to work together
with a wide variety of groupware servers, for example Kolab, Open-Xchange,
Citadel or OpenGroupware.org.

%files -f all.lang
%{_kde6_applicationsdir}/korganizer-import.desktop
%{_kde6_applicationsdir}/org.kde.korganizer.desktop
%{_bindir}/korganizer
%{_datadir}/config.kcfg/korganizer.kcfg
%dir %{_datadir}/korganizer/
%{_datadir}/korganizer/*
%{_docdir}/*/*/korganizer
%{_iconsdir}/hicolor/*/apps/korganizer.*
%{_iconsdir}/hicolor/*/apps/korg-journal.*
%{_iconsdir}/hicolor/*/apps/korg-todo.*
%{_iconsdir}/hicolor/*/apps/quickview.*
%{_datadir}/dbus-1/services/org.kde.korganizer.service
%{_datadir}/qlogging-categories6/korganizer.categories
%{_datadir}/qlogging-categories6/korganizer.renamecategories
%{_datadir}/knsrcfiles/korganizer.knsrc
%{_datadir}/metainfo/org.kde.korganizer.appdata.xml
%{_datadir}/dbus-1/interfaces/org.kde.korganizer.Korganizer.xml
%{_datadir}/dbus-1/interfaces/org.kde.Korganizer.Calendar.xml
%{_qt6_plugindir}/pim6/kcms/korganizer/korganizer_configcolorsandfonts.so
%{_qt6_plugindir}/pim6/kcms/korganizer/korganizer_configdesignerfields.so
%{_qt6_plugindir}/pim6/kcms/korganizer/korganizer_configfreebusy.so
%{_qt6_plugindir}/pim6/kcms/korganizer/korganizer_configgroupscheduling.so
%{_qt6_plugindir}/pim6/kcms/korganizer/korganizer_configmain.so
%{_qt6_plugindir}/pim6/kcms/korganizer/korganizer_configplugins.so
%{_qt6_plugindir}/pim6/kcms/korganizer/korganizer_configtime.so
%{_qt6_plugindir}/pim6/kcms/korganizer/korganizer_configviews.so
%{_qt6_plugindir}/pim6/kcms/korganizer/korganizer_userfeedback.so
%{_qt6_plugindir}/pim6/kcms/summary/kcmapptsummary.so
%{_qt6_plugindir}/pim6/kcms/summary/kcmsdsummary.so
%{_qt6_plugindir}/pim6/kcms/summary/kcmtodosummary.so
%{_qt6_plugindir}/pim6/kontact/kontact_journalplugin.so
%{_qt6_plugindir}/pim6/kontact/kontact_korganizerplugin.so
%{_qt6_plugindir}/pim6/kontact/kontact_specialdatesplugin.so
%{_qt6_plugindir}/pim6/kontact/kontact_todoplugin.so
%{_qt6_plugindir}/korganizerpart.so
%{_datadir}/applications/korganizer-view.desktop

#----------------------------------------------------------------------------

%define korganizer_core_major 6
%define libkorganizer_core %mklibname korganizer_core %{korganizer_core_major}

%package -n %{libkorganizer_core}
Summary:	KDE PIM shared library
Group:		System/Libraries

%description -n %{libkorganizer_core}
KDE PIM shared library.

%files -n %{libkorganizer_core}
%{_libdir}/libkorganizer_core.so.%{korganizer_core_major}*

#----------------------------------------------------------------------------

%define korganizer_interfaces_major 6
%define libkorganizer_interfaces %mklibname korganizer_interfaces %{korganizer_interfaces_major}

%package -n %{libkorganizer_interfaces}
Summary:	KDE PIM shared library
Group:		System/Libraries

%description -n %{libkorganizer_interfaces}
KDE PIM shared library.

%files -n %{libkorganizer_interfaces}
%{_libdir}/libkorganizer_interfaces.so.%{korganizer_interfaces_major}*

#----------------------------------------------------------------------------

%define korganizerprivate_major 6
%define libkorganizerprivate %mklibname korganizerprivate %{korganizerprivate_major}

%package -n %{libkorganizerprivate}
Summary:	KDE PIM shared library
Group:		System/Libraries

%description -n %{libkorganizerprivate}
KDE PIM shared library.

%files -n %{libkorganizerprivate}
%{_libdir}/libkorganizerprivate.so.%{korganizerprivate_major}*

#----------------------------------------------------------------------

%prep
%autosetup -p1
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja -C build

%install
%ninja_install -C build

rm -rf %{buildroot}%{_kde6_libdir}/libkorganizer_core.so
rm -rf %{buildroot}%{_kde6_libdir}/libkorganizer_interfaces.so

%find_lang %{name}

cat *.lang >all.lang
