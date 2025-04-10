# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GetHttpDetectResponseBodyDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'http_code': 'int',
        'http_response': 'str'
    }

    attribute_map = {
        'http_code': 'httpCode',
        'http_response': 'httpResponse'
    }

    def __init__(self, http_code=None, http_response=None):
        r"""GetHttpDetectResponseBodyDetail

        The model defined in huaweicloud sdk

        :param http_code: 探测终端返回的http返回码，0代表用户在黑名单无法发送，-1代表用户终端超过5秒未响应，-2代表队列已满，Http探测任务未执行。其他httpcode为终端实际返回值。
        :type http_code: int
        :param http_response: 终端探测响应体，如果httpCode为0，-1，-2, 2xx时响应体内容固定，由SMN定义。其余httpCode的响应体内容为终端返回内容。
        :type http_response: str
        """
        
        

        self._http_code = None
        self._http_response = None
        self.discriminator = None

        self.http_code = http_code
        self.http_response = http_response

    @property
    def http_code(self):
        r"""Gets the http_code of this GetHttpDetectResponseBodyDetail.

        探测终端返回的http返回码，0代表用户在黑名单无法发送，-1代表用户终端超过5秒未响应，-2代表队列已满，Http探测任务未执行。其他httpcode为终端实际返回值。

        :return: The http_code of this GetHttpDetectResponseBodyDetail.
        :rtype: int
        """
        return self._http_code

    @http_code.setter
    def http_code(self, http_code):
        r"""Sets the http_code of this GetHttpDetectResponseBodyDetail.

        探测终端返回的http返回码，0代表用户在黑名单无法发送，-1代表用户终端超过5秒未响应，-2代表队列已满，Http探测任务未执行。其他httpcode为终端实际返回值。

        :param http_code: The http_code of this GetHttpDetectResponseBodyDetail.
        :type http_code: int
        """
        self._http_code = http_code

    @property
    def http_response(self):
        r"""Gets the http_response of this GetHttpDetectResponseBodyDetail.

        终端探测响应体，如果httpCode为0，-1，-2, 2xx时响应体内容固定，由SMN定义。其余httpCode的响应体内容为终端返回内容。

        :return: The http_response of this GetHttpDetectResponseBodyDetail.
        :rtype: str
        """
        return self._http_response

    @http_response.setter
    def http_response(self, http_response):
        r"""Sets the http_response of this GetHttpDetectResponseBodyDetail.

        终端探测响应体，如果httpCode为0，-1，-2, 2xx时响应体内容固定，由SMN定义。其余httpCode的响应体内容为终端返回内容。

        :param http_response: The http_response of this GetHttpDetectResponseBodyDetail.
        :type http_response: str
        """
        self._http_response = http_response

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
        if not isinstance(other, GetHttpDetectResponseBodyDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
