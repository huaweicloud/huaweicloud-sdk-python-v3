# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ApiConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enable_independent_api': 'bool',
        'backend_timeout': 'int'
    }

    attribute_map = {
        'enable_independent_api': 'enable_independent_api',
        'backend_timeout': 'backend_timeout'
    }

    def __init__(self, enable_independent_api=None, backend_timeout=None):
        r"""ApiConfig

        The model defined in huaweicloud sdk

        :param enable_independent_api: - **参数解释**：是否开启Ray Service独立Api功能。 - **约束限制**：不涉及。 - **取值范围**：开启true，关闭false。 - **默认取值**：false。 
        :type enable_independent_api: bool
        :param backend_timeout: - **参数解释**：Ray Service独立Api设置的接口超时时间。 - **约束限制**：不涉及。 - **取值范围**：[0,600000]。 - **默认取值**：60000。
        :type backend_timeout: int
        """
        
        

        self._enable_independent_api = None
        self._backend_timeout = None
        self.discriminator = None

        if enable_independent_api is not None:
            self.enable_independent_api = enable_independent_api
        if backend_timeout is not None:
            self.backend_timeout = backend_timeout

    @property
    def enable_independent_api(self):
        r"""Gets the enable_independent_api of this ApiConfig.

        - **参数解释**：是否开启Ray Service独立Api功能。 - **约束限制**：不涉及。 - **取值范围**：开启true，关闭false。 - **默认取值**：false。 

        :return: The enable_independent_api of this ApiConfig.
        :rtype: bool
        """
        return self._enable_independent_api

    @enable_independent_api.setter
    def enable_independent_api(self, enable_independent_api):
        r"""Sets the enable_independent_api of this ApiConfig.

        - **参数解释**：是否开启Ray Service独立Api功能。 - **约束限制**：不涉及。 - **取值范围**：开启true，关闭false。 - **默认取值**：false。 

        :param enable_independent_api: The enable_independent_api of this ApiConfig.
        :type enable_independent_api: bool
        """
        self._enable_independent_api = enable_independent_api

    @property
    def backend_timeout(self):
        r"""Gets the backend_timeout of this ApiConfig.

        - **参数解释**：Ray Service独立Api设置的接口超时时间。 - **约束限制**：不涉及。 - **取值范围**：[0,600000]。 - **默认取值**：60000。

        :return: The backend_timeout of this ApiConfig.
        :rtype: int
        """
        return self._backend_timeout

    @backend_timeout.setter
    def backend_timeout(self, backend_timeout):
        r"""Sets the backend_timeout of this ApiConfig.

        - **参数解释**：Ray Service独立Api设置的接口超时时间。 - **约束限制**：不涉及。 - **取值范围**：[0,600000]。 - **默认取值**：60000。

        :param backend_timeout: The backend_timeout of this ApiConfig.
        :type backend_timeout: int
        """
        self._backend_timeout = backend_timeout

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
        if not isinstance(other, ApiConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
