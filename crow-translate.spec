%global debug_package %{nil}

Name:		crow-translate
Version:	3.1.0
Release:	1
Source0:	https://download.kde.org/stable/%{name}/%{version}/%{name}-v%{version}.tar.gz
Summary:	A simple and lightweight translator
URL:		https://apps.kde.org/crowtranslate/
License:	GPL-3.0-only AND GPL-3.0-or-later AND BSD-3-Clause AND MIT
Group:		KDE/Application

BuildSystem:	cmake
BuildRequires:	cmake
BuildRequires:	extra-cmake-modules
BuildRequires:	cmake(Qt5)
BuildRequires:	cmake(Qt5Network)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(Qt5X11Extras)
BuildRequires:	cmake(Qt5Multimedia)
BuildRequires:	cmake(Qt5LinguistTools)
BuildRequires:	cmake(Qt5Concurrent)
BuildRequires:	cmake(tesseract)
BuildRequires:	cmake(qt5dbus)
BuildRequires:	cmake(KF5Wayland)

Requires: hicolor-icon-theme

Recommends: gstreamer1.0-plugins-good

Provides: bundled(qonlinetranslator)
Provides: bundled(qhotkey)
Provides: bundled(qtaskbarcontrol)
Provides: bundled(singleapplication)
%description
%summary

%prep
%autosetup -n %{name}-v%{version} -p1
rm -r src/qgittag

%files
%license LICENSES/*
%doc README.md
%{_bindir}/crow
%{_localedir}/*
%{_iconsdir}/hicolor/*/*/*.png
%{_iconsdir}/hicolor/scalable/*/*.svg
%{_datadir}/applications/*.desktop
%{_metainfodir}/*
