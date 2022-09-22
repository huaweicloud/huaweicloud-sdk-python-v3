# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SearchMeetingsRequest:

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
        'query_conf_mode': 'str',
        'sort_type': 'str',
        'x_authorization_type': 'str',
        'x_site_id': 'str'
    }

    attribute_map = {
        'user_uuid': 'userUUID',
        'offset': 'offset',
        'limit': 'limit',
        'query_all': 'queryAll',
        'search_key': 'searchKey',
        'query_conf_mode': 'queryConfMode',
        'sort_type': 'sortType',
        'x_authorization_type': 'X-Authorization-Type',
        'x_site_id': 'X-Site-Id'
    }

    def __init__(self, user_uuid=None, offset=None, limit=None, query_all=None, search_key=None, query_conf_mode=None, sort_type=None, x_authorization_type=None, x_site_id=None):
        """SearchMeetingsRequest

        The model defined in huaweicloud sdk

        :param user_uuid: 用户的UUID。 &gt; 仅管理员有权限查询本企业其他用户的会议列表；普通帐号该字段无效，只能查询自己的。 
        :type user_uuid: str
        :param offset: 查询偏移量。默认为0。
        :type offset: int
        :param limit: 查询数量。默认是20，最大500条。
        :type limit: int
        :param query_all: 是否查询企业下所有用户的会议记录。默认值为false。 * true：查询所有用户的会议 * false：仅查询管理员自己创建的会议 &gt; 仅对企业管理员生效。
        :type query_all: bool
        :param search_key: 查询条件。会议主题、会议预约人和会议ID等可作为搜索内容。长度限制为1-128个字符。
        :type search_key: str
        :param query_conf_mode: 查询时间范围。 - ADAY:  一天 - AWEEK:  一周 - AMONTH:  一个月 - ALL:  查询所有
        :type query_conf_mode: str
        :param sort_type: 查询结果排序。 - ASC_StartTIME:  按会议开始时间升序排序 - DSC_StartTIME:  按会议开始时间降序排序
        :type sort_type: str
        :param x_authorization_type: 标识是否为第三方portal过来的请求。 &gt; 该参数将废弃，请勿使用。 
        :type x_authorization_type: str
        :param x_site_id: 用于区分到哪个HCSO站点鉴权。 &gt; 该参数将废弃，请勿使用。 
        :type x_site_id: str
        """
        
        

        self._user_uuid = None
        self._offset = None
        self._limit = None
        self._query_all = None
        self._search_key = None
        self._query_conf_mode = None
        self._sort_type = None
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
        if query_conf_mode is not None:
            self.query_conf_mode = query_conf_mode
        if sort_type is not None:
            self.sort_type = sort_type
        if x_authorization_type is not None:
            self.x_authorization_type = x_authorization_type
        if x_site_id is not None:
            self.x_site_id = x_site_id

    @property
    def user_uuid(self):
        """Gets the user_uuid of this SearchMeetingsRequest.

        用户的UUID。 > 仅管理员有权限查询本企业其他用户的会议列表；普通帐号该字段无效，只能查询自己的。 

        :return: The user_uuid of this SearchMeetingsRequest.
        :rtype: str
        """
        return self._user_uuid

    @user_uuid.setter
    def user_uuid(self, user_uuid):
        """Sets the user_uuid of this SearchMeetingsRequest.

        用户的UUID。 > 仅管理员有权限查询本企业其他用户的会议列表；普通帐号该字段无效，只能查询自己的。 

        :param user_uuid: The user_uuid of this SearchMeetingsRequest.
        :type user_uuid: str
        """
        self._user_uuid = user_uuid

    @property
    def offset(self):
        """Gets the offset of this SearchMeetingsRequest.

        查询偏移量。默认为0。

        :return: The offset of this SearchMeetingsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this SearchMeetingsRequest.

        查询偏移量。默认为0。

        :param offset: The offset of this SearchMeetingsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this SearchMeetingsRequest.

        查询数量。默认是20，最大500条。

        :return: The limit of this SearchMeetingsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this SearchMeetingsRequest.

        查询数量。默认是20，最大500条。

        :param limit: The limit of this SearchMeetingsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def query_all(self):
        """Gets the query_all of this SearchMeetingsRequest.

        是否查询企业下所有用户的会议记录。默认值为false。 * true：查询所有用户的会议 * false：仅查询管理员自己创建的会议 > 仅对企业管理员生效。

        :return: The query_all of this SearchMeetingsRequest.
        :rtype: bool
        """
        return self._query_all

    @query_all.setter
    def query_all(self, query_all):
        """Sets the query_all of this SearchMeetingsRequest.

        是否查询企业下所有用户的会议记录。默认值为false。 * true：查询所有用户的会议 * false：仅查询管理员自己创建的会议 > 仅对企业管理员生效。

        :param query_all: The query_all of this SearchMeetingsRequest.
        :type query_all: bool
        """
        self._query_all = query_all

    @property
    def search_key(self):
        """Gets the search_key of this SearchMeetingsRequest.

        查询条件。会议主题、会议预约人和会议ID等可作为搜索内容。长度限制为1-128个字符。

        :return: The search_key of this SearchMeetingsRequest.
        :rtype: str
        """
        return self._search_key

    @search_key.setter
    def search_key(self, search_key):
        """Sets the search_key of this SearchMeetingsRequest.

        查询条件。会议主题、会议预约人和会议ID等可作为搜索内容。长度限制为1-128个字符。

        :param search_key: The search_key of this SearchMeetingsRequest.
        :type search_key: str
        """
        self._search_key = search_key

    @property
    def query_conf_mode(self):
        """Gets the query_conf_mode of this SearchMeetingsRequest.

        查询时间范围。 - ADAY:  一天 - AWEEK:  一周 - AMONTH:  一个月 - ALL:  查询所有

        :return: The query_conf_mode of this SearchMeetingsRequest.
        :rtype: str
        """
        return self._query_conf_mode

    @query_conf_mode.setter
    def query_conf_mode(self, query_conf_mode):
        """Sets the query_conf_mode of this SearchMeetingsRequest.

        查询时间范围。 - ADAY:  一天 - AWEEK:  一周 - AMONTH:  一个月 - ALL:  查询所有

        :param query_conf_mode: The query_conf_mode of this SearchMeetingsRequest.
        :type query_conf_mode: str
        """
        self._query_conf_mode = query_conf_mode

    @property
    def sort_type(self):
        """Gets the sort_type of this SearchMeetingsRequest.

        查询结果排序。 - ASC_StartTIME:  按会议开始时间升序排序 - DSC_StartTIME:  按会议开始时间降序排序

        :return: The sort_type of this SearchMeetingsRequest.
        :rtype: str
        """
        return self._sort_type

    @sort_type.setter
    def sort_type(self, sort_type):
        """Sets the sort_type of this SearchMeetingsRequest.

        查询结果排序。 - ASC_StartTIME:  按会议开始时间升序排序 - DSC_StartTIME:  按会议开始时间降序排序

        :param sort_type: The sort_type of this SearchMeetingsRequest.
        :type sort_type: str
        """
        self._sort_type = sort_type

    @property
    def x_authorization_type(self):
        """Gets the x_authorization_type of this SearchMeetingsRequest.

        标识是否为第三方portal过来的请求。 > 该参数将废弃，请勿使用。 

        :return: The x_authorization_type of this SearchMeetingsRequest.
        :rtype: str
        """
        return self._x_authorization_type

    @x_authorization_type.setter
    def x_authorization_type(self, x_authorization_type):
        """Sets the x_authorization_type of this SearchMeetingsRequest.

        标识是否为第三方portal过来的请求。 > 该参数将废弃，请勿使用。 

        :param x_authorization_type: The x_authorization_type of this SearchMeetingsRequest.
        :type x_authorization_type: str
        """
        self._x_authorization_type = x_authorization_type

    @property
    def x_site_id(self):
        """Gets the x_site_id of this SearchMeetingsRequest.

        用于区分到哪个HCSO站点鉴权。 > 该参数将废弃，请勿使用。 

        :return: The x_site_id of this SearchMeetingsRequest.
        :rtype: str
        """
        return self._x_site_id

    @x_site_id.setter
    def x_site_id(self, x_site_id):
        """Sets the x_site_id of this SearchMeetingsRequest.

        用于区分到哪个HCSO站点鉴权。 > 该参数将废弃，请勿使用。 

        :param x_site_id: The x_site_id of this SearchMeetingsRequest.
        :type x_site_id: str
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
        if not isinstance(other, SearchMeetingsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
