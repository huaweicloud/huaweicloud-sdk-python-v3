# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListIncidentsResponse(SdkResponse):

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
        'data': 'list[ListIncidentDetail]',
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
        r"""ListIncidentsResponse

        The model defined in huaweicloud sdk

        :param code: Id value
        :type code: str
        :param message: Error message
        :type message: str
        :param total: tatal count
        :type total: int
        :param limit: 当前页大小
        :type limit: int
        :param offset: 当前页码
        :type offset: int
        :param success: success
        :type success: bool
        :param data: 事件列表
        :type data: list[:class:`huaweicloudsdksa.v2.ListIncidentDetail`]
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(ListIncidentsResponse, self).__init__()

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
        r"""Gets the code of this ListIncidentsResponse.

        Id value

        :return: The code of this ListIncidentsResponse.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        r"""Sets the code of this ListIncidentsResponse.

        Id value

        :param code: The code of this ListIncidentsResponse.
        :type code: str
        """
        self._code = code

    @property
    def message(self):
        r"""Gets the message of this ListIncidentsResponse.

        Error message

        :return: The message of this ListIncidentsResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this ListIncidentsResponse.

        Error message

        :param message: The message of this ListIncidentsResponse.
        :type message: str
        """
        self._message = message

    @property
    def total(self):
        r"""Gets the total of this ListIncidentsResponse.

        tatal count

        :return: The total of this ListIncidentsResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListIncidentsResponse.

        tatal count

        :param total: The total of this ListIncidentsResponse.
        :type total: int
        """
        self._total = total

    @property
    def limit(self):
        r"""Gets the limit of this ListIncidentsResponse.

        当前页大小

        :return: The limit of this ListIncidentsResponse.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListIncidentsResponse.

        当前页大小

        :param limit: The limit of this ListIncidentsResponse.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListIncidentsResponse.

        当前页码

        :return: The offset of this ListIncidentsResponse.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListIncidentsResponse.

        当前页码

        :param offset: The offset of this ListIncidentsResponse.
        :type offset: int
        """
        self._offset = offset

    @property
    def success(self):
        r"""Gets the success of this ListIncidentsResponse.

        success

        :return: The success of this ListIncidentsResponse.
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        r"""Sets the success of this ListIncidentsResponse.

        success

        :param success: The success of this ListIncidentsResponse.
        :type success: bool
        """
        self._success = success

    @property
    def data(self):
        r"""Gets the data of this ListIncidentsResponse.

        事件列表

        :return: The data of this ListIncidentsResponse.
        :rtype: list[:class:`huaweicloudsdksa.v2.ListIncidentDetail`]
        """
        return self._data

    @data.setter
    def data(self, data):
        r"""Sets the data of this ListIncidentsResponse.

        事件列表

        :param data: The data of this ListIncidentsResponse.
        :type data: list[:class:`huaweicloudsdksa.v2.ListIncidentDetail`]
        """
        self._data = data

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this ListIncidentsResponse.

        :return: The x_request_id of this ListIncidentsResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this ListIncidentsResponse.

        :param x_request_id: The x_request_id of this ListIncidentsResponse.
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
        if not isinstance(other, ListIncidentsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
