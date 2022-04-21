# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListWhitelistsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'limit': 'int',
        'marker': 'str',
        'page_reverse': 'bool',
        'id': 'str',
        'enable_whitelist': 'bool',
        'listener_id': 'str',
        'whitelist': 'str'
    }

    attribute_map = {
        'limit': 'limit',
        'marker': 'marker',
        'page_reverse': 'page_reverse',
        'id': 'id',
        'enable_whitelist': 'enable_whitelist',
        'listener_id': 'listener_id',
        'whitelist': 'whitelist'
    }

    def __init__(self, limit=None, marker=None, page_reverse=None, id=None, enable_whitelist=None, listener_id=None, whitelist=None):
        """ListWhitelistsRequest

        The model defined in huaweicloud sdk

        :param limit: 分页查询中每页的白名单个数
        :type limit: int
        :param marker: 分页查询的起始的资源id，表示上一页最后一条查询记录的白名单的id。不指定时表示查询第一页。
        :type marker: str
        :param page_reverse: 分页的顺序，true表示从后往前分页，false表示从前往后分页，默认为false。
        :type page_reverse: bool
        :param id: 白名单ID。
        :type id: str
        :param enable_whitelist: 是否开启访问控制开关。true：打开false：关闭
        :type enable_whitelist: bool
        :param listener_id: 白名单关联的监听器ID。
        :type listener_id: str
        :param whitelist: 白名单IP的字符串。
        :type whitelist: str
        """
        
        

        self._limit = None
        self._marker = None
        self._page_reverse = None
        self._id = None
        self._enable_whitelist = None
        self._listener_id = None
        self._whitelist = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if page_reverse is not None:
            self.page_reverse = page_reverse
        if id is not None:
            self.id = id
        if enable_whitelist is not None:
            self.enable_whitelist = enable_whitelist
        if listener_id is not None:
            self.listener_id = listener_id
        if whitelist is not None:
            self.whitelist = whitelist

    @property
    def limit(self):
        """Gets the limit of this ListWhitelistsRequest.

        分页查询中每页的白名单个数

        :return: The limit of this ListWhitelistsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListWhitelistsRequest.

        分页查询中每页的白名单个数

        :param limit: The limit of this ListWhitelistsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        """Gets the marker of this ListWhitelistsRequest.

        分页查询的起始的资源id，表示上一页最后一条查询记录的白名单的id。不指定时表示查询第一页。

        :return: The marker of this ListWhitelistsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListWhitelistsRequest.

        分页查询的起始的资源id，表示上一页最后一条查询记录的白名单的id。不指定时表示查询第一页。

        :param marker: The marker of this ListWhitelistsRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def page_reverse(self):
        """Gets the page_reverse of this ListWhitelistsRequest.

        分页的顺序，true表示从后往前分页，false表示从前往后分页，默认为false。

        :return: The page_reverse of this ListWhitelistsRequest.
        :rtype: bool
        """
        return self._page_reverse

    @page_reverse.setter
    def page_reverse(self, page_reverse):
        """Sets the page_reverse of this ListWhitelistsRequest.

        分页的顺序，true表示从后往前分页，false表示从前往后分页，默认为false。

        :param page_reverse: The page_reverse of this ListWhitelistsRequest.
        :type page_reverse: bool
        """
        self._page_reverse = page_reverse

    @property
    def id(self):
        """Gets the id of this ListWhitelistsRequest.

        白名单ID。

        :return: The id of this ListWhitelistsRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListWhitelistsRequest.

        白名单ID。

        :param id: The id of this ListWhitelistsRequest.
        :type id: str
        """
        self._id = id

    @property
    def enable_whitelist(self):
        """Gets the enable_whitelist of this ListWhitelistsRequest.

        是否开启访问控制开关。true：打开false：关闭

        :return: The enable_whitelist of this ListWhitelistsRequest.
        :rtype: bool
        """
        return self._enable_whitelist

    @enable_whitelist.setter
    def enable_whitelist(self, enable_whitelist):
        """Sets the enable_whitelist of this ListWhitelistsRequest.

        是否开启访问控制开关。true：打开false：关闭

        :param enable_whitelist: The enable_whitelist of this ListWhitelistsRequest.
        :type enable_whitelist: bool
        """
        self._enable_whitelist = enable_whitelist

    @property
    def listener_id(self):
        """Gets the listener_id of this ListWhitelistsRequest.

        白名单关联的监听器ID。

        :return: The listener_id of this ListWhitelistsRequest.
        :rtype: str
        """
        return self._listener_id

    @listener_id.setter
    def listener_id(self, listener_id):
        """Sets the listener_id of this ListWhitelistsRequest.

        白名单关联的监听器ID。

        :param listener_id: The listener_id of this ListWhitelistsRequest.
        :type listener_id: str
        """
        self._listener_id = listener_id

    @property
    def whitelist(self):
        """Gets the whitelist of this ListWhitelistsRequest.

        白名单IP的字符串。

        :return: The whitelist of this ListWhitelistsRequest.
        :rtype: str
        """
        return self._whitelist

    @whitelist.setter
    def whitelist(self, whitelist):
        """Sets the whitelist of this ListWhitelistsRequest.

        白名单IP的字符串。

        :param whitelist: The whitelist of this ListWhitelistsRequest.
        :type whitelist: str
        """
        self._whitelist = whitelist

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
        if not isinstance(other, ListWhitelistsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
