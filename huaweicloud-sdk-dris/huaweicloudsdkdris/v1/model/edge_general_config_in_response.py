# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EdgeGeneralConfigInResponse:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'avp_enabled': 'bool',
        'rsm_enabled': 'bool',
        'time_compensate': 'bool',
        'rsi_positioning_enabled': 'bool',
        'log_level': 'str',
        'road_detection_length': 'float',
        'ramp_detection_length': 'float',
        'gat1400_username': 'str',
        'user_name': 'str'
    }

    attribute_map = {
        'avp_enabled': 'avp_enabled',
        'rsm_enabled': 'rsm_enabled',
        'time_compensate': 'time_compensate',
        'rsi_positioning_enabled': 'rsi_positioning_enabled',
        'log_level': 'log_level',
        'road_detection_length': 'road_detection_length',
        'ramp_detection_length': 'ramp_detection_length',
        'gat1400_username': 'gat1400_username',
        'user_name': 'user_name'
    }

    def __init__(self, avp_enabled=None, rsm_enabled=None, time_compensate=None, rsi_positioning_enabled=None, log_level=None, road_detection_length=None, ramp_detection_length=None, gat1400_username=None, user_name=None):
        """EdgeGeneralConfigInResponse

        The model defined in huaweicloud sdk

        :param avp_enabled: **参数说明**：AVP场景。
        :type avp_enabled: bool
        :param rsm_enabled: **参数说明**：RSM上报：默认不上报。
        :type rsm_enabled: bool
        :param time_compensate: **参数说明**：时延补偿：是否启动Edge时延补偿功能。
        :type time_compensate: bool
        :param rsi_positioning_enabled: **参数说明**：RSI事件定位功能。
        :type rsi_positioning_enabled: bool
        :param log_level: **参数说明**：应用日志级别  **取值范围**：on/off，默认关闭。
        :type log_level: str
        :param road_detection_length: **参数说明**：道路检测长度，单位：米。
        :type road_detection_length: float
        :param ramp_detection_length: **参数说明**：匝道检测长度，单位：米。
        :type ramp_detection_length: float
        :param gat1400_username: **参数说明**：1400接口用户名。  **取值范围**：长度不小于8，不大于32，只允许数字字母下划线组合，且不能以数字下划线开头，不能有中文和特殊字符，gat1400用户名不能与gat1400密码相同。
        :type gat1400_username: str
        :param user_name: **参数说明**：ITS800鉴权用的用户名和密码。
        :type user_name: str
        """
        
        

        self._avp_enabled = None
        self._rsm_enabled = None
        self._time_compensate = None
        self._rsi_positioning_enabled = None
        self._log_level = None
        self._road_detection_length = None
        self._ramp_detection_length = None
        self._gat1400_username = None
        self._user_name = None
        self.discriminator = None

        if avp_enabled is not None:
            self.avp_enabled = avp_enabled
        if rsm_enabled is not None:
            self.rsm_enabled = rsm_enabled
        if time_compensate is not None:
            self.time_compensate = time_compensate
        if rsi_positioning_enabled is not None:
            self.rsi_positioning_enabled = rsi_positioning_enabled
        if log_level is not None:
            self.log_level = log_level
        if road_detection_length is not None:
            self.road_detection_length = road_detection_length
        if ramp_detection_length is not None:
            self.ramp_detection_length = ramp_detection_length
        if gat1400_username is not None:
            self.gat1400_username = gat1400_username
        if user_name is not None:
            self.user_name = user_name

    @property
    def avp_enabled(self):
        """Gets the avp_enabled of this EdgeGeneralConfigInResponse.

        **参数说明**：AVP场景。

        :return: The avp_enabled of this EdgeGeneralConfigInResponse.
        :rtype: bool
        """
        return self._avp_enabled

    @avp_enabled.setter
    def avp_enabled(self, avp_enabled):
        """Sets the avp_enabled of this EdgeGeneralConfigInResponse.

        **参数说明**：AVP场景。

        :param avp_enabled: The avp_enabled of this EdgeGeneralConfigInResponse.
        :type avp_enabled: bool
        """
        self._avp_enabled = avp_enabled

    @property
    def rsm_enabled(self):
        """Gets the rsm_enabled of this EdgeGeneralConfigInResponse.

        **参数说明**：RSM上报：默认不上报。

        :return: The rsm_enabled of this EdgeGeneralConfigInResponse.
        :rtype: bool
        """
        return self._rsm_enabled

    @rsm_enabled.setter
    def rsm_enabled(self, rsm_enabled):
        """Sets the rsm_enabled of this EdgeGeneralConfigInResponse.

        **参数说明**：RSM上报：默认不上报。

        :param rsm_enabled: The rsm_enabled of this EdgeGeneralConfigInResponse.
        :type rsm_enabled: bool
        """
        self._rsm_enabled = rsm_enabled

    @property
    def time_compensate(self):
        """Gets the time_compensate of this EdgeGeneralConfigInResponse.

        **参数说明**：时延补偿：是否启动Edge时延补偿功能。

        :return: The time_compensate of this EdgeGeneralConfigInResponse.
        :rtype: bool
        """
        return self._time_compensate

    @time_compensate.setter
    def time_compensate(self, time_compensate):
        """Sets the time_compensate of this EdgeGeneralConfigInResponse.

        **参数说明**：时延补偿：是否启动Edge时延补偿功能。

        :param time_compensate: The time_compensate of this EdgeGeneralConfigInResponse.
        :type time_compensate: bool
        """
        self._time_compensate = time_compensate

    @property
    def rsi_positioning_enabled(self):
        """Gets the rsi_positioning_enabled of this EdgeGeneralConfigInResponse.

        **参数说明**：RSI事件定位功能。

        :return: The rsi_positioning_enabled of this EdgeGeneralConfigInResponse.
        :rtype: bool
        """
        return self._rsi_positioning_enabled

    @rsi_positioning_enabled.setter
    def rsi_positioning_enabled(self, rsi_positioning_enabled):
        """Sets the rsi_positioning_enabled of this EdgeGeneralConfigInResponse.

        **参数说明**：RSI事件定位功能。

        :param rsi_positioning_enabled: The rsi_positioning_enabled of this EdgeGeneralConfigInResponse.
        :type rsi_positioning_enabled: bool
        """
        self._rsi_positioning_enabled = rsi_positioning_enabled

    @property
    def log_level(self):
        """Gets the log_level of this EdgeGeneralConfigInResponse.

        **参数说明**：应用日志级别  **取值范围**：on/off，默认关闭。

        :return: The log_level of this EdgeGeneralConfigInResponse.
        :rtype: str
        """
        return self._log_level

    @log_level.setter
    def log_level(self, log_level):
        """Sets the log_level of this EdgeGeneralConfigInResponse.

        **参数说明**：应用日志级别  **取值范围**：on/off，默认关闭。

        :param log_level: The log_level of this EdgeGeneralConfigInResponse.
        :type log_level: str
        """
        self._log_level = log_level

    @property
    def road_detection_length(self):
        """Gets the road_detection_length of this EdgeGeneralConfigInResponse.

        **参数说明**：道路检测长度，单位：米。

        :return: The road_detection_length of this EdgeGeneralConfigInResponse.
        :rtype: float
        """
        return self._road_detection_length

    @road_detection_length.setter
    def road_detection_length(self, road_detection_length):
        """Sets the road_detection_length of this EdgeGeneralConfigInResponse.

        **参数说明**：道路检测长度，单位：米。

        :param road_detection_length: The road_detection_length of this EdgeGeneralConfigInResponse.
        :type road_detection_length: float
        """
        self._road_detection_length = road_detection_length

    @property
    def ramp_detection_length(self):
        """Gets the ramp_detection_length of this EdgeGeneralConfigInResponse.

        **参数说明**：匝道检测长度，单位：米。

        :return: The ramp_detection_length of this EdgeGeneralConfigInResponse.
        :rtype: float
        """
        return self._ramp_detection_length

    @ramp_detection_length.setter
    def ramp_detection_length(self, ramp_detection_length):
        """Sets the ramp_detection_length of this EdgeGeneralConfigInResponse.

        **参数说明**：匝道检测长度，单位：米。

        :param ramp_detection_length: The ramp_detection_length of this EdgeGeneralConfigInResponse.
        :type ramp_detection_length: float
        """
        self._ramp_detection_length = ramp_detection_length

    @property
    def gat1400_username(self):
        """Gets the gat1400_username of this EdgeGeneralConfigInResponse.

        **参数说明**：1400接口用户名。  **取值范围**：长度不小于8，不大于32，只允许数字字母下划线组合，且不能以数字下划线开头，不能有中文和特殊字符，gat1400用户名不能与gat1400密码相同。

        :return: The gat1400_username of this EdgeGeneralConfigInResponse.
        :rtype: str
        """
        return self._gat1400_username

    @gat1400_username.setter
    def gat1400_username(self, gat1400_username):
        """Sets the gat1400_username of this EdgeGeneralConfigInResponse.

        **参数说明**：1400接口用户名。  **取值范围**：长度不小于8，不大于32，只允许数字字母下划线组合，且不能以数字下划线开头，不能有中文和特殊字符，gat1400用户名不能与gat1400密码相同。

        :param gat1400_username: The gat1400_username of this EdgeGeneralConfigInResponse.
        :type gat1400_username: str
        """
        self._gat1400_username = gat1400_username

    @property
    def user_name(self):
        """Gets the user_name of this EdgeGeneralConfigInResponse.

        **参数说明**：ITS800鉴权用的用户名和密码。

        :return: The user_name of this EdgeGeneralConfigInResponse.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this EdgeGeneralConfigInResponse.

        **参数说明**：ITS800鉴权用的用户名和密码。

        :param user_name: The user_name of this EdgeGeneralConfigInResponse.
        :type user_name: str
        """
        self._user_name = user_name

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
        if not isinstance(other, EdgeGeneralConfigInResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
