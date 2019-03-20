%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary:	KDE calendar and scheduling component
Name:		korganizer
Version:	18.12.3
Release:	2
Epoch:		3
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://www.kde.org
Source0:	http://download.kde.org/%{stable}/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:	pkgconfig(Qt5DBus)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5Test)
BuildRequires:	pkgconfig(Qt5UiTools)
BuildRequires:	cmake(KF5AkonadiSearch)
BuildRequires:	cmake(KF5AkonadiContact)
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
BuildRequires:	cmake(KF5IdentityManagement)
BuildRequires:	cmake(KF5MailTransportAkonadi)
BuildRequires:	cmake(KF5AkonadiMime)
BuildRequires:	cmake(KF5CalendarUtils)
BuildRequires:	cmake(KF5Notifications)
BuildRequires:	cmake(KF5Holidays)
BuildRequires:	cmake(KF5Ldap)
BuildRequires:	cmake(KF5AkonadiCalendar)
BuildRequires:	cmake(Phonon4Qt5)
BuildRequires:	cmake(KF5KontactInterface)
BuildRequires:	cmake(KF5Mime)
BuildRequires:	cmake(KF5AkonadiNotes)
BuildRequires:	cmake(KF5KdepimDBusInterfaces)
BuildRequires:	cmake(KF5PimCommonAkonadi)
BuildRequires:	cmake(KF5LibkdepimAkonadi)
BuildRequires:	cmake(KF5IncidenceEditor)
BuildRequires:	cmake(KF5CalendarSupport)
BuildRequires:	cmake(KF5EventViews)
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
%{_kde5_autostart}/org.kde.korgac.desktop
%{_bindir}/korgac
%{_bindir}/korganizer
%{_datadir}/config.kcfg/korganizer.kcfg
%{_datadir}/kconf_update/korganizer*
%{_datadir}/kontact/ksettingsdialog/korganizer.setdlg
%{_datadir}/kontact/ksettingsdialog/specialdates.setdlg
%dir %{_datadir}/korgac/
%{_datadir}/korgac/*
%dir %{_datadir}/korganizer/
%{_datadir}/korganizer/*
%{_docdir}/*/*/korganizer
%{_iconsdir}/hicolor/*/apps/korganizer.*
%{_iconsdir}/hicolor/*/apps/korg-journal.*
%{_iconsdir}/hicolor/*/apps/korg-todo.*
%{_iconsdir}/hicolor/*/apps/quickview.*
%{_iconsdir}/oxygen/*/actions/checkmark.*
%{_iconsdir}/oxygen/*/actions/smallclock.*
%{_iconsdir}/oxygen/*/actions/upindicator.*
%{_kde5_services}/kcmapptsummary.desktop
%{_kde5_services}/kcmsdsummary.desktop
%{_kde5_services}/kcmtodosummary.desktop
%{_kde5_services}/kontact/journalplugin.desktop
%{_kde5_services}/kontact/korganizerplugin.desktop
%{_kde5_services}/kontact/specialdatesplugin.desktop
%{_kde5_services}/kontact/todoplugin.desktop
%{_kde5_services}/korganizer_*.desktop
%{_kde5_services}/webcal.protocol
%{_kde5_servicetypes}/dbuscalendar.desktop
%{_sysconfdir}/xdg/korganizer.categories
%{_sysconfdir}/xdg/korganizer.renamecategories
%{_sysconfdir}/xdg/korganizer.knsrc
%{_datadir}/metainfo/org.kde.korganizer.appdata.xml
%{_datadir}/dbus-1/interfaces/org.kde.korganizer.KOrgac.xml
%{_datadir}/dbus-1/interfaces/org.kde.korganizer.Korganizer.xml
%{_datadir}/dbus-1/interfaces/org.kde.Korganizer.Calendar.xml
%{_qt5_plugindir}/kcm_apptsummary.so
%{_qt5_plugindir}/kcm_korganizer.so
%{_qt5_plugindir}/kcm_sdsummary.so
%{_qt5_plugindir}/kcm_todosummary.so
%{_qt5_plugindir}/kontact_journalplugin.so
%{_qt5_plugindir}/kontact_korganizerplugin.so
%{_qt5_plugindir}/kontact_specialdatesplugin.so
%{_qt5_plugindir}/kontact_todoplugin.so
%{_qt5_plugindir}/korganizerpart.so

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
%setup -q
%apply_patches
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

rm -rf %{buildroot}%{_kde5_libdir}/libkorganizer_core.so
rm -rf %{buildroot}%{_kde5_libdir}/libkorganizer_interfaces.so

%find_lang %{name}
%find_lang korgac

cat *.lang >all.lang
