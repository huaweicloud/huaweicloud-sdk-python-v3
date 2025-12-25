# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IsapJobOutputSetting:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'alert_custom_properties': 'dict(str, str)',
        'alert_description': 'str',
        'alert_grouping': 'bool',
        'alert_mapping': 'dict(str, str)',
        'alert_name': 'str',
        'alert_remediation': 'str',
        'alert_severity': 'str',
        'alert_suppression': 'bool',
        'alert_type': 'dict(str, str)',
        'entity_extraction': 'dict(str, str)',
        'field_mapping': 'dict(str, str)'
    }

    attribute_map = {
        'alert_custom_properties': 'alert_custom_properties',
        'alert_description': 'alert_description',
        'alert_grouping': 'alert_grouping',
        'alert_mapping': 'alert_mapping',
        'alert_name': 'alert_name',
        'alert_remediation': 'alert_remediation',
        'alert_severity': 'alert_severity',
        'alert_suppression': 'alert_suppression',
        'alert_type': 'alert_type',
        'entity_extraction': 'entity_extraction',
        'field_mapping': 'field_mapping'
    }

    def __init__(self, alert_custom_properties=None, alert_description=None, alert_grouping=None, alert_mapping=None, alert_name=None, alert_remediation=None, alert_severity=None, alert_suppression=None, alert_type=None, entity_extraction=None, field_mapping=None):
        r"""IsapJobOutputSetting

        The model defined in huaweicloud sdk

        :param alert_custom_properties: 映射表
        :type alert_custom_properties: dict(str, str)
        :param alert_description: 告警描述
        :type alert_description: str
        :param alert_grouping: 分组标志
        :type alert_grouping: bool
        :param alert_mapping: 映射表
        :type alert_mapping: dict(str, str)
        :param alert_name: 告警报名称
        :type alert_name: str
        :param alert_remediation: 告警修复建议
        :type alert_remediation: str
        :param alert_severity: **参数解释**: 告警等级 - TIPS 提示 - LOW 低危 - MEDIUM 中危 - HIGH 高危 - FATAL 致命  **约束限制** 不涉及 **取值范围**: - TIPS - LOW - MEDIUM - HIGH - FATAL  **默认值** 不涉及  
        :type alert_severity: str
        :param alert_suppression: 抑制标志
        :type alert_suppression: bool
        :param alert_type: 告警类型映射表
        :type alert_type: dict(str, str)
        :param entity_extraction: 提取的实体
        :type entity_extraction: dict(str, str)
        :param field_mapping: 字段映射
        :type field_mapping: dict(str, str)
        """
        
        

        self._alert_custom_properties = None
        self._alert_description = None
        self._alert_grouping = None
        self._alert_mapping = None
        self._alert_name = None
        self._alert_remediation = None
        self._alert_severity = None
        self._alert_suppression = None
        self._alert_type = None
        self._entity_extraction = None
        self._field_mapping = None
        self.discriminator = None

        if alert_custom_properties is not None:
            self.alert_custom_properties = alert_custom_properties
        if alert_description is not None:
            self.alert_description = alert_description
        if alert_grouping is not None:
            self.alert_grouping = alert_grouping
        if alert_mapping is not None:
            self.alert_mapping = alert_mapping
        if alert_name is not None:
            self.alert_name = alert_name
        if alert_remediation is not None:
            self.alert_remediation = alert_remediation
        if alert_severity is not None:
            self.alert_severity = alert_severity
        if alert_suppression is not None:
            self.alert_suppression = alert_suppression
        if alert_type is not None:
            self.alert_type = alert_type
        if entity_extraction is not None:
            self.entity_extraction = entity_extraction
        if field_mapping is not None:
            self.field_mapping = field_mapping

    @property
    def alert_custom_properties(self):
        r"""Gets the alert_custom_properties of this IsapJobOutputSetting.

        映射表

        :return: The alert_custom_properties of this IsapJobOutputSetting.
        :rtype: dict(str, str)
        """
        return self._alert_custom_properties

    @alert_custom_properties.setter
    def alert_custom_properties(self, alert_custom_properties):
        r"""Sets the alert_custom_properties of this IsapJobOutputSetting.

        映射表

        :param alert_custom_properties: The alert_custom_properties of this IsapJobOutputSetting.
        :type alert_custom_properties: dict(str, str)
        """
        self._alert_custom_properties = alert_custom_properties

    @property
    def alert_description(self):
        r"""Gets the alert_description of this IsapJobOutputSetting.

        告警描述

        :return: The alert_description of this IsapJobOutputSetting.
        :rtype: str
        """
        return self._alert_description

    @alert_description.setter
    def alert_description(self, alert_description):
        r"""Sets the alert_description of this IsapJobOutputSetting.

        告警描述

        :param alert_description: The alert_description of this IsapJobOutputSetting.
        :type alert_description: str
        """
        self._alert_description = alert_description

    @property
    def alert_grouping(self):
        r"""Gets the alert_grouping of this IsapJobOutputSetting.

        分组标志

        :return: The alert_grouping of this IsapJobOutputSetting.
        :rtype: bool
        """
        return self._alert_grouping

    @alert_grouping.setter
    def alert_grouping(self, alert_grouping):
        r"""Sets the alert_grouping of this IsapJobOutputSetting.

        分组标志

        :param alert_grouping: The alert_grouping of this IsapJobOutputSetting.
        :type alert_grouping: bool
        """
        self._alert_grouping = alert_grouping

    @property
    def alert_mapping(self):
        r"""Gets the alert_mapping of this IsapJobOutputSetting.

        映射表

        :return: The alert_mapping of this IsapJobOutputSetting.
        :rtype: dict(str, str)
        """
        return self._alert_mapping

    @alert_mapping.setter
    def alert_mapping(self, alert_mapping):
        r"""Sets the alert_mapping of this IsapJobOutputSetting.

        映射表

        :param alert_mapping: The alert_mapping of this IsapJobOutputSetting.
        :type alert_mapping: dict(str, str)
        """
        self._alert_mapping = alert_mapping

    @property
    def alert_name(self):
        r"""Gets the alert_name of this IsapJobOutputSetting.

        告警报名称

        :return: The alert_name of this IsapJobOutputSetting.
        :rtype: str
        """
        return self._alert_name

    @alert_name.setter
    def alert_name(self, alert_name):
        r"""Sets the alert_name of this IsapJobOutputSetting.

        告警报名称

        :param alert_name: The alert_name of this IsapJobOutputSetting.
        :type alert_name: str
        """
        self._alert_name = alert_name

    @property
    def alert_remediation(self):
        r"""Gets the alert_remediation of this IsapJobOutputSetting.

        告警修复建议

        :return: The alert_remediation of this IsapJobOutputSetting.
        :rtype: str
        """
        return self._alert_remediation

    @alert_remediation.setter
    def alert_remediation(self, alert_remediation):
        r"""Sets the alert_remediation of this IsapJobOutputSetting.

        告警修复建议

        :param alert_remediation: The alert_remediation of this IsapJobOutputSetting.
        :type alert_remediation: str
        """
        self._alert_remediation = alert_remediation

    @property
    def alert_severity(self):
        r"""Gets the alert_severity of this IsapJobOutputSetting.

        **参数解释**: 告警等级 - TIPS 提示 - LOW 低危 - MEDIUM 中危 - HIGH 高危 - FATAL 致命  **约束限制** 不涉及 **取值范围**: - TIPS - LOW - MEDIUM - HIGH - FATAL  **默认值** 不涉及  

        :return: The alert_severity of this IsapJobOutputSetting.
        :rtype: str
        """
        return self._alert_severity

    @alert_severity.setter
    def alert_severity(self, alert_severity):
        r"""Sets the alert_severity of this IsapJobOutputSetting.

        **参数解释**: 告警等级 - TIPS 提示 - LOW 低危 - MEDIUM 中危 - HIGH 高危 - FATAL 致命  **约束限制** 不涉及 **取值范围**: - TIPS - LOW - MEDIUM - HIGH - FATAL  **默认值** 不涉及  

        :param alert_severity: The alert_severity of this IsapJobOutputSetting.
        :type alert_severity: str
        """
        self._alert_severity = alert_severity

    @property
    def alert_suppression(self):
        r"""Gets the alert_suppression of this IsapJobOutputSetting.

        抑制标志

        :return: The alert_suppression of this IsapJobOutputSetting.
        :rtype: bool
        """
        return self._alert_suppression

    @alert_suppression.setter
    def alert_suppression(self, alert_suppression):
        r"""Sets the alert_suppression of this IsapJobOutputSetting.

        抑制标志

        :param alert_suppression: The alert_suppression of this IsapJobOutputSetting.
        :type alert_suppression: bool
        """
        self._alert_suppression = alert_suppression

    @property
    def alert_type(self):
        r"""Gets the alert_type of this IsapJobOutputSetting.

        告警类型映射表

        :return: The alert_type of this IsapJobOutputSetting.
        :rtype: dict(str, str)
        """
        return self._alert_type

    @alert_type.setter
    def alert_type(self, alert_type):
        r"""Sets the alert_type of this IsapJobOutputSetting.

        告警类型映射表

        :param alert_type: The alert_type of this IsapJobOutputSetting.
        :type alert_type: dict(str, str)
        """
        self._alert_type = alert_type

    @property
    def entity_extraction(self):
        r"""Gets the entity_extraction of this IsapJobOutputSetting.

        提取的实体

        :return: The entity_extraction of this IsapJobOutputSetting.
        :rtype: dict(str, str)
        """
        return self._entity_extraction

    @entity_extraction.setter
    def entity_extraction(self, entity_extraction):
        r"""Sets the entity_extraction of this IsapJobOutputSetting.

        提取的实体

        :param entity_extraction: The entity_extraction of this IsapJobOutputSetting.
        :type entity_extraction: dict(str, str)
        """
        self._entity_extraction = entity_extraction

    @property
    def field_mapping(self):
        r"""Gets the field_mapping of this IsapJobOutputSetting.

        字段映射

        :return: The field_mapping of this IsapJobOutputSetting.
        :rtype: dict(str, str)
        """
        return self._field_mapping

    @field_mapping.setter
    def field_mapping(self, field_mapping):
        r"""Sets the field_mapping of this IsapJobOutputSetting.

        字段映射

        :param field_mapping: The field_mapping of this IsapJobOutputSetting.
        :type field_mapping: dict(str, str)
        """
        self._field_mapping = field_mapping

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
        if not isinstance(other, IsapJobOutputSetting):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
