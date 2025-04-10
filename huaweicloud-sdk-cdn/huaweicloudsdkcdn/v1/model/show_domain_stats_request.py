# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDomainStatsRequest:

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
        'interval': 'int',
        'group_by': 'str',
        'service_area': 'str',
        'enterprise_project_id': 'str'
    }

    attribute_map = {
        'action': 'action',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'domain_name': 'domain_name',
        'stat_type': 'stat_type',
        'interval': 'interval',
        'group_by': 'group_by',
        'service_area': 'service_area',
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, action=None, start_time=None, end_time=None, domain_name=None, stat_type=None, interval=None, group_by=None, service_area=None, enterprise_project_id=None):
        r"""ShowDomainStatsRequest

        The model defined in huaweicloud sdk

        :param action: - 动作名称，可选summary、detail。 - summary：查询汇总数据 - detail：查询数据详情。
        :type action: str
        :param start_time: - 查询起始时间戳，需与结束时间戳同时指定，左闭右开，设置方式如下：  - interval为300时，start_time设置为整5分钟时刻点，如：1631240100000(对应2021-09-10 10:15:00)  - interval为3600时，start_time设置为整小时时刻点，如：1631239200000(对应2021-09-10 10:00:00)  - interval为86400时，start_time设置为东8区零点时刻点，如：1631203200000(对应2021-09-10 00:00:00)
        :type start_time: int
        :param end_time: - 查询结束时间戳，需与开始时间戳同时指定，左闭右开，设置方式如下：  - interval为300时，end_time设置为整5分钟时刻点，如：1631243700000(对应2021-09-10 11:15:00)  - interval为3600时，end_time设置为整小时时刻点，如：1631325600000(对应2021-09-11 10:00:00)  - interval为86400时，end_time设置为东8区零点时刻点，如：1631376000000(对应2021-09-12 00:00:00)
        :type end_time: int
        :param domain_name: 域名列表，多个域名以逗号（半角）分隔，如：www.test1.com,www.test2.com，all表示查询名下全部域名。如果域名在查询时间段内无数据，结果将不返回该域名的信息。
        :type domain_name: str
        :param stat_type: - 网络资源消耗：   - bw（带宽）   - flux（流量）   - bs_bw（回源带宽）   - bs_flux（回源流量） - 访问情况：   - req_num（请求总数）   - hit_num（请求命中次数）   - bs_num（回源总数）   - bs_fail_num（回源失败数）   - hit_flux（命中流量） - HTTP状态码（组合指标）：   - http_code_2xx（状态码汇总2xx）   - http_code_3xx（状态码汇总3xx）   - http_code_4xx（状态码汇总4xx）   - http_code_5xx（状态码汇总5xx）   - bs_http_code_2xx（回源状态码汇总2xx）   - bs_http_code_3xx（回源状态码汇总3xx）   - bs_http_code_4xx（回源状态码汇总4xx）   - bs_http_code_5xx（回源状态码汇总5xx）   - status_code_2xx（状态码详情2xx）   - status_code_3xx（状态码详情3xx）   - status_code_4xx（状态码详情4xx）   - status_code_5xx（状态码详情5xx）   - bs_status_code_2xx（回源状态码详情2xx）   - bs_status_code_3xx（回源状态码详情3xx）   - bs_status_code_4xx（回源状态码详情4xx）   - bs_status_code_5xx（回源状态码详情5xx）   - status_code和bs_status_code不能一起查询
        :type stat_type: str
        :param interval: - 查询时间间隔，单位：秒，取值说明： - 300(5分钟)：最大查询跨度2天 - 3600(1小时)：最大查询跨度7天 - 86400(1天)：最大查询跨度31天 - 如果不传，默认取对应时间跨度的最小间隔。
        :type interval: int
        :param group_by: 数据分组方式，可选domain，默认不分组。
        :type group_by: str
        :param service_area: 服务区域：mainland_china（默认）、outside_mainland_china，当查询回源类指标时该参数无效。
        :type service_area: str
        :param enterprise_project_id: 当用户开启企业项目功能时，该参数生效，表示查询资源所属项目，\&quot;all\&quot;表示所有项目。注意：当使用子帐号调用接口时，该参数必传。  您可以通过调用企业项目管理服务（EPS）的查询企业项目列表接口（ListEnterpriseProject）查询企业项目id。
        :type enterprise_project_id: str
        """
        
        

        self._action = None
        self._start_time = None
        self._end_time = None
        self._domain_name = None
        self._stat_type = None
        self._interval = None
        self._group_by = None
        self._service_area = None
        self._enterprise_project_id = None
        self.discriminator = None

        self.action = action
        self.start_time = start_time
        self.end_time = end_time
        self.domain_name = domain_name
        self.stat_type = stat_type
        if interval is not None:
            self.interval = interval
        if group_by is not None:
            self.group_by = group_by
        if service_area is not None:
            self.service_area = service_area
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id

    @property
    def action(self):
        r"""Gets the action of this ShowDomainStatsRequest.

        - 动作名称，可选summary、detail。 - summary：查询汇总数据 - detail：查询数据详情。

        :return: The action of this ShowDomainStatsRequest.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this ShowDomainStatsRequest.

        - 动作名称，可选summary、detail。 - summary：查询汇总数据 - detail：查询数据详情。

        :param action: The action of this ShowDomainStatsRequest.
        :type action: str
        """
        self._action = action

    @property
    def start_time(self):
        r"""Gets the start_time of this ShowDomainStatsRequest.

        - 查询起始时间戳，需与结束时间戳同时指定，左闭右开，设置方式如下：  - interval为300时，start_time设置为整5分钟时刻点，如：1631240100000(对应2021-09-10 10:15:00)  - interval为3600时，start_time设置为整小时时刻点，如：1631239200000(对应2021-09-10 10:00:00)  - interval为86400时，start_time设置为东8区零点时刻点，如：1631203200000(对应2021-09-10 00:00:00)

        :return: The start_time of this ShowDomainStatsRequest.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ShowDomainStatsRequest.

        - 查询起始时间戳，需与结束时间戳同时指定，左闭右开，设置方式如下：  - interval为300时，start_time设置为整5分钟时刻点，如：1631240100000(对应2021-09-10 10:15:00)  - interval为3600时，start_time设置为整小时时刻点，如：1631239200000(对应2021-09-10 10:00:00)  - interval为86400时，start_time设置为东8区零点时刻点，如：1631203200000(对应2021-09-10 00:00:00)

        :param start_time: The start_time of this ShowDomainStatsRequest.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ShowDomainStatsRequest.

        - 查询结束时间戳，需与开始时间戳同时指定，左闭右开，设置方式如下：  - interval为300时，end_time设置为整5分钟时刻点，如：1631243700000(对应2021-09-10 11:15:00)  - interval为3600时，end_time设置为整小时时刻点，如：1631325600000(对应2021-09-11 10:00:00)  - interval为86400时，end_time设置为东8区零点时刻点，如：1631376000000(对应2021-09-12 00:00:00)

        :return: The end_time of this ShowDomainStatsRequest.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ShowDomainStatsRequest.

        - 查询结束时间戳，需与开始时间戳同时指定，左闭右开，设置方式如下：  - interval为300时，end_time设置为整5分钟时刻点，如：1631243700000(对应2021-09-10 11:15:00)  - interval为3600时，end_time设置为整小时时刻点，如：1631325600000(对应2021-09-11 10:00:00)  - interval为86400时，end_time设置为东8区零点时刻点，如：1631376000000(对应2021-09-12 00:00:00)

        :param end_time: The end_time of this ShowDomainStatsRequest.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def domain_name(self):
        r"""Gets the domain_name of this ShowDomainStatsRequest.

        域名列表，多个域名以逗号（半角）分隔，如：www.test1.com,www.test2.com，all表示查询名下全部域名。如果域名在查询时间段内无数据，结果将不返回该域名的信息。

        :return: The domain_name of this ShowDomainStatsRequest.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        r"""Sets the domain_name of this ShowDomainStatsRequest.

        域名列表，多个域名以逗号（半角）分隔，如：www.test1.com,www.test2.com，all表示查询名下全部域名。如果域名在查询时间段内无数据，结果将不返回该域名的信息。

        :param domain_name: The domain_name of this ShowDomainStatsRequest.
        :type domain_name: str
        """
        self._domain_name = domain_name

    @property
    def stat_type(self):
        r"""Gets the stat_type of this ShowDomainStatsRequest.

        - 网络资源消耗：   - bw（带宽）   - flux（流量）   - bs_bw（回源带宽）   - bs_flux（回源流量） - 访问情况：   - req_num（请求总数）   - hit_num（请求命中次数）   - bs_num（回源总数）   - bs_fail_num（回源失败数）   - hit_flux（命中流量） - HTTP状态码（组合指标）：   - http_code_2xx（状态码汇总2xx）   - http_code_3xx（状态码汇总3xx）   - http_code_4xx（状态码汇总4xx）   - http_code_5xx（状态码汇总5xx）   - bs_http_code_2xx（回源状态码汇总2xx）   - bs_http_code_3xx（回源状态码汇总3xx）   - bs_http_code_4xx（回源状态码汇总4xx）   - bs_http_code_5xx（回源状态码汇总5xx）   - status_code_2xx（状态码详情2xx）   - status_code_3xx（状态码详情3xx）   - status_code_4xx（状态码详情4xx）   - status_code_5xx（状态码详情5xx）   - bs_status_code_2xx（回源状态码详情2xx）   - bs_status_code_3xx（回源状态码详情3xx）   - bs_status_code_4xx（回源状态码详情4xx）   - bs_status_code_5xx（回源状态码详情5xx）   - status_code和bs_status_code不能一起查询

        :return: The stat_type of this ShowDomainStatsRequest.
        :rtype: str
        """
        return self._stat_type

    @stat_type.setter
    def stat_type(self, stat_type):
        r"""Sets the stat_type of this ShowDomainStatsRequest.

        - 网络资源消耗：   - bw（带宽）   - flux（流量）   - bs_bw（回源带宽）   - bs_flux（回源流量） - 访问情况：   - req_num（请求总数）   - hit_num（请求命中次数）   - bs_num（回源总数）   - bs_fail_num（回源失败数）   - hit_flux（命中流量） - HTTP状态码（组合指标）：   - http_code_2xx（状态码汇总2xx）   - http_code_3xx（状态码汇总3xx）   - http_code_4xx（状态码汇总4xx）   - http_code_5xx（状态码汇总5xx）   - bs_http_code_2xx（回源状态码汇总2xx）   - bs_http_code_3xx（回源状态码汇总3xx）   - bs_http_code_4xx（回源状态码汇总4xx）   - bs_http_code_5xx（回源状态码汇总5xx）   - status_code_2xx（状态码详情2xx）   - status_code_3xx（状态码详情3xx）   - status_code_4xx（状态码详情4xx）   - status_code_5xx（状态码详情5xx）   - bs_status_code_2xx（回源状态码详情2xx）   - bs_status_code_3xx（回源状态码详情3xx）   - bs_status_code_4xx（回源状态码详情4xx）   - bs_status_code_5xx（回源状态码详情5xx）   - status_code和bs_status_code不能一起查询

        :param stat_type: The stat_type of this ShowDomainStatsRequest.
        :type stat_type: str
        """
        self._stat_type = stat_type

    @property
    def interval(self):
        r"""Gets the interval of this ShowDomainStatsRequest.

        - 查询时间间隔，单位：秒，取值说明： - 300(5分钟)：最大查询跨度2天 - 3600(1小时)：最大查询跨度7天 - 86400(1天)：最大查询跨度31天 - 如果不传，默认取对应时间跨度的最小间隔。

        :return: The interval of this ShowDomainStatsRequest.
        :rtype: int
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        r"""Sets the interval of this ShowDomainStatsRequest.

        - 查询时间间隔，单位：秒，取值说明： - 300(5分钟)：最大查询跨度2天 - 3600(1小时)：最大查询跨度7天 - 86400(1天)：最大查询跨度31天 - 如果不传，默认取对应时间跨度的最小间隔。

        :param interval: The interval of this ShowDomainStatsRequest.
        :type interval: int
        """
        self._interval = interval

    @property
    def group_by(self):
        r"""Gets the group_by of this ShowDomainStatsRequest.

        数据分组方式，可选domain，默认不分组。

        :return: The group_by of this ShowDomainStatsRequest.
        :rtype: str
        """
        return self._group_by

    @group_by.setter
    def group_by(self, group_by):
        r"""Sets the group_by of this ShowDomainStatsRequest.

        数据分组方式，可选domain，默认不分组。

        :param group_by: The group_by of this ShowDomainStatsRequest.
        :type group_by: str
        """
        self._group_by = group_by

    @property
    def service_area(self):
        r"""Gets the service_area of this ShowDomainStatsRequest.

        服务区域：mainland_china（默认）、outside_mainland_china，当查询回源类指标时该参数无效。

        :return: The service_area of this ShowDomainStatsRequest.
        :rtype: str
        """
        return self._service_area

    @service_area.setter
    def service_area(self, service_area):
        r"""Sets the service_area of this ShowDomainStatsRequest.

        服务区域：mainland_china（默认）、outside_mainland_china，当查询回源类指标时该参数无效。

        :param service_area: The service_area of this ShowDomainStatsRequest.
        :type service_area: str
        """
        self._service_area = service_area

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ShowDomainStatsRequest.

        当用户开启企业项目功能时，该参数生效，表示查询资源所属项目，\"all\"表示所有项目。注意：当使用子帐号调用接口时，该参数必传。  您可以通过调用企业项目管理服务（EPS）的查询企业项目列表接口（ListEnterpriseProject）查询企业项目id。

        :return: The enterprise_project_id of this ShowDomainStatsRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ShowDomainStatsRequest.

        当用户开启企业项目功能时，该参数生效，表示查询资源所属项目，\"all\"表示所有项目。注意：当使用子帐号调用接口时，该参数必传。  您可以通过调用企业项目管理服务（EPS）的查询企业项目列表接口（ListEnterpriseProject）查询企业项目id。

        :param enterprise_project_id: The enterprise_project_id of this ShowDomainStatsRequest.
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
        if not isinstance(other, ShowDomainStatsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
