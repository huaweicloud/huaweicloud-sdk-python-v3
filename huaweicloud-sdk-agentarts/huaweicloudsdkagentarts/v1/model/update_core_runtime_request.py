# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateCoreRuntimeRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'runtime_id': 'str',
        'body': 'UpdateCoreRuntimeRequestBody'
    }

    attribute_map = {
        'runtime_id': 'runtime_id',
        'body': 'body'
    }

    def __init__(self, runtime_id=None, body=None):
        r"""UpdateCoreRuntimeRequest

        The model defined in huaweicloud sdk

        :param runtime_id: 运行时ID，用于唯一标识一个Agent运行时实例。
        :type runtime_id: str
        :param body: Body of the UpdateCoreRuntimeRequest
        :type body: :class:`huaweicloudsdkagentarts.v1.UpdateCoreRuntimeRequestBody`
        """
        
        

        self._runtime_id = None
        self._body = None
        self.discriminator = None

        self.runtime_id = runtime_id
        if body is not None:
            self.body = body

    @property
    def runtime_id(self):
        r"""Gets the runtime_id of this UpdateCoreRuntimeRequest.

        运行时ID，用于唯一标识一个Agent运行时实例。

        :return: The runtime_id of this UpdateCoreRuntimeRequest.
        :rtype: str
        """
        return self._runtime_id

    @runtime_id.setter
    def runtime_id(self, runtime_id):
        r"""Sets the runtime_id of this UpdateCoreRuntimeRequest.

        运行时ID，用于唯一标识一个Agent运行时实例。

        :param runtime_id: The runtime_id of this UpdateCoreRuntimeRequest.
        :type runtime_id: str
        """
        self._runtime_id = runtime_id

    @property
    def body(self):
        r"""Gets the body of this UpdateCoreRuntimeRequest.

        :return: The body of this UpdateCoreRuntimeRequest.
        :rtype: :class:`huaweicloudsdkagentarts.v1.UpdateCoreRuntimeRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this UpdateCoreRuntimeRequest.

        :param body: The body of this UpdateCoreRuntimeRequest.
        :type body: :class:`huaweicloudsdkagentarts.v1.UpdateCoreRuntimeRequestBody`
        """
        self._body = body

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
        if not isinstance(other, UpdateCoreRuntimeRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
