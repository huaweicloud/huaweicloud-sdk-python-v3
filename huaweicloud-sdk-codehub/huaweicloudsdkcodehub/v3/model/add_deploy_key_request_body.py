# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddDeployKeyRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'application': 'str',
        'can_push': 'bool',
        'key': 'str',
        'key_title': 'str'
    }

    attribute_map = {
        'application': 'application',
        'can_push': 'can_push',
        'key': 'key',
        'key_title': 'key_title'
    }

    def __init__(self, application=None, can_push=None, key=None, key_title=None):
        """AddDeployKeyRequestBody

        The model defined in huaweicloud sdk

        :param application: 部署使用的SSH密钥的来源
        :type application: str
        :param can_push: 部署使用的SSH密钥是否可以推送代码
        :type can_push: bool
        :param key: 部署使用的SSH密钥
        :type key: str
        :param key_title: 部署使用的SSH密钥名称
        :type key_title: str
        """
        
        

        self._application = None
        self._can_push = None
        self._key = None
        self._key_title = None
        self.discriminator = None

        self.application = application
        self.can_push = can_push
        self.key = key
        self.key_title = key_title

    @property
    def application(self):
        """Gets the application of this AddDeployKeyRequestBody.

        部署使用的SSH密钥的来源

        :return: The application of this AddDeployKeyRequestBody.
        :rtype: str
        """
        return self._application

    @application.setter
    def application(self, application):
        """Sets the application of this AddDeployKeyRequestBody.

        部署使用的SSH密钥的来源

        :param application: The application of this AddDeployKeyRequestBody.
        :type application: str
        """
        self._application = application

    @property
    def can_push(self):
        """Gets the can_push of this AddDeployKeyRequestBody.

        部署使用的SSH密钥是否可以推送代码

        :return: The can_push of this AddDeployKeyRequestBody.
        :rtype: bool
        """
        return self._can_push

    @can_push.setter
    def can_push(self, can_push):
        """Sets the can_push of this AddDeployKeyRequestBody.

        部署使用的SSH密钥是否可以推送代码

        :param can_push: The can_push of this AddDeployKeyRequestBody.
        :type can_push: bool
        """
        self._can_push = can_push

    @property
    def key(self):
        """Gets the key of this AddDeployKeyRequestBody.

        部署使用的SSH密钥

        :return: The key of this AddDeployKeyRequestBody.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this AddDeployKeyRequestBody.

        部署使用的SSH密钥

        :param key: The key of this AddDeployKeyRequestBody.
        :type key: str
        """
        self._key = key

    @property
    def key_title(self):
        """Gets the key_title of this AddDeployKeyRequestBody.

        部署使用的SSH密钥名称

        :return: The key_title of this AddDeployKeyRequestBody.
        :rtype: str
        """
        return self._key_title

    @key_title.setter
    def key_title(self, key_title):
        """Sets the key_title of this AddDeployKeyRequestBody.

        部署使用的SSH密钥名称

        :param key_title: The key_title of this AddDeployKeyRequestBody.
        :type key_title: str
        """
        self._key_title = key_title

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
        if not isinstance(other, AddDeployKeyRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
