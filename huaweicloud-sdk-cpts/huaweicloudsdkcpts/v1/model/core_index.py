# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CoreIndex:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'error_request_count': 'int',
        'max_rps': 'int',
        'max_users': 'int',
        'request_count': 'int',
        'rps': 'float',
        'success_count': 'int',
        'success_rate': 'int',
        'trans_tps': 'float',
        'response_time': 'ResponseTimeInfo'
    }

    attribute_map = {
        'error_request_count': 'error_request_count',
        'max_rps': 'max_rps',
        'max_users': 'max_users',
        'request_count': 'request_count',
        'rps': 'rps',
        'success_count': 'success_count',
        'success_rate': 'success_rate',
        'trans_tps': 'trans_tps',
        'response_time': 'response_time'
    }

    def __init__(self, error_request_count=None, max_rps=None, max_users=None, request_count=None, rps=None, success_count=None, success_rate=None, trans_tps=None, response_time=None):
        r"""CoreIndex

        The model defined in huaweicloud sdk

        :param error_request_count: 错误请求数
        :type error_request_count: int
        :param max_rps: 最大RPS
        :type max_rps: int
        :param max_users: 最大并发数
        :type max_users: int
        :param request_count: 请求总数
        :type request_count: int
        :param rps: 平均RPS
        :type rps: float
        :param success_count: 成功数
        :type success_count: int
        :param success_rate: 成功率
        :type success_rate: int
        :param trans_tps: 平均TPS
        :type trans_tps: float
        :param response_time: 
        :type response_time: :class:`huaweicloudsdkcpts.v1.ResponseTimeInfo`
        """
        
        

        self._error_request_count = None
        self._max_rps = None
        self._max_users = None
        self._request_count = None
        self._rps = None
        self._success_count = None
        self._success_rate = None
        self._trans_tps = None
        self._response_time = None
        self.discriminator = None

        if error_request_count is not None:
            self.error_request_count = error_request_count
        if max_rps is not None:
            self.max_rps = max_rps
        if max_users is not None:
            self.max_users = max_users
        if request_count is not None:
            self.request_count = request_count
        if rps is not None:
            self.rps = rps
        if success_count is not None:
            self.success_count = success_count
        if success_rate is not None:
            self.success_rate = success_rate
        if trans_tps is not None:
            self.trans_tps = trans_tps
        if response_time is not None:
            self.response_time = response_time

    @property
    def error_request_count(self):
        r"""Gets the error_request_count of this CoreIndex.

        错误请求数

        :return: The error_request_count of this CoreIndex.
        :rtype: int
        """
        return self._error_request_count

    @error_request_count.setter
    def error_request_count(self, error_request_count):
        r"""Sets the error_request_count of this CoreIndex.

        错误请求数

        :param error_request_count: The error_request_count of this CoreIndex.
        :type error_request_count: int
        """
        self._error_request_count = error_request_count

    @property
    def max_rps(self):
        r"""Gets the max_rps of this CoreIndex.

        最大RPS

        :return: The max_rps of this CoreIndex.
        :rtype: int
        """
        return self._max_rps

    @max_rps.setter
    def max_rps(self, max_rps):
        r"""Sets the max_rps of this CoreIndex.

        最大RPS

        :param max_rps: The max_rps of this CoreIndex.
        :type max_rps: int
        """
        self._max_rps = max_rps

    @property
    def max_users(self):
        r"""Gets the max_users of this CoreIndex.

        最大并发数

        :return: The max_users of this CoreIndex.
        :rtype: int
        """
        return self._max_users

    @max_users.setter
    def max_users(self, max_users):
        r"""Sets the max_users of this CoreIndex.

        最大并发数

        :param max_users: The max_users of this CoreIndex.
        :type max_users: int
        """
        self._max_users = max_users

    @property
    def request_count(self):
        r"""Gets the request_count of this CoreIndex.

        请求总数

        :return: The request_count of this CoreIndex.
        :rtype: int
        """
        return self._request_count

    @request_count.setter
    def request_count(self, request_count):
        r"""Sets the request_count of this CoreIndex.

        请求总数

        :param request_count: The request_count of this CoreIndex.
        :type request_count: int
        """
        self._request_count = request_count

    @property
    def rps(self):
        r"""Gets the rps of this CoreIndex.

        平均RPS

        :return: The rps of this CoreIndex.
        :rtype: float
        """
        return self._rps

    @rps.setter
    def rps(self, rps):
        r"""Sets the rps of this CoreIndex.

        平均RPS

        :param rps: The rps of this CoreIndex.
        :type rps: float
        """
        self._rps = rps

    @property
    def success_count(self):
        r"""Gets the success_count of this CoreIndex.

        成功数

        :return: The success_count of this CoreIndex.
        :rtype: int
        """
        return self._success_count

    @success_count.setter
    def success_count(self, success_count):
        r"""Sets the success_count of this CoreIndex.

        成功数

        :param success_count: The success_count of this CoreIndex.
        :type success_count: int
        """
        self._success_count = success_count

    @property
    def success_rate(self):
        r"""Gets the success_rate of this CoreIndex.

        成功率

        :return: The success_rate of this CoreIndex.
        :rtype: int
        """
        return self._success_rate

    @success_rate.setter
    def success_rate(self, success_rate):
        r"""Sets the success_rate of this CoreIndex.

        成功率

        :param success_rate: The success_rate of this CoreIndex.
        :type success_rate: int
        """
        self._success_rate = success_rate

    @property
    def trans_tps(self):
        r"""Gets the trans_tps of this CoreIndex.

        平均TPS

        :return: The trans_tps of this CoreIndex.
        :rtype: float
        """
        return self._trans_tps

    @trans_tps.setter
    def trans_tps(self, trans_tps):
        r"""Sets the trans_tps of this CoreIndex.

        平均TPS

        :param trans_tps: The trans_tps of this CoreIndex.
        :type trans_tps: float
        """
        self._trans_tps = trans_tps

    @property
    def response_time(self):
        r"""Gets the response_time of this CoreIndex.

        :return: The response_time of this CoreIndex.
        :rtype: :class:`huaweicloudsdkcpts.v1.ResponseTimeInfo`
        """
        return self._response_time

    @response_time.setter
    def response_time(self, response_time):
        r"""Sets the response_time of this CoreIndex.

        :param response_time: The response_time of this CoreIndex.
        :type response_time: :class:`huaweicloudsdkcpts.v1.ResponseTimeInfo`
        """
        self._response_time = response_time

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
        if not isinstance(other, CoreIndex):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
