# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Hook:

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
        'type': 'str',
        'callback_url': 'str'
    }

    attribute_map = {
        'id': 'id',
        'type': 'type',
        'callback_url': 'callback_url'
    }

    def __init__(self, id=None, type=None, callback_url=None):
        """Hook

        The model defined in huaweicloud sdk

        :param id: hook ID。
        :type id: str
        :param type: hook类型。
        :type type: str
        :param callback_url: 回滚URL。
        :type callback_url: str
        """
        
        

        self._id = None
        self._type = None
        self._callback_url = None
        self.discriminator = None

        self.id = id
        self.type = type
        self.callback_url = callback_url

    @property
    def id(self):
        """Gets the id of this Hook.

        hook ID。

        :return: The id of this Hook.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Hook.

        hook ID。

        :param id: The id of this Hook.
        :type id: str
        """
        self._id = id

    @property
    def type(self):
        """Gets the type of this Hook.

        hook类型。

        :return: The type of this Hook.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Hook.

        hook类型。

        :param type: The type of this Hook.
        :type type: str
        """
        self._type = type

    @property
    def callback_url(self):
        """Gets the callback_url of this Hook.

        回滚URL。

        :return: The callback_url of this Hook.
        :rtype: str
        """
        return self._callback_url

    @callback_url.setter
    def callback_url(self, callback_url):
        """Sets the callback_url of this Hook.

        回滚URL。

        :param callback_url: The callback_url of this Hook.
        :type callback_url: str
        """
        self._callback_url = callback_url

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
        if not isinstance(other, Hook):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
