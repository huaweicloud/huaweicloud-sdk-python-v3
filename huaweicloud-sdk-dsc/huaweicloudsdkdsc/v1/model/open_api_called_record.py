# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OpenApiCalledRecord:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'user_name': 'str',
        'user_id': 'str',
        'domain_name': 'str',
        'domain_id': 'str',
        'request_url': 'str',
        'request_method': 'str',
        'response_code': 'str',
        'fail_reason': 'str',
        'timestamp': 'int'
    }

    attribute_map = {
        'user_name': 'user_name',
        'user_id': 'user_id',
        'domain_name': 'domain_name',
        'domain_id': 'domain_id',
        'request_url': 'request_url',
        'request_method': 'request_method',
        'response_code': 'response_code',
        'fail_reason': 'fail_reason',
        'timestamp': 'timestamp'
    }

    def __init__(self, user_name=None, user_id=None, domain_name=None, domain_id=None, request_url=None, request_method=None, response_code=None, fail_reason=None, timestamp=None):
        """OpenApiCalledRecord

        The model defined in huaweicloud sdk

        :param user_name: 调用API的user_name
        :type user_name: str
        :param user_id: 调用API的user_id
        :type user_id: str
        :param domain_name: 调用API的domain_name
        :type domain_name: str
        :param domain_id: 调用API的domain_id
        :type domain_id: str
        :param request_url: 调用API的URL
        :type request_url: str
        :param request_method: http请求方法
        :type request_method: str
        :param response_code: http状态码
        :type response_code: str
        :param fail_reason: 调用API失败原因
        :type fail_reason: str
        :param timestamp: 调用API的时间（Unix timestamp），单位：毫秒
        :type timestamp: int
        """
        
        

        self._user_name = None
        self._user_id = None
        self._domain_name = None
        self._domain_id = None
        self._request_url = None
        self._request_method = None
        self._response_code = None
        self._fail_reason = None
        self._timestamp = None
        self.discriminator = None

        if user_name is not None:
            self.user_name = user_name
        if user_id is not None:
            self.user_id = user_id
        if domain_name is not None:
            self.domain_name = domain_name
        if domain_id is not None:
            self.domain_id = domain_id
        if request_url is not None:
            self.request_url = request_url
        if request_method is not None:
            self.request_method = request_method
        if response_code is not None:
            self.response_code = response_code
        if fail_reason is not None:
            self.fail_reason = fail_reason
        if timestamp is not None:
            self.timestamp = timestamp

    @property
    def user_name(self):
        """Gets the user_name of this OpenApiCalledRecord.

        调用API的user_name

        :return: The user_name of this OpenApiCalledRecord.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this OpenApiCalledRecord.

        调用API的user_name

        :param user_name: The user_name of this OpenApiCalledRecord.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def user_id(self):
        """Gets the user_id of this OpenApiCalledRecord.

        调用API的user_id

        :return: The user_id of this OpenApiCalledRecord.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this OpenApiCalledRecord.

        调用API的user_id

        :param user_id: The user_id of this OpenApiCalledRecord.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def domain_name(self):
        """Gets the domain_name of this OpenApiCalledRecord.

        调用API的domain_name

        :return: The domain_name of this OpenApiCalledRecord.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        """Sets the domain_name of this OpenApiCalledRecord.

        调用API的domain_name

        :param domain_name: The domain_name of this OpenApiCalledRecord.
        :type domain_name: str
        """
        self._domain_name = domain_name

    @property
    def domain_id(self):
        """Gets the domain_id of this OpenApiCalledRecord.

        调用API的domain_id

        :return: The domain_id of this OpenApiCalledRecord.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this OpenApiCalledRecord.

        调用API的domain_id

        :param domain_id: The domain_id of this OpenApiCalledRecord.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def request_url(self):
        """Gets the request_url of this OpenApiCalledRecord.

        调用API的URL

        :return: The request_url of this OpenApiCalledRecord.
        :rtype: str
        """
        return self._request_url

    @request_url.setter
    def request_url(self, request_url):
        """Sets the request_url of this OpenApiCalledRecord.

        调用API的URL

        :param request_url: The request_url of this OpenApiCalledRecord.
        :type request_url: str
        """
        self._request_url = request_url

    @property
    def request_method(self):
        """Gets the request_method of this OpenApiCalledRecord.

        http请求方法

        :return: The request_method of this OpenApiCalledRecord.
        :rtype: str
        """
        return self._request_method

    @request_method.setter
    def request_method(self, request_method):
        """Sets the request_method of this OpenApiCalledRecord.

        http请求方法

        :param request_method: The request_method of this OpenApiCalledRecord.
        :type request_method: str
        """
        self._request_method = request_method

    @property
    def response_code(self):
        """Gets the response_code of this OpenApiCalledRecord.

        http状态码

        :return: The response_code of this OpenApiCalledRecord.
        :rtype: str
        """
        return self._response_code

    @response_code.setter
    def response_code(self, response_code):
        """Sets the response_code of this OpenApiCalledRecord.

        http状态码

        :param response_code: The response_code of this OpenApiCalledRecord.
        :type response_code: str
        """
        self._response_code = response_code

    @property
    def fail_reason(self):
        """Gets the fail_reason of this OpenApiCalledRecord.

        调用API失败原因

        :return: The fail_reason of this OpenApiCalledRecord.
        :rtype: str
        """
        return self._fail_reason

    @fail_reason.setter
    def fail_reason(self, fail_reason):
        """Sets the fail_reason of this OpenApiCalledRecord.

        调用API失败原因

        :param fail_reason: The fail_reason of this OpenApiCalledRecord.
        :type fail_reason: str
        """
        self._fail_reason = fail_reason

    @property
    def timestamp(self):
        """Gets the timestamp of this OpenApiCalledRecord.

        调用API的时间（Unix timestamp），单位：毫秒

        :return: The timestamp of this OpenApiCalledRecord.
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this OpenApiCalledRecord.

        调用API的时间（Unix timestamp），单位：毫秒

        :param timestamp: The timestamp of this OpenApiCalledRecord.
        :type timestamp: int
        """
        self._timestamp = timestamp

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
        if not isinstance(other, OpenApiCalledRecord):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
