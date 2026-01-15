# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ReportSetting:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'setting_name': 'str',
        'enabled': 'bool',
        'region_ids': 'list[str]',
        'resource_types': 'list[ResourceTypeEnum]',
        'time_range': 'int',
        'report_template_name': 'str',
        'frequency': 'int',
        'retention_duration': 'int',
        'report_name_prefix': 'str'
    }

    attribute_map = {
        'setting_name': 'setting_name',
        'enabled': 'enabled',
        'region_ids': 'region_ids',
        'resource_types': 'resource_types',
        'time_range': 'time_range',
        'report_template_name': 'report_template_name',
        'frequency': 'frequency',
        'retention_duration': 'retention_duration',
        'report_name_prefix': 'report_name_prefix'
    }

    def __init__(self, setting_name=None, enabled=None, region_ids=None, resource_types=None, time_range=None, report_template_name=None, frequency=None, retention_duration=None, report_name_prefix=None):
        r"""ReportSetting

        The model defined in huaweicloud sdk

        :param setting_name: 配置名称，取值长度为2到32个字符
        :type setting_name: str
        :param enabled: 是否启用,取值范围：true,false
        :type enabled: bool
        :param region_ids: 参与统计的资源归属的区域列表，不设置表示全部区域，默认不设置
        :type region_ids: list[str]
        :param resource_types: 参与统计的资源类型列表，不设置表示全部资源类型，默认不设置
        :type resource_types: list[:class:`huaweicloudsdkbcc.v1.ResourceTypeEnum`]
        :param time_range: 参与统计的数据范围（生成报告时刻往前多少天内的数据参与统计，滚动计算），默认7天，取值范围：7到30天，详情类数据报告不受此项配置约束
        :type time_range: int
        :param report_template_name: 报告模板名称，例如TEMPLATE.TASK
        :type report_template_name: str
        :param frequency: 生成报告的频率（每隔多少天生成一次报告），默认7天，取值范围7到30天
        :type frequency: int
        :param retention_duration: 报告保留天数，默认7天，取值范围7到1095天
        :type retention_duration: int
        :param report_name_prefix: 报告名称的前缀，取值长度为2到32个字符
        :type report_name_prefix: str
        """
        
        

        self._setting_name = None
        self._enabled = None
        self._region_ids = None
        self._resource_types = None
        self._time_range = None
        self._report_template_name = None
        self._frequency = None
        self._retention_duration = None
        self._report_name_prefix = None
        self.discriminator = None

        self.setting_name = setting_name
        self.enabled = enabled
        if region_ids is not None:
            self.region_ids = region_ids
        if resource_types is not None:
            self.resource_types = resource_types
        self.time_range = time_range
        self.report_template_name = report_template_name
        self.frequency = frequency
        self.retention_duration = retention_duration
        self.report_name_prefix = report_name_prefix

    @property
    def setting_name(self):
        r"""Gets the setting_name of this ReportSetting.

        配置名称，取值长度为2到32个字符

        :return: The setting_name of this ReportSetting.
        :rtype: str
        """
        return self._setting_name

    @setting_name.setter
    def setting_name(self, setting_name):
        r"""Sets the setting_name of this ReportSetting.

        配置名称，取值长度为2到32个字符

        :param setting_name: The setting_name of this ReportSetting.
        :type setting_name: str
        """
        self._setting_name = setting_name

    @property
    def enabled(self):
        r"""Gets the enabled of this ReportSetting.

        是否启用,取值范围：true,false

        :return: The enabled of this ReportSetting.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        r"""Sets the enabled of this ReportSetting.

        是否启用,取值范围：true,false

        :param enabled: The enabled of this ReportSetting.
        :type enabled: bool
        """
        self._enabled = enabled

    @property
    def region_ids(self):
        r"""Gets the region_ids of this ReportSetting.

        参与统计的资源归属的区域列表，不设置表示全部区域，默认不设置

        :return: The region_ids of this ReportSetting.
        :rtype: list[str]
        """
        return self._region_ids

    @region_ids.setter
    def region_ids(self, region_ids):
        r"""Sets the region_ids of this ReportSetting.

        参与统计的资源归属的区域列表，不设置表示全部区域，默认不设置

        :param region_ids: The region_ids of this ReportSetting.
        :type region_ids: list[str]
        """
        self._region_ids = region_ids

    @property
    def resource_types(self):
        r"""Gets the resource_types of this ReportSetting.

        参与统计的资源类型列表，不设置表示全部资源类型，默认不设置

        :return: The resource_types of this ReportSetting.
        :rtype: list[:class:`huaweicloudsdkbcc.v1.ResourceTypeEnum`]
        """
        return self._resource_types

    @resource_types.setter
    def resource_types(self, resource_types):
        r"""Sets the resource_types of this ReportSetting.

        参与统计的资源类型列表，不设置表示全部资源类型，默认不设置

        :param resource_types: The resource_types of this ReportSetting.
        :type resource_types: list[:class:`huaweicloudsdkbcc.v1.ResourceTypeEnum`]
        """
        self._resource_types = resource_types

    @property
    def time_range(self):
        r"""Gets the time_range of this ReportSetting.

        参与统计的数据范围（生成报告时刻往前多少天内的数据参与统计，滚动计算），默认7天，取值范围：7到30天，详情类数据报告不受此项配置约束

        :return: The time_range of this ReportSetting.
        :rtype: int
        """
        return self._time_range

    @time_range.setter
    def time_range(self, time_range):
        r"""Sets the time_range of this ReportSetting.

        参与统计的数据范围（生成报告时刻往前多少天内的数据参与统计，滚动计算），默认7天，取值范围：7到30天，详情类数据报告不受此项配置约束

        :param time_range: The time_range of this ReportSetting.
        :type time_range: int
        """
        self._time_range = time_range

    @property
    def report_template_name(self):
        r"""Gets the report_template_name of this ReportSetting.

        报告模板名称，例如TEMPLATE.TASK

        :return: The report_template_name of this ReportSetting.
        :rtype: str
        """
        return self._report_template_name

    @report_template_name.setter
    def report_template_name(self, report_template_name):
        r"""Sets the report_template_name of this ReportSetting.

        报告模板名称，例如TEMPLATE.TASK

        :param report_template_name: The report_template_name of this ReportSetting.
        :type report_template_name: str
        """
        self._report_template_name = report_template_name

    @property
    def frequency(self):
        r"""Gets the frequency of this ReportSetting.

        生成报告的频率（每隔多少天生成一次报告），默认7天，取值范围7到30天

        :return: The frequency of this ReportSetting.
        :rtype: int
        """
        return self._frequency

    @frequency.setter
    def frequency(self, frequency):
        r"""Sets the frequency of this ReportSetting.

        生成报告的频率（每隔多少天生成一次报告），默认7天，取值范围7到30天

        :param frequency: The frequency of this ReportSetting.
        :type frequency: int
        """
        self._frequency = frequency

    @property
    def retention_duration(self):
        r"""Gets the retention_duration of this ReportSetting.

        报告保留天数，默认7天，取值范围7到1095天

        :return: The retention_duration of this ReportSetting.
        :rtype: int
        """
        return self._retention_duration

    @retention_duration.setter
    def retention_duration(self, retention_duration):
        r"""Sets the retention_duration of this ReportSetting.

        报告保留天数，默认7天，取值范围7到1095天

        :param retention_duration: The retention_duration of this ReportSetting.
        :type retention_duration: int
        """
        self._retention_duration = retention_duration

    @property
    def report_name_prefix(self):
        r"""Gets the report_name_prefix of this ReportSetting.

        报告名称的前缀，取值长度为2到32个字符

        :return: The report_name_prefix of this ReportSetting.
        :rtype: str
        """
        return self._report_name_prefix

    @report_name_prefix.setter
    def report_name_prefix(self, report_name_prefix):
        r"""Sets the report_name_prefix of this ReportSetting.

        报告名称的前缀，取值长度为2到32个字符

        :param report_name_prefix: The report_name_prefix of this ReportSetting.
        :type report_name_prefix: str
        """
        self._report_name_prefix = report_name_prefix

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
        if not isinstance(other, ReportSetting):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
