# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ReportEntity:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'report_id': 'str',
        'report_name': 'str',
        'report_generated_time': 'str',
        'report_setting_id': 'str',
        'report_setting_name': 'str',
        'report_template': 'str',
        'report_template_id': 'str'
    }

    attribute_map = {
        'report_id': 'report_id',
        'report_name': 'report_name',
        'report_generated_time': 'report_generated_time',
        'report_setting_id': 'report_setting_id',
        'report_setting_name': 'report_setting_name',
        'report_template': 'report_template',
        'report_template_id': 'report_template_id'
    }

    def __init__(self, report_id=None, report_name=None, report_generated_time=None, report_setting_id=None, report_setting_name=None, report_template=None, report_template_id=None):
        r"""ReportEntity

        The model defined in huaweicloud sdk

        :param report_id: 报告ID
        :type report_id: str
        :param report_name: 报告名称
        :type report_name: str
        :param report_generated_time: 报告生成时间
        :type report_generated_time: str
        :param report_setting_id: 报告配置ID
        :type report_setting_id: str
        :param report_setting_name: 报告配置名称
        :type report_setting_name: str
        :param report_template: 报告模板名称
        :type report_template: str
        :param report_template_id: 报告模板ID
        :type report_template_id: str
        """
        
        

        self._report_id = None
        self._report_name = None
        self._report_generated_time = None
        self._report_setting_id = None
        self._report_setting_name = None
        self._report_template = None
        self._report_template_id = None
        self.discriminator = None

        self.report_id = report_id
        self.report_name = report_name
        self.report_generated_time = report_generated_time
        self.report_setting_id = report_setting_id
        self.report_setting_name = report_setting_name
        self.report_template = report_template
        self.report_template_id = report_template_id

    @property
    def report_id(self):
        r"""Gets the report_id of this ReportEntity.

        报告ID

        :return: The report_id of this ReportEntity.
        :rtype: str
        """
        return self._report_id

    @report_id.setter
    def report_id(self, report_id):
        r"""Sets the report_id of this ReportEntity.

        报告ID

        :param report_id: The report_id of this ReportEntity.
        :type report_id: str
        """
        self._report_id = report_id

    @property
    def report_name(self):
        r"""Gets the report_name of this ReportEntity.

        报告名称

        :return: The report_name of this ReportEntity.
        :rtype: str
        """
        return self._report_name

    @report_name.setter
    def report_name(self, report_name):
        r"""Sets the report_name of this ReportEntity.

        报告名称

        :param report_name: The report_name of this ReportEntity.
        :type report_name: str
        """
        self._report_name = report_name

    @property
    def report_generated_time(self):
        r"""Gets the report_generated_time of this ReportEntity.

        报告生成时间

        :return: The report_generated_time of this ReportEntity.
        :rtype: str
        """
        return self._report_generated_time

    @report_generated_time.setter
    def report_generated_time(self, report_generated_time):
        r"""Sets the report_generated_time of this ReportEntity.

        报告生成时间

        :param report_generated_time: The report_generated_time of this ReportEntity.
        :type report_generated_time: str
        """
        self._report_generated_time = report_generated_time

    @property
    def report_setting_id(self):
        r"""Gets the report_setting_id of this ReportEntity.

        报告配置ID

        :return: The report_setting_id of this ReportEntity.
        :rtype: str
        """
        return self._report_setting_id

    @report_setting_id.setter
    def report_setting_id(self, report_setting_id):
        r"""Sets the report_setting_id of this ReportEntity.

        报告配置ID

        :param report_setting_id: The report_setting_id of this ReportEntity.
        :type report_setting_id: str
        """
        self._report_setting_id = report_setting_id

    @property
    def report_setting_name(self):
        r"""Gets the report_setting_name of this ReportEntity.

        报告配置名称

        :return: The report_setting_name of this ReportEntity.
        :rtype: str
        """
        return self._report_setting_name

    @report_setting_name.setter
    def report_setting_name(self, report_setting_name):
        r"""Sets the report_setting_name of this ReportEntity.

        报告配置名称

        :param report_setting_name: The report_setting_name of this ReportEntity.
        :type report_setting_name: str
        """
        self._report_setting_name = report_setting_name

    @property
    def report_template(self):
        r"""Gets the report_template of this ReportEntity.

        报告模板名称

        :return: The report_template of this ReportEntity.
        :rtype: str
        """
        return self._report_template

    @report_template.setter
    def report_template(self, report_template):
        r"""Sets the report_template of this ReportEntity.

        报告模板名称

        :param report_template: The report_template of this ReportEntity.
        :type report_template: str
        """
        self._report_template = report_template

    @property
    def report_template_id(self):
        r"""Gets the report_template_id of this ReportEntity.

        报告模板ID

        :return: The report_template_id of this ReportEntity.
        :rtype: str
        """
        return self._report_template_id

    @report_template_id.setter
    def report_template_id(self, report_template_id):
        r"""Sets the report_template_id of this ReportEntity.

        报告模板ID

        :param report_template_id: The report_template_id of this ReportEntity.
        :type report_template_id: str
        """
        self._report_template_id = report_template_id

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
        if not isinstance(other, ReportEntity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
