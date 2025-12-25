# coding: utf-8

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
        'offset': 'int',
        'limit': 'int',
        'host_id': 'str',
        'start_time': 'int',
        'end_time': 'int',
        'app_type': 'str',
        'severity': 'str',
        'attack_tag': 'str',
        'protect_status': 'str'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'offset': 'offset',
        'limit': 'limit',
        'host_id': 'host_id',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'app_type': 'app_type',
        'severity': 'severity',
        'attack_tag': 'attack_tag',
        'protect_status': 'protect_status'
    }

    def __init__(self, enterprise_project_id=None, offset=None, limit=None, host_id=None, start_time=None, end_time=None, app_type=None, severity=None, attack_tag=None, protect_status=None):
        r"""ListRaspEventsRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 
        :type enterprise_project_id: str
        :param offset: **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 
        :type offset: int
        :param limit: **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 
        :type limit: int
        :param host_id: Host Id
        :type host_id: str
        :param start_time: **参数解释**: 应用防护事件的查询起始时间（Unix时间戳），与end_time配合筛选指定时间段内的事件 **时间格式** Unix时间戳（精确到毫秒，如1736414463000表示2024-12-10 10:41:03） **约束限制**: 需小于end_time，否则返回空结果；时间戳需为有效时间（1970-01-01 00:00:00至今） **取值范围**: 取值0-9223372036854775807 **默认取值**: 无 
        :type start_time: int
        :param end_time: **参数解释**: 查询时间段的终止时间，毫秒级时间戳(ms) **约束限制**: 不涉及 **取值范围**: 取值0-9223372036854775807 **默认取值**: 无 
        :type end_time: int
        :param app_type: **参数解释** 应用防护的应用类型，用于筛选指定类型应用的防护事件 **约束限制** 当前仅支持java类型，传其他值返回空结果，区分大小写 **取值范围** - java：Java语言开发的应用防护事件 **默认取值** 无（查询所有支持的应用类型事件）
        :type app_type: str
        :param severity: **参数解释** 应用防护事件的告警级别，用于筛选指定严重程度的事件 **约束限制** 取值必须在指定范围内，否则返回空结果 **取值范围** - Security：信息级 - Low：低危 - Medium：中危 - High：高危 - Critical：紧急 **默认取值** 无 
        :type severity: str
        :param attack_tag: **参数解释** 应用防护事件的攻击类型标识，用于筛选指定攻击类型的事件 **约束限制** 取值区分大小写，必须与指定格式一致，否则返回空结果 **取值范围** - Attack Success：攻击成功 - Attack Attempt：攻击尝试 - Attack Blocked：攻击被阻断 - Abnormal Behavior：异常行为 - Collapsible Host：主机失陷 - System Vulnerability：系统脆弱性 **默认取值** 无 
        :type attack_tag: str
        :param protect_status: **参数解释** 应用防护的启用状态，用于筛选指定防护状态下的事件 **约束限制** 取值区分大小写，必须在指定范围内，否则返回空结果 **取值范围** - closed：未开启防护 - opened：已开启防护 **默认取值** 无（查询所有防护状态的事件） 
        :type protect_status: str
        """
        
        

        self._enterprise_project_id = None
        self._offset = None
        self._limit = None
        self._host_id = None
        self._start_time = None
        self._end_time = None
        self._app_type = None
        self._severity = None
        self._attack_tag = None
        self._protect_status = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        self.host_id = host_id
        self.start_time = start_time
        self.end_time = end_time
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
    def offset(self):
        r"""Gets the offset of this ListRaspEventsRequest.

        **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 

        :return: The offset of this ListRaspEventsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListRaspEventsRequest.

        **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 

        :param offset: The offset of this ListRaspEventsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListRaspEventsRequest.

        **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 

        :return: The limit of this ListRaspEventsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListRaspEventsRequest.

        **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 

        :param limit: The limit of this ListRaspEventsRequest.
        :type limit: int
        """
        self._limit = limit

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

        **参数解释**: 应用防护事件的查询起始时间（Unix时间戳），与end_time配合筛选指定时间段内的事件 **时间格式** Unix时间戳（精确到毫秒，如1736414463000表示2024-12-10 10:41:03） **约束限制**: 需小于end_time，否则返回空结果；时间戳需为有效时间（1970-01-01 00:00:00至今） **取值范围**: 取值0-9223372036854775807 **默认取值**: 无 

        :return: The start_time of this ListRaspEventsRequest.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ListRaspEventsRequest.

        **参数解释**: 应用防护事件的查询起始时间（Unix时间戳），与end_time配合筛选指定时间段内的事件 **时间格式** Unix时间戳（精确到毫秒，如1736414463000表示2024-12-10 10:41:03） **约束限制**: 需小于end_time，否则返回空结果；时间戳需为有效时间（1970-01-01 00:00:00至今） **取值范围**: 取值0-9223372036854775807 **默认取值**: 无 

        :param start_time: The start_time of this ListRaspEventsRequest.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ListRaspEventsRequest.

        **参数解释**: 查询时间段的终止时间，毫秒级时间戳(ms) **约束限制**: 不涉及 **取值范围**: 取值0-9223372036854775807 **默认取值**: 无 

        :return: The end_time of this ListRaspEventsRequest.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ListRaspEventsRequest.

        **参数解释**: 查询时间段的终止时间，毫秒级时间戳(ms) **约束限制**: 不涉及 **取值范围**: 取值0-9223372036854775807 **默认取值**: 无 

        :param end_time: The end_time of this ListRaspEventsRequest.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def app_type(self):
        r"""Gets the app_type of this ListRaspEventsRequest.

        **参数解释** 应用防护的应用类型，用于筛选指定类型应用的防护事件 **约束限制** 当前仅支持java类型，传其他值返回空结果，区分大小写 **取值范围** - java：Java语言开发的应用防护事件 **默认取值** 无（查询所有支持的应用类型事件）

        :return: The app_type of this ListRaspEventsRequest.
        :rtype: str
        """
        return self._app_type

    @app_type.setter
    def app_type(self, app_type):
        r"""Sets the app_type of this ListRaspEventsRequest.

        **参数解释** 应用防护的应用类型，用于筛选指定类型应用的防护事件 **约束限制** 当前仅支持java类型，传其他值返回空结果，区分大小写 **取值范围** - java：Java语言开发的应用防护事件 **默认取值** 无（查询所有支持的应用类型事件）

        :param app_type: The app_type of this ListRaspEventsRequest.
        :type app_type: str
        """
        self._app_type = app_type

    @property
    def severity(self):
        r"""Gets the severity of this ListRaspEventsRequest.

        **参数解释** 应用防护事件的告警级别，用于筛选指定严重程度的事件 **约束限制** 取值必须在指定范围内，否则返回空结果 **取值范围** - Security：信息级 - Low：低危 - Medium：中危 - High：高危 - Critical：紧急 **默认取值** 无 

        :return: The severity of this ListRaspEventsRequest.
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        r"""Sets the severity of this ListRaspEventsRequest.

        **参数解释** 应用防护事件的告警级别，用于筛选指定严重程度的事件 **约束限制** 取值必须在指定范围内，否则返回空结果 **取值范围** - Security：信息级 - Low：低危 - Medium：中危 - High：高危 - Critical：紧急 **默认取值** 无 

        :param severity: The severity of this ListRaspEventsRequest.
        :type severity: str
        """
        self._severity = severity

    @property
    def attack_tag(self):
        r"""Gets the attack_tag of this ListRaspEventsRequest.

        **参数解释** 应用防护事件的攻击类型标识，用于筛选指定攻击类型的事件 **约束限制** 取值区分大小写，必须与指定格式一致，否则返回空结果 **取值范围** - Attack Success：攻击成功 - Attack Attempt：攻击尝试 - Attack Blocked：攻击被阻断 - Abnormal Behavior：异常行为 - Collapsible Host：主机失陷 - System Vulnerability：系统脆弱性 **默认取值** 无 

        :return: The attack_tag of this ListRaspEventsRequest.
        :rtype: str
        """
        return self._attack_tag

    @attack_tag.setter
    def attack_tag(self, attack_tag):
        r"""Sets the attack_tag of this ListRaspEventsRequest.

        **参数解释** 应用防护事件的攻击类型标识，用于筛选指定攻击类型的事件 **约束限制** 取值区分大小写，必须与指定格式一致，否则返回空结果 **取值范围** - Attack Success：攻击成功 - Attack Attempt：攻击尝试 - Attack Blocked：攻击被阻断 - Abnormal Behavior：异常行为 - Collapsible Host：主机失陷 - System Vulnerability：系统脆弱性 **默认取值** 无 

        :param attack_tag: The attack_tag of this ListRaspEventsRequest.
        :type attack_tag: str
        """
        self._attack_tag = attack_tag

    @property
    def protect_status(self):
        r"""Gets the protect_status of this ListRaspEventsRequest.

        **参数解释** 应用防护的启用状态，用于筛选指定防护状态下的事件 **约束限制** 取值区分大小写，必须在指定范围内，否则返回空结果 **取值范围** - closed：未开启防护 - opened：已开启防护 **默认取值** 无（查询所有防护状态的事件） 

        :return: The protect_status of this ListRaspEventsRequest.
        :rtype: str
        """
        return self._protect_status

    @protect_status.setter
    def protect_status(self, protect_status):
        r"""Sets the protect_status of this ListRaspEventsRequest.

        **参数解释** 应用防护的启用状态，用于筛选指定防护状态下的事件 **约束限制** 取值区分大小写，必须在指定范围内，否则返回空结果 **取值范围** - closed：未开启防护 - opened：已开启防护 **默认取值** 无（查询所有防护状态的事件） 

        :param protect_status: The protect_status of this ListRaspEventsRequest.
        :type protect_status: str
        """
        self._protect_status = protect_status

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
        if not isinstance(other, ListRaspEventsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
