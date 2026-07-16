# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteCoreRuntimeEndpointRequest:

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
        'endpoint_id': 'str'
    }

    attribute_map = {
        'runtime_id': 'runtime_id',
        'endpoint_id': 'endpoint_id'
    }

    def __init__(self, runtime_id=None, endpoint_id=None):
        r"""DeleteCoreRuntimeEndpointRequest

        The model defined in huaweicloud sdk

        :param runtime_id: 运行时ID，用于唯一标识一个Agent运行时实例。
        :type runtime_id: str
        :param endpoint_id: 访问方式ID，用于唯一标识一个Agent运行时访问方式实例。
        :type endpoint_id: str
        """
        
        

        self._runtime_id = None
        self._endpoint_id = None
        self.discriminator = None

        self.runtime_id = runtime_id
        self.endpoint_id = endpoint_id

    @property
    def runtime_id(self):
        r"""Gets the runtime_id of this DeleteCoreRuntimeEndpointRequest.

        运行时ID，用于唯一标识一个Agent运行时实例。

        :return: The runtime_id of this DeleteCoreRuntimeEndpointRequest.
        :rtype: str
        """
        return self._runtime_id

    @runtime_id.setter
    def runtime_id(self, runtime_id):
        r"""Sets the runtime_id of this DeleteCoreRuntimeEndpointRequest.

        运行时ID，用于唯一标识一个Agent运行时实例。

        :param runtime_id: The runtime_id of this DeleteCoreRuntimeEndpointRequest.
        :type runtime_id: str
        """
        self._runtime_id = runtime_id

    @property
    def endpoint_id(self):
        r"""Gets the endpoint_id of this DeleteCoreRuntimeEndpointRequest.

        访问方式ID，用于唯一标识一个Agent运行时访问方式实例。

        :return: The endpoint_id of this DeleteCoreRuntimeEndpointRequest.
        :rtype: str
        """
        return self._endpoint_id

    @endpoint_id.setter
    def endpoint_id(self, endpoint_id):
        r"""Sets the endpoint_id of this DeleteCoreRuntimeEndpointRequest.

        访问方式ID，用于唯一标识一个Agent运行时访问方式实例。

        :param endpoint_id: The endpoint_id of this DeleteCoreRuntimeEndpointRequest.
        :type endpoint_id: str
        """
        self._endpoint_id = endpoint_id

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
        if not isinstance(other, DeleteCoreRuntimeEndpointRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
