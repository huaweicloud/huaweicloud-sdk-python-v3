# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListIndicatorsResponse(SdkResponse):

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
        'data': 'list[IndicatorDetail]',
        'x_request_id': 'str'
    }

    attribute_map = {
        'code': 'code',
        'message': 'message',
        'total': 'total',
        'data': 'data',
        'x_request_id': 'X-request-id'
    }

    def __init__(self, code=None, message=None, total=None, data=None, x_request_id=None):
        """ListIndicatorsResponse

        The model defined in huaweicloud sdk

        :param code: Id value
        :type code: str
        :param message: Error message
        :type message: str
        :param total: tatal count
        :type total: int
        :param data: list of informations of indicator
        :type data: list[:class:`huaweicloudsdksecmaster.v2.IndicatorDetail`]
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(ListIndicatorsResponse, self).__init__()

        self._code = None
        self._message = None
        self._total = None
        self._data = None
        self._x_request_id = None
        self.discriminator = None

        if code is not None:
            self.code = code
        if message is not None:
            self.message = message
        if total is not None:
            self.total = total
        if data is not None:
            self.data = data
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def code(self):
        """Gets the code of this ListIndicatorsResponse.

        Id value

        :return: The code of this ListIndicatorsResponse.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this ListIndicatorsResponse.

        Id value

        :param code: The code of this ListIndicatorsResponse.
        :type code: str
        """
        self._code = code

    @property
    def message(self):
        """Gets the message of this ListIndicatorsResponse.

        Error message

        :return: The message of this ListIndicatorsResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this ListIndicatorsResponse.

        Error message

        :param message: The message of this ListIndicatorsResponse.
        :type message: str
        """
        self._message = message

    @property
    def total(self):
        """Gets the total of this ListIndicatorsResponse.

        tatal count

        :return: The total of this ListIndicatorsResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ListIndicatorsResponse.

        tatal count

        :param total: The total of this ListIndicatorsResponse.
        :type total: int
        """
        self._total = total

    @property
    def data(self):
        """Gets the data of this ListIndicatorsResponse.

        list of informations of indicator

        :return: The data of this ListIndicatorsResponse.
        :rtype: list[:class:`huaweicloudsdksecmaster.v2.IndicatorDetail`]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this ListIndicatorsResponse.

        list of informations of indicator

        :param data: The data of this ListIndicatorsResponse.
        :type data: list[:class:`huaweicloudsdksecmaster.v2.IndicatorDetail`]
        """
        self._data = data

    @property
    def x_request_id(self):
        """Gets the x_request_id of this ListIndicatorsResponse.

        :return: The x_request_id of this ListIndicatorsResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        """Sets the x_request_id of this ListIndicatorsResponse.

        :param x_request_id: The x_request_id of this ListIndicatorsResponse.
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
        if not isinstance(other, ListIndicatorsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
