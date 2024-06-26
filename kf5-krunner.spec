#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeframever	5.116
%define		qtver		5.15.2
%define		kfname		krunner

Summary:	Framework for Plasma runners
Summary(pl.UTF-8):	Szkielet dla uruchamiaczy Plasmy
Name:		kf5-%{kfname}
Version:	5.116.0
Release:	1
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/frameworks/%{kdeframever}/%{kfname}-%{version}.tar.xz
# Source0-md5:	b8f6dbe96d6da138e1a8991c7cebd9b0
URL:		https://kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5DBus-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= %{qtver}
BuildRequires:	Qt5Network-devel >= %{qtver}
BuildRequires:	Qt5Qml-devel >= %{qtver}
BuildRequires:	Qt5Quick-devel >= %{qtver}
BuildRequires:	Qt5Test-devel >= %{qtver}
BuildRequires:	Qt5Widgets-devel >= %{qtver}
BuildRequires:	Qt5Xml-devel >= %{qtver}
BuildRequires:	cmake >= 3.16
BuildRequires:	gettext-devel
BuildRequires:	kf5-attica-devel >= %{version}
BuildRequires:	kf5-extra-cmake-modules >= %{version}
BuildRequires:	kf5-kauth-devel >= %{version}
BuildRequires:	kf5-kbookmarks-devel >= %{version}
BuildRequires:	kf5-kcodecs-devel >= %{version}
BuildRequires:	kf5-kcompletion-devel >= %{version}
BuildRequires:	kf5-kconfig-devel >= %{version}
BuildRequires:	kf5-kconfigwidgets-devel >= %{version}
BuildRequires:	kf5-kcoreaddons-devel >= %{version}
BuildRequires:	kf5-kdbusaddons-devel >= %{version}
BuildRequires:	kf5-kglobalaccel-devel >= %{version}
BuildRequires:	kf5-kguiaddons-devel >= %{version}
BuildRequires:	kf5-ki18n-devel >= %{version}
BuildRequires:	kf5-kiconthemes-devel >= %{version}
BuildRequires:	kf5-kio-devel >= %{version}
BuildRequires:	kf5-kitemviews-devel >= %{version}
BuildRequires:	kf5-kjobwidgets-devel >= %{version}
BuildRequires:	kf5-kservice-devel >= %{version}
BuildRequires:	kf5-ktextwidgets-devel >= %{version}
BuildRequires:	kf5-kwidgetsaddons-devel >= %{version}
BuildRequires:	kf5-kwindowsystem-devel >= %{version}
BuildRequires:	kf5-kxmlgui-devel >= %{version}
BuildRequires:	kf5-plasma-framework-devel >= %{version}
BuildRequires:	kf5-solid-devel >= %{version}
BuildRequires:	kf5-sonnet-devel >= %{version}
BuildRequires:	kf5-threadweaver-devel >= %{version}
BuildRequires:	ninja
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	kf5-dirs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		qt5dir		%{_libdir}/qt5

%description
The Plasma workspace provides an application called KRunner which,
among other things, allows one to type into a text area which causes
various actions and information that match the text appear as the text
is being typed.

One application for this is the universal runner you can launch with
ALT-F2.

This functionality is provided via plugins loaded at runtime called
"Runners". These plugins can be used by any application using the
Plasma library. The KRunner framework is used to write these plugins.

%description -l pl.UTF-8
Środowisko Plasma udostępnia aplikację o nazwie KRunner, która, między
innymi, pozwala na wpisanie tekstu w obszar tekstu, co powoduje różne
akcje, a informacje, które pasują do tekstu, pojawiają się w miarę
jego pisania.

Jedną z takich aplikacji jest uniwersalny uruchamiacz, który można
przywołać poprzez ALT-F2.

Niniejsza funkcjonalność jest zapewniana przez ładowane w trakcie
działania środowiska wtyczki zwane "Uruchamiaczami". Wtyczki te mogą
być używane przez dowolną aplikację przy użyciu biblioteki Plasma.
Szkielet KRunner służy do pisania takich wtyczek.

%package devel
Summary:	Header files for %{kfname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{kfname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	Qt5Core-devel >= %{qtver}
Requires:	Qt5Gui-devel >= %{qtver}
Requires:	kf5-kcoreaddons-devel >= %{version}
Requires:	kf5-kconfig-devel >= %{version}
Requires:	kf5-plasma-framework-devel >= %{version}

%description devel
Header files for %{kfname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{kfname}.

%prep
%setup -q -n %{kfname}-%{version}

%build
%cmake -B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON

%ninja_build -C build

%if %{with tests}
%ninja_build -C build test
%endif


%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README.md
%{_datadir}/qlogging-categories5/krunner.categories
%ghost %{_libdir}/libKF5Runner.so.5
%attr(755,root,root) %{_libdir}/libKF5Runner.so.*.*
%attr(755,root,root) %{_libdir}/qt5/qml/org/kde/runnermodel/librunnermodelplugin.so
%{_libdir}/qt5/qml/org/kde/runnermodel/qmldir
%{_datadir}/kservicetypes5/plasma-runner.desktop
%{_datadir}/dbus-1/interfaces/kf5_org.kde.krunner1.xml
%{_datadir}/qlogging-categories5/krunner.renamecategories
%{_datadir}/kdevappwizard/templates/runner.tar.bz2
%{_datadir}/kdevappwizard/templates/runnerpython.tar.bz2

%files devel
%defattr(644,root,root,755)
%{_includedir}/KF5/KRunner
%{_libdir}/cmake/KF5Runner
%{_libdir}/libKF5Runner.so
%{qt5dir}/mkspecs/modules/qt_KRunner.pri
