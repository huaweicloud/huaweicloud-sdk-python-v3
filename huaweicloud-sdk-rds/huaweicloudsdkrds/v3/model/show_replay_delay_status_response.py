# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowReplayDelayStatusResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cur_delay_time_mills': 'int',
        'delay_time_value_range': 'str',
        'real_delay_time_mills': 'int',
        'cur_log_replay_paused': 'bool',
        'latest_receive_log': 'str',
        'latest_replay_log': 'str'
    }

    attribute_map = {
        'cur_delay_time_mills': 'cur_delay_time_mills',
        'delay_time_value_range': 'delay_time_value_range',
        'real_delay_time_mills': 'real_delay_time_mills',
        'cur_log_replay_paused': 'cur_log_replay_paused',
        'latest_receive_log': 'latest_receive_log',
        'latest_replay_log': 'latest_replay_log'
    }

    def __init__(self, cur_delay_time_mills=None, delay_time_value_range=None, real_delay_time_mills=None, cur_log_replay_paused=None, latest_receive_log=None, latest_replay_log=None):
        r"""ShowReplayDelayStatusResponse

        The model defined in huaweicloud sdk

        :param cur_delay_time_mills: 当前配置的延迟时间，单位ms
        :type cur_delay_time_mills: int
        :param delay_time_value_range: 延迟时间参数取值范围
        :type delay_time_value_range: str
        :param real_delay_time_mills: 真实延迟时间，单位ms
        :type real_delay_time_mills: int
        :param cur_log_replay_paused: 当前日志回放状态。true表示回放暂停，false表示回放正常
        :type cur_log_replay_paused: bool
        :param latest_receive_log: 最新接收的日志
        :type latest_receive_log: str
        :param latest_replay_log: 最新回放的日志位点
        :type latest_replay_log: str
        """
        
        super(ShowReplayDelayStatusResponse, self).__init__()

        self._cur_delay_time_mills = None
        self._delay_time_value_range = None
        self._real_delay_time_mills = None
        self._cur_log_replay_paused = None
        self._latest_receive_log = None
        self._latest_replay_log = None
        self.discriminator = None

        if cur_delay_time_mills is not None:
            self.cur_delay_time_mills = cur_delay_time_mills
        if delay_time_value_range is not None:
            self.delay_time_value_range = delay_time_value_range
        if real_delay_time_mills is not None:
            self.real_delay_time_mills = real_delay_time_mills
        if cur_log_replay_paused is not None:
            self.cur_log_replay_paused = cur_log_replay_paused
        if latest_receive_log is not None:
            self.latest_receive_log = latest_receive_log
        if latest_replay_log is not None:
            self.latest_replay_log = latest_replay_log

    @property
    def cur_delay_time_mills(self):
        r"""Gets the cur_delay_time_mills of this ShowReplayDelayStatusResponse.

        当前配置的延迟时间，单位ms

        :return: The cur_delay_time_mills of this ShowReplayDelayStatusResponse.
        :rtype: int
        """
        return self._cur_delay_time_mills

    @cur_delay_time_mills.setter
    def cur_delay_time_mills(self, cur_delay_time_mills):
        r"""Sets the cur_delay_time_mills of this ShowReplayDelayStatusResponse.

        当前配置的延迟时间，单位ms

        :param cur_delay_time_mills: The cur_delay_time_mills of this ShowReplayDelayStatusResponse.
        :type cur_delay_time_mills: int
        """
        self._cur_delay_time_mills = cur_delay_time_mills

    @property
    def delay_time_value_range(self):
        r"""Gets the delay_time_value_range of this ShowReplayDelayStatusResponse.

        延迟时间参数取值范围

        :return: The delay_time_value_range of this ShowReplayDelayStatusResponse.
        :rtype: str
        """
        return self._delay_time_value_range

    @delay_time_value_range.setter
    def delay_time_value_range(self, delay_time_value_range):
        r"""Sets the delay_time_value_range of this ShowReplayDelayStatusResponse.

        延迟时间参数取值范围

        :param delay_time_value_range: The delay_time_value_range of this ShowReplayDelayStatusResponse.
        :type delay_time_value_range: str
        """
        self._delay_time_value_range = delay_time_value_range

    @property
    def real_delay_time_mills(self):
        r"""Gets the real_delay_time_mills of this ShowReplayDelayStatusResponse.

        真实延迟时间，单位ms

        :return: The real_delay_time_mills of this ShowReplayDelayStatusResponse.
        :rtype: int
        """
        return self._real_delay_time_mills

    @real_delay_time_mills.setter
    def real_delay_time_mills(self, real_delay_time_mills):
        r"""Sets the real_delay_time_mills of this ShowReplayDelayStatusResponse.

        真实延迟时间，单位ms

        :param real_delay_time_mills: The real_delay_time_mills of this ShowReplayDelayStatusResponse.
        :type real_delay_time_mills: int
        """
        self._real_delay_time_mills = real_delay_time_mills

    @property
    def cur_log_replay_paused(self):
        r"""Gets the cur_log_replay_paused of this ShowReplayDelayStatusResponse.

        当前日志回放状态。true表示回放暂停，false表示回放正常

        :return: The cur_log_replay_paused of this ShowReplayDelayStatusResponse.
        :rtype: bool
        """
        return self._cur_log_replay_paused

    @cur_log_replay_paused.setter
    def cur_log_replay_paused(self, cur_log_replay_paused):
        r"""Sets the cur_log_replay_paused of this ShowReplayDelayStatusResponse.

        当前日志回放状态。true表示回放暂停，false表示回放正常

        :param cur_log_replay_paused: The cur_log_replay_paused of this ShowReplayDelayStatusResponse.
        :type cur_log_replay_paused: bool
        """
        self._cur_log_replay_paused = cur_log_replay_paused

    @property
    def latest_receive_log(self):
        r"""Gets the latest_receive_log of this ShowReplayDelayStatusResponse.

        最新接收的日志

        :return: The latest_receive_log of this ShowReplayDelayStatusResponse.
        :rtype: str
        """
        return self._latest_receive_log

    @latest_receive_log.setter
    def latest_receive_log(self, latest_receive_log):
        r"""Sets the latest_receive_log of this ShowReplayDelayStatusResponse.

        最新接收的日志

        :param latest_receive_log: The latest_receive_log of this ShowReplayDelayStatusResponse.
        :type latest_receive_log: str
        """
        self._latest_receive_log = latest_receive_log

    @property
    def latest_replay_log(self):
        r"""Gets the latest_replay_log of this ShowReplayDelayStatusResponse.

        最新回放的日志位点

        :return: The latest_replay_log of this ShowReplayDelayStatusResponse.
        :rtype: str
        """
        return self._latest_replay_log

    @latest_replay_log.setter
    def latest_replay_log(self, latest_replay_log):
        r"""Sets the latest_replay_log of this ShowReplayDelayStatusResponse.

        最新回放的日志位点

        :param latest_replay_log: The latest_replay_log of this ShowReplayDelayStatusResponse.
        :type latest_replay_log: str
        """
        self._latest_replay_log = latest_replay_log

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
        if not isinstance(other, ShowReplayDelayStatusResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
