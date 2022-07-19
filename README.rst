Yodaplus-py
###########

.. class:: no-web no-pdf

|python| |django| |pipy| |readthedocs|

Yodaplus-py, a fork of gnosis-py, includes a set of libraries to work with XDC and Yodaplus projects. 
  - `EthereumClient`, a wrapper over Web3.py `Web3` client including utilities to deal with ERC20/721
    tokens and tracing.
  - `Yplus Vault <https://github.com/yodaplus/gnosis-safe-contracts>`_ classes and utilities.
  - Django serializers, models and utils.

Quick start
-----------

Just run ``pip install yodaplus-py`` or add it to your **requirements.txt**

If you want django ethereum utils (models, serializers, filters...) you need to run
``pip install yodaplus-py[django]``

If you have issues building **coincurve** maybe
`you are missing some libraries <https://ofek.dev/coincurve/install/#source>`_

Ethereum utils
--------------
gnosis.eth
~~~~~~~~~~~~~~~~~~~~
- ``class EthereumClient (ethereum_node_url: str)``: Class to connect and do operations
  with a ethereum node. Uses web3 and raw rpc calls for things not supported in web3.
  Only ``http/https`` urls are suppored for the node url.

``EthereumClient`` has some utils that improve a lot performance using Ethereum nodes, like
the possibility of doing ``batch_calls`` (a single request making read-only calls to multiple contracts):

.. code-block:: python

  from gnosis.eth import EthereumClient
  from gnosis.eth.contracts import get_erc721_contract
  ethereum_client = EthereumClient(ETHEREUM_NODE_URL)
  erc721_contract = get_erc721_contract(self.w3, token_address)
  name, symbol = ethereum_client.batch_call([
                      erc721_contract.functions.name(),
                      erc721_contract.functions.symbol(),
                  ])

If you want to use the underlying `web3.py <https://github.com/ethereum/web3.py>`_ library:

.. code-block:: python

  from gnosis.eth import EthereumClient
  ethereum_client = EthereumClient(ETHEREUM_NODE_URL)
  ethereum_client.w3.eth.get_block(57)


gnosis.eth.constants
~~~~~~~~~~~~~~~~~~~~
- ``NULL_ADDRESS (0x000...0)``: Solidity ``address(0)``.
- ``SENTINEL_ADDRESS (0x000...1)``: Used for Gnosis Safe's linked lists (modules, owners...).
- Maximum an minimum values for `R`, `S` and `V` in ethereum signatures.

gnosis.eth.utils
~~~~~~~~~~~~~~~~

Contains utils for ethereum operations:

- ``get_eth_address_with_key() -> Tuple[str, bytes]``: Returns a tuple of a valid public ethereum checksumed
  address with the private key.
- ``generate_address_2(from_: Union[str, bytes], salt: Union[str, bytes], init_code: [str, bytes]) -> str``:
  Calculates the address of a new contract created using the new CREATE2 opcode.

Ethereum django (REST) utils
----------------------------
Django utils are available under ``gnosis.eth.django``.
You can find a set of helpers for working with Ethereum using Django and Django Rest framework.

It includes:

- **gnosis.eth.django.filters**: EthereumAddressFilter.
- **gnosis.eth.django.models**: Model fields (Ethereum address, Ethereum big integer field).
- **gnosis.eth.django.serializers**: Serializer fields (Ethereum address field, hexadecimal field).
- **gnosis.eth.django.validators**: Ethereum related validators.
- **gnosis.safe.serializers**: Serializers for Gnosis Safe (signature, transaction...).
- All the tests are written using Django Test suite.

.. |python| image:: https://img.shields.io/badge/Python-3.9-blue.svg
    :alt: Python 3.9

.. |django| image:: https://img.shields.io/badge/Django-2-blue.svg
    :alt: Django 2.2

.. |pipy| image:: https://badge.fury.io/py/yodaplus-py.svg
    :target: https://badge.fury.io/py/yodaplus-py
    :alt: Pypi package

.. |readthedocs| image:: https://readthedocs.org/projects/gnosis-py/badge/?version=latest
    :target: https://gnosis-py.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status
