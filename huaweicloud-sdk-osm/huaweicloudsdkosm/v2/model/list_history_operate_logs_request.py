# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListHistoryOperateLogsRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'authorization_id': 'int',
        'authorization_detail_id': 'int',
        'group_id': 'str',
        'session_id': 'int',
        'sort': 'int',
        'offset': 'int',
        'limit': 'int',
        'x_site': 'int',
        'x_language': 'str',
        'x_time_zone': 'str'
    }

    attribute_map = {
        'authorization_id': 'authorization_id',
        'authorization_detail_id': 'authorization_detail_id',
        'group_id': 'group_id',
        'session_id': 'session_id',
        'sort': 'sort',
        'offset': 'offset',
        'limit': 'limit',
        'x_site': 'X-Site',
        'x_language': 'X-Language',
        'x_time_zone': 'X-Time-Zone'
    }

    def __init__(self, authorization_id=None, authorization_detail_id=None, group_id=None, session_id=None, sort=None, offset=None, limit=None, x_site=None, x_language=None, x_time_zone=None):
        """ListHistoryOperateLogsRequest - a model defined in huaweicloud sdk"""
        
        

        self._authorization_id = None
        self._authorization_detail_id = None
        self._group_id = None
        self._session_id = None
        self._sort = None
        self._offset = None
        self._limit = None
        self._x_site = None
        self._x_language = None
        self._x_time_zone = None
        self.discriminator = None

        self.authorization_id = authorization_id
        self.authorization_detail_id = authorization_detail_id
        if group_id is not None:
            self.group_id = group_id
        self.session_id = session_id
        if sort is not None:
            self.sort = sort
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if x_site is not None:
            self.x_site = x_site
        if x_language is not None:
            self.x_language = x_language
        if x_time_zone is not None:
            self.x_time_zone = x_time_zone

    @property
    def authorization_id(self):
        """Gets the authorization_id of this ListHistoryOperateLogsRequest.

        授权id

        :return: The authorization_id of this ListHistoryOperateLogsRequest.
        :rtype: int
        """
        return self._authorization_id

    @authorization_id.setter
    def authorization_id(self, authorization_id):
        """Sets the authorization_id of this ListHistoryOperateLogsRequest.

        授权id

        :param authorization_id: The authorization_id of this ListHistoryOperateLogsRequest.
        :type: int
        """
        self._authorization_id = authorization_id

    @property
    def authorization_detail_id(self):
        """Gets the authorization_detail_id of this ListHistoryOperateLogsRequest.

        授权详情id

        :return: The authorization_detail_id of this ListHistoryOperateLogsRequest.
        :rtype: int
        """
        return self._authorization_detail_id

    @authorization_detail_id.setter
    def authorization_detail_id(self, authorization_detail_id):
        """Sets the authorization_detail_id of this ListHistoryOperateLogsRequest.

        授权详情id

        :param authorization_detail_id: The authorization_detail_id of this ListHistoryOperateLogsRequest.
        :type: int
        """
        self._authorization_detail_id = authorization_detail_id

    @property
    def group_id(self):
        """Gets the group_id of this ListHistoryOperateLogsRequest.

        IAM组id

        :return: The group_id of this ListHistoryOperateLogsRequest.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this ListHistoryOperateLogsRequest.

        IAM组id

        :param group_id: The group_id of this ListHistoryOperateLogsRequest.
        :type: str
        """
        self._group_id = group_id

    @property
    def session_id(self):
        """Gets the session_id of this ListHistoryOperateLogsRequest.

        会话id

        :return: The session_id of this ListHistoryOperateLogsRequest.
        :rtype: int
        """
        return self._session_id

    @session_id.setter
    def session_id(self, session_id):
        """Sets the session_id of this ListHistoryOperateLogsRequest.

        会话id

        :param session_id: The session_id of this ListHistoryOperateLogsRequest.
        :type: int
        """
        self._session_id = session_id

    @property
    def sort(self):
        """Gets the sort of this ListHistoryOperateLogsRequest.

        1：按操作时间升序； 0：按操作时间降序；默认0

        :return: The sort of this ListHistoryOperateLogsRequest.
        :rtype: int
        """
        return self._sort

    @sort.setter
    def sort(self, sort):
        """Sets the sort of this ListHistoryOperateLogsRequest.

        1：按操作时间升序； 0：按操作时间降序；默认0

        :param sort: The sort of this ListHistoryOperateLogsRequest.
        :type: int
        """
        self._sort = sort

    @property
    def offset(self):
        """Gets the offset of this ListHistoryOperateLogsRequest.

        查询偏移量

        :return: The offset of this ListHistoryOperateLogsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListHistoryOperateLogsRequest.

        查询偏移量

        :param offset: The offset of this ListHistoryOperateLogsRequest.
        :type: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListHistoryOperateLogsRequest.

        查询限制条数

        :return: The limit of this ListHistoryOperateLogsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListHistoryOperateLogsRequest.

        查询限制条数

        :param limit: The limit of this ListHistoryOperateLogsRequest.
        :type: int
        """
        self._limit = limit

    @property
    def x_site(self):
        """Gets the x_site of this ListHistoryOperateLogsRequest.

        对接站点信息。  0（中国站） 1（国际站），不填的话默认为0。

        :return: The x_site of this ListHistoryOperateLogsRequest.
        :rtype: int
        """
        return self._x_site

    @x_site.setter
    def x_site(self, x_site):
        """Sets the x_site of this ListHistoryOperateLogsRequest.

        对接站点信息。  0（中国站） 1（国际站），不填的话默认为0。

        :param x_site: The x_site of this ListHistoryOperateLogsRequest.
        :type: int
        """
        self._x_site = x_site

    @property
    def x_language(self):
        """Gets the x_language of this ListHistoryOperateLogsRequest.

        语言环境，值为通用的语言描述字符串，比如zh-cn等，默认为zh-cn。  会根据语言环境对应展示一些国际化的信息，比如工单类型名称等。

        :return: The x_language of this ListHistoryOperateLogsRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        """Sets the x_language of this ListHistoryOperateLogsRequest.

        语言环境，值为通用的语言描述字符串，比如zh-cn等，默认为zh-cn。  会根据语言环境对应展示一些国际化的信息，比如工单类型名称等。

        :param x_language: The x_language of this ListHistoryOperateLogsRequest.
        :type: str
        """
        self._x_language = x_language

    @property
    def x_time_zone(self):
        """Gets the x_time_zone of this ListHistoryOperateLogsRequest.

        环境时区，值为通用的时区描述字符串，比如GMT+8等，默认为GMT+8。  涉及时间的数据会根据环境时区处理。

        :return: The x_time_zone of this ListHistoryOperateLogsRequest.
        :rtype: str
        """
        return self._x_time_zone

    @x_time_zone.setter
    def x_time_zone(self, x_time_zone):
        """Sets the x_time_zone of this ListHistoryOperateLogsRequest.

        环境时区，值为通用的时区描述字符串，比如GMT+8等，默认为GMT+8。  涉及时间的数据会根据环境时区处理。

        :param x_time_zone: The x_time_zone of this ListHistoryOperateLogsRequest.
        :type: str
        """
        self._x_time_zone = x_time_zone

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
        import simplejson as json
        return json.dumps(sanitize_for_serialization(self))

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListHistoryOperateLogsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
