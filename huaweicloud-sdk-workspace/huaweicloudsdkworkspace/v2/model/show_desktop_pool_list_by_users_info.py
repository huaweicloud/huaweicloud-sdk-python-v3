# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDesktopPoolListByUsersInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'user_id': 'str',
        'desktop_pool_count': 'int',
        'desktop_pools': 'list[AttachDesktopPoolsInfo]'
    }

    attribute_map = {
        'user_id': 'user_id',
        'desktop_pool_count': 'desktop_pool_count',
        'desktop_pools': 'desktop_pools'
    }

    def __init__(self, user_id=None, desktop_pool_count=None, desktop_pools=None):
        r"""ShowDesktopPoolListByUsersInfo

        The model defined in huaweicloud sdk

        :param user_id: 用户id
        :type user_id: str
        :param desktop_pool_count: 桌面池数
        :type desktop_pool_count: int
        :param desktop_pools: 运行状态统计
        :type desktop_pools: list[:class:`huaweicloudsdkworkspace.v2.AttachDesktopPoolsInfo`]
        """
        
        

        self._user_id = None
        self._desktop_pool_count = None
        self._desktop_pools = None
        self.discriminator = None

        if user_id is not None:
            self.user_id = user_id
        if desktop_pool_count is not None:
            self.desktop_pool_count = desktop_pool_count
        if desktop_pools is not None:
            self.desktop_pools = desktop_pools

    @property
    def user_id(self):
        r"""Gets the user_id of this ShowDesktopPoolListByUsersInfo.

        用户id

        :return: The user_id of this ShowDesktopPoolListByUsersInfo.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        r"""Sets the user_id of this ShowDesktopPoolListByUsersInfo.

        用户id

        :param user_id: The user_id of this ShowDesktopPoolListByUsersInfo.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def desktop_pool_count(self):
        r"""Gets the desktop_pool_count of this ShowDesktopPoolListByUsersInfo.

        桌面池数

        :return: The desktop_pool_count of this ShowDesktopPoolListByUsersInfo.
        :rtype: int
        """
        return self._desktop_pool_count

    @desktop_pool_count.setter
    def desktop_pool_count(self, desktop_pool_count):
        r"""Sets the desktop_pool_count of this ShowDesktopPoolListByUsersInfo.

        桌面池数

        :param desktop_pool_count: The desktop_pool_count of this ShowDesktopPoolListByUsersInfo.
        :type desktop_pool_count: int
        """
        self._desktop_pool_count = desktop_pool_count

    @property
    def desktop_pools(self):
        r"""Gets the desktop_pools of this ShowDesktopPoolListByUsersInfo.

        运行状态统计

        :return: The desktop_pools of this ShowDesktopPoolListByUsersInfo.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.AttachDesktopPoolsInfo`]
        """
        return self._desktop_pools

    @desktop_pools.setter
    def desktop_pools(self, desktop_pools):
        r"""Sets the desktop_pools of this ShowDesktopPoolListByUsersInfo.

        运行状态统计

        :param desktop_pools: The desktop_pools of this ShowDesktopPoolListByUsersInfo.
        :type desktop_pools: list[:class:`huaweicloudsdkworkspace.v2.AttachDesktopPoolsInfo`]
        """
        self._desktop_pools = desktop_pools

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ShowDesktopPoolListByUsersInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
