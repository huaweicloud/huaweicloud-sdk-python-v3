# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HttpVo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'request': 'ProtocolReqVo',
        'response': 'ProtocolResVo'
    }

    attribute_map = {
        'request': 'request',
        'response': 'response'
    }

    def __init__(self, request=None, response=None):
        r"""HttpVo

        The model defined in huaweicloud sdk

        :param request: 
        :type request: :class:`huaweicloudsdkcloudtest.v1.ProtocolReqVo`
        :param response: 
        :type response: :class:`huaweicloudsdkcloudtest.v1.ProtocolResVo`
        """
        
        

        self._request = None
        self._response = None
        self.discriminator = None

        if request is not None:
            self.request = request
        if response is not None:
            self.response = response

    @property
    def request(self):
        r"""Gets the request of this HttpVo.

        :return: The request of this HttpVo.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.ProtocolReqVo`
        """
        return self._request

    @request.setter
    def request(self, request):
        r"""Sets the request of this HttpVo.

        :param request: The request of this HttpVo.
        :type request: :class:`huaweicloudsdkcloudtest.v1.ProtocolReqVo`
        """
        self._request = request

    @property
    def response(self):
        r"""Gets the response of this HttpVo.

        :return: The response of this HttpVo.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.ProtocolResVo`
        """
        return self._response

    @response.setter
    def response(self, response):
        r"""Sets the response of this HttpVo.

        :param response: The response of this HttpVo.
        :type response: :class:`huaweicloudsdkcloudtest.v1.ProtocolResVo`
        """
        self._response = response

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, HttpVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
