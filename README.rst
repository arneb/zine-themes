===========
Zine Themes
===========

Zine_ is an open source weblog engine written in Python.  

This repository holds my port of the famous `Kubrick theme`_ by 
Michael Heilemann.

The port is released under the same terms as the original work: GPL_.

More information on theme development for Zine can be found in the 
`Zine Wiki`_.


Usage
-----

Copy or checkout the ``kubrick_theme`` directory to your ``instance/plugins/``
directory and activate it in the plugins section of the administration 
interface.


Status
------

The port is still work in progress.

Currently the sidebar widgets are hardcoded in ``_widgets.html`` this will
be changed when Zine implements dynamic widgets, which can be changed in 
the administration interface.

Zine outputs HTML4 and according to the FAQ there is no easy way to make Zine
output XHTML. The original Kubrick themes uses the XHTML 1.0 Transitional
doctype and therefore the current implementation of this theme will not pass
validation because form elements (comment-form) will be rendered as HTML4
elements while the rest of the page is written in XHTML. This can be considered
a bug in the theme and may be fixed in the next version.


Customization
-------------

The Kubrick theme provides a hook to allow customizazion without altering the
code directly, for example changing the header image.

The ``example_theme`` folder is a Zine plugin, which will customize the 
``kubrick_theme`` by changing the header image and text-color in the header. 
You can use this as a starting point to build your own customization.

.. _Zine: http://zine.pocoo.org/
.. _`Kubrick theme`: http://binarybonsai.com/wordpress/kubrick/
.. _GPL: http://www.opensource.org/licenses/gpl-license.php
.. _`Zine Wiki`: http://dev.pocoo.org/projects/zine/wiki/ThemeDevelopment