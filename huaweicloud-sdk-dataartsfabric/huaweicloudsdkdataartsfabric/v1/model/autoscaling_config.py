# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AutoscalingConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'target_ongoing_requests': 'int',
        'min_replicas': 'int',
        'max_replicas': 'int',
        'initial_replicas': 'int',
        'upscale_delay_s': 'int',
        'downscale_delay_s': 'int'
    }

    attribute_map = {
        'target_ongoing_requests': 'target_ongoing_requests',
        'min_replicas': 'min_replicas',
        'max_replicas': 'max_replicas',
        'initial_replicas': 'initial_replicas',
        'upscale_delay_s': 'upscale_delay_s',
        'downscale_delay_s': 'downscale_delay_s'
    }

    def __init__(self, target_ongoing_requests=None, min_replicas=None, max_replicas=None, initial_replicas=None, upscale_delay_s=None, downscale_delay_s=None):
        r"""AutoscalingConfig

        The model defined in huaweicloud sdk

        :param target_ongoing_requests: **参数解释**：每个副本单位时间能提供的平均请求数。 **约束限制**：不涉及。 **取值范围**：[1,1000]。 **默认取值**：不涉及。
        :type target_ongoing_requests: int
        :param min_replicas: **参数解释**：最小副本数。 **约束限制**：不涉及。 **取值范围**：[0,1000]。 **默认取值**：不涉及。
        :type min_replicas: int
        :param max_replicas: **参数解释**：最大副本数。 **约束限制**：不涉及。 **取值范围**：[0,1000]。 **默认取值**：不涉及。
        :type max_replicas: int
        :param initial_replicas: **参数解释**：初始副本数。 **约束限制**：不涉及。 **取值范围**：[0,1000]。 **默认取值**：不涉及。
        :type initial_replicas: int
        :param upscale_delay_s: **参数解释**：扩容之前的等待时间。 **约束限制**：不涉及。 **取值范围**：[0,86400]。 **默认取值**：不涉及。
        :type upscale_delay_s: int
        :param downscale_delay_s: **参数解释**：缩容之前的等待时间。 **约束限制**：不涉及。 **取值范围**：[0,86400]。 **默认取值**：不涉及。
        :type downscale_delay_s: int
        """
        
        

        self._target_ongoing_requests = None
        self._min_replicas = None
        self._max_replicas = None
        self._initial_replicas = None
        self._upscale_delay_s = None
        self._downscale_delay_s = None
        self.discriminator = None

        if target_ongoing_requests is not None:
            self.target_ongoing_requests = target_ongoing_requests
        if min_replicas is not None:
            self.min_replicas = min_replicas
        if max_replicas is not None:
            self.max_replicas = max_replicas
        if initial_replicas is not None:
            self.initial_replicas = initial_replicas
        if upscale_delay_s is not None:
            self.upscale_delay_s = upscale_delay_s
        if downscale_delay_s is not None:
            self.downscale_delay_s = downscale_delay_s

    @property
    def target_ongoing_requests(self):
        r"""Gets the target_ongoing_requests of this AutoscalingConfig.

        **参数解释**：每个副本单位时间能提供的平均请求数。 **约束限制**：不涉及。 **取值范围**：[1,1000]。 **默认取值**：不涉及。

        :return: The target_ongoing_requests of this AutoscalingConfig.
        :rtype: int
        """
        return self._target_ongoing_requests

    @target_ongoing_requests.setter
    def target_ongoing_requests(self, target_ongoing_requests):
        r"""Sets the target_ongoing_requests of this AutoscalingConfig.

        **参数解释**：每个副本单位时间能提供的平均请求数。 **约束限制**：不涉及。 **取值范围**：[1,1000]。 **默认取值**：不涉及。

        :param target_ongoing_requests: The target_ongoing_requests of this AutoscalingConfig.
        :type target_ongoing_requests: int
        """
        self._target_ongoing_requests = target_ongoing_requests

    @property
    def min_replicas(self):
        r"""Gets the min_replicas of this AutoscalingConfig.

        **参数解释**：最小副本数。 **约束限制**：不涉及。 **取值范围**：[0,1000]。 **默认取值**：不涉及。

        :return: The min_replicas of this AutoscalingConfig.
        :rtype: int
        """
        return self._min_replicas

    @min_replicas.setter
    def min_replicas(self, min_replicas):
        r"""Sets the min_replicas of this AutoscalingConfig.

        **参数解释**：最小副本数。 **约束限制**：不涉及。 **取值范围**：[0,1000]。 **默认取值**：不涉及。

        :param min_replicas: The min_replicas of this AutoscalingConfig.
        :type min_replicas: int
        """
        self._min_replicas = min_replicas

    @property
    def max_replicas(self):
        r"""Gets the max_replicas of this AutoscalingConfig.

        **参数解释**：最大副本数。 **约束限制**：不涉及。 **取值范围**：[0,1000]。 **默认取值**：不涉及。

        :return: The max_replicas of this AutoscalingConfig.
        :rtype: int
        """
        return self._max_replicas

    @max_replicas.setter
    def max_replicas(self, max_replicas):
        r"""Sets the max_replicas of this AutoscalingConfig.

        **参数解释**：最大副本数。 **约束限制**：不涉及。 **取值范围**：[0,1000]。 **默认取值**：不涉及。

        :param max_replicas: The max_replicas of this AutoscalingConfig.
        :type max_replicas: int
        """
        self._max_replicas = max_replicas

    @property
    def initial_replicas(self):
        r"""Gets the initial_replicas of this AutoscalingConfig.

        **参数解释**：初始副本数。 **约束限制**：不涉及。 **取值范围**：[0,1000]。 **默认取值**：不涉及。

        :return: The initial_replicas of this AutoscalingConfig.
        :rtype: int
        """
        return self._initial_replicas

    @initial_replicas.setter
    def initial_replicas(self, initial_replicas):
        r"""Sets the initial_replicas of this AutoscalingConfig.

        **参数解释**：初始副本数。 **约束限制**：不涉及。 **取值范围**：[0,1000]。 **默认取值**：不涉及。

        :param initial_replicas: The initial_replicas of this AutoscalingConfig.
        :type initial_replicas: int
        """
        self._initial_replicas = initial_replicas

    @property
    def upscale_delay_s(self):
        r"""Gets the upscale_delay_s of this AutoscalingConfig.

        **参数解释**：扩容之前的等待时间。 **约束限制**：不涉及。 **取值范围**：[0,86400]。 **默认取值**：不涉及。

        :return: The upscale_delay_s of this AutoscalingConfig.
        :rtype: int
        """
        return self._upscale_delay_s

    @upscale_delay_s.setter
    def upscale_delay_s(self, upscale_delay_s):
        r"""Sets the upscale_delay_s of this AutoscalingConfig.

        **参数解释**：扩容之前的等待时间。 **约束限制**：不涉及。 **取值范围**：[0,86400]。 **默认取值**：不涉及。

        :param upscale_delay_s: The upscale_delay_s of this AutoscalingConfig.
        :type upscale_delay_s: int
        """
        self._upscale_delay_s = upscale_delay_s

    @property
    def downscale_delay_s(self):
        r"""Gets the downscale_delay_s of this AutoscalingConfig.

        **参数解释**：缩容之前的等待时间。 **约束限制**：不涉及。 **取值范围**：[0,86400]。 **默认取值**：不涉及。

        :return: The downscale_delay_s of this AutoscalingConfig.
        :rtype: int
        """
        return self._downscale_delay_s

    @downscale_delay_s.setter
    def downscale_delay_s(self, downscale_delay_s):
        r"""Sets the downscale_delay_s of this AutoscalingConfig.

        **参数解释**：缩容之前的等待时间。 **约束限制**：不涉及。 **取值范围**：[0,86400]。 **默认取值**：不涉及。

        :param downscale_delay_s: The downscale_delay_s of this AutoscalingConfig.
        :type downscale_delay_s: int
        """
        self._downscale_delay_s = downscale_delay_s

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
        if not isinstance(other, AutoscalingConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
