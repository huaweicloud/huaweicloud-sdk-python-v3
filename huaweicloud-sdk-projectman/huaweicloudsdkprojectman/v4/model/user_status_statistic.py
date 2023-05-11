# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UserStatusStatistic:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'user': 'IssueUser',
        'item_count': 'int',
        'data': 'dict(str, int)'
    }

    attribute_map = {
        'user': 'user',
        'item_count': 'item_count',
        'data': 'data'
    }

    def __init__(self, user=None, item_count=None, data=None):
        """UserStatusStatistic

        The model defined in huaweicloud sdk

        :param user: 
        :type user: :class:`huaweicloudsdkprojectman.v4.IssueUser`
        :param item_count: 满足条件的工作项总数
        :type item_count: int
        :param data: 工作项对应状态的统计计数
        :type data: dict(str, int)
        """
        
        

        self._user = None
        self._item_count = None
        self._data = None
        self.discriminator = None

        if user is not None:
            self.user = user
        if item_count is not None:
            self.item_count = item_count
        if data is not None:
            self.data = data

    @property
    def user(self):
        """Gets the user of this UserStatusStatistic.

        :return: The user of this UserStatusStatistic.
        :rtype: :class:`huaweicloudsdkprojectman.v4.IssueUser`
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this UserStatusStatistic.

        :param user: The user of this UserStatusStatistic.
        :type user: :class:`huaweicloudsdkprojectman.v4.IssueUser`
        """
        self._user = user

    @property
    def item_count(self):
        """Gets the item_count of this UserStatusStatistic.

        满足条件的工作项总数

        :return: The item_count of this UserStatusStatistic.
        :rtype: int
        """
        return self._item_count

    @item_count.setter
    def item_count(self, item_count):
        """Sets the item_count of this UserStatusStatistic.

        满足条件的工作项总数

        :param item_count: The item_count of this UserStatusStatistic.
        :type item_count: int
        """
        self._item_count = item_count

    @property
    def data(self):
        """Gets the data of this UserStatusStatistic.

        工作项对应状态的统计计数

        :return: The data of this UserStatusStatistic.
        :rtype: dict(str, int)
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this UserStatusStatistic.

        工作项对应状态的统计计数

        :param data: The data of this UserStatusStatistic.
        :type data: dict(str, int)
        """
        self._data = data

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
        if not isinstance(other, UserStatusStatistic):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
