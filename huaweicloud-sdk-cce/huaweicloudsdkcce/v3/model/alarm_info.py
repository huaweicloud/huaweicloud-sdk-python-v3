# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AlarmInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'topics': 'list[str]',
        'alarm_rule_template_id': 'str',
        'prom_instance_id': 'str',
        'prom_enterprise_project_id': 'str'
    }

    attribute_map = {
        'topics': 'topics',
        'alarm_rule_template_id': 'alarmRuleTemplateId',
        'prom_instance_id': 'promInstanceID',
        'prom_enterprise_project_id': 'promEnterpriseProjectID'
    }

    def __init__(self, topics=None, alarm_rule_template_id=None, prom_instance_id=None, prom_enterprise_project_id=None):
        r"""AlarmInfo

        The model defined in huaweicloud sdk

        :param topics: **参数解释：** 联系组列表。填写SMN主题名称，通过配置告警联系组，分组管理订阅终端，接收告警信息。 **约束限制：** 不涉及
        :type topics: list[str]
        :param alarm_rule_template_id: **参数解释：** 开启告警助手时传入告警模板ID。默认采用容器场景下的告警规则模板。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type alarm_rule_template_id: str
        :param prom_instance_id: **参数解释：** 开启告警助手时传入AOM普罗实例的id。若未安装普罗插件或者未对接AOM实例，此参数无需指定，告警中心将不会创建指标类告警规则。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type prom_instance_id: str
        :param prom_enterprise_project_id: **参数解释：** 开启告警助手时传入AOM普罗实例的企业项目id。若未安装普罗插件或者未对接AOM实例，此参数无需指定，告警中心将不会创建指标类告警规则。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type prom_enterprise_project_id: str
        """
        
        

        self._topics = None
        self._alarm_rule_template_id = None
        self._prom_instance_id = None
        self._prom_enterprise_project_id = None
        self.discriminator = None

        self.topics = topics
        if alarm_rule_template_id is not None:
            self.alarm_rule_template_id = alarm_rule_template_id
        if prom_instance_id is not None:
            self.prom_instance_id = prom_instance_id
        if prom_enterprise_project_id is not None:
            self.prom_enterprise_project_id = prom_enterprise_project_id

    @property
    def topics(self):
        r"""Gets the topics of this AlarmInfo.

        **参数解释：** 联系组列表。填写SMN主题名称，通过配置告警联系组，分组管理订阅终端，接收告警信息。 **约束限制：** 不涉及

        :return: The topics of this AlarmInfo.
        :rtype: list[str]
        """
        return self._topics

    @topics.setter
    def topics(self, topics):
        r"""Sets the topics of this AlarmInfo.

        **参数解释：** 联系组列表。填写SMN主题名称，通过配置告警联系组，分组管理订阅终端，接收告警信息。 **约束限制：** 不涉及

        :param topics: The topics of this AlarmInfo.
        :type topics: list[str]
        """
        self._topics = topics

    @property
    def alarm_rule_template_id(self):
        r"""Gets the alarm_rule_template_id of this AlarmInfo.

        **参数解释：** 开启告警助手时传入告警模板ID。默认采用容器场景下的告警规则模板。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The alarm_rule_template_id of this AlarmInfo.
        :rtype: str
        """
        return self._alarm_rule_template_id

    @alarm_rule_template_id.setter
    def alarm_rule_template_id(self, alarm_rule_template_id):
        r"""Sets the alarm_rule_template_id of this AlarmInfo.

        **参数解释：** 开启告警助手时传入告警模板ID。默认采用容器场景下的告警规则模板。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param alarm_rule_template_id: The alarm_rule_template_id of this AlarmInfo.
        :type alarm_rule_template_id: str
        """
        self._alarm_rule_template_id = alarm_rule_template_id

    @property
    def prom_instance_id(self):
        r"""Gets the prom_instance_id of this AlarmInfo.

        **参数解释：** 开启告警助手时传入AOM普罗实例的id。若未安装普罗插件或者未对接AOM实例，此参数无需指定，告警中心将不会创建指标类告警规则。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The prom_instance_id of this AlarmInfo.
        :rtype: str
        """
        return self._prom_instance_id

    @prom_instance_id.setter
    def prom_instance_id(self, prom_instance_id):
        r"""Sets the prom_instance_id of this AlarmInfo.

        **参数解释：** 开启告警助手时传入AOM普罗实例的id。若未安装普罗插件或者未对接AOM实例，此参数无需指定，告警中心将不会创建指标类告警规则。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param prom_instance_id: The prom_instance_id of this AlarmInfo.
        :type prom_instance_id: str
        """
        self._prom_instance_id = prom_instance_id

    @property
    def prom_enterprise_project_id(self):
        r"""Gets the prom_enterprise_project_id of this AlarmInfo.

        **参数解释：** 开启告警助手时传入AOM普罗实例的企业项目id。若未安装普罗插件或者未对接AOM实例，此参数无需指定，告警中心将不会创建指标类告警规则。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The prom_enterprise_project_id of this AlarmInfo.
        :rtype: str
        """
        return self._prom_enterprise_project_id

    @prom_enterprise_project_id.setter
    def prom_enterprise_project_id(self, prom_enterprise_project_id):
        r"""Sets the prom_enterprise_project_id of this AlarmInfo.

        **参数解释：** 开启告警助手时传入AOM普罗实例的企业项目id。若未安装普罗插件或者未对接AOM实例，此参数无需指定，告警中心将不会创建指标类告警规则。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param prom_enterprise_project_id: The prom_enterprise_project_id of this AlarmInfo.
        :type prom_enterprise_project_id: str
        """
        self._prom_enterprise_project_id = prom_enterprise_project_id

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
        if not isinstance(other, AlarmInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
