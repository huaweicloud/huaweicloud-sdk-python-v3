# coding: utf-8

import re
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
        'interval': 'int',
        'domain_name': 'str',
        'stat_type': 'str',
        'group_by': 'str',
        'country': 'str',
        'district': 'str',
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
        'district': 'district',
        'isp': 'isp',
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, action=None, start_time=None, end_time=None, interval=None, domain_name=None, stat_type=None, group_by=None, country=None, district=None, isp=None, enterprise_project_id=None):
        """ShowDomainStatsRequest - a model defined in huaweicloud sdk"""
        
        

        self._action = None
        self._start_time = None
        self._end_time = None
        self._interval = None
        self._domain_name = None
        self._stat_type = None
        self._group_by = None
        self._country = None
        self._district = None
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
        if district is not None:
            self.district = district
        if isp is not None:
            self.isp = isp
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id

    @property
    def action(self):
        """Gets the action of this ShowDomainStatsRequest.

        查询类型，可选location_summary,location_detail  location_summary：查询汇总数据 location_detail：查询数据详情 

        :return: The action of this ShowDomainStatsRequest.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this ShowDomainStatsRequest.

        查询类型，可选location_summary,location_detail  location_summary：查询汇总数据 location_detail：查询数据详情 

        :param action: The action of this ShowDomainStatsRequest.
        :type: str
        """
        self._action = action

    @property
    def start_time(self):
        """Gets the start_time of this ShowDomainStatsRequest.

        查询起始时间戳， 时间戳应设置需为整5分钟或整小时时刻点，设置方式如下  interval为300时，start_time设置为整5分钟时刻点，如：1631240100000(对应2021-09-10 10:15:00) interval大于等于3600时，start_time设置为整小时时刻点，如：1631239200000(对应2021-09-10 10:00:00) 

        :return: The start_time of this ShowDomainStatsRequest.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ShowDomainStatsRequest.

        查询起始时间戳， 时间戳应设置需为整5分钟或整小时时刻点，设置方式如下  interval为300时，start_time设置为整5分钟时刻点，如：1631240100000(对应2021-09-10 10:15:00) interval大于等于3600时，start_time设置为整小时时刻点，如：1631239200000(对应2021-09-10 10:00:00) 

        :param start_time: The start_time of this ShowDomainStatsRequest.
        :type: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this ShowDomainStatsRequest.

        查询结束时间戳， 时间戳应设置需为整5分钟或整小时时刻点，设置方式如下  interval为300时，end_time设置为整5分钟时刻点，如：1631243700000(对应2021-09-11 10:15:00) interval大于等于3600时，end_time设置为整小时时刻点，如：1631325600000(对应2021-09-11 10:00:00) 

        :return: The end_time of this ShowDomainStatsRequest.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ShowDomainStatsRequest.

        查询结束时间戳， 时间戳应设置需为整5分钟或整小时时刻点，设置方式如下  interval为300时，end_time设置为整5分钟时刻点，如：1631243700000(对应2021-09-11 10:15:00) interval大于等于3600时，end_time设置为整小时时刻点，如：1631325600000(对应2021-09-11 10:00:00) 

        :param end_time: The end_time of this ShowDomainStatsRequest.
        :type: int
        """
        self._end_time = end_time

    @property
    def interval(self):
        """Gets the interval of this ShowDomainStatsRequest.

        查询时间间隔，单位为秒，可设置值300(5分钟),3600(1小时),14400(4小时)等

        :return: The interval of this ShowDomainStatsRequest.
        :rtype: int
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        """Sets the interval of this ShowDomainStatsRequest.

        查询时间间隔，单位为秒，可设置值300(5分钟),3600(1小时),14400(4小时)等

        :param interval: The interval of this ShowDomainStatsRequest.
        :type: int
        """
        self._interval = interval

    @property
    def domain_name(self):
        """Gets the domain_name of this ShowDomainStatsRequest.

        域名列表，多个域名以逗号（半角）分隔，如：www.test1.com,www.test2.com，all表示查询名下全部域名

        :return: The domain_name of this ShowDomainStatsRequest.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        """Sets the domain_name of this ShowDomainStatsRequest.

        域名列表，多个域名以逗号（半角）分隔，如：www.test1.com,www.test2.com，all表示查询名下全部域名

        :param domain_name: The domain_name of this ShowDomainStatsRequest.
        :type: str
        """
        self._domain_name = domain_name

    @property
    def stat_type(self):
        """Gets the stat_type of this ShowDomainStatsRequest.

        网络资源消耗： - bw（带宽） - flux（流量）  HTTP状态码（组合指标）： - status_code_2xx（状态码详情2xx） - status_code_3xx（状态码详情3xx） - status_code_4xx（状态码详情4xx） - status_code_5xx（状态码详情5xx） - bs_status_code_2xx（回源状态码详情2xx） - bs_status_code_3xx（回源状态码详情3xx） - bs_status_code_4xx（回源状态码详情4xx） - bs_status_code_5xx（回源状态码详情5xx） - status_code和bs_status_code不能一起查询，否则数据会不准确，status_code不支持指定服务区域

        :return: The stat_type of this ShowDomainStatsRequest.
        :rtype: str
        """
        return self._stat_type

    @stat_type.setter
    def stat_type(self, stat_type):
        """Sets the stat_type of this ShowDomainStatsRequest.

        网络资源消耗： - bw（带宽） - flux（流量）  HTTP状态码（组合指标）： - status_code_2xx（状态码详情2xx） - status_code_3xx（状态码详情3xx） - status_code_4xx（状态码详情4xx） - status_code_5xx（状态码详情5xx） - bs_status_code_2xx（回源状态码详情2xx） - bs_status_code_3xx（回源状态码详情3xx） - bs_status_code_4xx（回源状态码详情4xx） - bs_status_code_5xx（回源状态码详情5xx） - status_code和bs_status_code不能一起查询，否则数据会不准确，status_code不支持指定服务区域

        :param stat_type: The stat_type of this ShowDomainStatsRequest.
        :type: str
        """
        self._stat_type = stat_type

    @property
    def group_by(self):
        """Gets the group_by of this ShowDomainStatsRequest.

        数据分组方式，多个以英文逗号分隔，可选domain,country,district,isp，默认不分组

        :return: The group_by of this ShowDomainStatsRequest.
        :rtype: str
        """
        return self._group_by

    @group_by.setter
    def group_by(self, group_by):
        """Sets the group_by of this ShowDomainStatsRequest.

        数据分组方式，多个以英文逗号分隔，可选domain,country,district,isp，默认不分组

        :param group_by: The group_by of this ShowDomainStatsRequest.
        :type: str
        """
        self._group_by = group_by

    @property
    def country(self):
        """Gets the country of this ShowDomainStatsRequest.

        需要过滤的国家编码，多个以英文逗号分隔，all表示全部

        :return: The country of this ShowDomainStatsRequest.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this ShowDomainStatsRequest.

        需要过滤的国家编码，多个以英文逗号分隔，all表示全部

        :param country: The country of this ShowDomainStatsRequest.
        :type: str
        """
        self._country = country

    @property
    def district(self):
        """Gets the district of this ShowDomainStatsRequest.

        需要过滤的地区编码，多个以英文逗号分隔，all表示全部，仅仅country字段为cn时设置才合法

        :return: The district of this ShowDomainStatsRequest.
        :rtype: str
        """
        return self._district

    @district.setter
    def district(self, district):
        """Sets the district of this ShowDomainStatsRequest.

        需要过滤的地区编码，多个以英文逗号分隔，all表示全部，仅仅country字段为cn时设置才合法

        :param district: The district of this ShowDomainStatsRequest.
        :type: str
        """
        self._district = district

    @property
    def isp(self):
        """Gets the isp of this ShowDomainStatsRequest.

        需要过滤的运营商编码，多个以英文逗号分隔，all表示全部

        :return: The isp of this ShowDomainStatsRequest.
        :rtype: str
        """
        return self._isp

    @isp.setter
    def isp(self, isp):
        """Sets the isp of this ShowDomainStatsRequest.

        需要过滤的运营商编码，多个以英文逗号分隔，all表示全部

        :param isp: The isp of this ShowDomainStatsRequest.
        :type: str
        """
        self._isp = isp

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ShowDomainStatsRequest.

        当用户开启企业项目功能时，该参数生效，表示资源所属企业项目，不传表示默认项目。

        :return: The enterprise_project_id of this ShowDomainStatsRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ShowDomainStatsRequest.

        当用户开启企业项目功能时，该参数生效，表示资源所属企业项目，不传表示默认项目。

        :param enterprise_project_id: The enterprise_project_id of this ShowDomainStatsRequest.
        :type: str
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
