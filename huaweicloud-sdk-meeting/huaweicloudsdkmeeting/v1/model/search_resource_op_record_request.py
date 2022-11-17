# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SearchResourceOpRecordRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'x_request_id': 'str',
        'accept_language': 'str',
        'offset': 'int',
        'limit': 'int',
        'search_key': 'str',
        'corp_id': 'str',
        'start_expire_date': 'int',
        'end_expire_date': 'int',
        'start_operate_date': 'int',
        'end_operate_date': 'int',
        'type': 'str',
        'type_id': 'str',
        'operate_type': 'int'
    }

    attribute_map = {
        'x_request_id': 'X-Request-Id',
        'accept_language': 'Accept-Language',
        'offset': 'offset',
        'limit': 'limit',
        'search_key': 'searchKey',
        'corp_id': 'corp_id',
        'start_expire_date': 'startExpireDate',
        'end_expire_date': 'endExpireDate',
        'start_operate_date': 'startOperateDate',
        'end_operate_date': 'endOperateDate',
        'type': 'type',
        'type_id': 'typeId',
        'operate_type': 'operateType'
    }

    def __init__(self, x_request_id=None, accept_language=None, offset=None, limit=None, search_key=None, corp_id=None, start_expire_date=None, end_expire_date=None, start_operate_date=None, end_operate_date=None, type=None, type_id=None, operate_type=None):
        """SearchResourceOpRecordRequest

        The model defined in huaweicloud sdk

        :param x_request_id: 请求requestId，用来标识一路请求，用于问题跟踪定位，建议使用UUID，若不携带，则后台自动生成。
        :type x_request_id: str
        :param accept_language: 语言参数，默认为中文zh-CN，英文为en-US。
        :type accept_language: str
        :param offset: 查询偏移量,若超过最大数量，则返回最后一页的数据。 默认值：0。 
        :type offset: int
        :param limit: 查询数量。 默认值：10。 
        :type limit: int
        :param search_key: 搜索条件。
        :type search_key: str
        :param corp_id: 企业id。
        :type corp_id: str
        :param start_expire_date: 查询过期时间在该时间戳之后的订单操作记录。
        :type start_expire_date: int
        :param end_expire_date: 查询过期时间在该时间戳之前的订单操作记录。
        :type end_expire_date: int
        :param start_operate_date: 查询操作时间在该时间戳之后的订单操作记录。
        :type start_operate_date: int
        :param end_operate_date: 查询操作时间在该时间戳之前的订单操作记录。
        :type end_operate_date: int
        :param type: 订单资源类型。
        :type type: str
        :param type_id: 当前仅当资源类型为vmr时生效。
        :type type_id: str
        :param operate_type: 操作类型。 - 0：添加 - 1：删除 - 2：修改 - 3：停用 - 4：启用
        :type operate_type: int
        """
        
        

        self._x_request_id = None
        self._accept_language = None
        self._offset = None
        self._limit = None
        self._search_key = None
        self._corp_id = None
        self._start_expire_date = None
        self._end_expire_date = None
        self._start_operate_date = None
        self._end_operate_date = None
        self._type = None
        self._type_id = None
        self._operate_type = None
        self.discriminator = None

        if x_request_id is not None:
            self.x_request_id = x_request_id
        if accept_language is not None:
            self.accept_language = accept_language
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if search_key is not None:
            self.search_key = search_key
        self.corp_id = corp_id
        if start_expire_date is not None:
            self.start_expire_date = start_expire_date
        if end_expire_date is not None:
            self.end_expire_date = end_expire_date
        if start_operate_date is not None:
            self.start_operate_date = start_operate_date
        if end_operate_date is not None:
            self.end_operate_date = end_operate_date
        if type is not None:
            self.type = type
        if type_id is not None:
            self.type_id = type_id
        if operate_type is not None:
            self.operate_type = operate_type

    @property
    def x_request_id(self):
        """Gets the x_request_id of this SearchResourceOpRecordRequest.

        请求requestId，用来标识一路请求，用于问题跟踪定位，建议使用UUID，若不携带，则后台自动生成。

        :return: The x_request_id of this SearchResourceOpRecordRequest.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        """Sets the x_request_id of this SearchResourceOpRecordRequest.

        请求requestId，用来标识一路请求，用于问题跟踪定位，建议使用UUID，若不携带，则后台自动生成。

        :param x_request_id: The x_request_id of this SearchResourceOpRecordRequest.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

    @property
    def accept_language(self):
        """Gets the accept_language of this SearchResourceOpRecordRequest.

        语言参数，默认为中文zh-CN，英文为en-US。

        :return: The accept_language of this SearchResourceOpRecordRequest.
        :rtype: str
        """
        return self._accept_language

    @accept_language.setter
    def accept_language(self, accept_language):
        """Sets the accept_language of this SearchResourceOpRecordRequest.

        语言参数，默认为中文zh-CN，英文为en-US。

        :param accept_language: The accept_language of this SearchResourceOpRecordRequest.
        :type accept_language: str
        """
        self._accept_language = accept_language

    @property
    def offset(self):
        """Gets the offset of this SearchResourceOpRecordRequest.

        查询偏移量,若超过最大数量，则返回最后一页的数据。 默认值：0。 

        :return: The offset of this SearchResourceOpRecordRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this SearchResourceOpRecordRequest.

        查询偏移量,若超过最大数量，则返回最后一页的数据。 默认值：0。 

        :param offset: The offset of this SearchResourceOpRecordRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this SearchResourceOpRecordRequest.

        查询数量。 默认值：10。 

        :return: The limit of this SearchResourceOpRecordRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this SearchResourceOpRecordRequest.

        查询数量。 默认值：10。 

        :param limit: The limit of this SearchResourceOpRecordRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def search_key(self):
        """Gets the search_key of this SearchResourceOpRecordRequest.

        搜索条件。

        :return: The search_key of this SearchResourceOpRecordRequest.
        :rtype: str
        """
        return self._search_key

    @search_key.setter
    def search_key(self, search_key):
        """Sets the search_key of this SearchResourceOpRecordRequest.

        搜索条件。

        :param search_key: The search_key of this SearchResourceOpRecordRequest.
        :type search_key: str
        """
        self._search_key = search_key

    @property
    def corp_id(self):
        """Gets the corp_id of this SearchResourceOpRecordRequest.

        企业id。

        :return: The corp_id of this SearchResourceOpRecordRequest.
        :rtype: str
        """
        return self._corp_id

    @corp_id.setter
    def corp_id(self, corp_id):
        """Sets the corp_id of this SearchResourceOpRecordRequest.

        企业id。

        :param corp_id: The corp_id of this SearchResourceOpRecordRequest.
        :type corp_id: str
        """
        self._corp_id = corp_id

    @property
    def start_expire_date(self):
        """Gets the start_expire_date of this SearchResourceOpRecordRequest.

        查询过期时间在该时间戳之后的订单操作记录。

        :return: The start_expire_date of this SearchResourceOpRecordRequest.
        :rtype: int
        """
        return self._start_expire_date

    @start_expire_date.setter
    def start_expire_date(self, start_expire_date):
        """Sets the start_expire_date of this SearchResourceOpRecordRequest.

        查询过期时间在该时间戳之后的订单操作记录。

        :param start_expire_date: The start_expire_date of this SearchResourceOpRecordRequest.
        :type start_expire_date: int
        """
        self._start_expire_date = start_expire_date

    @property
    def end_expire_date(self):
        """Gets the end_expire_date of this SearchResourceOpRecordRequest.

        查询过期时间在该时间戳之前的订单操作记录。

        :return: The end_expire_date of this SearchResourceOpRecordRequest.
        :rtype: int
        """
        return self._end_expire_date

    @end_expire_date.setter
    def end_expire_date(self, end_expire_date):
        """Sets the end_expire_date of this SearchResourceOpRecordRequest.

        查询过期时间在该时间戳之前的订单操作记录。

        :param end_expire_date: The end_expire_date of this SearchResourceOpRecordRequest.
        :type end_expire_date: int
        """
        self._end_expire_date = end_expire_date

    @property
    def start_operate_date(self):
        """Gets the start_operate_date of this SearchResourceOpRecordRequest.

        查询操作时间在该时间戳之后的订单操作记录。

        :return: The start_operate_date of this SearchResourceOpRecordRequest.
        :rtype: int
        """
        return self._start_operate_date

    @start_operate_date.setter
    def start_operate_date(self, start_operate_date):
        """Sets the start_operate_date of this SearchResourceOpRecordRequest.

        查询操作时间在该时间戳之后的订单操作记录。

        :param start_operate_date: The start_operate_date of this SearchResourceOpRecordRequest.
        :type start_operate_date: int
        """
        self._start_operate_date = start_operate_date

    @property
    def end_operate_date(self):
        """Gets the end_operate_date of this SearchResourceOpRecordRequest.

        查询操作时间在该时间戳之前的订单操作记录。

        :return: The end_operate_date of this SearchResourceOpRecordRequest.
        :rtype: int
        """
        return self._end_operate_date

    @end_operate_date.setter
    def end_operate_date(self, end_operate_date):
        """Sets the end_operate_date of this SearchResourceOpRecordRequest.

        查询操作时间在该时间戳之前的订单操作记录。

        :param end_operate_date: The end_operate_date of this SearchResourceOpRecordRequest.
        :type end_operate_date: int
        """
        self._end_operate_date = end_operate_date

    @property
    def type(self):
        """Gets the type of this SearchResourceOpRecordRequest.

        订单资源类型。

        :return: The type of this SearchResourceOpRecordRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SearchResourceOpRecordRequest.

        订单资源类型。

        :param type: The type of this SearchResourceOpRecordRequest.
        :type type: str
        """
        self._type = type

    @property
    def type_id(self):
        """Gets the type_id of this SearchResourceOpRecordRequest.

        当前仅当资源类型为vmr时生效。

        :return: The type_id of this SearchResourceOpRecordRequest.
        :rtype: str
        """
        return self._type_id

    @type_id.setter
    def type_id(self, type_id):
        """Sets the type_id of this SearchResourceOpRecordRequest.

        当前仅当资源类型为vmr时生效。

        :param type_id: The type_id of this SearchResourceOpRecordRequest.
        :type type_id: str
        """
        self._type_id = type_id

    @property
    def operate_type(self):
        """Gets the operate_type of this SearchResourceOpRecordRequest.

        操作类型。 - 0：添加 - 1：删除 - 2：修改 - 3：停用 - 4：启用

        :return: The operate_type of this SearchResourceOpRecordRequest.
        :rtype: int
        """
        return self._operate_type

    @operate_type.setter
    def operate_type(self, operate_type):
        """Sets the operate_type of this SearchResourceOpRecordRequest.

        操作类型。 - 0：添加 - 1：删除 - 2：修改 - 3：停用 - 4：启用

        :param operate_type: The operate_type of this SearchResourceOpRecordRequest.
        :type operate_type: int
        """
        self._operate_type = operate_type

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
        if not isinstance(other, SearchResourceOpRecordRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
