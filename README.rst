============
random_name
============

A simple library for generating random names, similar to the docker random
name generator found `here <https://github.com/docker/docker/blob/master/pkg/namesgenerator/names-generator.go>`_.

.. code:: python

    >>> import random_name
    >>> random_name.generate_name()
    'snazzy-heliotrope-stingray'
    >>> random_name.generate(1)
    ['skanky-orange-bordeaux']
    >>> random_name.generate(10)
    ['woolly-saffron-squirrel', 'slaphappy-black-indri', 'dorky-smalt-cichlid', 'crabby-cobalt-bullfrog', 'lumpy-puce-stoat', 'snappy-magenta-dormouse', 'woolly-apricot-okapi', 'snippy-coral-woodpecker', 'lanky-cream-foxhound', 'queasy-alizarin-moth']
