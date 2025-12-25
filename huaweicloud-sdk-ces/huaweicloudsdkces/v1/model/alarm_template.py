# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AlarmTemplate:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'template_name': 'str',
        'template_description': 'str',
        'namespace': 'str',
        'dimension_name': 'str',
        'template_items': 'list[TemplateItem]',
        'template_id': 'str'
    }

    attribute_map = {
        'template_name': 'template_name',
        'template_description': 'template_description',
        'namespace': 'namespace',
        'dimension_name': 'dimension_name',
        'template_items': 'template_items',
        'template_id': 'template_id'
    }

    def __init__(self, template_name=None, template_description=None, namespace=None, dimension_name=None, template_items=None, template_id=None):
        r"""AlarmTemplate

        The model defined in huaweicloud sdk

        :param template_name: **参数解释**： 自定义告警模板名称 **约束限制**： 不涉及。 **取值范围**： 以字母或汉字开头，可包含字母、数字、汉字、_、-，长度为[1,256]个字符，如：alarmTemplate-Test01。        **默认取值**： 不涉及。 
        :type template_name: str
        :param template_description: **参数解释**： 自定义告警模板描述。    **约束限制**： 不涉及。 **取值范围**： 长度范围[0,256]。          **默认取值**： 空字符串。 
        :type template_description: str
        :param namespace: **参数解释** 创建自定义告警模板选择的资源类型，即服务命名空间，如：选择弹性云服务器，则命名空间为SYS.ECS；各服务的命名空间可查看：“[服务命名空间](ces_03_0059.xml)”。 **约束限制**： 不涉及 **取值范围**： 格式为service.item；service和item必须是字符串，必须以字母开头，只能包含0-9/a-z/A-Z/_。字符串的长度必须在 3 到 32个字符之间。 **默认取值**： 不涉及 
        :type namespace: str
        :param dimension_name: **参数解释** 资源类型对应的指标监控维度，选择弹性云服务器，则维度为云服务器，dimension_name值为instance_id；各服务资源的指标维度名称可查看：“[服务指标维度](ces_03_0059.xml)”。 **约束限制**： 不涉及 **取值范围**： 必须以字母开头，多维度用\&quot;,\&quot;分隔，只能包含0-9/a-z/A-Z/_/-，每个维度的最大长度为32。目前最大支持4个维度。字符串总最大长度为131。举例：单维度场景：instance_id；多维度场景：instance_id,disk        **默认取值**： 不涉及 
        :type dimension_name: str
        :param template_items: 自定义告警模板添加的一组或者多个告警策略。
        :type template_items: list[:class:`huaweicloudsdkces.v1.TemplateItem`]
        :param template_id: **参数解释** 自定义告警模版的ID，如：at1603330892378wkDm77y6B **约束限制**： 不涉及 **取值范围**： 以at开头，后跟字母、数字，长度最长为64 **默认取值**： 不涉及 
        :type template_id: str
        """
        
        

        self._template_name = None
        self._template_description = None
        self._namespace = None
        self._dimension_name = None
        self._template_items = None
        self._template_id = None
        self.discriminator = None

        if template_name is not None:
            self.template_name = template_name
        if template_description is not None:
            self.template_description = template_description
        if namespace is not None:
            self.namespace = namespace
        if dimension_name is not None:
            self.dimension_name = dimension_name
        if template_items is not None:
            self.template_items = template_items
        if template_id is not None:
            self.template_id = template_id

    @property
    def template_name(self):
        r"""Gets the template_name of this AlarmTemplate.

        **参数解释**： 自定义告警模板名称 **约束限制**： 不涉及。 **取值范围**： 以字母或汉字开头，可包含字母、数字、汉字、_、-，长度为[1,256]个字符，如：alarmTemplate-Test01。        **默认取值**： 不涉及。 

        :return: The template_name of this AlarmTemplate.
        :rtype: str
        """
        return self._template_name

    @template_name.setter
    def template_name(self, template_name):
        r"""Sets the template_name of this AlarmTemplate.

        **参数解释**： 自定义告警模板名称 **约束限制**： 不涉及。 **取值范围**： 以字母或汉字开头，可包含字母、数字、汉字、_、-，长度为[1,256]个字符，如：alarmTemplate-Test01。        **默认取值**： 不涉及。 

        :param template_name: The template_name of this AlarmTemplate.
        :type template_name: str
        """
        self._template_name = template_name

    @property
    def template_description(self):
        r"""Gets the template_description of this AlarmTemplate.

        **参数解释**： 自定义告警模板描述。    **约束限制**： 不涉及。 **取值范围**： 长度范围[0,256]。          **默认取值**： 空字符串。 

        :return: The template_description of this AlarmTemplate.
        :rtype: str
        """
        return self._template_description

    @template_description.setter
    def template_description(self, template_description):
        r"""Sets the template_description of this AlarmTemplate.

        **参数解释**： 自定义告警模板描述。    **约束限制**： 不涉及。 **取值范围**： 长度范围[0,256]。          **默认取值**： 空字符串。 

        :param template_description: The template_description of this AlarmTemplate.
        :type template_description: str
        """
        self._template_description = template_description

    @property
    def namespace(self):
        r"""Gets the namespace of this AlarmTemplate.

        **参数解释** 创建自定义告警模板选择的资源类型，即服务命名空间，如：选择弹性云服务器，则命名空间为SYS.ECS；各服务的命名空间可查看：“[服务命名空间](ces_03_0059.xml)”。 **约束限制**： 不涉及 **取值范围**： 格式为service.item；service和item必须是字符串，必须以字母开头，只能包含0-9/a-z/A-Z/_。字符串的长度必须在 3 到 32个字符之间。 **默认取值**： 不涉及 

        :return: The namespace of this AlarmTemplate.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        r"""Sets the namespace of this AlarmTemplate.

        **参数解释** 创建自定义告警模板选择的资源类型，即服务命名空间，如：选择弹性云服务器，则命名空间为SYS.ECS；各服务的命名空间可查看：“[服务命名空间](ces_03_0059.xml)”。 **约束限制**： 不涉及 **取值范围**： 格式为service.item；service和item必须是字符串，必须以字母开头，只能包含0-9/a-z/A-Z/_。字符串的长度必须在 3 到 32个字符之间。 **默认取值**： 不涉及 

        :param namespace: The namespace of this AlarmTemplate.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def dimension_name(self):
        r"""Gets the dimension_name of this AlarmTemplate.

        **参数解释** 资源类型对应的指标监控维度，选择弹性云服务器，则维度为云服务器，dimension_name值为instance_id；各服务资源的指标维度名称可查看：“[服务指标维度](ces_03_0059.xml)”。 **约束限制**： 不涉及 **取值范围**： 必须以字母开头，多维度用\",\"分隔，只能包含0-9/a-z/A-Z/_/-，每个维度的最大长度为32。目前最大支持4个维度。字符串总最大长度为131。举例：单维度场景：instance_id；多维度场景：instance_id,disk        **默认取值**： 不涉及 

        :return: The dimension_name of this AlarmTemplate.
        :rtype: str
        """
        return self._dimension_name

    @dimension_name.setter
    def dimension_name(self, dimension_name):
        r"""Sets the dimension_name of this AlarmTemplate.

        **参数解释** 资源类型对应的指标监控维度，选择弹性云服务器，则维度为云服务器，dimension_name值为instance_id；各服务资源的指标维度名称可查看：“[服务指标维度](ces_03_0059.xml)”。 **约束限制**： 不涉及 **取值范围**： 必须以字母开头，多维度用\",\"分隔，只能包含0-9/a-z/A-Z/_/-，每个维度的最大长度为32。目前最大支持4个维度。字符串总最大长度为131。举例：单维度场景：instance_id；多维度场景：instance_id,disk        **默认取值**： 不涉及 

        :param dimension_name: The dimension_name of this AlarmTemplate.
        :type dimension_name: str
        """
        self._dimension_name = dimension_name

    @property
    def template_items(self):
        r"""Gets the template_items of this AlarmTemplate.

        自定义告警模板添加的一组或者多个告警策略。

        :return: The template_items of this AlarmTemplate.
        :rtype: list[:class:`huaweicloudsdkces.v1.TemplateItem`]
        """
        return self._template_items

    @template_items.setter
    def template_items(self, template_items):
        r"""Sets the template_items of this AlarmTemplate.

        自定义告警模板添加的一组或者多个告警策略。

        :param template_items: The template_items of this AlarmTemplate.
        :type template_items: list[:class:`huaweicloudsdkces.v1.TemplateItem`]
        """
        self._template_items = template_items

    @property
    def template_id(self):
        r"""Gets the template_id of this AlarmTemplate.

        **参数解释** 自定义告警模版的ID，如：at1603330892378wkDm77y6B **约束限制**： 不涉及 **取值范围**： 以at开头，后跟字母、数字，长度最长为64 **默认取值**： 不涉及 

        :return: The template_id of this AlarmTemplate.
        :rtype: str
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        r"""Sets the template_id of this AlarmTemplate.

        **参数解释** 自定义告警模版的ID，如：at1603330892378wkDm77y6B **约束限制**： 不涉及 **取值范围**： 以at开头，后跟字母、数字，长度最长为64 **默认取值**： 不涉及 

        :param template_id: The template_id of this AlarmTemplate.
        :type template_id: str
        """
        self._template_id = template_id

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
        if not isinstance(other, AlarmTemplate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
