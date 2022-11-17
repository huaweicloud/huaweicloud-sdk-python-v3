# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SearchHisMeetingsRequest:

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
        'search_key': 'str',
        'query_all': 'bool',
        'start_date': 'int',
        'end_date': 'int',
        'sort_type': 'str',
        'x_authorization_type': 'str',
        'x_site_id': 'str'
    }

    attribute_map = {
        'user_uuid': 'userUUID',
        'offset': 'offset',
        'limit': 'limit',
        'search_key': 'searchKey',
        'query_all': 'queryAll',
        'start_date': 'startDate',
        'end_date': 'endDate',
        'sort_type': 'sortType',
        'x_authorization_type': 'X-Authorization-Type',
        'x_site_id': 'X-Site-Id'
    }

    def __init__(self, user_uuid=None, offset=None, limit=None, search_key=None, query_all=None, start_date=None, end_date=None, sort_type=None, x_authorization_type=None, x_site_id=None):
        """SearchHisMeetingsRequest

        The model defined in huaweicloud sdk

        :param user_uuid: 用户的UUID。 &gt; 该参数将废弃，请勿使用。
        :type user_uuid: str
        :param offset: 查询偏移量。默认为0。
        :type offset: int
        :param limit: 查询数量。默认是20，最大500条。
        :type limit: int
        :param search_key: 查询条件。会议主题、会议预约人和会议ID等可作为搜索内容。
        :type search_key: str
        :param query_all: 是否查询企业下所有用户的历史会议。 * true：查询所有用户的历史会议 * false：仅查询管理员自己的历史会议 &gt; 仅对企业管理员生效。
        :type query_all: bool
        :param start_date: 查询的起始时间戳（单位毫秒）。
        :type start_date: int
        :param end_date: 查询的截止时间戳（单位毫秒）。
        :type end_date: int
        :param sort_type: 查询结果排序类型。 * ASC_StartTIME：根据会议开始时间升序排序 * DSC_StartTIME：根据会议开始时间降序排序 * ASC_RecordTYPE：根据是否具有录播文件排序，之后默认按照会议开始时间升序排序 * DSC_RecordTYPE：根据是否含有录播文件排序，之后默认按照会议开始时间降序排序
        :type sort_type: str
        :param x_authorization_type: 标识是否为第三方portal过来的请求。 &gt; 该参数将废弃，请勿使用。 
        :type x_authorization_type: str
        :param x_site_id: 用于区分到哪个HCSO站点鉴权。 &gt; 该参数将废弃，请勿使用。 
        :type x_site_id: str
        """
        
        

        self._user_uuid = None
        self._offset = None
        self._limit = None
        self._search_key = None
        self._query_all = None
        self._start_date = None
        self._end_date = None
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
        if search_key is not None:
            self.search_key = search_key
        if query_all is not None:
            self.query_all = query_all
        self.start_date = start_date
        self.end_date = end_date
        if sort_type is not None:
            self.sort_type = sort_type
        if x_authorization_type is not None:
            self.x_authorization_type = x_authorization_type
        if x_site_id is not None:
            self.x_site_id = x_site_id

    @property
    def user_uuid(self):
        """Gets the user_uuid of this SearchHisMeetingsRequest.

        用户的UUID。 > 该参数将废弃，请勿使用。

        :return: The user_uuid of this SearchHisMeetingsRequest.
        :rtype: str
        """
        return self._user_uuid

    @user_uuid.setter
    def user_uuid(self, user_uuid):
        """Sets the user_uuid of this SearchHisMeetingsRequest.

        用户的UUID。 > 该参数将废弃，请勿使用。

        :param user_uuid: The user_uuid of this SearchHisMeetingsRequest.
        :type user_uuid: str
        """
        self._user_uuid = user_uuid

    @property
    def offset(self):
        """Gets the offset of this SearchHisMeetingsRequest.

        查询偏移量。默认为0。

        :return: The offset of this SearchHisMeetingsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this SearchHisMeetingsRequest.

        查询偏移量。默认为0。

        :param offset: The offset of this SearchHisMeetingsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this SearchHisMeetingsRequest.

        查询数量。默认是20，最大500条。

        :return: The limit of this SearchHisMeetingsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this SearchHisMeetingsRequest.

        查询数量。默认是20，最大500条。

        :param limit: The limit of this SearchHisMeetingsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def search_key(self):
        """Gets the search_key of this SearchHisMeetingsRequest.

        查询条件。会议主题、会议预约人和会议ID等可作为搜索内容。

        :return: The search_key of this SearchHisMeetingsRequest.
        :rtype: str
        """
        return self._search_key

    @search_key.setter
    def search_key(self, search_key):
        """Sets the search_key of this SearchHisMeetingsRequest.

        查询条件。会议主题、会议预约人和会议ID等可作为搜索内容。

        :param search_key: The search_key of this SearchHisMeetingsRequest.
        :type search_key: str
        """
        self._search_key = search_key

    @property
    def query_all(self):
        """Gets the query_all of this SearchHisMeetingsRequest.

        是否查询企业下所有用户的历史会议。 * true：查询所有用户的历史会议 * false：仅查询管理员自己的历史会议 > 仅对企业管理员生效。

        :return: The query_all of this SearchHisMeetingsRequest.
        :rtype: bool
        """
        return self._query_all

    @query_all.setter
    def query_all(self, query_all):
        """Sets the query_all of this SearchHisMeetingsRequest.

        是否查询企业下所有用户的历史会议。 * true：查询所有用户的历史会议 * false：仅查询管理员自己的历史会议 > 仅对企业管理员生效。

        :param query_all: The query_all of this SearchHisMeetingsRequest.
        :type query_all: bool
        """
        self._query_all = query_all

    @property
    def start_date(self):
        """Gets the start_date of this SearchHisMeetingsRequest.

        查询的起始时间戳（单位毫秒）。

        :return: The start_date of this SearchHisMeetingsRequest.
        :rtype: int
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this SearchHisMeetingsRequest.

        查询的起始时间戳（单位毫秒）。

        :param start_date: The start_date of this SearchHisMeetingsRequest.
        :type start_date: int
        """
        self._start_date = start_date

    @property
    def end_date(self):
        """Gets the end_date of this SearchHisMeetingsRequest.

        查询的截止时间戳（单位毫秒）。

        :return: The end_date of this SearchHisMeetingsRequest.
        :rtype: int
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this SearchHisMeetingsRequest.

        查询的截止时间戳（单位毫秒）。

        :param end_date: The end_date of this SearchHisMeetingsRequest.
        :type end_date: int
        """
        self._end_date = end_date

    @property
    def sort_type(self):
        """Gets the sort_type of this SearchHisMeetingsRequest.

        查询结果排序类型。 * ASC_StartTIME：根据会议开始时间升序排序 * DSC_StartTIME：根据会议开始时间降序排序 * ASC_RecordTYPE：根据是否具有录播文件排序，之后默认按照会议开始时间升序排序 * DSC_RecordTYPE：根据是否含有录播文件排序，之后默认按照会议开始时间降序排序

        :return: The sort_type of this SearchHisMeetingsRequest.
        :rtype: str
        """
        return self._sort_type

    @sort_type.setter
    def sort_type(self, sort_type):
        """Sets the sort_type of this SearchHisMeetingsRequest.

        查询结果排序类型。 * ASC_StartTIME：根据会议开始时间升序排序 * DSC_StartTIME：根据会议开始时间降序排序 * ASC_RecordTYPE：根据是否具有录播文件排序，之后默认按照会议开始时间升序排序 * DSC_RecordTYPE：根据是否含有录播文件排序，之后默认按照会议开始时间降序排序

        :param sort_type: The sort_type of this SearchHisMeetingsRequest.
        :type sort_type: str
        """
        self._sort_type = sort_type

    @property
    def x_authorization_type(self):
        """Gets the x_authorization_type of this SearchHisMeetingsRequest.

        标识是否为第三方portal过来的请求。 > 该参数将废弃，请勿使用。 

        :return: The x_authorization_type of this SearchHisMeetingsRequest.
        :rtype: str
        """
        return self._x_authorization_type

    @x_authorization_type.setter
    def x_authorization_type(self, x_authorization_type):
        """Sets the x_authorization_type of this SearchHisMeetingsRequest.

        标识是否为第三方portal过来的请求。 > 该参数将废弃，请勿使用。 

        :param x_authorization_type: The x_authorization_type of this SearchHisMeetingsRequest.
        :type x_authorization_type: str
        """
        self._x_authorization_type = x_authorization_type

    @property
    def x_site_id(self):
        """Gets the x_site_id of this SearchHisMeetingsRequest.

        用于区分到哪个HCSO站点鉴权。 > 该参数将废弃，请勿使用。 

        :return: The x_site_id of this SearchHisMeetingsRequest.
        :rtype: str
        """
        return self._x_site_id

    @x_site_id.setter
    def x_site_id(self, x_site_id):
        """Sets the x_site_id of this SearchHisMeetingsRequest.

        用于区分到哪个HCSO站点鉴权。 > 该参数将废弃，请勿使用。 

        :param x_site_id: The x_site_id of this SearchHisMeetingsRequest.
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
        if not isinstance(other, SearchHisMeetingsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
