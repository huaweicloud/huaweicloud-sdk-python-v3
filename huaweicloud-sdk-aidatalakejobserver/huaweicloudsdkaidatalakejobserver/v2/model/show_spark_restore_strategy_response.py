# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowSparkRestoreStrategyResponse:

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
        r"""ShowSparkRestoreStrategyResponse

        The model defined in huaweicloud sdk

        :param max_retry: **参数解释**：最大重试次数，用于控制作业失败后的自动重试。 **取值范围**：大于0表示开启失败重试，0表示不开启重试。 
        :type max_retry: int
        :param retry_delay: **参数解释**：重试间隔时间，用于指定每次重试之间的等待时间。 **取值范围**：单位为秒，默认值为30秒。 
        :type retry_delay: int
        :param queued_timeout: **参数解释**：排队超时时间，用于指定作业提交后的最大等待时间。 **取值范围**：单位为分钟，默认值为180分钟，最小值为10分钟，最大值180分钟。超过此时间作业仍未运行则作业失败。 
        :type queued_timeout: int
        :param running_timeout: **参数解释**：运行超时时间，用于指定作业运行的最大时长。 **取值范围**：单位为分钟，默认值为-1（表示不限制），最小值为10分钟，最大值为525600分钟（10年）。超过此时间作业未结束则作业会取消运行并标记失败。 
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
        r"""Gets the max_retry of this ShowSparkRestoreStrategyResponse.

        **参数解释**：最大重试次数，用于控制作业失败后的自动重试。 **取值范围**：大于0表示开启失败重试，0表示不开启重试。 

        :return: The max_retry of this ShowSparkRestoreStrategyResponse.
        :rtype: int
        """
        return self._max_retry

    @max_retry.setter
    def max_retry(self, max_retry):
        r"""Sets the max_retry of this ShowSparkRestoreStrategyResponse.

        **参数解释**：最大重试次数，用于控制作业失败后的自动重试。 **取值范围**：大于0表示开启失败重试，0表示不开启重试。 

        :param max_retry: The max_retry of this ShowSparkRestoreStrategyResponse.
        :type max_retry: int
        """
        self._max_retry = max_retry

    @property
    def retry_delay(self):
        r"""Gets the retry_delay of this ShowSparkRestoreStrategyResponse.

        **参数解释**：重试间隔时间，用于指定每次重试之间的等待时间。 **取值范围**：单位为秒，默认值为30秒。 

        :return: The retry_delay of this ShowSparkRestoreStrategyResponse.
        :rtype: int
        """
        return self._retry_delay

    @retry_delay.setter
    def retry_delay(self, retry_delay):
        r"""Sets the retry_delay of this ShowSparkRestoreStrategyResponse.

        **参数解释**：重试间隔时间，用于指定每次重试之间的等待时间。 **取值范围**：单位为秒，默认值为30秒。 

        :param retry_delay: The retry_delay of this ShowSparkRestoreStrategyResponse.
        :type retry_delay: int
        """
        self._retry_delay = retry_delay

    @property
    def queued_timeout(self):
        r"""Gets the queued_timeout of this ShowSparkRestoreStrategyResponse.

        **参数解释**：排队超时时间，用于指定作业提交后的最大等待时间。 **取值范围**：单位为分钟，默认值为180分钟，最小值为10分钟，最大值180分钟。超过此时间作业仍未运行则作业失败。 

        :return: The queued_timeout of this ShowSparkRestoreStrategyResponse.
        :rtype: int
        """
        return self._queued_timeout

    @queued_timeout.setter
    def queued_timeout(self, queued_timeout):
        r"""Sets the queued_timeout of this ShowSparkRestoreStrategyResponse.

        **参数解释**：排队超时时间，用于指定作业提交后的最大等待时间。 **取值范围**：单位为分钟，默认值为180分钟，最小值为10分钟，最大值180分钟。超过此时间作业仍未运行则作业失败。 

        :param queued_timeout: The queued_timeout of this ShowSparkRestoreStrategyResponse.
        :type queued_timeout: int
        """
        self._queued_timeout = queued_timeout

    @property
    def running_timeout(self):
        r"""Gets the running_timeout of this ShowSparkRestoreStrategyResponse.

        **参数解释**：运行超时时间，用于指定作业运行的最大时长。 **取值范围**：单位为分钟，默认值为-1（表示不限制），最小值为10分钟，最大值为525600分钟（10年）。超过此时间作业未结束则作业会取消运行并标记失败。 

        :return: The running_timeout of this ShowSparkRestoreStrategyResponse.
        :rtype: int
        """
        return self._running_timeout

    @running_timeout.setter
    def running_timeout(self, running_timeout):
        r"""Sets the running_timeout of this ShowSparkRestoreStrategyResponse.

        **参数解释**：运行超时时间，用于指定作业运行的最大时长。 **取值范围**：单位为分钟，默认值为-1（表示不限制），最小值为10分钟，最大值为525600分钟（10年）。超过此时间作业未结束则作业会取消运行并标记失败。 

        :param running_timeout: The running_timeout of this ShowSparkRestoreStrategyResponse.
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
        if not isinstance(other, ShowSparkRestoreStrategyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
