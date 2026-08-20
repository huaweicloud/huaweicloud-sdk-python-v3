# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExportTaskVo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'action': 'str',
        'domain_name': 'str',
        'start_time': 'int',
        'end_time': 'int',
        'group_by': 'str',
        'interval': 'int',
        'service_area': 'str',
        'stat_type': 'str',
        'country': 'str',
        'province': 'str',
        'isp': 'str',
        'language': 'str'
    }

    attribute_map = {
        'action': 'action',
        'domain_name': 'domain_name',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'group_by': 'group_by',
        'interval': 'interval',
        'service_area': 'service_area',
        'stat_type': 'stat_type',
        'country': 'country',
        'province': 'province',
        'isp': 'isp',
        'language': 'language'
    }

    def __init__(self, action=None, domain_name=None, start_time=None, end_time=None, group_by=None, interval=None, service_area=None, stat_type=None, country=None, province=None, isp=None, language=None):
        r"""ExportTaskVo

        The model defined in huaweicloud sdk

        :param action: **参数解释：** 导出数据类型 **约束限制：** 不涉及 **取值范围：** - reports_detail：基础话单数据导出 - top_url_detail：TOP URL数据导出 - top_ua_detail：TOP UA数据导出 - top_referer_detail：TOP referer数据导出 - top_ip_detail：TOP IP数据导出 - isp_detail：运营商数据导出, - top_path_detail： TOP path数据导出, - uv：UV数据导出 **默认取值：** 不涉及
        :type action: str
        :param domain_name: **参数解释：** 订阅的域名列表 &gt; 支持同时输入多个域名  **约束限制：** 不涉及 **取值范围：** - 多个域名用半角逗号（,）分隔 - 如果该参数为all，则为账号下的所有域名订阅运营报表 **默认取值：** 不涉及
        :type domain_name: str
        :param start_time: **参数解释：** 导出起始时间 **约束限制：** 不涉及 **取值范围：** 相对于UTC 1970-01-01到当前时间相隔的毫秒数 **默认取值：** 不涉及
        :type start_time: int
        :param end_time: **参数解释：** 导出结束时间 **约束限制：** 不涉及 **取值范围：** 相对于UTC 1970-01-01到当前时间相隔的毫秒数 **默认取值：** 不涉及
        :type end_time: int
        :param group_by: **参数解释：** 数据分组方式 **约束限制：** 不涉及 **取值范围：** domain：按域名分组 **默认取值：** 默认不分组
        :type group_by: str
        :param interval: **参数解释：** 查询时间粒度 **约束限制：** 当导出时间跨度超过90天时，仅支持1小时粒度（3600） **取值范围：** - 300：采样时间间隔为5分钟，单位：秒 - 3600：采样时间间隔为1小时，单位：秒 **默认取值：** 不涉及
        :type interval: int
        :param service_area: **参数解释：** 服务范围 **约束限制：** 服务范围为中国大陆或全球时，加速域名需要到工信部备案 **取值范围：** - mainland_china：中国大陆 - outside_mainland_china：中国大陆境外 - global：全球 **默认取值：** mainland_china：中国大陆
        :type service_area: str
        :param stat_type: **参数解释：** 统计指标类型 **约束限制：** 不涉及 **取值范围：** - flux：流量 - req_num：请求总数 **默认取值：** 不涉及
        :type stat_type: str
        :param country: **参数解释：** 国家&amp;地区编码 **约束限制：** - 查询运营商统计数据时，不传该参数 - 查询top_url数据时，不传该参数 - 查询区域情况数据时，该参数传cn（中国） **取值范围：** - 多个以英文逗号分隔 - all表示全部，取值见附录 **默认取值：** 不涉及
        :type country: str
        :param province: **参数解释：** 省份编码： **约束限制：** 当country为cn（中国）时，该参数有效 **取值范围：** all表示全部，取值见附录 **默认取值：** 不涉及
        :type province: str
        :param isp: **参数解释：** 运营商名称 &gt; 如果IP归属地未知，该字段返回null  **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type isp: str
        :param language: **参数解释：** 语言 **约束限制：** 不涉及 **取值范围：** - zh：中文 - en：英文 **默认取值：** zh：中文
        :type language: str
        """
        
        

        self._action = None
        self._domain_name = None
        self._start_time = None
        self._end_time = None
        self._group_by = None
        self._interval = None
        self._service_area = None
        self._stat_type = None
        self._country = None
        self._province = None
        self._isp = None
        self._language = None
        self.discriminator = None

        if action is not None:
            self.action = action
        if domain_name is not None:
            self.domain_name = domain_name
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if group_by is not None:
            self.group_by = group_by
        if interval is not None:
            self.interval = interval
        if service_area is not None:
            self.service_area = service_area
        if stat_type is not None:
            self.stat_type = stat_type
        if country is not None:
            self.country = country
        if province is not None:
            self.province = province
        if isp is not None:
            self.isp = isp
        if language is not None:
            self.language = language

    @property
    def action(self):
        r"""Gets the action of this ExportTaskVo.

        **参数解释：** 导出数据类型 **约束限制：** 不涉及 **取值范围：** - reports_detail：基础话单数据导出 - top_url_detail：TOP URL数据导出 - top_ua_detail：TOP UA数据导出 - top_referer_detail：TOP referer数据导出 - top_ip_detail：TOP IP数据导出 - isp_detail：运营商数据导出, - top_path_detail： TOP path数据导出, - uv：UV数据导出 **默认取值：** 不涉及

        :return: The action of this ExportTaskVo.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this ExportTaskVo.

        **参数解释：** 导出数据类型 **约束限制：** 不涉及 **取值范围：** - reports_detail：基础话单数据导出 - top_url_detail：TOP URL数据导出 - top_ua_detail：TOP UA数据导出 - top_referer_detail：TOP referer数据导出 - top_ip_detail：TOP IP数据导出 - isp_detail：运营商数据导出, - top_path_detail： TOP path数据导出, - uv：UV数据导出 **默认取值：** 不涉及

        :param action: The action of this ExportTaskVo.
        :type action: str
        """
        self._action = action

    @property
    def domain_name(self):
        r"""Gets the domain_name of this ExportTaskVo.

        **参数解释：** 订阅的域名列表 > 支持同时输入多个域名  **约束限制：** 不涉及 **取值范围：** - 多个域名用半角逗号（,）分隔 - 如果该参数为all，则为账号下的所有域名订阅运营报表 **默认取值：** 不涉及

        :return: The domain_name of this ExportTaskVo.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        r"""Sets the domain_name of this ExportTaskVo.

        **参数解释：** 订阅的域名列表 > 支持同时输入多个域名  **约束限制：** 不涉及 **取值范围：** - 多个域名用半角逗号（,）分隔 - 如果该参数为all，则为账号下的所有域名订阅运营报表 **默认取值：** 不涉及

        :param domain_name: The domain_name of this ExportTaskVo.
        :type domain_name: str
        """
        self._domain_name = domain_name

    @property
    def start_time(self):
        r"""Gets the start_time of this ExportTaskVo.

        **参数解释：** 导出起始时间 **约束限制：** 不涉及 **取值范围：** 相对于UTC 1970-01-01到当前时间相隔的毫秒数 **默认取值：** 不涉及

        :return: The start_time of this ExportTaskVo.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ExportTaskVo.

        **参数解释：** 导出起始时间 **约束限制：** 不涉及 **取值范围：** 相对于UTC 1970-01-01到当前时间相隔的毫秒数 **默认取值：** 不涉及

        :param start_time: The start_time of this ExportTaskVo.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ExportTaskVo.

        **参数解释：** 导出结束时间 **约束限制：** 不涉及 **取值范围：** 相对于UTC 1970-01-01到当前时间相隔的毫秒数 **默认取值：** 不涉及

        :return: The end_time of this ExportTaskVo.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ExportTaskVo.

        **参数解释：** 导出结束时间 **约束限制：** 不涉及 **取值范围：** 相对于UTC 1970-01-01到当前时间相隔的毫秒数 **默认取值：** 不涉及

        :param end_time: The end_time of this ExportTaskVo.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def group_by(self):
        r"""Gets the group_by of this ExportTaskVo.

        **参数解释：** 数据分组方式 **约束限制：** 不涉及 **取值范围：** domain：按域名分组 **默认取值：** 默认不分组

        :return: The group_by of this ExportTaskVo.
        :rtype: str
        """
        return self._group_by

    @group_by.setter
    def group_by(self, group_by):
        r"""Sets the group_by of this ExportTaskVo.

        **参数解释：** 数据分组方式 **约束限制：** 不涉及 **取值范围：** domain：按域名分组 **默认取值：** 默认不分组

        :param group_by: The group_by of this ExportTaskVo.
        :type group_by: str
        """
        self._group_by = group_by

    @property
    def interval(self):
        r"""Gets the interval of this ExportTaskVo.

        **参数解释：** 查询时间粒度 **约束限制：** 当导出时间跨度超过90天时，仅支持1小时粒度（3600） **取值范围：** - 300：采样时间间隔为5分钟，单位：秒 - 3600：采样时间间隔为1小时，单位：秒 **默认取值：** 不涉及

        :return: The interval of this ExportTaskVo.
        :rtype: int
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        r"""Sets the interval of this ExportTaskVo.

        **参数解释：** 查询时间粒度 **约束限制：** 当导出时间跨度超过90天时，仅支持1小时粒度（3600） **取值范围：** - 300：采样时间间隔为5分钟，单位：秒 - 3600：采样时间间隔为1小时，单位：秒 **默认取值：** 不涉及

        :param interval: The interval of this ExportTaskVo.
        :type interval: int
        """
        self._interval = interval

    @property
    def service_area(self):
        r"""Gets the service_area of this ExportTaskVo.

        **参数解释：** 服务范围 **约束限制：** 服务范围为中国大陆或全球时，加速域名需要到工信部备案 **取值范围：** - mainland_china：中国大陆 - outside_mainland_china：中国大陆境外 - global：全球 **默认取值：** mainland_china：中国大陆

        :return: The service_area of this ExportTaskVo.
        :rtype: str
        """
        return self._service_area

    @service_area.setter
    def service_area(self, service_area):
        r"""Sets the service_area of this ExportTaskVo.

        **参数解释：** 服务范围 **约束限制：** 服务范围为中国大陆或全球时，加速域名需要到工信部备案 **取值范围：** - mainland_china：中国大陆 - outside_mainland_china：中国大陆境外 - global：全球 **默认取值：** mainland_china：中国大陆

        :param service_area: The service_area of this ExportTaskVo.
        :type service_area: str
        """
        self._service_area = service_area

    @property
    def stat_type(self):
        r"""Gets the stat_type of this ExportTaskVo.

        **参数解释：** 统计指标类型 **约束限制：** 不涉及 **取值范围：** - flux：流量 - req_num：请求总数 **默认取值：** 不涉及

        :return: The stat_type of this ExportTaskVo.
        :rtype: str
        """
        return self._stat_type

    @stat_type.setter
    def stat_type(self, stat_type):
        r"""Sets the stat_type of this ExportTaskVo.

        **参数解释：** 统计指标类型 **约束限制：** 不涉及 **取值范围：** - flux：流量 - req_num：请求总数 **默认取值：** 不涉及

        :param stat_type: The stat_type of this ExportTaskVo.
        :type stat_type: str
        """
        self._stat_type = stat_type

    @property
    def country(self):
        r"""Gets the country of this ExportTaskVo.

        **参数解释：** 国家&地区编码 **约束限制：** - 查询运营商统计数据时，不传该参数 - 查询top_url数据时，不传该参数 - 查询区域情况数据时，该参数传cn（中国） **取值范围：** - 多个以英文逗号分隔 - all表示全部，取值见附录 **默认取值：** 不涉及

        :return: The country of this ExportTaskVo.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        r"""Sets the country of this ExportTaskVo.

        **参数解释：** 国家&地区编码 **约束限制：** - 查询运营商统计数据时，不传该参数 - 查询top_url数据时，不传该参数 - 查询区域情况数据时，该参数传cn（中国） **取值范围：** - 多个以英文逗号分隔 - all表示全部，取值见附录 **默认取值：** 不涉及

        :param country: The country of this ExportTaskVo.
        :type country: str
        """
        self._country = country

    @property
    def province(self):
        r"""Gets the province of this ExportTaskVo.

        **参数解释：** 省份编码： **约束限制：** 当country为cn（中国）时，该参数有效 **取值范围：** all表示全部，取值见附录 **默认取值：** 不涉及

        :return: The province of this ExportTaskVo.
        :rtype: str
        """
        return self._province

    @province.setter
    def province(self, province):
        r"""Sets the province of this ExportTaskVo.

        **参数解释：** 省份编码： **约束限制：** 当country为cn（中国）时，该参数有效 **取值范围：** all表示全部，取值见附录 **默认取值：** 不涉及

        :param province: The province of this ExportTaskVo.
        :type province: str
        """
        self._province = province

    @property
    def isp(self):
        r"""Gets the isp of this ExportTaskVo.

        **参数解释：** 运营商名称 > 如果IP归属地未知，该字段返回null  **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The isp of this ExportTaskVo.
        :rtype: str
        """
        return self._isp

    @isp.setter
    def isp(self, isp):
        r"""Sets the isp of this ExportTaskVo.

        **参数解释：** 运营商名称 > 如果IP归属地未知，该字段返回null  **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param isp: The isp of this ExportTaskVo.
        :type isp: str
        """
        self._isp = isp

    @property
    def language(self):
        r"""Gets the language of this ExportTaskVo.

        **参数解释：** 语言 **约束限制：** 不涉及 **取值范围：** - zh：中文 - en：英文 **默认取值：** zh：中文

        :return: The language of this ExportTaskVo.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        r"""Sets the language of this ExportTaskVo.

        **参数解释：** 语言 **约束限制：** 不涉及 **取值范围：** - zh：中文 - en：英文 **默认取值：** zh：中文

        :param language: The language of this ExportTaskVo.
        :type language: str
        """
        self._language = language

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
        if not isinstance(other, ExportTaskVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
