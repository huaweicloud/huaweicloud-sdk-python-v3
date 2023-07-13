# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PoliciesClient:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'automatic_reconnection_interval': 'int',
        'session_persistence_time': 'int',
        'forbid_screen_capture': 'bool'
    }

    attribute_map = {
        'automatic_reconnection_interval': 'automatic_reconnection_interval',
        'session_persistence_time': 'session_persistence_time',
        'forbid_screen_capture': 'forbid_screen_capture'
    }

    def __init__(self, automatic_reconnection_interval=None, session_persistence_time=None, forbid_screen_capture=None):
        """PoliciesClient

        The model defined in huaweicloud sdk

        :param automatic_reconnection_interval: 自动重连间隔（秒）。取值范围为[1-50]。默认：5。
        :type automatic_reconnection_interval: int
        :param session_persistence_time: 自动重连会话保持时长（秒）。取值范围为[0-180]。默认：180。
        :type session_persistence_time: int
        :param forbid_screen_capture: 防截屏策略开关。 false：表示关闭。 true：表示开启。
        :type forbid_screen_capture: bool
        """
        
        

        self._automatic_reconnection_interval = None
        self._session_persistence_time = None
        self._forbid_screen_capture = None
        self.discriminator = None

        if automatic_reconnection_interval is not None:
            self.automatic_reconnection_interval = automatic_reconnection_interval
        if session_persistence_time is not None:
            self.session_persistence_time = session_persistence_time
        if forbid_screen_capture is not None:
            self.forbid_screen_capture = forbid_screen_capture

    @property
    def automatic_reconnection_interval(self):
        """Gets the automatic_reconnection_interval of this PoliciesClient.

        自动重连间隔（秒）。取值范围为[1-50]。默认：5。

        :return: The automatic_reconnection_interval of this PoliciesClient.
        :rtype: int
        """
        return self._automatic_reconnection_interval

    @automatic_reconnection_interval.setter
    def automatic_reconnection_interval(self, automatic_reconnection_interval):
        """Sets the automatic_reconnection_interval of this PoliciesClient.

        自动重连间隔（秒）。取值范围为[1-50]。默认：5。

        :param automatic_reconnection_interval: The automatic_reconnection_interval of this PoliciesClient.
        :type automatic_reconnection_interval: int
        """
        self._automatic_reconnection_interval = automatic_reconnection_interval

    @property
    def session_persistence_time(self):
        """Gets the session_persistence_time of this PoliciesClient.

        自动重连会话保持时长（秒）。取值范围为[0-180]。默认：180。

        :return: The session_persistence_time of this PoliciesClient.
        :rtype: int
        """
        return self._session_persistence_time

    @session_persistence_time.setter
    def session_persistence_time(self, session_persistence_time):
        """Sets the session_persistence_time of this PoliciesClient.

        自动重连会话保持时长（秒）。取值范围为[0-180]。默认：180。

        :param session_persistence_time: The session_persistence_time of this PoliciesClient.
        :type session_persistence_time: int
        """
        self._session_persistence_time = session_persistence_time

    @property
    def forbid_screen_capture(self):
        """Gets the forbid_screen_capture of this PoliciesClient.

        防截屏策略开关。 false：表示关闭。 true：表示开启。

        :return: The forbid_screen_capture of this PoliciesClient.
        :rtype: bool
        """
        return self._forbid_screen_capture

    @forbid_screen_capture.setter
    def forbid_screen_capture(self, forbid_screen_capture):
        """Sets the forbid_screen_capture of this PoliciesClient.

        防截屏策略开关。 false：表示关闭。 true：表示开启。

        :param forbid_screen_capture: The forbid_screen_capture of this PoliciesClient.
        :type forbid_screen_capture: bool
        """
        self._forbid_screen_capture = forbid_screen_capture

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
        if not isinstance(other, PoliciesClient):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
