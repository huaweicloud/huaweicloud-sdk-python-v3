# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DesktopDimensionAttachInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'desktop_name': 'str',
        'desktop_id': 'str',
        'user_num': 'int',
        'user_name': 'str'
    }

    attribute_map = {
        'desktop_name': 'desktop_name',
        'desktop_id': 'desktop_id',
        'user_num': 'user_num',
        'user_name': 'user_name'
    }

    def __init__(self, desktop_name=None, desktop_id=None, user_num=None, user_name=None):
        r"""DesktopDimensionAttachInfo

        The model defined in huaweicloud sdk

        :param desktop_name: 桌面名称。
        :type desktop_name: str
        :param desktop_id: 桌面id。
        :type desktop_id: str
        :param user_num: 计划分配用户数。
        :type user_num: int
        :param user_name: 计划分配用户名称，如果有多个用逗号隔开。
        :type user_name: str
        """
        
        

        self._desktop_name = None
        self._desktop_id = None
        self._user_num = None
        self._user_name = None
        self.discriminator = None

        if desktop_name is not None:
            self.desktop_name = desktop_name
        if desktop_id is not None:
            self.desktop_id = desktop_id
        if user_num is not None:
            self.user_num = user_num
        if user_name is not None:
            self.user_name = user_name

    @property
    def desktop_name(self):
        r"""Gets the desktop_name of this DesktopDimensionAttachInfo.

        桌面名称。

        :return: The desktop_name of this DesktopDimensionAttachInfo.
        :rtype: str
        """
        return self._desktop_name

    @desktop_name.setter
    def desktop_name(self, desktop_name):
        r"""Sets the desktop_name of this DesktopDimensionAttachInfo.

        桌面名称。

        :param desktop_name: The desktop_name of this DesktopDimensionAttachInfo.
        :type desktop_name: str
        """
        self._desktop_name = desktop_name

    @property
    def desktop_id(self):
        r"""Gets the desktop_id of this DesktopDimensionAttachInfo.

        桌面id。

        :return: The desktop_id of this DesktopDimensionAttachInfo.
        :rtype: str
        """
        return self._desktop_id

    @desktop_id.setter
    def desktop_id(self, desktop_id):
        r"""Sets the desktop_id of this DesktopDimensionAttachInfo.

        桌面id。

        :param desktop_id: The desktop_id of this DesktopDimensionAttachInfo.
        :type desktop_id: str
        """
        self._desktop_id = desktop_id

    @property
    def user_num(self):
        r"""Gets the user_num of this DesktopDimensionAttachInfo.

        计划分配用户数。

        :return: The user_num of this DesktopDimensionAttachInfo.
        :rtype: int
        """
        return self._user_num

    @user_num.setter
    def user_num(self, user_num):
        r"""Sets the user_num of this DesktopDimensionAttachInfo.

        计划分配用户数。

        :param user_num: The user_num of this DesktopDimensionAttachInfo.
        :type user_num: int
        """
        self._user_num = user_num

    @property
    def user_name(self):
        r"""Gets the user_name of this DesktopDimensionAttachInfo.

        计划分配用户名称，如果有多个用逗号隔开。

        :return: The user_name of this DesktopDimensionAttachInfo.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this DesktopDimensionAttachInfo.

        计划分配用户名称，如果有多个用逗号隔开。

        :param user_name: The user_name of this DesktopDimensionAttachInfo.
        :type user_name: str
        """
        self._user_name = user_name

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
        if not isinstance(other, DesktopDimensionAttachInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
