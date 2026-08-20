# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SparkSqlTimeout:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'queued_timeout': 'int',
        'running_timeout': 'int'
    }

    attribute_map = {
        'queued_timeout': 'queued_timeout',
        'running_timeout': 'running_timeout'
    }

    def __init__(self, queued_timeout=None, running_timeout=None):
        r"""SparkSqlTimeout

        The model defined in huaweicloud sdk

        :param queued_timeout: **参数解释**：作业排队超时时间，单位为分钟。如果超过此时间作业仍未开始运行，则作业会被标记为排队超时并失败。 **取值范围**：10~180分钟。 
        :type queued_timeout: int
        :param running_timeout: **参数解释**：作业运行超时时间，单位为分钟。如果超过此时间作业仍未运行结束，则作业会被取消并标记为运行超时。 **取值范围**：10~720分钟。 
        :type running_timeout: int
        """
        
        

        self._queued_timeout = None
        self._running_timeout = None
        self.discriminator = None

        if queued_timeout is not None:
            self.queued_timeout = queued_timeout
        if running_timeout is not None:
            self.running_timeout = running_timeout

    @property
    def queued_timeout(self):
        r"""Gets the queued_timeout of this SparkSqlTimeout.

        **参数解释**：作业排队超时时间，单位为分钟。如果超过此时间作业仍未开始运行，则作业会被标记为排队超时并失败。 **取值范围**：10~180分钟。 

        :return: The queued_timeout of this SparkSqlTimeout.
        :rtype: int
        """
        return self._queued_timeout

    @queued_timeout.setter
    def queued_timeout(self, queued_timeout):
        r"""Sets the queued_timeout of this SparkSqlTimeout.

        **参数解释**：作业排队超时时间，单位为分钟。如果超过此时间作业仍未开始运行，则作业会被标记为排队超时并失败。 **取值范围**：10~180分钟。 

        :param queued_timeout: The queued_timeout of this SparkSqlTimeout.
        :type queued_timeout: int
        """
        self._queued_timeout = queued_timeout

    @property
    def running_timeout(self):
        r"""Gets the running_timeout of this SparkSqlTimeout.

        **参数解释**：作业运行超时时间，单位为分钟。如果超过此时间作业仍未运行结束，则作业会被取消并标记为运行超时。 **取值范围**：10~720分钟。 

        :return: The running_timeout of this SparkSqlTimeout.
        :rtype: int
        """
        return self._running_timeout

    @running_timeout.setter
    def running_timeout(self, running_timeout):
        r"""Sets the running_timeout of this SparkSqlTimeout.

        **参数解释**：作业运行超时时间，单位为分钟。如果超过此时间作业仍未运行结束，则作业会被取消并标记为运行超时。 **取值范围**：10~720分钟。 

        :param running_timeout: The running_timeout of this SparkSqlTimeout.
        :type running_timeout: int
        """
        self._running_timeout = running_timeout

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
        if not isinstance(other, SparkSqlTimeout):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
