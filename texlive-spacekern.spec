%global tl_name spacekern
%global tl_revision 78632

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.3
Release:	%{tl_revision}.1
Summary:	Kerning between words and against space
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/luatex/latex/spacekern
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/spacekern.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/spacekern.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides two shorthands for typesetting breaking and non-
breaking small spaces, where both hyphenation and kerning against space
are correctly applied. Additionally, interword kerning can be applied.

