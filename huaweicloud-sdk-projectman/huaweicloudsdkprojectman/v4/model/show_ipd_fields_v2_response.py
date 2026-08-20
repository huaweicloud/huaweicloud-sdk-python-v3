# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowIpdFieldsV2Response(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status': 'str',
        'message': 'str',
        'result': 'list[FieldVO]'
    }

    attribute_map = {
        'status': 'status',
        'message': 'message',
        'result': 'result'
    }

    def __init__(self, status=None, message=None, result=None):
        r"""ShowIpdFieldsV2Response

        The model defined in huaweicloud sdk

        :param status: 响应状态码。标识查询工作项实例字段列表请求的处理结果。
        :type status: str
        :param message: 响应消息。请求失败时包含详细错误信息，可用于问题排查。
        :type message: str
        :param result: 字段列表结果。返回创建工作项实例时可选用的字段配置信息，包含字段ID、编码、名称、类型等属性，包含系统字段和项目自定义字段。
        :type result: list[:class:`huaweicloudsdkprojectman.v4.FieldVO`]
        """
        
        super().__init__()

        self._status = None
        self._message = None
        self._result = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if message is not None:
            self.message = message
        if result is not None:
            self.result = result

    @property
    def status(self):
        r"""Gets the status of this ShowIpdFieldsV2Response.

        响应状态码。标识查询工作项实例字段列表请求的处理结果。

        :return: The status of this ShowIpdFieldsV2Response.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ShowIpdFieldsV2Response.

        响应状态码。标识查询工作项实例字段列表请求的处理结果。

        :param status: The status of this ShowIpdFieldsV2Response.
        :type status: str
        """
        self._status = status

    @property
    def message(self):
        r"""Gets the message of this ShowIpdFieldsV2Response.

        响应消息。请求失败时包含详细错误信息，可用于问题排查。

        :return: The message of this ShowIpdFieldsV2Response.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this ShowIpdFieldsV2Response.

        响应消息。请求失败时包含详细错误信息，可用于问题排查。

        :param message: The message of this ShowIpdFieldsV2Response.
        :type message: str
        """
        self._message = message

    @property
    def result(self):
        r"""Gets the result of this ShowIpdFieldsV2Response.

        字段列表结果。返回创建工作项实例时可选用的字段配置信息，包含字段ID、编码、名称、类型等属性，包含系统字段和项目自定义字段。

        :return: The result of this ShowIpdFieldsV2Response.
        :rtype: list[:class:`huaweicloudsdkprojectman.v4.FieldVO`]
        """
        return self._result

    @result.setter
    def result(self, result):
        r"""Sets the result of this ShowIpdFieldsV2Response.

        字段列表结果。返回创建工作项实例时可选用的字段配置信息，包含字段ID、编码、名称、类型等属性，包含系统字段和项目自定义字段。

        :param result: The result of this ShowIpdFieldsV2Response.
        :type result: list[:class:`huaweicloudsdkprojectman.v4.FieldVO`]
        """
        self._result = result

    def to_dict(self):
        import warnings
        warnings.warn("ShowIpdFieldsV2Response.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, ShowIpdFieldsV2Response):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
