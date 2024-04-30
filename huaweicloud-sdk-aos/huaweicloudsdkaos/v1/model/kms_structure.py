# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class KmsStructure:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'cipher_text': 'str'
    }

    attribute_map = {
        'id': 'id',
        'cipher_text': 'cipher_text'
    }

    def __init__(self, id=None, cipher_text=None):
        """KmsStructure

        The model defined in huaweicloud sdk

        :param id: 解密时，资源编排服务应该使用的KMS密钥的ID，通常是加密时所使用的密钥ID
        :type id: str
        :param cipher_text: 数据加密密钥所对应的密文
        :type cipher_text: str
        """
        
        

        self._id = None
        self._cipher_text = None
        self.discriminator = None

        self.id = id
        self.cipher_text = cipher_text

    @property
    def id(self):
        """Gets the id of this KmsStructure.

        解密时，资源编排服务应该使用的KMS密钥的ID，通常是加密时所使用的密钥ID

        :return: The id of this KmsStructure.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this KmsStructure.

        解密时，资源编排服务应该使用的KMS密钥的ID，通常是加密时所使用的密钥ID

        :param id: The id of this KmsStructure.
        :type id: str
        """
        self._id = id

    @property
    def cipher_text(self):
        """Gets the cipher_text of this KmsStructure.

        数据加密密钥所对应的密文

        :return: The cipher_text of this KmsStructure.
        :rtype: str
        """
        return self._cipher_text

    @cipher_text.setter
    def cipher_text(self, cipher_text):
        """Sets the cipher_text of this KmsStructure.

        数据加密密钥所对应的密文

        :param cipher_text: The cipher_text of this KmsStructure.
        :type cipher_text: str
        """
        self._cipher_text = cipher_text

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
        if not isinstance(other, KmsStructure):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
