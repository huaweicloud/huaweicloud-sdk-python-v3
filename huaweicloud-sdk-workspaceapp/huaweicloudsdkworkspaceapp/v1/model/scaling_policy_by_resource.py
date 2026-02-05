# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ScalingPolicyByResource:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cpu_usage_threshold': 'int',
        'mem_usage_threshold': 'int',
        'gpu_usage_threshold': 'int'
    }

    attribute_map = {
        'cpu_usage_threshold': 'cpu_usage_threshold',
        'mem_usage_threshold': 'mem_usage_threshold',
        'gpu_usage_threshold': 'gpu_usage_threshold'
    }

    def __init__(self, cpu_usage_threshold=None, mem_usage_threshold=None, gpu_usage_threshold=None):
        r"""ScalingPolicyByResource

        The model defined in huaweicloud sdk

        :param cpu_usage_threshold: 分组的总cpu使用率(达到阈值后扩容)。
        :type cpu_usage_threshold: int
        :param mem_usage_threshold: 分组的总mem使用率(达到改阈值后扩容)。
        :type mem_usage_threshold: int
        :param gpu_usage_threshold: 分组的总显存使用率(达到改阈值后扩容)。
        :type gpu_usage_threshold: int
        """
        
        

        self._cpu_usage_threshold = None
        self._mem_usage_threshold = None
        self._gpu_usage_threshold = None
        self.discriminator = None

        if cpu_usage_threshold is not None:
            self.cpu_usage_threshold = cpu_usage_threshold
        if mem_usage_threshold is not None:
            self.mem_usage_threshold = mem_usage_threshold
        if gpu_usage_threshold is not None:
            self.gpu_usage_threshold = gpu_usage_threshold

    @property
    def cpu_usage_threshold(self):
        r"""Gets the cpu_usage_threshold of this ScalingPolicyByResource.

        分组的总cpu使用率(达到阈值后扩容)。

        :return: The cpu_usage_threshold of this ScalingPolicyByResource.
        :rtype: int
        """
        return self._cpu_usage_threshold

    @cpu_usage_threshold.setter
    def cpu_usage_threshold(self, cpu_usage_threshold):
        r"""Sets the cpu_usage_threshold of this ScalingPolicyByResource.

        分组的总cpu使用率(达到阈值后扩容)。

        :param cpu_usage_threshold: The cpu_usage_threshold of this ScalingPolicyByResource.
        :type cpu_usage_threshold: int
        """
        self._cpu_usage_threshold = cpu_usage_threshold

    @property
    def mem_usage_threshold(self):
        r"""Gets the mem_usage_threshold of this ScalingPolicyByResource.

        分组的总mem使用率(达到改阈值后扩容)。

        :return: The mem_usage_threshold of this ScalingPolicyByResource.
        :rtype: int
        """
        return self._mem_usage_threshold

    @mem_usage_threshold.setter
    def mem_usage_threshold(self, mem_usage_threshold):
        r"""Sets the mem_usage_threshold of this ScalingPolicyByResource.

        分组的总mem使用率(达到改阈值后扩容)。

        :param mem_usage_threshold: The mem_usage_threshold of this ScalingPolicyByResource.
        :type mem_usage_threshold: int
        """
        self._mem_usage_threshold = mem_usage_threshold

    @property
    def gpu_usage_threshold(self):
        r"""Gets the gpu_usage_threshold of this ScalingPolicyByResource.

        分组的总显存使用率(达到改阈值后扩容)。

        :return: The gpu_usage_threshold of this ScalingPolicyByResource.
        :rtype: int
        """
        return self._gpu_usage_threshold

    @gpu_usage_threshold.setter
    def gpu_usage_threshold(self, gpu_usage_threshold):
        r"""Sets the gpu_usage_threshold of this ScalingPolicyByResource.

        分组的总显存使用率(达到改阈值后扩容)。

        :param gpu_usage_threshold: The gpu_usage_threshold of this ScalingPolicyByResource.
        :type gpu_usage_threshold: int
        """
        self._gpu_usage_threshold = gpu_usage_threshold

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
        if not isinstance(other, ScalingPolicyByResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
