# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpgradeProbeTimeoutConfigDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'timeout': 'int',
        'failure_threshold': 'int'
    }

    attribute_map = {
        'timeout': 'timeout',
        'failure_threshold': 'failure_threshold'
    }

    def __init__(self, timeout=None, failure_threshold=None):
        r"""UpgradeProbeTimeoutConfigDTO

        The model defined in huaweicloud sdk

        :param timeout: 超时时间
        :type timeout: int
        :param failure_threshold: 失败阈值
        :type failure_threshold: int
        """
        
        

        self._timeout = None
        self._failure_threshold = None
        self.discriminator = None

        if timeout is not None:
            self.timeout = timeout
        if failure_threshold is not None:
            self.failure_threshold = failure_threshold

    @property
    def timeout(self):
        r"""Gets the timeout of this UpgradeProbeTimeoutConfigDTO.

        超时时间

        :return: The timeout of this UpgradeProbeTimeoutConfigDTO.
        :rtype: int
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        r"""Sets the timeout of this UpgradeProbeTimeoutConfigDTO.

        超时时间

        :param timeout: The timeout of this UpgradeProbeTimeoutConfigDTO.
        :type timeout: int
        """
        self._timeout = timeout

    @property
    def failure_threshold(self):
        r"""Gets the failure_threshold of this UpgradeProbeTimeoutConfigDTO.

        失败阈值

        :return: The failure_threshold of this UpgradeProbeTimeoutConfigDTO.
        :rtype: int
        """
        return self._failure_threshold

    @failure_threshold.setter
    def failure_threshold(self, failure_threshold):
        r"""Sets the failure_threshold of this UpgradeProbeTimeoutConfigDTO.

        失败阈值

        :param failure_threshold: The failure_threshold of this UpgradeProbeTimeoutConfigDTO.
        :type failure_threshold: int
        """
        self._failure_threshold = failure_threshold

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
        if not isinstance(other, UpgradeProbeTimeoutConfigDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
