# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PortProtocolsEntity:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'private_plain_enable': 'bool',
        'private_plain_address': 'str',
        'private_plain_domain_name': 'str',
        'private_sasl_ssl_enable': 'bool',
        'private_sasl_ssl_address': 'str',
        'private_sasl_ssl_domain_name': 'str',
        'private_sasl_plaintext_enable': 'bool',
        'private_sasl_plaintext_address': 'str',
        'private_sasl_plaintext_domain_name': 'str',
        'public_plain_enable': 'bool',
        'public_plain_address': 'str',
        'public_plain_domain_name': 'str',
        'public_sasl_ssl_enable': 'bool',
        'public_sasl_ssl_address': 'str',
        'public_sasl_ssl_domain_name': 'str',
        'public_sasl_plaintext_enable': 'bool',
        'public_sasl_plaintext_address': 'str',
        'public_sasl_plaintext_domain_name': 'str'
    }

    attribute_map = {
        'private_plain_enable': 'private_plain_enable',
        'private_plain_address': 'private_plain_address',
        'private_plain_domain_name': 'private_plain_domain_name',
        'private_sasl_ssl_enable': 'private_sasl_ssl_enable',
        'private_sasl_ssl_address': 'private_sasl_ssl_address',
        'private_sasl_ssl_domain_name': 'private_sasl_ssl_domain_name',
        'private_sasl_plaintext_enable': 'private_sasl_plaintext_enable',
        'private_sasl_plaintext_address': 'private_sasl_plaintext_address',
        'private_sasl_plaintext_domain_name': 'private_sasl_plaintext_domain_name',
        'public_plain_enable': 'public_plain_enable',
        'public_plain_address': 'public_plain_address',
        'public_plain_domain_name': 'public_plain_domain_name',
        'public_sasl_ssl_enable': 'public_sasl_ssl_enable',
        'public_sasl_ssl_address': 'public_sasl_ssl_address',
        'public_sasl_ssl_domain_name': 'public_sasl_ssl_domain_name',
        'public_sasl_plaintext_enable': 'public_sasl_plaintext_enable',
        'public_sasl_plaintext_address': 'public_sasl_plaintext_address',
        'public_sasl_plaintext_domain_name': 'public_sasl_plaintext_domain_name'
    }

    def __init__(self, private_plain_enable=None, private_plain_address=None, private_plain_domain_name=None, private_sasl_ssl_enable=None, private_sasl_ssl_address=None, private_sasl_ssl_domain_name=None, private_sasl_plaintext_enable=None, private_sasl_plaintext_address=None, private_sasl_plaintext_domain_name=None, public_plain_enable=None, public_plain_address=None, public_plain_domain_name=None, public_sasl_ssl_enable=None, public_sasl_ssl_address=None, public_sasl_ssl_domain_name=None, public_sasl_plaintext_enable=None, public_sasl_plaintext_address=None, public_sasl_plaintext_domain_name=None):
        r"""PortProtocolsEntity

        The model defined in huaweicloud sdk

        :param private_plain_enable: 实例是否支持内网PLAINTEXT访问接入方式。  - true：实例支持内网PLAINTEXT访问方式接入方式。  - false：实例不支持内网PLAINTEXT访问接入方式。
        :type private_plain_enable: bool
        :param private_plain_address: kafka内网PLAINTEXT接入方式连接地址。
        :type private_plain_address: str
        :param private_plain_domain_name: 内网明文连接域名
        :type private_plain_domain_name: str
        :param private_sasl_ssl_enable: 实例是否支持内网SASL_SSL访问接入方式。  - true：实例支持内网SASL_SSL访问方式接入方式。  - false：实例不支持内网SASL_SSL访问接入方式。
        :type private_sasl_ssl_enable: bool
        :param private_sasl_ssl_address: kafka内网SASL_SSL接入方式连接地址。
        :type private_sasl_ssl_address: str
        :param private_sasl_ssl_domain_name: 内网SASL_SSL连接域名
        :type private_sasl_ssl_domain_name: str
        :param private_sasl_plaintext_enable: 实例是否支持内网SASL_PLAINTEXT访问接入方式。  - true，实例支持内网SASL_PLAINTEXT访问方式接入方式。  - false，实例不支持内网SASL_PLAINTEXT访问接入方式。
        :type private_sasl_plaintext_enable: bool
        :param private_sasl_plaintext_address: kafka内网SASL_PLAINTEXT接入方式连接地址。
        :type private_sasl_plaintext_address: str
        :param private_sasl_plaintext_domain_name: 内网SASL_PLAINTEXT连接域名
        :type private_sasl_plaintext_domain_name: str
        :param public_plain_enable: 实例是否支持公网PLAINTEXT访问接入方式。  - true，实例支持公网PLAINTEXT访问方式接入方式。  - false，实例不支持公网PLAINTEXT访问接入方式。
        :type public_plain_enable: bool
        :param public_plain_address: kafka公网PLAINTEXT接入方式连接地址。
        :type public_plain_address: str
        :param public_plain_domain_name: 公网明文连接域名
        :type public_plain_domain_name: str
        :param public_sasl_ssl_enable: 实例是否支持公网SASL_SSL访问接入方式。  - true，实例支持内网SASL_SSL访问方式接入方式。  - false，实例不支持公网SASL_SSL访问接入方式。
        :type public_sasl_ssl_enable: bool
        :param public_sasl_ssl_address: kafka公网SASL_SSL接入方式连接地址。
        :type public_sasl_ssl_address: str
        :param public_sasl_ssl_domain_name: 公网SASL_SSL连接域名
        :type public_sasl_ssl_domain_name: str
        :param public_sasl_plaintext_enable: 实例是否支持公网SASL_PLAINTEXT访问接入方式。  - true，实例支持公网SASL_PLAINTEXT访问方式接入方式。  - false，实例不支持公网SASL_PLAINTEXT访问接入方式。
        :type public_sasl_plaintext_enable: bool
        :param public_sasl_plaintext_address: kafka公网SASL_PLAINTEXT接入方式连接地址。
        :type public_sasl_plaintext_address: str
        :param public_sasl_plaintext_domain_name: 公网SASL_PLAINTEXT连接域名
        :type public_sasl_plaintext_domain_name: str
        """
        
        

        self._private_plain_enable = None
        self._private_plain_address = None
        self._private_plain_domain_name = None
        self._private_sasl_ssl_enable = None
        self._private_sasl_ssl_address = None
        self._private_sasl_ssl_domain_name = None
        self._private_sasl_plaintext_enable = None
        self._private_sasl_plaintext_address = None
        self._private_sasl_plaintext_domain_name = None
        self._public_plain_enable = None
        self._public_plain_address = None
        self._public_plain_domain_name = None
        self._public_sasl_ssl_enable = None
        self._public_sasl_ssl_address = None
        self._public_sasl_ssl_domain_name = None
        self._public_sasl_plaintext_enable = None
        self._public_sasl_plaintext_address = None
        self._public_sasl_plaintext_domain_name = None
        self.discriminator = None

        if private_plain_enable is not None:
            self.private_plain_enable = private_plain_enable
        if private_plain_address is not None:
            self.private_plain_address = private_plain_address
        if private_plain_domain_name is not None:
            self.private_plain_domain_name = private_plain_domain_name
        if private_sasl_ssl_enable is not None:
            self.private_sasl_ssl_enable = private_sasl_ssl_enable
        if private_sasl_ssl_address is not None:
            self.private_sasl_ssl_address = private_sasl_ssl_address
        if private_sasl_ssl_domain_name is not None:
            self.private_sasl_ssl_domain_name = private_sasl_ssl_domain_name
        if private_sasl_plaintext_enable is not None:
            self.private_sasl_plaintext_enable = private_sasl_plaintext_enable
        if private_sasl_plaintext_address is not None:
            self.private_sasl_plaintext_address = private_sasl_plaintext_address
        if private_sasl_plaintext_domain_name is not None:
            self.private_sasl_plaintext_domain_name = private_sasl_plaintext_domain_name
        if public_plain_enable is not None:
            self.public_plain_enable = public_plain_enable
        if public_plain_address is not None:
            self.public_plain_address = public_plain_address
        if public_plain_domain_name is not None:
            self.public_plain_domain_name = public_plain_domain_name
        if public_sasl_ssl_enable is not None:
            self.public_sasl_ssl_enable = public_sasl_ssl_enable
        if public_sasl_ssl_address is not None:
            self.public_sasl_ssl_address = public_sasl_ssl_address
        if public_sasl_ssl_domain_name is not None:
            self.public_sasl_ssl_domain_name = public_sasl_ssl_domain_name
        if public_sasl_plaintext_enable is not None:
            self.public_sasl_plaintext_enable = public_sasl_plaintext_enable
        if public_sasl_plaintext_address is not None:
            self.public_sasl_plaintext_address = public_sasl_plaintext_address
        if public_sasl_plaintext_domain_name is not None:
            self.public_sasl_plaintext_domain_name = public_sasl_plaintext_domain_name

    @property
    def private_plain_enable(self):
        r"""Gets the private_plain_enable of this PortProtocolsEntity.

        实例是否支持内网PLAINTEXT访问接入方式。  - true：实例支持内网PLAINTEXT访问方式接入方式。  - false：实例不支持内网PLAINTEXT访问接入方式。

        :return: The private_plain_enable of this PortProtocolsEntity.
        :rtype: bool
        """
        return self._private_plain_enable

    @private_plain_enable.setter
    def private_plain_enable(self, private_plain_enable):
        r"""Sets the private_plain_enable of this PortProtocolsEntity.

        实例是否支持内网PLAINTEXT访问接入方式。  - true：实例支持内网PLAINTEXT访问方式接入方式。  - false：实例不支持内网PLAINTEXT访问接入方式。

        :param private_plain_enable: The private_plain_enable of this PortProtocolsEntity.
        :type private_plain_enable: bool
        """
        self._private_plain_enable = private_plain_enable

    @property
    def private_plain_address(self):
        r"""Gets the private_plain_address of this PortProtocolsEntity.

        kafka内网PLAINTEXT接入方式连接地址。

        :return: The private_plain_address of this PortProtocolsEntity.
        :rtype: str
        """
        return self._private_plain_address

    @private_plain_address.setter
    def private_plain_address(self, private_plain_address):
        r"""Sets the private_plain_address of this PortProtocolsEntity.

        kafka内网PLAINTEXT接入方式连接地址。

        :param private_plain_address: The private_plain_address of this PortProtocolsEntity.
        :type private_plain_address: str
        """
        self._private_plain_address = private_plain_address

    @property
    def private_plain_domain_name(self):
        r"""Gets the private_plain_domain_name of this PortProtocolsEntity.

        内网明文连接域名

        :return: The private_plain_domain_name of this PortProtocolsEntity.
        :rtype: str
        """
        return self._private_plain_domain_name

    @private_plain_domain_name.setter
    def private_plain_domain_name(self, private_plain_domain_name):
        r"""Sets the private_plain_domain_name of this PortProtocolsEntity.

        内网明文连接域名

        :param private_plain_domain_name: The private_plain_domain_name of this PortProtocolsEntity.
        :type private_plain_domain_name: str
        """
        self._private_plain_domain_name = private_plain_domain_name

    @property
    def private_sasl_ssl_enable(self):
        r"""Gets the private_sasl_ssl_enable of this PortProtocolsEntity.

        实例是否支持内网SASL_SSL访问接入方式。  - true：实例支持内网SASL_SSL访问方式接入方式。  - false：实例不支持内网SASL_SSL访问接入方式。

        :return: The private_sasl_ssl_enable of this PortProtocolsEntity.
        :rtype: bool
        """
        return self._private_sasl_ssl_enable

    @private_sasl_ssl_enable.setter
    def private_sasl_ssl_enable(self, private_sasl_ssl_enable):
        r"""Sets the private_sasl_ssl_enable of this PortProtocolsEntity.

        实例是否支持内网SASL_SSL访问接入方式。  - true：实例支持内网SASL_SSL访问方式接入方式。  - false：实例不支持内网SASL_SSL访问接入方式。

        :param private_sasl_ssl_enable: The private_sasl_ssl_enable of this PortProtocolsEntity.
        :type private_sasl_ssl_enable: bool
        """
        self._private_sasl_ssl_enable = private_sasl_ssl_enable

    @property
    def private_sasl_ssl_address(self):
        r"""Gets the private_sasl_ssl_address of this PortProtocolsEntity.

        kafka内网SASL_SSL接入方式连接地址。

        :return: The private_sasl_ssl_address of this PortProtocolsEntity.
        :rtype: str
        """
        return self._private_sasl_ssl_address

    @private_sasl_ssl_address.setter
    def private_sasl_ssl_address(self, private_sasl_ssl_address):
        r"""Sets the private_sasl_ssl_address of this PortProtocolsEntity.

        kafka内网SASL_SSL接入方式连接地址。

        :param private_sasl_ssl_address: The private_sasl_ssl_address of this PortProtocolsEntity.
        :type private_sasl_ssl_address: str
        """
        self._private_sasl_ssl_address = private_sasl_ssl_address

    @property
    def private_sasl_ssl_domain_name(self):
        r"""Gets the private_sasl_ssl_domain_name of this PortProtocolsEntity.

        内网SASL_SSL连接域名

        :return: The private_sasl_ssl_domain_name of this PortProtocolsEntity.
        :rtype: str
        """
        return self._private_sasl_ssl_domain_name

    @private_sasl_ssl_domain_name.setter
    def private_sasl_ssl_domain_name(self, private_sasl_ssl_domain_name):
        r"""Sets the private_sasl_ssl_domain_name of this PortProtocolsEntity.

        内网SASL_SSL连接域名

        :param private_sasl_ssl_domain_name: The private_sasl_ssl_domain_name of this PortProtocolsEntity.
        :type private_sasl_ssl_domain_name: str
        """
        self._private_sasl_ssl_domain_name = private_sasl_ssl_domain_name

    @property
    def private_sasl_plaintext_enable(self):
        r"""Gets the private_sasl_plaintext_enable of this PortProtocolsEntity.

        实例是否支持内网SASL_PLAINTEXT访问接入方式。  - true，实例支持内网SASL_PLAINTEXT访问方式接入方式。  - false，实例不支持内网SASL_PLAINTEXT访问接入方式。

        :return: The private_sasl_plaintext_enable of this PortProtocolsEntity.
        :rtype: bool
        """
        return self._private_sasl_plaintext_enable

    @private_sasl_plaintext_enable.setter
    def private_sasl_plaintext_enable(self, private_sasl_plaintext_enable):
        r"""Sets the private_sasl_plaintext_enable of this PortProtocolsEntity.

        实例是否支持内网SASL_PLAINTEXT访问接入方式。  - true，实例支持内网SASL_PLAINTEXT访问方式接入方式。  - false，实例不支持内网SASL_PLAINTEXT访问接入方式。

        :param private_sasl_plaintext_enable: The private_sasl_plaintext_enable of this PortProtocolsEntity.
        :type private_sasl_plaintext_enable: bool
        """
        self._private_sasl_plaintext_enable = private_sasl_plaintext_enable

    @property
    def private_sasl_plaintext_address(self):
        r"""Gets the private_sasl_plaintext_address of this PortProtocolsEntity.

        kafka内网SASL_PLAINTEXT接入方式连接地址。

        :return: The private_sasl_plaintext_address of this PortProtocolsEntity.
        :rtype: str
        """
        return self._private_sasl_plaintext_address

    @private_sasl_plaintext_address.setter
    def private_sasl_plaintext_address(self, private_sasl_plaintext_address):
        r"""Sets the private_sasl_plaintext_address of this PortProtocolsEntity.

        kafka内网SASL_PLAINTEXT接入方式连接地址。

        :param private_sasl_plaintext_address: The private_sasl_plaintext_address of this PortProtocolsEntity.
        :type private_sasl_plaintext_address: str
        """
        self._private_sasl_plaintext_address = private_sasl_plaintext_address

    @property
    def private_sasl_plaintext_domain_name(self):
        r"""Gets the private_sasl_plaintext_domain_name of this PortProtocolsEntity.

        内网SASL_PLAINTEXT连接域名

        :return: The private_sasl_plaintext_domain_name of this PortProtocolsEntity.
        :rtype: str
        """
        return self._private_sasl_plaintext_domain_name

    @private_sasl_plaintext_domain_name.setter
    def private_sasl_plaintext_domain_name(self, private_sasl_plaintext_domain_name):
        r"""Sets the private_sasl_plaintext_domain_name of this PortProtocolsEntity.

        内网SASL_PLAINTEXT连接域名

        :param private_sasl_plaintext_domain_name: The private_sasl_plaintext_domain_name of this PortProtocolsEntity.
        :type private_sasl_plaintext_domain_name: str
        """
        self._private_sasl_plaintext_domain_name = private_sasl_plaintext_domain_name

    @property
    def public_plain_enable(self):
        r"""Gets the public_plain_enable of this PortProtocolsEntity.

        实例是否支持公网PLAINTEXT访问接入方式。  - true，实例支持公网PLAINTEXT访问方式接入方式。  - false，实例不支持公网PLAINTEXT访问接入方式。

        :return: The public_plain_enable of this PortProtocolsEntity.
        :rtype: bool
        """
        return self._public_plain_enable

    @public_plain_enable.setter
    def public_plain_enable(self, public_plain_enable):
        r"""Sets the public_plain_enable of this PortProtocolsEntity.

        实例是否支持公网PLAINTEXT访问接入方式。  - true，实例支持公网PLAINTEXT访问方式接入方式。  - false，实例不支持公网PLAINTEXT访问接入方式。

        :param public_plain_enable: The public_plain_enable of this PortProtocolsEntity.
        :type public_plain_enable: bool
        """
        self._public_plain_enable = public_plain_enable

    @property
    def public_plain_address(self):
        r"""Gets the public_plain_address of this PortProtocolsEntity.

        kafka公网PLAINTEXT接入方式连接地址。

        :return: The public_plain_address of this PortProtocolsEntity.
        :rtype: str
        """
        return self._public_plain_address

    @public_plain_address.setter
    def public_plain_address(self, public_plain_address):
        r"""Sets the public_plain_address of this PortProtocolsEntity.

        kafka公网PLAINTEXT接入方式连接地址。

        :param public_plain_address: The public_plain_address of this PortProtocolsEntity.
        :type public_plain_address: str
        """
        self._public_plain_address = public_plain_address

    @property
    def public_plain_domain_name(self):
        r"""Gets the public_plain_domain_name of this PortProtocolsEntity.

        公网明文连接域名

        :return: The public_plain_domain_name of this PortProtocolsEntity.
        :rtype: str
        """
        return self._public_plain_domain_name

    @public_plain_domain_name.setter
    def public_plain_domain_name(self, public_plain_domain_name):
        r"""Sets the public_plain_domain_name of this PortProtocolsEntity.

        公网明文连接域名

        :param public_plain_domain_name: The public_plain_domain_name of this PortProtocolsEntity.
        :type public_plain_domain_name: str
        """
        self._public_plain_domain_name = public_plain_domain_name

    @property
    def public_sasl_ssl_enable(self):
        r"""Gets the public_sasl_ssl_enable of this PortProtocolsEntity.

        实例是否支持公网SASL_SSL访问接入方式。  - true，实例支持内网SASL_SSL访问方式接入方式。  - false，实例不支持公网SASL_SSL访问接入方式。

        :return: The public_sasl_ssl_enable of this PortProtocolsEntity.
        :rtype: bool
        """
        return self._public_sasl_ssl_enable

    @public_sasl_ssl_enable.setter
    def public_sasl_ssl_enable(self, public_sasl_ssl_enable):
        r"""Sets the public_sasl_ssl_enable of this PortProtocolsEntity.

        实例是否支持公网SASL_SSL访问接入方式。  - true，实例支持内网SASL_SSL访问方式接入方式。  - false，实例不支持公网SASL_SSL访问接入方式。

        :param public_sasl_ssl_enable: The public_sasl_ssl_enable of this PortProtocolsEntity.
        :type public_sasl_ssl_enable: bool
        """
        self._public_sasl_ssl_enable = public_sasl_ssl_enable

    @property
    def public_sasl_ssl_address(self):
        r"""Gets the public_sasl_ssl_address of this PortProtocolsEntity.

        kafka公网SASL_SSL接入方式连接地址。

        :return: The public_sasl_ssl_address of this PortProtocolsEntity.
        :rtype: str
        """
        return self._public_sasl_ssl_address

    @public_sasl_ssl_address.setter
    def public_sasl_ssl_address(self, public_sasl_ssl_address):
        r"""Sets the public_sasl_ssl_address of this PortProtocolsEntity.

        kafka公网SASL_SSL接入方式连接地址。

        :param public_sasl_ssl_address: The public_sasl_ssl_address of this PortProtocolsEntity.
        :type public_sasl_ssl_address: str
        """
        self._public_sasl_ssl_address = public_sasl_ssl_address

    @property
    def public_sasl_ssl_domain_name(self):
        r"""Gets the public_sasl_ssl_domain_name of this PortProtocolsEntity.

        公网SASL_SSL连接域名

        :return: The public_sasl_ssl_domain_name of this PortProtocolsEntity.
        :rtype: str
        """
        return self._public_sasl_ssl_domain_name

    @public_sasl_ssl_domain_name.setter
    def public_sasl_ssl_domain_name(self, public_sasl_ssl_domain_name):
        r"""Sets the public_sasl_ssl_domain_name of this PortProtocolsEntity.

        公网SASL_SSL连接域名

        :param public_sasl_ssl_domain_name: The public_sasl_ssl_domain_name of this PortProtocolsEntity.
        :type public_sasl_ssl_domain_name: str
        """
        self._public_sasl_ssl_domain_name = public_sasl_ssl_domain_name

    @property
    def public_sasl_plaintext_enable(self):
        r"""Gets the public_sasl_plaintext_enable of this PortProtocolsEntity.

        实例是否支持公网SASL_PLAINTEXT访问接入方式。  - true，实例支持公网SASL_PLAINTEXT访问方式接入方式。  - false，实例不支持公网SASL_PLAINTEXT访问接入方式。

        :return: The public_sasl_plaintext_enable of this PortProtocolsEntity.
        :rtype: bool
        """
        return self._public_sasl_plaintext_enable

    @public_sasl_plaintext_enable.setter
    def public_sasl_plaintext_enable(self, public_sasl_plaintext_enable):
        r"""Sets the public_sasl_plaintext_enable of this PortProtocolsEntity.

        实例是否支持公网SASL_PLAINTEXT访问接入方式。  - true，实例支持公网SASL_PLAINTEXT访问方式接入方式。  - false，实例不支持公网SASL_PLAINTEXT访问接入方式。

        :param public_sasl_plaintext_enable: The public_sasl_plaintext_enable of this PortProtocolsEntity.
        :type public_sasl_plaintext_enable: bool
        """
        self._public_sasl_plaintext_enable = public_sasl_plaintext_enable

    @property
    def public_sasl_plaintext_address(self):
        r"""Gets the public_sasl_plaintext_address of this PortProtocolsEntity.

        kafka公网SASL_PLAINTEXT接入方式连接地址。

        :return: The public_sasl_plaintext_address of this PortProtocolsEntity.
        :rtype: str
        """
        return self._public_sasl_plaintext_address

    @public_sasl_plaintext_address.setter
    def public_sasl_plaintext_address(self, public_sasl_plaintext_address):
        r"""Sets the public_sasl_plaintext_address of this PortProtocolsEntity.

        kafka公网SASL_PLAINTEXT接入方式连接地址。

        :param public_sasl_plaintext_address: The public_sasl_plaintext_address of this PortProtocolsEntity.
        :type public_sasl_plaintext_address: str
        """
        self._public_sasl_plaintext_address = public_sasl_plaintext_address

    @property
    def public_sasl_plaintext_domain_name(self):
        r"""Gets the public_sasl_plaintext_domain_name of this PortProtocolsEntity.

        公网SASL_PLAINTEXT连接域名

        :return: The public_sasl_plaintext_domain_name of this PortProtocolsEntity.
        :rtype: str
        """
        return self._public_sasl_plaintext_domain_name

    @public_sasl_plaintext_domain_name.setter
    def public_sasl_plaintext_domain_name(self, public_sasl_plaintext_domain_name):
        r"""Sets the public_sasl_plaintext_domain_name of this PortProtocolsEntity.

        公网SASL_PLAINTEXT连接域名

        :param public_sasl_plaintext_domain_name: The public_sasl_plaintext_domain_name of this PortProtocolsEntity.
        :type public_sasl_plaintext_domain_name: str
        """
        self._public_sasl_plaintext_domain_name = public_sasl_plaintext_domain_name

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                if attr in self.sensitive_list:
                    result[attr] = "****"
                else:
                    result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        import simplejson as json
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PortProtocolsEntity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
