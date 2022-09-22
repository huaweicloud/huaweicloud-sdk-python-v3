# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SearchCorpResourcesRequest:

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
        'start_expire_date': 'int',
        'end_expire_date': 'int',
        'type': 'str',
        'vmr_mode': 'int',
        'type_id': 'str',
        'order_id': 'str',
        'status': 'int'
    }

    attribute_map = {
        'x_request_id': 'X-Request-Id',
        'accept_language': 'Accept-Language',
        'offset': 'offset',
        'limit': 'limit',
        'search_key': 'searchKey',
        'start_expire_date': 'startExpireDate',
        'end_expire_date': 'endExpireDate',
        'type': 'type',
        'vmr_mode': 'vmrMode',
        'type_id': 'typeId',
        'order_id': 'orderId',
        'status': 'status'
    }

    def __init__(self, x_request_id=None, accept_language=None, offset=None, limit=None, search_key=None, start_expire_date=None, end_expire_date=None, type=None, vmr_mode=None, type_id=None, order_id=None, status=None):
        """SearchCorpResourcesRequest

        The model defined in huaweicloud sdk

        :param x_request_id: 请求requestId，用来标识一路请求，用于问题跟踪定位，建议使用UUID，若不携带，则后台自动生成。
        :type x_request_id: str
        :param accept_language: 语言参数，默认为中文zh-CN，英文为en-US。
        :type accept_language: str
        :param offset: 查询偏移量,若超过最大数量，则返回最后一页的数据。 默认值：0。 
        :type offset: int
        :param limit: 查询数量。 默认值：10。 
        :type limit: int
        :param search_key: 搜索条件，支持resourceId模糊查询。
        :type search_key: str
        :param start_expire_date: 查询过期时间在该时间戳之后的资源项。
        :type start_expire_date: int
        :param end_expire_date: 查询过期时间在该时间戳之前的资源项。
        :type end_expire_date: int
        :param type: 资源类型。 - VMR        - 云会议室 - CONF_CALL  - 会议并发数 - HARD_1080P - 1080P硬终端 - HARD_720P  - 720P硬终端 - SOFT       - 软终端用户数 - ROOM       - 大屏软终端 - LIVE       - 直播推流 - RECORD     - 录播空间 - HARD_THIRD_PARTY - 第三方硬终端帐号 - HUAWEI_VISION -智慧屏 &gt; 查询网络研讨会资源时type字段为VMR。 
        :type type: str
        :param vmr_mode: VMR模式，type为VMR时传递该参数 * 0：个人会议ID * 1：云会议室 * 2：网络研讨会 
        :type vmr_mode: int
        :param type_id: 资源类型Id,若想搜索5方VMR时，需携带5方vmrpkg对应的id。
        :type type_id: str
        :param order_id: 订单Id。
        :type order_id: str
        :param status: 订单状态。 - 0：正常 - 1：到期 - 2：停用 
        :type status: int
        """
        
        

        self._x_request_id = None
        self._accept_language = None
        self._offset = None
        self._limit = None
        self._search_key = None
        self._start_expire_date = None
        self._end_expire_date = None
        self._type = None
        self._vmr_mode = None
        self._type_id = None
        self._order_id = None
        self._status = None
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
        if start_expire_date is not None:
            self.start_expire_date = start_expire_date
        if end_expire_date is not None:
            self.end_expire_date = end_expire_date
        if type is not None:
            self.type = type
        if vmr_mode is not None:
            self.vmr_mode = vmr_mode
        if type_id is not None:
            self.type_id = type_id
        if order_id is not None:
            self.order_id = order_id
        if status is not None:
            self.status = status

    @property
    def x_request_id(self):
        """Gets the x_request_id of this SearchCorpResourcesRequest.

        请求requestId，用来标识一路请求，用于问题跟踪定位，建议使用UUID，若不携带，则后台自动生成。

        :return: The x_request_id of this SearchCorpResourcesRequest.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        """Sets the x_request_id of this SearchCorpResourcesRequest.

        请求requestId，用来标识一路请求，用于问题跟踪定位，建议使用UUID，若不携带，则后台自动生成。

        :param x_request_id: The x_request_id of this SearchCorpResourcesRequest.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

    @property
    def accept_language(self):
        """Gets the accept_language of this SearchCorpResourcesRequest.

        语言参数，默认为中文zh-CN，英文为en-US。

        :return: The accept_language of this SearchCorpResourcesRequest.
        :rtype: str
        """
        return self._accept_language

    @accept_language.setter
    def accept_language(self, accept_language):
        """Sets the accept_language of this SearchCorpResourcesRequest.

        语言参数，默认为中文zh-CN，英文为en-US。

        :param accept_language: The accept_language of this SearchCorpResourcesRequest.
        :type accept_language: str
        """
        self._accept_language = accept_language

    @property
    def offset(self):
        """Gets the offset of this SearchCorpResourcesRequest.

        查询偏移量,若超过最大数量，则返回最后一页的数据。 默认值：0。 

        :return: The offset of this SearchCorpResourcesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this SearchCorpResourcesRequest.

        查询偏移量,若超过最大数量，则返回最后一页的数据。 默认值：0。 

        :param offset: The offset of this SearchCorpResourcesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this SearchCorpResourcesRequest.

        查询数量。 默认值：10。 

        :return: The limit of this SearchCorpResourcesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this SearchCorpResourcesRequest.

        查询数量。 默认值：10。 

        :param limit: The limit of this SearchCorpResourcesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def search_key(self):
        """Gets the search_key of this SearchCorpResourcesRequest.

        搜索条件，支持resourceId模糊查询。

        :return: The search_key of this SearchCorpResourcesRequest.
        :rtype: str
        """
        return self._search_key

    @search_key.setter
    def search_key(self, search_key):
        """Sets the search_key of this SearchCorpResourcesRequest.

        搜索条件，支持resourceId模糊查询。

        :param search_key: The search_key of this SearchCorpResourcesRequest.
        :type search_key: str
        """
        self._search_key = search_key

    @property
    def start_expire_date(self):
        """Gets the start_expire_date of this SearchCorpResourcesRequest.

        查询过期时间在该时间戳之后的资源项。

        :return: The start_expire_date of this SearchCorpResourcesRequest.
        :rtype: int
        """
        return self._start_expire_date

    @start_expire_date.setter
    def start_expire_date(self, start_expire_date):
        """Sets the start_expire_date of this SearchCorpResourcesRequest.

        查询过期时间在该时间戳之后的资源项。

        :param start_expire_date: The start_expire_date of this SearchCorpResourcesRequest.
        :type start_expire_date: int
        """
        self._start_expire_date = start_expire_date

    @property
    def end_expire_date(self):
        """Gets the end_expire_date of this SearchCorpResourcesRequest.

        查询过期时间在该时间戳之前的资源项。

        :return: The end_expire_date of this SearchCorpResourcesRequest.
        :rtype: int
        """
        return self._end_expire_date

    @end_expire_date.setter
    def end_expire_date(self, end_expire_date):
        """Sets the end_expire_date of this SearchCorpResourcesRequest.

        查询过期时间在该时间戳之前的资源项。

        :param end_expire_date: The end_expire_date of this SearchCorpResourcesRequest.
        :type end_expire_date: int
        """
        self._end_expire_date = end_expire_date

    @property
    def type(self):
        """Gets the type of this SearchCorpResourcesRequest.

        资源类型。 - VMR        - 云会议室 - CONF_CALL  - 会议并发数 - HARD_1080P - 1080P硬终端 - HARD_720P  - 720P硬终端 - SOFT       - 软终端用户数 - ROOM       - 大屏软终端 - LIVE       - 直播推流 - RECORD     - 录播空间 - HARD_THIRD_PARTY - 第三方硬终端帐号 - HUAWEI_VISION -智慧屏 > 查询网络研讨会资源时type字段为VMR。 

        :return: The type of this SearchCorpResourcesRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SearchCorpResourcesRequest.

        资源类型。 - VMR        - 云会议室 - CONF_CALL  - 会议并发数 - HARD_1080P - 1080P硬终端 - HARD_720P  - 720P硬终端 - SOFT       - 软终端用户数 - ROOM       - 大屏软终端 - LIVE       - 直播推流 - RECORD     - 录播空间 - HARD_THIRD_PARTY - 第三方硬终端帐号 - HUAWEI_VISION -智慧屏 > 查询网络研讨会资源时type字段为VMR。 

        :param type: The type of this SearchCorpResourcesRequest.
        :type type: str
        """
        self._type = type

    @property
    def vmr_mode(self):
        """Gets the vmr_mode of this SearchCorpResourcesRequest.

        VMR模式，type为VMR时传递该参数 * 0：个人会议ID * 1：云会议室 * 2：网络研讨会 

        :return: The vmr_mode of this SearchCorpResourcesRequest.
        :rtype: int
        """
        return self._vmr_mode

    @vmr_mode.setter
    def vmr_mode(self, vmr_mode):
        """Sets the vmr_mode of this SearchCorpResourcesRequest.

        VMR模式，type为VMR时传递该参数 * 0：个人会议ID * 1：云会议室 * 2：网络研讨会 

        :param vmr_mode: The vmr_mode of this SearchCorpResourcesRequest.
        :type vmr_mode: int
        """
        self._vmr_mode = vmr_mode

    @property
    def type_id(self):
        """Gets the type_id of this SearchCorpResourcesRequest.

        资源类型Id,若想搜索5方VMR时，需携带5方vmrpkg对应的id。

        :return: The type_id of this SearchCorpResourcesRequest.
        :rtype: str
        """
        return self._type_id

    @type_id.setter
    def type_id(self, type_id):
        """Sets the type_id of this SearchCorpResourcesRequest.

        资源类型Id,若想搜索5方VMR时，需携带5方vmrpkg对应的id。

        :param type_id: The type_id of this SearchCorpResourcesRequest.
        :type type_id: str
        """
        self._type_id = type_id

    @property
    def order_id(self):
        """Gets the order_id of this SearchCorpResourcesRequest.

        订单Id。

        :return: The order_id of this SearchCorpResourcesRequest.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this SearchCorpResourcesRequest.

        订单Id。

        :param order_id: The order_id of this SearchCorpResourcesRequest.
        :type order_id: str
        """
        self._order_id = order_id

    @property
    def status(self):
        """Gets the status of this SearchCorpResourcesRequest.

        订单状态。 - 0：正常 - 1：到期 - 2：停用 

        :return: The status of this SearchCorpResourcesRequest.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this SearchCorpResourcesRequest.

        订单状态。 - 0：正常 - 1：到期 - 2：停用 

        :param status: The status of this SearchCorpResourcesRequest.
        :type status: int
        """
        self._status = status

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
        if not isinstance(other, SearchCorpResourcesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
