%define fuseversion 2.5.2

Summary: 	Tool used to mount local media on an Xterminal from the terminals serveur	
Name:		ltspfs
Version:	0.1
Release:	%mkrel 1
License:	GPL
Group:		System/Servers
URL:		http://wiki.ltsp.org/twiki/bin/view/Ltsp/LtspFS
Source:		%{name}-%{version}.tar.bz2
BuildRequires:	libfuse-devel >= %{fuseversion}
Requires:	fuse >= %{fuseversion}

%description
ltspfs is a remote filesystem consisting of two parts: 
  1) A network server daemon that runs on the LTSP terminal.
  2) A FUSE module that runs in user-space on the server, that connects with
     the daemon on the client.

The goals of ltspfs are:

   1. Provide a lightweight file access mechanism that will be feasable on
      lower end hardware.
   2. Provide a stateless file access method that will feature "atomic" reads
      and writes to minimize impact from client network disruptions.
   3. Provide a network filesystem that handles client reboots and
      disconnections in a manner that doesn't leave inaccesible, unmountable
      filesystems on the LTSP server.
   4. Provide a network filesystem that can easily handle the oddities of
      dealing with removable media, and integrate well with udev (LTSP's
      preferred device handling support).

%prep

%setup -q 

%build
rm -rf .deps autom4te.cache

%configure2_5x

%make  

%install
rm -rf %{buildroot}

%makeinstall 

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog README
%attr(0755,root,root) %{_bindir}/%{name}


