# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StructTemplateModel:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'project_id': 'str',
        'template_name': 'str',
        'template_type': 'str',
        'demo_log': 'str',
        'demo_fields': 'list[DemoField]',
        'tag_fields': 'list[TagFieldNew]',
        'rule': 'TemplateRule',
        'demo_label': 'str',
        'create_time': 'int',
        'id': 'str'
    }

    attribute_map = {
        'project_id': 'project_id',
        'template_name': 'template_name',
        'template_type': 'template_type',
        'demo_log': 'demo_log',
        'demo_fields': 'demo_fields',
        'tag_fields': 'tag_fields',
        'rule': 'rule',
        'demo_label': 'demo_label',
        'create_time': 'create_time',
        'id': 'id'
    }

    def __init__(self, project_id=None, template_name=None, template_type=None, demo_log=None, demo_fields=None, tag_fields=None, rule=None, demo_label=None, create_time=None, id=None):
        r"""StructTemplateModel

        The model defined in huaweicloud sdk

        :param project_id: 项目id
        :type project_id: str
        :param template_name: 模板名称
        :type template_name: str
        :param template_type: 模板类型，regex,json,split,nginx
        :type template_type: str
        :param demo_log: 示例日志
        :type demo_log: str
        :param demo_fields: 示例字段数组
        :type demo_fields: list[:class:`huaweicloudsdklts.v2.DemoField`]
        :param tag_fields: Tag字段数组
        :type tag_fields: list[:class:`huaweicloudsdklts.v2.TagFieldNew`]
        :param rule: 
        :type rule: :class:`huaweicloudsdklts.v2.TemplateRule`
        :param demo_label: 示例日志标签
        :type demo_label: str
        :param create_time: 创建时间
        :type create_time: int
        :param id: 模板id
        :type id: str
        """
        
        

        self._project_id = None
        self._template_name = None
        self._template_type = None
        self._demo_log = None
        self._demo_fields = None
        self._tag_fields = None
        self._rule = None
        self._demo_label = None
        self._create_time = None
        self._id = None
        self.discriminator = None

        self.project_id = project_id
        self.template_name = template_name
        self.template_type = template_type
        self.demo_log = demo_log
        self.demo_fields = demo_fields
        self.tag_fields = tag_fields
        self.rule = rule
        if demo_label is not None:
            self.demo_label = demo_label
        if create_time is not None:
            self.create_time = create_time
        if id is not None:
            self.id = id

    @property
    def project_id(self):
        r"""Gets the project_id of this StructTemplateModel.

        项目id

        :return: The project_id of this StructTemplateModel.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this StructTemplateModel.

        项目id

        :param project_id: The project_id of this StructTemplateModel.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def template_name(self):
        r"""Gets the template_name of this StructTemplateModel.

        模板名称

        :return: The template_name of this StructTemplateModel.
        :rtype: str
        """
        return self._template_name

    @template_name.setter
    def template_name(self, template_name):
        r"""Sets the template_name of this StructTemplateModel.

        模板名称

        :param template_name: The template_name of this StructTemplateModel.
        :type template_name: str
        """
        self._template_name = template_name

    @property
    def template_type(self):
        r"""Gets the template_type of this StructTemplateModel.

        模板类型，regex,json,split,nginx

        :return: The template_type of this StructTemplateModel.
        :rtype: str
        """
        return self._template_type

    @template_type.setter
    def template_type(self, template_type):
        r"""Sets the template_type of this StructTemplateModel.

        模板类型，regex,json,split,nginx

        :param template_type: The template_type of this StructTemplateModel.
        :type template_type: str
        """
        self._template_type = template_type

    @property
    def demo_log(self):
        r"""Gets the demo_log of this StructTemplateModel.

        示例日志

        :return: The demo_log of this StructTemplateModel.
        :rtype: str
        """
        return self._demo_log

    @demo_log.setter
    def demo_log(self, demo_log):
        r"""Sets the demo_log of this StructTemplateModel.

        示例日志

        :param demo_log: The demo_log of this StructTemplateModel.
        :type demo_log: str
        """
        self._demo_log = demo_log

    @property
    def demo_fields(self):
        r"""Gets the demo_fields of this StructTemplateModel.

        示例字段数组

        :return: The demo_fields of this StructTemplateModel.
        :rtype: list[:class:`huaweicloudsdklts.v2.DemoField`]
        """
        return self._demo_fields

    @demo_fields.setter
    def demo_fields(self, demo_fields):
        r"""Sets the demo_fields of this StructTemplateModel.

        示例字段数组

        :param demo_fields: The demo_fields of this StructTemplateModel.
        :type demo_fields: list[:class:`huaweicloudsdklts.v2.DemoField`]
        """
        self._demo_fields = demo_fields

    @property
    def tag_fields(self):
        r"""Gets the tag_fields of this StructTemplateModel.

        Tag字段数组

        :return: The tag_fields of this StructTemplateModel.
        :rtype: list[:class:`huaweicloudsdklts.v2.TagFieldNew`]
        """
        return self._tag_fields

    @tag_fields.setter
    def tag_fields(self, tag_fields):
        r"""Sets the tag_fields of this StructTemplateModel.

        Tag字段数组

        :param tag_fields: The tag_fields of this StructTemplateModel.
        :type tag_fields: list[:class:`huaweicloudsdklts.v2.TagFieldNew`]
        """
        self._tag_fields = tag_fields

    @property
    def rule(self):
        r"""Gets the rule of this StructTemplateModel.

        :return: The rule of this StructTemplateModel.
        :rtype: :class:`huaweicloudsdklts.v2.TemplateRule`
        """
        return self._rule

    @rule.setter
    def rule(self, rule):
        r"""Sets the rule of this StructTemplateModel.

        :param rule: The rule of this StructTemplateModel.
        :type rule: :class:`huaweicloudsdklts.v2.TemplateRule`
        """
        self._rule = rule

    @property
    def demo_label(self):
        r"""Gets the demo_label of this StructTemplateModel.

        示例日志标签

        :return: The demo_label of this StructTemplateModel.
        :rtype: str
        """
        return self._demo_label

    @demo_label.setter
    def demo_label(self, demo_label):
        r"""Sets the demo_label of this StructTemplateModel.

        示例日志标签

        :param demo_label: The demo_label of this StructTemplateModel.
        :type demo_label: str
        """
        self._demo_label = demo_label

    @property
    def create_time(self):
        r"""Gets the create_time of this StructTemplateModel.

        创建时间

        :return: The create_time of this StructTemplateModel.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this StructTemplateModel.

        创建时间

        :param create_time: The create_time of this StructTemplateModel.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def id(self):
        r"""Gets the id of this StructTemplateModel.

        模板id

        :return: The id of this StructTemplateModel.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this StructTemplateModel.

        模板id

        :param id: The id of this StructTemplateModel.
        :type id: str
        """
        self._id = id

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
        if not isinstance(other, StructTemplateModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
