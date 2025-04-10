# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DownloadRegionCarrierExcelRequest:

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
        'interval': 'int',
        'country': 'str',
        'excel_language': 'str',
        'enterprise_project_id': 'str',
        'excel_type': 'str',
        'region': 'str',
        'carrier': 'str'
    }

    attribute_map = {
        'start_time': 'start_time',
        'end_time': 'end_time',
        'domain_name': 'domain_name',
        'interval': 'interval',
        'country': 'country',
        'excel_language': 'excel_language',
        'enterprise_project_id': 'enterprise_project_id',
        'excel_type': 'excel_type',
        'region': 'region',
        'carrier': 'carrier'
    }

    def __init__(self, start_time=None, end_time=None, domain_name=None, interval=None, country=None, excel_language=None, enterprise_project_id=None, excel_type=None, region=None, carrier=None):
        r"""DownloadRegionCarrierExcelRequest

        The model defined in huaweicloud sdk

        :param start_time: 查询起始时间戳，需与结束时间戳同时指定，左闭右开，设置方式如下： - interval为300时，start_time设置为整5分钟时刻点，如：1631240100000(对应2021-09-10 10:15:00) - interval为3600时，start_time设置为整小时时刻点，如：1631239200000(对应2021-09-10 10:00:00) - interval为86400时，start_time设置为东8区零点时刻点，如：1631203200000(对应2021-09-10 00:00:00)
        :type start_time: int
        :param end_time: 查询结束时间戳，需与开始时间戳同时指定，左闭右开，设置方式如下： - interval为300时，end_time设置为整5分钟时刻点，如：1631243700000(对应2021-09-10 11:15:00) - interval为3600时，end_time设置为整小时时刻点，如：1631325600000(对应2021-09-11 10:00:00) - interval为86400时，end_time设置为东8区零点时刻点，如：1631376000000(对应2021-09-12 00:00:00)
        :type end_time: int
        :param domain_name: 域名列表，多个域名以逗号（半角）分隔，如：www.test1.com,www.test2.com all表示查询名下全部域名。如果域名在查询时间段内无数据，结果将不返回该域名的信息。
        :type domain_name: str
        :param interval: - 查询时间间隔，单位：秒，取值说明： - 300(5分钟)：最大查询跨度2天 - 3600(1小时)：最大查询跨度7天 - 86400(1天)：最大查询跨度31天 - 如果不传，默认取对应时间跨度的最小间隔。
        :type interval: int
        :param country: - 国家&amp;地区编码，多个以英文逗号分隔，all表示全部，取值见附录 - 访问运营商统计数据时不能填写 - 访问top_url数据时不能填写 - 访问区域情况数据时只能填写cn(中国)
        :type country: str
        :param excel_language: 创建表格语言，支持zh(中文)，en(英文)两种，如果不传默认为zh
        :type excel_language: str
        :param enterprise_project_id: 当用户开启企业项目功能时，该参数生效，表示查询资源所属项目，\&quot;all\&quot;表示所有项目。注意：当使用子账号调用接口时，该参数必传。
        :type enterprise_project_id: str
        :param excel_type: 统计数据表格类型,目前支持 - 区域用量统计数据(excel_type_usage) - 区域访问情况统计数据(excel_type_access) - 区域情况统计数据（excel_type_region） - 区域运营商情况统计数据(excel_type_carrier) - 国家情况统计数据(excel_type_country) - top_url统计数据(excel_type_top_url)
        :type excel_type: str
        :param region: - 地区区域,当country为cn（中国）时有效 - 访问运营商统计数据时不能填写 - 访问国家统计数据时不能填写 - 访问top_url数据时不能填写
        :type region: str
        :param carrier: - 运营商编码 - 访问区域统计数据时不能填写 - 访问国家统计数据时不能填写 - 访问top_url数据时不能填写
        :type carrier: str
        """
        
        

        self._start_time = None
        self._end_time = None
        self._domain_name = None
        self._interval = None
        self._country = None
        self._excel_language = None
        self._enterprise_project_id = None
        self._excel_type = None
        self._region = None
        self._carrier = None
        self.discriminator = None

        self.start_time = start_time
        self.end_time = end_time
        self.domain_name = domain_name
        if interval is not None:
            self.interval = interval
        if country is not None:
            self.country = country
        if excel_language is not None:
            self.excel_language = excel_language
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        self.excel_type = excel_type
        if region is not None:
            self.region = region
        if carrier is not None:
            self.carrier = carrier

    @property
    def start_time(self):
        r"""Gets the start_time of this DownloadRegionCarrierExcelRequest.

        查询起始时间戳，需与结束时间戳同时指定，左闭右开，设置方式如下： - interval为300时，start_time设置为整5分钟时刻点，如：1631240100000(对应2021-09-10 10:15:00) - interval为3600时，start_time设置为整小时时刻点，如：1631239200000(对应2021-09-10 10:00:00) - interval为86400时，start_time设置为东8区零点时刻点，如：1631203200000(对应2021-09-10 00:00:00)

        :return: The start_time of this DownloadRegionCarrierExcelRequest.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this DownloadRegionCarrierExcelRequest.

        查询起始时间戳，需与结束时间戳同时指定，左闭右开，设置方式如下： - interval为300时，start_time设置为整5分钟时刻点，如：1631240100000(对应2021-09-10 10:15:00) - interval为3600时，start_time设置为整小时时刻点，如：1631239200000(对应2021-09-10 10:00:00) - interval为86400时，start_time设置为东8区零点时刻点，如：1631203200000(对应2021-09-10 00:00:00)

        :param start_time: The start_time of this DownloadRegionCarrierExcelRequest.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this DownloadRegionCarrierExcelRequest.

        查询结束时间戳，需与开始时间戳同时指定，左闭右开，设置方式如下： - interval为300时，end_time设置为整5分钟时刻点，如：1631243700000(对应2021-09-10 11:15:00) - interval为3600时，end_time设置为整小时时刻点，如：1631325600000(对应2021-09-11 10:00:00) - interval为86400时，end_time设置为东8区零点时刻点，如：1631376000000(对应2021-09-12 00:00:00)

        :return: The end_time of this DownloadRegionCarrierExcelRequest.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this DownloadRegionCarrierExcelRequest.

        查询结束时间戳，需与开始时间戳同时指定，左闭右开，设置方式如下： - interval为300时，end_time设置为整5分钟时刻点，如：1631243700000(对应2021-09-10 11:15:00) - interval为3600时，end_time设置为整小时时刻点，如：1631325600000(对应2021-09-11 10:00:00) - interval为86400时，end_time设置为东8区零点时刻点，如：1631376000000(对应2021-09-12 00:00:00)

        :param end_time: The end_time of this DownloadRegionCarrierExcelRequest.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def domain_name(self):
        r"""Gets the domain_name of this DownloadRegionCarrierExcelRequest.

        域名列表，多个域名以逗号（半角）分隔，如：www.test1.com,www.test2.com all表示查询名下全部域名。如果域名在查询时间段内无数据，结果将不返回该域名的信息。

        :return: The domain_name of this DownloadRegionCarrierExcelRequest.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        r"""Sets the domain_name of this DownloadRegionCarrierExcelRequest.

        域名列表，多个域名以逗号（半角）分隔，如：www.test1.com,www.test2.com all表示查询名下全部域名。如果域名在查询时间段内无数据，结果将不返回该域名的信息。

        :param domain_name: The domain_name of this DownloadRegionCarrierExcelRequest.
        :type domain_name: str
        """
        self._domain_name = domain_name

    @property
    def interval(self):
        r"""Gets the interval of this DownloadRegionCarrierExcelRequest.

        - 查询时间间隔，单位：秒，取值说明： - 300(5分钟)：最大查询跨度2天 - 3600(1小时)：最大查询跨度7天 - 86400(1天)：最大查询跨度31天 - 如果不传，默认取对应时间跨度的最小间隔。

        :return: The interval of this DownloadRegionCarrierExcelRequest.
        :rtype: int
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        r"""Sets the interval of this DownloadRegionCarrierExcelRequest.

        - 查询时间间隔，单位：秒，取值说明： - 300(5分钟)：最大查询跨度2天 - 3600(1小时)：最大查询跨度7天 - 86400(1天)：最大查询跨度31天 - 如果不传，默认取对应时间跨度的最小间隔。

        :param interval: The interval of this DownloadRegionCarrierExcelRequest.
        :type interval: int
        """
        self._interval = interval

    @property
    def country(self):
        r"""Gets the country of this DownloadRegionCarrierExcelRequest.

        - 国家&地区编码，多个以英文逗号分隔，all表示全部，取值见附录 - 访问运营商统计数据时不能填写 - 访问top_url数据时不能填写 - 访问区域情况数据时只能填写cn(中国)

        :return: The country of this DownloadRegionCarrierExcelRequest.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        r"""Sets the country of this DownloadRegionCarrierExcelRequest.

        - 国家&地区编码，多个以英文逗号分隔，all表示全部，取值见附录 - 访问运营商统计数据时不能填写 - 访问top_url数据时不能填写 - 访问区域情况数据时只能填写cn(中国)

        :param country: The country of this DownloadRegionCarrierExcelRequest.
        :type country: str
        """
        self._country = country

    @property
    def excel_language(self):
        r"""Gets the excel_language of this DownloadRegionCarrierExcelRequest.

        创建表格语言，支持zh(中文)，en(英文)两种，如果不传默认为zh

        :return: The excel_language of this DownloadRegionCarrierExcelRequest.
        :rtype: str
        """
        return self._excel_language

    @excel_language.setter
    def excel_language(self, excel_language):
        r"""Sets the excel_language of this DownloadRegionCarrierExcelRequest.

        创建表格语言，支持zh(中文)，en(英文)两种，如果不传默认为zh

        :param excel_language: The excel_language of this DownloadRegionCarrierExcelRequest.
        :type excel_language: str
        """
        self._excel_language = excel_language

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this DownloadRegionCarrierExcelRequest.

        当用户开启企业项目功能时，该参数生效，表示查询资源所属项目，\"all\"表示所有项目。注意：当使用子账号调用接口时，该参数必传。

        :return: The enterprise_project_id of this DownloadRegionCarrierExcelRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this DownloadRegionCarrierExcelRequest.

        当用户开启企业项目功能时，该参数生效，表示查询资源所属项目，\"all\"表示所有项目。注意：当使用子账号调用接口时，该参数必传。

        :param enterprise_project_id: The enterprise_project_id of this DownloadRegionCarrierExcelRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def excel_type(self):
        r"""Gets the excel_type of this DownloadRegionCarrierExcelRequest.

        统计数据表格类型,目前支持 - 区域用量统计数据(excel_type_usage) - 区域访问情况统计数据(excel_type_access) - 区域情况统计数据（excel_type_region） - 区域运营商情况统计数据(excel_type_carrier) - 国家情况统计数据(excel_type_country) - top_url统计数据(excel_type_top_url)

        :return: The excel_type of this DownloadRegionCarrierExcelRequest.
        :rtype: str
        """
        return self._excel_type

    @excel_type.setter
    def excel_type(self, excel_type):
        r"""Sets the excel_type of this DownloadRegionCarrierExcelRequest.

        统计数据表格类型,目前支持 - 区域用量统计数据(excel_type_usage) - 区域访问情况统计数据(excel_type_access) - 区域情况统计数据（excel_type_region） - 区域运营商情况统计数据(excel_type_carrier) - 国家情况统计数据(excel_type_country) - top_url统计数据(excel_type_top_url)

        :param excel_type: The excel_type of this DownloadRegionCarrierExcelRequest.
        :type excel_type: str
        """
        self._excel_type = excel_type

    @property
    def region(self):
        r"""Gets the region of this DownloadRegionCarrierExcelRequest.

        - 地区区域,当country为cn（中国）时有效 - 访问运营商统计数据时不能填写 - 访问国家统计数据时不能填写 - 访问top_url数据时不能填写

        :return: The region of this DownloadRegionCarrierExcelRequest.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this DownloadRegionCarrierExcelRequest.

        - 地区区域,当country为cn（中国）时有效 - 访问运营商统计数据时不能填写 - 访问国家统计数据时不能填写 - 访问top_url数据时不能填写

        :param region: The region of this DownloadRegionCarrierExcelRequest.
        :type region: str
        """
        self._region = region

    @property
    def carrier(self):
        r"""Gets the carrier of this DownloadRegionCarrierExcelRequest.

        - 运营商编码 - 访问区域统计数据时不能填写 - 访问国家统计数据时不能填写 - 访问top_url数据时不能填写

        :return: The carrier of this DownloadRegionCarrierExcelRequest.
        :rtype: str
        """
        return self._carrier

    @carrier.setter
    def carrier(self, carrier):
        r"""Sets the carrier of this DownloadRegionCarrierExcelRequest.

        - 运营商编码 - 访问区域统计数据时不能填写 - 访问国家统计数据时不能填写 - 访问top_url数据时不能填写

        :param carrier: The carrier of this DownloadRegionCarrierExcelRequest.
        :type carrier: str
        """
        self._carrier = carrier

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
        if not isinstance(other, DownloadRegionCarrierExcelRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
