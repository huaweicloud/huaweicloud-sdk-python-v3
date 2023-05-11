# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeploymentSecrets:

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
        'key': 'str'
    }

    attribute_map = {
        'name': 'name',
        'key': 'key'
    }

    def __init__(self, name=None, key=None):
        """DeploymentSecrets

        The model defined in huaweicloud sdk

        :param name: 密钥的名称，以英文小写字母开头，由中文字符，英文字母，数字，下划线和中划线组成，不能以中划线结尾，长度4-64位
        :type name: str
        :param key: 密钥的属性名，以英文字母和中划线开头，由英文字母、数字、点号、中划线和下划线组成，长度1-63位
        :type key: str
        """
        
        

        self._name = None
        self._key = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if key is not None:
            self.key = key

    @property
    def name(self):
        """Gets the name of this DeploymentSecrets.

        密钥的名称，以英文小写字母开头，由中文字符，英文字母，数字，下划线和中划线组成，不能以中划线结尾，长度4-64位

        :return: The name of this DeploymentSecrets.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DeploymentSecrets.

        密钥的名称，以英文小写字母开头，由中文字符，英文字母，数字，下划线和中划线组成，不能以中划线结尾，长度4-64位

        :param name: The name of this DeploymentSecrets.
        :type name: str
        """
        self._name = name

    @property
    def key(self):
        """Gets the key of this DeploymentSecrets.

        密钥的属性名，以英文字母和中划线开头，由英文字母、数字、点号、中划线和下划线组成，长度1-63位

        :return: The key of this DeploymentSecrets.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this DeploymentSecrets.

        密钥的属性名，以英文字母和中划线开头，由英文字母、数字、点号、中划线和下划线组成，长度1-63位

        :param key: The key of this DeploymentSecrets.
        :type key: str
        """
        self._key = key

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
        if not isinstance(other, DeploymentSecrets):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
