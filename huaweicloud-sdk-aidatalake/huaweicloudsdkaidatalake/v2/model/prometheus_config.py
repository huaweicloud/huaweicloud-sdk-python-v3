# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PrometheusConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enable': 'bool',
        'aom_prometheus_id': 'str'
    }

    attribute_map = {
        'enable': 'enable',
        'aom_prometheus_id': 'aom_prometheus_id'
    }

    def __init__(self, enable=None, aom_prometheus_id=None):
        r"""PrometheusConfig

        The model defined in huaweicloud sdk

        :param enable: **参数解释**：是否接入AOM。 **约束限制**：不涉及。 **取值范围**：   - true：接入AOM。   - false：不接入AOM。 **默认取值**：false。 
        :type enable: bool
        :param aom_prometheus_id: **参数解释**：AOM Prometheus实例ID，可通过AOM管理控制台或查询AOM Prometheus实例列表接口获取。 **约束限制**：不涉及。 **取值范围**：长度为0~256个字符，支持英文字符、数字、中划线和下划线的组合。 **默认取值**：不涉及。 
        :type aom_prometheus_id: str
        """
        
        

        self._enable = None
        self._aom_prometheus_id = None
        self.discriminator = None

        if enable is not None:
            self.enable = enable
        if aom_prometheus_id is not None:
            self.aom_prometheus_id = aom_prometheus_id

    @property
    def enable(self):
        r"""Gets the enable of this PrometheusConfig.

        **参数解释**：是否接入AOM。 **约束限制**：不涉及。 **取值范围**：   - true：接入AOM。   - false：不接入AOM。 **默认取值**：false。 

        :return: The enable of this PrometheusConfig.
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        r"""Sets the enable of this PrometheusConfig.

        **参数解释**：是否接入AOM。 **约束限制**：不涉及。 **取值范围**：   - true：接入AOM。   - false：不接入AOM。 **默认取值**：false。 

        :param enable: The enable of this PrometheusConfig.
        :type enable: bool
        """
        self._enable = enable

    @property
    def aom_prometheus_id(self):
        r"""Gets the aom_prometheus_id of this PrometheusConfig.

        **参数解释**：AOM Prometheus实例ID，可通过AOM管理控制台或查询AOM Prometheus实例列表接口获取。 **约束限制**：不涉及。 **取值范围**：长度为0~256个字符，支持英文字符、数字、中划线和下划线的组合。 **默认取值**：不涉及。 

        :return: The aom_prometheus_id of this PrometheusConfig.
        :rtype: str
        """
        return self._aom_prometheus_id

    @aom_prometheus_id.setter
    def aom_prometheus_id(self, aom_prometheus_id):
        r"""Sets the aom_prometheus_id of this PrometheusConfig.

        **参数解释**：AOM Prometheus实例ID，可通过AOM管理控制台或查询AOM Prometheus实例列表接口获取。 **约束限制**：不涉及。 **取值范围**：长度为0~256个字符，支持英文字符、数字、中划线和下划线的组合。 **默认取值**：不涉及。 

        :param aom_prometheus_id: The aom_prometheus_id of this PrometheusConfig.
        :type aom_prometheus_id: str
        """
        self._aom_prometheus_id = aom_prometheus_id

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
        if not isinstance(other, PrometheusConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
