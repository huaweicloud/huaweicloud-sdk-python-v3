# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ServerlessScalingPolicy:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enlarge_step_size': 'str',
        'custom_scaling_config': 'CustomScalingConfig'
    }

    attribute_map = {
        'enlarge_step_size': 'enlarge_step_size',
        'custom_scaling_config': 'custom_scaling_config'
    }

    def __init__(self, enlarge_step_size=None, custom_scaling_config=None):
        r"""ServerlessScalingPolicy

        The model defined in huaweicloud sdk

        :param enlarge_step_size: **参数描述**：  自定义扩容步长。  **约束限制**：  不涉及。  **取值范围**：  2-算力上限的一半。  **默认取值**：  不涉及。
        :type enlarge_step_size: str
        :param custom_scaling_config: 
        :type custom_scaling_config: :class:`huaweicloudsdkgaussdb.v3.CustomScalingConfig`
        """
        
        

        self._enlarge_step_size = None
        self._custom_scaling_config = None
        self.discriminator = None

        if enlarge_step_size is not None:
            self.enlarge_step_size = enlarge_step_size
        if custom_scaling_config is not None:
            self.custom_scaling_config = custom_scaling_config

    @property
    def enlarge_step_size(self):
        r"""Gets the enlarge_step_size of this ServerlessScalingPolicy.

        **参数描述**：  自定义扩容步长。  **约束限制**：  不涉及。  **取值范围**：  2-算力上限的一半。  **默认取值**：  不涉及。

        :return: The enlarge_step_size of this ServerlessScalingPolicy.
        :rtype: str
        """
        return self._enlarge_step_size

    @enlarge_step_size.setter
    def enlarge_step_size(self, enlarge_step_size):
        r"""Sets the enlarge_step_size of this ServerlessScalingPolicy.

        **参数描述**：  自定义扩容步长。  **约束限制**：  不涉及。  **取值范围**：  2-算力上限的一半。  **默认取值**：  不涉及。

        :param enlarge_step_size: The enlarge_step_size of this ServerlessScalingPolicy.
        :type enlarge_step_size: str
        """
        self._enlarge_step_size = enlarge_step_size

    @property
    def custom_scaling_config(self):
        r"""Gets the custom_scaling_config of this ServerlessScalingPolicy.

        :return: The custom_scaling_config of this ServerlessScalingPolicy.
        :rtype: :class:`huaweicloudsdkgaussdb.v3.CustomScalingConfig`
        """
        return self._custom_scaling_config

    @custom_scaling_config.setter
    def custom_scaling_config(self, custom_scaling_config):
        r"""Sets the custom_scaling_config of this ServerlessScalingPolicy.

        :param custom_scaling_config: The custom_scaling_config of this ServerlessScalingPolicy.
        :type custom_scaling_config: :class:`huaweicloudsdkgaussdb.v3.CustomScalingConfig`
        """
        self._custom_scaling_config = custom_scaling_config

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
        if not isinstance(other, ServerlessScalingPolicy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
