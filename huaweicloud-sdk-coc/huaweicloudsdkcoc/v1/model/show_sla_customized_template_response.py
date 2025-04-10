# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowSlaCustomizedTemplateResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'description': 'str',
        'trigger_type': 'str',
        'trigger_level': 'str',
        'application': 'str',
        'default_template': 'bool',
        'enabled': 'bool',
        'sla_rules': 'list[SlaRuleInfo]',
        'effective_type': 'str',
        'effective_period': 'str',
        'effective_start_time': 'str',
        'effective_end_time': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'trigger_type': 'trigger_type',
        'trigger_level': 'trigger_level',
        'application': 'application',
        'default_template': 'default_template',
        'enabled': 'enabled',
        'sla_rules': 'sla_rules',
        'effective_type': 'effective_type',
        'effective_period': 'effective_period',
        'effective_start_time': 'effective_start_time',
        'effective_end_time': 'effective_end_time'
    }

    def __init__(self, id=None, name=None, description=None, trigger_type=None, trigger_level=None, application=None, default_template=None, enabled=None, sla_rules=None, effective_type=None, effective_period=None, effective_start_time=None, effective_end_time=None):
        r"""ShowSlaCustomizedTemplateResponse

        The model defined in huaweicloud sdk

        :param id: Id
        :type id: str
        :param name: 名称
        :type name: str
        :param description: 描述
        :type description: str
        :param trigger_type: 触发类型(EVENT_TICKET,ALARM_TICKET,CHANGE_NOTE,TO_DO_TASKS,ISSUE_TICKET)
        :type trigger_type: str
        :param trigger_level: 触发等级
        :type trigger_level: str
        :param application: 应用
        :type application: str
        :param default_template: 默认模板
        :type default_template: bool
        :param enabled: 启用状态
        :type enabled: bool
        :param sla_rules: 规则信息
        :type sla_rules: list[:class:`huaweicloudsdkcoc.v1.SlaRuleInfo`]
        :param effective_type: 生效类型（MON_SUN_24_HOURS一直生效、SPECIFIC_TIME阶段性生效）
        :type effective_type: str
        :param effective_period: 生效周期（每天、周一、周二、周三、周四、周五、周六、周日）
        :type effective_period: str
        :param effective_start_time: 生效开始时间
        :type effective_start_time: str
        :param effective_end_time: 生效结束时间
        :type effective_end_time: str
        """
        
        super(ShowSlaCustomizedTemplateResponse, self).__init__()

        self._id = None
        self._name = None
        self._description = None
        self._trigger_type = None
        self._trigger_level = None
        self._application = None
        self._default_template = None
        self._enabled = None
        self._sla_rules = None
        self._effective_type = None
        self._effective_period = None
        self._effective_start_time = None
        self._effective_end_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if trigger_type is not None:
            self.trigger_type = trigger_type
        if trigger_level is not None:
            self.trigger_level = trigger_level
        if application is not None:
            self.application = application
        if default_template is not None:
            self.default_template = default_template
        if enabled is not None:
            self.enabled = enabled
        if sla_rules is not None:
            self.sla_rules = sla_rules
        if effective_type is not None:
            self.effective_type = effective_type
        if effective_period is not None:
            self.effective_period = effective_period
        if effective_start_time is not None:
            self.effective_start_time = effective_start_time
        if effective_end_time is not None:
            self.effective_end_time = effective_end_time

    @property
    def id(self):
        r"""Gets the id of this ShowSlaCustomizedTemplateResponse.

        Id

        :return: The id of this ShowSlaCustomizedTemplateResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ShowSlaCustomizedTemplateResponse.

        Id

        :param id: The id of this ShowSlaCustomizedTemplateResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ShowSlaCustomizedTemplateResponse.

        名称

        :return: The name of this ShowSlaCustomizedTemplateResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ShowSlaCustomizedTemplateResponse.

        名称

        :param name: The name of this ShowSlaCustomizedTemplateResponse.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this ShowSlaCustomizedTemplateResponse.

        描述

        :return: The description of this ShowSlaCustomizedTemplateResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ShowSlaCustomizedTemplateResponse.

        描述

        :param description: The description of this ShowSlaCustomizedTemplateResponse.
        :type description: str
        """
        self._description = description

    @property
    def trigger_type(self):
        r"""Gets the trigger_type of this ShowSlaCustomizedTemplateResponse.

        触发类型(EVENT_TICKET,ALARM_TICKET,CHANGE_NOTE,TO_DO_TASKS,ISSUE_TICKET)

        :return: The trigger_type of this ShowSlaCustomizedTemplateResponse.
        :rtype: str
        """
        return self._trigger_type

    @trigger_type.setter
    def trigger_type(self, trigger_type):
        r"""Sets the trigger_type of this ShowSlaCustomizedTemplateResponse.

        触发类型(EVENT_TICKET,ALARM_TICKET,CHANGE_NOTE,TO_DO_TASKS,ISSUE_TICKET)

        :param trigger_type: The trigger_type of this ShowSlaCustomizedTemplateResponse.
        :type trigger_type: str
        """
        self._trigger_type = trigger_type

    @property
    def trigger_level(self):
        r"""Gets the trigger_level of this ShowSlaCustomizedTemplateResponse.

        触发等级

        :return: The trigger_level of this ShowSlaCustomizedTemplateResponse.
        :rtype: str
        """
        return self._trigger_level

    @trigger_level.setter
    def trigger_level(self, trigger_level):
        r"""Sets the trigger_level of this ShowSlaCustomizedTemplateResponse.

        触发等级

        :param trigger_level: The trigger_level of this ShowSlaCustomizedTemplateResponse.
        :type trigger_level: str
        """
        self._trigger_level = trigger_level

    @property
    def application(self):
        r"""Gets the application of this ShowSlaCustomizedTemplateResponse.

        应用

        :return: The application of this ShowSlaCustomizedTemplateResponse.
        :rtype: str
        """
        return self._application

    @application.setter
    def application(self, application):
        r"""Sets the application of this ShowSlaCustomizedTemplateResponse.

        应用

        :param application: The application of this ShowSlaCustomizedTemplateResponse.
        :type application: str
        """
        self._application = application

    @property
    def default_template(self):
        r"""Gets the default_template of this ShowSlaCustomizedTemplateResponse.

        默认模板

        :return: The default_template of this ShowSlaCustomizedTemplateResponse.
        :rtype: bool
        """
        return self._default_template

    @default_template.setter
    def default_template(self, default_template):
        r"""Sets the default_template of this ShowSlaCustomizedTemplateResponse.

        默认模板

        :param default_template: The default_template of this ShowSlaCustomizedTemplateResponse.
        :type default_template: bool
        """
        self._default_template = default_template

    @property
    def enabled(self):
        r"""Gets the enabled of this ShowSlaCustomizedTemplateResponse.

        启用状态

        :return: The enabled of this ShowSlaCustomizedTemplateResponse.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        r"""Sets the enabled of this ShowSlaCustomizedTemplateResponse.

        启用状态

        :param enabled: The enabled of this ShowSlaCustomizedTemplateResponse.
        :type enabled: bool
        """
        self._enabled = enabled

    @property
    def sla_rules(self):
        r"""Gets the sla_rules of this ShowSlaCustomizedTemplateResponse.

        规则信息

        :return: The sla_rules of this ShowSlaCustomizedTemplateResponse.
        :rtype: list[:class:`huaweicloudsdkcoc.v1.SlaRuleInfo`]
        """
        return self._sla_rules

    @sla_rules.setter
    def sla_rules(self, sla_rules):
        r"""Sets the sla_rules of this ShowSlaCustomizedTemplateResponse.

        规则信息

        :param sla_rules: The sla_rules of this ShowSlaCustomizedTemplateResponse.
        :type sla_rules: list[:class:`huaweicloudsdkcoc.v1.SlaRuleInfo`]
        """
        self._sla_rules = sla_rules

    @property
    def effective_type(self):
        r"""Gets the effective_type of this ShowSlaCustomizedTemplateResponse.

        生效类型（MON_SUN_24_HOURS一直生效、SPECIFIC_TIME阶段性生效）

        :return: The effective_type of this ShowSlaCustomizedTemplateResponse.
        :rtype: str
        """
        return self._effective_type

    @effective_type.setter
    def effective_type(self, effective_type):
        r"""Sets the effective_type of this ShowSlaCustomizedTemplateResponse.

        生效类型（MON_SUN_24_HOURS一直生效、SPECIFIC_TIME阶段性生效）

        :param effective_type: The effective_type of this ShowSlaCustomizedTemplateResponse.
        :type effective_type: str
        """
        self._effective_type = effective_type

    @property
    def effective_period(self):
        r"""Gets the effective_period of this ShowSlaCustomizedTemplateResponse.

        生效周期（每天、周一、周二、周三、周四、周五、周六、周日）

        :return: The effective_period of this ShowSlaCustomizedTemplateResponse.
        :rtype: str
        """
        return self._effective_period

    @effective_period.setter
    def effective_period(self, effective_period):
        r"""Sets the effective_period of this ShowSlaCustomizedTemplateResponse.

        生效周期（每天、周一、周二、周三、周四、周五、周六、周日）

        :param effective_period: The effective_period of this ShowSlaCustomizedTemplateResponse.
        :type effective_period: str
        """
        self._effective_period = effective_period

    @property
    def effective_start_time(self):
        r"""Gets the effective_start_time of this ShowSlaCustomizedTemplateResponse.

        生效开始时间

        :return: The effective_start_time of this ShowSlaCustomizedTemplateResponse.
        :rtype: str
        """
        return self._effective_start_time

    @effective_start_time.setter
    def effective_start_time(self, effective_start_time):
        r"""Sets the effective_start_time of this ShowSlaCustomizedTemplateResponse.

        生效开始时间

        :param effective_start_time: The effective_start_time of this ShowSlaCustomizedTemplateResponse.
        :type effective_start_time: str
        """
        self._effective_start_time = effective_start_time

    @property
    def effective_end_time(self):
        r"""Gets the effective_end_time of this ShowSlaCustomizedTemplateResponse.

        生效结束时间

        :return: The effective_end_time of this ShowSlaCustomizedTemplateResponse.
        :rtype: str
        """
        return self._effective_end_time

    @effective_end_time.setter
    def effective_end_time(self, effective_end_time):
        r"""Sets the effective_end_time of this ShowSlaCustomizedTemplateResponse.

        生效结束时间

        :param effective_end_time: The effective_end_time of this ShowSlaCustomizedTemplateResponse.
        :type effective_end_time: str
        """
        self._effective_end_time = effective_end_time

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
        if not isinstance(other, ShowSlaCustomizedTemplateResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
