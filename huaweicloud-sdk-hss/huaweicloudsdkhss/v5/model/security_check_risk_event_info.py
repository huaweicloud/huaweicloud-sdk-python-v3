# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SecurityCheckRiskEventInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'severity': 'str',
        'event_name': 'str',
        'event_class_id': 'str',
        'attack_flag': 'str',
        'attack_time': 'int',
        'status': 'str'
    }

    attribute_map = {
        'severity': 'severity',
        'event_name': 'event_name',
        'event_class_id': 'event_class_id',
        'attack_flag': 'attack_flag',
        'attack_time': 'attack_time',
        'status': 'status'
    }

    def __init__(self, severity=None, event_name=None, event_class_id=None, attack_flag=None, attack_time=None, status=None):
        r"""SecurityCheckRiskEventInfo

        The model defined in huaweicloud sdk

        :param severity: **参数解释**： 风险级别 **取值范围**： - high：高危 - medium：中危 - low：低危 - safe：安全，无风险 
        :type severity: str
        :param event_name: **参数解释**： 告警事件名称 **取值范围**： 不涉及 
        :type event_name: str
        :param event_class_id: **参数解释**： 告警事件class，用于前台生成事件名称 **取值范围**： 不涉及 
        :type event_class_id: str
        :param attack_flag: **参数解释**： 攻击标识 **取值范围**： 不涉及 
        :type attack_flag: str
        :param attack_time: **参数解释**： 攻击时间 **取值范围**： 不涉及 
        :type attack_time: int
        :param status: **参数解释**： 处理状态 **取值范围**： - unhandled：未处理 - handled：已处理 
        :type status: str
        """
        
        

        self._severity = None
        self._event_name = None
        self._event_class_id = None
        self._attack_flag = None
        self._attack_time = None
        self._status = None
        self.discriminator = None

        if severity is not None:
            self.severity = severity
        if event_name is not None:
            self.event_name = event_name
        if event_class_id is not None:
            self.event_class_id = event_class_id
        if attack_flag is not None:
            self.attack_flag = attack_flag
        if attack_time is not None:
            self.attack_time = attack_time
        if status is not None:
            self.status = status

    @property
    def severity(self):
        r"""Gets the severity of this SecurityCheckRiskEventInfo.

        **参数解释**： 风险级别 **取值范围**： - high：高危 - medium：中危 - low：低危 - safe：安全，无风险 

        :return: The severity of this SecurityCheckRiskEventInfo.
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        r"""Sets the severity of this SecurityCheckRiskEventInfo.

        **参数解释**： 风险级别 **取值范围**： - high：高危 - medium：中危 - low：低危 - safe：安全，无风险 

        :param severity: The severity of this SecurityCheckRiskEventInfo.
        :type severity: str
        """
        self._severity = severity

    @property
    def event_name(self):
        r"""Gets the event_name of this SecurityCheckRiskEventInfo.

        **参数解释**： 告警事件名称 **取值范围**： 不涉及 

        :return: The event_name of this SecurityCheckRiskEventInfo.
        :rtype: str
        """
        return self._event_name

    @event_name.setter
    def event_name(self, event_name):
        r"""Sets the event_name of this SecurityCheckRiskEventInfo.

        **参数解释**： 告警事件名称 **取值范围**： 不涉及 

        :param event_name: The event_name of this SecurityCheckRiskEventInfo.
        :type event_name: str
        """
        self._event_name = event_name

    @property
    def event_class_id(self):
        r"""Gets the event_class_id of this SecurityCheckRiskEventInfo.

        **参数解释**： 告警事件class，用于前台生成事件名称 **取值范围**： 不涉及 

        :return: The event_class_id of this SecurityCheckRiskEventInfo.
        :rtype: str
        """
        return self._event_class_id

    @event_class_id.setter
    def event_class_id(self, event_class_id):
        r"""Sets the event_class_id of this SecurityCheckRiskEventInfo.

        **参数解释**： 告警事件class，用于前台生成事件名称 **取值范围**： 不涉及 

        :param event_class_id: The event_class_id of this SecurityCheckRiskEventInfo.
        :type event_class_id: str
        """
        self._event_class_id = event_class_id

    @property
    def attack_flag(self):
        r"""Gets the attack_flag of this SecurityCheckRiskEventInfo.

        **参数解释**： 攻击标识 **取值范围**： 不涉及 

        :return: The attack_flag of this SecurityCheckRiskEventInfo.
        :rtype: str
        """
        return self._attack_flag

    @attack_flag.setter
    def attack_flag(self, attack_flag):
        r"""Sets the attack_flag of this SecurityCheckRiskEventInfo.

        **参数解释**： 攻击标识 **取值范围**： 不涉及 

        :param attack_flag: The attack_flag of this SecurityCheckRiskEventInfo.
        :type attack_flag: str
        """
        self._attack_flag = attack_flag

    @property
    def attack_time(self):
        r"""Gets the attack_time of this SecurityCheckRiskEventInfo.

        **参数解释**： 攻击时间 **取值范围**： 不涉及 

        :return: The attack_time of this SecurityCheckRiskEventInfo.
        :rtype: int
        """
        return self._attack_time

    @attack_time.setter
    def attack_time(self, attack_time):
        r"""Sets the attack_time of this SecurityCheckRiskEventInfo.

        **参数解释**： 攻击时间 **取值范围**： 不涉及 

        :param attack_time: The attack_time of this SecurityCheckRiskEventInfo.
        :type attack_time: int
        """
        self._attack_time = attack_time

    @property
    def status(self):
        r"""Gets the status of this SecurityCheckRiskEventInfo.

        **参数解释**： 处理状态 **取值范围**： - unhandled：未处理 - handled：已处理 

        :return: The status of this SecurityCheckRiskEventInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this SecurityCheckRiskEventInfo.

        **参数解释**： 处理状态 **取值范围**： - unhandled：未处理 - handled：已处理 

        :param status: The status of this SecurityCheckRiskEventInfo.
        :type status: str
        """
        self._status = status

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
        if not isinstance(other, SecurityCheckRiskEventInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
