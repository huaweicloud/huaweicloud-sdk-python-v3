# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UserDimensionAttachInfo:

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
        'user_id': 'str',
        'desktop_num': 'int',
        'desktop_name': 'str'
    }

    attribute_map = {
        'user_name': 'user_name',
        'user_id': 'user_id',
        'desktop_num': 'desktop_num',
        'desktop_name': 'desktop_name'
    }

    def __init__(self, user_name=None, user_id=None, desktop_num=None, desktop_name=None):
        r"""UserDimensionAttachInfo

        The model defined in huaweicloud sdk

        :param user_name: 用户名称。
        :type user_name: str
        :param user_id: 桌面id。
        :type user_id: str
        :param desktop_num: 计划分配桌面数。
        :type desktop_num: int
        :param desktop_name: 计划分配桌面名称，如果有多个用逗号隔开。
        :type desktop_name: str
        """
        
        

        self._user_name = None
        self._user_id = None
        self._desktop_num = None
        self._desktop_name = None
        self.discriminator = None

        if user_name is not None:
            self.user_name = user_name
        if user_id is not None:
            self.user_id = user_id
        if desktop_num is not None:
            self.desktop_num = desktop_num
        if desktop_name is not None:
            self.desktop_name = desktop_name

    @property
    def user_name(self):
        r"""Gets the user_name of this UserDimensionAttachInfo.

        用户名称。

        :return: The user_name of this UserDimensionAttachInfo.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this UserDimensionAttachInfo.

        用户名称。

        :param user_name: The user_name of this UserDimensionAttachInfo.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def user_id(self):
        r"""Gets the user_id of this UserDimensionAttachInfo.

        桌面id。

        :return: The user_id of this UserDimensionAttachInfo.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        r"""Sets the user_id of this UserDimensionAttachInfo.

        桌面id。

        :param user_id: The user_id of this UserDimensionAttachInfo.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def desktop_num(self):
        r"""Gets the desktop_num of this UserDimensionAttachInfo.

        计划分配桌面数。

        :return: The desktop_num of this UserDimensionAttachInfo.
        :rtype: int
        """
        return self._desktop_num

    @desktop_num.setter
    def desktop_num(self, desktop_num):
        r"""Sets the desktop_num of this UserDimensionAttachInfo.

        计划分配桌面数。

        :param desktop_num: The desktop_num of this UserDimensionAttachInfo.
        :type desktop_num: int
        """
        self._desktop_num = desktop_num

    @property
    def desktop_name(self):
        r"""Gets the desktop_name of this UserDimensionAttachInfo.

        计划分配桌面名称，如果有多个用逗号隔开。

        :return: The desktop_name of this UserDimensionAttachInfo.
        :rtype: str
        """
        return self._desktop_name

    @desktop_name.setter
    def desktop_name(self, desktop_name):
        r"""Sets the desktop_name of this UserDimensionAttachInfo.

        计划分配桌面名称，如果有多个用逗号隔开。

        :param desktop_name: The desktop_name of this UserDimensionAttachInfo.
        :type desktop_name: str
        """
        self._desktop_name = desktop_name

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
        if not isinstance(other, UserDimensionAttachInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
