# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DebugLiveDataApiV2Response(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'test_status_code': 'str',
        'test_request': 'str',
        'test_used_time': 'int',
        'test_operator': 'str',
        'test_response': 'str',
        'test_method': 'str',
        'test_id': 'int',
        'test_date': 'datetime',
        'ld_api_id': 'str',
        'debug_log': 'list[str]'
    }

    attribute_map = {
        'test_status_code': 'test_status_code',
        'test_request': 'test_request',
        'test_used_time': 'test_used_time',
        'test_operator': 'test_operator',
        'test_response': 'test_response',
        'test_method': 'test_method',
        'test_id': 'test_id',
        'test_date': 'test_date',
        'ld_api_id': 'ld_api_id',
        'debug_log': 'debug_log'
    }

    def __init__(self, test_status_code=None, test_request=None, test_used_time=None, test_operator=None, test_response=None, test_method=None, test_id=None, test_date=None, ld_api_id=None, debug_log=None):
        r"""DebugLiveDataApiV2Response

        The model defined in huaweicloud sdk

        :param test_status_code: 测试返回的状态码
        :type test_status_code: str
        :param test_request: 测试的请求内容
        :type test_request: str
        :param test_used_time: 测试耗时
        :type test_used_time: int
        :param test_operator: 测试者的项目编号
        :type test_operator: str
        :param test_response: 测试的响应内容
        :type test_response: str
        :param test_method: 测试的请求方法
        :type test_method: str
        :param test_id: 测试编号
        :type test_id: int
        :param test_date: 测试时间
        :type test_date: datetime
        :param ld_api_id: 后端API编号
        :type ld_api_id: str
        :param debug_log: 本次测试日志列表
        :type debug_log: list[str]
        """
        
        super(DebugLiveDataApiV2Response, self).__init__()

        self._test_status_code = None
        self._test_request = None
        self._test_used_time = None
        self._test_operator = None
        self._test_response = None
        self._test_method = None
        self._test_id = None
        self._test_date = None
        self._ld_api_id = None
        self._debug_log = None
        self.discriminator = None

        if test_status_code is not None:
            self.test_status_code = test_status_code
        if test_request is not None:
            self.test_request = test_request
        if test_used_time is not None:
            self.test_used_time = test_used_time
        if test_operator is not None:
            self.test_operator = test_operator
        if test_response is not None:
            self.test_response = test_response
        if test_method is not None:
            self.test_method = test_method
        if test_id is not None:
            self.test_id = test_id
        if test_date is not None:
            self.test_date = test_date
        if ld_api_id is not None:
            self.ld_api_id = ld_api_id
        if debug_log is not None:
            self.debug_log = debug_log

    @property
    def test_status_code(self):
        r"""Gets the test_status_code of this DebugLiveDataApiV2Response.

        测试返回的状态码

        :return: The test_status_code of this DebugLiveDataApiV2Response.
        :rtype: str
        """
        return self._test_status_code

    @test_status_code.setter
    def test_status_code(self, test_status_code):
        r"""Sets the test_status_code of this DebugLiveDataApiV2Response.

        测试返回的状态码

        :param test_status_code: The test_status_code of this DebugLiveDataApiV2Response.
        :type test_status_code: str
        """
        self._test_status_code = test_status_code

    @property
    def test_request(self):
        r"""Gets the test_request of this DebugLiveDataApiV2Response.

        测试的请求内容

        :return: The test_request of this DebugLiveDataApiV2Response.
        :rtype: str
        """
        return self._test_request

    @test_request.setter
    def test_request(self, test_request):
        r"""Sets the test_request of this DebugLiveDataApiV2Response.

        测试的请求内容

        :param test_request: The test_request of this DebugLiveDataApiV2Response.
        :type test_request: str
        """
        self._test_request = test_request

    @property
    def test_used_time(self):
        r"""Gets the test_used_time of this DebugLiveDataApiV2Response.

        测试耗时

        :return: The test_used_time of this DebugLiveDataApiV2Response.
        :rtype: int
        """
        return self._test_used_time

    @test_used_time.setter
    def test_used_time(self, test_used_time):
        r"""Sets the test_used_time of this DebugLiveDataApiV2Response.

        测试耗时

        :param test_used_time: The test_used_time of this DebugLiveDataApiV2Response.
        :type test_used_time: int
        """
        self._test_used_time = test_used_time

    @property
    def test_operator(self):
        r"""Gets the test_operator of this DebugLiveDataApiV2Response.

        测试者的项目编号

        :return: The test_operator of this DebugLiveDataApiV2Response.
        :rtype: str
        """
        return self._test_operator

    @test_operator.setter
    def test_operator(self, test_operator):
        r"""Sets the test_operator of this DebugLiveDataApiV2Response.

        测试者的项目编号

        :param test_operator: The test_operator of this DebugLiveDataApiV2Response.
        :type test_operator: str
        """
        self._test_operator = test_operator

    @property
    def test_response(self):
        r"""Gets the test_response of this DebugLiveDataApiV2Response.

        测试的响应内容

        :return: The test_response of this DebugLiveDataApiV2Response.
        :rtype: str
        """
        return self._test_response

    @test_response.setter
    def test_response(self, test_response):
        r"""Sets the test_response of this DebugLiveDataApiV2Response.

        测试的响应内容

        :param test_response: The test_response of this DebugLiveDataApiV2Response.
        :type test_response: str
        """
        self._test_response = test_response

    @property
    def test_method(self):
        r"""Gets the test_method of this DebugLiveDataApiV2Response.

        测试的请求方法

        :return: The test_method of this DebugLiveDataApiV2Response.
        :rtype: str
        """
        return self._test_method

    @test_method.setter
    def test_method(self, test_method):
        r"""Sets the test_method of this DebugLiveDataApiV2Response.

        测试的请求方法

        :param test_method: The test_method of this DebugLiveDataApiV2Response.
        :type test_method: str
        """
        self._test_method = test_method

    @property
    def test_id(self):
        r"""Gets the test_id of this DebugLiveDataApiV2Response.

        测试编号

        :return: The test_id of this DebugLiveDataApiV2Response.
        :rtype: int
        """
        return self._test_id

    @test_id.setter
    def test_id(self, test_id):
        r"""Sets the test_id of this DebugLiveDataApiV2Response.

        测试编号

        :param test_id: The test_id of this DebugLiveDataApiV2Response.
        :type test_id: int
        """
        self._test_id = test_id

    @property
    def test_date(self):
        r"""Gets the test_date of this DebugLiveDataApiV2Response.

        测试时间

        :return: The test_date of this DebugLiveDataApiV2Response.
        :rtype: datetime
        """
        return self._test_date

    @test_date.setter
    def test_date(self, test_date):
        r"""Sets the test_date of this DebugLiveDataApiV2Response.

        测试时间

        :param test_date: The test_date of this DebugLiveDataApiV2Response.
        :type test_date: datetime
        """
        self._test_date = test_date

    @property
    def ld_api_id(self):
        r"""Gets the ld_api_id of this DebugLiveDataApiV2Response.

        后端API编号

        :return: The ld_api_id of this DebugLiveDataApiV2Response.
        :rtype: str
        """
        return self._ld_api_id

    @ld_api_id.setter
    def ld_api_id(self, ld_api_id):
        r"""Sets the ld_api_id of this DebugLiveDataApiV2Response.

        后端API编号

        :param ld_api_id: The ld_api_id of this DebugLiveDataApiV2Response.
        :type ld_api_id: str
        """
        self._ld_api_id = ld_api_id

    @property
    def debug_log(self):
        r"""Gets the debug_log of this DebugLiveDataApiV2Response.

        本次测试日志列表

        :return: The debug_log of this DebugLiveDataApiV2Response.
        :rtype: list[str]
        """
        return self._debug_log

    @debug_log.setter
    def debug_log(self, debug_log):
        r"""Sets the debug_log of this DebugLiveDataApiV2Response.

        本次测试日志列表

        :param debug_log: The debug_log of this DebugLiveDataApiV2Response.
        :type debug_log: list[str]
        """
        self._debug_log = debug_log

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
        if not isinstance(other, DebugLiveDataApiV2Response):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
