# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UserStatisticInfoResponseInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'user_name': 'str',
        'num': 'int'
    }

    attribute_map = {
        'user_name': 'user_name',
        'num': 'num'
    }

    def __init__(self, user_name=None, num=None):
        """UserStatisticInfoResponseInfo

        The model defined in huaweicloud sdk

        :param user_name: 账号名称
        :type user_name: str
        :param num: 账号数量
        :type num: int
        """
        
        

        self._user_name = None
        self._num = None
        self.discriminator = None

        if user_name is not None:
            self.user_name = user_name
        if num is not None:
            self.num = num

    @property
    def user_name(self):
        """Gets the user_name of this UserStatisticInfoResponseInfo.

        账号名称

        :return: The user_name of this UserStatisticInfoResponseInfo.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this UserStatisticInfoResponseInfo.

        账号名称

        :param user_name: The user_name of this UserStatisticInfoResponseInfo.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def num(self):
        """Gets the num of this UserStatisticInfoResponseInfo.

        账号数量

        :return: The num of this UserStatisticInfoResponseInfo.
        :rtype: int
        """
        return self._num

    @num.setter
    def num(self, num):
        """Sets the num of this UserStatisticInfoResponseInfo.

        账号数量

        :param num: The num of this UserStatisticInfoResponseInfo.
        :type num: int
        """
        self._num = num

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
        if not isinstance(other, UserStatisticInfoResponseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
