# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDomainLocationStatsRequest:

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
        'interval': 'int',
        'domain_name': 'str',
        'stat_type': 'str',
        'group_by': 'str',
        'country': 'str',
        'province': 'str',
        'isp': 'str',
        'enterprise_project_id': 'str'
    }

    attribute_map = {
        'action': 'action',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'interval': 'interval',
        'domain_name': 'domain_name',
        'stat_type': 'stat_type',
        'group_by': 'group_by',
        'country': 'country',
        'province': 'province',
        'isp': 'isp',
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, action=None, start_time=None, end_time=None, interval=None, domain_name=None, stat_type=None, group_by=None, country=None, province=None, isp=None, enterprise_project_id=None):
        r"""ShowDomainLocationStatsRequest

        The model defined in huaweicloud sdk

        :param action: - 动作名称，可选location_summary、location_detail。 - location_summary：查询汇总数据 - location_detail：查询数据详情。
        :type action: str
        :param start_time: - 查询起始时间戳，需与结束时间戳同时指定，左闭右开，设置方式如下：  - interval为300时，start_time设置为整5分钟时刻点，如：1631240100000(对应2021-09-10 10:15:00)  - interval为3600时，start_time设置为整小时时刻点，如：1631239200000(对应2021-09-10 10:00:00)  - interval为86400时，start_time设置为东8区零点时刻点，如：1631203200000(对应2021-09-10 00:00:00)
        :type start_time: int
        :param end_time: - 查询结束时间戳，需与开始时间戳同时指定，左闭右开，设置方式如下：  - interval为300时，end_time设置为整5分钟时刻点，如：1631243700000(对应2021-09-10 11:15:00)  - interval为3600时，end_time设置为整小时时刻点，如：1631325600000(对应2021-09-11 10:00:00)  - interval为86400时，end_time设置为东8区零点时刻点，如：1631376000000(对应2021-09-12 00:00:00)
        :type end_time: int
        :param interval: - 查询时间间隔，单位：秒，取值说明： - 300(5分钟)：最大查询跨度2天 - 3600(1小时)：最大查询跨度7天 - 86400(1天)：最大查询跨度31天 - 如果不传，默认取对应时间跨度的最小间隔。
        :type interval: int
        :param domain_name: 域名列表，多个域名以逗号（半角）分隔，如：www.test1.com,www.test2.com，all表示查询名下全部域名。如果域名在查询时间段内无数据，结果将不返回该域名的信息。
        :type domain_name: str
        :param stat_type: - 网络资源消耗   - bw(带宽)   - flux(流量) - 访问情况   - req_num(请求总数) - HTTP状态码（组合指标）   - http_code_2xx(状态码汇总2xx)   - http_code_3xx(状态码汇总3xx)   - http_code_4xx(状态码汇总4xx)   - http_code_5xx(状态码汇总5xx)   - status_code_2xx(状态码详情2xx)   - status_code_3xx(状态码详情3xx)   - status_code_4xx(状态码详情4xx)   - status_code_5xx(状态码详情5xx)
        :type stat_type: str
        :param group_by: 数据分组方式，多个以英文逗号分隔，可选domain、country、province、isp，默认不分组。
        :type group_by: str
        :param country: 国家编码，多个以英文逗号分隔，all表示全部，取值见附录。
        :type country: str
        :param province: 省份编码，当country为cn（中国）时有效，多个以英文逗号分隔，all表示全部，取值见附录。
        :type province: str
        :param isp: 运营商编码，多个以英文逗号分隔，all表示全部，取值见附录。
        :type isp: str
        :param enterprise_project_id: 当用户开启企业项目功能时，该参数生效，表示查询资源所属项目，\&quot;all\&quot;表示所有项目。注意：当使用子帐号调用接口时，该参数必传。  您可以通过调用企业项目管理服务（EPS）的查询企业项目列表接口（ListEnterpriseProject）查询企业项目id。
        :type enterprise_project_id: str
        """
        
        

        self._action = None
        self._start_time = None
        self._end_time = None
        self._interval = None
        self._domain_name = None
        self._stat_type = None
        self._group_by = None
        self._country = None
        self._province = None
        self._isp = None
        self._enterprise_project_id = None
        self.discriminator = None

        self.action = action
        self.start_time = start_time
        self.end_time = end_time
        if interval is not None:
            self.interval = interval
        self.domain_name = domain_name
        self.stat_type = stat_type
        if group_by is not None:
            self.group_by = group_by
        if country is not None:
            self.country = country
        if province is not None:
            self.province = province
        if isp is not None:
            self.isp = isp
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id

    @property
    def action(self):
        r"""Gets the action of this ShowDomainLocationStatsRequest.

        - 动作名称，可选location_summary、location_detail。 - location_summary：查询汇总数据 - location_detail：查询数据详情。

        :return: The action of this ShowDomainLocationStatsRequest.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this ShowDomainLocationStatsRequest.

        - 动作名称，可选location_summary、location_detail。 - location_summary：查询汇总数据 - location_detail：查询数据详情。

        :param action: The action of this ShowDomainLocationStatsRequest.
        :type action: str
        """
        self._action = action

    @property
    def start_time(self):
        r"""Gets the start_time of this ShowDomainLocationStatsRequest.

        - 查询起始时间戳，需与结束时间戳同时指定，左闭右开，设置方式如下：  - interval为300时，start_time设置为整5分钟时刻点，如：1631240100000(对应2021-09-10 10:15:00)  - interval为3600时，start_time设置为整小时时刻点，如：1631239200000(对应2021-09-10 10:00:00)  - interval为86400时，start_time设置为东8区零点时刻点，如：1631203200000(对应2021-09-10 00:00:00)

        :return: The start_time of this ShowDomainLocationStatsRequest.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ShowDomainLocationStatsRequest.

        - 查询起始时间戳，需与结束时间戳同时指定，左闭右开，设置方式如下：  - interval为300时，start_time设置为整5分钟时刻点，如：1631240100000(对应2021-09-10 10:15:00)  - interval为3600时，start_time设置为整小时时刻点，如：1631239200000(对应2021-09-10 10:00:00)  - interval为86400时，start_time设置为东8区零点时刻点，如：1631203200000(对应2021-09-10 00:00:00)

        :param start_time: The start_time of this ShowDomainLocationStatsRequest.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ShowDomainLocationStatsRequest.

        - 查询结束时间戳，需与开始时间戳同时指定，左闭右开，设置方式如下：  - interval为300时，end_time设置为整5分钟时刻点，如：1631243700000(对应2021-09-10 11:15:00)  - interval为3600时，end_time设置为整小时时刻点，如：1631325600000(对应2021-09-11 10:00:00)  - interval为86400时，end_time设置为东8区零点时刻点，如：1631376000000(对应2021-09-12 00:00:00)

        :return: The end_time of this ShowDomainLocationStatsRequest.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ShowDomainLocationStatsRequest.

        - 查询结束时间戳，需与开始时间戳同时指定，左闭右开，设置方式如下：  - interval为300时，end_time设置为整5分钟时刻点，如：1631243700000(对应2021-09-10 11:15:00)  - interval为3600时，end_time设置为整小时时刻点，如：1631325600000(对应2021-09-11 10:00:00)  - interval为86400时，end_time设置为东8区零点时刻点，如：1631376000000(对应2021-09-12 00:00:00)

        :param end_time: The end_time of this ShowDomainLocationStatsRequest.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def interval(self):
        r"""Gets the interval of this ShowDomainLocationStatsRequest.

        - 查询时间间隔，单位：秒，取值说明： - 300(5分钟)：最大查询跨度2天 - 3600(1小时)：最大查询跨度7天 - 86400(1天)：最大查询跨度31天 - 如果不传，默认取对应时间跨度的最小间隔。

        :return: The interval of this ShowDomainLocationStatsRequest.
        :rtype: int
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        r"""Sets the interval of this ShowDomainLocationStatsRequest.

        - 查询时间间隔，单位：秒，取值说明： - 300(5分钟)：最大查询跨度2天 - 3600(1小时)：最大查询跨度7天 - 86400(1天)：最大查询跨度31天 - 如果不传，默认取对应时间跨度的最小间隔。

        :param interval: The interval of this ShowDomainLocationStatsRequest.
        :type interval: int
        """
        self._interval = interval

    @property
    def domain_name(self):
        r"""Gets the domain_name of this ShowDomainLocationStatsRequest.

        域名列表，多个域名以逗号（半角）分隔，如：www.test1.com,www.test2.com，all表示查询名下全部域名。如果域名在查询时间段内无数据，结果将不返回该域名的信息。

        :return: The domain_name of this ShowDomainLocationStatsRequest.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        r"""Sets the domain_name of this ShowDomainLocationStatsRequest.

        域名列表，多个域名以逗号（半角）分隔，如：www.test1.com,www.test2.com，all表示查询名下全部域名。如果域名在查询时间段内无数据，结果将不返回该域名的信息。

        :param domain_name: The domain_name of this ShowDomainLocationStatsRequest.
        :type domain_name: str
        """
        self._domain_name = domain_name

    @property
    def stat_type(self):
        r"""Gets the stat_type of this ShowDomainLocationStatsRequest.

        - 网络资源消耗   - bw(带宽)   - flux(流量) - 访问情况   - req_num(请求总数) - HTTP状态码（组合指标）   - http_code_2xx(状态码汇总2xx)   - http_code_3xx(状态码汇总3xx)   - http_code_4xx(状态码汇总4xx)   - http_code_5xx(状态码汇总5xx)   - status_code_2xx(状态码详情2xx)   - status_code_3xx(状态码详情3xx)   - status_code_4xx(状态码详情4xx)   - status_code_5xx(状态码详情5xx)

        :return: The stat_type of this ShowDomainLocationStatsRequest.
        :rtype: str
        """
        return self._stat_type

    @stat_type.setter
    def stat_type(self, stat_type):
        r"""Sets the stat_type of this ShowDomainLocationStatsRequest.

        - 网络资源消耗   - bw(带宽)   - flux(流量) - 访问情况   - req_num(请求总数) - HTTP状态码（组合指标）   - http_code_2xx(状态码汇总2xx)   - http_code_3xx(状态码汇总3xx)   - http_code_4xx(状态码汇总4xx)   - http_code_5xx(状态码汇总5xx)   - status_code_2xx(状态码详情2xx)   - status_code_3xx(状态码详情3xx)   - status_code_4xx(状态码详情4xx)   - status_code_5xx(状态码详情5xx)

        :param stat_type: The stat_type of this ShowDomainLocationStatsRequest.
        :type stat_type: str
        """
        self._stat_type = stat_type

    @property
    def group_by(self):
        r"""Gets the group_by of this ShowDomainLocationStatsRequest.

        数据分组方式，多个以英文逗号分隔，可选domain、country、province、isp，默认不分组。

        :return: The group_by of this ShowDomainLocationStatsRequest.
        :rtype: str
        """
        return self._group_by

    @group_by.setter
    def group_by(self, group_by):
        r"""Sets the group_by of this ShowDomainLocationStatsRequest.

        数据分组方式，多个以英文逗号分隔，可选domain、country、province、isp，默认不分组。

        :param group_by: The group_by of this ShowDomainLocationStatsRequest.
        :type group_by: str
        """
        self._group_by = group_by

    @property
    def country(self):
        r"""Gets the country of this ShowDomainLocationStatsRequest.

        国家编码，多个以英文逗号分隔，all表示全部，取值见附录。

        :return: The country of this ShowDomainLocationStatsRequest.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        r"""Sets the country of this ShowDomainLocationStatsRequest.

        国家编码，多个以英文逗号分隔，all表示全部，取值见附录。

        :param country: The country of this ShowDomainLocationStatsRequest.
        :type country: str
        """
        self._country = country

    @property
    def province(self):
        r"""Gets the province of this ShowDomainLocationStatsRequest.

        省份编码，当country为cn（中国）时有效，多个以英文逗号分隔，all表示全部，取值见附录。

        :return: The province of this ShowDomainLocationStatsRequest.
        :rtype: str
        """
        return self._province

    @province.setter
    def province(self, province):
        r"""Sets the province of this ShowDomainLocationStatsRequest.

        省份编码，当country为cn（中国）时有效，多个以英文逗号分隔，all表示全部，取值见附录。

        :param province: The province of this ShowDomainLocationStatsRequest.
        :type province: str
        """
        self._province = province

    @property
    def isp(self):
        r"""Gets the isp of this ShowDomainLocationStatsRequest.

        运营商编码，多个以英文逗号分隔，all表示全部，取值见附录。

        :return: The isp of this ShowDomainLocationStatsRequest.
        :rtype: str
        """
        return self._isp

    @isp.setter
    def isp(self, isp):
        r"""Sets the isp of this ShowDomainLocationStatsRequest.

        运营商编码，多个以英文逗号分隔，all表示全部，取值见附录。

        :param isp: The isp of this ShowDomainLocationStatsRequest.
        :type isp: str
        """
        self._isp = isp

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ShowDomainLocationStatsRequest.

        当用户开启企业项目功能时，该参数生效，表示查询资源所属项目，\"all\"表示所有项目。注意：当使用子帐号调用接口时，该参数必传。  您可以通过调用企业项目管理服务（EPS）的查询企业项目列表接口（ListEnterpriseProject）查询企业项目id。

        :return: The enterprise_project_id of this ShowDomainLocationStatsRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ShowDomainLocationStatsRequest.

        当用户开启企业项目功能时，该参数生效，表示查询资源所属项目，\"all\"表示所有项目。注意：当使用子帐号调用接口时，该参数必传。  您可以通过调用企业项目管理服务（EPS）的查询企业项目列表接口（ListEnterpriseProject）查询企业项目id。

        :param enterprise_project_id: The enterprise_project_id of this ShowDomainLocationStatsRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

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
        if not isinstance(other, ShowDomainLocationStatsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
