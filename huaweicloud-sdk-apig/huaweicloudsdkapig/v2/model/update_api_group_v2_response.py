# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


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
        'url_domains': 'list[UrlDomainsResp]',
        'call_limits': 'int',
        'update_time': 'datetime',
        'name': 'str',
        'time_unit': 'str',
        'on_sell_status': 'int',
        'remark': 'str',
        'sl_domain': 'str',
        'sl_domains': 'list[str]',
        'id': 'str',
        'time_interval': 'int',
        'register_time': 'datetime',
        'status': 'int',
        'is_default': 'int'
    }

    attribute_map = {
        'url_domains': 'url_domains',
        'call_limits': 'call_limits',
        'update_time': 'update_time',
        'name': 'name',
        'time_unit': 'time_unit',
        'on_sell_status': 'on_sell_status',
        'remark': 'remark',
        'sl_domain': 'sl_domain',
        'sl_domains': 'sl_domains',
        'id': 'id',
        'time_interval': 'time_interval',
        'register_time': 'register_time',
        'status': 'status',
        'is_default': 'is_default'
    }

    def __init__(self, url_domains=None, call_limits=None, update_time=None, name=None, time_unit=None, on_sell_status=None, remark=None, sl_domain=None, sl_domains=None, id=None, time_interval=None, register_time=None, status=None, is_default=None):
        """UpdateApiGroupV2Response - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._url_domains = None
        self._call_limits = None
        self._update_time = None
        self._name = None
        self._time_unit = None
        self._on_sell_status = None
        self._remark = None
        self._sl_domain = None
        self._sl_domains = None
        self._id = None
        self._time_interval = None
        self._register_time = None
        self._status = None
        self._is_default = None
        self.discriminator = None

        if url_domains is not None:
            self.url_domains = url_domains
        if call_limits is not None:
            self.call_limits = call_limits
        if update_time is not None:
            self.update_time = update_time
        if name is not None:
            self.name = name
        if time_unit is not None:
            self.time_unit = time_unit
        if on_sell_status is not None:
            self.on_sell_status = on_sell_status
        if remark is not None:
            self.remark = remark
        if sl_domain is not None:
            self.sl_domain = sl_domain
        if sl_domains is not None:
            self.sl_domains = sl_domains
        if id is not None:
            self.id = id
        if time_interval is not None:
            self.time_interval = time_interval
        if register_time is not None:
            self.register_time = register_time
        if status is not None:
            self.status = status
        if is_default is not None:
            self.is_default = is_default

    @property
    def url_domains(self):
        """Gets the url_domains of this UpdateApiGroupV2Response.

        分组上绑定的独立域名列表

        :return: The url_domains of this UpdateApiGroupV2Response.
        :rtype: list[UrlDomainsResp]
        """
        return self._url_domains

    @url_domains.setter
    def url_domains(self, url_domains):
        """Sets the url_domains of this UpdateApiGroupV2Response.

        分组上绑定的独立域名列表

        :param url_domains: The url_domains of this UpdateApiGroupV2Response.
        :type: list[UrlDomainsResp]
        """
        self._url_domains = url_domains

    @property
    def call_limits(self):
        """Gets the call_limits of this UpdateApiGroupV2Response.

        流控时长内分组下的API的总访问次数限制，默认不限，请根据服务的负载能力自行设置  暂不支持

        :return: The call_limits of this UpdateApiGroupV2Response.
        :rtype: int
        """
        return self._call_limits

    @call_limits.setter
    def call_limits(self, call_limits):
        """Sets the call_limits of this UpdateApiGroupV2Response.

        流控时长内分组下的API的总访问次数限制，默认不限，请根据服务的负载能力自行设置  暂不支持

        :param call_limits: The call_limits of this UpdateApiGroupV2Response.
        :type: int
        """
        self._call_limits = call_limits

    @property
    def update_time(self):
        """Gets the update_time of this UpdateApiGroupV2Response.

        最近修改时间

        :return: The update_time of this UpdateApiGroupV2Response.
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this UpdateApiGroupV2Response.

        最近修改时间

        :param update_time: The update_time of this UpdateApiGroupV2Response.
        :type: datetime
        """
        self._update_time = update_time

    @property
    def name(self):
        """Gets the name of this UpdateApiGroupV2Response.

        API分组名称

        :return: The name of this UpdateApiGroupV2Response.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateApiGroupV2Response.

        API分组名称

        :param name: The name of this UpdateApiGroupV2Response.
        :type: str
        """
        self._name = name

    @property
    def time_unit(self):
        """Gets the time_unit of this UpdateApiGroupV2Response.

        流控的时间单位  暂不支持

        :return: The time_unit of this UpdateApiGroupV2Response.
        :rtype: str
        """
        return self._time_unit

    @time_unit.setter
    def time_unit(self, time_unit):
        """Sets the time_unit of this UpdateApiGroupV2Response.

        流控的时间单位  暂不支持

        :param time_unit: The time_unit of this UpdateApiGroupV2Response.
        :type: str
        """
        self._time_unit = time_unit

    @property
    def on_sell_status(self):
        """Gets the on_sell_status of this UpdateApiGroupV2Response.

        是否已上架云市场： - 1：已上架 - 2：未上架 - 3：审核中

        :return: The on_sell_status of this UpdateApiGroupV2Response.
        :rtype: int
        """
        return self._on_sell_status

    @on_sell_status.setter
    def on_sell_status(self, on_sell_status):
        """Sets the on_sell_status of this UpdateApiGroupV2Response.

        是否已上架云市场： - 1：已上架 - 2：未上架 - 3：审核中

        :param on_sell_status: The on_sell_status of this UpdateApiGroupV2Response.
        :type: int
        """
        self._on_sell_status = on_sell_status

    @property
    def remark(self):
        """Gets the remark of this UpdateApiGroupV2Response.

        描述

        :return: The remark of this UpdateApiGroupV2Response.
        :rtype: str
        """
        return self._remark

    @remark.setter
    def remark(self, remark):
        """Sets the remark of this UpdateApiGroupV2Response.

        描述

        :param remark: The remark of this UpdateApiGroupV2Response.
        :type: str
        """
        self._remark = remark

    @property
    def sl_domain(self):
        """Gets the sl_domain of this UpdateApiGroupV2Response.

        系统默认分配的子域名

        :return: The sl_domain of this UpdateApiGroupV2Response.
        :rtype: str
        """
        return self._sl_domain

    @sl_domain.setter
    def sl_domain(self, sl_domain):
        """Sets the sl_domain of this UpdateApiGroupV2Response.

        系统默认分配的子域名

        :param sl_domain: The sl_domain of this UpdateApiGroupV2Response.
        :type: str
        """
        self._sl_domain = sl_domain

    @property
    def sl_domains(self):
        """Gets the sl_domains of this UpdateApiGroupV2Response.

        系统默认分配的子域名列表

        :return: The sl_domains of this UpdateApiGroupV2Response.
        :rtype: list[str]
        """
        return self._sl_domains

    @sl_domains.setter
    def sl_domains(self, sl_domains):
        """Sets the sl_domains of this UpdateApiGroupV2Response.

        系统默认分配的子域名列表

        :param sl_domains: The sl_domains of this UpdateApiGroupV2Response.
        :type: list[str]
        """
        self._sl_domains = sl_domains

    @property
    def id(self):
        """Gets the id of this UpdateApiGroupV2Response.

        编号

        :return: The id of this UpdateApiGroupV2Response.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UpdateApiGroupV2Response.

        编号

        :param id: The id of this UpdateApiGroupV2Response.
        :type: str
        """
        self._id = id

    @property
    def time_interval(self):
        """Gets the time_interval of this UpdateApiGroupV2Response.

        流控时长  暂不支持

        :return: The time_interval of this UpdateApiGroupV2Response.
        :rtype: int
        """
        return self._time_interval

    @time_interval.setter
    def time_interval(self, time_interval):
        """Sets the time_interval of this UpdateApiGroupV2Response.

        流控时长  暂不支持

        :param time_interval: The time_interval of this UpdateApiGroupV2Response.
        :type: int
        """
        self._time_interval = time_interval

    @property
    def register_time(self):
        """Gets the register_time of this UpdateApiGroupV2Response.

        创建时间

        :return: The register_time of this UpdateApiGroupV2Response.
        :rtype: datetime
        """
        return self._register_time

    @register_time.setter
    def register_time(self, register_time):
        """Sets the register_time of this UpdateApiGroupV2Response.

        创建时间

        :param register_time: The register_time of this UpdateApiGroupV2Response.
        :type: datetime
        """
        self._register_time = register_time

    @property
    def status(self):
        """Gets the status of this UpdateApiGroupV2Response.

        状态

        :return: The status of this UpdateApiGroupV2Response.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this UpdateApiGroupV2Response.

        状态

        :param status: The status of this UpdateApiGroupV2Response.
        :type: int
        """
        self._status = status

    @property
    def is_default(self):
        """Gets the is_default of this UpdateApiGroupV2Response.

        是否为默认分组

        :return: The is_default of this UpdateApiGroupV2Response.
        :rtype: int
        """
        return self._is_default

    @is_default.setter
    def is_default(self, is_default):
        """Sets the is_default of this UpdateApiGroupV2Response.

        是否为默认分组

        :param is_default: The is_default of this UpdateApiGroupV2Response.
        :type: int
        """
        self._is_default = is_default

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UpdateApiGroupV2Response):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
