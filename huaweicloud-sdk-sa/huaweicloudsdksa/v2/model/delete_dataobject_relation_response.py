# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteDataobjectRelationResponse(SdkResponse):

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
        'request_id': 'str',
        'success': 'bool',
        'total': 'int',
        'limit': 'int',
        'offset': 'int',
        'data': 'DataResponse',
        'x_request_id': 'str'
    }

    attribute_map = {
        'code': 'code',
        'message': 'message',
        'request_id': 'request_id',
        'success': 'success',
        'total': 'total',
        'limit': 'limit',
        'offset': 'offset',
        'data': 'data',
        'x_request_id': 'X-request-id'
    }

    def __init__(self, code=None, message=None, request_id=None, success=None, total=None, limit=None, offset=None, data=None, x_request_id=None):
        """DeleteDataobjectRelationResponse

        The model defined in huaweicloud sdk

        :param code: Id value
        :type code: str
        :param message: Error message
        :type message: str
        :param request_id: Error message
        :type request_id: str
        :param success: Error message
        :type success: bool
        :param total: tatal count
        :type total: int
        :param limit: current page count
        :type limit: int
        :param offset: current page size
        :type offset: int
        :param data: 
        :type data: :class:`huaweicloudsdksa.v2.DataResponse`
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(DeleteDataobjectRelationResponse, self).__init__()

        self._code = None
        self._message = None
        self._request_id = None
        self._success = None
        self._total = None
        self._limit = None
        self._offset = None
        self._data = None
        self._x_request_id = None
        self.discriminator = None

        if code is not None:
            self.code = code
        if message is not None:
            self.message = message
        if request_id is not None:
            self.request_id = request_id
        if success is not None:
            self.success = success
        if total is not None:
            self.total = total
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if data is not None:
            self.data = data
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def code(self):
        """Gets the code of this DeleteDataobjectRelationResponse.

        Id value

        :return: The code of this DeleteDataobjectRelationResponse.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this DeleteDataobjectRelationResponse.

        Id value

        :param code: The code of this DeleteDataobjectRelationResponse.
        :type code: str
        """
        self._code = code

    @property
    def message(self):
        """Gets the message of this DeleteDataobjectRelationResponse.

        Error message

        :return: The message of this DeleteDataobjectRelationResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this DeleteDataobjectRelationResponse.

        Error message

        :param message: The message of this DeleteDataobjectRelationResponse.
        :type message: str
        """
        self._message = message

    @property
    def request_id(self):
        """Gets the request_id of this DeleteDataobjectRelationResponse.

        Error message

        :return: The request_id of this DeleteDataobjectRelationResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this DeleteDataobjectRelationResponse.

        Error message

        :param request_id: The request_id of this DeleteDataobjectRelationResponse.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def success(self):
        """Gets the success of this DeleteDataobjectRelationResponse.

        Error message

        :return: The success of this DeleteDataobjectRelationResponse.
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this DeleteDataobjectRelationResponse.

        Error message

        :param success: The success of this DeleteDataobjectRelationResponse.
        :type success: bool
        """
        self._success = success

    @property
    def total(self):
        """Gets the total of this DeleteDataobjectRelationResponse.

        tatal count

        :return: The total of this DeleteDataobjectRelationResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this DeleteDataobjectRelationResponse.

        tatal count

        :param total: The total of this DeleteDataobjectRelationResponse.
        :type total: int
        """
        self._total = total

    @property
    def limit(self):
        """Gets the limit of this DeleteDataobjectRelationResponse.

        current page count

        :return: The limit of this DeleteDataobjectRelationResponse.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this DeleteDataobjectRelationResponse.

        current page count

        :param limit: The limit of this DeleteDataobjectRelationResponse.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this DeleteDataobjectRelationResponse.

        current page size

        :return: The offset of this DeleteDataobjectRelationResponse.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this DeleteDataobjectRelationResponse.

        current page size

        :param offset: The offset of this DeleteDataobjectRelationResponse.
        :type offset: int
        """
        self._offset = offset

    @property
    def data(self):
        """Gets the data of this DeleteDataobjectRelationResponse.

        :return: The data of this DeleteDataobjectRelationResponse.
        :rtype: :class:`huaweicloudsdksa.v2.DataResponse`
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this DeleteDataobjectRelationResponse.

        :param data: The data of this DeleteDataobjectRelationResponse.
        :type data: :class:`huaweicloudsdksa.v2.DataResponse`
        """
        self._data = data

    @property
    def x_request_id(self):
        """Gets the x_request_id of this DeleteDataobjectRelationResponse.

        :return: The x_request_id of this DeleteDataobjectRelationResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        """Sets the x_request_id of this DeleteDataobjectRelationResponse.

        :param x_request_id: The x_request_id of this DeleteDataobjectRelationResponse.
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
        if not isinstance(other, DeleteDataobjectRelationResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
