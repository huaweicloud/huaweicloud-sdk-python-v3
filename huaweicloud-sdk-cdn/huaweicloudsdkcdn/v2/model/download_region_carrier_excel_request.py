# coding: utf-8

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

        :param start_time: **参数解释：** 查询起始时间戳 **约束限制：** 需与结束时间戳同时指定，左闭右开 **取值范围：** - 若查询5分钟时间粒度（即interval为300）数据，start_time设置为整5分钟时刻点，如：1631240100000(对应2021-09-10 10:15:00) - 若查询1小时时间粒度（即interval为3600）数据，start_time设置为整小时时刻点，如：1631239200000(对应2021-09-10 10:00:00) - 若查询1天时间粒度（即interval为86400）数据，start_time设置为东8区零点时刻点，如：1631203200000(对应2021-09-10 00:00:00) **默认取值：** 不涉及
        :type start_time: int
        :param end_time: **参数解释：** 查询结束时间戳 **约束限制：** 需与起始时间戳同时指定，左闭右开 **取值范围：** - 若查询5分钟时间粒度（即interval为300）数据，end_time设置为整5分钟时刻点，如：1631240100000）对应2021-09-10 10:15:00） - 若查询1小时时间粒度（即interval为3600）数据，end_time设置为整小时时刻点，如：1631239200000（对应2021-09-10 10:00:00） - 若查询1天时间粒度（即interval为86400）数据，end_time设置为东8区零点时刻点，如：1631203200000（对应2021-09-10 00:00:00） **默认取值：** 不涉及
        :type end_time: int
        :param domain_name: **参数解释：** 域名列表 &gt; 如果域名在查询时间段内无数据，结果将不返回该域名的信息  **约束限制：** 仅支持查询已经在CDN创建成功的域名 **取值范围：** - all表示查询名下全部域名 - 多个域名以逗号（半角）分隔，如：www.test1.com,www.test2.com **默认取值：** 不涉及
        :type domain_name: str
        :param interval: **参数解释：** 查询时间粒度 **约束限制：** - 查询跨度不超过1天时，支持5分钟粒度、1小时粒度 - 查询跨度不超过7天时，支持5分钟、1小时粒度、1天粒度 - 查询跨度不超过31天时，支持1小时粒度、1天粒度  **取值范围：** - 300：采样时间间隔为5分钟，单位：秒 - 3600：采样时间间隔为1小时，单位：秒 - 86400：采样时间间隔为1天，单位：秒 **默认取值：** 默认取对应查询时间跨度的最小时间间隔 &gt; 时间跨度小于等于7天，最小时间间隔为300；时间跨度大于7天，最小时间间隔为3600
        :type interval: int
        :param country: **参数解释：** 国家&amp;地区编码 **约束限制：** - 查询运营商统计数据时，不传该参数 - 查询top_url数据时，不传该参数 - 查询区域情况数据时，该参数只能传cn(中国)  **取值范围：** - 多个以英文逗号分隔 - all表示全部，取值见附录 **默认取值：** 不涉及
        :type country: str
        :param excel_language: **参数解释：** 创建表格语言 **约束限制：** 不涉及 **取值范围：** - zh：中文 - en：英文 **默认取值：** zh：中文
        :type excel_language: str
        :param enterprise_project_id: **参数解释：** 企业项目id &gt; 您可以通过调用企业项目管理服务（EPS）的查询企业项目列表接口（ListEnterpriseProject）查询企业项目id  **约束限制：** - 当用户开启企业项目功能时，该参数生效，表示查询资源所属项目 - 当使用子账号调用接口时，该参数必传 **取值范围：** all表示所有项目 **默认取值：** 不涉及
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

        **参数解释：** 查询起始时间戳 **约束限制：** 需与结束时间戳同时指定，左闭右开 **取值范围：** - 若查询5分钟时间粒度（即interval为300）数据，start_time设置为整5分钟时刻点，如：1631240100000(对应2021-09-10 10:15:00) - 若查询1小时时间粒度（即interval为3600）数据，start_time设置为整小时时刻点，如：1631239200000(对应2021-09-10 10:00:00) - 若查询1天时间粒度（即interval为86400）数据，start_time设置为东8区零点时刻点，如：1631203200000(对应2021-09-10 00:00:00) **默认取值：** 不涉及

        :return: The start_time of this DownloadRegionCarrierExcelRequest.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this DownloadRegionCarrierExcelRequest.

        **参数解释：** 查询起始时间戳 **约束限制：** 需与结束时间戳同时指定，左闭右开 **取值范围：** - 若查询5分钟时间粒度（即interval为300）数据，start_time设置为整5分钟时刻点，如：1631240100000(对应2021-09-10 10:15:00) - 若查询1小时时间粒度（即interval为3600）数据，start_time设置为整小时时刻点，如：1631239200000(对应2021-09-10 10:00:00) - 若查询1天时间粒度（即interval为86400）数据，start_time设置为东8区零点时刻点，如：1631203200000(对应2021-09-10 00:00:00) **默认取值：** 不涉及

        :param start_time: The start_time of this DownloadRegionCarrierExcelRequest.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this DownloadRegionCarrierExcelRequest.

        **参数解释：** 查询结束时间戳 **约束限制：** 需与起始时间戳同时指定，左闭右开 **取值范围：** - 若查询5分钟时间粒度（即interval为300）数据，end_time设置为整5分钟时刻点，如：1631240100000）对应2021-09-10 10:15:00） - 若查询1小时时间粒度（即interval为3600）数据，end_time设置为整小时时刻点，如：1631239200000（对应2021-09-10 10:00:00） - 若查询1天时间粒度（即interval为86400）数据，end_time设置为东8区零点时刻点，如：1631203200000（对应2021-09-10 00:00:00） **默认取值：** 不涉及

        :return: The end_time of this DownloadRegionCarrierExcelRequest.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this DownloadRegionCarrierExcelRequest.

        **参数解释：** 查询结束时间戳 **约束限制：** 需与起始时间戳同时指定，左闭右开 **取值范围：** - 若查询5分钟时间粒度（即interval为300）数据，end_time设置为整5分钟时刻点，如：1631240100000）对应2021-09-10 10:15:00） - 若查询1小时时间粒度（即interval为3600）数据，end_time设置为整小时时刻点，如：1631239200000（对应2021-09-10 10:00:00） - 若查询1天时间粒度（即interval为86400）数据，end_time设置为东8区零点时刻点，如：1631203200000（对应2021-09-10 00:00:00） **默认取值：** 不涉及

        :param end_time: The end_time of this DownloadRegionCarrierExcelRequest.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def domain_name(self):
        r"""Gets the domain_name of this DownloadRegionCarrierExcelRequest.

        **参数解释：** 域名列表 > 如果域名在查询时间段内无数据，结果将不返回该域名的信息  **约束限制：** 仅支持查询已经在CDN创建成功的域名 **取值范围：** - all表示查询名下全部域名 - 多个域名以逗号（半角）分隔，如：www.test1.com,www.test2.com **默认取值：** 不涉及

        :return: The domain_name of this DownloadRegionCarrierExcelRequest.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        r"""Sets the domain_name of this DownloadRegionCarrierExcelRequest.

        **参数解释：** 域名列表 > 如果域名在查询时间段内无数据，结果将不返回该域名的信息  **约束限制：** 仅支持查询已经在CDN创建成功的域名 **取值范围：** - all表示查询名下全部域名 - 多个域名以逗号（半角）分隔，如：www.test1.com,www.test2.com **默认取值：** 不涉及

        :param domain_name: The domain_name of this DownloadRegionCarrierExcelRequest.
        :type domain_name: str
        """
        self._domain_name = domain_name

    @property
    def interval(self):
        r"""Gets the interval of this DownloadRegionCarrierExcelRequest.

        **参数解释：** 查询时间粒度 **约束限制：** - 查询跨度不超过1天时，支持5分钟粒度、1小时粒度 - 查询跨度不超过7天时，支持5分钟、1小时粒度、1天粒度 - 查询跨度不超过31天时，支持1小时粒度、1天粒度  **取值范围：** - 300：采样时间间隔为5分钟，单位：秒 - 3600：采样时间间隔为1小时，单位：秒 - 86400：采样时间间隔为1天，单位：秒 **默认取值：** 默认取对应查询时间跨度的最小时间间隔 > 时间跨度小于等于7天，最小时间间隔为300；时间跨度大于7天，最小时间间隔为3600

        :return: The interval of this DownloadRegionCarrierExcelRequest.
        :rtype: int
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        r"""Sets the interval of this DownloadRegionCarrierExcelRequest.

        **参数解释：** 查询时间粒度 **约束限制：** - 查询跨度不超过1天时，支持5分钟粒度、1小时粒度 - 查询跨度不超过7天时，支持5分钟、1小时粒度、1天粒度 - 查询跨度不超过31天时，支持1小时粒度、1天粒度  **取值范围：** - 300：采样时间间隔为5分钟，单位：秒 - 3600：采样时间间隔为1小时，单位：秒 - 86400：采样时间间隔为1天，单位：秒 **默认取值：** 默认取对应查询时间跨度的最小时间间隔 > 时间跨度小于等于7天，最小时间间隔为300；时间跨度大于7天，最小时间间隔为3600

        :param interval: The interval of this DownloadRegionCarrierExcelRequest.
        :type interval: int
        """
        self._interval = interval

    @property
    def country(self):
        r"""Gets the country of this DownloadRegionCarrierExcelRequest.

        **参数解释：** 国家&地区编码 **约束限制：** - 查询运营商统计数据时，不传该参数 - 查询top_url数据时，不传该参数 - 查询区域情况数据时，该参数只能传cn(中国)  **取值范围：** - 多个以英文逗号分隔 - all表示全部，取值见附录 **默认取值：** 不涉及

        :return: The country of this DownloadRegionCarrierExcelRequest.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        r"""Sets the country of this DownloadRegionCarrierExcelRequest.

        **参数解释：** 国家&地区编码 **约束限制：** - 查询运营商统计数据时，不传该参数 - 查询top_url数据时，不传该参数 - 查询区域情况数据时，该参数只能传cn(中国)  **取值范围：** - 多个以英文逗号分隔 - all表示全部，取值见附录 **默认取值：** 不涉及

        :param country: The country of this DownloadRegionCarrierExcelRequest.
        :type country: str
        """
        self._country = country

    @property
    def excel_language(self):
        r"""Gets the excel_language of this DownloadRegionCarrierExcelRequest.

        **参数解释：** 创建表格语言 **约束限制：** 不涉及 **取值范围：** - zh：中文 - en：英文 **默认取值：** zh：中文

        :return: The excel_language of this DownloadRegionCarrierExcelRequest.
        :rtype: str
        """
        return self._excel_language

    @excel_language.setter
    def excel_language(self, excel_language):
        r"""Sets the excel_language of this DownloadRegionCarrierExcelRequest.

        **参数解释：** 创建表格语言 **约束限制：** 不涉及 **取值范围：** - zh：中文 - en：英文 **默认取值：** zh：中文

        :param excel_language: The excel_language of this DownloadRegionCarrierExcelRequest.
        :type excel_language: str
        """
        self._excel_language = excel_language

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this DownloadRegionCarrierExcelRequest.

        **参数解释：** 企业项目id > 您可以通过调用企业项目管理服务（EPS）的查询企业项目列表接口（ListEnterpriseProject）查询企业项目id  **约束限制：** - 当用户开启企业项目功能时，该参数生效，表示查询资源所属项目 - 当使用子账号调用接口时，该参数必传 **取值范围：** all表示所有项目 **默认取值：** 不涉及

        :return: The enterprise_project_id of this DownloadRegionCarrierExcelRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this DownloadRegionCarrierExcelRequest.

        **参数解释：** 企业项目id > 您可以通过调用企业项目管理服务（EPS）的查询企业项目列表接口（ListEnterpriseProject）查询企业项目id  **约束限制：** - 当用户开启企业项目功能时，该参数生效，表示查询资源所属项目 - 当使用子账号调用接口时，该参数必传 **取值范围：** all表示所有项目 **默认取值：** 不涉及

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
        if not isinstance(other, DownloadRegionCarrierExcelRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
