# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowInstanceInfosResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status_code': 'int',
        'body': 'str',
        'header_map': 'object'
    }

    attribute_map = {
        'status_code': 'status_code',
        'body': 'body',
        'header_map': 'header_map'
    }

    def __init__(self, status_code=None, body=None, header_map=None):
        r"""ShowInstanceInfosResponse

        The model defined in huaweicloud sdk

        :param status_code: 响应码
        :type status_code: int
        :param body: 响应体
        :type body: str
        :param header_map: 响应头，结构为Map&lt;String,String&gt;
        :type header_map: object
        """
        
        super(ShowInstanceInfosResponse, self).__init__()

        self._status_code = None
        self._body = None
        self._header_map = None
        self.discriminator = None

        if status_code is not None:
            self.status_code = status_code
        if body is not None:
            self.body = body
        if header_map is not None:
            self.header_map = header_map

    @property
    def status_code(self):
        r"""Gets the status_code of this ShowInstanceInfosResponse.

        响应码

        :return: The status_code of this ShowInstanceInfosResponse.
        :rtype: int
        """
        return self._status_code

    @status_code.setter
    def status_code(self, status_code):
        r"""Sets the status_code of this ShowInstanceInfosResponse.

        响应码

        :param status_code: The status_code of this ShowInstanceInfosResponse.
        :type status_code: int
        """
        self._status_code = status_code

    @property
    def body(self):
        r"""Gets the body of this ShowInstanceInfosResponse.

        响应体

        :return: The body of this ShowInstanceInfosResponse.
        :rtype: str
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this ShowInstanceInfosResponse.

        响应体

        :param body: The body of this ShowInstanceInfosResponse.
        :type body: str
        """
        self._body = body

    @property
    def header_map(self):
        r"""Gets the header_map of this ShowInstanceInfosResponse.

        响应头，结构为Map<String,String>

        :return: The header_map of this ShowInstanceInfosResponse.
        :rtype: object
        """
        return self._header_map

    @header_map.setter
    def header_map(self, header_map):
        r"""Sets the header_map of this ShowInstanceInfosResponse.

        响应头，结构为Map<String,String>

        :param header_map: The header_map of this ShowInstanceInfosResponse.
        :type header_map: object
        """
        self._header_map = header_map

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
        if not isinstance(other, ShowInstanceInfosResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
