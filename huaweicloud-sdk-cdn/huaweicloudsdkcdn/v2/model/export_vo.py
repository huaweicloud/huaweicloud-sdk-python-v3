# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExportVo:

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
        'service_area': 'str',
        'stat_type': 'str',
        'country': 'str'
    }

    attribute_map = {
        'action': 'action',
        'domain_name': 'domain_name',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'group_by': 'group_by',
        'service_area': 'service_area',
        'stat_type': 'stat_type',
        'country': 'country'
    }

    def __init__(self, action=None, domain_name=None, start_time=None, end_time=None, group_by=None, service_area=None, stat_type=None, country=None):
        r"""ExportVo

        The model defined in huaweicloud sdk

        :param action: **参数解释：** 规则行为 **约束限制：** 不涉及
        :type action: str
        :param domain_name: 域名列表，支持同时输入多个域名，多个域名用半角逗号（,）分隔；说明：如果该参数为all，则为账号下的所有域名报表。
        :type domain_name: str
        :param start_time: 查询起始时间，相对于UTC 1970-01-01到当前时间相隔的毫秒数。
        :type start_time: int
        :param end_time: 查询结束时间，相对于UTC 1970-01-01到当前时间相隔的毫秒数。
        :type end_time: int
        :param group_by: 数据分组方式
        :type group_by: str
        :param service_area: **参数解释：** 域名服务范围 **约束限制：** 服务范围为中国大陆或全球时，加速域名需要到工信部备案 **取值范围：** - mainland_china: 中国大陆 - outside_mainland_china: 中国大陆境外 - global: 全球 **默认取值：** mainland_china: 中国大陆
        :type service_area: str
        :param stat_type: 参数类型支持：flux(流量)，req_num(请求总数)。
        :type stat_type: str
        :param country: - 国家&amp;地区编码，多个以英文逗号分隔，all表示全部，取值见附录 - 访问运营商统计数据时不能填写 - 访问top_url数据时不能填写 - 访问区域情况数据时只能填写cn(中国)
        :type country: str
        """
        
        

        self._action = None
        self._domain_name = None
        self._start_time = None
        self._end_time = None
        self._group_by = None
        self._service_area = None
        self._stat_type = None
        self._country = None
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
        if service_area is not None:
            self.service_area = service_area
        if stat_type is not None:
            self.stat_type = stat_type
        if country is not None:
            self.country = country

    @property
    def action(self):
        r"""Gets the action of this ExportVo.

        **参数解释：** 规则行为 **约束限制：** 不涉及

        :return: The action of this ExportVo.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this ExportVo.

        **参数解释：** 规则行为 **约束限制：** 不涉及

        :param action: The action of this ExportVo.
        :type action: str
        """
        self._action = action

    @property
    def domain_name(self):
        r"""Gets the domain_name of this ExportVo.

        域名列表，支持同时输入多个域名，多个域名用半角逗号（,）分隔；说明：如果该参数为all，则为账号下的所有域名报表。

        :return: The domain_name of this ExportVo.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        r"""Sets the domain_name of this ExportVo.

        域名列表，支持同时输入多个域名，多个域名用半角逗号（,）分隔；说明：如果该参数为all，则为账号下的所有域名报表。

        :param domain_name: The domain_name of this ExportVo.
        :type domain_name: str
        """
        self._domain_name = domain_name

    @property
    def start_time(self):
        r"""Gets the start_time of this ExportVo.

        查询起始时间，相对于UTC 1970-01-01到当前时间相隔的毫秒数。

        :return: The start_time of this ExportVo.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ExportVo.

        查询起始时间，相对于UTC 1970-01-01到当前时间相隔的毫秒数。

        :param start_time: The start_time of this ExportVo.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ExportVo.

        查询结束时间，相对于UTC 1970-01-01到当前时间相隔的毫秒数。

        :return: The end_time of this ExportVo.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ExportVo.

        查询结束时间，相对于UTC 1970-01-01到当前时间相隔的毫秒数。

        :param end_time: The end_time of this ExportVo.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def group_by(self):
        r"""Gets the group_by of this ExportVo.

        数据分组方式

        :return: The group_by of this ExportVo.
        :rtype: str
        """
        return self._group_by

    @group_by.setter
    def group_by(self, group_by):
        r"""Sets the group_by of this ExportVo.

        数据分组方式

        :param group_by: The group_by of this ExportVo.
        :type group_by: str
        """
        self._group_by = group_by

    @property
    def service_area(self):
        r"""Gets the service_area of this ExportVo.

        **参数解释：** 域名服务范围 **约束限制：** 服务范围为中国大陆或全球时，加速域名需要到工信部备案 **取值范围：** - mainland_china: 中国大陆 - outside_mainland_china: 中国大陆境外 - global: 全球 **默认取值：** mainland_china: 中国大陆

        :return: The service_area of this ExportVo.
        :rtype: str
        """
        return self._service_area

    @service_area.setter
    def service_area(self, service_area):
        r"""Sets the service_area of this ExportVo.

        **参数解释：** 域名服务范围 **约束限制：** 服务范围为中国大陆或全球时，加速域名需要到工信部备案 **取值范围：** - mainland_china: 中国大陆 - outside_mainland_china: 中国大陆境外 - global: 全球 **默认取值：** mainland_china: 中国大陆

        :param service_area: The service_area of this ExportVo.
        :type service_area: str
        """
        self._service_area = service_area

    @property
    def stat_type(self):
        r"""Gets the stat_type of this ExportVo.

        参数类型支持：flux(流量)，req_num(请求总数)。

        :return: The stat_type of this ExportVo.
        :rtype: str
        """
        return self._stat_type

    @stat_type.setter
    def stat_type(self, stat_type):
        r"""Sets the stat_type of this ExportVo.

        参数类型支持：flux(流量)，req_num(请求总数)。

        :param stat_type: The stat_type of this ExportVo.
        :type stat_type: str
        """
        self._stat_type = stat_type

    @property
    def country(self):
        r"""Gets the country of this ExportVo.

        - 国家&地区编码，多个以英文逗号分隔，all表示全部，取值见附录 - 访问运营商统计数据时不能填写 - 访问top_url数据时不能填写 - 访问区域情况数据时只能填写cn(中国)

        :return: The country of this ExportVo.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        r"""Sets the country of this ExportVo.

        - 国家&地区编码，多个以英文逗号分隔，all表示全部，取值见附录 - 访问运营商统计数据时不能填写 - 访问top_url数据时不能填写 - 访问区域情况数据时只能填写cn(中国)

        :param country: The country of this ExportVo.
        :type country: str
        """
        self._country = country

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
        if not isinstance(other, ExportVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
