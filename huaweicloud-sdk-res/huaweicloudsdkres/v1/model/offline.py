# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Offline:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'user_url': 'str',
        'item_url': 'str',
        'behavior_url': 'str'
    }

    attribute_map = {
        'user_url': 'user_url',
        'item_url': 'item_url',
        'behavior_url': 'behavior_url'
    }

    def __init__(self, user_url=None, item_url=None, behavior_url=None):
        """Offline

        The model defined in huaweicloud sdk

        :param user_url: 用户数据url。
        :type user_url: str
        :param item_url: 物品数据url。
        :type item_url: str
        :param behavior_url: 行为数据url。
        :type behavior_url: str
        """
        
        

        self._user_url = None
        self._item_url = None
        self._behavior_url = None
        self.discriminator = None

        self.user_url = user_url
        self.item_url = item_url
        self.behavior_url = behavior_url

    @property
    def user_url(self):
        """Gets the user_url of this Offline.

        用户数据url。

        :return: The user_url of this Offline.
        :rtype: str
        """
        return self._user_url

    @user_url.setter
    def user_url(self, user_url):
        """Sets the user_url of this Offline.

        用户数据url。

        :param user_url: The user_url of this Offline.
        :type user_url: str
        """
        self._user_url = user_url

    @property
    def item_url(self):
        """Gets the item_url of this Offline.

        物品数据url。

        :return: The item_url of this Offline.
        :rtype: str
        """
        return self._item_url

    @item_url.setter
    def item_url(self, item_url):
        """Sets the item_url of this Offline.

        物品数据url。

        :param item_url: The item_url of this Offline.
        :type item_url: str
        """
        self._item_url = item_url

    @property
    def behavior_url(self):
        """Gets the behavior_url of this Offline.

        行为数据url。

        :return: The behavior_url of this Offline.
        :rtype: str
        """
        return self._behavior_url

    @behavior_url.setter
    def behavior_url(self, behavior_url):
        """Sets the behavior_url of this Offline.

        行为数据url。

        :param behavior_url: The behavior_url of this Offline.
        :type behavior_url: str
        """
        self._behavior_url = behavior_url

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
        if not isinstance(other, Offline):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
