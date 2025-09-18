%define major %(echo %{version} |cut -d. -f1-2)
%define stable %([ "$(echo %{version} |cut -d. -f2)" -ge 80 -o "$(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)

%define libname %mklibname KF6DAV
%define devname %mklibname KF6DAV -d
#define git 20240217

Name: kf6-kdav
Version: 6.18.0
Release: %{?git:0.%{git}.}1
%if 0%{?git:1}
Source0: https://invent.kde.org/frameworks/kdav/-/archive/master/kdav-master.tar.bz2#/kdav-%{git}.tar.bz2
%else
Source0: https://download.kde.org/%{stable}/frameworks/%{major}/kdav-%{version}.tar.xz
%endif
Summary: DAV protocol implementation with KJobs
URL: https://invent.kde.org/frameworks/kdav
License: CC0-1.0 LGPL-2.0+ LGPL-2.1 LGPL-3.0
Group: System/Libraries
BuildRequires: cmake
BuildRequires: cmake(ECM)
BuildRequires: python
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6QmlTools)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6GuiTools)
BuildRequires: cmake(Qt6QuickTest)
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: gettext
BuildRequires: doxygen
BuildRequires: cmake(Qt6ToolsTools)
BuildRequires: cmake(Qt6)
BuildRequires: cmake(Qt6QuickTest)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6I18n)
Requires: %{libname} = %{EVRD}

%description
DAV protocol implementation with KJobs

%package -n %{libname}
Summary: DAV protocol implementation with KJobs
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libname}
DAV protocol implementation with KJobs

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

DAV protocol implementation with KJobs

%prep
%autosetup -p1 -n kdav-%{?git:master}%{!?git:%{version}}
%cmake \
	-DBUILD_QCH:BOOL=ON \
	-DBUILD_WITH_QT6:BOOL=ON \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%find_lang %{name} --all-name --with-qt --with-html

%files -f %{name}.lang
%{_datadir}/qlogging-categories6/kdav.*

%files -n %{devname}
%{_includedir}/KF6/KDAV
%{_libdir}/cmake/KF6DAV

%files -n %{libname}
%{_libdir}/libKF6DAV.so*
