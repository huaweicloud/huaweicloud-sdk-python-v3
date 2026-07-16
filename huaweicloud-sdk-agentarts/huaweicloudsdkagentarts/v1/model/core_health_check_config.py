# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CoreHealthCheckConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enabled': 'bool',
        'port': 'int',
        'warm_up_probe': 'CoreRunWarmUpProbeConfig',
        'liveness_probe': 'CoreRunLivenessProbeConfig'
    }

    attribute_map = {
        'enabled': 'enabled',
        'port': 'port',
        'warm_up_probe': 'warm_up_probe',
        'liveness_probe': 'liveness_probe'
    }

    def __init__(self, enabled=None, port=None, warm_up_probe=None, liveness_probe=None):
        r"""CoreHealthCheckConfig

        The model defined in huaweicloud sdk

        :param enabled: **参数解释**: 是否开启自定义的预热和健康检查配置。
        :type enabled: bool
        :param port: **参数解释**: 健康检查探测的端口号。 
        :type port: int
        :param warm_up_probe: 
        :type warm_up_probe: :class:`huaweicloudsdkagentarts.v1.CoreRunWarmUpProbeConfig`
        :param liveness_probe: 
        :type liveness_probe: :class:`huaweicloudsdkagentarts.v1.CoreRunLivenessProbeConfig`
        """
        
        

        self._enabled = None
        self._port = None
        self._warm_up_probe = None
        self._liveness_probe = None
        self.discriminator = None

        if enabled is not None:
            self.enabled = enabled
        if port is not None:
            self.port = port
        if warm_up_probe is not None:
            self.warm_up_probe = warm_up_probe
        if liveness_probe is not None:
            self.liveness_probe = liveness_probe

    @property
    def enabled(self):
        r"""Gets the enabled of this CoreHealthCheckConfig.

        **参数解释**: 是否开启自定义的预热和健康检查配置。

        :return: The enabled of this CoreHealthCheckConfig.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        r"""Sets the enabled of this CoreHealthCheckConfig.

        **参数解释**: 是否开启自定义的预热和健康检查配置。

        :param enabled: The enabled of this CoreHealthCheckConfig.
        :type enabled: bool
        """
        self._enabled = enabled

    @property
    def port(self):
        r"""Gets the port of this CoreHealthCheckConfig.

        **参数解释**: 健康检查探测的端口号。 

        :return: The port of this CoreHealthCheckConfig.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        r"""Sets the port of this CoreHealthCheckConfig.

        **参数解释**: 健康检查探测的端口号。 

        :param port: The port of this CoreHealthCheckConfig.
        :type port: int
        """
        self._port = port

    @property
    def warm_up_probe(self):
        r"""Gets the warm_up_probe of this CoreHealthCheckConfig.

        :return: The warm_up_probe of this CoreHealthCheckConfig.
        :rtype: :class:`huaweicloudsdkagentarts.v1.CoreRunWarmUpProbeConfig`
        """
        return self._warm_up_probe

    @warm_up_probe.setter
    def warm_up_probe(self, warm_up_probe):
        r"""Sets the warm_up_probe of this CoreHealthCheckConfig.

        :param warm_up_probe: The warm_up_probe of this CoreHealthCheckConfig.
        :type warm_up_probe: :class:`huaweicloudsdkagentarts.v1.CoreRunWarmUpProbeConfig`
        """
        self._warm_up_probe = warm_up_probe

    @property
    def liveness_probe(self):
        r"""Gets the liveness_probe of this CoreHealthCheckConfig.

        :return: The liveness_probe of this CoreHealthCheckConfig.
        :rtype: :class:`huaweicloudsdkagentarts.v1.CoreRunLivenessProbeConfig`
        """
        return self._liveness_probe

    @liveness_probe.setter
    def liveness_probe(self, liveness_probe):
        r"""Sets the liveness_probe of this CoreHealthCheckConfig.

        :param liveness_probe: The liveness_probe of this CoreHealthCheckConfig.
        :type liveness_probe: :class:`huaweicloudsdkagentarts.v1.CoreRunLivenessProbeConfig`
        """
        self._liveness_probe = liveness_probe

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
        if not isinstance(other, CoreHealthCheckConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
