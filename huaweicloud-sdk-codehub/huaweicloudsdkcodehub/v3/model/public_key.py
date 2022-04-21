# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PublicKey:

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
        'key': 'str',
        'title': 'str'
    }

    attribute_map = {
        'id': 'id',
        'key': 'key',
        'title': 'title'
    }

    def __init__(self, id=None, key=None, title=None):
        """PublicKey

        The model defined in huaweicloud sdk

        :param id: 密钥id
        :type id: str
        :param key: 密钥
        :type key: str
        :param title: 密钥名称
        :type title: str
        """
        
        

        self._id = None
        self._key = None
        self._title = None
        self.discriminator = None

        self.id = id
        self.key = key
        self.title = title

    @property
    def id(self):
        """Gets the id of this PublicKey.

        密钥id

        :return: The id of this PublicKey.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PublicKey.

        密钥id

        :param id: The id of this PublicKey.
        :type id: str
        """
        self._id = id

    @property
    def key(self):
        """Gets the key of this PublicKey.

        密钥

        :return: The key of this PublicKey.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this PublicKey.

        密钥

        :param key: The key of this PublicKey.
        :type key: str
        """
        self._key = key

    @property
    def title(self):
        """Gets the title of this PublicKey.

        密钥名称

        :return: The title of this PublicKey.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this PublicKey.

        密钥名称

        :param title: The title of this PublicKey.
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
        if not isinstance(other, PublicKey):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
