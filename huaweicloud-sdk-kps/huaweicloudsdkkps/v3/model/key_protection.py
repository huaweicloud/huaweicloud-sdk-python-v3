# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class KeyProtection:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'private_key': 'str',
        'encryption': 'Encryption'
    }

    attribute_map = {
        'private_key': 'private_key',
        'encryption': 'encryption'
    }

    def __init__(self, private_key=None, encryption=None):
        r"""KeyProtection

        The model defined in huaweicloud sdk

        :param private_key: 导入SSH密钥对的私钥。
        :type private_key: str
        :param encryption: 
        :type encryption: :class:`huaweicloudsdkkps.v3.Encryption`
        """
        
        

        self._private_key = None
        self._encryption = None
        self.discriminator = None

        if private_key is not None:
            self.private_key = private_key
        self.encryption = encryption

    @property
    def private_key(self):
        r"""Gets the private_key of this KeyProtection.

        导入SSH密钥对的私钥。

        :return: The private_key of this KeyProtection.
        :rtype: str
        """
        return self._private_key

    @private_key.setter
    def private_key(self, private_key):
        r"""Sets the private_key of this KeyProtection.

        导入SSH密钥对的私钥。

        :param private_key: The private_key of this KeyProtection.
        :type private_key: str
        """
        self._private_key = private_key

    @property
    def encryption(self):
        r"""Gets the encryption of this KeyProtection.

        :return: The encryption of this KeyProtection.
        :rtype: :class:`huaweicloudsdkkps.v3.Encryption`
        """
        return self._encryption

    @encryption.setter
    def encryption(self, encryption):
        r"""Sets the encryption of this KeyProtection.

        :param encryption: The encryption of this KeyProtection.
        :type encryption: :class:`huaweicloudsdkkps.v3.Encryption`
        """
        self._encryption = encryption

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
        if not isinstance(other, KeyProtection):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
