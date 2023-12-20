Name:		texlive-spacekern
Version:	67604
Release:	1
Summary:	Kerning between words and against space
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/spacekern
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/spacekern.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/spacekern.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides two shorthands for typesetting breaking
and non-breaking small spaces, where both hyphenation and
kerning against space are correctly applied. Additionally,
interword kerning can be applied.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/lualatex/spacekern
%doc %{_texmfdistdir}/doc/lualatex/spacekern

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
