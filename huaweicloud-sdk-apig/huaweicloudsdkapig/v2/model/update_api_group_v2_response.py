# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateApiGroupV2Response(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'status': 'int',
        'sl_domain': 'str',
        'register_time': 'datetime',
        'update_time': 'datetime',
        'on_sell_status': 'int',
        'url_domains': 'list[UrlDomain]',
        'sl_domain_access_enabled': 'bool',
        'sl_domains': 'list[str]',
        'remark': 'str',
        'call_limits': 'int',
        'time_interval': 'int',
        'time_unit': 'str',
        'is_default': 'int',
        'version': 'str',
        'roma_app_id': 'str',
        'roma_app_name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'status': 'status',
        'sl_domain': 'sl_domain',
        'register_time': 'register_time',
        'update_time': 'update_time',
        'on_sell_status': 'on_sell_status',
        'url_domains': 'url_domains',
        'sl_domain_access_enabled': 'sl_domain_access_enabled',
        'sl_domains': 'sl_domains',
        'remark': 'remark',
        'call_limits': 'call_limits',
        'time_interval': 'time_interval',
        'time_unit': 'time_unit',
        'is_default': 'is_default',
        'version': 'version',
        'roma_app_id': 'roma_app_id',
        'roma_app_name': 'roma_app_name'
    }

    def __init__(self, id=None, name=None, status=None, sl_domain=None, register_time=None, update_time=None, on_sell_status=None, url_domains=None, sl_domain_access_enabled=None, sl_domains=None, remark=None, call_limits=None, time_interval=None, time_unit=None, is_default=None, version=None, roma_app_id=None, roma_app_name=None):
        r"""UpdateApiGroupV2Response

        The model defined in huaweicloud sdk

        :param id: 编号
        :type id: str
        :param name: API分组名称
        :type name: str
        :param status: 状态   - 1： 有效
        :type status: int
        :param sl_domain: 系统默认分配的子域名
        :type sl_domain: str
        :param register_time: 创建时间
        :type register_time: datetime
        :param update_time: 最近修改时间
        :type update_time: datetime
        :param on_sell_status: 是否已上架云商店： - 1：已上架 - 2：未上架 - 3：审核中  [暂不支持](tag:cmcc,ctc,DT,g42,hk_g42,hk_sbc,hk_tm,hws_eu,hws_ocb,OCB,sbc,tm,hws_hk)
        :type on_sell_status: int
        :param url_domains: 分组上绑定的独立域名列表
        :type url_domains: list[:class:`huaweicloudsdkapig.v2.UrlDomain`]
        :param sl_domain_access_enabled: 调试域名是否可以访问，true表示可以访问，false表示禁止访问
        :type sl_domain_access_enabled: bool
        :param sl_domains: 系统默认分配的子域名列表
        :type sl_domains: list[str]
        :param remark: 描述
        :type remark: str
        :param call_limits: 流控时长内分组下的API的总访问次数限制，默认不限，请根据服务的负载能力自行设置  暂不支持
        :type call_limits: int
        :param time_interval: 流控时长  暂不支持
        :type time_interval: int
        :param time_unit: 流控的时间单位  暂不支持
        :type time_unit: str
        :param is_default: 是否为默认分组
        :type is_default: int
        :param version: 分组版本  - V1：全局分组 - V2：应用级分组  暂不支持，默认为V1
        :type version: str
        :param roma_app_id: 分组归属的集成应用编号。  分组版本V2时必填。  暂不支持
        :type roma_app_id: str
        :param roma_app_name: 分组归属的集成应用名称  暂不支持
        :type roma_app_name: str
        """
        
        super(UpdateApiGroupV2Response, self).__init__()

        self._id = None
        self._name = None
        self._status = None
        self._sl_domain = None
        self._register_time = None
        self._update_time = None
        self._on_sell_status = None
        self._url_domains = None
        self._sl_domain_access_enabled = None
        self._sl_domains = None
        self._remark = None
        self._call_limits = None
        self._time_interval = None
        self._time_unit = None
        self._is_default = None
        self._version = None
        self._roma_app_id = None
        self._roma_app_name = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.status = status
        self.sl_domain = sl_domain
        self.register_time = register_time
        self.update_time = update_time
        self.on_sell_status = on_sell_status
        if url_domains is not None:
            self.url_domains = url_domains
        if sl_domain_access_enabled is not None:
            self.sl_domain_access_enabled = sl_domain_access_enabled
        if sl_domains is not None:
            self.sl_domains = sl_domains
        if remark is not None:
            self.remark = remark
        if call_limits is not None:
            self.call_limits = call_limits
        if time_interval is not None:
            self.time_interval = time_interval
        if time_unit is not None:
            self.time_unit = time_unit
        if is_default is not None:
            self.is_default = is_default
        if version is not None:
            self.version = version
        if roma_app_id is not None:
            self.roma_app_id = roma_app_id
        if roma_app_name is not None:
            self.roma_app_name = roma_app_name

    @property
    def id(self):
        r"""Gets the id of this UpdateApiGroupV2Response.

        编号

        :return: The id of this UpdateApiGroupV2Response.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this UpdateApiGroupV2Response.

        编号

        :param id: The id of this UpdateApiGroupV2Response.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this UpdateApiGroupV2Response.

        API分组名称

        :return: The name of this UpdateApiGroupV2Response.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this UpdateApiGroupV2Response.

        API分组名称

        :param name: The name of this UpdateApiGroupV2Response.
        :type name: str
        """
        self._name = name

    @property
    def status(self):
        r"""Gets the status of this UpdateApiGroupV2Response.

        状态   - 1： 有效

        :return: The status of this UpdateApiGroupV2Response.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this UpdateApiGroupV2Response.

        状态   - 1： 有效

        :param status: The status of this UpdateApiGroupV2Response.
        :type status: int
        """
        self._status = status

    @property
    def sl_domain(self):
        r"""Gets the sl_domain of this UpdateApiGroupV2Response.

        系统默认分配的子域名

        :return: The sl_domain of this UpdateApiGroupV2Response.
        :rtype: str
        """
        return self._sl_domain

    @sl_domain.setter
    def sl_domain(self, sl_domain):
        r"""Sets the sl_domain of this UpdateApiGroupV2Response.

        系统默认分配的子域名

        :param sl_domain: The sl_domain of this UpdateApiGroupV2Response.
        :type sl_domain: str
        """
        self._sl_domain = sl_domain

    @property
    def register_time(self):
        r"""Gets the register_time of this UpdateApiGroupV2Response.

        创建时间

        :return: The register_time of this UpdateApiGroupV2Response.
        :rtype: datetime
        """
        return self._register_time

    @register_time.setter
    def register_time(self, register_time):
        r"""Sets the register_time of this UpdateApiGroupV2Response.

        创建时间

        :param register_time: The register_time of this UpdateApiGroupV2Response.
        :type register_time: datetime
        """
        self._register_time = register_time

    @property
    def update_time(self):
        r"""Gets the update_time of this UpdateApiGroupV2Response.

        最近修改时间

        :return: The update_time of this UpdateApiGroupV2Response.
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this UpdateApiGroupV2Response.

        最近修改时间

        :param update_time: The update_time of this UpdateApiGroupV2Response.
        :type update_time: datetime
        """
        self._update_time = update_time

    @property
    def on_sell_status(self):
        r"""Gets the on_sell_status of this UpdateApiGroupV2Response.

        是否已上架云商店： - 1：已上架 - 2：未上架 - 3：审核中  [暂不支持](tag:cmcc,ctc,DT,g42,hk_g42,hk_sbc,hk_tm,hws_eu,hws_ocb,OCB,sbc,tm,hws_hk)

        :return: The on_sell_status of this UpdateApiGroupV2Response.
        :rtype: int
        """
        return self._on_sell_status

    @on_sell_status.setter
    def on_sell_status(self, on_sell_status):
        r"""Sets the on_sell_status of this UpdateApiGroupV2Response.

        是否已上架云商店： - 1：已上架 - 2：未上架 - 3：审核中  [暂不支持](tag:cmcc,ctc,DT,g42,hk_g42,hk_sbc,hk_tm,hws_eu,hws_ocb,OCB,sbc,tm,hws_hk)

        :param on_sell_status: The on_sell_status of this UpdateApiGroupV2Response.
        :type on_sell_status: int
        """
        self._on_sell_status = on_sell_status

    @property
    def url_domains(self):
        r"""Gets the url_domains of this UpdateApiGroupV2Response.

        分组上绑定的独立域名列表

        :return: The url_domains of this UpdateApiGroupV2Response.
        :rtype: list[:class:`huaweicloudsdkapig.v2.UrlDomain`]
        """
        return self._url_domains

    @url_domains.setter
    def url_domains(self, url_domains):
        r"""Sets the url_domains of this UpdateApiGroupV2Response.

        分组上绑定的独立域名列表

        :param url_domains: The url_domains of this UpdateApiGroupV2Response.
        :type url_domains: list[:class:`huaweicloudsdkapig.v2.UrlDomain`]
        """
        self._url_domains = url_domains

    @property
    def sl_domain_access_enabled(self):
        r"""Gets the sl_domain_access_enabled of this UpdateApiGroupV2Response.

        调试域名是否可以访问，true表示可以访问，false表示禁止访问

        :return: The sl_domain_access_enabled of this UpdateApiGroupV2Response.
        :rtype: bool
        """
        return self._sl_domain_access_enabled

    @sl_domain_access_enabled.setter
    def sl_domain_access_enabled(self, sl_domain_access_enabled):
        r"""Sets the sl_domain_access_enabled of this UpdateApiGroupV2Response.

        调试域名是否可以访问，true表示可以访问，false表示禁止访问

        :param sl_domain_access_enabled: The sl_domain_access_enabled of this UpdateApiGroupV2Response.
        :type sl_domain_access_enabled: bool
        """
        self._sl_domain_access_enabled = sl_domain_access_enabled

    @property
    def sl_domains(self):
        r"""Gets the sl_domains of this UpdateApiGroupV2Response.

        系统默认分配的子域名列表

        :return: The sl_domains of this UpdateApiGroupV2Response.
        :rtype: list[str]
        """
        return self._sl_domains

    @sl_domains.setter
    def sl_domains(self, sl_domains):
        r"""Sets the sl_domains of this UpdateApiGroupV2Response.

        系统默认分配的子域名列表

        :param sl_domains: The sl_domains of this UpdateApiGroupV2Response.
        :type sl_domains: list[str]
        """
        self._sl_domains = sl_domains

    @property
    def remark(self):
        r"""Gets the remark of this UpdateApiGroupV2Response.

        描述

        :return: The remark of this UpdateApiGroupV2Response.
        :rtype: str
        """
        return self._remark

    @remark.setter
    def remark(self, remark):
        r"""Sets the remark of this UpdateApiGroupV2Response.

        描述

        :param remark: The remark of this UpdateApiGroupV2Response.
        :type remark: str
        """
        self._remark = remark

    @property
    def call_limits(self):
        r"""Gets the call_limits of this UpdateApiGroupV2Response.

        流控时长内分组下的API的总访问次数限制，默认不限，请根据服务的负载能力自行设置  暂不支持

        :return: The call_limits of this UpdateApiGroupV2Response.
        :rtype: int
        """
        return self._call_limits

    @call_limits.setter
    def call_limits(self, call_limits):
        r"""Sets the call_limits of this UpdateApiGroupV2Response.

        流控时长内分组下的API的总访问次数限制，默认不限，请根据服务的负载能力自行设置  暂不支持

        :param call_limits: The call_limits of this UpdateApiGroupV2Response.
        :type call_limits: int
        """
        self._call_limits = call_limits

    @property
    def time_interval(self):
        r"""Gets the time_interval of this UpdateApiGroupV2Response.

        流控时长  暂不支持

        :return: The time_interval of this UpdateApiGroupV2Response.
        :rtype: int
        """
        return self._time_interval

    @time_interval.setter
    def time_interval(self, time_interval):
        r"""Sets the time_interval of this UpdateApiGroupV2Response.

        流控时长  暂不支持

        :param time_interval: The time_interval of this UpdateApiGroupV2Response.
        :type time_interval: int
        """
        self._time_interval = time_interval

    @property
    def time_unit(self):
        r"""Gets the time_unit of this UpdateApiGroupV2Response.

        流控的时间单位  暂不支持

        :return: The time_unit of this UpdateApiGroupV2Response.
        :rtype: str
        """
        return self._time_unit

    @time_unit.setter
    def time_unit(self, time_unit):
        r"""Sets the time_unit of this UpdateApiGroupV2Response.

        流控的时间单位  暂不支持

        :param time_unit: The time_unit of this UpdateApiGroupV2Response.
        :type time_unit: str
        """
        self._time_unit = time_unit

    @property
    def is_default(self):
        r"""Gets the is_default of this UpdateApiGroupV2Response.

        是否为默认分组

        :return: The is_default of this UpdateApiGroupV2Response.
        :rtype: int
        """
        return self._is_default

    @is_default.setter
    def is_default(self, is_default):
        r"""Sets the is_default of this UpdateApiGroupV2Response.

        是否为默认分组

        :param is_default: The is_default of this UpdateApiGroupV2Response.
        :type is_default: int
        """
        self._is_default = is_default

    @property
    def version(self):
        r"""Gets the version of this UpdateApiGroupV2Response.

        分组版本  - V1：全局分组 - V2：应用级分组  暂不支持，默认为V1

        :return: The version of this UpdateApiGroupV2Response.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this UpdateApiGroupV2Response.

        分组版本  - V1：全局分组 - V2：应用级分组  暂不支持，默认为V1

        :param version: The version of this UpdateApiGroupV2Response.
        :type version: str
        """
        self._version = version

    @property
    def roma_app_id(self):
        r"""Gets the roma_app_id of this UpdateApiGroupV2Response.

        分组归属的集成应用编号。  分组版本V2时必填。  暂不支持

        :return: The roma_app_id of this UpdateApiGroupV2Response.
        :rtype: str
        """
        return self._roma_app_id

    @roma_app_id.setter
    def roma_app_id(self, roma_app_id):
        r"""Sets the roma_app_id of this UpdateApiGroupV2Response.

        分组归属的集成应用编号。  分组版本V2时必填。  暂不支持

        :param roma_app_id: The roma_app_id of this UpdateApiGroupV2Response.
        :type roma_app_id: str
        """
        self._roma_app_id = roma_app_id

    @property
    def roma_app_name(self):
        r"""Gets the roma_app_name of this UpdateApiGroupV2Response.

        分组归属的集成应用名称  暂不支持

        :return: The roma_app_name of this UpdateApiGroupV2Response.
        :rtype: str
        """
        return self._roma_app_name

    @roma_app_name.setter
    def roma_app_name(self, roma_app_name):
        r"""Sets the roma_app_name of this UpdateApiGroupV2Response.

        分组归属的集成应用名称  暂不支持

        :param roma_app_name: The roma_app_name of this UpdateApiGroupV2Response.
        :type roma_app_name: str
        """
        self._roma_app_name = roma_app_name

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
        if not isinstance(other, UpdateApiGroupV2Response):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
