# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateKeypairRequestBody:

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
        'public_key': 'str'
    }

    attribute_map = {
        'name': 'name',
        'public_key': 'public_key'
    }

    def __init__(self, name=None, public_key=None):
        """CreateKeypairRequestBody

        The model defined in huaweicloud sdk

        :param name: 密钥对名称。 新创建的密钥名称不能和已有密钥名称相同。
        :type name: str
        :param public_key: 导入的公钥信息。 建议导入的公钥长度不大于1024字节。 &gt; 长度超过1024字节会导致边缘实例注入该密钥失败。
        :type public_key: str
        """
        
        

        self._name = None
        self._public_key = None
        self.discriminator = None

        self.name = name
        if public_key is not None:
            self.public_key = public_key

    @property
    def name(self):
        """Gets the name of this CreateKeypairRequestBody.

        密钥对名称。 新创建的密钥名称不能和已有密钥名称相同。

        :return: The name of this CreateKeypairRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateKeypairRequestBody.

        密钥对名称。 新创建的密钥名称不能和已有密钥名称相同。

        :param name: The name of this CreateKeypairRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def public_key(self):
        """Gets the public_key of this CreateKeypairRequestBody.

        导入的公钥信息。 建议导入的公钥长度不大于1024字节。 > 长度超过1024字节会导致边缘实例注入该密钥失败。

        :return: The public_key of this CreateKeypairRequestBody.
        :rtype: str
        """
        return self._public_key

    @public_key.setter
    def public_key(self, public_key):
        """Sets the public_key of this CreateKeypairRequestBody.

        导入的公钥信息。 建议导入的公钥长度不大于1024字节。 > 长度超过1024字节会导致边缘实例注入该密钥失败。

        :param public_key: The public_key of this CreateKeypairRequestBody.
        :type public_key: str
        """
        self._public_key = public_key

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
        if not isinstance(other, CreateKeypairRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
