# Rust packages always list license files and docs
# inside the crate as well as the containing directory
%undefine _duplicate_files_terminate_build
%bcond_without check
%global debug_package %{nil}

%global crate roxmltree

Name:           rust-roxmltree
Version:        0.20.0
Release:        1
Summary:        Represent an XML as a read-only tree
Group:          Development/Rust

License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/roxmltree
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}

BuildRequires:  cargo-rpm-macros >= 24
BuildRequires:  rust >= 1.60

%global _description %{expand:
Represent an XML as a read-only tree.}

%description %{_description}

%package        devel
Summary:        %{summary}
Group:          Development/Rust
BuildArch:      noarch
Provides:       crate(roxmltree) = 0.20.0
Requires:       cargo
Requires:       rust >= 1.60

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE-APACHE
%license %{crate_instdir}/LICENSE-MIT
%doc %{crate_instdir}/CHANGELOG.md
%doc %{crate_instdir}/README.md
%{crate_instdir}/

%package     -n %{name}+default-devel
Summary:        %{summary}
Group:          Development/Rust
BuildArch:      noarch
Provides:       crate(roxmltree/default) = 0.20.0
Requires:       cargo
Requires:       crate(roxmltree) = 0.20.0
Requires:       crate(roxmltree/positions) = 0.20.0
Requires:       crate(roxmltree/std) = 0.20.0

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+positions-devel
Summary:        %{summary}
Group:          Development/Rust
BuildArch:      noarch
Provides:       crate(roxmltree/positions) = 0.20.0
Requires:       cargo
Requires:       crate(roxmltree) = 0.20.0

%description -n %{name}+positions-devel %{_description}

This package contains library source intended for building other packages which
use the "positions" feature of the "%{crate}" crate.

%files       -n %{name}+positions-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+std-devel
Summary:        %{summary}
Group:          Development/Rust
BuildArch:      noarch
Provides:       crate(roxmltree/std) = 0.20.0
Requires:       cargo
Requires:       crate(roxmltree) = 0.20.0

%description -n %{name}+std-devel %{_description}

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%files       -n %{name}+std-devel
%ghost %{crate_instdir}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version} -p1
%cargo_prep

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif
