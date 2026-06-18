# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowRepositoryNavigationSchemaResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'result': 'str',
        'message': 'str',
        'schema': 'SchemaDto'
    }

    attribute_map = {
        'result': 'result',
        'message': 'message',
        'schema': 'schema'
    }

    def __init__(self, result=None, message=None, schema=None):
        r"""ShowRepositoryNavigationSchemaResponse

        The model defined in huaweicloud sdk

        :param result: **参数解释：** 结果标识。 **约束限制：** 不涉及。
        :type result: str
        :param message: **参数解释：** 结果消息。 **约束限制：** 不涉及。
        :type message: str
        :param schema: 
        :type schema: :class:`huaweicloudsdkcodeartsrepo.v4.SchemaDto`
        """
        
        super().__init__()

        self._result = None
        self._message = None
        self._schema = None
        self.discriminator = None

        if result is not None:
            self.result = result
        if message is not None:
            self.message = message
        if schema is not None:
            self.schema = schema

    @property
    def result(self):
        r"""Gets the result of this ShowRepositoryNavigationSchemaResponse.

        **参数解释：** 结果标识。 **约束限制：** 不涉及。

        :return: The result of this ShowRepositoryNavigationSchemaResponse.
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result):
        r"""Sets the result of this ShowRepositoryNavigationSchemaResponse.

        **参数解释：** 结果标识。 **约束限制：** 不涉及。

        :param result: The result of this ShowRepositoryNavigationSchemaResponse.
        :type result: str
        """
        self._result = result

    @property
    def message(self):
        r"""Gets the message of this ShowRepositoryNavigationSchemaResponse.

        **参数解释：** 结果消息。 **约束限制：** 不涉及。

        :return: The message of this ShowRepositoryNavigationSchemaResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this ShowRepositoryNavigationSchemaResponse.

        **参数解释：** 结果消息。 **约束限制：** 不涉及。

        :param message: The message of this ShowRepositoryNavigationSchemaResponse.
        :type message: str
        """
        self._message = message

    @property
    def schema(self):
        r"""Gets the schema of this ShowRepositoryNavigationSchemaResponse.

        :return: The schema of this ShowRepositoryNavigationSchemaResponse.
        :rtype: :class:`huaweicloudsdkcodeartsrepo.v4.SchemaDto`
        """
        return self._schema

    @schema.setter
    def schema(self, schema):
        r"""Sets the schema of this ShowRepositoryNavigationSchemaResponse.

        :param schema: The schema of this ShowRepositoryNavigationSchemaResponse.
        :type schema: :class:`huaweicloudsdkcodeartsrepo.v4.SchemaDto`
        """
        self._schema = schema

    def to_dict(self):
        import warnings
        warnings.warn("ShowRepositoryNavigationSchemaResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowRepositoryNavigationSchemaResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
