# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DownloadStatisticsExcelRequest:

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
        'excel_language': 'str',
        'service_area': 'str',
        'interval': 'int',
        'enterprise_project_id': 'str',
        'excel_type': 'str'
    }

    attribute_map = {
        'start_time': 'start_time',
        'end_time': 'end_time',
        'domain_name': 'domain_name',
        'excel_language': 'excel_language',
        'service_area': 'service_area',
        'interval': 'interval',
        'enterprise_project_id': 'enterprise_project_id',
        'excel_type': 'excel_type'
    }

    def __init__(self, start_time=None, end_time=None, domain_name=None, excel_language=None, service_area=None, interval=None, enterprise_project_id=None, excel_type=None):
        """DownloadStatisticsExcelRequest

        The model defined in huaweicloud sdk

        :param start_time: - 查询起始时间戳，时间戳应设置需为整5分钟，设置方式如下： - interval为300时，start_time设置为整5分钟时刻点，如：1631240100000(对应2021-09-10 10:15:00) - interval为3600时，start_time设置为整小时时刻点，如：1631239200000(对应2021-09-10 10:00:00) - interval为86400时，start_time设置为东8区零点时刻点，如：1631203200000(对应2021-09-10 00:00:00)
        :type start_time: int
        :param end_time: - 查询结束时间戳，时间戳应设置需为整5分钟，设置方式如下： - interval为300时，end_time设置为整5分钟时刻点，如：1631243700000(对应2021-09-10 11:15:00) - interval为3600时，end_time设置为整小时时刻点，如：1631325600000(对应2021-09-11 10:00:00) - interval为86400时，end_time设置为东8区零点时刻点，如：1631376000000(对应2021-09-12 00:00:00)
        :type end_time: int
        :param domain_name: 域名列表，多个域名以逗号（半角）分隔，如：www.test1.com,www.test2.com all表示查询名下全部域名
        :type domain_name: str
        :param excel_language: 创建表格语言，支持zh(中文)，en(英文)两种，如果不传默认为zh
        :type excel_language: str
        :param service_area: 服务区域：mainland_china（默认）、outside_mainland_china，当查询回源类指标时该参数无效。
        :type service_area: str
        :param interval: - 查询时间间隔，单位：秒，取值说明： - 300(5分钟)：最大查询跨度2天 - 3600(1小时)：最大查询跨度7天 - 86400(1天)：最大查询跨度31天 - 如果不传，默认取对应时间跨度的最小间隔。
        :type interval: int
        :param enterprise_project_id: 当用户开启企业项目功能时，该参数生效，表示查询资源所属项目，\&quot;all\&quot;表示所有项目。注意：当使用子账号调用接口时，该参数必传。
        :type enterprise_project_id: str
        :param excel_type: 统计数据表格类型,目前支持 - 用量统计数据(excel_type_usage) - 访问情况统计数据(excel_type_access) - 回源情况统计数据（excel_type_origin） - http_code统计数据(excel_type_http_code)
        :type excel_type: str
        """
        
        

        self._start_time = None
        self._end_time = None
        self._domain_name = None
        self._excel_language = None
        self._service_area = None
        self._interval = None
        self._enterprise_project_id = None
        self._excel_type = None
        self.discriminator = None

        self.start_time = start_time
        self.end_time = end_time
        self.domain_name = domain_name
        if excel_language is not None:
            self.excel_language = excel_language
        if service_area is not None:
            self.service_area = service_area
        if interval is not None:
            self.interval = interval
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        self.excel_type = excel_type

    @property
    def start_time(self):
        """Gets the start_time of this DownloadStatisticsExcelRequest.

        - 查询起始时间戳，时间戳应设置需为整5分钟，设置方式如下： - interval为300时，start_time设置为整5分钟时刻点，如：1631240100000(对应2021-09-10 10:15:00) - interval为3600时，start_time设置为整小时时刻点，如：1631239200000(对应2021-09-10 10:00:00) - interval为86400时，start_time设置为东8区零点时刻点，如：1631203200000(对应2021-09-10 00:00:00)

        :return: The start_time of this DownloadStatisticsExcelRequest.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this DownloadStatisticsExcelRequest.

        - 查询起始时间戳，时间戳应设置需为整5分钟，设置方式如下： - interval为300时，start_time设置为整5分钟时刻点，如：1631240100000(对应2021-09-10 10:15:00) - interval为3600时，start_time设置为整小时时刻点，如：1631239200000(对应2021-09-10 10:00:00) - interval为86400时，start_time设置为东8区零点时刻点，如：1631203200000(对应2021-09-10 00:00:00)

        :param start_time: The start_time of this DownloadStatisticsExcelRequest.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this DownloadStatisticsExcelRequest.

        - 查询结束时间戳，时间戳应设置需为整5分钟，设置方式如下： - interval为300时，end_time设置为整5分钟时刻点，如：1631243700000(对应2021-09-10 11:15:00) - interval为3600时，end_time设置为整小时时刻点，如：1631325600000(对应2021-09-11 10:00:00) - interval为86400时，end_time设置为东8区零点时刻点，如：1631376000000(对应2021-09-12 00:00:00)

        :return: The end_time of this DownloadStatisticsExcelRequest.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this DownloadStatisticsExcelRequest.

        - 查询结束时间戳，时间戳应设置需为整5分钟，设置方式如下： - interval为300时，end_time设置为整5分钟时刻点，如：1631243700000(对应2021-09-10 11:15:00) - interval为3600时，end_time设置为整小时时刻点，如：1631325600000(对应2021-09-11 10:00:00) - interval为86400时，end_time设置为东8区零点时刻点，如：1631376000000(对应2021-09-12 00:00:00)

        :param end_time: The end_time of this DownloadStatisticsExcelRequest.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def domain_name(self):
        """Gets the domain_name of this DownloadStatisticsExcelRequest.

        域名列表，多个域名以逗号（半角）分隔，如：www.test1.com,www.test2.com all表示查询名下全部域名

        :return: The domain_name of this DownloadStatisticsExcelRequest.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        """Sets the domain_name of this DownloadStatisticsExcelRequest.

        域名列表，多个域名以逗号（半角）分隔，如：www.test1.com,www.test2.com all表示查询名下全部域名

        :param domain_name: The domain_name of this DownloadStatisticsExcelRequest.
        :type domain_name: str
        """
        self._domain_name = domain_name

    @property
    def excel_language(self):
        """Gets the excel_language of this DownloadStatisticsExcelRequest.

        创建表格语言，支持zh(中文)，en(英文)两种，如果不传默认为zh

        :return: The excel_language of this DownloadStatisticsExcelRequest.
        :rtype: str
        """
        return self._excel_language

    @excel_language.setter
    def excel_language(self, excel_language):
        """Sets the excel_language of this DownloadStatisticsExcelRequest.

        创建表格语言，支持zh(中文)，en(英文)两种，如果不传默认为zh

        :param excel_language: The excel_language of this DownloadStatisticsExcelRequest.
        :type excel_language: str
        """
        self._excel_language = excel_language

    @property
    def service_area(self):
        """Gets the service_area of this DownloadStatisticsExcelRequest.

        服务区域：mainland_china（默认）、outside_mainland_china，当查询回源类指标时该参数无效。

        :return: The service_area of this DownloadStatisticsExcelRequest.
        :rtype: str
        """
        return self._service_area

    @service_area.setter
    def service_area(self, service_area):
        """Sets the service_area of this DownloadStatisticsExcelRequest.

        服务区域：mainland_china（默认）、outside_mainland_china，当查询回源类指标时该参数无效。

        :param service_area: The service_area of this DownloadStatisticsExcelRequest.
        :type service_area: str
        """
        self._service_area = service_area

    @property
    def interval(self):
        """Gets the interval of this DownloadStatisticsExcelRequest.

        - 查询时间间隔，单位：秒，取值说明： - 300(5分钟)：最大查询跨度2天 - 3600(1小时)：最大查询跨度7天 - 86400(1天)：最大查询跨度31天 - 如果不传，默认取对应时间跨度的最小间隔。

        :return: The interval of this DownloadStatisticsExcelRequest.
        :rtype: int
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        """Sets the interval of this DownloadStatisticsExcelRequest.

        - 查询时间间隔，单位：秒，取值说明： - 300(5分钟)：最大查询跨度2天 - 3600(1小时)：最大查询跨度7天 - 86400(1天)：最大查询跨度31天 - 如果不传，默认取对应时间跨度的最小间隔。

        :param interval: The interval of this DownloadStatisticsExcelRequest.
        :type interval: int
        """
        self._interval = interval

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this DownloadStatisticsExcelRequest.

        当用户开启企业项目功能时，该参数生效，表示查询资源所属项目，\"all\"表示所有项目。注意：当使用子账号调用接口时，该参数必传。

        :return: The enterprise_project_id of this DownloadStatisticsExcelRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this DownloadStatisticsExcelRequest.

        当用户开启企业项目功能时，该参数生效，表示查询资源所属项目，\"all\"表示所有项目。注意：当使用子账号调用接口时，该参数必传。

        :param enterprise_project_id: The enterprise_project_id of this DownloadStatisticsExcelRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def excel_type(self):
        """Gets the excel_type of this DownloadStatisticsExcelRequest.

        统计数据表格类型,目前支持 - 用量统计数据(excel_type_usage) - 访问情况统计数据(excel_type_access) - 回源情况统计数据（excel_type_origin） - http_code统计数据(excel_type_http_code)

        :return: The excel_type of this DownloadStatisticsExcelRequest.
        :rtype: str
        """
        return self._excel_type

    @excel_type.setter
    def excel_type(self, excel_type):
        """Sets the excel_type of this DownloadStatisticsExcelRequest.

        统计数据表格类型,目前支持 - 用量统计数据(excel_type_usage) - 访问情况统计数据(excel_type_access) - 回源情况统计数据（excel_type_origin） - http_code统计数据(excel_type_http_code)

        :param excel_type: The excel_type of this DownloadStatisticsExcelRequest.
        :type excel_type: str
        """
        self._excel_type = excel_type

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
        if not isinstance(other, DownloadStatisticsExcelRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
