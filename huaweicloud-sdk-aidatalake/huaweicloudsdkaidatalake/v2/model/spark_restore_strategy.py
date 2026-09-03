# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SparkRestoreStrategy:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'max_retry': 'int',
        'retry_delay': 'int',
        'queued_timeout': 'int',
        'running_timeout': 'int'
    }

    attribute_map = {
        'max_retry': 'max_retry',
        'retry_delay': 'retry_delay',
        'queued_timeout': 'queued_timeout',
        'running_timeout': 'running_timeout'
    }

    def __init__(self, max_retry=None, retry_delay=None, queued_timeout=None, running_timeout=None):
        r"""SparkRestoreStrategy

        The model defined in huaweicloud sdk

        :param max_retry: **参数解释**：最大重试次数，用于控制作业失败后的自动重试次数。如果配置的值大于0，则自动开启失败重试；如果不配置或者配置为0，则不开启作业失败重试。 **约束限制**：不涉及。 **取值范围**：0~65535。 **默认取值**：0。 
        :type max_retry: int
        :param retry_delay: **参数解释**：重试间隔时间，用于指定作业失败重试机制中每次重试的时间间隔，单位为秒。 **约束限制**：不涉及。 **取值范围**：1~3600。 **默认取值**：30。 
        :type retry_delay: int
        :param queued_timeout: **参数解释**：排队超时时间，用于指定作业提交后等待运行的最长时间，单位为分钟。如果超过此时间作业仍未运行，则作业失败。 **约束限制**：不涉及。 **取值范围**：10~180。 **默认取值**：180。 
        :type queued_timeout: int
        :param running_timeout: **参数解释**：运行超时时间，用于指定作业运行的最大时长，单位为分钟。如果超过此时间作业还未运行结束，则作业会取消运行并标记为运行超时。 **约束限制**：不涉及。 **取值范围**：10~525600。 **默认取值**：不涉及。 
        :type running_timeout: int
        """
        
        

        self._max_retry = None
        self._retry_delay = None
        self._queued_timeout = None
        self._running_timeout = None
        self.discriminator = None

        if max_retry is not None:
            self.max_retry = max_retry
        if retry_delay is not None:
            self.retry_delay = retry_delay
        if queued_timeout is not None:
            self.queued_timeout = queued_timeout
        if running_timeout is not None:
            self.running_timeout = running_timeout

    @property
    def max_retry(self):
        r"""Gets the max_retry of this SparkRestoreStrategy.

        **参数解释**：最大重试次数，用于控制作业失败后的自动重试次数。如果配置的值大于0，则自动开启失败重试；如果不配置或者配置为0，则不开启作业失败重试。 **约束限制**：不涉及。 **取值范围**：0~65535。 **默认取值**：0。 

        :return: The max_retry of this SparkRestoreStrategy.
        :rtype: int
        """
        return self._max_retry

    @max_retry.setter
    def max_retry(self, max_retry):
        r"""Sets the max_retry of this SparkRestoreStrategy.

        **参数解释**：最大重试次数，用于控制作业失败后的自动重试次数。如果配置的值大于0，则自动开启失败重试；如果不配置或者配置为0，则不开启作业失败重试。 **约束限制**：不涉及。 **取值范围**：0~65535。 **默认取值**：0。 

        :param max_retry: The max_retry of this SparkRestoreStrategy.
        :type max_retry: int
        """
        self._max_retry = max_retry

    @property
    def retry_delay(self):
        r"""Gets the retry_delay of this SparkRestoreStrategy.

        **参数解释**：重试间隔时间，用于指定作业失败重试机制中每次重试的时间间隔，单位为秒。 **约束限制**：不涉及。 **取值范围**：1~3600。 **默认取值**：30。 

        :return: The retry_delay of this SparkRestoreStrategy.
        :rtype: int
        """
        return self._retry_delay

    @retry_delay.setter
    def retry_delay(self, retry_delay):
        r"""Sets the retry_delay of this SparkRestoreStrategy.

        **参数解释**：重试间隔时间，用于指定作业失败重试机制中每次重试的时间间隔，单位为秒。 **约束限制**：不涉及。 **取值范围**：1~3600。 **默认取值**：30。 

        :param retry_delay: The retry_delay of this SparkRestoreStrategy.
        :type retry_delay: int
        """
        self._retry_delay = retry_delay

    @property
    def queued_timeout(self):
        r"""Gets the queued_timeout of this SparkRestoreStrategy.

        **参数解释**：排队超时时间，用于指定作业提交后等待运行的最长时间，单位为分钟。如果超过此时间作业仍未运行，则作业失败。 **约束限制**：不涉及。 **取值范围**：10~180。 **默认取值**：180。 

        :return: The queued_timeout of this SparkRestoreStrategy.
        :rtype: int
        """
        return self._queued_timeout

    @queued_timeout.setter
    def queued_timeout(self, queued_timeout):
        r"""Sets the queued_timeout of this SparkRestoreStrategy.

        **参数解释**：排队超时时间，用于指定作业提交后等待运行的最长时间，单位为分钟。如果超过此时间作业仍未运行，则作业失败。 **约束限制**：不涉及。 **取值范围**：10~180。 **默认取值**：180。 

        :param queued_timeout: The queued_timeout of this SparkRestoreStrategy.
        :type queued_timeout: int
        """
        self._queued_timeout = queued_timeout

    @property
    def running_timeout(self):
        r"""Gets the running_timeout of this SparkRestoreStrategy.

        **参数解释**：运行超时时间，用于指定作业运行的最大时长，单位为分钟。如果超过此时间作业还未运行结束，则作业会取消运行并标记为运行超时。 **约束限制**：不涉及。 **取值范围**：10~525600。 **默认取值**：不涉及。 

        :return: The running_timeout of this SparkRestoreStrategy.
        :rtype: int
        """
        return self._running_timeout

    @running_timeout.setter
    def running_timeout(self, running_timeout):
        r"""Sets the running_timeout of this SparkRestoreStrategy.

        **参数解释**：运行超时时间，用于指定作业运行的最大时长，单位为分钟。如果超过此时间作业还未运行结束，则作业会取消运行并标记为运行超时。 **约束限制**：不涉及。 **取值范围**：10~525600。 **默认取值**：不涉及。 

        :param running_timeout: The running_timeout of this SparkRestoreStrategy.
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
        if not isinstance(other, SparkRestoreStrategy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
