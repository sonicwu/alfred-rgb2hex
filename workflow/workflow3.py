# encoding: utf-8
#
# Copyright (c) 2016 Dean Jackson <deanishe@deanishe.net>
#
# MIT Licence. See http://opensource.org/licenses/MIT
#
# Created on 2016-06-25
#

"""An Alfred 3+ version of :class:`~workflow.Workflow`.

:class:`~workflow.Workflow3` supports new features, such as
setting :ref:`workflow-variables` and
:class:`the more advanced modifiers <Modifier>` supported by Alfred 3+.

In order for the feedback mechanism to work correctly, it's important
to create :class:`Item3` and :class:`Modifier` objects via the
:meth:`Workflow3.add_item()` and :meth:`Item3.add_modifier()` methods
respectively. If you instantiate :class:`Item3` or :class:`Modifier`
objects directly, the current :class:`Workflow3` object won't be aware
of them, and they won't be sent to Alfred when you call
:meth:`Workflow3.send_feedback()`.

"""

<<<<<<< HEAD
=======
from __future__ import print_function, unicode_literals, absolute_import
>>>>>>> 62b1f663a30cba5a4712a37c2c375cf8ad81cb4a

import json
import os
import sys

from .workflow import ICON_WARNING, Workflow


class Variables(dict):
    """Workflow variables for Run Script actions.

    .. versionadded: 1.26

    This class allows you to set workflow variables from
    Run Script actions.

    It is a subclass of :class:`dict`.

    >>> v = Variables(username='deanishe', password='hunter2')
    >>> v.arg = u'output value'
    >>> print(v)

    See :ref:`variables-run-script` in the User Guide for more
    information.

    Args:
<<<<<<< HEAD
        arg (unicode or list, optional): Main output/``{query}``.
        **variables: Workflow variables to set.

    In Alfred 4.1+ and Alfred-Workflow 1.40+, ``arg`` may also be a
    :class:`list` or :class:`tuple`.

    Attributes:
        arg (unicode or list): Output value (``{query}``).
            In Alfred 4.1+ and Alfred-Workflow 1.40+, ``arg`` may also be a
            :class:`list` or :class:`tuple`.
=======
        arg (unicode, optional): Main output/``{query}``.
        **variables: Workflow variables to set.


    Attributes:
        arg (unicode): Output value (``{query}``).
>>>>>>> 62b1f663a30cba5a4712a37c2c375cf8ad81cb4a
        config (dict): Configuration for downstream workflow element.

    """

    def __init__(self, arg=None, **variables):
        """Create a new `Variables` object."""
        self.arg = arg
        self.config = {}
        super(Variables, self).__init__(**variables)

    @property
    def obj(self):
<<<<<<< HEAD
        """``alfredworkflow`` :class:`dict`."""
        o = {}
        if self:
            d2 = {}
            for k, v in list(self.items()):
                d2[k] = v
            o["variables"] = d2

        if self.config:
            o["config"] = self.config

        if self.arg is not None:
            o["arg"] = self.arg

        return {"alfredworkflow": o}

    def __str__(self):
=======
        """Return ``alfredworkflow`` `dict`."""
        o = {}
        if self:
            d2 = {}
            for k, v in self.items():
                d2[k] = v
            o['variables'] = d2

        if self.config:
            o['config'] = self.config

        if self.arg is not None:
            o['arg'] = self.arg

        return {'alfredworkflow': o}

    def __unicode__(self):
>>>>>>> 62b1f663a30cba5a4712a37c2c375cf8ad81cb4a
        """Convert to ``alfredworkflow`` JSON object.

        Returns:
            unicode: ``alfredworkflow`` JSON object

        """
        if not self and not self.config:
<<<<<<< HEAD
            if not self.arg:
                return ""
            if isinstance(self.arg, str):
                return self.arg

        return json.dumps(self.obj)

=======
            if self.arg:
                return self.arg
            else:
                return u''

        return json.dumps(self.obj)

    def __str__(self):
        """Convert to ``alfredworkflow`` JSON object.

        Returns:
            str: UTF-8 encoded ``alfredworkflow`` JSON object

        """
        return unicode(self).encode('utf-8')

>>>>>>> 62b1f663a30cba5a4712a37c2c375cf8ad81cb4a

class Modifier(object):
    """Modify :class:`Item3` arg/icon/variables when modifier key is pressed.

    Don't use this class directly (as it won't be associated with any
    :class:`Item3`), but rather use :meth:`Item3.add_modifier()`
    to add modifiers to results.

    >>> it = wf.add_item('Title', 'Subtitle', valid=True)
    >>> it.setvar('name', 'default')
    >>> m = it.add_modifier('cmd')
    >>> m.setvar('name', 'alternate')

    See :ref:`workflow-variables` in the User Guide for more information
    and :ref:`example usage <example-variables>`.

    Args:
        key (unicode): Modifier key, e.g. ``"cmd"``, ``"alt"`` etc.
        subtitle (unicode, optional): Override default subtitle.
        arg (unicode, optional): Argument to pass for this modifier.
        valid (bool, optional): Override item's validity.
        icon (unicode, optional): Filepath/UTI of icon to use
        icontype (unicode, optional): Type of icon. See
            :meth:`Workflow.add_item() <workflow.Workflow.add_item>`
            for valid values.

    Attributes:
        arg (unicode): Arg to pass to following action.
        config (dict): Configuration for a downstream element, such as
            a File Filter.
        icon (unicode): Filepath/UTI of icon.
        icontype (unicode): Type of icon. See
            :meth:`Workflow.add_item() <workflow.Workflow.add_item>`
            for valid values.
        key (unicode): Modifier key (see above).
        subtitle (unicode): Override item subtitle.
        valid (bool): Override item validity.
        variables (dict): Workflow variables set by this modifier.

    """

<<<<<<< HEAD
    def __init__(
        self, key, subtitle=None, arg=None, valid=None, icon=None, icontype=None
    ):
=======
    def __init__(self, key, subtitle=None, arg=None, valid=None, icon=None,
                 icontype=None):
>>>>>>> 62b1f663a30cba5a4712a37c2c375cf8ad81cb4a
        """Create a new :class:`Modifier`.

        Don't use this class directly (as it won't be associated with any
        :class:`Item3`), but rather use :meth:`Item3.add_modifier()`
        to add modifiers to results.

        Args:
            key (unicode): Modifier key, e.g. ``"cmd"``, ``"alt"`` etc.
            subtitle (unicode, optional): Override default subtitle.
            arg (unicode, optional): Argument to pass for this modifier.
            valid (bool, optional): Override item's validity.
            icon (unicode, optional): Filepath/UTI of icon to use
            icontype (unicode, optional): Type of icon. See
                :meth:`Workflow.add_item() <workflow.Workflow.add_item>`
                for valid values.

        """
        self.key = key
        self.subtitle = subtitle
        self.arg = arg
        self.valid = valid
        self.icon = icon
        self.icontype = icontype

        self.config = {}
        self.variables = {}

    def setvar(self, name, value):
        """Set a workflow variable for this Item.

        Args:
            name (unicode): Name of variable.
            value (unicode): Value of variable.

        """
        self.variables[name] = value

    def getvar(self, name, default=None):
        """Return value of workflow variable for ``name`` or ``default``.

        Args:
            name (unicode): Variable name.
            default (None, optional): Value to return if variable is unset.

        Returns:
            unicode or ``default``: Value of variable if set or ``default``.

        """
        return self.variables.get(name, default)

    @property
    def obj(self):
        """Modifier formatted for JSON serialization for Alfred 3.

        Returns:
            dict: Modifier for serializing to JSON.

        """
        o = {}

        if self.subtitle is not None:
<<<<<<< HEAD
            o["subtitle"] = self.subtitle

        if self.arg is not None:
            o["arg"] = self.arg

        if self.valid is not None:
            o["valid"] = self.valid

        if self.variables:
            o["variables"] = self.variables

        if self.config:
            o["config"] = self.config

        icon = self._icon()
        if icon:
            o["icon"] = icon
=======
            o['subtitle'] = self.subtitle

        if self.arg is not None:
            o['arg'] = self.arg

        if self.valid is not None:
            o['valid'] = self.valid

        if self.variables:
            o['variables'] = self.variables

        if self.config:
            o['config'] = self.config

        icon = self._icon()
        if icon:
            o['icon'] = icon
>>>>>>> 62b1f663a30cba5a4712a37c2c375cf8ad81cb4a

        return o

    def _icon(self):
        """Return `icon` object for item.

        Returns:
            dict: Mapping for item `icon` (may be empty).

        """
        icon = {}
        if self.icon is not None:
<<<<<<< HEAD
            icon["path"] = self.icon

        if self.icontype is not None:
            icon["type"] = self.icontype
=======
            icon['path'] = self.icon

        if self.icontype is not None:
            icon['type'] = self.icontype
>>>>>>> 62b1f663a30cba5a4712a37c2c375cf8ad81cb4a

        return icon


class Item3(object):
    """Represents a feedback item for Alfred 3+.

    Generates Alfred-compliant JSON for a single item.

    Don't use this class directly (as it then won't be associated with
    any :class:`Workflow3 <workflow.Workflow3>` object), but rather use
    :meth:`Workflow3.add_item() <workflow.Workflow3.add_item>`.
    See :meth:`~workflow.Workflow3.add_item` for details of arguments.

    """

<<<<<<< HEAD
    def __init__(
        self,
        title,
        subtitle="",
        arg=None,
        autocomplete=None,
        match=None,
        valid=False,
        uid=None,
        icon=None,
        icontype=None,
        type=None,
        largetext=None,
        copytext=None,
        quicklookurl=None,
    ):
=======
    def __init__(self, title, subtitle='', arg=None, autocomplete=None,
                 match=None, valid=False, uid=None, icon=None, icontype=None,
                 type=None, largetext=None, copytext=None, quicklookurl=None):
>>>>>>> 62b1f663a30cba5a4712a37c2c375cf8ad81cb4a
        """Create a new :class:`Item3` object.

        Use same arguments as for
        :class:`Workflow.Item <workflow.Workflow.Item>`.

        Argument ``subtitle_modifiers`` is not supported.

        """
        self.title = title
        self.subtitle = subtitle
        self.arg = arg
        self.autocomplete = autocomplete
        self.match = match
        self.valid = valid
        self.uid = uid
        self.icon = icon
        self.icontype = icontype
        self.type = type
        self.quicklookurl = quicklookurl
        self.largetext = largetext
        self.copytext = copytext

        self.modifiers = {}

        self.config = {}
        self.variables = {}

    def setvar(self, name, value):
        """Set a workflow variable for this Item.

        Args:
            name (unicode): Name of variable.
            value (unicode): Value of variable.

        """
        self.variables[name] = value

    def getvar(self, name, default=None):
        """Return value of workflow variable for ``name`` or ``default``.

        Args:
            name (unicode): Variable name.
            default (None, optional): Value to return if variable is unset.

        Returns:
            unicode or ``default``: Value of variable if set or ``default``.

        """
        return self.variables.get(name, default)

<<<<<<< HEAD
    def add_modifier(
        self, key, subtitle=None, arg=None, valid=None, icon=None, icontype=None
    ):
=======
    def add_modifier(self, key, subtitle=None, arg=None, valid=None, icon=None,
                     icontype=None):
>>>>>>> 62b1f663a30cba5a4712a37c2c375cf8ad81cb4a
        """Add alternative values for a modifier key.

        Args:
            key (unicode): Modifier key, e.g. ``"cmd"`` or ``"alt"``
            subtitle (unicode, optional): Override item subtitle.
            arg (unicode, optional): Input for following action.
            valid (bool, optional): Override item validity.
            icon (unicode, optional): Filepath/UTI of icon.
            icontype (unicode, optional): Type of icon.  See
                :meth:`Workflow.add_item() <workflow.Workflow.add_item>`
                for valid values.

<<<<<<< HEAD
        In Alfred 4.1+ and Alfred-Workflow 1.40+, ``arg`` may also be a
        :class:`list` or :class:`tuple`.

=======
>>>>>>> 62b1f663a30cba5a4712a37c2c375cf8ad81cb4a
        Returns:
            Modifier: Configured :class:`Modifier`.

        """
        mod = Modifier(key, subtitle, arg, valid, icon, icontype)

        # Add Item variables to Modifier
        mod.variables.update(self.variables)

        self.modifiers[key] = mod

        return mod

    @property
    def obj(self):
        """Item formatted for JSON serialization.

        Returns:
            dict: Data suitable for Alfred 3 feedback.

        """
        # Required values
<<<<<<< HEAD
        o = {"title": self.title, "subtitle": self.subtitle, "valid": self.valid}

        # Optional values
        if self.arg is not None:
            o["arg"] = self.arg

        if self.autocomplete is not None:
            o["autocomplete"] = self.autocomplete

        if self.match is not None:
            o["match"] = self.match

        if self.uid is not None:
            o["uid"] = self.uid

        if self.type is not None:
            o["type"] = self.type

        if self.quicklookurl is not None:
            o["quicklookurl"] = self.quicklookurl

        if self.variables:
            o["variables"] = self.variables

        if self.config:
            o["config"] = self.config
=======
        o = {
            'title': self.title,
            'subtitle': self.subtitle,
            'valid': self.valid,
        }

        # Optional values
        if self.arg is not None:
            o['arg'] = self.arg

        if self.autocomplete is not None:
            o['autocomplete'] = self.autocomplete

        if self.match is not None:
            o['match'] = self.match

        if self.uid is not None:
            o['uid'] = self.uid

        if self.type is not None:
            o['type'] = self.type

        if self.quicklookurl is not None:
            o['quicklookurl'] = self.quicklookurl

        if self.variables:
            o['variables'] = self.variables

        if self.config:
            o['config'] = self.config
>>>>>>> 62b1f663a30cba5a4712a37c2c375cf8ad81cb4a

        # Largetype and copytext
        text = self._text()
        if text:
<<<<<<< HEAD
            o["text"] = text

        icon = self._icon()
        if icon:
            o["icon"] = icon
=======
            o['text'] = text

        icon = self._icon()
        if icon:
            o['icon'] = icon
>>>>>>> 62b1f663a30cba5a4712a37c2c375cf8ad81cb4a

        # Modifiers
        mods = self._modifiers()
        if mods:
<<<<<<< HEAD
            o["mods"] = mods
=======
            o['mods'] = mods
>>>>>>> 62b1f663a30cba5a4712a37c2c375cf8ad81cb4a

        return o

    def _icon(self):
        """Return `icon` object for item.

        Returns:
            dict: Mapping for item `icon` (may be empty).

        """
        icon = {}
        if self.icon is not None:
<<<<<<< HEAD
            icon["path"] = self.icon

        if self.icontype is not None:
            icon["type"] = self.icontype
=======
            icon['path'] = self.icon

        if self.icontype is not None:
            icon['type'] = self.icontype
>>>>>>> 62b1f663a30cba5a4712a37c2c375cf8ad81cb4a

        return icon

    def _text(self):
        """Return `largetext` and `copytext` object for item.

        Returns:
            dict: `text` mapping (may be empty)

        """
        text = {}
        if self.largetext is not None:
<<<<<<< HEAD
            text["largetype"] = self.largetext

        if self.copytext is not None:
            text["copy"] = self.copytext
=======
            text['largetype'] = self.largetext

        if self.copytext is not None:
            text['copy'] = self.copytext
>>>>>>> 62b1f663a30cba5a4712a37c2c375cf8ad81cb4a

        return text

    def _modifiers(self):
        """Build `mods` dictionary for JSON feedback.

        Returns:
            dict: Modifier mapping or `None`.

        """
        if self.modifiers:
            mods = {}
<<<<<<< HEAD
            for k, mod in list(self.modifiers.items()):
=======
            for k, mod in self.modifiers.items():
>>>>>>> 62b1f663a30cba5a4712a37c2c375cf8ad81cb4a
                mods[k] = mod.obj

            return mods

        return None


class Workflow3(Workflow):
    """Workflow class that generates Alfred 3+ feedback.

    It is a subclass of :class:`~workflow.Workflow` and most of its
    methods are documented there.

    Attributes:
        item_class (class): Class used to generate feedback items.
        variables (dict): Top level workflow variables.

    """

    item_class = Item3

    def __init__(self, **kwargs):
        """Create a new :class:`Workflow3` object.

        See :class:`~workflow.Workflow` for documentation.

        """
        Workflow.__init__(self, **kwargs)
        self.variables = {}
        self._rerun = 0
        # Get session ID from environment if present
<<<<<<< HEAD
        self._session_id = os.getenv("_WF_SESSION_ID") or None
        if self._session_id:
            self.setvar("_WF_SESSION_ID", self._session_id)
=======
        self._session_id = os.getenv('_WF_SESSION_ID') or None
        if self._session_id:
            self.setvar('_WF_SESSION_ID', self._session_id)
>>>>>>> 62b1f663a30cba5a4712a37c2c375cf8ad81cb4a

    @property
    def _default_cachedir(self):
        """Alfred 4's default cache directory."""
        return os.path.join(
            os.path.expanduser(
<<<<<<< HEAD
                "~/Library/Caches/com.runningwithcrayons.Alfred/" "Workflow Data/"
            ),
            self.bundleid,
        )
=======
                '~/Library/Caches/com.runningwithcrayons.Alfred/'
                'Workflow Data/'),
            self.bundleid)
>>>>>>> 62b1f663a30cba5a4712a37c2c375cf8ad81cb4a

    @property
    def _default_datadir(self):
        """Alfred 4's default data directory."""
<<<<<<< HEAD
        return os.path.join(
            os.path.expanduser("~/Library/Application Support/Alfred/Workflow Data/"),
            self.bundleid,
        )
=======
        return os.path.join(os.path.expanduser(
            '~/Library/Application Support/Alfred/Workflow Data/'),
            self.bundleid)
>>>>>>> 62b1f663a30cba5a4712a37c2c375cf8ad81cb4a

    @property
    def rerun(self):
        """How often (in seconds) Alfred should re-run the Script Filter."""
        return self._rerun

    @rerun.setter
    def rerun(self, seconds):
        """Interval at which Alfred should re-run the Script Filter.

        Args:
            seconds (int): Interval between runs.
        """
        self._rerun = seconds

    @property
    def session_id(self):
        """A unique session ID every time the user uses the workflow.

        .. versionadded:: 1.25

        The session ID persists while the user is using this workflow.
        It expires when the user runs a different workflow or closes
        Alfred.

        """
        if not self._session_id:
            from uuid import uuid4
<<<<<<< HEAD

            self._session_id = uuid4().hex
            self.setvar("_WF_SESSION_ID", self._session_id)
=======
            self._session_id = uuid4().hex
            self.setvar('_WF_SESSION_ID', self._session_id)
>>>>>>> 62b1f663a30cba5a4712a37c2c375cf8ad81cb4a

        return self._session_id

    def setvar(self, name, value, persist=False):
        """Set a "global" workflow variable.

        .. versionchanged:: 1.33

        These variables are always passed to downstream workflow objects.

        If you have set :attr:`rerun`, these variables are also passed
        back to the script when Alfred runs it again.

        Args:
            name (unicode): Name of variable.
            value (unicode): Value of variable.
            persist (bool, optional): Also save variable to ``info.plist``?

        """
        self.variables[name] = value
        if persist:
            from .util import set_config
<<<<<<< HEAD

            set_config(name, value, self.bundleid)
            self.logger.debug(
                "saved variable %r with value %r to info.plist", name, value
            )
=======
            set_config(name, value, self.bundleid)
            self.logger.debug('saved variable %r with value %r to info.plist',
                              name, value)
>>>>>>> 62b1f663a30cba5a4712a37c2c375cf8ad81cb4a

    def getvar(self, name, default=None):
        """Return value of workflow variable for ``name`` or ``default``.

        Args:
            name (unicode): Variable name.
            default (None, optional): Value to return if variable is unset.

        Returns:
            unicode or ``default``: Value of variable if set or ``default``.

        """
        return self.variables.get(name, default)

<<<<<<< HEAD
    def add_item(
        self,
        title,
        subtitle="",
        arg=None,
        autocomplete=None,
        valid=False,
        uid=None,
        icon=None,
        icontype=None,
        type=None,
        largetext=None,
        copytext=None,
        quicklookurl=None,
        match=None,
    ):
=======
    def add_item(self, title, subtitle='', arg=None, autocomplete=None,
                 valid=False, uid=None, icon=None, icontype=None, type=None,
                 largetext=None, copytext=None, quicklookurl=None, match=None):
>>>>>>> 62b1f663a30cba5a4712a37c2c375cf8ad81cb4a
        """Add an item to be output to Alfred.

        Args:
            match (unicode, optional): If you have "Alfred filters results"
                turned on for your Script Filter, Alfred (version 3.5 and
                above) will filter against this field, not ``title``.

<<<<<<< HEAD
        In Alfred 4.1+ and Alfred-Workflow 1.40+, ``arg`` may also be a
        :class:`list` or :class:`tuple`.

=======
>>>>>>> 62b1f663a30cba5a4712a37c2c375cf8ad81cb4a
        See :meth:`Workflow.add_item() <workflow.Workflow.add_item>` for
        the main documentation and other parameters.

        The key difference is that this method does not support the
        ``modifier_subtitles`` argument. Use the :meth:`~Item3.add_modifier()`
        method instead on the returned item instead.

        Returns:
            Item3: Alfred feedback item.

        """
<<<<<<< HEAD
        item = self.item_class(
            title,
            subtitle,
            arg,
            autocomplete,
            match,
            valid,
            uid,
            icon,
            icontype,
            type,
            largetext,
            copytext,
            quicklookurl,
        )
=======
        item = self.item_class(title, subtitle, arg, autocomplete,
                               match, valid, uid, icon, icontype, type,
                               largetext, copytext, quicklookurl)
>>>>>>> 62b1f663a30cba5a4712a37c2c375cf8ad81cb4a

        # Add variables to child item
        item.variables.update(self.variables)

        self._items.append(item)
        return item

    @property
    def _session_prefix(self):
        """Filename prefix for current session."""
<<<<<<< HEAD
        return "_wfsess-{0}-".format(self.session_id)
=======
        return '_wfsess-{0}-'.format(self.session_id)
>>>>>>> 62b1f663a30cba5a4712a37c2c375cf8ad81cb4a

    def _mk_session_name(self, name):
        """New cache name/key based on session ID."""
        return self._session_prefix + name

    def cache_data(self, name, data, session=False):
        """Cache API with session-scoped expiry.

        .. versionadded:: 1.25

        Args:
            name (str): Cache key
            data (object): Data to cache
            session (bool, optional): Whether to scope the cache
                to the current session.

        ``name`` and ``data`` are the same as for the
        :meth:`~workflow.Workflow.cache_data` method on
        :class:`~workflow.Workflow`.

        If ``session`` is ``True``, then ``name`` is prefixed
        with :attr:`session_id`.

        """
        if session:
            name = self._mk_session_name(name)

        return super(Workflow3, self).cache_data(name, data)

    def cached_data(self, name, data_func=None, max_age=60, session=False):
        """Cache API with session-scoped expiry.

        .. versionadded:: 1.25

        Args:
            name (str): Cache key
            data_func (callable): Callable that returns fresh data. It
                is called if the cache has expired or doesn't exist.
            max_age (int): Maximum allowable age of cache in seconds.
            session (bool, optional): Whether to scope the cache
                to the current session.

        ``name``, ``data_func`` and ``max_age`` are the same as for the
        :meth:`~workflow.Workflow.cached_data` method on
        :class:`~workflow.Workflow`.

        If ``session`` is ``True``, then ``name`` is prefixed
        with :attr:`session_id`.

        """
        if session:
            name = self._mk_session_name(name)

        return super(Workflow3, self).cached_data(name, data_func, max_age)

    def clear_session_cache(self, current=False):
        """Remove session data from the cache.

        .. versionadded:: 1.25
        .. versionchanged:: 1.27

        By default, data belonging to the current session won't be
        deleted. Set ``current=True`` to also clear current session.

        Args:
            current (bool, optional): If ``True``, also remove data for
                current session.

        """
<<<<<<< HEAD

        def _is_session_file(filename):
            if current:
                return filename.startswith("_wfsess-")
            return filename.startswith("_wfsess-") and not filename.startswith(
                self._session_prefix
            )
=======
        def _is_session_file(filename):
            if current:
                return filename.startswith('_wfsess-')
            return filename.startswith('_wfsess-') \
                and not filename.startswith(self._session_prefix)
>>>>>>> 62b1f663a30cba5a4712a37c2c375cf8ad81cb4a

        self.clear_cache(_is_session_file)

    @property
    def obj(self):
        """Feedback formatted for JSON serialization.

        Returns:
            dict: Data suitable for Alfred 3 feedback.

        """
        items = []
        for item in self._items:
            items.append(item.obj)

<<<<<<< HEAD
        o = {"items": items}
        if self.variables:
            o["variables"] = self.variables
        if self.rerun:
            o["rerun"] = self.rerun
        return o

    def warn_empty(self, title, subtitle="", icon=None):
=======
        o = {'items': items}
        if self.variables:
            o['variables'] = self.variables
        if self.rerun:
            o['rerun'] = self.rerun
        return o

    def warn_empty(self, title, subtitle=u'', icon=None):
>>>>>>> 62b1f663a30cba5a4712a37c2c375cf8ad81cb4a
        """Add a warning to feedback if there are no items.

        .. versionadded:: 1.31

        Add a "warning" item to Alfred feedback if no other items
        have been added. This is a handy shortcut to prevent Alfred
        from showing its fallback searches, which is does if no
        items are returned.

        Args:
            title (unicode): Title of feedback item.
            subtitle (unicode, optional): Subtitle of feedback item.
            icon (str, optional): Icon for feedback item. If not
                specified, ``ICON_WARNING`` is used.

        Returns:
            Item3: Newly-created item.

        """
        if len(self._items):
            return

        icon = icon or ICON_WARNING
        return self.add_item(title, subtitle, icon=icon)

    def send_feedback(self):
        """Print stored items to console/Alfred as JSON."""
<<<<<<< HEAD
        if self.debugging:
            json.dump(self.obj, sys.stdout, indent=2, separators=(",", ": "))
        else:
            json.dump(self.obj, sys.stdout)
=======
        json.dump(self.obj, sys.stdout)
>>>>>>> 62b1f663a30cba5a4712a37c2c375cf8ad81cb4a
        sys.stdout.flush()
