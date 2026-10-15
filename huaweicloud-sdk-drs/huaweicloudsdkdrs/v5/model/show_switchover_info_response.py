# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowSwitchoverInfoResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'last_switchover_time': 'str',
        'increment_check_point': 'str',
        'target_safe_point': 'str'
    }

    attribute_map = {
        'last_switchover_time': 'last_switchover_time',
        'increment_check_point': 'increment_check_point',
        'target_safe_point': 'target_safe_point'
    }

    def __init__(self, last_switchover_time=None, increment_check_point=None, target_safe_point=None):
        r"""ShowSwitchoverInfoResponse

        The model defined in huaweicloud sdk

        :param last_switchover_time: 上次倒换完成时间点
        :type last_switchover_time: str
        :param increment_check_point: 上次倒换任务位点信息
        :type increment_check_point: str
        :param target_safe_point: 上次倒换目标库倒换时位点
        :type target_safe_point: str
        """
        
        super().__init__()

        self._last_switchover_time = None
        self._increment_check_point = None
        self._target_safe_point = None
        self.discriminator = None

        if last_switchover_time is not None:
            self.last_switchover_time = last_switchover_time
        if increment_check_point is not None:
            self.increment_check_point = increment_check_point
        if target_safe_point is not None:
            self.target_safe_point = target_safe_point

    @property
    def last_switchover_time(self):
        r"""Gets the last_switchover_time of this ShowSwitchoverInfoResponse.

        上次倒换完成时间点

        :return: The last_switchover_time of this ShowSwitchoverInfoResponse.
        :rtype: str
        """
        return self._last_switchover_time

    @last_switchover_time.setter
    def last_switchover_time(self, last_switchover_time):
        r"""Sets the last_switchover_time of this ShowSwitchoverInfoResponse.

        上次倒换完成时间点

        :param last_switchover_time: The last_switchover_time of this ShowSwitchoverInfoResponse.
        :type last_switchover_time: str
        """
        self._last_switchover_time = last_switchover_time

    @property
    def increment_check_point(self):
        r"""Gets the increment_check_point of this ShowSwitchoverInfoResponse.

        上次倒换任务位点信息

        :return: The increment_check_point of this ShowSwitchoverInfoResponse.
        :rtype: str
        """
        return self._increment_check_point

    @increment_check_point.setter
    def increment_check_point(self, increment_check_point):
        r"""Sets the increment_check_point of this ShowSwitchoverInfoResponse.

        上次倒换任务位点信息

        :param increment_check_point: The increment_check_point of this ShowSwitchoverInfoResponse.
        :type increment_check_point: str
        """
        self._increment_check_point = increment_check_point

    @property
    def target_safe_point(self):
        r"""Gets the target_safe_point of this ShowSwitchoverInfoResponse.

        上次倒换目标库倒换时位点

        :return: The target_safe_point of this ShowSwitchoverInfoResponse.
        :rtype: str
        """
        return self._target_safe_point

    @target_safe_point.setter
    def target_safe_point(self, target_safe_point):
        r"""Sets the target_safe_point of this ShowSwitchoverInfoResponse.

        上次倒换目标库倒换时位点

        :param target_safe_point: The target_safe_point of this ShowSwitchoverInfoResponse.
        :type target_safe_point: str
        """
        self._target_safe_point = target_safe_point

    def to_dict(self):
        import warnings
        warnings.warn("ShowSwitchoverInfoResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, ShowSwitchoverInfoResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
