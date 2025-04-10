# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDesktopsConnectStatusRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'user_names': 'list[str]',
        'connect_status': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'user_names': 'user_names',
        'connect_status': 'connect_status',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, user_names=None, connect_status=None, offset=None, limit=None):
        r"""ListDesktopsConnectStatusRequest

        The model defined in huaweicloud sdk

        :param user_names: 桌面所属用户，批量筛选，最多不超过100个用户。
        :type user_names: list[str]
        :param connect_status: 桌面的连接状态。  - UNREGISTER：表示桌面未注册时的状态（桌面启动后，会自动注册）。关机后也会出现未注册的状态。 - REGISTERED：表示桌面注册以后，等待用户连接的状态。 - CONNECTED：表示用户已经成功连接，正在使用桌面。 - DISCONNECTED：表示桌面与客户端断开会话后显示的状态，可能为关闭客户端窗口，或客户端与桌面网络断开引起。
        :type connect_status: str
        :param offset: 从查询结果中的第几条数据开始返回,用于分页查询，取值范围0-2000，默认从0开始。
        :type offset: int
        :param limit: 查询结果中想要返回的信息条目数量,用于分页查询，取值范围0-2000，默认值100。
        :type limit: int
        """
        
        

        self._user_names = None
        self._connect_status = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        if user_names is not None:
            self.user_names = user_names
        if connect_status is not None:
            self.connect_status = connect_status
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def user_names(self):
        r"""Gets the user_names of this ListDesktopsConnectStatusRequest.

        桌面所属用户，批量筛选，最多不超过100个用户。

        :return: The user_names of this ListDesktopsConnectStatusRequest.
        :rtype: list[str]
        """
        return self._user_names

    @user_names.setter
    def user_names(self, user_names):
        r"""Sets the user_names of this ListDesktopsConnectStatusRequest.

        桌面所属用户，批量筛选，最多不超过100个用户。

        :param user_names: The user_names of this ListDesktopsConnectStatusRequest.
        :type user_names: list[str]
        """
        self._user_names = user_names

    @property
    def connect_status(self):
        r"""Gets the connect_status of this ListDesktopsConnectStatusRequest.

        桌面的连接状态。  - UNREGISTER：表示桌面未注册时的状态（桌面启动后，会自动注册）。关机后也会出现未注册的状态。 - REGISTERED：表示桌面注册以后，等待用户连接的状态。 - CONNECTED：表示用户已经成功连接，正在使用桌面。 - DISCONNECTED：表示桌面与客户端断开会话后显示的状态，可能为关闭客户端窗口，或客户端与桌面网络断开引起。

        :return: The connect_status of this ListDesktopsConnectStatusRequest.
        :rtype: str
        """
        return self._connect_status

    @connect_status.setter
    def connect_status(self, connect_status):
        r"""Sets the connect_status of this ListDesktopsConnectStatusRequest.

        桌面的连接状态。  - UNREGISTER：表示桌面未注册时的状态（桌面启动后，会自动注册）。关机后也会出现未注册的状态。 - REGISTERED：表示桌面注册以后，等待用户连接的状态。 - CONNECTED：表示用户已经成功连接，正在使用桌面。 - DISCONNECTED：表示桌面与客户端断开会话后显示的状态，可能为关闭客户端窗口，或客户端与桌面网络断开引起。

        :param connect_status: The connect_status of this ListDesktopsConnectStatusRequest.
        :type connect_status: str
        """
        self._connect_status = connect_status

    @property
    def offset(self):
        r"""Gets the offset of this ListDesktopsConnectStatusRequest.

        从查询结果中的第几条数据开始返回,用于分页查询，取值范围0-2000，默认从0开始。

        :return: The offset of this ListDesktopsConnectStatusRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListDesktopsConnectStatusRequest.

        从查询结果中的第几条数据开始返回,用于分页查询，取值范围0-2000，默认从0开始。

        :param offset: The offset of this ListDesktopsConnectStatusRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListDesktopsConnectStatusRequest.

        查询结果中想要返回的信息条目数量,用于分页查询，取值范围0-2000，默认值100。

        :return: The limit of this ListDesktopsConnectStatusRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListDesktopsConnectStatusRequest.

        查询结果中想要返回的信息条目数量,用于分页查询，取值范围0-2000，默认值100。

        :param limit: The limit of this ListDesktopsConnectStatusRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ListDesktopsConnectStatusRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
