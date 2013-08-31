# rpmbuild

The various build environments used to make the rpms in the rpmrepo project.
These are all designed to be built on a CentOS 6 installation.

# Usage

Each directory in the top level (for instance `nginxbuild`) is its own rpmbuild
environment. To compile the rpms/srpms for a project:

```
cd /path/to/rpmbuild/nginxbuild
rpmbuild --define "_topdir /path/to/rpmbuild/nginxbuild" -ba SPECS/nginx.spec
```
