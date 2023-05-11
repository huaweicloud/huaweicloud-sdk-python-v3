# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EncryptDataNodeReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'encrypt_datas': 'list[str]'
    }

    attribute_map = {
        'encrypt_datas': 'encrypt_datas'
    }

    def __init__(self, encrypt_datas=None):
        """EncryptDataNodeReq

        The model defined in huaweicloud sdk

        :param encrypt_datas: 加密数据ID列表
        :type encrypt_datas: list[str]
        """
        
        

        self._encrypt_datas = None
        self.discriminator = None

        self.encrypt_datas = encrypt_datas

    @property
    def encrypt_datas(self):
        """Gets the encrypt_datas of this EncryptDataNodeReq.

        加密数据ID列表

        :return: The encrypt_datas of this EncryptDataNodeReq.
        :rtype: list[str]
        """
        return self._encrypt_datas

    @encrypt_datas.setter
    def encrypt_datas(self, encrypt_datas):
        """Sets the encrypt_datas of this EncryptDataNodeReq.

        加密数据ID列表

        :param encrypt_datas: The encrypt_datas of this EncryptDataNodeReq.
        :type encrypt_datas: list[str]
        """
        self._encrypt_datas = encrypt_datas

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
        if not isinstance(other, EncryptDataNodeReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
