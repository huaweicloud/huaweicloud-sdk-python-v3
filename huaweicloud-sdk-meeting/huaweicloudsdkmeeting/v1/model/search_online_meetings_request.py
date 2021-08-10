# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SearchOnlineMeetingsRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'user_uuid': 'str',
        'offset': 'int',
        'limit': 'int',
        'query_all': 'bool',
        'search_key': 'str',
        'x_authorization_type': 'str',
        'x_site_id': 'str'
    }

    attribute_map = {
        'user_uuid': 'userUUID',
        'offset': 'offset',
        'limit': 'limit',
        'query_all': 'queryAll',
        'search_key': 'searchKey',
        'x_authorization_type': 'X-Authorization-Type',
        'x_site_id': 'X-Site-Id'
    }

    def __init__(self, user_uuid=None, offset=None, limit=None, query_all=None, search_key=None, x_authorization_type=None, x_site_id=None):
        """SearchOnlineMeetingsRequest - a model defined in huaweicloud sdk"""
        
        

        self._user_uuid = None
        self._offset = None
        self._limit = None
        self._query_all = None
        self._search_key = None
        self._x_authorization_type = None
        self._x_site_id = None
        self.discriminator = None

        if user_uuid is not None:
            self.user_uuid = user_uuid
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if query_all is not None:
            self.query_all = query_all
        if search_key is not None:
            self.search_key = search_key
        if x_authorization_type is not None:
            self.x_authorization_type = x_authorization_type
        if x_site_id is not None:
            self.x_site_id = x_site_id

    @property
    def user_uuid(self):
        """Gets the user_uuid of this SearchOnlineMeetingsRequest.

        用户UUID。 仅管理员有权限查询权限范围内的所有帐号，普通帐号仅能查询自己的。

        :return: The user_uuid of this SearchOnlineMeetingsRequest.
        :rtype: str
        """
        return self._user_uuid

    @user_uuid.setter
    def user_uuid(self, user_uuid):
        """Sets the user_uuid of this SearchOnlineMeetingsRequest.

        用户UUID。 仅管理员有权限查询权限范围内的所有帐号，普通帐号仅能查询自己的。

        :param user_uuid: The user_uuid of this SearchOnlineMeetingsRequest.
        :type: str
        """
        self._user_uuid = user_uuid

    @property
    def offset(self):
        """Gets the offset of this SearchOnlineMeetingsRequest.

        指定返回的记录索引。该值必须大于等于0； 默认为0。

        :return: The offset of this SearchOnlineMeetingsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this SearchOnlineMeetingsRequest.

        指定返回的记录索引。该值必须大于等于0； 默认为0。

        :param offset: The offset of this SearchOnlineMeetingsRequest.
        :type: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this SearchOnlineMeetingsRequest.

        指定返回的记录数。默认是20，最大值为500。

        :return: The limit of this SearchOnlineMeetingsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this SearchOnlineMeetingsRequest.

        指定返回的记录数。默认是20，最大值为500。

        :param limit: The limit of this SearchOnlineMeetingsRequest.
        :type: int
        """
        self._limit = limit

    @property
    def query_all(self):
        """Gets the query_all of this SearchOnlineMeetingsRequest.

        指定是否查询企业下所有用户的会议记录。 如果登录帐号不是企业管理员，则该字段无效。 如果该字段为true，则userUUID字段无效。 default : false

        :return: The query_all of this SearchOnlineMeetingsRequest.
        :rtype: bool
        """
        return self._query_all

    @query_all.setter
    def query_all(self, query_all):
        """Sets the query_all of this SearchOnlineMeetingsRequest.

        指定是否查询企业下所有用户的会议记录。 如果登录帐号不是企业管理员，则该字段无效。 如果该字段为true，则userUUID字段无效。 default : false

        :param query_all: The query_all of this SearchOnlineMeetingsRequest.
        :type: bool
        """
        self._query_all = query_all

    @property
    def search_key(self):
        """Gets the search_key of this SearchOnlineMeetingsRequest.

        查询用来当作关键词的字符串。会议主题、会议预约人和会议ID等可作为搜索内容。

        :return: The search_key of this SearchOnlineMeetingsRequest.
        :rtype: str
        """
        return self._search_key

    @search_key.setter
    def search_key(self, search_key):
        """Sets the search_key of this SearchOnlineMeetingsRequest.

        查询用来当作关键词的字符串。会议主题、会议预约人和会议ID等可作为搜索内容。

        :param search_key: The search_key of this SearchOnlineMeetingsRequest.
        :type: str
        """
        self._search_key = search_key

    @property
    def x_authorization_type(self):
        """Gets the x_authorization_type of this SearchOnlineMeetingsRequest.

        标识是否为第三方portal过来的请求。

        :return: The x_authorization_type of this SearchOnlineMeetingsRequest.
        :rtype: str
        """
        return self._x_authorization_type

    @x_authorization_type.setter
    def x_authorization_type(self, x_authorization_type):
        """Sets the x_authorization_type of this SearchOnlineMeetingsRequest.

        标识是否为第三方portal过来的请求。

        :param x_authorization_type: The x_authorization_type of this SearchOnlineMeetingsRequest.
        :type: str
        """
        self._x_authorization_type = x_authorization_type

    @property
    def x_site_id(self):
        """Gets the x_site_id of this SearchOnlineMeetingsRequest.

        用于区分到哪个HCSO站点鉴权。

        :return: The x_site_id of this SearchOnlineMeetingsRequest.
        :rtype: str
        """
        return self._x_site_id

    @x_site_id.setter
    def x_site_id(self, x_site_id):
        """Sets the x_site_id of this SearchOnlineMeetingsRequest.

        用于区分到哪个HCSO站点鉴权。

        :param x_site_id: The x_site_id of this SearchOnlineMeetingsRequest.
        :type: str
        """
        self._x_site_id = x_site_id

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
        if not isinstance(other, SearchOnlineMeetingsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
