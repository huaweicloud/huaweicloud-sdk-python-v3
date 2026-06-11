# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RoutePolicyDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'max_session': 'int',
        'cpu_threshold': 'int',
        'gpu_threshold': 'int',
        'mem_threshold': 'int'
    }

    attribute_map = {
        'max_session': 'max_session',
        'cpu_threshold': 'cpu_threshold',
        'gpu_threshold': 'gpu_threshold',
        'mem_threshold': 'mem_threshold'
    }

    def __init__(self, max_session=None, cpu_threshold=None, gpu_threshold=None, mem_threshold=None):
        r"""RoutePolicyDetail

        The model defined in huaweicloud sdk

        :param max_session: 单台服务器最大的连接会话数。
        :type max_session: int
        :param cpu_threshold: cpu使用率阈值，单位为%。
        :type cpu_threshold: int
        :param gpu_threshold: gpu显存使用率阈值，单位为%。
        :type gpu_threshold: int
        :param mem_threshold: 内存使用率阈值，单位为%。
        :type mem_threshold: int
        """
        
        

        self._max_session = None
        self._cpu_threshold = None
        self._gpu_threshold = None
        self._mem_threshold = None
        self.discriminator = None

        if max_session is not None:
            self.max_session = max_session
        if cpu_threshold is not None:
            self.cpu_threshold = cpu_threshold
        if gpu_threshold is not None:
            self.gpu_threshold = gpu_threshold
        if mem_threshold is not None:
            self.mem_threshold = mem_threshold

    @property
    def max_session(self):
        r"""Gets the max_session of this RoutePolicyDetail.

        单台服务器最大的连接会话数。

        :return: The max_session of this RoutePolicyDetail.
        :rtype: int
        """
        return self._max_session

    @max_session.setter
    def max_session(self, max_session):
        r"""Sets the max_session of this RoutePolicyDetail.

        单台服务器最大的连接会话数。

        :param max_session: The max_session of this RoutePolicyDetail.
        :type max_session: int
        """
        self._max_session = max_session

    @property
    def cpu_threshold(self):
        r"""Gets the cpu_threshold of this RoutePolicyDetail.

        cpu使用率阈值，单位为%。

        :return: The cpu_threshold of this RoutePolicyDetail.
        :rtype: int
        """
        return self._cpu_threshold

    @cpu_threshold.setter
    def cpu_threshold(self, cpu_threshold):
        r"""Sets the cpu_threshold of this RoutePolicyDetail.

        cpu使用率阈值，单位为%。

        :param cpu_threshold: The cpu_threshold of this RoutePolicyDetail.
        :type cpu_threshold: int
        """
        self._cpu_threshold = cpu_threshold

    @property
    def gpu_threshold(self):
        r"""Gets the gpu_threshold of this RoutePolicyDetail.

        gpu显存使用率阈值，单位为%。

        :return: The gpu_threshold of this RoutePolicyDetail.
        :rtype: int
        """
        return self._gpu_threshold

    @gpu_threshold.setter
    def gpu_threshold(self, gpu_threshold):
        r"""Sets the gpu_threshold of this RoutePolicyDetail.

        gpu显存使用率阈值，单位为%。

        :param gpu_threshold: The gpu_threshold of this RoutePolicyDetail.
        :type gpu_threshold: int
        """
        self._gpu_threshold = gpu_threshold

    @property
    def mem_threshold(self):
        r"""Gets the mem_threshold of this RoutePolicyDetail.

        内存使用率阈值，单位为%。

        :return: The mem_threshold of this RoutePolicyDetail.
        :rtype: int
        """
        return self._mem_threshold

    @mem_threshold.setter
    def mem_threshold(self, mem_threshold):
        r"""Sets the mem_threshold of this RoutePolicyDetail.

        内存使用率阈值，单位为%。

        :param mem_threshold: The mem_threshold of this RoutePolicyDetail.
        :type mem_threshold: int
        """
        self._mem_threshold = mem_threshold

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
        if not isinstance(other, RoutePolicyDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
