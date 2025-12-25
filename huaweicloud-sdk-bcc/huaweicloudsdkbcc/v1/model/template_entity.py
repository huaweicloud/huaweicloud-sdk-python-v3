# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TemplateEntity:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'template_id': 'str',
        'template_name': 'str',
        'template_type': 'str',
        'create_time': 'str',
        'last_update_time': 'str',
        'template_contents': 'list[str]'
    }

    attribute_map = {
        'template_id': 'template_id',
        'template_name': 'template_name',
        'template_type': 'template_type',
        'create_time': 'create_time',
        'last_update_time': 'last_update_time',
        'template_contents': 'template_contents'
    }

    def __init__(self, template_id=None, template_name=None, template_type=None, create_time=None, last_update_time=None, template_contents=None):
        r"""TemplateEntity

        The model defined in huaweicloud sdk

        :param template_id: 模板ID
        :type template_id: str
        :param template_name: 模板名称
        :type template_name: str
        :param template_type: 模板类型枚举
        :type template_type: str
        :param create_time: 模板创建时间
        :type create_time: str
        :param last_update_time: 最后更新时间
        :type last_update_time: str
        :param template_contents: 模板具体的内容项，例如：存储库-使用率，存储库-摘要，任务-趋势，任务-摘要，任务-详情
        :type template_contents: list[str]
        """
        
        

        self._template_id = None
        self._template_name = None
        self._template_type = None
        self._create_time = None
        self._last_update_time = None
        self._template_contents = None
        self.discriminator = None

        self.template_id = template_id
        self.template_name = template_name
        self.template_type = template_type
        self.create_time = create_time
        self.last_update_time = last_update_time
        self.template_contents = template_contents

    @property
    def template_id(self):
        r"""Gets the template_id of this TemplateEntity.

        模板ID

        :return: The template_id of this TemplateEntity.
        :rtype: str
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        r"""Sets the template_id of this TemplateEntity.

        模板ID

        :param template_id: The template_id of this TemplateEntity.
        :type template_id: str
        """
        self._template_id = template_id

    @property
    def template_name(self):
        r"""Gets the template_name of this TemplateEntity.

        模板名称

        :return: The template_name of this TemplateEntity.
        :rtype: str
        """
        return self._template_name

    @template_name.setter
    def template_name(self, template_name):
        r"""Sets the template_name of this TemplateEntity.

        模板名称

        :param template_name: The template_name of this TemplateEntity.
        :type template_name: str
        """
        self._template_name = template_name

    @property
    def template_type(self):
        r"""Gets the template_type of this TemplateEntity.

        模板类型枚举

        :return: The template_type of this TemplateEntity.
        :rtype: str
        """
        return self._template_type

    @template_type.setter
    def template_type(self, template_type):
        r"""Sets the template_type of this TemplateEntity.

        模板类型枚举

        :param template_type: The template_type of this TemplateEntity.
        :type template_type: str
        """
        self._template_type = template_type

    @property
    def create_time(self):
        r"""Gets the create_time of this TemplateEntity.

        模板创建时间

        :return: The create_time of this TemplateEntity.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this TemplateEntity.

        模板创建时间

        :param create_time: The create_time of this TemplateEntity.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def last_update_time(self):
        r"""Gets the last_update_time of this TemplateEntity.

        最后更新时间

        :return: The last_update_time of this TemplateEntity.
        :rtype: str
        """
        return self._last_update_time

    @last_update_time.setter
    def last_update_time(self, last_update_time):
        r"""Sets the last_update_time of this TemplateEntity.

        最后更新时间

        :param last_update_time: The last_update_time of this TemplateEntity.
        :type last_update_time: str
        """
        self._last_update_time = last_update_time

    @property
    def template_contents(self):
        r"""Gets the template_contents of this TemplateEntity.

        模板具体的内容项，例如：存储库-使用率，存储库-摘要，任务-趋势，任务-摘要，任务-详情

        :return: The template_contents of this TemplateEntity.
        :rtype: list[str]
        """
        return self._template_contents

    @template_contents.setter
    def template_contents(self, template_contents):
        r"""Sets the template_contents of this TemplateEntity.

        模板具体的内容项，例如：存储库-使用率，存储库-摘要，任务-趋势，任务-摘要，任务-详情

        :param template_contents: The template_contents of this TemplateEntity.
        :type template_contents: list[str]
        """
        self._template_contents = template_contents

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
        if not isinstance(other, TemplateEntity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
