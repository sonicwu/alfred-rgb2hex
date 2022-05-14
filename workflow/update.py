#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2014 Fabio Niephaus <fabio.niephaus@gmail.com>,
#       Dean Jackson <deanishe@deanishe.net>
#
# MIT Licence. See http://opensource.org/licenses/MIT
#
# Created on 2014-08-16
#

"""Self-updating from GitHub.

.. versionadded:: 1.9

.. note::

   This module is not intended to be used directly. Automatic updates
   are controlled by the ``update_settings`` :class:`dict` passed to
   :class:`~workflow.workflow.Workflow` objects.

"""

<<<<<<< HEAD

import json
import os
import re
import subprocess
import tempfile
from collections import defaultdict
from functools import total_ordering
from itertools import zip_longest
from urllib import request

from workflow.util import atomic_writer

from . import workflow
=======
from __future__ import print_function, unicode_literals

from collections import defaultdict
from functools import total_ordering
import json
import os
import tempfile
import re
import subprocess

import workflow
import web
>>>>>>> 62b1f663a30cba5a4712a37c2c375cf8ad81cb4a

# __all__ = []


<<<<<<< HEAD
RELEASES_BASE = "https://api.github.com/repos/{}/releases"
match_workflow = re.compile(r"\.alfred(\d+)?workflow$").search
=======
RELEASES_BASE = 'https://api.github.com/repos/{}/releases'
match_workflow = re.compile(r'\.alfred(\d+)?workflow$').search
>>>>>>> 62b1f663a30cba5a4712a37c2c375cf8ad81cb4a

_wf = None


def wf():
    """Lazy `Workflow` object."""
    global _wf
    if _wf is None:
        _wf = workflow.Workflow()
    return _wf


@total_ordering
class Download(object):
    """A workflow file that is available for download.

    .. versionadded: 1.37

    Attributes:
        url (str): URL of workflow file.
        filename (str): Filename of workflow file.
        version (Version): Semantic version of workflow.
        prerelease (bool): Whether version is a pre-release.
        alfred_version (Version): Minimum compatible version
            of Alfred.

    """

    @classmethod
    def from_dict(cls, d):
        """Create a `Download` from a `dict`."""
<<<<<<< HEAD
        return cls(
            url=d["url"],
            filename=d["filename"],
            version=Version(d["version"]),
            prerelease=d["prerelease"],
        )
=======
        return cls(url=d['url'], filename=d['filename'],
                   version=Version(d['version']),
                   prerelease=d['prerelease'])
>>>>>>> 62b1f663a30cba5a4712a37c2c375cf8ad81cb4a

    @classmethod
    def from_releases(cls, js):
        """Extract downloads from GitHub releases.

        Searches releases with semantic tags for assets with
        file extension .alfredworkflow or .alfredXworkflow where
        X is a number.

        Files are returned sorted by latest version first. Any
        releases containing multiple files with the same (workflow)
        extension are rejected as ambiguous.

        Args:
            js (str): JSON response from GitHub's releases endpoint.

        Returns:
            list: Sequence of `Download`.
        """
        releases = json.loads(js)
        downloads = []
        for release in releases:
<<<<<<< HEAD
            tag = release["tag_name"]
=======
            tag = release['tag_name']
>>>>>>> 62b1f663a30cba5a4712a37c2c375cf8ad81cb4a
            dupes = defaultdict(int)
            try:
                version = Version(tag)
            except ValueError as err:
<<<<<<< HEAD
                wf().logger.debug('ignored release: bad version "%s": %s', tag, err)
                continue

            dls = []
            for asset in release.get("assets", []):
                url = asset.get("browser_download_url")
                filename = os.path.basename(url)
                m = match_workflow(filename)
                if not m:
                    wf().logger.debug("unwanted file: %s", filename)
=======
                wf().logger.debug('ignored release: bad version "%s": %s',
                                  tag, err)
                continue

            dls = []
            for asset in release.get('assets', []):
                url = asset.get('browser_download_url')
                filename = os.path.basename(url)
                m = match_workflow(filename)
                if not m:
                    wf().logger.debug('unwanted file: %s', filename)
>>>>>>> 62b1f663a30cba5a4712a37c2c375cf8ad81cb4a
                    continue

                ext = m.group(0)
                dupes[ext] = dupes[ext] + 1
<<<<<<< HEAD
                dls.append(Download(url, filename, version, release["prerelease"]))

            valid = True
            for ext, n in list(dupes.items()):
                if n > 1:
                    wf().logger.debug(
                        'ignored release "%s": multiple assets ' 'with extension "%s"',
                        tag,
                        ext,
                    )
=======
                dls.append(Download(url, filename, version,
                                    release['prerelease']))

            valid = True
            for ext, n in dupes.items():
                if n > 1:
                    wf().logger.debug('ignored release "%s": multiple assets '
                                      'with extension "%s"', tag, ext)
>>>>>>> 62b1f663a30cba5a4712a37c2c375cf8ad81cb4a
                    valid = False
                    break

            if valid:
                downloads.extend(dls)

        downloads.sort(reverse=True)
        return downloads

    def __init__(self, url, filename, version, prerelease=False):
        """Create a new Download.

        Args:
            url (str): URL of workflow file.
            filename (str): Filename of workflow file.
            version (Version): Version of workflow.
            prerelease (bool, optional): Whether version is
                pre-release. Defaults to False.

        """
<<<<<<< HEAD
        if isinstance(version, str):
=======
        if isinstance(version, basestring):
>>>>>>> 62b1f663a30cba5a4712a37c2c375cf8ad81cb4a
            version = Version(version)

        self.url = url
        self.filename = filename
        self.version = version
        self.prerelease = prerelease

    @property
    def alfred_version(self):
        """Minimum Alfred version based on filename extension."""
        m = match_workflow(self.filename)
        if not m or not m.group(1):
<<<<<<< HEAD
            return Version("0")
=======
            return Version('0')
>>>>>>> 62b1f663a30cba5a4712a37c2c375cf8ad81cb4a
        return Version(m.group(1))

    @property
    def dict(self):
        """Convert `Download` to `dict`."""
<<<<<<< HEAD
        return dict(
            url=self.url,
            filename=self.filename,
            version=str(self.version),
            prerelease=self.prerelease,
        )

    def __str__(self):
        """Format `Download` for printing."""
        return (
            "Download("
            "url={dl.url!r}, "
            "filename={dl.filename!r}, "
            "version={dl.version!r}, "
            "prerelease={dl.prerelease!r}"
            ")"
        ).format(dl=self)
=======
        return dict(url=self.url, filename=self.filename,
                    version=str(self.version), prerelease=self.prerelease)

    def __str__(self):
        """Format `Download` for printing."""
        u = ('Download(url={dl.url!r}, '
             'filename={dl.filename!r}, '
             'version={dl.version!r}, '
             'prerelease={dl.prerelease!r})'.format(dl=self))

        return u.encode('utf-8')
>>>>>>> 62b1f663a30cba5a4712a37c2c375cf8ad81cb4a

    def __repr__(self):
        """Code-like representation of `Download`."""
        return str(self)

    def __eq__(self, other):
        """Compare Downloads based on version numbers."""
<<<<<<< HEAD
        if (
            self.url != other.url
            or self.filename != other.filename
            or self.version != other.version
            or self.prerelease != other.prerelease
        ):
=======
        if self.url != other.url \
                or self.filename != other.filename \
                or self.version != other.version \
                or self.prerelease != other.prerelease:
>>>>>>> 62b1f663a30cba5a4712a37c2c375cf8ad81cb4a
            return False
        return True

    def __ne__(self, other):
        """Compare Downloads based on version numbers."""
        return not self.__eq__(other)

    def __lt__(self, other):
        """Compare Downloads based on version numbers."""
        if self.version != other.version:
            return self.version < other.version
        return self.alfred_version < other.alfred_version


class Version(object):
    """Mostly semantic versioning.

    The main difference to proper :ref:`semantic versioning <semver>`
    is that this implementation doesn't require a minor or patch version.

    Version strings may also be prefixed with "v", e.g.:

    >>> v = Version('v1.1.1')
    >>> v.tuple
    (1, 1, 1, '')

    >>> v = Version('2.0')
    >>> v.tuple
    (2, 0, 0, '')

    >>> Version('3.1-beta').tuple
    (3, 1, 0, 'beta')

    >>> Version('1.0.1') > Version('0.0.1')
    True
    """

    #: Match version and pre-release/build information in version strings
<<<<<<< HEAD
    match_version = re.compile(r"([0-9][0-9\.]*)(.+)?").match
=======
    match_version = re.compile(r'([0-9\.]+)(.+)?').match
>>>>>>> 62b1f663a30cba5a4712a37c2c375cf8ad81cb4a

    def __init__(self, vstr):
        """Create new `Version` object.

        Args:
            vstr (basestring): Semantic version string.
        """
        if not vstr:
<<<<<<< HEAD
            raise ValueError("invalid version number: {!r}".format(vstr))
=======
            raise ValueError('invalid version number: {!r}'.format(vstr))
>>>>>>> 62b1f663a30cba5a4712a37c2c375cf8ad81cb4a

        self.vstr = vstr
        self.major = 0
        self.minor = 0
        self.patch = 0
<<<<<<< HEAD
        self.suffix = ""
        self.build = ""
        self._parse(vstr)

    def _parse(self, vstr):
        vstr = str(vstr)
        if vstr.startswith("v"):
=======
        self.suffix = ''
        self.build = ''
        self._parse(vstr)

    def _parse(self, vstr):
        if vstr.startswith('v'):
>>>>>>> 62b1f663a30cba5a4712a37c2c375cf8ad81cb4a
            m = self.match_version(vstr[1:])
        else:
            m = self.match_version(vstr)
        if not m:
<<<<<<< HEAD
            raise ValueError("invalid version number: " + vstr)
=======
            raise ValueError('invalid version number: {!r}'.format(vstr))
>>>>>>> 62b1f663a30cba5a4712a37c2c375cf8ad81cb4a

        version, suffix = m.groups()
        parts = self._parse_dotted_string(version)
        self.major = parts.pop(0)
        if len(parts):
            self.minor = parts.pop(0)
        if len(parts):
            self.patch = parts.pop(0)
        if not len(parts) == 0:
<<<<<<< HEAD
            raise ValueError("version number too long: " + vstr)

        if suffix:
            # Build info
            idx = suffix.find("+")
            if idx > -1:
                self.build = suffix[idx + 1 :]
                suffix = suffix[:idx]
            if suffix:
                if not suffix.startswith("-"):
                    raise ValueError("suffix must start with - : " + suffix)
                self.suffix = suffix[1:]

    def _parse_dotted_string(self, s):
        """Parse string ``s`` into list of ints and strings."""
        parsed = []
        parts = s.split(".")
=======
            raise ValueError('version number too long: {!r}'.format(vstr))

        if suffix:
            # Build info
            idx = suffix.find('+')
            if idx > -1:
                self.build = suffix[idx+1:]
                suffix = suffix[:idx]
            if suffix:
                if not suffix.startswith('-'):
                    raise ValueError(
                        'suffix must start with - : {0}'.format(suffix))
                self.suffix = suffix[1:]

        # wf().logger.debug('version str `{}` -> {}'.format(vstr, repr(self)))

    def _parse_dotted_string(self, s):
        """Parse string ``s`` into list of ints and strings."""
        parsed = []
        parts = s.split('.')
>>>>>>> 62b1f663a30cba5a4712a37c2c375cf8ad81cb4a
        for p in parts:
            if p.isdigit():
                p = int(p)
            parsed.append(p)
        return parsed

    @property
    def tuple(self):
        """Version number as a tuple of major, minor, patch, pre-release."""
        return (self.major, self.minor, self.patch, self.suffix)

    def __lt__(self, other):
        """Implement comparison."""
        if not isinstance(other, Version):
<<<<<<< HEAD
            raise ValueError("not a Version instance: {0!r}".format(other))
=======
            raise ValueError('not a Version instance: {0!r}'.format(other))
>>>>>>> 62b1f663a30cba5a4712a37c2c375cf8ad81cb4a
        t = self.tuple[:3]
        o = other.tuple[:3]
        if t < o:
            return True
        if t == o:  # We need to compare suffixes
            if self.suffix and not other.suffix:
                return True
            if other.suffix and not self.suffix:
                return False
<<<<<<< HEAD

            self_suffix = self._parse_dotted_string(self.suffix)
            other_suffix = self._parse_dotted_string(other.suffix)

            for s, o in zip_longest(self_suffix, other_suffix):
                if s is None:  # shorter value wins
                    return True
                elif o is None:  # longer value loses
                    return False
                elif type(s) != type(o):  # type coersion
                    s, o = str(s), str(o)
                if s == o:  # next if the same compare
                    continue
                return s < o  # finally compare
=======
            return self._parse_dotted_string(self.suffix) \
                < self._parse_dotted_string(other.suffix)
>>>>>>> 62b1f663a30cba5a4712a37c2c375cf8ad81cb4a
        # t > o
        return False

    def __eq__(self, other):
        """Implement comparison."""
        if not isinstance(other, Version):
<<<<<<< HEAD
            raise ValueError("not a Version instance: {0!r}".format(other))
=======
            raise ValueError('not a Version instance: {0!r}'.format(other))
>>>>>>> 62b1f663a30cba5a4712a37c2c375cf8ad81cb4a
        return self.tuple == other.tuple

    def __ne__(self, other):
        """Implement comparison."""
        return not self.__eq__(other)

    def __gt__(self, other):
        """Implement comparison."""
        if not isinstance(other, Version):
<<<<<<< HEAD
            raise ValueError("not a Version instance: {0!r}".format(other))
=======
            raise ValueError('not a Version instance: {0!r}'.format(other))
>>>>>>> 62b1f663a30cba5a4712a37c2c375cf8ad81cb4a
        return other.__lt__(self)

    def __le__(self, other):
        """Implement comparison."""
        if not isinstance(other, Version):
<<<<<<< HEAD
            raise ValueError("not a Version instance: {0!r}".format(other))
=======
            raise ValueError('not a Version instance: {0!r}'.format(other))
>>>>>>> 62b1f663a30cba5a4712a37c2c375cf8ad81cb4a
        return not other.__lt__(self)

    def __ge__(self, other):
        """Implement comparison."""
        return not self.__lt__(other)

    def __str__(self):
        """Return semantic version string."""
<<<<<<< HEAD
        vstr = "{0}.{1}.{2}".format(self.major, self.minor, self.patch)
        if self.suffix:
            vstr = "{0}-{1}".format(vstr, self.suffix)
        if self.build:
            vstr = "{0}+{1}".format(vstr, self.build)
=======
        vstr = '{0}.{1}.{2}'.format(self.major, self.minor, self.patch)
        if self.suffix:
            vstr = '{0}-{1}'.format(vstr, self.suffix)
        if self.build:
            vstr = '{0}+{1}'.format(vstr, self.build)
>>>>>>> 62b1f663a30cba5a4712a37c2c375cf8ad81cb4a
        return vstr

    def __repr__(self):
        """Return 'code' representation of `Version`."""
        return "Version('{0}')".format(str(self))


def retrieve_download(dl):
    """Saves a download to a temporary file and returns path.

    .. versionadded: 1.37

    Args:
        url (unicode): URL to .alfredworkflow file in GitHub repo

    Returns:
        unicode: path to downloaded file

    """
    if not match_workflow(dl.filename):
<<<<<<< HEAD
        raise ValueError("attachment not a workflow: " + dl.filename)

    path = os.path.join(tempfile.gettempdir(), dl.filename)
    wf().logger.debug("downloading update from " "%r to %r ...", dl.url, path)

    r = request.urlopen(dl.url)

    with atomic_writer(path, "wb") as file_obj:
        file_obj.write(r.read())
=======
        raise ValueError('attachment not a workflow: ' + dl.filename)

    path = os.path.join(tempfile.gettempdir(), dl.filename)
    wf().logger.debug('downloading update from '
                      '%r to %r ...', dl.url, path)

    r = web.get(dl.url)
    r.raise_for_status()

    r.save_to_path(path)
>>>>>>> 62b1f663a30cba5a4712a37c2c375cf8ad81cb4a

    return path


def build_api_url(repo):
    """Generate releases URL from GitHub repo.

    Args:
        repo (unicode): Repo name in form ``username/repo``

    Returns:
        unicode: URL to the API endpoint for the repo's releases

    """
<<<<<<< HEAD
    if len(repo.split("/")) != 2:
        raise ValueError("invalid GitHub repo: {!r}".format(repo))
=======
    if len(repo.split('/')) != 2:
        raise ValueError('invalid GitHub repo: {!r}'.format(repo))
>>>>>>> 62b1f663a30cba5a4712a37c2c375cf8ad81cb4a

    return RELEASES_BASE.format(repo)


def get_downloads(repo):
    """Load available ``Download``s for GitHub repo.

    .. versionadded: 1.37

    Args:
        repo (unicode): GitHub repo to load releases for.

    Returns:
        list: Sequence of `Download` contained in GitHub releases.
    """
    url = build_api_url(repo)

    def _fetch():
<<<<<<< HEAD
        wf().logger.info("retrieving releases for %r ...", repo)
        r = request.urlopen(url)
        return r.read()

    key = "github-releases-" + repo.replace("/", "-")
=======
        wf().logger.info('retrieving releases for %r ...', repo)
        r = web.get(url)
        r.raise_for_status()
        return r.content

    key = 'github-releases-' + repo.replace('/', '-')
>>>>>>> 62b1f663a30cba5a4712a37c2c375cf8ad81cb4a
    js = wf().cached_data(key, _fetch, max_age=60)

    return Download.from_releases(js)


def latest_download(dls, alfred_version=None, prereleases=False):
    """Return newest `Download`."""
<<<<<<< HEAD
    alfred_version = alfred_version or os.getenv("alfred_version")
=======
    alfred_version = alfred_version or os.getenv('alfred_version')
>>>>>>> 62b1f663a30cba5a4712a37c2c375cf8ad81cb4a
    version = None
    if alfred_version:
        version = Version(alfred_version)

    dls.sort(reverse=True)
    for dl in dls:
        if dl.prerelease and not prereleases:
<<<<<<< HEAD
            wf().logger.debug("ignored prerelease: %s", dl.version)
            continue
        if version and dl.alfred_version > version:
            wf().logger.debug(
                "ignored incompatible (%s > %s): %s",
                dl.alfred_version,
                version,
                dl.filename,
            )
            continue

        wf().logger.debug("latest version: %s (%s)", dl.version, dl.filename)
=======
            wf().logger.debug('ignored prerelease: %s', dl.version)
            continue
        if version and dl.alfred_version > version:
            wf().logger.debug('ignored incompatible (%s > %s): %s',
                              dl.alfred_version, version, dl.filename)
            continue

        wf().logger.debug('latest version: %s (%s)', dl.version, dl.filename)
>>>>>>> 62b1f663a30cba5a4712a37c2c375cf8ad81cb4a
        return dl

    return None


<<<<<<< HEAD
def check_update(repo, current_version, prereleases=False, alfred_version=None):
=======
def check_update(repo, current_version, prereleases=False,
                 alfred_version=None):
>>>>>>> 62b1f663a30cba5a4712a37c2c375cf8ad81cb4a
    """Check whether a newer release is available on GitHub.

    Args:
        repo (unicode): ``username/repo`` for workflow's GitHub repo
        current_version (unicode): the currently installed version of the
            workflow. :ref:`Semantic versioning <semver>` is required.
        prereleases (bool): Whether to include pre-releases.
        alfred_version (unicode): version of currently-running Alfred.
            if empty, defaults to ``$alfred_version`` environment variable.

    Returns:
        bool: ``True`` if an update is available, else ``False``

    If an update is available, its version number and download URL will
    be cached.

    """
<<<<<<< HEAD
    key = "__workflow_latest_version"
    # data stored when no update is available
    no_update = {"available": False, "download": None, "version": None}
=======
    key = '__workflow_latest_version'
    # data stored when no update is available
    no_update = {
        'available': False,
        'download': None,
        'version': None,
    }
>>>>>>> 62b1f663a30cba5a4712a37c2c375cf8ad81cb4a
    current = Version(current_version)

    dls = get_downloads(repo)
    if not len(dls):
<<<<<<< HEAD
        wf().logger.warning("no valid downloads for %s", repo)
        wf().cache_data(key, no_update)
        return False

    wf().logger.info("%d download(s) for %s", len(dls), repo)
=======
        wf().logger.warning('no valid downloads for %s', repo)
        wf().cache_data(key, no_update)
        return False

    wf().logger.info('%d download(s) for %s', len(dls), repo)
>>>>>>> 62b1f663a30cba5a4712a37c2c375cf8ad81cb4a

    dl = latest_download(dls, alfred_version, prereleases)

    if not dl:
<<<<<<< HEAD
        wf().logger.warning("no compatible downloads for %s", repo)
        wf().cache_data(key, no_update)
        return False

    wf().logger.debug("latest=%r, installed=%r", dl.version, current)

    if dl.version > current:
        wf().cache_data(
            key, {"version": str(dl.version), "download": dl.dict, "available": True}
        )
=======
        wf().logger.warning('no compatible downloads for %s', repo)
        wf().cache_data(key, no_update)
        return False

    wf().logger.debug('latest=%r, installed=%r', dl.version, current)

    if dl.version > current:
        wf().cache_data(key, {
            'version': str(dl.version),
            'download': dl.dict,
            'available': True,
        })
>>>>>>> 62b1f663a30cba5a4712a37c2c375cf8ad81cb4a
        return True

    wf().cache_data(key, no_update)
    return False


def install_update():
    """If a newer release is available, download and install it.

    :returns: ``True`` if an update is installed, else ``False``

    """
<<<<<<< HEAD
    key = "__workflow_latest_version"
    # data stored when no update is available
    no_update = {"available": False, "download": None, "version": None}
    status = wf().cached_data(key, max_age=0)

    if not status or not status.get("available"):
        wf().logger.info("no update available")
        return False

    dl = status.get("download")
    if not dl:
        wf().logger.info("no download information")
=======
    key = '__workflow_latest_version'
    # data stored when no update is available
    no_update = {
        'available': False,
        'download': None,
        'version': None,
    }
    status = wf().cached_data(key, max_age=0)

    if not status or not status.get('available'):
        wf().logger.info('no update available')
        return False

    dl = status.get('download')
    if not dl:
        wf().logger.info('no download information')
>>>>>>> 62b1f663a30cba5a4712a37c2c375cf8ad81cb4a
        return False

    path = retrieve_download(Download.from_dict(dl))

<<<<<<< HEAD
    wf().logger.info("installing updated workflow ...")
    subprocess.call(["open", path])  # nosec
=======
    wf().logger.info('installing updated workflow ...')
    subprocess.call(['open', path])
>>>>>>> 62b1f663a30cba5a4712a37c2c375cf8ad81cb4a

    wf().cache_data(key, no_update)
    return True


<<<<<<< HEAD
if __name__ == "__main__":  # pragma: nocover
=======
if __name__ == '__main__':  # pragma: nocover
>>>>>>> 62b1f663a30cba5a4712a37c2c375cf8ad81cb4a
    import sys

    prereleases = False

    def show_help(status=0):
        """Print help message."""
<<<<<<< HEAD
        print("usage: update.py (check|install) " "[--prereleases] <repo> <version>")
        sys.exit(status)

    argv = sys.argv[:]
    if "-h" in argv or "--help" in argv:
        show_help()

    if "--prereleases" in argv:
        argv.remove("--prereleases")
=======
        print('usage: update.py (check|install) '
              '[--prereleases] <repo> <version>')
        sys.exit(status)

    argv = sys.argv[:]
    if '-h' in argv or '--help' in argv:
        show_help()

    if '--prereleases' in argv:
        argv.remove('--prereleases')
>>>>>>> 62b1f663a30cba5a4712a37c2c375cf8ad81cb4a
        prereleases = True

    if len(argv) != 4:
        show_help(1)

    action = argv[1]
    repo = argv[2]
    version = argv[3]

    try:

<<<<<<< HEAD
        if action == "check":
            check_update(repo, version, prereleases)
        elif action == "install":
=======
        if action == 'check':
            check_update(repo, version, prereleases)
        elif action == 'install':
>>>>>>> 62b1f663a30cba5a4712a37c2c375cf8ad81cb4a
            install_update()
        else:
            show_help(1)

    except Exception as err:  # ensure traceback is in log file
        wf().logger.exception(err)
        raise err
