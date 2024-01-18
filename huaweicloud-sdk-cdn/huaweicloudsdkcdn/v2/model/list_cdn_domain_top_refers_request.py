# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCdnDomainTopRefersRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'start_time': 'int',
        'end_time': 'int',
        'domain_name': 'str',
        'stat_type': 'str',
        'service_area': 'str',
        'enterprise_project_id': 'str',
        'include_ratio': 'bool'
    }

    attribute_map = {
        'start_time': 'start_time',
        'end_time': 'end_time',
        'domain_name': 'domain_name',
        'stat_type': 'stat_type',
        'service_area': 'service_area',
        'enterprise_project_id': 'enterprise_project_id',
        'include_ratio': 'include_ratio'
    }

    def __init__(self, start_time=None, end_time=None, domain_name=None, stat_type=None, service_area=None, enterprise_project_id=None, include_ratio=None):
        """ListCdnDomainTopRefersRequest

        The model defined in huaweicloud sdk

        :param start_time: 查询起始时间戳，需与结束时间戳同时指定，左闭右开，设置方式如下： - interval为300时，start_time设置为整5分钟时刻点，如：1631240100000(对应2021-09-10 10:15:00) - interval为3600时，start_time设置为整小时时刻点，如：1631239200000(对应2021-09-10 10:00:00) - interval为86400时，start_time设置为东8区零点时刻点，如：1631203200000(对应2021-09-10 00:00:00)
        :type start_time: int
        :param end_time: 查询结束时间戳，需与开始时间戳同时指定，左闭右开，设置方式如下： - interval为300时，end_time设置为整5分钟时刻点，如：1631243700000(对应2021-09-10 11:15:00) - interval为3600时，end_time设置为整小时时刻点，如：1631325600000(对应2021-09-11 10:00:00) - interval为86400时，end_time设置为东8区零点时刻点，如：1631376000000(对应2021-09-12 00:00:00)
        :type end_time: int
        :param domain_name: 域名列表，多个域名以逗号（半角）分隔，如：www.test1.com,www.test2.com all表示查询名下全部域名。如果域名在查询时间段内无数据，结果将不返回该域名的信息。
        :type domain_name: str
        :param stat_type: - 统计指标类型 - 目前只支持flux（流量），req_num（请求数）
        :type stat_type: str
        :param service_area: 服务区域：mainland_china(大陆)，outside_mainland_china(海外)，默认为global(全球)
        :type service_area: str
        :param enterprise_project_id: 当用户开启企业项目功能时，该参数生效，表示查询资源所属项目，\&quot;all\&quot;表示所有项目。注意：当使用子账号调用接口时，该参数必传。
        :type enterprise_project_id: str
        :param include_ratio: 是否包含百分比数据，默认false
        :type include_ratio: bool
        """
        
        

        self._start_time = None
        self._end_time = None
        self._domain_name = None
        self._stat_type = None
        self._service_area = None
        self._enterprise_project_id = None
        self._include_ratio = None
        self.discriminator = None

        self.start_time = start_time
        self.end_time = end_time
        self.domain_name = domain_name
        self.stat_type = stat_type
        if service_area is not None:
            self.service_area = service_area
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if include_ratio is not None:
            self.include_ratio = include_ratio

    @property
    def start_time(self):
        """Gets the start_time of this ListCdnDomainTopRefersRequest.

        查询起始时间戳，需与结束时间戳同时指定，左闭右开，设置方式如下： - interval为300时，start_time设置为整5分钟时刻点，如：1631240100000(对应2021-09-10 10:15:00) - interval为3600时，start_time设置为整小时时刻点，如：1631239200000(对应2021-09-10 10:00:00) - interval为86400时，start_time设置为东8区零点时刻点，如：1631203200000(对应2021-09-10 00:00:00)

        :return: The start_time of this ListCdnDomainTopRefersRequest.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ListCdnDomainTopRefersRequest.

        查询起始时间戳，需与结束时间戳同时指定，左闭右开，设置方式如下： - interval为300时，start_time设置为整5分钟时刻点，如：1631240100000(对应2021-09-10 10:15:00) - interval为3600时，start_time设置为整小时时刻点，如：1631239200000(对应2021-09-10 10:00:00) - interval为86400时，start_time设置为东8区零点时刻点，如：1631203200000(对应2021-09-10 00:00:00)

        :param start_time: The start_time of this ListCdnDomainTopRefersRequest.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this ListCdnDomainTopRefersRequest.

        查询结束时间戳，需与开始时间戳同时指定，左闭右开，设置方式如下： - interval为300时，end_time设置为整5分钟时刻点，如：1631243700000(对应2021-09-10 11:15:00) - interval为3600时，end_time设置为整小时时刻点，如：1631325600000(对应2021-09-11 10:00:00) - interval为86400时，end_time设置为东8区零点时刻点，如：1631376000000(对应2021-09-12 00:00:00)

        :return: The end_time of this ListCdnDomainTopRefersRequest.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ListCdnDomainTopRefersRequest.

        查询结束时间戳，需与开始时间戳同时指定，左闭右开，设置方式如下： - interval为300时，end_time设置为整5分钟时刻点，如：1631243700000(对应2021-09-10 11:15:00) - interval为3600时，end_time设置为整小时时刻点，如：1631325600000(对应2021-09-11 10:00:00) - interval为86400时，end_time设置为东8区零点时刻点，如：1631376000000(对应2021-09-12 00:00:00)

        :param end_time: The end_time of this ListCdnDomainTopRefersRequest.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def domain_name(self):
        """Gets the domain_name of this ListCdnDomainTopRefersRequest.

        域名列表，多个域名以逗号（半角）分隔，如：www.test1.com,www.test2.com all表示查询名下全部域名。如果域名在查询时间段内无数据，结果将不返回该域名的信息。

        :return: The domain_name of this ListCdnDomainTopRefersRequest.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        """Sets the domain_name of this ListCdnDomainTopRefersRequest.

        域名列表，多个域名以逗号（半角）分隔，如：www.test1.com,www.test2.com all表示查询名下全部域名。如果域名在查询时间段内无数据，结果将不返回该域名的信息。

        :param domain_name: The domain_name of this ListCdnDomainTopRefersRequest.
        :type domain_name: str
        """
        self._domain_name = domain_name

    @property
    def stat_type(self):
        """Gets the stat_type of this ListCdnDomainTopRefersRequest.

        - 统计指标类型 - 目前只支持flux（流量），req_num（请求数）

        :return: The stat_type of this ListCdnDomainTopRefersRequest.
        :rtype: str
        """
        return self._stat_type

    @stat_type.setter
    def stat_type(self, stat_type):
        """Sets the stat_type of this ListCdnDomainTopRefersRequest.

        - 统计指标类型 - 目前只支持flux（流量），req_num（请求数）

        :param stat_type: The stat_type of this ListCdnDomainTopRefersRequest.
        :type stat_type: str
        """
        self._stat_type = stat_type

    @property
    def service_area(self):
        """Gets the service_area of this ListCdnDomainTopRefersRequest.

        服务区域：mainland_china(大陆)，outside_mainland_china(海外)，默认为global(全球)

        :return: The service_area of this ListCdnDomainTopRefersRequest.
        :rtype: str
        """
        return self._service_area

    @service_area.setter
    def service_area(self, service_area):
        """Sets the service_area of this ListCdnDomainTopRefersRequest.

        服务区域：mainland_china(大陆)，outside_mainland_china(海外)，默认为global(全球)

        :param service_area: The service_area of this ListCdnDomainTopRefersRequest.
        :type service_area: str
        """
        self._service_area = service_area

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ListCdnDomainTopRefersRequest.

        当用户开启企业项目功能时，该参数生效，表示查询资源所属项目，\"all\"表示所有项目。注意：当使用子账号调用接口时，该参数必传。

        :return: The enterprise_project_id of this ListCdnDomainTopRefersRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ListCdnDomainTopRefersRequest.

        当用户开启企业项目功能时，该参数生效，表示查询资源所属项目，\"all\"表示所有项目。注意：当使用子账号调用接口时，该参数必传。

        :param enterprise_project_id: The enterprise_project_id of this ListCdnDomainTopRefersRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def include_ratio(self):
        """Gets the include_ratio of this ListCdnDomainTopRefersRequest.

        是否包含百分比数据，默认false

        :return: The include_ratio of this ListCdnDomainTopRefersRequest.
        :rtype: bool
        """
        return self._include_ratio

    @include_ratio.setter
    def include_ratio(self, include_ratio):
        """Sets the include_ratio of this ListCdnDomainTopRefersRequest.

        是否包含百分比数据，默认false

        :param include_ratio: The include_ratio of this ListCdnDomainTopRefersRequest.
        :type include_ratio: bool
        """
        self._include_ratio = include_ratio

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
        if not isinstance(other, ListCdnDomainTopRefersRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
