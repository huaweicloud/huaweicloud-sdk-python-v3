# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Target:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'address': 'str',
        'auth_header': 'str',
        'skip_cert_verify': 'bool',
        'address_type': 'str'
    }

    attribute_map = {
        'type': 'type',
        'address': 'address',
        'auth_header': 'auth_header',
        'skip_cert_verify': 'skip_cert_verify',
        'address_type': 'address_type'
    }

    def __init__(self, type=None, address=None, auth_header=None, skip_cert_verify=None, address_type=None):
        r"""Target

        The model defined in huaweicloud sdk

        :param type: 触发器类型，可选http
        :type type: str
        :param address: 触发地址，不可修改
        :type address: str
        :param auth_header: 请求头，格式为key1:value1;key2:value2
        :type auth_header: str
        :param skip_cert_verify: 是否跳过证书认证
        :type skip_cert_verify: bool
        :param address_type: 触发地址类型，可选internal(内网)，internet(公网)。internal必须为内网ip形式。
        :type address_type: str
        """
        
        

        self._type = None
        self._address = None
        self._auth_header = None
        self._skip_cert_verify = None
        self._address_type = None
        self.discriminator = None

        self.type = type
        self.address = address
        if auth_header is not None:
            self.auth_header = auth_header
        if skip_cert_verify is not None:
            self.skip_cert_verify = skip_cert_verify
        self.address_type = address_type

    @property
    def type(self):
        r"""Gets the type of this Target.

        触发器类型，可选http

        :return: The type of this Target.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this Target.

        触发器类型，可选http

        :param type: The type of this Target.
        :type type: str
        """
        self._type = type

    @property
    def address(self):
        r"""Gets the address of this Target.

        触发地址，不可修改

        :return: The address of this Target.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        r"""Sets the address of this Target.

        触发地址，不可修改

        :param address: The address of this Target.
        :type address: str
        """
        self._address = address

    @property
    def auth_header(self):
        r"""Gets the auth_header of this Target.

        请求头，格式为key1:value1;key2:value2

        :return: The auth_header of this Target.
        :rtype: str
        """
        return self._auth_header

    @auth_header.setter
    def auth_header(self, auth_header):
        r"""Sets the auth_header of this Target.

        请求头，格式为key1:value1;key2:value2

        :param auth_header: The auth_header of this Target.
        :type auth_header: str
        """
        self._auth_header = auth_header

    @property
    def skip_cert_verify(self):
        r"""Gets the skip_cert_verify of this Target.

        是否跳过证书认证

        :return: The skip_cert_verify of this Target.
        :rtype: bool
        """
        return self._skip_cert_verify

    @skip_cert_verify.setter
    def skip_cert_verify(self, skip_cert_verify):
        r"""Sets the skip_cert_verify of this Target.

        是否跳过证书认证

        :param skip_cert_verify: The skip_cert_verify of this Target.
        :type skip_cert_verify: bool
        """
        self._skip_cert_verify = skip_cert_verify

    @property
    def address_type(self):
        r"""Gets the address_type of this Target.

        触发地址类型，可选internal(内网)，internet(公网)。internal必须为内网ip形式。

        :return: The address_type of this Target.
        :rtype: str
        """
        return self._address_type

    @address_type.setter
    def address_type(self, address_type):
        r"""Sets the address_type of this Target.

        触发地址类型，可选internal(内网)，internet(公网)。internal必须为内网ip形式。

        :param address_type: The address_type of this Target.
        :type address_type: str
        """
        self._address_type = address_type

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
        if not isinstance(other, Target):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
