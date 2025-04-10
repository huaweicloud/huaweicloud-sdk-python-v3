# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RemoteAuthRuleVo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'auth_server': 'str',
        'request_method': 'str',
        'file_type_setting': 'str',
        'specified_file_type': 'str',
        'reserve_args_setting': 'str',
        'reserve_args': 'str',
        'add_custom_args_rules': 'list[CustomArgs]',
        'reserve_headers_setting': 'str',
        'add_custom_headers_rules': 'list[CustomArgs]',
        'auth_success_status': 'str',
        'auth_failed_status': 'str',
        'response_status': 'str',
        'timeout': 'int',
        'timeout_action': 'str',
        'reserve_headers': 'str'
    }

    attribute_map = {
        'auth_server': 'auth_server',
        'request_method': 'request_method',
        'file_type_setting': 'file_type_setting',
        'specified_file_type': 'specified_file_type',
        'reserve_args_setting': 'reserve_args_setting',
        'reserve_args': 'reserve_args',
        'add_custom_args_rules': 'add_custom_args_rules',
        'reserve_headers_setting': 'reserve_headers_setting',
        'add_custom_headers_rules': 'add_custom_headers_rules',
        'auth_success_status': 'auth_success_status',
        'auth_failed_status': 'auth_failed_status',
        'response_status': 'response_status',
        'timeout': 'timeout',
        'timeout_action': 'timeout_action',
        'reserve_headers': 'reserve_headers'
    }

    def __init__(self, auth_server=None, request_method=None, file_type_setting=None, specified_file_type=None, reserve_args_setting=None, reserve_args=None, add_custom_args_rules=None, reserve_headers_setting=None, add_custom_headers_rules=None, auth_success_status=None, auth_failed_status=None, response_status=None, timeout=None, timeout_action=None, reserve_headers=None):
        r"""RemoteAuthRuleVo

        The model defined in huaweicloud sdk

        :param auth_server: 可访问的鉴权服务器地址。 输入的URL必须有“http”或“https”。不能是localhost或127.0.0.1这类本地地址。 不能是CDN的加速域名。
        :type auth_server: str
        :param request_method: 鉴权服务器支持的请求方法，支持GET、POST、HEAD。
        :type request_method: str
        :param file_type_setting: all（所有文件类型）：所有文件均参与鉴权。 specific_file（指定文件类型）：指定类型的文件参与鉴权。示例：jpg|MP4。 文件类型不区分大小写，即：jpg和JPG代表同一种文件类型，多个文件类型用“|”分割。
        :type file_type_setting: str
        :param specified_file_type: 字符总数不能超过512,当file_type_setting等于specific_file时为必选，其余情况为空， 由大小写字母和数字构成，文件类型用竖线分隔，例如jpg|mp4，只有在必选情况下才会对该字段做校验。
        :type specified_file_type: str
        :param reserve_args_setting: 设置用户请求中需要参与鉴权的参数，可选reserve_all_args（保留所有URL参数）、reserve_specific_args（保留指定URL参数）、ignore_all_args（忽略所有URL参数）。
        :type reserve_args_setting: str
        :param reserve_args: 当reserve_args_setting等于reserve_specific_args时为必选，其余情况为空，要保留的参数，多个参数用竖线分隔：key1|key2。
        :type reserve_args: str
        :param add_custom_args_rules: URL鉴权参数
        :type add_custom_args_rules: list[:class:`huaweicloudsdkcdn.v1.CustomArgs`]
        :param reserve_headers_setting: 设置用户请求中参与鉴权请求头，可选reserve_all_headers（保留所有请求头参数）、reserve_specific_headers（保留指定请求头参数）、ignore_all_headers（忽略所有请求头参数）。
        :type reserve_headers_setting: str
        :param add_custom_headers_rules: 请求头鉴权参数
        :type add_custom_headers_rules: list[:class:`huaweicloudsdkcdn.v1.CustomArgs`]
        :param auth_success_status: 设置鉴权成功时远程鉴权服务器返回给CDN节点的状态码。取值范围：2xx/3xx。
        :type auth_success_status: str
        :param auth_failed_status: 设置鉴权失败时远程鉴权服务器返回给CDN节点的状态码。取值范围：4xx/5xx。
        :type auth_failed_status: str
        :param response_status: 设置鉴权失败时CDN节点返回给用户的状态码。取值范围：2xx/3xx/4xx/5xx。
        :type response_status: str
        :param timeout: 设置鉴权超时时间，即从CDN转发鉴权请求开始，到CDN节点收到远程鉴权服务器返回的结果的时间。单位为毫秒，值为0或50~3000。
        :type timeout: int
        :param timeout_action: 设置鉴权超时后，CDN节点如何处理用户请求。 pass(鉴权失败放过)：鉴权超时后允许用户请求，返回对应的资源。 forbid(鉴权失败拒绝)：鉴权超时后拒绝用户请求，返回配置的响应自定义状态码给用户。
        :type timeout_action: str
        :param reserve_headers: 当reserve_headers_setting等于reserve_specific_headers时为必选，其余情况为空，要保留的请求头，多个请求头用竖线分隔：key1|key2。
        :type reserve_headers: str
        """
        
        

        self._auth_server = None
        self._request_method = None
        self._file_type_setting = None
        self._specified_file_type = None
        self._reserve_args_setting = None
        self._reserve_args = None
        self._add_custom_args_rules = None
        self._reserve_headers_setting = None
        self._add_custom_headers_rules = None
        self._auth_success_status = None
        self._auth_failed_status = None
        self._response_status = None
        self._timeout = None
        self._timeout_action = None
        self._reserve_headers = None
        self.discriminator = None

        self.auth_server = auth_server
        self.request_method = request_method
        self.file_type_setting = file_type_setting
        if specified_file_type is not None:
            self.specified_file_type = specified_file_type
        self.reserve_args_setting = reserve_args_setting
        if reserve_args is not None:
            self.reserve_args = reserve_args
        if add_custom_args_rules is not None:
            self.add_custom_args_rules = add_custom_args_rules
        self.reserve_headers_setting = reserve_headers_setting
        if add_custom_headers_rules is not None:
            self.add_custom_headers_rules = add_custom_headers_rules
        self.auth_success_status = auth_success_status
        self.auth_failed_status = auth_failed_status
        self.response_status = response_status
        self.timeout = timeout
        self.timeout_action = timeout_action
        if reserve_headers is not None:
            self.reserve_headers = reserve_headers

    @property
    def auth_server(self):
        r"""Gets the auth_server of this RemoteAuthRuleVo.

        可访问的鉴权服务器地址。 输入的URL必须有“http”或“https”。不能是localhost或127.0.0.1这类本地地址。 不能是CDN的加速域名。

        :return: The auth_server of this RemoteAuthRuleVo.
        :rtype: str
        """
        return self._auth_server

    @auth_server.setter
    def auth_server(self, auth_server):
        r"""Sets the auth_server of this RemoteAuthRuleVo.

        可访问的鉴权服务器地址。 输入的URL必须有“http”或“https”。不能是localhost或127.0.0.1这类本地地址。 不能是CDN的加速域名。

        :param auth_server: The auth_server of this RemoteAuthRuleVo.
        :type auth_server: str
        """
        self._auth_server = auth_server

    @property
    def request_method(self):
        r"""Gets the request_method of this RemoteAuthRuleVo.

        鉴权服务器支持的请求方法，支持GET、POST、HEAD。

        :return: The request_method of this RemoteAuthRuleVo.
        :rtype: str
        """
        return self._request_method

    @request_method.setter
    def request_method(self, request_method):
        r"""Sets the request_method of this RemoteAuthRuleVo.

        鉴权服务器支持的请求方法，支持GET、POST、HEAD。

        :param request_method: The request_method of this RemoteAuthRuleVo.
        :type request_method: str
        """
        self._request_method = request_method

    @property
    def file_type_setting(self):
        r"""Gets the file_type_setting of this RemoteAuthRuleVo.

        all（所有文件类型）：所有文件均参与鉴权。 specific_file（指定文件类型）：指定类型的文件参与鉴权。示例：jpg|MP4。 文件类型不区分大小写，即：jpg和JPG代表同一种文件类型，多个文件类型用“|”分割。

        :return: The file_type_setting of this RemoteAuthRuleVo.
        :rtype: str
        """
        return self._file_type_setting

    @file_type_setting.setter
    def file_type_setting(self, file_type_setting):
        r"""Sets the file_type_setting of this RemoteAuthRuleVo.

        all（所有文件类型）：所有文件均参与鉴权。 specific_file（指定文件类型）：指定类型的文件参与鉴权。示例：jpg|MP4。 文件类型不区分大小写，即：jpg和JPG代表同一种文件类型，多个文件类型用“|”分割。

        :param file_type_setting: The file_type_setting of this RemoteAuthRuleVo.
        :type file_type_setting: str
        """
        self._file_type_setting = file_type_setting

    @property
    def specified_file_type(self):
        r"""Gets the specified_file_type of this RemoteAuthRuleVo.

        字符总数不能超过512,当file_type_setting等于specific_file时为必选，其余情况为空， 由大小写字母和数字构成，文件类型用竖线分隔，例如jpg|mp4，只有在必选情况下才会对该字段做校验。

        :return: The specified_file_type of this RemoteAuthRuleVo.
        :rtype: str
        """
        return self._specified_file_type

    @specified_file_type.setter
    def specified_file_type(self, specified_file_type):
        r"""Sets the specified_file_type of this RemoteAuthRuleVo.

        字符总数不能超过512,当file_type_setting等于specific_file时为必选，其余情况为空， 由大小写字母和数字构成，文件类型用竖线分隔，例如jpg|mp4，只有在必选情况下才会对该字段做校验。

        :param specified_file_type: The specified_file_type of this RemoteAuthRuleVo.
        :type specified_file_type: str
        """
        self._specified_file_type = specified_file_type

    @property
    def reserve_args_setting(self):
        r"""Gets the reserve_args_setting of this RemoteAuthRuleVo.

        设置用户请求中需要参与鉴权的参数，可选reserve_all_args（保留所有URL参数）、reserve_specific_args（保留指定URL参数）、ignore_all_args（忽略所有URL参数）。

        :return: The reserve_args_setting of this RemoteAuthRuleVo.
        :rtype: str
        """
        return self._reserve_args_setting

    @reserve_args_setting.setter
    def reserve_args_setting(self, reserve_args_setting):
        r"""Sets the reserve_args_setting of this RemoteAuthRuleVo.

        设置用户请求中需要参与鉴权的参数，可选reserve_all_args（保留所有URL参数）、reserve_specific_args（保留指定URL参数）、ignore_all_args（忽略所有URL参数）。

        :param reserve_args_setting: The reserve_args_setting of this RemoteAuthRuleVo.
        :type reserve_args_setting: str
        """
        self._reserve_args_setting = reserve_args_setting

    @property
    def reserve_args(self):
        r"""Gets the reserve_args of this RemoteAuthRuleVo.

        当reserve_args_setting等于reserve_specific_args时为必选，其余情况为空，要保留的参数，多个参数用竖线分隔：key1|key2。

        :return: The reserve_args of this RemoteAuthRuleVo.
        :rtype: str
        """
        return self._reserve_args

    @reserve_args.setter
    def reserve_args(self, reserve_args):
        r"""Sets the reserve_args of this RemoteAuthRuleVo.

        当reserve_args_setting等于reserve_specific_args时为必选，其余情况为空，要保留的参数，多个参数用竖线分隔：key1|key2。

        :param reserve_args: The reserve_args of this RemoteAuthRuleVo.
        :type reserve_args: str
        """
        self._reserve_args = reserve_args

    @property
    def add_custom_args_rules(self):
        r"""Gets the add_custom_args_rules of this RemoteAuthRuleVo.

        URL鉴权参数

        :return: The add_custom_args_rules of this RemoteAuthRuleVo.
        :rtype: list[:class:`huaweicloudsdkcdn.v1.CustomArgs`]
        """
        return self._add_custom_args_rules

    @add_custom_args_rules.setter
    def add_custom_args_rules(self, add_custom_args_rules):
        r"""Sets the add_custom_args_rules of this RemoteAuthRuleVo.

        URL鉴权参数

        :param add_custom_args_rules: The add_custom_args_rules of this RemoteAuthRuleVo.
        :type add_custom_args_rules: list[:class:`huaweicloudsdkcdn.v1.CustomArgs`]
        """
        self._add_custom_args_rules = add_custom_args_rules

    @property
    def reserve_headers_setting(self):
        r"""Gets the reserve_headers_setting of this RemoteAuthRuleVo.

        设置用户请求中参与鉴权请求头，可选reserve_all_headers（保留所有请求头参数）、reserve_specific_headers（保留指定请求头参数）、ignore_all_headers（忽略所有请求头参数）。

        :return: The reserve_headers_setting of this RemoteAuthRuleVo.
        :rtype: str
        """
        return self._reserve_headers_setting

    @reserve_headers_setting.setter
    def reserve_headers_setting(self, reserve_headers_setting):
        r"""Sets the reserve_headers_setting of this RemoteAuthRuleVo.

        设置用户请求中参与鉴权请求头，可选reserve_all_headers（保留所有请求头参数）、reserve_specific_headers（保留指定请求头参数）、ignore_all_headers（忽略所有请求头参数）。

        :param reserve_headers_setting: The reserve_headers_setting of this RemoteAuthRuleVo.
        :type reserve_headers_setting: str
        """
        self._reserve_headers_setting = reserve_headers_setting

    @property
    def add_custom_headers_rules(self):
        r"""Gets the add_custom_headers_rules of this RemoteAuthRuleVo.

        请求头鉴权参数

        :return: The add_custom_headers_rules of this RemoteAuthRuleVo.
        :rtype: list[:class:`huaweicloudsdkcdn.v1.CustomArgs`]
        """
        return self._add_custom_headers_rules

    @add_custom_headers_rules.setter
    def add_custom_headers_rules(self, add_custom_headers_rules):
        r"""Sets the add_custom_headers_rules of this RemoteAuthRuleVo.

        请求头鉴权参数

        :param add_custom_headers_rules: The add_custom_headers_rules of this RemoteAuthRuleVo.
        :type add_custom_headers_rules: list[:class:`huaweicloudsdkcdn.v1.CustomArgs`]
        """
        self._add_custom_headers_rules = add_custom_headers_rules

    @property
    def auth_success_status(self):
        r"""Gets the auth_success_status of this RemoteAuthRuleVo.

        设置鉴权成功时远程鉴权服务器返回给CDN节点的状态码。取值范围：2xx/3xx。

        :return: The auth_success_status of this RemoteAuthRuleVo.
        :rtype: str
        """
        return self._auth_success_status

    @auth_success_status.setter
    def auth_success_status(self, auth_success_status):
        r"""Sets the auth_success_status of this RemoteAuthRuleVo.

        设置鉴权成功时远程鉴权服务器返回给CDN节点的状态码。取值范围：2xx/3xx。

        :param auth_success_status: The auth_success_status of this RemoteAuthRuleVo.
        :type auth_success_status: str
        """
        self._auth_success_status = auth_success_status

    @property
    def auth_failed_status(self):
        r"""Gets the auth_failed_status of this RemoteAuthRuleVo.

        设置鉴权失败时远程鉴权服务器返回给CDN节点的状态码。取值范围：4xx/5xx。

        :return: The auth_failed_status of this RemoteAuthRuleVo.
        :rtype: str
        """
        return self._auth_failed_status

    @auth_failed_status.setter
    def auth_failed_status(self, auth_failed_status):
        r"""Sets the auth_failed_status of this RemoteAuthRuleVo.

        设置鉴权失败时远程鉴权服务器返回给CDN节点的状态码。取值范围：4xx/5xx。

        :param auth_failed_status: The auth_failed_status of this RemoteAuthRuleVo.
        :type auth_failed_status: str
        """
        self._auth_failed_status = auth_failed_status

    @property
    def response_status(self):
        r"""Gets the response_status of this RemoteAuthRuleVo.

        设置鉴权失败时CDN节点返回给用户的状态码。取值范围：2xx/3xx/4xx/5xx。

        :return: The response_status of this RemoteAuthRuleVo.
        :rtype: str
        """
        return self._response_status

    @response_status.setter
    def response_status(self, response_status):
        r"""Sets the response_status of this RemoteAuthRuleVo.

        设置鉴权失败时CDN节点返回给用户的状态码。取值范围：2xx/3xx/4xx/5xx。

        :param response_status: The response_status of this RemoteAuthRuleVo.
        :type response_status: str
        """
        self._response_status = response_status

    @property
    def timeout(self):
        r"""Gets the timeout of this RemoteAuthRuleVo.

        设置鉴权超时时间，即从CDN转发鉴权请求开始，到CDN节点收到远程鉴权服务器返回的结果的时间。单位为毫秒，值为0或50~3000。

        :return: The timeout of this RemoteAuthRuleVo.
        :rtype: int
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        r"""Sets the timeout of this RemoteAuthRuleVo.

        设置鉴权超时时间，即从CDN转发鉴权请求开始，到CDN节点收到远程鉴权服务器返回的结果的时间。单位为毫秒，值为0或50~3000。

        :param timeout: The timeout of this RemoteAuthRuleVo.
        :type timeout: int
        """
        self._timeout = timeout

    @property
    def timeout_action(self):
        r"""Gets the timeout_action of this RemoteAuthRuleVo.

        设置鉴权超时后，CDN节点如何处理用户请求。 pass(鉴权失败放过)：鉴权超时后允许用户请求，返回对应的资源。 forbid(鉴权失败拒绝)：鉴权超时后拒绝用户请求，返回配置的响应自定义状态码给用户。

        :return: The timeout_action of this RemoteAuthRuleVo.
        :rtype: str
        """
        return self._timeout_action

    @timeout_action.setter
    def timeout_action(self, timeout_action):
        r"""Sets the timeout_action of this RemoteAuthRuleVo.

        设置鉴权超时后，CDN节点如何处理用户请求。 pass(鉴权失败放过)：鉴权超时后允许用户请求，返回对应的资源。 forbid(鉴权失败拒绝)：鉴权超时后拒绝用户请求，返回配置的响应自定义状态码给用户。

        :param timeout_action: The timeout_action of this RemoteAuthRuleVo.
        :type timeout_action: str
        """
        self._timeout_action = timeout_action

    @property
    def reserve_headers(self):
        r"""Gets the reserve_headers of this RemoteAuthRuleVo.

        当reserve_headers_setting等于reserve_specific_headers时为必选，其余情况为空，要保留的请求头，多个请求头用竖线分隔：key1|key2。

        :return: The reserve_headers of this RemoteAuthRuleVo.
        :rtype: str
        """
        return self._reserve_headers

    @reserve_headers.setter
    def reserve_headers(self, reserve_headers):
        r"""Sets the reserve_headers of this RemoteAuthRuleVo.

        当reserve_headers_setting等于reserve_specific_headers时为必选，其余情况为空，要保留的请求头，多个请求头用竖线分隔：key1|key2。

        :param reserve_headers: The reserve_headers of this RemoteAuthRuleVo.
        :type reserve_headers: str
        """
        self._reserve_headers = reserve_headers

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
        if not isinstance(other, RemoteAuthRuleVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
