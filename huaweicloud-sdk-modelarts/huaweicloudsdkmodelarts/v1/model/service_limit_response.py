# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ServiceLimitResponse:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'rate_limit': 'RateLimitResponse',
        'request_size_limit': 'int',
        'request_timeout': 'int',
        'ip_white_list': 'list[str]',
        'ip_black_list': 'list[str]'
    }

    attribute_map = {
        'rate_limit': 'rate_limit',
        'request_size_limit': 'request_size_limit',
        'request_timeout': 'request_timeout',
        'ip_white_list': 'ip_white_list',
        'ip_black_list': 'ip_black_list'
    }

    def __init__(self, rate_limit=None, request_size_limit=None, request_timeout=None, ip_white_list=None, ip_black_list=None):
        r"""ServiceLimitResponse

        The model defined in huaweicloud sdk

        :param rate_limit: 
        :type rate_limit: :class:`huaweicloudsdkmodelarts.v1.RateLimitResponse`
        :param request_size_limit: **参数解释：** 请求大小限制。 **取值范围：** 1-50M。
        :type request_size_limit: int
        :param request_timeout: **参数解释：** 超时时间。 **取值范围：** 1到7200秒。
        :type request_timeout: int
        :param ip_white_list: **参数解释：** IP白名单。
        :type ip_white_list: list[str]
        :param ip_black_list: **参数解释：** IP黑名单。
        :type ip_black_list: list[str]
        """
        
        

        self._rate_limit = None
        self._request_size_limit = None
        self._request_timeout = None
        self._ip_white_list = None
        self._ip_black_list = None
        self.discriminator = None

        self.rate_limit = rate_limit
        self.request_size_limit = request_size_limit
        self.request_timeout = request_timeout
        if ip_white_list is not None:
            self.ip_white_list = ip_white_list
        if ip_black_list is not None:
            self.ip_black_list = ip_black_list

    @property
    def rate_limit(self):
        r"""Gets the rate_limit of this ServiceLimitResponse.

        :return: The rate_limit of this ServiceLimitResponse.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.RateLimitResponse`
        """
        return self._rate_limit

    @rate_limit.setter
    def rate_limit(self, rate_limit):
        r"""Sets the rate_limit of this ServiceLimitResponse.

        :param rate_limit: The rate_limit of this ServiceLimitResponse.
        :type rate_limit: :class:`huaweicloudsdkmodelarts.v1.RateLimitResponse`
        """
        self._rate_limit = rate_limit

    @property
    def request_size_limit(self):
        r"""Gets the request_size_limit of this ServiceLimitResponse.

        **参数解释：** 请求大小限制。 **取值范围：** 1-50M。

        :return: The request_size_limit of this ServiceLimitResponse.
        :rtype: int
        """
        return self._request_size_limit

    @request_size_limit.setter
    def request_size_limit(self, request_size_limit):
        r"""Sets the request_size_limit of this ServiceLimitResponse.

        **参数解释：** 请求大小限制。 **取值范围：** 1-50M。

        :param request_size_limit: The request_size_limit of this ServiceLimitResponse.
        :type request_size_limit: int
        """
        self._request_size_limit = request_size_limit

    @property
    def request_timeout(self):
        r"""Gets the request_timeout of this ServiceLimitResponse.

        **参数解释：** 超时时间。 **取值范围：** 1到7200秒。

        :return: The request_timeout of this ServiceLimitResponse.
        :rtype: int
        """
        return self._request_timeout

    @request_timeout.setter
    def request_timeout(self, request_timeout):
        r"""Sets the request_timeout of this ServiceLimitResponse.

        **参数解释：** 超时时间。 **取值范围：** 1到7200秒。

        :param request_timeout: The request_timeout of this ServiceLimitResponse.
        :type request_timeout: int
        """
        self._request_timeout = request_timeout

    @property
    def ip_white_list(self):
        r"""Gets the ip_white_list of this ServiceLimitResponse.

        **参数解释：** IP白名单。

        :return: The ip_white_list of this ServiceLimitResponse.
        :rtype: list[str]
        """
        return self._ip_white_list

    @ip_white_list.setter
    def ip_white_list(self, ip_white_list):
        r"""Sets the ip_white_list of this ServiceLimitResponse.

        **参数解释：** IP白名单。

        :param ip_white_list: The ip_white_list of this ServiceLimitResponse.
        :type ip_white_list: list[str]
        """
        self._ip_white_list = ip_white_list

    @property
    def ip_black_list(self):
        r"""Gets the ip_black_list of this ServiceLimitResponse.

        **参数解释：** IP黑名单。

        :return: The ip_black_list of this ServiceLimitResponse.
        :rtype: list[str]
        """
        return self._ip_black_list

    @ip_black_list.setter
    def ip_black_list(self, ip_black_list):
        r"""Sets the ip_black_list of this ServiceLimitResponse.

        **参数解释：** IP黑名单。

        :param ip_black_list: The ip_black_list of this ServiceLimitResponse.
        :type ip_black_list: list[str]
        """
        self._ip_black_list = ip_black_list

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
        if not isinstance(other, ServiceLimitResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
