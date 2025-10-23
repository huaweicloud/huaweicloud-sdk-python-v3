# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ReportSettingEntity:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'setting_id': 'str',
        'report_count': 'int',
        'create_time': 'str',
        'last_update_time': 'str',
        'report_template_id': 'str',
        'setting_content': 'ReportSetting'
    }

    attribute_map = {
        'setting_id': 'setting_id',
        'report_count': 'report_count',
        'create_time': 'create_time',
        'last_update_time': 'last_update_time',
        'report_template_id': 'report_template_id',
        'setting_content': 'setting_content'
    }

    def __init__(self, setting_id=None, report_count=None, create_time=None, last_update_time=None, report_template_id=None, setting_content=None):
        r"""ReportSettingEntity

        The model defined in huaweicloud sdk

        :param setting_id: 配置ID
        :type setting_id: str
        :param report_count: 本配置所有已经生成的报告数量，不包含已经删除的报告
        :type report_count: int
        :param create_time: 报告配置的创建时间
        :type create_time: str
        :param last_update_time: 报告配置的上一次更新时间
        :type last_update_time: str
        :param report_template_id: 报告关联的模板ID
        :type report_template_id: str
        :param setting_content: 
        :type setting_content: :class:`huaweicloudsdkbcc.v1.ReportSetting`
        """
        
        

        self._setting_id = None
        self._report_count = None
        self._create_time = None
        self._last_update_time = None
        self._report_template_id = None
        self._setting_content = None
        self.discriminator = None

        self.setting_id = setting_id
        self.report_count = report_count
        self.create_time = create_time
        self.last_update_time = last_update_time
        self.report_template_id = report_template_id
        self.setting_content = setting_content

    @property
    def setting_id(self):
        r"""Gets the setting_id of this ReportSettingEntity.

        配置ID

        :return: The setting_id of this ReportSettingEntity.
        :rtype: str
        """
        return self._setting_id

    @setting_id.setter
    def setting_id(self, setting_id):
        r"""Sets the setting_id of this ReportSettingEntity.

        配置ID

        :param setting_id: The setting_id of this ReportSettingEntity.
        :type setting_id: str
        """
        self._setting_id = setting_id

    @property
    def report_count(self):
        r"""Gets the report_count of this ReportSettingEntity.

        本配置所有已经生成的报告数量，不包含已经删除的报告

        :return: The report_count of this ReportSettingEntity.
        :rtype: int
        """
        return self._report_count

    @report_count.setter
    def report_count(self, report_count):
        r"""Sets the report_count of this ReportSettingEntity.

        本配置所有已经生成的报告数量，不包含已经删除的报告

        :param report_count: The report_count of this ReportSettingEntity.
        :type report_count: int
        """
        self._report_count = report_count

    @property
    def create_time(self):
        r"""Gets the create_time of this ReportSettingEntity.

        报告配置的创建时间

        :return: The create_time of this ReportSettingEntity.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ReportSettingEntity.

        报告配置的创建时间

        :param create_time: The create_time of this ReportSettingEntity.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def last_update_time(self):
        r"""Gets the last_update_time of this ReportSettingEntity.

        报告配置的上一次更新时间

        :return: The last_update_time of this ReportSettingEntity.
        :rtype: str
        """
        return self._last_update_time

    @last_update_time.setter
    def last_update_time(self, last_update_time):
        r"""Sets the last_update_time of this ReportSettingEntity.

        报告配置的上一次更新时间

        :param last_update_time: The last_update_time of this ReportSettingEntity.
        :type last_update_time: str
        """
        self._last_update_time = last_update_time

    @property
    def report_template_id(self):
        r"""Gets the report_template_id of this ReportSettingEntity.

        报告关联的模板ID

        :return: The report_template_id of this ReportSettingEntity.
        :rtype: str
        """
        return self._report_template_id

    @report_template_id.setter
    def report_template_id(self, report_template_id):
        r"""Sets the report_template_id of this ReportSettingEntity.

        报告关联的模板ID

        :param report_template_id: The report_template_id of this ReportSettingEntity.
        :type report_template_id: str
        """
        self._report_template_id = report_template_id

    @property
    def setting_content(self):
        r"""Gets the setting_content of this ReportSettingEntity.

        :return: The setting_content of this ReportSettingEntity.
        :rtype: :class:`huaweicloudsdkbcc.v1.ReportSetting`
        """
        return self._setting_content

    @setting_content.setter
    def setting_content(self, setting_content):
        r"""Sets the setting_content of this ReportSettingEntity.

        :param setting_content: The setting_content of this ReportSettingEntity.
        :type setting_content: :class:`huaweicloudsdkbcc.v1.ReportSetting`
        """
        self._setting_content = setting_content

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
        if not isinstance(other, ReportSettingEntity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
