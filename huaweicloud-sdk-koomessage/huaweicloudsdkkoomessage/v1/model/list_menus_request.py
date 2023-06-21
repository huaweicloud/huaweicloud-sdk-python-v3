# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListMenusRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'menu_id': 'str',
        'pub_id': 'str',
        'pub_name': 'str',
        'online_begin_time': 'str',
        'online_end_time': 'str',
        'state': 'int',
        'menu_name': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'menu_id': 'menu_id',
        'pub_id': 'pub_id',
        'pub_name': 'pub_name',
        'online_begin_time': 'online_begin_time',
        'online_end_time': 'online_end_time',
        'state': 'state',
        'menu_name': 'menu_name',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, menu_id=None, pub_id=None, pub_name=None, online_begin_time=None, online_end_time=None, state=None, menu_name=None, offset=None, limit=None):
        """ListMenusRequest

        The model defined in huaweicloud sdk

        :param menu_id: 菜单ID。
        :type menu_id: str
        :param pub_id: 服务号ID。
        :type pub_id: str
        :param pub_name: 服务号名称。
        :type pub_name: str
        :param online_begin_time: 上线开始时间。格式为：yyyy-MM-ddTHH:mm:ssZ。
        :type online_begin_time: str
        :param online_end_time: 上线结束时间。格式为：yyyy-MM-ddTHH:mm:ssZ。
        :type online_end_time: str
        :param state: 菜单状态。  - 1：未生效  - 2：已生效  - 3：已失效  - 4：服务号已冻结 
        :type state: int
        :param menu_name: 一级菜单名称。
        :type menu_name: str
        :param offset: 偏移量，表示从此偏移量开始查询，offset大于等于0。
        :type offset: int
        :param limit: 每页显示的条目数量。
        :type limit: int
        """
        
        

        self._menu_id = None
        self._pub_id = None
        self._pub_name = None
        self._online_begin_time = None
        self._online_end_time = None
        self._state = None
        self._menu_name = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        if menu_id is not None:
            self.menu_id = menu_id
        if pub_id is not None:
            self.pub_id = pub_id
        if pub_name is not None:
            self.pub_name = pub_name
        if online_begin_time is not None:
            self.online_begin_time = online_begin_time
        if online_end_time is not None:
            self.online_end_time = online_end_time
        if state is not None:
            self.state = state
        if menu_name is not None:
            self.menu_name = menu_name
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def menu_id(self):
        """Gets the menu_id of this ListMenusRequest.

        菜单ID。

        :return: The menu_id of this ListMenusRequest.
        :rtype: str
        """
        return self._menu_id

    @menu_id.setter
    def menu_id(self, menu_id):
        """Sets the menu_id of this ListMenusRequest.

        菜单ID。

        :param menu_id: The menu_id of this ListMenusRequest.
        :type menu_id: str
        """
        self._menu_id = menu_id

    @property
    def pub_id(self):
        """Gets the pub_id of this ListMenusRequest.

        服务号ID。

        :return: The pub_id of this ListMenusRequest.
        :rtype: str
        """
        return self._pub_id

    @pub_id.setter
    def pub_id(self, pub_id):
        """Sets the pub_id of this ListMenusRequest.

        服务号ID。

        :param pub_id: The pub_id of this ListMenusRequest.
        :type pub_id: str
        """
        self._pub_id = pub_id

    @property
    def pub_name(self):
        """Gets the pub_name of this ListMenusRequest.

        服务号名称。

        :return: The pub_name of this ListMenusRequest.
        :rtype: str
        """
        return self._pub_name

    @pub_name.setter
    def pub_name(self, pub_name):
        """Sets the pub_name of this ListMenusRequest.

        服务号名称。

        :param pub_name: The pub_name of this ListMenusRequest.
        :type pub_name: str
        """
        self._pub_name = pub_name

    @property
    def online_begin_time(self):
        """Gets the online_begin_time of this ListMenusRequest.

        上线开始时间。格式为：yyyy-MM-ddTHH:mm:ssZ。

        :return: The online_begin_time of this ListMenusRequest.
        :rtype: str
        """
        return self._online_begin_time

    @online_begin_time.setter
    def online_begin_time(self, online_begin_time):
        """Sets the online_begin_time of this ListMenusRequest.

        上线开始时间。格式为：yyyy-MM-ddTHH:mm:ssZ。

        :param online_begin_time: The online_begin_time of this ListMenusRequest.
        :type online_begin_time: str
        """
        self._online_begin_time = online_begin_time

    @property
    def online_end_time(self):
        """Gets the online_end_time of this ListMenusRequest.

        上线结束时间。格式为：yyyy-MM-ddTHH:mm:ssZ。

        :return: The online_end_time of this ListMenusRequest.
        :rtype: str
        """
        return self._online_end_time

    @online_end_time.setter
    def online_end_time(self, online_end_time):
        """Sets the online_end_time of this ListMenusRequest.

        上线结束时间。格式为：yyyy-MM-ddTHH:mm:ssZ。

        :param online_end_time: The online_end_time of this ListMenusRequest.
        :type online_end_time: str
        """
        self._online_end_time = online_end_time

    @property
    def state(self):
        """Gets the state of this ListMenusRequest.

        菜单状态。  - 1：未生效  - 2：已生效  - 3：已失效  - 4：服务号已冻结 

        :return: The state of this ListMenusRequest.
        :rtype: int
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this ListMenusRequest.

        菜单状态。  - 1：未生效  - 2：已生效  - 3：已失效  - 4：服务号已冻结 

        :param state: The state of this ListMenusRequest.
        :type state: int
        """
        self._state = state

    @property
    def menu_name(self):
        """Gets the menu_name of this ListMenusRequest.

        一级菜单名称。

        :return: The menu_name of this ListMenusRequest.
        :rtype: str
        """
        return self._menu_name

    @menu_name.setter
    def menu_name(self, menu_name):
        """Sets the menu_name of this ListMenusRequest.

        一级菜单名称。

        :param menu_name: The menu_name of this ListMenusRequest.
        :type menu_name: str
        """
        self._menu_name = menu_name

    @property
    def offset(self):
        """Gets the offset of this ListMenusRequest.

        偏移量，表示从此偏移量开始查询，offset大于等于0。

        :return: The offset of this ListMenusRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListMenusRequest.

        偏移量，表示从此偏移量开始查询，offset大于等于0。

        :param offset: The offset of this ListMenusRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListMenusRequest.

        每页显示的条目数量。

        :return: The limit of this ListMenusRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListMenusRequest.

        每页显示的条目数量。

        :param limit: The limit of this ListMenusRequest.
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
        if not isinstance(other, ListMenusRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
