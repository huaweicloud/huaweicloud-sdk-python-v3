# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateServerlessScaleToZeroPolicy:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'scale_to_zero': 'bool',
        'idle_duration_seconds': 'int'
    }

    attribute_map = {
        'scale_to_zero': 'scale_to_zero',
        'idle_duration_seconds': 'idle_duration_seconds'
    }

    def __init__(self, scale_to_zero=None, idle_duration_seconds=None):
        r"""UpdateServerlessScaleToZeroPolicy

        The model defined in huaweicloud sdk

        :param scale_to_zero: **参数解释**：  是否开启Scale to Zero自动启停。  **约束限制**：  仅Serverless实例支持。  **取值范围**：  - true：开启。实例空闲达idle_duration_seconds阈值时算力自动缩容到零（停止VM计费），有新连接时自动唤醒恢复。 - false：关闭。实例正常计费。  **默认取值**：  false。
        :type scale_to_zero: bool
        :param idle_duration_seconds: **参数解释**：  触发缩容到零的空闲检测时长（秒）。实例所有节点无活跃用户连接达到该时长后，自动缩容到零。  **约束限制**：  - 当scale_to_zero为true时，该参数必填。 - 当scale_to_zero为false时，该参数可不传。  **取值范围**：  300～3600。  **默认取值**：  不涉及。
        :type idle_duration_seconds: int
        """
        
        

        self._scale_to_zero = None
        self._idle_duration_seconds = None
        self.discriminator = None

        self.scale_to_zero = scale_to_zero
        if idle_duration_seconds is not None:
            self.idle_duration_seconds = idle_duration_seconds

    @property
    def scale_to_zero(self):
        r"""Gets the scale_to_zero of this UpdateServerlessScaleToZeroPolicy.

        **参数解释**：  是否开启Scale to Zero自动启停。  **约束限制**：  仅Serverless实例支持。  **取值范围**：  - true：开启。实例空闲达idle_duration_seconds阈值时算力自动缩容到零（停止VM计费），有新连接时自动唤醒恢复。 - false：关闭。实例正常计费。  **默认取值**：  false。

        :return: The scale_to_zero of this UpdateServerlessScaleToZeroPolicy.
        :rtype: bool
        """
        return self._scale_to_zero

    @scale_to_zero.setter
    def scale_to_zero(self, scale_to_zero):
        r"""Sets the scale_to_zero of this UpdateServerlessScaleToZeroPolicy.

        **参数解释**：  是否开启Scale to Zero自动启停。  **约束限制**：  仅Serverless实例支持。  **取值范围**：  - true：开启。实例空闲达idle_duration_seconds阈值时算力自动缩容到零（停止VM计费），有新连接时自动唤醒恢复。 - false：关闭。实例正常计费。  **默认取值**：  false。

        :param scale_to_zero: The scale_to_zero of this UpdateServerlessScaleToZeroPolicy.
        :type scale_to_zero: bool
        """
        self._scale_to_zero = scale_to_zero

    @property
    def idle_duration_seconds(self):
        r"""Gets the idle_duration_seconds of this UpdateServerlessScaleToZeroPolicy.

        **参数解释**：  触发缩容到零的空闲检测时长（秒）。实例所有节点无活跃用户连接达到该时长后，自动缩容到零。  **约束限制**：  - 当scale_to_zero为true时，该参数必填。 - 当scale_to_zero为false时，该参数可不传。  **取值范围**：  300～3600。  **默认取值**：  不涉及。

        :return: The idle_duration_seconds of this UpdateServerlessScaleToZeroPolicy.
        :rtype: int
        """
        return self._idle_duration_seconds

    @idle_duration_seconds.setter
    def idle_duration_seconds(self, idle_duration_seconds):
        r"""Sets the idle_duration_seconds of this UpdateServerlessScaleToZeroPolicy.

        **参数解释**：  触发缩容到零的空闲检测时长（秒）。实例所有节点无活跃用户连接达到该时长后，自动缩容到零。  **约束限制**：  - 当scale_to_zero为true时，该参数必填。 - 当scale_to_zero为false时，该参数可不传。  **取值范围**：  300～3600。  **默认取值**：  不涉及。

        :param idle_duration_seconds: The idle_duration_seconds of this UpdateServerlessScaleToZeroPolicy.
        :type idle_duration_seconds: int
        """
        self._idle_duration_seconds = idle_duration_seconds

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
        if not isinstance(other, UpdateServerlessScaleToZeroPolicy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
