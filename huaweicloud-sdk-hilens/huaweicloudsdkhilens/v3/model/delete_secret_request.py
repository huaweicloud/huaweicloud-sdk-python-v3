# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteSecretRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'secret_id': 'str'
    }

    attribute_map = {
        'secret_id': 'secret_id'
    }

    def __init__(self, secret_id=None):
        """DeleteSecretRequest

        The model defined in huaweicloud sdk

        :param secret_id: 密钥ID，从专业版HiLens控制台密钥管理[获密钥列表](getSecretsListUsingGET.xml)获取
        :type secret_id: str
        """
        
        

        self._secret_id = None
        self.discriminator = None

        self.secret_id = secret_id

    @property
    def secret_id(self):
        """Gets the secret_id of this DeleteSecretRequest.

        密钥ID，从专业版HiLens控制台密钥管理[获密钥列表](getSecretsListUsingGET.xml)获取

        :return: The secret_id of this DeleteSecretRequest.
        :rtype: str
        """
        return self._secret_id

    @secret_id.setter
    def secret_id(self, secret_id):
        """Sets the secret_id of this DeleteSecretRequest.

        密钥ID，从专业版HiLens控制台密钥管理[获密钥列表](getSecretsListUsingGET.xml)获取

        :param secret_id: The secret_id of this DeleteSecretRequest.
        :type secret_id: str
        """
        self._secret_id = secret_id

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
        if not isinstance(other, DeleteSecretRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
