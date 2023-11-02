# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAlertsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'code': 'str',
        'message': 'str',
        'total': 'int',
        'limit': 'int',
        'offset': 'int',
        'success': 'bool',
        'data': 'list[ListAlertDetail]',
        'x_request_id': 'str'
    }

    attribute_map = {
        'code': 'code',
        'message': 'message',
        'total': 'total',
        'limit': 'limit',
        'offset': 'offset',
        'success': 'success',
        'data': 'data',
        'x_request_id': 'X-request-id'
    }

    def __init__(self, code=None, message=None, total=None, limit=None, offset=None, success=None, data=None, x_request_id=None):
        """ListAlertsResponse

        The model defined in huaweicloud sdk

        :param code: 错误码
        :type code: str
        :param message: 错误信息
        :type message: str
        :param total: 告警总数
        :type total: int
        :param limit: 分页大小
        :type limit: int
        :param offset: 偏移量
        :type offset: int
        :param success: 是否成功
        :type success: bool
        :param data: 告警列表
        :type data: list[:class:`huaweicloudsdksecmaster.v2.ListAlertDetail`]
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(ListAlertsResponse, self).__init__()

        self._code = None
        self._message = None
        self._total = None
        self._limit = None
        self._offset = None
        self._success = None
        self._data = None
        self._x_request_id = None
        self.discriminator = None

        if code is not None:
            self.code = code
        if message is not None:
            self.message = message
        if total is not None:
            self.total = total
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if success is not None:
            self.success = success
        if data is not None:
            self.data = data
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def code(self):
        """Gets the code of this ListAlertsResponse.

        错误码

        :return: The code of this ListAlertsResponse.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this ListAlertsResponse.

        错误码

        :param code: The code of this ListAlertsResponse.
        :type code: str
        """
        self._code = code

    @property
    def message(self):
        """Gets the message of this ListAlertsResponse.

        错误信息

        :return: The message of this ListAlertsResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this ListAlertsResponse.

        错误信息

        :param message: The message of this ListAlertsResponse.
        :type message: str
        """
        self._message = message

    @property
    def total(self):
        """Gets the total of this ListAlertsResponse.

        告警总数

        :return: The total of this ListAlertsResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ListAlertsResponse.

        告警总数

        :param total: The total of this ListAlertsResponse.
        :type total: int
        """
        self._total = total

    @property
    def limit(self):
        """Gets the limit of this ListAlertsResponse.

        分页大小

        :return: The limit of this ListAlertsResponse.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListAlertsResponse.

        分页大小

        :param limit: The limit of this ListAlertsResponse.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListAlertsResponse.

        偏移量

        :return: The offset of this ListAlertsResponse.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListAlertsResponse.

        偏移量

        :param offset: The offset of this ListAlertsResponse.
        :type offset: int
        """
        self._offset = offset

    @property
    def success(self):
        """Gets the success of this ListAlertsResponse.

        是否成功

        :return: The success of this ListAlertsResponse.
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this ListAlertsResponse.

        是否成功

        :param success: The success of this ListAlertsResponse.
        :type success: bool
        """
        self._success = success

    @property
    def data(self):
        """Gets the data of this ListAlertsResponse.

        告警列表

        :return: The data of this ListAlertsResponse.
        :rtype: list[:class:`huaweicloudsdksecmaster.v2.ListAlertDetail`]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this ListAlertsResponse.

        告警列表

        :param data: The data of this ListAlertsResponse.
        :type data: list[:class:`huaweicloudsdksecmaster.v2.ListAlertDetail`]
        """
        self._data = data

    @property
    def x_request_id(self):
        """Gets the x_request_id of this ListAlertsResponse.

        :return: The x_request_id of this ListAlertsResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        """Sets the x_request_id of this ListAlertsResponse.

        :param x_request_id: The x_request_id of this ListAlertsResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

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
        if not isinstance(other, ListAlertsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
