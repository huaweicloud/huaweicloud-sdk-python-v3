# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MysqlTdeInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enable_tde': 'bool',
        'encryption_type': 'str'
    }

    attribute_map = {
        'enable_tde': 'enable_tde',
        'encryption_type': 'encryption_type'
    }

    def __init__(self, enable_tde=None, encryption_type=None):
        r"""MysqlTdeInfo

        The model defined in huaweicloud sdk

        :param enable_tde: 是否打开透明加密功能。
        :type enable_tde: bool
        :param encryption_type: 透明加密算法，支持AES256、SM4加密算法。
        :type encryption_type: str
        """
        
        

        self._enable_tde = None
        self._encryption_type = None
        self.discriminator = None

        self.enable_tde = enable_tde
        self.encryption_type = encryption_type

    @property
    def enable_tde(self):
        r"""Gets the enable_tde of this MysqlTdeInfo.

        是否打开透明加密功能。

        :return: The enable_tde of this MysqlTdeInfo.
        :rtype: bool
        """
        return self._enable_tde

    @enable_tde.setter
    def enable_tde(self, enable_tde):
        r"""Sets the enable_tde of this MysqlTdeInfo.

        是否打开透明加密功能。

        :param enable_tde: The enable_tde of this MysqlTdeInfo.
        :type enable_tde: bool
        """
        self._enable_tde = enable_tde

    @property
    def encryption_type(self):
        r"""Gets the encryption_type of this MysqlTdeInfo.

        透明加密算法，支持AES256、SM4加密算法。

        :return: The encryption_type of this MysqlTdeInfo.
        :rtype: str
        """
        return self._encryption_type

    @encryption_type.setter
    def encryption_type(self, encryption_type):
        r"""Sets the encryption_type of this MysqlTdeInfo.

        透明加密算法，支持AES256、SM4加密算法。

        :param encryption_type: The encryption_type of this MysqlTdeInfo.
        :type encryption_type: str
        """
        self._encryption_type = encryption_type

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
        if not isinstance(other, MysqlTdeInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
