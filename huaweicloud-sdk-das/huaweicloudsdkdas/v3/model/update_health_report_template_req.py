# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateHealthReportTemplateReq:

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
        'description': 'str',
        'chapters_config': 'dict(str, ChapterConfigReq)'
    }

    attribute_map = {
        'template_name': 'template_name',
        'description': 'description',
        'chapters_config': 'chapters_config'
    }

    def __init__(self, template_name=None, description=None, chapters_config=None):
        r"""UpdateHealthReportTemplateReq

        The model defined in huaweicloud sdk

        :param template_name: 模板名称。
        :type template_name: str
        :param description: 模板描述。
        :type description: str
        :param chapters_config: 章节配置，key为章节编码，value为章节配置对象。采用全量更新语义。
        :type chapters_config: dict(str, ChapterConfigReq)
        """
        
        

        self._template_name = None
        self._description = None
        self._chapters_config = None
        self.discriminator = None

        self.template_name = template_name
        if description is not None:
            self.description = description
        self.chapters_config = chapters_config

    @property
    def template_name(self):
        r"""Gets the template_name of this UpdateHealthReportTemplateReq.

        模板名称。

        :return: The template_name of this UpdateHealthReportTemplateReq.
        :rtype: str
        """
        return self._template_name

    @template_name.setter
    def template_name(self, template_name):
        r"""Sets the template_name of this UpdateHealthReportTemplateReq.

        模板名称。

        :param template_name: The template_name of this UpdateHealthReportTemplateReq.
        :type template_name: str
        """
        self._template_name = template_name

    @property
    def description(self):
        r"""Gets the description of this UpdateHealthReportTemplateReq.

        模板描述。

        :return: The description of this UpdateHealthReportTemplateReq.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this UpdateHealthReportTemplateReq.

        模板描述。

        :param description: The description of this UpdateHealthReportTemplateReq.
        :type description: str
        """
        self._description = description

    @property
    def chapters_config(self):
        r"""Gets the chapters_config of this UpdateHealthReportTemplateReq.

        章节配置，key为章节编码，value为章节配置对象。采用全量更新语义。

        :return: The chapters_config of this UpdateHealthReportTemplateReq.
        :rtype: dict(str, ChapterConfigReq)
        """
        return self._chapters_config

    @chapters_config.setter
    def chapters_config(self, chapters_config):
        r"""Sets the chapters_config of this UpdateHealthReportTemplateReq.

        章节配置，key为章节编码，value为章节配置对象。采用全量更新语义。

        :param chapters_config: The chapters_config of this UpdateHealthReportTemplateReq.
        :type chapters_config: dict(str, ChapterConfigReq)
        """
        self._chapters_config = chapters_config

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
        if not isinstance(other, UpdateHealthReportTemplateReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
