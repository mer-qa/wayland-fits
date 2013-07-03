Name:           wayland-fits
Version:        0.0.1
Release:        1
Summary:        Wayland Functional Integration Test Suite
Source0:        %{name}-%{version}.tar.gz
Group:          Development/Tools
License:        BSD
URL:            http://github.com/01org/wayland-fits

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  make
BuildRequires:  check-devel >= 0.9.8
BuildRequires:  wayland-devel >= 1.0.6
BuildRequires:  mesa-llvmpipe-libwayland-egl-devel
BuildRequires:  boost-devel >= 1.48.0

Requires:       boost-program-options >= 1.48.0
Requires:       boost-regex >= 1.48.0
Requires:       boost-filesystem >= 1.48.0
Requires:       boost-system >= 1.48.0
Requires:       check >= 0.9.8
Requires:       wayland >= 1.0.6

%description
Wayland-fits is a fully automated functional integration test suite.  It's
main purpose is to test the functionality and integration of client-side
(i.e. toolkit) and server-side (compositor) implementations of the Wayland
protocol.  It includes tests that validate user input events originating from
the server-side or from an emulated system-level device (depends on the type
of backend used).  There are also tests with emphasis on cross-validating client
and server states.

%prep
%setup -q

%build
cd wfits
./autogen.sh --prefix=/usr
make

%install
make -C wfits DESTDIR=$RPM_BUILD_ROOT install

%files
%defattr(-,root,root,-)
%doc wfits/COPYING wfits/README
/usr/bin/wfits
