# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CoreGatewayTargetInferenceConfiguration:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'endpoint': 'str',
        'operations': 'list[CoreGatewayTargetInferenceConfigurationOperations]',
        'model_mapping': 'CoreGatewayTargetInferenceConfigurationModelMapping'
    }

    attribute_map = {
        'endpoint': 'endpoint',
        'operations': 'operations',
        'model_mapping': 'model_mapping'
    }

    def __init__(self, endpoint=None, operations=None, model_mapping=None):
        r"""CoreGatewayTargetInferenceConfiguration

        The model defined in huaweicloud sdk

        :param endpoint: 推理提供者的HTTPS端点。
        :type endpoint: str
        :param operations: 推理操作配置列表。
        :type operations: list[:class:`huaweicloudsdkagentarts.v1.CoreGatewayTargetInferenceConfigurationOperations`]
        :param model_mapping: 
        :type model_mapping: :class:`huaweicloudsdkagentarts.v1.CoreGatewayTargetInferenceConfigurationModelMapping`
        """
        
        

        self._endpoint = None
        self._operations = None
        self._model_mapping = None
        self.discriminator = None

        if endpoint is not None:
            self.endpoint = endpoint
        if operations is not None:
            self.operations = operations
        if model_mapping is not None:
            self.model_mapping = model_mapping

    @property
    def endpoint(self):
        r"""Gets the endpoint of this CoreGatewayTargetInferenceConfiguration.

        推理提供者的HTTPS端点。

        :return: The endpoint of this CoreGatewayTargetInferenceConfiguration.
        :rtype: str
        """
        return self._endpoint

    @endpoint.setter
    def endpoint(self, endpoint):
        r"""Sets the endpoint of this CoreGatewayTargetInferenceConfiguration.

        推理提供者的HTTPS端点。

        :param endpoint: The endpoint of this CoreGatewayTargetInferenceConfiguration.
        :type endpoint: str
        """
        self._endpoint = endpoint

    @property
    def operations(self):
        r"""Gets the operations of this CoreGatewayTargetInferenceConfiguration.

        推理操作配置列表。

        :return: The operations of this CoreGatewayTargetInferenceConfiguration.
        :rtype: list[:class:`huaweicloudsdkagentarts.v1.CoreGatewayTargetInferenceConfigurationOperations`]
        """
        return self._operations

    @operations.setter
    def operations(self, operations):
        r"""Sets the operations of this CoreGatewayTargetInferenceConfiguration.

        推理操作配置列表。

        :param operations: The operations of this CoreGatewayTargetInferenceConfiguration.
        :type operations: list[:class:`huaweicloudsdkagentarts.v1.CoreGatewayTargetInferenceConfigurationOperations`]
        """
        self._operations = operations

    @property
    def model_mapping(self):
        r"""Gets the model_mapping of this CoreGatewayTargetInferenceConfiguration.

        :return: The model_mapping of this CoreGatewayTargetInferenceConfiguration.
        :rtype: :class:`huaweicloudsdkagentarts.v1.CoreGatewayTargetInferenceConfigurationModelMapping`
        """
        return self._model_mapping

    @model_mapping.setter
    def model_mapping(self, model_mapping):
        r"""Sets the model_mapping of this CoreGatewayTargetInferenceConfiguration.

        :param model_mapping: The model_mapping of this CoreGatewayTargetInferenceConfiguration.
        :type model_mapping: :class:`huaweicloudsdkagentarts.v1.CoreGatewayTargetInferenceConfigurationModelMapping`
        """
        self._model_mapping = model_mapping

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
        if not isinstance(other, CoreGatewayTargetInferenceConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
