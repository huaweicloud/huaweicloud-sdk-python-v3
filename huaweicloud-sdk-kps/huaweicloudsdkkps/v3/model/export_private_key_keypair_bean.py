# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExportPrivateKeyKeypairBean:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'private_key': 'str'
    }

    attribute_map = {
        'name': 'name',
        'private_key': 'private_key'
    }

    def __init__(self, name=None, private_key=None):
        """ExportPrivateKeyKeypairBean

        The model defined in huaweicloud sdk

        :param name: SSH密钥对的名称。
        :type name: str
        :param private_key: SSH密钥对的私钥
        :type private_key: str
        """
        
        

        self._name = None
        self._private_key = None
        self.discriminator = None

        self.name = name
        self.private_key = private_key

    @property
    def name(self):
        """Gets the name of this ExportPrivateKeyKeypairBean.

        SSH密钥对的名称。

        :return: The name of this ExportPrivateKeyKeypairBean.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ExportPrivateKeyKeypairBean.

        SSH密钥对的名称。

        :param name: The name of this ExportPrivateKeyKeypairBean.
        :type name: str
        """
        self._name = name

    @property
    def private_key(self):
        """Gets the private_key of this ExportPrivateKeyKeypairBean.

        SSH密钥对的私钥

        :return: The private_key of this ExportPrivateKeyKeypairBean.
        :rtype: str
        """
        return self._private_key

    @private_key.setter
    def private_key(self, private_key):
        """Sets the private_key of this ExportPrivateKeyKeypairBean.

        SSH密钥对的私钥

        :param private_key: The private_key of this ExportPrivateKeyKeypairBean.
        :type private_key: str
        """
        self._private_key = private_key

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
        if not isinstance(other, ExportPrivateKeyKeypairBean):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
