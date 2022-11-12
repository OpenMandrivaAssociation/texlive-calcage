Name:		texlive-calcage
Version:	27725
Release:	1
Summary:	Calculate the age of something, in years
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/calcage
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/calcage.r27725.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/calcage.doc.r27725.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/calcage.source.r27725.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package calculates the age of someone or something in
years. Internally it uses the datenumber package to calculate
the age in days; conversion from days to years is then
performed, taking care of leap years and such odd things.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/calcage/calcage.sty
%doc %{_texmfdistdir}/doc/latex/calcage/README
%doc %{_texmfdistdir}/doc/latex/calcage/calcage.pdf
#- source
%doc %{_texmfdistdir}/source/latex/calcage/calcage.dtx
%doc %{_texmfdistdir}/source/latex/calcage/calcage.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
