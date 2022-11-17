# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Key:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'can_push': 'bool',
        'created_at': 'str',
        'key': 'str',
        'key_id': 'str',
        'key_title': 'str'
    }

    attribute_map = {
        'can_push': 'can_push',
        'created_at': 'created_at',
        'key': 'key',
        'key_id': 'key_id',
        'key_title': 'key_title'
    }

    def __init__(self, can_push=None, created_at=None, key=None, key_id=None, key_title=None):
        """Key

        The model defined in huaweicloud sdk

        :param can_push: 是否允许推送
        :type can_push: bool
        :param created_at: 部署密钥新建时间
        :type created_at: str
        :param key: 部署密钥
        :type key: str
        :param key_id: 部署密钥id
        :type key_id: str
        :param key_title: 部署密钥名称
        :type key_title: str
        """
        
        

        self._can_push = None
        self._created_at = None
        self._key = None
        self._key_id = None
        self._key_title = None
        self.discriminator = None

        if can_push is not None:
            self.can_push = can_push
        if created_at is not None:
            self.created_at = created_at
        if key is not None:
            self.key = key
        if key_id is not None:
            self.key_id = key_id
        if key_title is not None:
            self.key_title = key_title

    @property
    def can_push(self):
        """Gets the can_push of this Key.

        是否允许推送

        :return: The can_push of this Key.
        :rtype: bool
        """
        return self._can_push

    @can_push.setter
    def can_push(self, can_push):
        """Sets the can_push of this Key.

        是否允许推送

        :param can_push: The can_push of this Key.
        :type can_push: bool
        """
        self._can_push = can_push

    @property
    def created_at(self):
        """Gets the created_at of this Key.

        部署密钥新建时间

        :return: The created_at of this Key.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Key.

        部署密钥新建时间

        :param created_at: The created_at of this Key.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def key(self):
        """Gets the key of this Key.

        部署密钥

        :return: The key of this Key.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this Key.

        部署密钥

        :param key: The key of this Key.
        :type key: str
        """
        self._key = key

    @property
    def key_id(self):
        """Gets the key_id of this Key.

        部署密钥id

        :return: The key_id of this Key.
        :rtype: str
        """
        return self._key_id

    @key_id.setter
    def key_id(self, key_id):
        """Sets the key_id of this Key.

        部署密钥id

        :param key_id: The key_id of this Key.
        :type key_id: str
        """
        self._key_id = key_id

    @property
    def key_title(self):
        """Gets the key_title of this Key.

        部署密钥名称

        :return: The key_title of this Key.
        :rtype: str
        """
        return self._key_title

    @key_title.setter
    def key_title(self, key_title):
        """Sets the key_title of this Key.

        部署密钥名称

        :param key_title: The key_title of this Key.
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
        if not isinstance(other, Key):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
