%global tl_name calcage
%global tl_revision 27725

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.90
Release:	%{tl_revision}.1
Summary:	Calculate the age of something, in years
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/calcage
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/calcage.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/calcage.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/calcage.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package calculates the age of someone or something in years.
Internally it uses the datenumber package to calculate the age in days;
conversion from days to years is then performed, taking care of leap
years and such odd things.

