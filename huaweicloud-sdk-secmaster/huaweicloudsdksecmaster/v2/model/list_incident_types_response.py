# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListIncidentTypesResponse(SdkResponse):

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
        'data': 'list[DataClassTypeDetailInfo]',
        'total': 'int',
        'size': 'int',
        'page': 'int',
        'x_request_id': 'str'
    }

    attribute_map = {
        'code': 'code',
        'message': 'message',
        'data': 'data',
        'total': 'total',
        'size': 'size',
        'page': 'page',
        'x_request_id': 'X-request-id'
    }

    def __init__(self, code=None, message=None, data=None, total=None, size=None, page=None, x_request_id=None):
        """ListIncidentTypesResponse

        The model defined in huaweicloud sdk

        :param code: Error code
        :type code: str
        :param message: Error message
        :type message: str
        :param data: Response of dataclass detail
        :type data: list[:class:`huaweicloudsdksecmaster.v2.DataClassTypeDetailInfo`]
        :param total: tatal count
        :type total: int
        :param size: current page size
        :type size: int
        :param page: current page count
        :type page: int
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(ListIncidentTypesResponse, self).__init__()

        self._code = None
        self._message = None
        self._data = None
        self._total = None
        self._size = None
        self._page = None
        self._x_request_id = None
        self.discriminator = None

        if code is not None:
            self.code = code
        if message is not None:
            self.message = message
        if data is not None:
            self.data = data
        if total is not None:
            self.total = total
        if size is not None:
            self.size = size
        if page is not None:
            self.page = page
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def code(self):
        """Gets the code of this ListIncidentTypesResponse.

        Error code

        :return: The code of this ListIncidentTypesResponse.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this ListIncidentTypesResponse.

        Error code

        :param code: The code of this ListIncidentTypesResponse.
        :type code: str
        """
        self._code = code

    @property
    def message(self):
        """Gets the message of this ListIncidentTypesResponse.

        Error message

        :return: The message of this ListIncidentTypesResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this ListIncidentTypesResponse.

        Error message

        :param message: The message of this ListIncidentTypesResponse.
        :type message: str
        """
        self._message = message

    @property
    def data(self):
        """Gets the data of this ListIncidentTypesResponse.

        Response of dataclass detail

        :return: The data of this ListIncidentTypesResponse.
        :rtype: list[:class:`huaweicloudsdksecmaster.v2.DataClassTypeDetailInfo`]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this ListIncidentTypesResponse.

        Response of dataclass detail

        :param data: The data of this ListIncidentTypesResponse.
        :type data: list[:class:`huaweicloudsdksecmaster.v2.DataClassTypeDetailInfo`]
        """
        self._data = data

    @property
    def total(self):
        """Gets the total of this ListIncidentTypesResponse.

        tatal count

        :return: The total of this ListIncidentTypesResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ListIncidentTypesResponse.

        tatal count

        :param total: The total of this ListIncidentTypesResponse.
        :type total: int
        """
        self._total = total

    @property
    def size(self):
        """Gets the size of this ListIncidentTypesResponse.

        current page size

        :return: The size of this ListIncidentTypesResponse.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this ListIncidentTypesResponse.

        current page size

        :param size: The size of this ListIncidentTypesResponse.
        :type size: int
        """
        self._size = size

    @property
    def page(self):
        """Gets the page of this ListIncidentTypesResponse.

        current page count

        :return: The page of this ListIncidentTypesResponse.
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this ListIncidentTypesResponse.

        current page count

        :param page: The page of this ListIncidentTypesResponse.
        :type page: int
        """
        self._page = page

    @property
    def x_request_id(self):
        """Gets the x_request_id of this ListIncidentTypesResponse.

        :return: The x_request_id of this ListIncidentTypesResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        """Sets the x_request_id of this ListIncidentTypesResponse.

        :param x_request_id: The x_request_id of this ListIncidentTypesResponse.
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
        if not isinstance(other, ListIncidentTypesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
