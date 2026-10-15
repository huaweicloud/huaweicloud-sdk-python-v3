# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HealthReportTemplateDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'template_id': 'int',
        'template_name': 'str',
        'description': 'str',
        'system': 'bool',
        'chapters_config': 'dict(str, ChapterConfig)',
        'create_at': 'int',
        'update_at': 'int'
    }

    attribute_map = {
        'template_id': 'template_id',
        'template_name': 'template_name',
        'description': 'description',
        'system': 'system',
        'chapters_config': 'chapters_config',
        'create_at': 'create_at',
        'update_at': 'update_at'
    }

    def __init__(self, template_id=None, template_name=None, description=None, system=None, chapters_config=None, create_at=None, update_at=None):
        r"""HealthReportTemplateDto

        The model defined in huaweicloud sdk

        :param template_id: 模板ID。
        :type template_id: int
        :param template_name: 模板名称。
        :type template_name: str
        :param description: 模板描述。
        :type description: str
        :param system: 是否为系统预设模板（true-系统模板 false-自定义模板）。
        :type system: bool
        :param chapters_config: 章节配置，key为章节编码，value为章节配置对象。
        :type chapters_config: dict(str, ChapterConfig)
        :param create_at: 创建时间（Unix timestamp），单位：毫秒。
        :type create_at: int
        :param update_at: 更新时间（Unix timestamp），单位：毫秒。
        :type update_at: int
        """
        
        

        self._template_id = None
        self._template_name = None
        self._description = None
        self._system = None
        self._chapters_config = None
        self._create_at = None
        self._update_at = None
        self.discriminator = None

        self.template_id = template_id
        self.template_name = template_name
        if description is not None:
            self.description = description
        self.system = system
        self.chapters_config = chapters_config
        self.create_at = create_at
        self.update_at = update_at

    @property
    def template_id(self):
        r"""Gets the template_id of this HealthReportTemplateDto.

        模板ID。

        :return: The template_id of this HealthReportTemplateDto.
        :rtype: int
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        r"""Sets the template_id of this HealthReportTemplateDto.

        模板ID。

        :param template_id: The template_id of this HealthReportTemplateDto.
        :type template_id: int
        """
        self._template_id = template_id

    @property
    def template_name(self):
        r"""Gets the template_name of this HealthReportTemplateDto.

        模板名称。

        :return: The template_name of this HealthReportTemplateDto.
        :rtype: str
        """
        return self._template_name

    @template_name.setter
    def template_name(self, template_name):
        r"""Sets the template_name of this HealthReportTemplateDto.

        模板名称。

        :param template_name: The template_name of this HealthReportTemplateDto.
        :type template_name: str
        """
        self._template_name = template_name

    @property
    def description(self):
        r"""Gets the description of this HealthReportTemplateDto.

        模板描述。

        :return: The description of this HealthReportTemplateDto.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this HealthReportTemplateDto.

        模板描述。

        :param description: The description of this HealthReportTemplateDto.
        :type description: str
        """
        self._description = description

    @property
    def system(self):
        r"""Gets the system of this HealthReportTemplateDto.

        是否为系统预设模板（true-系统模板 false-自定义模板）。

        :return: The system of this HealthReportTemplateDto.
        :rtype: bool
        """
        return self._system

    @system.setter
    def system(self, system):
        r"""Sets the system of this HealthReportTemplateDto.

        是否为系统预设模板（true-系统模板 false-自定义模板）。

        :param system: The system of this HealthReportTemplateDto.
        :type system: bool
        """
        self._system = system

    @property
    def chapters_config(self):
        r"""Gets the chapters_config of this HealthReportTemplateDto.

        章节配置，key为章节编码，value为章节配置对象。

        :return: The chapters_config of this HealthReportTemplateDto.
        :rtype: dict(str, ChapterConfig)
        """
        return self._chapters_config

    @chapters_config.setter
    def chapters_config(self, chapters_config):
        r"""Sets the chapters_config of this HealthReportTemplateDto.

        章节配置，key为章节编码，value为章节配置对象。

        :param chapters_config: The chapters_config of this HealthReportTemplateDto.
        :type chapters_config: dict(str, ChapterConfig)
        """
        self._chapters_config = chapters_config

    @property
    def create_at(self):
        r"""Gets the create_at of this HealthReportTemplateDto.

        创建时间（Unix timestamp），单位：毫秒。

        :return: The create_at of this HealthReportTemplateDto.
        :rtype: int
        """
        return self._create_at

    @create_at.setter
    def create_at(self, create_at):
        r"""Sets the create_at of this HealthReportTemplateDto.

        创建时间（Unix timestamp），单位：毫秒。

        :param create_at: The create_at of this HealthReportTemplateDto.
        :type create_at: int
        """
        self._create_at = create_at

    @property
    def update_at(self):
        r"""Gets the update_at of this HealthReportTemplateDto.

        更新时间（Unix timestamp），单位：毫秒。

        :return: The update_at of this HealthReportTemplateDto.
        :rtype: int
        """
        return self._update_at

    @update_at.setter
    def update_at(self, update_at):
        r"""Sets the update_at of this HealthReportTemplateDto.

        更新时间（Unix timestamp），单位：毫秒。

        :param update_at: The update_at of this HealthReportTemplateDto.
        :type update_at: int
        """
        self._update_at = update_at

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
        if not isinstance(other, HealthReportTemplateDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
