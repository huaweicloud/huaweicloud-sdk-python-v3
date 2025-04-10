# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateVgwIkePolicy:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'authentication_algorithm': 'str',
        'encryption_algorithm': 'str',
        'dh_group': 'str',
        'lifetime_seconds': 'int'
    }

    attribute_map = {
        'authentication_algorithm': 'authentication_algorithm',
        'encryption_algorithm': 'encryption_algorithm',
        'dh_group': 'dh_group',
        'lifetime_seconds': 'lifetime_seconds'
    }

    def __init__(self, authentication_algorithm=None, encryption_algorithm=None, dh_group=None, lifetime_seconds=None):
        r"""UpdateVgwIkePolicy

        The model defined in huaweicloud sdk

        :param authentication_algorithm: 加密算法
        :type authentication_algorithm: str
        :param encryption_algorithm: 加密算法
        :type encryption_algorithm: str
        :param dh_group: DH密钥组
        :type dh_group: str
        :param lifetime_seconds: 表示SA的生存周期，当该生存周期超时后IKE SA将自动更新
        :type lifetime_seconds: int
        """
        
        

        self._authentication_algorithm = None
        self._encryption_algorithm = None
        self._dh_group = None
        self._lifetime_seconds = None
        self.discriminator = None

        if authentication_algorithm is not None:
            self.authentication_algorithm = authentication_algorithm
        if encryption_algorithm is not None:
            self.encryption_algorithm = encryption_algorithm
        if dh_group is not None:
            self.dh_group = dh_group
        if lifetime_seconds is not None:
            self.lifetime_seconds = lifetime_seconds

    @property
    def authentication_algorithm(self):
        r"""Gets the authentication_algorithm of this UpdateVgwIkePolicy.

        加密算法

        :return: The authentication_algorithm of this UpdateVgwIkePolicy.
        :rtype: str
        """
        return self._authentication_algorithm

    @authentication_algorithm.setter
    def authentication_algorithm(self, authentication_algorithm):
        r"""Sets the authentication_algorithm of this UpdateVgwIkePolicy.

        加密算法

        :param authentication_algorithm: The authentication_algorithm of this UpdateVgwIkePolicy.
        :type authentication_algorithm: str
        """
        self._authentication_algorithm = authentication_algorithm

    @property
    def encryption_algorithm(self):
        r"""Gets the encryption_algorithm of this UpdateVgwIkePolicy.

        加密算法

        :return: The encryption_algorithm of this UpdateVgwIkePolicy.
        :rtype: str
        """
        return self._encryption_algorithm

    @encryption_algorithm.setter
    def encryption_algorithm(self, encryption_algorithm):
        r"""Sets the encryption_algorithm of this UpdateVgwIkePolicy.

        加密算法

        :param encryption_algorithm: The encryption_algorithm of this UpdateVgwIkePolicy.
        :type encryption_algorithm: str
        """
        self._encryption_algorithm = encryption_algorithm

    @property
    def dh_group(self):
        r"""Gets the dh_group of this UpdateVgwIkePolicy.

        DH密钥组

        :return: The dh_group of this UpdateVgwIkePolicy.
        :rtype: str
        """
        return self._dh_group

    @dh_group.setter
    def dh_group(self, dh_group):
        r"""Sets the dh_group of this UpdateVgwIkePolicy.

        DH密钥组

        :param dh_group: The dh_group of this UpdateVgwIkePolicy.
        :type dh_group: str
        """
        self._dh_group = dh_group

    @property
    def lifetime_seconds(self):
        r"""Gets the lifetime_seconds of this UpdateVgwIkePolicy.

        表示SA的生存周期，当该生存周期超时后IKE SA将自动更新

        :return: The lifetime_seconds of this UpdateVgwIkePolicy.
        :rtype: int
        """
        return self._lifetime_seconds

    @lifetime_seconds.setter
    def lifetime_seconds(self, lifetime_seconds):
        r"""Sets the lifetime_seconds of this UpdateVgwIkePolicy.

        表示SA的生存周期，当该生存周期超时后IKE SA将自动更新

        :param lifetime_seconds: The lifetime_seconds of this UpdateVgwIkePolicy.
        :type lifetime_seconds: int
        """
        self._lifetime_seconds = lifetime_seconds

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
        if not isinstance(other, UpdateVgwIkePolicy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
