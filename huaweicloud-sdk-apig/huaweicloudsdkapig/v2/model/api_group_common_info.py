# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ApiGroupCommonInfo:

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
        'sl_domain_access_enabled': 'bool'
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
        'sl_domain_access_enabled': 'sl_domain_access_enabled'
    }

    def __init__(self, id=None, name=None, status=None, sl_domain=None, register_time=None, update_time=None, on_sell_status=None, url_domains=None, sl_domain_access_enabled=None):
        r"""ApiGroupCommonInfo

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
        """
        
        

        self._id = None
        self._name = None
        self._status = None
        self._sl_domain = None
        self._register_time = None
        self._update_time = None
        self._on_sell_status = None
        self._url_domains = None
        self._sl_domain_access_enabled = None
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

    @property
    def id(self):
        r"""Gets the id of this ApiGroupCommonInfo.

        编号

        :return: The id of this ApiGroupCommonInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ApiGroupCommonInfo.

        编号

        :param id: The id of this ApiGroupCommonInfo.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ApiGroupCommonInfo.

        API分组名称

        :return: The name of this ApiGroupCommonInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ApiGroupCommonInfo.

        API分组名称

        :param name: The name of this ApiGroupCommonInfo.
        :type name: str
        """
        self._name = name

    @property
    def status(self):
        r"""Gets the status of this ApiGroupCommonInfo.

        状态   - 1： 有效

        :return: The status of this ApiGroupCommonInfo.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ApiGroupCommonInfo.

        状态   - 1： 有效

        :param status: The status of this ApiGroupCommonInfo.
        :type status: int
        """
        self._status = status

    @property
    def sl_domain(self):
        r"""Gets the sl_domain of this ApiGroupCommonInfo.

        系统默认分配的子域名

        :return: The sl_domain of this ApiGroupCommonInfo.
        :rtype: str
        """
        return self._sl_domain

    @sl_domain.setter
    def sl_domain(self, sl_domain):
        r"""Sets the sl_domain of this ApiGroupCommonInfo.

        系统默认分配的子域名

        :param sl_domain: The sl_domain of this ApiGroupCommonInfo.
        :type sl_domain: str
        """
        self._sl_domain = sl_domain

    @property
    def register_time(self):
        r"""Gets the register_time of this ApiGroupCommonInfo.

        创建时间

        :return: The register_time of this ApiGroupCommonInfo.
        :rtype: datetime
        """
        return self._register_time

    @register_time.setter
    def register_time(self, register_time):
        r"""Sets the register_time of this ApiGroupCommonInfo.

        创建时间

        :param register_time: The register_time of this ApiGroupCommonInfo.
        :type register_time: datetime
        """
        self._register_time = register_time

    @property
    def update_time(self):
        r"""Gets the update_time of this ApiGroupCommonInfo.

        最近修改时间

        :return: The update_time of this ApiGroupCommonInfo.
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this ApiGroupCommonInfo.

        最近修改时间

        :param update_time: The update_time of this ApiGroupCommonInfo.
        :type update_time: datetime
        """
        self._update_time = update_time

    @property
    def on_sell_status(self):
        r"""Gets the on_sell_status of this ApiGroupCommonInfo.

        是否已上架云商店： - 1：已上架 - 2：未上架 - 3：审核中  [暂不支持](tag:cmcc,ctc,DT,g42,hk_g42,hk_sbc,hk_tm,hws_eu,hws_ocb,OCB,sbc,tm,hws_hk)

        :return: The on_sell_status of this ApiGroupCommonInfo.
        :rtype: int
        """
        return self._on_sell_status

    @on_sell_status.setter
    def on_sell_status(self, on_sell_status):
        r"""Sets the on_sell_status of this ApiGroupCommonInfo.

        是否已上架云商店： - 1：已上架 - 2：未上架 - 3：审核中  [暂不支持](tag:cmcc,ctc,DT,g42,hk_g42,hk_sbc,hk_tm,hws_eu,hws_ocb,OCB,sbc,tm,hws_hk)

        :param on_sell_status: The on_sell_status of this ApiGroupCommonInfo.
        :type on_sell_status: int
        """
        self._on_sell_status = on_sell_status

    @property
    def url_domains(self):
        r"""Gets the url_domains of this ApiGroupCommonInfo.

        分组上绑定的独立域名列表

        :return: The url_domains of this ApiGroupCommonInfo.
        :rtype: list[:class:`huaweicloudsdkapig.v2.UrlDomain`]
        """
        return self._url_domains

    @url_domains.setter
    def url_domains(self, url_domains):
        r"""Sets the url_domains of this ApiGroupCommonInfo.

        分组上绑定的独立域名列表

        :param url_domains: The url_domains of this ApiGroupCommonInfo.
        :type url_domains: list[:class:`huaweicloudsdkapig.v2.UrlDomain`]
        """
        self._url_domains = url_domains

    @property
    def sl_domain_access_enabled(self):
        r"""Gets the sl_domain_access_enabled of this ApiGroupCommonInfo.

        调试域名是否可以访问，true表示可以访问，false表示禁止访问

        :return: The sl_domain_access_enabled of this ApiGroupCommonInfo.
        :rtype: bool
        """
        return self._sl_domain_access_enabled

    @sl_domain_access_enabled.setter
    def sl_domain_access_enabled(self, sl_domain_access_enabled):
        r"""Sets the sl_domain_access_enabled of this ApiGroupCommonInfo.

        调试域名是否可以访问，true表示可以访问，false表示禁止访问

        :param sl_domain_access_enabled: The sl_domain_access_enabled of this ApiGroupCommonInfo.
        :type sl_domain_access_enabled: bool
        """
        self._sl_domain_access_enabled = sl_domain_access_enabled

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
        if not isinstance(other, ApiGroupCommonInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
