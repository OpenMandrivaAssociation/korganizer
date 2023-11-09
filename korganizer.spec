%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary:	KDE calendar and scheduling component
Name:		korganizer
Version:	23.08.3
Release:	1
Epoch:		3
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://www.kde.org
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:	pkgconfig(Qt5DBus)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5Test)
BuildRequires:	pkgconfig(Qt5UiTools)
BuildRequires:	cmake(KPim5AkonadiSearch)
BuildRequires:	cmake(KPim5AkonadiContact)
BuildRequires:	cmake(KF5Codecs)
BuildRequires:	cmake(KF5Completion)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5ConfigWidgets)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5Crash)
BuildRequires:	cmake(KF5DBusAddons)
BuildRequires:	cmake(KF5DocTools)
BuildRequires:	cmake(KF5IconThemes)
BuildRequires:	cmake(KF5ItemViews)
BuildRequires:	cmake(KF5JobWidgets)
BuildRequires:	cmake(KF5KCMUtils)
BuildRequires:	cmake(KF5NewStuff)
BuildRequires:	cmake(KF5Parts)
BuildRequires:	cmake(KF5Service)
BuildRequires:	cmake(KF5WidgetsAddons)
BuildRequires:	cmake(KF5WindowSystem)
BuildRequires:	cmake(KF5XmlGui)
BuildRequires:	cmake(KF5PimTextEdit)
BuildRequires:	cmake(KF5Akonadi)
BuildRequires:	cmake(KF5Contacts)
BuildRequires:	cmake(KF5CalendarCore)
BuildRequires:	cmake(KPim5IdentityManagement)
BuildRequires:	cmake(KPim5MailTransport)
BuildRequires:	cmake(KPim5AkonadiMime)
BuildRequires:	cmake(KPim5CalendarUtils)
BuildRequires:	cmake(KF5Notifications)
BuildRequires:	cmake(KF5Holidays)
BuildRequires:	cmake(KPim5Ldap)
BuildRequires:	cmake(KPim5AkonadiCalendar)
BuildRequires:	cmake(Phonon4Qt5)
BuildRequires:	cmake(KPim5KontactInterface)
BuildRequires:	cmake(KPim5Mime)
BuildRequires:	cmake(KPim5AkonadiNotes)
BuildRequires:	cmake(KPim5PimCommonAkonadi)
BuildRequires:	cmake(KPim5IncidenceEditor)
BuildRequires:	cmake(KPim5CalendarSupport)
BuildRequires:	cmake(KPim5EventViews)
BuildRequires:	cmake(KUserFeedback)
BuildRequires:	cmake(KPim5Libkdepim)
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
%{_kde5_applicationsdir}/korganizer-import.desktop
%{_kde5_applicationsdir}/org.kde.korganizer.desktop
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
%{_datadir}/qlogging-categories5/korganizer.categories
%{_datadir}/qlogging-categories5/korganizer.renamecategories
%{_datadir}/knsrcfiles/korganizer.knsrc
%{_datadir}/metainfo/org.kde.korganizer.appdata.xml
%{_datadir}/dbus-1/interfaces/org.kde.korganizer.Korganizer.xml
%{_datadir}/dbus-1/interfaces/org.kde.Korganizer.Calendar.xml
%{_qt5_plugindir}/pim5/kcms/korganizer/korganizer_configcolorsandfonts.so
%{_qt5_plugindir}/pim5/kcms/korganizer/korganizer_configdesignerfields.so
%{_qt5_plugindir}/pim5/kcms/korganizer/korganizer_configfreebusy.so
%{_qt5_plugindir}/pim5/kcms/korganizer/korganizer_configgroupscheduling.so
%{_qt5_plugindir}/pim5/kcms/korganizer/korganizer_configmain.so
%{_qt5_plugindir}/pim5/kcms/korganizer/korganizer_configplugins.so
%{_qt5_plugindir}/pim5/kcms/korganizer/korganizer_configtime.so
%{_qt5_plugindir}/pim5/kcms/korganizer/korganizer_configviews.so
%{_qt5_plugindir}/pim5/kcms/korganizer/korganizer_userfeedback.so
%{_qt5_plugindir}/pim5/kcms/summary/kcmapptsummary.so
%{_qt5_plugindir}/pim5/kcms/summary/kcmsdsummary.so
%{_qt5_plugindir}/pim5/kcms/summary/kcmtodosummary.so
%{_qt5_plugindir}/pim5/kontact/kontact_journalplugin.so
%{_qt5_plugindir}/pim5/kontact/kontact_korganizerplugin.so
%{_qt5_plugindir}/pim5/kontact/kontact_specialdatesplugin.so
%{_qt5_plugindir}/pim5/kontact/kontact_todoplugin.so
%{_qt5_plugindir}/korganizerpart.so
%{_datadir}/applications/korganizer-view.desktop

#----------------------------------------------------------------------------

%define korganizer_core_major 5
%define libkorganizer_core %mklibname korganizer_core %{korganizer_core_major}

%package -n %{libkorganizer_core}
Summary:	KDE PIM shared library
Group:		System/Libraries

%description -n %{libkorganizer_core}
KDE PIM shared library.

%files -n %{libkorganizer_core}
%{_libdir}/libkorganizer_core.so.%{korganizer_core_major}*

#----------------------------------------------------------------------------

%define korganizer_interfaces_major 5
%define libkorganizer_interfaces %mklibname korganizer_interfaces %{korganizer_interfaces_major}

%package -n %{libkorganizer_interfaces}
Summary:	KDE PIM shared library
Group:		System/Libraries

%description -n %{libkorganizer_interfaces}
KDE PIM shared library.

%files -n %{libkorganizer_interfaces}
%{_libdir}/libkorganizer_interfaces.so.%{korganizer_interfaces_major}*

#----------------------------------------------------------------------------

%define korganizerprivate_major 5
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
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

rm -rf %{buildroot}%{_kde5_libdir}/libkorganizer_core.so
rm -rf %{buildroot}%{_kde5_libdir}/libkorganizer_interfaces.so

%find_lang %{name}

cat *.lang >all.lang
