=============
multisettings
=============

Tool to handle multiple settings for editor, shell and other command line tools.


Usage
=====

#. Create ``~/.multisettings.yaml`` like below.
#. Run ``multisettings USER [-c CONFIG_FILE]`` (ex: ``multisettings wkentaro -c ~/multisettings.yaml``)


``~/.multisettings.yaml``
=========================

::

    username:
      .default_config_file: .user_specific_config_file

    wkentaro:
      .vimrc: .vimrc.wkentaro
      .zshrc: .zshrc.wkentaro
