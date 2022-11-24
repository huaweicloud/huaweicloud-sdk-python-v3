# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DomainsWithPort:

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
        'domain_name': 'str',
        'business_type': 'str',
        'user_domain_id': 'str',
        'domain_status': 'str',
        'cname': 'str',
        'sources': 'list[SourceWithPort]',
        'domain_origin_host': 'DomainOriginHost',
        'https_status': 'int',
        'create_time': 'int',
        'modify_time': 'int',
        'disabled': 'int',
        'locked': 'int',
        'auto_refresh_preheat': 'int',
        'service_area': 'str',
        'range_status': 'str',
        'follow_status': 'str',
        'origin_status': 'str',
        'banned_reason': 'str',
        'locked_reason': 'str',
        'enterprise_project_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'domain_name': 'domain_name',
        'business_type': 'business_type',
        'user_domain_id': 'user_domain_id',
        'domain_status': 'domain_status',
        'cname': 'cname',
        'sources': 'sources',
        'domain_origin_host': 'domain_origin_host',
        'https_status': 'https_status',
        'create_time': 'create_time',
        'modify_time': 'modify_time',
        'disabled': 'disabled',
        'locked': 'locked',
        'auto_refresh_preheat': 'auto_refresh_preheat',
        'service_area': 'service_area',
        'range_status': 'range_status',
        'follow_status': 'follow_status',
        'origin_status': 'origin_status',
        'banned_reason': 'banned_reason',
        'locked_reason': 'locked_reason',
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, id=None, domain_name=None, business_type=None, user_domain_id=None, domain_status=None, cname=None, sources=None, domain_origin_host=None, https_status=None, create_time=None, modify_time=None, disabled=None, locked=None, auto_refresh_preheat=None, service_area=None, range_status=None, follow_status=None, origin_status=None, banned_reason=None, locked_reason=None, enterprise_project_id=None):
        """DomainsWithPort

        The model defined in huaweicloud sdk

        :param id: 加速域名ID。
        :type id: str
        :param domain_name: 加速域名。
        :type domain_name: str
        :param business_type: 域名业务类型，若为web，则表示类型为网站加速；若为download，则表示业务类型为文件下载加速；若为video，则表示业务类型为点播加速；若为wholeSite，则表示类型为全站加速。
        :type business_type: str
        :param user_domain_id: 域名所属用户的domain_id。
        :type user_domain_id: str
        :param domain_status: 加速域名状态。取值意义： - online表示“已开启” - offline表示“已停用” - configuring表示“配置中” - configure_failed表示“配置失败” - checking表示“审核中” - check_failed表示“审核未通过” - deleting表示“删除中”。
        :type domain_status: str
        :param cname: 加速域名对应的CNAME。
        :type cname: str
        :param sources: 源站域名或源站IP，源站为IP类型时，仅支持IPv4，如需传入多个源站IP，以多个源站对象传入，除IP其他参数请保持一致，主源站最多支持15个源站IP对象，备源站最多支持15个源站IP对象；源站为域名类型时仅支持1个源站对象。不支持IP源站和域名源站混用。
        :type sources: list[:class:`huaweicloudsdkcdn.v1.SourceWithPort`]
        :param domain_origin_host: 
        :type domain_origin_host: :class:`huaweicloudsdkcdn.v1.DomainOriginHost`
        :param https_status: 是否开启HTTPS加速。 0：代表未开启HTTPS加速； 1：代表开启HTTPS加速，且回源方式为协议跟随； 2：代表开启HTTPS加速，且回源方式为HTTP； 3：代表开启HTTPS加速，且回源方式为HTTPS。
        :type https_status: int
        :param create_time: 域名创建时间，相对于UTC 1970-01-01到当前时间相隔的毫秒数。
        :type create_time: int
        :param modify_time: 域名修改时间，相对于UTC 1970-01-01到当前时间相隔的毫秒数。
        :type modify_time: int
        :param disabled: 封禁状态（0代表未禁用；1代表禁用）。
        :type disabled: int
        :param locked: 锁定状态（0代表未锁定；1代表锁定）。
        :type locked: int
        :param auto_refresh_preheat: 自动刷新预热（0代表关闭；1代表打开）
        :type auto_refresh_preheat: int
        :param service_area: 华为云CDN提供的加速服务范围，包含：mainland_china中国大陆、outside_mainland_china中国大陆境外、global全球。
        :type service_area: str
        :param range_status: Range回源状态（off代表关闭 on代表开启）。
        :type range_status: str
        :param follow_status: 回源跟随状态（off代表关闭 on代表开启）。
        :type follow_status: str
        :param origin_status: 是否暂停源站回源（off代表关闭 on代表开启）。
        :type origin_status: str
        :param banned_reason: 域名禁用原因。 1：该域名涉嫌违规内容（涉黄/涉赌/涉毒/涉政）已被禁用； 2：该域名因备案失效已被禁用； 3：该域名遭受攻击，已被禁用； 150：该域名涉嫌违规内容涉黄已被禁用； 151：该域名涉嫌违规内容涉政已被禁用； 152：该域名涉嫌违规内容涉暴已被禁用； 153：该域名涉嫌违规内容涉赌已被禁用。
        :type banned_reason: str
        :param locked_reason: 域名锁定原因（Changing the config, please wait）。
        :type locked_reason: str
        :param enterprise_project_id: 当用户开启企业项目功能时，该参数生效，表示查询资源所属项目，不传表示查询默认项目。注意：当使用子帐号调用接口时，该参数必传。  您可以通过调用企业项目管理服务（EPS）的查询企业项目列表接口（ListEnterpriseProject）查询企业项目id。
        :type enterprise_project_id: str
        """
        
        

        self._id = None
        self._domain_name = None
        self._business_type = None
        self._user_domain_id = None
        self._domain_status = None
        self._cname = None
        self._sources = None
        self._domain_origin_host = None
        self._https_status = None
        self._create_time = None
        self._modify_time = None
        self._disabled = None
        self._locked = None
        self._auto_refresh_preheat = None
        self._service_area = None
        self._range_status = None
        self._follow_status = None
        self._origin_status = None
        self._banned_reason = None
        self._locked_reason = None
        self._enterprise_project_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if domain_name is not None:
            self.domain_name = domain_name
        if business_type is not None:
            self.business_type = business_type
        if user_domain_id is not None:
            self.user_domain_id = user_domain_id
        if domain_status is not None:
            self.domain_status = domain_status
        if cname is not None:
            self.cname = cname
        if sources is not None:
            self.sources = sources
        if domain_origin_host is not None:
            self.domain_origin_host = domain_origin_host
        if https_status is not None:
            self.https_status = https_status
        if create_time is not None:
            self.create_time = create_time
        if modify_time is not None:
            self.modify_time = modify_time
        if disabled is not None:
            self.disabled = disabled
        if locked is not None:
            self.locked = locked
        if auto_refresh_preheat is not None:
            self.auto_refresh_preheat = auto_refresh_preheat
        if service_area is not None:
            self.service_area = service_area
        if range_status is not None:
            self.range_status = range_status
        if follow_status is not None:
            self.follow_status = follow_status
        if origin_status is not None:
            self.origin_status = origin_status
        if banned_reason is not None:
            self.banned_reason = banned_reason
        if locked_reason is not None:
            self.locked_reason = locked_reason
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id

    @property
    def id(self):
        """Gets the id of this DomainsWithPort.

        加速域名ID。

        :return: The id of this DomainsWithPort.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DomainsWithPort.

        加速域名ID。

        :param id: The id of this DomainsWithPort.
        :type id: str
        """
        self._id = id

    @property
    def domain_name(self):
        """Gets the domain_name of this DomainsWithPort.

        加速域名。

        :return: The domain_name of this DomainsWithPort.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        """Sets the domain_name of this DomainsWithPort.

        加速域名。

        :param domain_name: The domain_name of this DomainsWithPort.
        :type domain_name: str
        """
        self._domain_name = domain_name

    @property
    def business_type(self):
        """Gets the business_type of this DomainsWithPort.

        域名业务类型，若为web，则表示类型为网站加速；若为download，则表示业务类型为文件下载加速；若为video，则表示业务类型为点播加速；若为wholeSite，则表示类型为全站加速。

        :return: The business_type of this DomainsWithPort.
        :rtype: str
        """
        return self._business_type

    @business_type.setter
    def business_type(self, business_type):
        """Sets the business_type of this DomainsWithPort.

        域名业务类型，若为web，则表示类型为网站加速；若为download，则表示业务类型为文件下载加速；若为video，则表示业务类型为点播加速；若为wholeSite，则表示类型为全站加速。

        :param business_type: The business_type of this DomainsWithPort.
        :type business_type: str
        """
        self._business_type = business_type

    @property
    def user_domain_id(self):
        """Gets the user_domain_id of this DomainsWithPort.

        域名所属用户的domain_id。

        :return: The user_domain_id of this DomainsWithPort.
        :rtype: str
        """
        return self._user_domain_id

    @user_domain_id.setter
    def user_domain_id(self, user_domain_id):
        """Sets the user_domain_id of this DomainsWithPort.

        域名所属用户的domain_id。

        :param user_domain_id: The user_domain_id of this DomainsWithPort.
        :type user_domain_id: str
        """
        self._user_domain_id = user_domain_id

    @property
    def domain_status(self):
        """Gets the domain_status of this DomainsWithPort.

        加速域名状态。取值意义： - online表示“已开启” - offline表示“已停用” - configuring表示“配置中” - configure_failed表示“配置失败” - checking表示“审核中” - check_failed表示“审核未通过” - deleting表示“删除中”。

        :return: The domain_status of this DomainsWithPort.
        :rtype: str
        """
        return self._domain_status

    @domain_status.setter
    def domain_status(self, domain_status):
        """Sets the domain_status of this DomainsWithPort.

        加速域名状态。取值意义： - online表示“已开启” - offline表示“已停用” - configuring表示“配置中” - configure_failed表示“配置失败” - checking表示“审核中” - check_failed表示“审核未通过” - deleting表示“删除中”。

        :param domain_status: The domain_status of this DomainsWithPort.
        :type domain_status: str
        """
        self._domain_status = domain_status

    @property
    def cname(self):
        """Gets the cname of this DomainsWithPort.

        加速域名对应的CNAME。

        :return: The cname of this DomainsWithPort.
        :rtype: str
        """
        return self._cname

    @cname.setter
    def cname(self, cname):
        """Sets the cname of this DomainsWithPort.

        加速域名对应的CNAME。

        :param cname: The cname of this DomainsWithPort.
        :type cname: str
        """
        self._cname = cname

    @property
    def sources(self):
        """Gets the sources of this DomainsWithPort.

        源站域名或源站IP，源站为IP类型时，仅支持IPv4，如需传入多个源站IP，以多个源站对象传入，除IP其他参数请保持一致，主源站最多支持15个源站IP对象，备源站最多支持15个源站IP对象；源站为域名类型时仅支持1个源站对象。不支持IP源站和域名源站混用。

        :return: The sources of this DomainsWithPort.
        :rtype: list[:class:`huaweicloudsdkcdn.v1.SourceWithPort`]
        """
        return self._sources

    @sources.setter
    def sources(self, sources):
        """Sets the sources of this DomainsWithPort.

        源站域名或源站IP，源站为IP类型时，仅支持IPv4，如需传入多个源站IP，以多个源站对象传入，除IP其他参数请保持一致，主源站最多支持15个源站IP对象，备源站最多支持15个源站IP对象；源站为域名类型时仅支持1个源站对象。不支持IP源站和域名源站混用。

        :param sources: The sources of this DomainsWithPort.
        :type sources: list[:class:`huaweicloudsdkcdn.v1.SourceWithPort`]
        """
        self._sources = sources

    @property
    def domain_origin_host(self):
        """Gets the domain_origin_host of this DomainsWithPort.

        :return: The domain_origin_host of this DomainsWithPort.
        :rtype: :class:`huaweicloudsdkcdn.v1.DomainOriginHost`
        """
        return self._domain_origin_host

    @domain_origin_host.setter
    def domain_origin_host(self, domain_origin_host):
        """Sets the domain_origin_host of this DomainsWithPort.

        :param domain_origin_host: The domain_origin_host of this DomainsWithPort.
        :type domain_origin_host: :class:`huaweicloudsdkcdn.v1.DomainOriginHost`
        """
        self._domain_origin_host = domain_origin_host

    @property
    def https_status(self):
        """Gets the https_status of this DomainsWithPort.

        是否开启HTTPS加速。 0：代表未开启HTTPS加速； 1：代表开启HTTPS加速，且回源方式为协议跟随； 2：代表开启HTTPS加速，且回源方式为HTTP； 3：代表开启HTTPS加速，且回源方式为HTTPS。

        :return: The https_status of this DomainsWithPort.
        :rtype: int
        """
        return self._https_status

    @https_status.setter
    def https_status(self, https_status):
        """Sets the https_status of this DomainsWithPort.

        是否开启HTTPS加速。 0：代表未开启HTTPS加速； 1：代表开启HTTPS加速，且回源方式为协议跟随； 2：代表开启HTTPS加速，且回源方式为HTTP； 3：代表开启HTTPS加速，且回源方式为HTTPS。

        :param https_status: The https_status of this DomainsWithPort.
        :type https_status: int
        """
        self._https_status = https_status

    @property
    def create_time(self):
        """Gets the create_time of this DomainsWithPort.

        域名创建时间，相对于UTC 1970-01-01到当前时间相隔的毫秒数。

        :return: The create_time of this DomainsWithPort.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this DomainsWithPort.

        域名创建时间，相对于UTC 1970-01-01到当前时间相隔的毫秒数。

        :param create_time: The create_time of this DomainsWithPort.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def modify_time(self):
        """Gets the modify_time of this DomainsWithPort.

        域名修改时间，相对于UTC 1970-01-01到当前时间相隔的毫秒数。

        :return: The modify_time of this DomainsWithPort.
        :rtype: int
        """
        return self._modify_time

    @modify_time.setter
    def modify_time(self, modify_time):
        """Sets the modify_time of this DomainsWithPort.

        域名修改时间，相对于UTC 1970-01-01到当前时间相隔的毫秒数。

        :param modify_time: The modify_time of this DomainsWithPort.
        :type modify_time: int
        """
        self._modify_time = modify_time

    @property
    def disabled(self):
        """Gets the disabled of this DomainsWithPort.

        封禁状态（0代表未禁用；1代表禁用）。

        :return: The disabled of this DomainsWithPort.
        :rtype: int
        """
        return self._disabled

    @disabled.setter
    def disabled(self, disabled):
        """Sets the disabled of this DomainsWithPort.

        封禁状态（0代表未禁用；1代表禁用）。

        :param disabled: The disabled of this DomainsWithPort.
        :type disabled: int
        """
        self._disabled = disabled

    @property
    def locked(self):
        """Gets the locked of this DomainsWithPort.

        锁定状态（0代表未锁定；1代表锁定）。

        :return: The locked of this DomainsWithPort.
        :rtype: int
        """
        return self._locked

    @locked.setter
    def locked(self, locked):
        """Sets the locked of this DomainsWithPort.

        锁定状态（0代表未锁定；1代表锁定）。

        :param locked: The locked of this DomainsWithPort.
        :type locked: int
        """
        self._locked = locked

    @property
    def auto_refresh_preheat(self):
        """Gets the auto_refresh_preheat of this DomainsWithPort.

        自动刷新预热（0代表关闭；1代表打开）

        :return: The auto_refresh_preheat of this DomainsWithPort.
        :rtype: int
        """
        return self._auto_refresh_preheat

    @auto_refresh_preheat.setter
    def auto_refresh_preheat(self, auto_refresh_preheat):
        """Sets the auto_refresh_preheat of this DomainsWithPort.

        自动刷新预热（0代表关闭；1代表打开）

        :param auto_refresh_preheat: The auto_refresh_preheat of this DomainsWithPort.
        :type auto_refresh_preheat: int
        """
        self._auto_refresh_preheat = auto_refresh_preheat

    @property
    def service_area(self):
        """Gets the service_area of this DomainsWithPort.

        华为云CDN提供的加速服务范围，包含：mainland_china中国大陆、outside_mainland_china中国大陆境外、global全球。

        :return: The service_area of this DomainsWithPort.
        :rtype: str
        """
        return self._service_area

    @service_area.setter
    def service_area(self, service_area):
        """Sets the service_area of this DomainsWithPort.

        华为云CDN提供的加速服务范围，包含：mainland_china中国大陆、outside_mainland_china中国大陆境外、global全球。

        :param service_area: The service_area of this DomainsWithPort.
        :type service_area: str
        """
        self._service_area = service_area

    @property
    def range_status(self):
        """Gets the range_status of this DomainsWithPort.

        Range回源状态（off代表关闭 on代表开启）。

        :return: The range_status of this DomainsWithPort.
        :rtype: str
        """
        return self._range_status

    @range_status.setter
    def range_status(self, range_status):
        """Sets the range_status of this DomainsWithPort.

        Range回源状态（off代表关闭 on代表开启）。

        :param range_status: The range_status of this DomainsWithPort.
        :type range_status: str
        """
        self._range_status = range_status

    @property
    def follow_status(self):
        """Gets the follow_status of this DomainsWithPort.

        回源跟随状态（off代表关闭 on代表开启）。

        :return: The follow_status of this DomainsWithPort.
        :rtype: str
        """
        return self._follow_status

    @follow_status.setter
    def follow_status(self, follow_status):
        """Sets the follow_status of this DomainsWithPort.

        回源跟随状态（off代表关闭 on代表开启）。

        :param follow_status: The follow_status of this DomainsWithPort.
        :type follow_status: str
        """
        self._follow_status = follow_status

    @property
    def origin_status(self):
        """Gets the origin_status of this DomainsWithPort.

        是否暂停源站回源（off代表关闭 on代表开启）。

        :return: The origin_status of this DomainsWithPort.
        :rtype: str
        """
        return self._origin_status

    @origin_status.setter
    def origin_status(self, origin_status):
        """Sets the origin_status of this DomainsWithPort.

        是否暂停源站回源（off代表关闭 on代表开启）。

        :param origin_status: The origin_status of this DomainsWithPort.
        :type origin_status: str
        """
        self._origin_status = origin_status

    @property
    def banned_reason(self):
        """Gets the banned_reason of this DomainsWithPort.

        域名禁用原因。 1：该域名涉嫌违规内容（涉黄/涉赌/涉毒/涉政）已被禁用； 2：该域名因备案失效已被禁用； 3：该域名遭受攻击，已被禁用； 150：该域名涉嫌违规内容涉黄已被禁用； 151：该域名涉嫌违规内容涉政已被禁用； 152：该域名涉嫌违规内容涉暴已被禁用； 153：该域名涉嫌违规内容涉赌已被禁用。

        :return: The banned_reason of this DomainsWithPort.
        :rtype: str
        """
        return self._banned_reason

    @banned_reason.setter
    def banned_reason(self, banned_reason):
        """Sets the banned_reason of this DomainsWithPort.

        域名禁用原因。 1：该域名涉嫌违规内容（涉黄/涉赌/涉毒/涉政）已被禁用； 2：该域名因备案失效已被禁用； 3：该域名遭受攻击，已被禁用； 150：该域名涉嫌违规内容涉黄已被禁用； 151：该域名涉嫌违规内容涉政已被禁用； 152：该域名涉嫌违规内容涉暴已被禁用； 153：该域名涉嫌违规内容涉赌已被禁用。

        :param banned_reason: The banned_reason of this DomainsWithPort.
        :type banned_reason: str
        """
        self._banned_reason = banned_reason

    @property
    def locked_reason(self):
        """Gets the locked_reason of this DomainsWithPort.

        域名锁定原因（Changing the config, please wait）。

        :return: The locked_reason of this DomainsWithPort.
        :rtype: str
        """
        return self._locked_reason

    @locked_reason.setter
    def locked_reason(self, locked_reason):
        """Sets the locked_reason of this DomainsWithPort.

        域名锁定原因（Changing the config, please wait）。

        :param locked_reason: The locked_reason of this DomainsWithPort.
        :type locked_reason: str
        """
        self._locked_reason = locked_reason

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this DomainsWithPort.

        当用户开启企业项目功能时，该参数生效，表示查询资源所属项目，不传表示查询默认项目。注意：当使用子帐号调用接口时，该参数必传。  您可以通过调用企业项目管理服务（EPS）的查询企业项目列表接口（ListEnterpriseProject）查询企业项目id。

        :return: The enterprise_project_id of this DomainsWithPort.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this DomainsWithPort.

        当用户开启企业项目功能时，该参数生效，表示查询资源所属项目，不传表示查询默认项目。注意：当使用子帐号调用接口时，该参数必传。  您可以通过调用企业项目管理服务（EPS）的查询企业项目列表接口（ListEnterpriseProject）查询企业项目id。

        :param enterprise_project_id: The enterprise_project_id of this DomainsWithPort.
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
        if not isinstance(other, DomainsWithPort):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
