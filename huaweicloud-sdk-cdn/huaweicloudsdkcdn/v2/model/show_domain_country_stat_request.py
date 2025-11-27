# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDomainCountryStatRequest:

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
        'start_time': 'int',
        'end_time': 'int',
        'domain_name': 'str',
        'stat_type': 'str',
        'country': 'str',
        'group_by': 'str',
        'user_domain_id': 'str'
    }

    attribute_map = {
        'action': 'action',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'domain_name': 'domain_name',
        'stat_type': 'stat_type',
        'country': 'country',
        'group_by': 'group_by',
        'user_domain_id': 'user_domain_id'
    }

    def __init__(self, action=None, start_time=None, end_time=None, domain_name=None, stat_type=None, country=None, group_by=None, user_domain_id=None):
        r"""ShowDomainCountryStatRequest

        The model defined in huaweicloud sdk

        :param action: 动作名称，可选summary、detail。 - summary：查询汇总数据 - detail：查询数据详情。
        :type action: str
        :param start_time: 查询起始时间戳，需与结束时间戳同时指定，左闭右开，设置方式如下： - interval为300时，start_time设置为整5分钟时刻点，如：1631240100000(对应2021-09-10 10:15:00) - interval为3600时，start_time设置为整小时时刻点，如：1631239200000(对应2021-09-10 10:00:00) - interval为86400时，start_time设置为东8区零点时刻点，如：1631203200000(对应2021-09-10 00:00:00)
        :type start_time: int
        :param end_time: 查询结束时间戳，需与开始时间戳同时指定，左闭右开，设置方式如下： - interval为300时，end_time设置为整5分钟时刻点，如：1631243700000(对应2021-09-10 11:15:00) - interval为3600时，end_time设置为整小时时刻点，如：1631325600000(对应2021-09-11 10:00:00) - interval为86400时，end_time设置为东8区零点时刻点，如：1631376000000(对应2021-09-12 00:00:00)
        :type end_time: int
        :param domain_name: 域名列表，多个域名以逗号（半角）分隔，如：www.test1.com,www.test2.com all表示查询名下全部域名。如果域名在查询时间段内无数据，结果将不返回该域名的信息。
        :type domain_name: str
        :param stat_type: - 网络资源消耗   - bw（带宽）   - flux（流量） - 访问情况   - req_num（请求总数） - HTTP状态码（组合指标）   - http_code_2xx(状态码汇总2xx)   - http_code_3xx(状态码汇总3xx)   - http_code_4xx(状态码汇总4xx)   - http_code_5xx(状态码汇总5xx)   - status_code_2xx(状态码详情2xx)   - status_code_3xx(状态码详情3xx)   - status_code_4xx(状态码详情4xx)   - status_code_5xx(状态码详情5xx)
        :type stat_type: str
        :param country: - 国家&amp;地区编码，多个以英文逗号分隔，all表示全部，取值见附录 - 访问运营商统计数据时不能填写 - 访问top_url数据时不能填写 - 访问区域情况数据时只能填写cn(中国)
        :type country: str
        :param group_by: 数据分组方式，多个以英文逗号分隔，可选domain（域名）、country（国家）、province（省份，仅国家为中国时有效）、isp（区域运营商），默认不分组
        :type group_by: str
        :param user_domain_id: 域名所属用户的domain_id。
        :type user_domain_id: str
        """
        
        

        self._action = None
        self._start_time = None
        self._end_time = None
        self._domain_name = None
        self._stat_type = None
        self._country = None
        self._group_by = None
        self._user_domain_id = None
        self.discriminator = None

        self.action = action
        self.start_time = start_time
        self.end_time = end_time
        self.domain_name = domain_name
        self.stat_type = stat_type
        if country is not None:
            self.country = country
        if group_by is not None:
            self.group_by = group_by
        if user_domain_id is not None:
            self.user_domain_id = user_domain_id

    @property
    def action(self):
        r"""Gets the action of this ShowDomainCountryStatRequest.

        动作名称，可选summary、detail。 - summary：查询汇总数据 - detail：查询数据详情。

        :return: The action of this ShowDomainCountryStatRequest.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this ShowDomainCountryStatRequest.

        动作名称，可选summary、detail。 - summary：查询汇总数据 - detail：查询数据详情。

        :param action: The action of this ShowDomainCountryStatRequest.
        :type action: str
        """
        self._action = action

    @property
    def start_time(self):
        r"""Gets the start_time of this ShowDomainCountryStatRequest.

        查询起始时间戳，需与结束时间戳同时指定，左闭右开，设置方式如下： - interval为300时，start_time设置为整5分钟时刻点，如：1631240100000(对应2021-09-10 10:15:00) - interval为3600时，start_time设置为整小时时刻点，如：1631239200000(对应2021-09-10 10:00:00) - interval为86400时，start_time设置为东8区零点时刻点，如：1631203200000(对应2021-09-10 00:00:00)

        :return: The start_time of this ShowDomainCountryStatRequest.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ShowDomainCountryStatRequest.

        查询起始时间戳，需与结束时间戳同时指定，左闭右开，设置方式如下： - interval为300时，start_time设置为整5分钟时刻点，如：1631240100000(对应2021-09-10 10:15:00) - interval为3600时，start_time设置为整小时时刻点，如：1631239200000(对应2021-09-10 10:00:00) - interval为86400时，start_time设置为东8区零点时刻点，如：1631203200000(对应2021-09-10 00:00:00)

        :param start_time: The start_time of this ShowDomainCountryStatRequest.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ShowDomainCountryStatRequest.

        查询结束时间戳，需与开始时间戳同时指定，左闭右开，设置方式如下： - interval为300时，end_time设置为整5分钟时刻点，如：1631243700000(对应2021-09-10 11:15:00) - interval为3600时，end_time设置为整小时时刻点，如：1631325600000(对应2021-09-11 10:00:00) - interval为86400时，end_time设置为东8区零点时刻点，如：1631376000000(对应2021-09-12 00:00:00)

        :return: The end_time of this ShowDomainCountryStatRequest.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ShowDomainCountryStatRequest.

        查询结束时间戳，需与开始时间戳同时指定，左闭右开，设置方式如下： - interval为300时，end_time设置为整5分钟时刻点，如：1631243700000(对应2021-09-10 11:15:00) - interval为3600时，end_time设置为整小时时刻点，如：1631325600000(对应2021-09-11 10:00:00) - interval为86400时，end_time设置为东8区零点时刻点，如：1631376000000(对应2021-09-12 00:00:00)

        :param end_time: The end_time of this ShowDomainCountryStatRequest.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def domain_name(self):
        r"""Gets the domain_name of this ShowDomainCountryStatRequest.

        域名列表，多个域名以逗号（半角）分隔，如：www.test1.com,www.test2.com all表示查询名下全部域名。如果域名在查询时间段内无数据，结果将不返回该域名的信息。

        :return: The domain_name of this ShowDomainCountryStatRequest.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        r"""Sets the domain_name of this ShowDomainCountryStatRequest.

        域名列表，多个域名以逗号（半角）分隔，如：www.test1.com,www.test2.com all表示查询名下全部域名。如果域名在查询时间段内无数据，结果将不返回该域名的信息。

        :param domain_name: The domain_name of this ShowDomainCountryStatRequest.
        :type domain_name: str
        """
        self._domain_name = domain_name

    @property
    def stat_type(self):
        r"""Gets the stat_type of this ShowDomainCountryStatRequest.

        - 网络资源消耗   - bw（带宽）   - flux（流量） - 访问情况   - req_num（请求总数） - HTTP状态码（组合指标）   - http_code_2xx(状态码汇总2xx)   - http_code_3xx(状态码汇总3xx)   - http_code_4xx(状态码汇总4xx)   - http_code_5xx(状态码汇总5xx)   - status_code_2xx(状态码详情2xx)   - status_code_3xx(状态码详情3xx)   - status_code_4xx(状态码详情4xx)   - status_code_5xx(状态码详情5xx)

        :return: The stat_type of this ShowDomainCountryStatRequest.
        :rtype: str
        """
        return self._stat_type

    @stat_type.setter
    def stat_type(self, stat_type):
        r"""Sets the stat_type of this ShowDomainCountryStatRequest.

        - 网络资源消耗   - bw（带宽）   - flux（流量） - 访问情况   - req_num（请求总数） - HTTP状态码（组合指标）   - http_code_2xx(状态码汇总2xx)   - http_code_3xx(状态码汇总3xx)   - http_code_4xx(状态码汇总4xx)   - http_code_5xx(状态码汇总5xx)   - status_code_2xx(状态码详情2xx)   - status_code_3xx(状态码详情3xx)   - status_code_4xx(状态码详情4xx)   - status_code_5xx(状态码详情5xx)

        :param stat_type: The stat_type of this ShowDomainCountryStatRequest.
        :type stat_type: str
        """
        self._stat_type = stat_type

    @property
    def country(self):
        r"""Gets the country of this ShowDomainCountryStatRequest.

        - 国家&地区编码，多个以英文逗号分隔，all表示全部，取值见附录 - 访问运营商统计数据时不能填写 - 访问top_url数据时不能填写 - 访问区域情况数据时只能填写cn(中国)

        :return: The country of this ShowDomainCountryStatRequest.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        r"""Sets the country of this ShowDomainCountryStatRequest.

        - 国家&地区编码，多个以英文逗号分隔，all表示全部，取值见附录 - 访问运营商统计数据时不能填写 - 访问top_url数据时不能填写 - 访问区域情况数据时只能填写cn(中国)

        :param country: The country of this ShowDomainCountryStatRequest.
        :type country: str
        """
        self._country = country

    @property
    def group_by(self):
        r"""Gets the group_by of this ShowDomainCountryStatRequest.

        数据分组方式，多个以英文逗号分隔，可选domain（域名）、country（国家）、province（省份，仅国家为中国时有效）、isp（区域运营商），默认不分组

        :return: The group_by of this ShowDomainCountryStatRequest.
        :rtype: str
        """
        return self._group_by

    @group_by.setter
    def group_by(self, group_by):
        r"""Sets the group_by of this ShowDomainCountryStatRequest.

        数据分组方式，多个以英文逗号分隔，可选domain（域名）、country（国家）、province（省份，仅国家为中国时有效）、isp（区域运营商），默认不分组

        :param group_by: The group_by of this ShowDomainCountryStatRequest.
        :type group_by: str
        """
        self._group_by = group_by

    @property
    def user_domain_id(self):
        r"""Gets the user_domain_id of this ShowDomainCountryStatRequest.

        域名所属用户的domain_id。

        :return: The user_domain_id of this ShowDomainCountryStatRequest.
        :rtype: str
        """
        return self._user_domain_id

    @user_domain_id.setter
    def user_domain_id(self, user_domain_id):
        r"""Sets the user_domain_id of this ShowDomainCountryStatRequest.

        域名所属用户的domain_id。

        :param user_domain_id: The user_domain_id of this ShowDomainCountryStatRequest.
        :type user_domain_id: str
        """
        self._user_domain_id = user_domain_id

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
        if not isinstance(other, ShowDomainCountryStatRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
