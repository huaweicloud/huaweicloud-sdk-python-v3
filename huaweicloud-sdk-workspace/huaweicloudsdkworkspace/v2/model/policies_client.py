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
        'autoclose_monitor_after_locked': 'bool',
        'autoclose_monitor_options': 'PoliciesClientAutocloseMonitorOptions',
        'forbid_screen_capture': 'bool',
        'client_machine_join_domain': 'bool',
        'client_type': 'PoliciesClientClientType'
    }

    attribute_map = {
        'automatic_reconnection_interval': 'automatic_reconnection_interval',
        'session_persistence_time': 'session_persistence_time',
        'autoclose_monitor_after_locked': 'autoclose_monitor_after_locked',
        'autoclose_monitor_options': 'autoclose_monitor_options',
        'forbid_screen_capture': 'forbid_screen_capture',
        'client_machine_join_domain': 'client_machine_join_domain',
        'client_type': 'client_type'
    }

    def __init__(self, automatic_reconnection_interval=None, session_persistence_time=None, autoclose_monitor_after_locked=None, autoclose_monitor_options=None, forbid_screen_capture=None, client_machine_join_domain=None, client_type=None):
        r"""PoliciesClient

        The model defined in huaweicloud sdk

        :param automatic_reconnection_interval: 自动重连间隔（秒）。取值范围为[1-50]。默认：5。
        :type automatic_reconnection_interval: int
        :param session_persistence_time: 自动重连会话保持时长（秒）。取值范围为[0-180]。默认：180。
        :type session_persistence_time: int
        :param autoclose_monitor_after_locked: 锁屏后自动关闭本地显示器。取值为： false：表示关闭。 true：表示开启。
        :type autoclose_monitor_after_locked: bool
        :param autoclose_monitor_options: 
        :type autoclose_monitor_options: :class:`huaweicloudsdkworkspace.v2.PoliciesClientAutocloseMonitorOptions`
        :param forbid_screen_capture: 防截屏策略开关。 false：表示关闭。 true：表示开启。
        :type forbid_screen_capture: bool
        :param client_machine_join_domain: 终端机器加域校验开关。 false：表示关闭。 true：表示开启。
        :type client_machine_join_domain: bool
        :param client_type: 
        :type client_type: :class:`huaweicloudsdkworkspace.v2.PoliciesClientClientType`
        """
        
        

        self._automatic_reconnection_interval = None
        self._session_persistence_time = None
        self._autoclose_monitor_after_locked = None
        self._autoclose_monitor_options = None
        self._forbid_screen_capture = None
        self._client_machine_join_domain = None
        self._client_type = None
        self.discriminator = None

        if automatic_reconnection_interval is not None:
            self.automatic_reconnection_interval = automatic_reconnection_interval
        if session_persistence_time is not None:
            self.session_persistence_time = session_persistence_time
        if autoclose_monitor_after_locked is not None:
            self.autoclose_monitor_after_locked = autoclose_monitor_after_locked
        if autoclose_monitor_options is not None:
            self.autoclose_monitor_options = autoclose_monitor_options
        if forbid_screen_capture is not None:
            self.forbid_screen_capture = forbid_screen_capture
        if client_machine_join_domain is not None:
            self.client_machine_join_domain = client_machine_join_domain
        if client_type is not None:
            self.client_type = client_type

    @property
    def automatic_reconnection_interval(self):
        r"""Gets the automatic_reconnection_interval of this PoliciesClient.

        自动重连间隔（秒）。取值范围为[1-50]。默认：5。

        :return: The automatic_reconnection_interval of this PoliciesClient.
        :rtype: int
        """
        return self._automatic_reconnection_interval

    @automatic_reconnection_interval.setter
    def automatic_reconnection_interval(self, automatic_reconnection_interval):
        r"""Sets the automatic_reconnection_interval of this PoliciesClient.

        自动重连间隔（秒）。取值范围为[1-50]。默认：5。

        :param automatic_reconnection_interval: The automatic_reconnection_interval of this PoliciesClient.
        :type automatic_reconnection_interval: int
        """
        self._automatic_reconnection_interval = automatic_reconnection_interval

    @property
    def session_persistence_time(self):
        r"""Gets the session_persistence_time of this PoliciesClient.

        自动重连会话保持时长（秒）。取值范围为[0-180]。默认：180。

        :return: The session_persistence_time of this PoliciesClient.
        :rtype: int
        """
        return self._session_persistence_time

    @session_persistence_time.setter
    def session_persistence_time(self, session_persistence_time):
        r"""Sets the session_persistence_time of this PoliciesClient.

        自动重连会话保持时长（秒）。取值范围为[0-180]。默认：180。

        :param session_persistence_time: The session_persistence_time of this PoliciesClient.
        :type session_persistence_time: int
        """
        self._session_persistence_time = session_persistence_time

    @property
    def autoclose_monitor_after_locked(self):
        r"""Gets the autoclose_monitor_after_locked of this PoliciesClient.

        锁屏后自动关闭本地显示器。取值为： false：表示关闭。 true：表示开启。

        :return: The autoclose_monitor_after_locked of this PoliciesClient.
        :rtype: bool
        """
        return self._autoclose_monitor_after_locked

    @autoclose_monitor_after_locked.setter
    def autoclose_monitor_after_locked(self, autoclose_monitor_after_locked):
        r"""Sets the autoclose_monitor_after_locked of this PoliciesClient.

        锁屏后自动关闭本地显示器。取值为： false：表示关闭。 true：表示开启。

        :param autoclose_monitor_after_locked: The autoclose_monitor_after_locked of this PoliciesClient.
        :type autoclose_monitor_after_locked: bool
        """
        self._autoclose_monitor_after_locked = autoclose_monitor_after_locked

    @property
    def autoclose_monitor_options(self):
        r"""Gets the autoclose_monitor_options of this PoliciesClient.

        :return: The autoclose_monitor_options of this PoliciesClient.
        :rtype: :class:`huaweicloudsdkworkspace.v2.PoliciesClientAutocloseMonitorOptions`
        """
        return self._autoclose_monitor_options

    @autoclose_monitor_options.setter
    def autoclose_monitor_options(self, autoclose_monitor_options):
        r"""Sets the autoclose_monitor_options of this PoliciesClient.

        :param autoclose_monitor_options: The autoclose_monitor_options of this PoliciesClient.
        :type autoclose_monitor_options: :class:`huaweicloudsdkworkspace.v2.PoliciesClientAutocloseMonitorOptions`
        """
        self._autoclose_monitor_options = autoclose_monitor_options

    @property
    def forbid_screen_capture(self):
        r"""Gets the forbid_screen_capture of this PoliciesClient.

        防截屏策略开关。 false：表示关闭。 true：表示开启。

        :return: The forbid_screen_capture of this PoliciesClient.
        :rtype: bool
        """
        return self._forbid_screen_capture

    @forbid_screen_capture.setter
    def forbid_screen_capture(self, forbid_screen_capture):
        r"""Sets the forbid_screen_capture of this PoliciesClient.

        防截屏策略开关。 false：表示关闭。 true：表示开启。

        :param forbid_screen_capture: The forbid_screen_capture of this PoliciesClient.
        :type forbid_screen_capture: bool
        """
        self._forbid_screen_capture = forbid_screen_capture

    @property
    def client_machine_join_domain(self):
        r"""Gets the client_machine_join_domain of this PoliciesClient.

        终端机器加域校验开关。 false：表示关闭。 true：表示开启。

        :return: The client_machine_join_domain of this PoliciesClient.
        :rtype: bool
        """
        return self._client_machine_join_domain

    @client_machine_join_domain.setter
    def client_machine_join_domain(self, client_machine_join_domain):
        r"""Sets the client_machine_join_domain of this PoliciesClient.

        终端机器加域校验开关。 false：表示关闭。 true：表示开启。

        :param client_machine_join_domain: The client_machine_join_domain of this PoliciesClient.
        :type client_machine_join_domain: bool
        """
        self._client_machine_join_domain = client_machine_join_domain

    @property
    def client_type(self):
        r"""Gets the client_type of this PoliciesClient.

        :return: The client_type of this PoliciesClient.
        :rtype: :class:`huaweicloudsdkworkspace.v2.PoliciesClientClientType`
        """
        return self._client_type

    @client_type.setter
    def client_type(self, client_type):
        r"""Sets the client_type of this PoliciesClient.

        :param client_type: The client_type of this PoliciesClient.
        :type client_type: :class:`huaweicloudsdkworkspace.v2.PoliciesClientClientType`
        """
        self._client_type = client_type

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
