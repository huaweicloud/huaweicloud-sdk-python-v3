# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListRaspEventsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enterprise_project_id': 'str',
        'host_id': 'str',
        'start_time': 'int',
        'end_time': 'int',
        'limit': 'int',
        'offset': 'int',
        'app_type': 'str',
        'severity': 'str',
        'attack_tag': 'str',
        'protect_status': 'str'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'host_id': 'host_id',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'limit': 'limit',
        'offset': 'offset',
        'app_type': 'app_type',
        'severity': 'severity',
        'attack_tag': 'attack_tag',
        'protect_status': 'protect_status'
    }

    def __init__(self, enterprise_project_id=None, host_id=None, start_time=None, end_time=None, limit=None, offset=None, app_type=None, severity=None, attack_tag=None, protect_status=None):
        r"""ListRaspEventsRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 
        :type enterprise_project_id: str
        :param host_id: Host Id
        :type host_id: str
        :param start_time: 查询时间段的起始时间，毫秒级时间戳(ms)
        :type start_time: int
        :param end_time: 查询时间段的终止时间，毫秒级时间戳(ms)
        :type end_time: int
        :param limit: 默认10
        :type limit: int
        :param offset: 默认0
        :type offset: int
        :param app_type: 应用类型，包含如下1种。   - java ：java类型应用防护。
        :type app_type: str
        :param severity: 告警级别 |- 告警级别，包含如下1种。 - 0 ：Info级别告警 - 1 ：Low级别告警 - 2 ：Medium级别告警 - 3 ：High级别告警 - 4 ：Critical级别告警
        :type severity: str
        :param attack_tag: 攻击标识 |- 攻击标识，包含如下6种。 - Attack Success：攻击成功 - Attack Attempt：攻击尝试 - Attack Blocked：攻击被阻断 - Abnormal Behavior：异常行为 - Collapsible Host：主机失陷 - System Vulnerability：系统脆弱性
        :type attack_tag: str
        :param protect_status: 防护状态，包含如下2种。   - closed ：未开启。   - opened ：防护中。
        :type protect_status: str
        """
        
        

        self._enterprise_project_id = None
        self._host_id = None
        self._start_time = None
        self._end_time = None
        self._limit = None
        self._offset = None
        self._app_type = None
        self._severity = None
        self._attack_tag = None
        self._protect_status = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        self.host_id = host_id
        self.start_time = start_time
        self.end_time = end_time
        self.limit = limit
        self.offset = offset
        if app_type is not None:
            self.app_type = app_type
        if severity is not None:
            self.severity = severity
        if attack_tag is not None:
            self.attack_tag = attack_tag
        if protect_status is not None:
            self.protect_status = protect_status

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListRaspEventsRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :return: The enterprise_project_id of this ListRaspEventsRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListRaspEventsRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :param enterprise_project_id: The enterprise_project_id of this ListRaspEventsRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def host_id(self):
        r"""Gets the host_id of this ListRaspEventsRequest.

        Host Id

        :return: The host_id of this ListRaspEventsRequest.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        r"""Sets the host_id of this ListRaspEventsRequest.

        Host Id

        :param host_id: The host_id of this ListRaspEventsRequest.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def start_time(self):
        r"""Gets the start_time of this ListRaspEventsRequest.

        查询时间段的起始时间，毫秒级时间戳(ms)

        :return: The start_time of this ListRaspEventsRequest.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ListRaspEventsRequest.

        查询时间段的起始时间，毫秒级时间戳(ms)

        :param start_time: The start_time of this ListRaspEventsRequest.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ListRaspEventsRequest.

        查询时间段的终止时间，毫秒级时间戳(ms)

        :return: The end_time of this ListRaspEventsRequest.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ListRaspEventsRequest.

        查询时间段的终止时间，毫秒级时间戳(ms)

        :param end_time: The end_time of this ListRaspEventsRequest.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def limit(self):
        r"""Gets the limit of this ListRaspEventsRequest.

        默认10

        :return: The limit of this ListRaspEventsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListRaspEventsRequest.

        默认10

        :param limit: The limit of this ListRaspEventsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListRaspEventsRequest.

        默认0

        :return: The offset of this ListRaspEventsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListRaspEventsRequest.

        默认0

        :param offset: The offset of this ListRaspEventsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def app_type(self):
        r"""Gets the app_type of this ListRaspEventsRequest.

        应用类型，包含如下1种。   - java ：java类型应用防护。

        :return: The app_type of this ListRaspEventsRequest.
        :rtype: str
        """
        return self._app_type

    @app_type.setter
    def app_type(self, app_type):
        r"""Sets the app_type of this ListRaspEventsRequest.

        应用类型，包含如下1种。   - java ：java类型应用防护。

        :param app_type: The app_type of this ListRaspEventsRequest.
        :type app_type: str
        """
        self._app_type = app_type

    @property
    def severity(self):
        r"""Gets the severity of this ListRaspEventsRequest.

        告警级别 |- 告警级别，包含如下1种。 - 0 ：Info级别告警 - 1 ：Low级别告警 - 2 ：Medium级别告警 - 3 ：High级别告警 - 4 ：Critical级别告警

        :return: The severity of this ListRaspEventsRequest.
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        r"""Sets the severity of this ListRaspEventsRequest.

        告警级别 |- 告警级别，包含如下1种。 - 0 ：Info级别告警 - 1 ：Low级别告警 - 2 ：Medium级别告警 - 3 ：High级别告警 - 4 ：Critical级别告警

        :param severity: The severity of this ListRaspEventsRequest.
        :type severity: str
        """
        self._severity = severity

    @property
    def attack_tag(self):
        r"""Gets the attack_tag of this ListRaspEventsRequest.

        攻击标识 |- 攻击标识，包含如下6种。 - Attack Success：攻击成功 - Attack Attempt：攻击尝试 - Attack Blocked：攻击被阻断 - Abnormal Behavior：异常行为 - Collapsible Host：主机失陷 - System Vulnerability：系统脆弱性

        :return: The attack_tag of this ListRaspEventsRequest.
        :rtype: str
        """
        return self._attack_tag

    @attack_tag.setter
    def attack_tag(self, attack_tag):
        r"""Sets the attack_tag of this ListRaspEventsRequest.

        攻击标识 |- 攻击标识，包含如下6种。 - Attack Success：攻击成功 - Attack Attempt：攻击尝试 - Attack Blocked：攻击被阻断 - Abnormal Behavior：异常行为 - Collapsible Host：主机失陷 - System Vulnerability：系统脆弱性

        :param attack_tag: The attack_tag of this ListRaspEventsRequest.
        :type attack_tag: str
        """
        self._attack_tag = attack_tag

    @property
    def protect_status(self):
        r"""Gets the protect_status of this ListRaspEventsRequest.

        防护状态，包含如下2种。   - closed ：未开启。   - opened ：防护中。

        :return: The protect_status of this ListRaspEventsRequest.
        :rtype: str
        """
        return self._protect_status

    @protect_status.setter
    def protect_status(self, protect_status):
        r"""Sets the protect_status of this ListRaspEventsRequest.

        防护状态，包含如下2种。   - closed ：未开启。   - opened ：防护中。

        :param protect_status: The protect_status of this ListRaspEventsRequest.
        :type protect_status: str
        """
        self._protect_status = protect_status

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
        if not isinstance(other, ListRaspEventsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
