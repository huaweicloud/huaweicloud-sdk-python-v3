# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddSshKeyRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'key': 'str',
        'title': 'str'
    }

    attribute_map = {
        'key': 'key',
        'title': 'title'
    }

    def __init__(self, key=None, title=None):
        """AddSshKeyRequestBody

        The model defined in huaweicloud sdk

        :param key: 密钥
        :type key: str
        :param title: 密钥名称
        :type title: str
        """
        
        

        self._key = None
        self._title = None
        self.discriminator = None

        self.key = key
        self.title = title

    @property
    def key(self):
        """Gets the key of this AddSshKeyRequestBody.

        密钥

        :return: The key of this AddSshKeyRequestBody.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this AddSshKeyRequestBody.

        密钥

        :param key: The key of this AddSshKeyRequestBody.
        :type key: str
        """
        self._key = key

    @property
    def title(self):
        """Gets the title of this AddSshKeyRequestBody.

        密钥名称

        :return: The title of this AddSshKeyRequestBody.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this AddSshKeyRequestBody.

        密钥名称

        :param title: The title of this AddSshKeyRequestBody.
        :type title: str
        """
        self._title = title

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
        if not isinstance(other, AddSshKeyRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
