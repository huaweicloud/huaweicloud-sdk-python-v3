# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AlarmRuleTemplateBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'alarm_rule_template_name': 'str',
        'alarm_rule_template_name_en': 'str',
        'alarm_rule_template_description': 'str',
        'alarm_rule_template_id': 'str',
        'alarm_rule_template_project_id': 'str',
        'alarm_rule_template_type': 'str',
        'alarm_rule_template_source': 'str',
        'alarm_rule_template_binding': 'dict(str, str)',
        'alarm_template_spec_list': 'list[AlarmRuleTemplateSpecWithCloudService]',
        'enterprise_project_id': 'str',
        'create_time': 'int',
        'modify_time': 'int',
        'templating': 'Templating',
        'template_version': 'str'
    }

    attribute_map = {
        'alarm_rule_template_name': 'alarm_rule_template_name',
        'alarm_rule_template_name_en': 'alarm_rule_template_name_en',
        'alarm_rule_template_description': 'alarm_rule_template_description',
        'alarm_rule_template_id': 'alarm_rule_template_id',
        'alarm_rule_template_project_id': 'alarm_rule_template_project_id',
        'alarm_rule_template_type': 'alarm_rule_template_type',
        'alarm_rule_template_source': 'alarm_rule_template_source',
        'alarm_rule_template_binding': 'alarm_rule_template_binding',
        'alarm_template_spec_list': 'alarm_template_spec_list',
        'enterprise_project_id': 'enterprise_project_id',
        'create_time': 'create_time',
        'modify_time': 'modify_time',
        'templating': 'templating',
        'template_version': 'template_version'
    }

    def __init__(self, alarm_rule_template_name=None, alarm_rule_template_name_en=None, alarm_rule_template_description=None, alarm_rule_template_id=None, alarm_rule_template_project_id=None, alarm_rule_template_type=None, alarm_rule_template_source=None, alarm_rule_template_binding=None, alarm_template_spec_list=None, enterprise_project_id=None, create_time=None, modify_time=None, templating=None, template_version=None):
        r"""AlarmRuleTemplateBody

        The model defined in huaweicloud sdk

        :param alarm_rule_template_name: 告警模板名称。
        :type alarm_rule_template_name: str
        :param alarm_rule_template_name_en: 告警模板英文名称。
        :type alarm_rule_template_name_en: str
        :param alarm_rule_template_description: 告警模板描述。
        :type alarm_rule_template_description: str
        :param alarm_rule_template_id: 告警模板id。
        :type alarm_rule_template_id: str
        :param alarm_rule_template_project_id: 项目ID，可以从控制台获取，也可以从调用API处获取。获取方式请参见：[获取项目ID](aom_04_0024.xml)。
        :type alarm_rule_template_project_id: str
        :param alarm_rule_template_type: 告警模板类型 - “statics”：静态告警模板 - “dynamic”：动态告警模板
        :type alarm_rule_template_type: str
        :param alarm_rule_template_source: 告警模板来源。
        :type alarm_rule_template_source: str
        :param alarm_rule_template_binding: 告警模板所绑定的告警规则。
        :type alarm_rule_template_binding: dict(str, str)
        :param alarm_template_spec_list: 告警模板列表。
        :type alarm_template_spec_list: list[:class:`huaweicloudsdkaom.v2.AlarmRuleTemplateSpecWithCloudService`]
        :param enterprise_project_id: 企业项目id。获取方式请参见：[获取企业项目ID](aom_04_0024.xml)。
        :type enterprise_project_id: str
        :param create_time: 创建时间。
        :type create_time: int
        :param modify_time: 更新时间。
        :type modify_time: int
        :param templating: 
        :type templating: :class:`huaweicloudsdkaom.v2.Templating`
        :param template_version: 告警模板版本。
        :type template_version: str
        """
        
        

        self._alarm_rule_template_name = None
        self._alarm_rule_template_name_en = None
        self._alarm_rule_template_description = None
        self._alarm_rule_template_id = None
        self._alarm_rule_template_project_id = None
        self._alarm_rule_template_type = None
        self._alarm_rule_template_source = None
        self._alarm_rule_template_binding = None
        self._alarm_template_spec_list = None
        self._enterprise_project_id = None
        self._create_time = None
        self._modify_time = None
        self._templating = None
        self._template_version = None
        self.discriminator = None

        self.alarm_rule_template_name = alarm_rule_template_name
        if alarm_rule_template_name_en is not None:
            self.alarm_rule_template_name_en = alarm_rule_template_name_en
        self.alarm_rule_template_description = alarm_rule_template_description
        self.alarm_rule_template_id = alarm_rule_template_id
        if alarm_rule_template_project_id is not None:
            self.alarm_rule_template_project_id = alarm_rule_template_project_id
        self.alarm_rule_template_type = alarm_rule_template_type
        if alarm_rule_template_source is not None:
            self.alarm_rule_template_source = alarm_rule_template_source
        self.alarm_rule_template_binding = alarm_rule_template_binding
        self.alarm_template_spec_list = alarm_template_spec_list
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if create_time is not None:
            self.create_time = create_time
        if modify_time is not None:
            self.modify_time = modify_time
        self.templating = templating
        self.template_version = template_version

    @property
    def alarm_rule_template_name(self):
        r"""Gets the alarm_rule_template_name of this AlarmRuleTemplateBody.

        告警模板名称。

        :return: The alarm_rule_template_name of this AlarmRuleTemplateBody.
        :rtype: str
        """
        return self._alarm_rule_template_name

    @alarm_rule_template_name.setter
    def alarm_rule_template_name(self, alarm_rule_template_name):
        r"""Sets the alarm_rule_template_name of this AlarmRuleTemplateBody.

        告警模板名称。

        :param alarm_rule_template_name: The alarm_rule_template_name of this AlarmRuleTemplateBody.
        :type alarm_rule_template_name: str
        """
        self._alarm_rule_template_name = alarm_rule_template_name

    @property
    def alarm_rule_template_name_en(self):
        r"""Gets the alarm_rule_template_name_en of this AlarmRuleTemplateBody.

        告警模板英文名称。

        :return: The alarm_rule_template_name_en of this AlarmRuleTemplateBody.
        :rtype: str
        """
        return self._alarm_rule_template_name_en

    @alarm_rule_template_name_en.setter
    def alarm_rule_template_name_en(self, alarm_rule_template_name_en):
        r"""Sets the alarm_rule_template_name_en of this AlarmRuleTemplateBody.

        告警模板英文名称。

        :param alarm_rule_template_name_en: The alarm_rule_template_name_en of this AlarmRuleTemplateBody.
        :type alarm_rule_template_name_en: str
        """
        self._alarm_rule_template_name_en = alarm_rule_template_name_en

    @property
    def alarm_rule_template_description(self):
        r"""Gets the alarm_rule_template_description of this AlarmRuleTemplateBody.

        告警模板描述。

        :return: The alarm_rule_template_description of this AlarmRuleTemplateBody.
        :rtype: str
        """
        return self._alarm_rule_template_description

    @alarm_rule_template_description.setter
    def alarm_rule_template_description(self, alarm_rule_template_description):
        r"""Sets the alarm_rule_template_description of this AlarmRuleTemplateBody.

        告警模板描述。

        :param alarm_rule_template_description: The alarm_rule_template_description of this AlarmRuleTemplateBody.
        :type alarm_rule_template_description: str
        """
        self._alarm_rule_template_description = alarm_rule_template_description

    @property
    def alarm_rule_template_id(self):
        r"""Gets the alarm_rule_template_id of this AlarmRuleTemplateBody.

        告警模板id。

        :return: The alarm_rule_template_id of this AlarmRuleTemplateBody.
        :rtype: str
        """
        return self._alarm_rule_template_id

    @alarm_rule_template_id.setter
    def alarm_rule_template_id(self, alarm_rule_template_id):
        r"""Sets the alarm_rule_template_id of this AlarmRuleTemplateBody.

        告警模板id。

        :param alarm_rule_template_id: The alarm_rule_template_id of this AlarmRuleTemplateBody.
        :type alarm_rule_template_id: str
        """
        self._alarm_rule_template_id = alarm_rule_template_id

    @property
    def alarm_rule_template_project_id(self):
        r"""Gets the alarm_rule_template_project_id of this AlarmRuleTemplateBody.

        项目ID，可以从控制台获取，也可以从调用API处获取。获取方式请参见：[获取项目ID](aom_04_0024.xml)。

        :return: The alarm_rule_template_project_id of this AlarmRuleTemplateBody.
        :rtype: str
        """
        return self._alarm_rule_template_project_id

    @alarm_rule_template_project_id.setter
    def alarm_rule_template_project_id(self, alarm_rule_template_project_id):
        r"""Sets the alarm_rule_template_project_id of this AlarmRuleTemplateBody.

        项目ID，可以从控制台获取，也可以从调用API处获取。获取方式请参见：[获取项目ID](aom_04_0024.xml)。

        :param alarm_rule_template_project_id: The alarm_rule_template_project_id of this AlarmRuleTemplateBody.
        :type alarm_rule_template_project_id: str
        """
        self._alarm_rule_template_project_id = alarm_rule_template_project_id

    @property
    def alarm_rule_template_type(self):
        r"""Gets the alarm_rule_template_type of this AlarmRuleTemplateBody.

        告警模板类型 - “statics”：静态告警模板 - “dynamic”：动态告警模板

        :return: The alarm_rule_template_type of this AlarmRuleTemplateBody.
        :rtype: str
        """
        return self._alarm_rule_template_type

    @alarm_rule_template_type.setter
    def alarm_rule_template_type(self, alarm_rule_template_type):
        r"""Sets the alarm_rule_template_type of this AlarmRuleTemplateBody.

        告警模板类型 - “statics”：静态告警模板 - “dynamic”：动态告警模板

        :param alarm_rule_template_type: The alarm_rule_template_type of this AlarmRuleTemplateBody.
        :type alarm_rule_template_type: str
        """
        self._alarm_rule_template_type = alarm_rule_template_type

    @property
    def alarm_rule_template_source(self):
        r"""Gets the alarm_rule_template_source of this AlarmRuleTemplateBody.

        告警模板来源。

        :return: The alarm_rule_template_source of this AlarmRuleTemplateBody.
        :rtype: str
        """
        return self._alarm_rule_template_source

    @alarm_rule_template_source.setter
    def alarm_rule_template_source(self, alarm_rule_template_source):
        r"""Sets the alarm_rule_template_source of this AlarmRuleTemplateBody.

        告警模板来源。

        :param alarm_rule_template_source: The alarm_rule_template_source of this AlarmRuleTemplateBody.
        :type alarm_rule_template_source: str
        """
        self._alarm_rule_template_source = alarm_rule_template_source

    @property
    def alarm_rule_template_binding(self):
        r"""Gets the alarm_rule_template_binding of this AlarmRuleTemplateBody.

        告警模板所绑定的告警规则。

        :return: The alarm_rule_template_binding of this AlarmRuleTemplateBody.
        :rtype: dict(str, str)
        """
        return self._alarm_rule_template_binding

    @alarm_rule_template_binding.setter
    def alarm_rule_template_binding(self, alarm_rule_template_binding):
        r"""Sets the alarm_rule_template_binding of this AlarmRuleTemplateBody.

        告警模板所绑定的告警规则。

        :param alarm_rule_template_binding: The alarm_rule_template_binding of this AlarmRuleTemplateBody.
        :type alarm_rule_template_binding: dict(str, str)
        """
        self._alarm_rule_template_binding = alarm_rule_template_binding

    @property
    def alarm_template_spec_list(self):
        r"""Gets the alarm_template_spec_list of this AlarmRuleTemplateBody.

        告警模板列表。

        :return: The alarm_template_spec_list of this AlarmRuleTemplateBody.
        :rtype: list[:class:`huaweicloudsdkaom.v2.AlarmRuleTemplateSpecWithCloudService`]
        """
        return self._alarm_template_spec_list

    @alarm_template_spec_list.setter
    def alarm_template_spec_list(self, alarm_template_spec_list):
        r"""Sets the alarm_template_spec_list of this AlarmRuleTemplateBody.

        告警模板列表。

        :param alarm_template_spec_list: The alarm_template_spec_list of this AlarmRuleTemplateBody.
        :type alarm_template_spec_list: list[:class:`huaweicloudsdkaom.v2.AlarmRuleTemplateSpecWithCloudService`]
        """
        self._alarm_template_spec_list = alarm_template_spec_list

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this AlarmRuleTemplateBody.

        企业项目id。获取方式请参见：[获取企业项目ID](aom_04_0024.xml)。

        :return: The enterprise_project_id of this AlarmRuleTemplateBody.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this AlarmRuleTemplateBody.

        企业项目id。获取方式请参见：[获取企业项目ID](aom_04_0024.xml)。

        :param enterprise_project_id: The enterprise_project_id of this AlarmRuleTemplateBody.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def create_time(self):
        r"""Gets the create_time of this AlarmRuleTemplateBody.

        创建时间。

        :return: The create_time of this AlarmRuleTemplateBody.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this AlarmRuleTemplateBody.

        创建时间。

        :param create_time: The create_time of this AlarmRuleTemplateBody.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def modify_time(self):
        r"""Gets the modify_time of this AlarmRuleTemplateBody.

        更新时间。

        :return: The modify_time of this AlarmRuleTemplateBody.
        :rtype: int
        """
        return self._modify_time

    @modify_time.setter
    def modify_time(self, modify_time):
        r"""Sets the modify_time of this AlarmRuleTemplateBody.

        更新时间。

        :param modify_time: The modify_time of this AlarmRuleTemplateBody.
        :type modify_time: int
        """
        self._modify_time = modify_time

    @property
    def templating(self):
        r"""Gets the templating of this AlarmRuleTemplateBody.

        :return: The templating of this AlarmRuleTemplateBody.
        :rtype: :class:`huaweicloudsdkaom.v2.Templating`
        """
        return self._templating

    @templating.setter
    def templating(self, templating):
        r"""Sets the templating of this AlarmRuleTemplateBody.

        :param templating: The templating of this AlarmRuleTemplateBody.
        :type templating: :class:`huaweicloudsdkaom.v2.Templating`
        """
        self._templating = templating

    @property
    def template_version(self):
        r"""Gets the template_version of this AlarmRuleTemplateBody.

        告警模板版本。

        :return: The template_version of this AlarmRuleTemplateBody.
        :rtype: str
        """
        return self._template_version

    @template_version.setter
    def template_version(self, template_version):
        r"""Sets the template_version of this AlarmRuleTemplateBody.

        告警模板版本。

        :param template_version: The template_version of this AlarmRuleTemplateBody.
        :type template_version: str
        """
        self._template_version = template_version

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
        if not isinstance(other, AlarmRuleTemplateBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
