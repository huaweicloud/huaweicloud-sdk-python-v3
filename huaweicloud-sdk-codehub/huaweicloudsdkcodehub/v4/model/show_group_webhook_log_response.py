# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowGroupWebhookLogResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'int',
        'web_hook_id': 'int',
        'trigger': 'str',
        'url': 'str',
        'response_status': 'str',
        'execution_duration': 'float',
        'uuid': 'str',
        'created_at': 'str',
        'updated_at': 'str',
        'request_headers': 'object',
        'request_data': 'object',
        'response_headers': 'object',
        'response_body': 'object'
    }

    attribute_map = {
        'id': 'id',
        'web_hook_id': 'web_hook_id',
        'trigger': 'trigger',
        'url': 'url',
        'response_status': 'response_status',
        'execution_duration': 'execution_duration',
        'uuid': 'uuid',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'request_headers': 'request_headers',
        'request_data': 'request_data',
        'response_headers': 'response_headers',
        'response_body': 'response_body'
    }

    def __init__(self, id=None, web_hook_id=None, trigger=None, url=None, response_status=None, execution_duration=None, uuid=None, created_at=None, updated_at=None, request_headers=None, request_data=None, response_headers=None, response_body=None):
        r"""ShowGroupWebhookLogResponse

        The model defined in huaweicloud sdk

        :param id: **参数解释：** Webhook 日志id。
        :type id: int
        :param web_hook_id: **参数解释：** Webhook id。
        :type web_hook_id: int
        :param trigger: **参数解释：** 触发类型。
        :type trigger: str
        :param url: **参数解释：** 请求地址。
        :type url: str
        :param response_status: **参数解释：** 响应状态，默认是响应码，如果webhook地址未返回或者其他异常情况，则记录为internal error
        :type response_status: str
        :param execution_duration: **参数解释：** 响应耗时，单位是秒
        :type execution_duration: float
        :param uuid: **参数解释：** Webhook每次发送消息的时候，会在请求体中带上uuid字段，此处为该记录的uuid字段
        :type uuid: str
        :param created_at: **参数解释：** 创建时间。
        :type created_at: str
        :param updated_at: **参数解释：** 更新时间。
        :type updated_at: str
        :param request_headers: **参数解释：** 请求头，此处会将敏感信息如传递的token隐藏
        :type request_headers: object
        :param request_data: **参数解释：** 请求体，此处会将用户邮箱隐藏
        :type request_data: object
        :param response_headers: **参数解释：** 响应头
        :type response_headers: object
        :param response_body: **参数解释：** 响应体
        :type response_body: object
        """
        
        super(ShowGroupWebhookLogResponse, self).__init__()

        self._id = None
        self._web_hook_id = None
        self._trigger = None
        self._url = None
        self._response_status = None
        self._execution_duration = None
        self._uuid = None
        self._created_at = None
        self._updated_at = None
        self._request_headers = None
        self._request_data = None
        self._response_headers = None
        self._response_body = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if web_hook_id is not None:
            self.web_hook_id = web_hook_id
        if trigger is not None:
            self.trigger = trigger
        if url is not None:
            self.url = url
        if response_status is not None:
            self.response_status = response_status
        if execution_duration is not None:
            self.execution_duration = execution_duration
        if uuid is not None:
            self.uuid = uuid
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if request_headers is not None:
            self.request_headers = request_headers
        if request_data is not None:
            self.request_data = request_data
        if response_headers is not None:
            self.response_headers = response_headers
        if response_body is not None:
            self.response_body = response_body

    @property
    def id(self):
        r"""Gets the id of this ShowGroupWebhookLogResponse.

        **参数解释：** Webhook 日志id。

        :return: The id of this ShowGroupWebhookLogResponse.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ShowGroupWebhookLogResponse.

        **参数解释：** Webhook 日志id。

        :param id: The id of this ShowGroupWebhookLogResponse.
        :type id: int
        """
        self._id = id

    @property
    def web_hook_id(self):
        r"""Gets the web_hook_id of this ShowGroupWebhookLogResponse.

        **参数解释：** Webhook id。

        :return: The web_hook_id of this ShowGroupWebhookLogResponse.
        :rtype: int
        """
        return self._web_hook_id

    @web_hook_id.setter
    def web_hook_id(self, web_hook_id):
        r"""Sets the web_hook_id of this ShowGroupWebhookLogResponse.

        **参数解释：** Webhook id。

        :param web_hook_id: The web_hook_id of this ShowGroupWebhookLogResponse.
        :type web_hook_id: int
        """
        self._web_hook_id = web_hook_id

    @property
    def trigger(self):
        r"""Gets the trigger of this ShowGroupWebhookLogResponse.

        **参数解释：** 触发类型。

        :return: The trigger of this ShowGroupWebhookLogResponse.
        :rtype: str
        """
        return self._trigger

    @trigger.setter
    def trigger(self, trigger):
        r"""Sets the trigger of this ShowGroupWebhookLogResponse.

        **参数解释：** 触发类型。

        :param trigger: The trigger of this ShowGroupWebhookLogResponse.
        :type trigger: str
        """
        self._trigger = trigger

    @property
    def url(self):
        r"""Gets the url of this ShowGroupWebhookLogResponse.

        **参数解释：** 请求地址。

        :return: The url of this ShowGroupWebhookLogResponse.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        r"""Sets the url of this ShowGroupWebhookLogResponse.

        **参数解释：** 请求地址。

        :param url: The url of this ShowGroupWebhookLogResponse.
        :type url: str
        """
        self._url = url

    @property
    def response_status(self):
        r"""Gets the response_status of this ShowGroupWebhookLogResponse.

        **参数解释：** 响应状态，默认是响应码，如果webhook地址未返回或者其他异常情况，则记录为internal error

        :return: The response_status of this ShowGroupWebhookLogResponse.
        :rtype: str
        """
        return self._response_status

    @response_status.setter
    def response_status(self, response_status):
        r"""Sets the response_status of this ShowGroupWebhookLogResponse.

        **参数解释：** 响应状态，默认是响应码，如果webhook地址未返回或者其他异常情况，则记录为internal error

        :param response_status: The response_status of this ShowGroupWebhookLogResponse.
        :type response_status: str
        """
        self._response_status = response_status

    @property
    def execution_duration(self):
        r"""Gets the execution_duration of this ShowGroupWebhookLogResponse.

        **参数解释：** 响应耗时，单位是秒

        :return: The execution_duration of this ShowGroupWebhookLogResponse.
        :rtype: float
        """
        return self._execution_duration

    @execution_duration.setter
    def execution_duration(self, execution_duration):
        r"""Sets the execution_duration of this ShowGroupWebhookLogResponse.

        **参数解释：** 响应耗时，单位是秒

        :param execution_duration: The execution_duration of this ShowGroupWebhookLogResponse.
        :type execution_duration: float
        """
        self._execution_duration = execution_duration

    @property
    def uuid(self):
        r"""Gets the uuid of this ShowGroupWebhookLogResponse.

        **参数解释：** Webhook每次发送消息的时候，会在请求体中带上uuid字段，此处为该记录的uuid字段

        :return: The uuid of this ShowGroupWebhookLogResponse.
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        r"""Sets the uuid of this ShowGroupWebhookLogResponse.

        **参数解释：** Webhook每次发送消息的时候，会在请求体中带上uuid字段，此处为该记录的uuid字段

        :param uuid: The uuid of this ShowGroupWebhookLogResponse.
        :type uuid: str
        """
        self._uuid = uuid

    @property
    def created_at(self):
        r"""Gets the created_at of this ShowGroupWebhookLogResponse.

        **参数解释：** 创建时间。

        :return: The created_at of this ShowGroupWebhookLogResponse.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this ShowGroupWebhookLogResponse.

        **参数解释：** 创建时间。

        :param created_at: The created_at of this ShowGroupWebhookLogResponse.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this ShowGroupWebhookLogResponse.

        **参数解释：** 更新时间。

        :return: The updated_at of this ShowGroupWebhookLogResponse.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this ShowGroupWebhookLogResponse.

        **参数解释：** 更新时间。

        :param updated_at: The updated_at of this ShowGroupWebhookLogResponse.
        :type updated_at: str
        """
        self._updated_at = updated_at

    @property
    def request_headers(self):
        r"""Gets the request_headers of this ShowGroupWebhookLogResponse.

        **参数解释：** 请求头，此处会将敏感信息如传递的token隐藏

        :return: The request_headers of this ShowGroupWebhookLogResponse.
        :rtype: object
        """
        return self._request_headers

    @request_headers.setter
    def request_headers(self, request_headers):
        r"""Sets the request_headers of this ShowGroupWebhookLogResponse.

        **参数解释：** 请求头，此处会将敏感信息如传递的token隐藏

        :param request_headers: The request_headers of this ShowGroupWebhookLogResponse.
        :type request_headers: object
        """
        self._request_headers = request_headers

    @property
    def request_data(self):
        r"""Gets the request_data of this ShowGroupWebhookLogResponse.

        **参数解释：** 请求体，此处会将用户邮箱隐藏

        :return: The request_data of this ShowGroupWebhookLogResponse.
        :rtype: object
        """
        return self._request_data

    @request_data.setter
    def request_data(self, request_data):
        r"""Sets the request_data of this ShowGroupWebhookLogResponse.

        **参数解释：** 请求体，此处会将用户邮箱隐藏

        :param request_data: The request_data of this ShowGroupWebhookLogResponse.
        :type request_data: object
        """
        self._request_data = request_data

    @property
    def response_headers(self):
        r"""Gets the response_headers of this ShowGroupWebhookLogResponse.

        **参数解释：** 响应头

        :return: The response_headers of this ShowGroupWebhookLogResponse.
        :rtype: object
        """
        return self._response_headers

    @response_headers.setter
    def response_headers(self, response_headers):
        r"""Sets the response_headers of this ShowGroupWebhookLogResponse.

        **参数解释：** 响应头

        :param response_headers: The response_headers of this ShowGroupWebhookLogResponse.
        :type response_headers: object
        """
        self._response_headers = response_headers

    @property
    def response_body(self):
        r"""Gets the response_body of this ShowGroupWebhookLogResponse.

        **参数解释：** 响应体

        :return: The response_body of this ShowGroupWebhookLogResponse.
        :rtype: object
        """
        return self._response_body

    @response_body.setter
    def response_body(self, response_body):
        r"""Sets the response_body of this ShowGroupWebhookLogResponse.

        **参数解释：** 响应体

        :param response_body: The response_body of this ShowGroupWebhookLogResponse.
        :type response_body: object
        """
        self._response_body = response_body

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
        if not isinstance(other, ShowGroupWebhookLogResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
