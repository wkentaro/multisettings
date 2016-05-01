multisettings
=============

Tool to handle multiple settings for editor, shell and other command line tools.


Usage
-----

#. Create ``~/.multisettings.yaml`` like below.
#. Run ``multisettings USER [-c CONFIG_FILE]`` (ex: ``multisettings wkentaro -c ~/multisettings.yaml``)


``~/.multisettings.yaml``
-------------------------

::

    wkentaro:
      .vimrc: .vimrc.wkentaro
      .zshrc: .zshrc.wkentaro
