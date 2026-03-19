# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListEventRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'x_language': 'str',
        'enterprise_project_id': 'str',
        'recent': 'str',
        '_from': 'int',
        'to': 'int',
        'ids': 'list[str]',
        'nids': 'list[str]',
        'attacks': 'list[str]',
        'nattacks': 'list[str]',
        'rules': 'list[str]',
        'nrules': 'list[str]',
        'sips': 'list[str]',
        'nsips': 'list[str]',
        'sip': 'str',
        'urls': 'list[str]',
        'nurls': 'list[str]',
        'url': 'str',
        'actions': 'list[str]',
        'nactions': 'list[str]',
        'domain': 'str',
        'ndomain': 'str',
        'domains': 'list[str]',
        'ip_countries': 'list[str]',
        'nip_countries': 'list[str]',
        'ip_regions': 'list[str]',
        'nip_regions': 'list[str]',
        'response_codes': 'list[str]',
        'payload': 'str',
        'hosts': 'list[str]',
        'instances': 'list[str]',
        'page': 'int',
        'pagesize': 'int',
        'sort_key': 'str',
        'sort_direction': 'str',
        'query_mode': 'str'
    }

    attribute_map = {
        'x_language': 'X-Language',
        'enterprise_project_id': 'enterprise_project_id',
        'recent': 'recent',
        '_from': 'from',
        'to': 'to',
        'ids': 'ids',
        'nids': 'nids',
        'attacks': 'attacks',
        'nattacks': 'nattacks',
        'rules': 'rules',
        'nrules': 'nrules',
        'sips': 'sips',
        'nsips': 'nsips',
        'sip': 'sip',
        'urls': 'urls',
        'nurls': 'nurls',
        'url': 'url',
        'actions': 'actions',
        'nactions': 'nactions',
        'domain': 'domain',
        'ndomain': 'ndomain',
        'domains': 'domains',
        'ip_countries': 'ip_countries',
        'nip_countries': 'nip_countries',
        'ip_regions': 'ip_regions',
        'nip_regions': 'nip_regions',
        'response_codes': 'response_codes',
        'payload': 'payload',
        'hosts': 'hosts',
        'instances': 'instances',
        'page': 'page',
        'pagesize': 'pagesize',
        'sort_key': 'sort_key',
        'sort_direction': 'sort_direction',
        'query_mode': 'query_mode'
    }

    def __init__(self, x_language=None, enterprise_project_id=None, recent=None, _from=None, to=None, ids=None, nids=None, attacks=None, nattacks=None, rules=None, nrules=None, sips=None, nsips=None, sip=None, urls=None, nurls=None, url=None, actions=None, nactions=None, domain=None, ndomain=None, domains=None, ip_countries=None, nip_countries=None, ip_regions=None, nip_regions=None, response_codes=None, payload=None, hosts=None, instances=None, page=None, pagesize=None, sort_key=None, sort_direction=None, query_mode=None):
        r"""ListEventRequest

        The model defined in huaweicloud sdk

        :param x_language: **参数解释：** 客户端IP所属地理位置展示语言，默认值为en-us **约束限制：** 不涉及 **取值范围：** - zh-cn 中文 - en-us 英文 **默认取值：** en-us
        :type x_language: str
        :param enterprise_project_id: 您可以通过调用企业项目管理服务（EPS）的查询企业项目列表接口（ListEnterpriseProject）查询企业项目id。若需要查询当前用户所有企业项目绑定的资源信息，请传参all_granted_eps。
        :type enterprise_project_id: str
        :param recent: **参数解释：** 查询日志的时间范围，recent参数与from、to必须使用其中一个。当同时使用recent参数与from、to时，以recent参数为准 **约束限制：** 不涉及 **取值范围：**  - yesterday：昨天  - today：今天  - 3days：近3天   - 1week：近7天   - 1month：近30天  **默认取值：** 不涉及
        :type recent: str
        :param _from: **参数解释：** 起始时间(毫秒时间戳)，需要和to同时使用 **约束限制：** from &lt;&#x3D; to **取值范围：** from ~ to 最大范围30天 **默认取值：** 不涉及
        :type _from: int
        :param to: **参数解释：** 结束时间(毫秒时间戳)，需要和from同时使用 **约束限制：** from ~ to 最大范围30天 **取值范围：** 不能超过当天的结束时间 **默认取值：** 不涉及
        :type to: int
        :param ids: **参数解释：** 防护事件id列表，支持模糊查询 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type ids: list[str]
        :param nids: **参数解释：** 防护事件id列表（排除搜索），支持模糊查询 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type nids: list[str]
        :param attacks: **参数解释：** 攻击类型 **约束限制：** 不涉及 **取值范围：** - xss：XSS攻击  - botm：BOT攻击 - webshell：网站木马  - vuln：其他漏洞攻击 - sqli：sql注入攻击  - robot：恶意爬虫  - rfi：远程文件包含  - rce：远程代码执行 - ptr：目录遍历 - lfi：本地文件包含 - antileakage：网站信息泄漏  - iprank：IP信誉库 - custom_whiteblackip：IP黑白名单 - custom_whiteip：白名单 - custom_blackip：黑名单 - custom_robot：扫描器爬虫 - custom_geoip：地理访问控制 - custom_idc_ip：IDC情报 - custom_custom：精准防护  - cmdi：命令注入攻击  - cc：cc攻击  - antitamper：网页防篡改  - anticrawler：网站反爬虫   - third_bot_river：第三方反爬虫 - antiscan_high_freq_scan：高频扫描封禁 - antiscan_dir_traversal：目录遍历防护 - illegal：非法请求 - followed_action：攻击惩罚 - advanced_bot：BOT管理 - llm_prompt_injection：提示词注入攻击 - llm_prompt_sensitive：提示词违规 - llm_response_sensitive：响应违规 **默认取值：** 不涉及
        :type attacks: list[str]
        :param nattacks: **参数解释：** 攻击类型（排除搜索） **约束限制：** 不涉及 **取值范围：** - xss：XSS攻击  - botm：BOT攻击 - webshell：网站木马  - vuln：其他漏洞攻击 - sqli：sql注入攻击  - robot：恶意爬虫  - rfi：远程文件包含  - rce：远程代码执行 - ptr：目录遍历 - lfi：本地文件包含 - antileakage：网站信息泄漏  - iprank：IP信誉库 - custom_whiteblackip：IP黑白名单 - custom_whiteip：白名单 - custom_blackip：黑名单 - custom_robot：扫描器爬虫 - custom_geoip：地理访问控制 - custom_idc_ip：IDC情报 - custom_custom：精准防护  - cmdi：命令注入攻击  - cc：cc攻击  - antitamper：网页防篡改  - anticrawler：网站反爬虫   - third_bot_river：第三方反爬虫 - antiscan_high_freq_scan：高频扫描封禁 - antiscan_dir_traversal：目录遍历防护 - illegal：非法请求 - followed_action：攻击惩罚 - advanced_bot：BOT管理 - llm_prompt_injection：提示词注入攻击 - llm_prompt_sensitive：提示词违规 - llm_response_sensitive：响应违规 **默认取值：** 不涉及
        :type nattacks: list[str]
        :param rules: **参数解释：** 规则id列表 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type rules: list[str]
        :param nrules: **参数解释：** 规则id列表（排除搜索） **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type nrules: list[str]
        :param sips: **参数解释：** 客户端IP列表 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type sips: list[str]
        :param nsips: **参数解释：** 客户端IP列表（排除搜索） **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type nsips: list[str]
        :param sip: **参数解释：** 客户端IP，当query_mode为\&quot;equal\&quot;时为精确查询，否则模糊查询 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type sip: str
        :param urls: **参数解释：** url列表 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type urls: list[str]
        :param nurls: **参数解释：** url列表（排除搜索） **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type nurls: list[str]
        :param url: **参数解释：** URL，当query_mode为\&quot;equal\&quot;时为精确查询，否则模糊查询 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type url: str
        :param actions: **参数解释：** 防护动作列表 **约束限制：** 不涉及 **取值范围：** - block：拦截 - pass：放行 - log：仅记录 - captcha：人机验证 - cache：不匹配 - mask：过滤 - js_challenge：JS挑战 - advanced_captcha：高级人机验证 - abort_response：中断响应 - desensitize：脱敏 **默认取值：** 不涉及
        :type actions: list[str]
        :param nactions: **参数解释：** 防护动作列表（排除搜索） **约束限制：** 不涉及 **取值范围：** - block：拦截 - pass：放行 - log：仅记录 - captcha：人机验证 - cache：不匹配 - mask：过滤 - js_challenge：JS挑战 - advanced_captcha：高级人机验证 - abort_response：中断响应 - desensitize：脱敏 **默认取值：** 不涉及
        :type nactions: list[str]
        :param domain: **参数解释：** 域名，支持模糊查询 **约束限制：** domain和ndomain不可同时查询，当两个都存在时以domain为准 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type domain: str
        :param ndomain: **参数解释：** 域名（排除搜索），支持模糊查询 **约束限制：** domain和ndomain不可同时查询，当两个都存在时以domain为准 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type ndomain: str
        :param domains: **参数解释：** 域名列表 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type domains: list[str]
        :param ip_countries: **参数解释：** 客户端IP所属国家列表 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type ip_countries: list[str]
        :param nip_countries: **参数解释：** 客户端IP所属国家列表（排除搜索） **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type nip_countries: list[str]
        :param ip_regions: **参数解释：** 客户端IP所属省份列表，仅中国省份生效 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type ip_regions: list[str]
        :param nip_regions: **参数解释：** 客户端IP所属身份列表（排除搜索），仅中国省份生效 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type nip_regions: list[str]
        :param response_codes: **参数解释：** 响应码列表 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type response_codes: list[str]
        :param payload: **参数解释：** 恶意负载（被WAF识别的攻击片段）： Web 基础防护(SQL注入、XSS、命令注入等)：被WAF识别的攻击片段 CC 攻击：命中规则的请求次数 精准防护、IP黑白名单、地理访问控制：空 攻击惩罚：命中攻击惩罚的用户标识 恶意爬虫：命中规则的 User-Agent 字段 网页反爬虫：JS 脚本事件：js_verified（JS 脚本验证通过事件）和 js_challenge（发送 JS 验证内容事件）。如果请求验证失败则为空。 网站信息泄露：敏感信息过滤为过滤类型，既电话号码,电子邮箱,身份证号；响应码拦截则为拦截的响应码值。 BOT攻击：命中规则的User-Agent等异常请求特征，或AI行为检测结果的评分细节 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type payload: str
        :param hosts: **参数解释：** 域名id列表，从获取防护网站列表（ListHost）接口获取域名id **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type hosts: list[str]
        :param instances: **参数解释：** 引擎实例id列表 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type instances: list[str]
        :param page: **参数解释：** 分页查询时，返回第几页数据 **约束限制：** 不涉及 **取值范围：** page参数的实际有效范围取决于总数据量和pagesize的取值，不能大于总页数 **默认取值：** 1
        :type page: int
        :param pagesize: **参数解释：** 分页查询时，每页包含的结果条数 **约束限制：** 不涉及 **取值范围：** [0, 总数据量] **默认取值：** 10
        :type pagesize: int
        :param sort_key: **参数解释：** 排序字段，默认attack_time，选择其他字段时，会按照指定字段和attack_time共同排序 **约束限制：** 不涉及 **取值范围：** - attack_time 攻击时间 - sort_ip 客户端IP - host 域名 - geo_str 地理位置 - component 应用组件 - rule 规则ID - attack 事件类型（攻击类型） **默认取值：** attack_time
        :type sort_key: str
        :param sort_direction: **参数解释：** 排序方向 **约束限制：** 不涉及 **取值范围：** - desc 降序 - asc 升序 **默认取值：** desc
        :type sort_direction: str
        :param query_mode: **参数解释：** 查询模式，仅影响参数sip、url **约束限制：** 不涉及 **取值范围：** - equal 精确查询 - include 模糊查询 **默认取值：** include
        :type query_mode: str
        """
        
        

        self._x_language = None
        self._enterprise_project_id = None
        self._recent = None
        self.__from = None
        self._to = None
        self._ids = None
        self._nids = None
        self._attacks = None
        self._nattacks = None
        self._rules = None
        self._nrules = None
        self._sips = None
        self._nsips = None
        self._sip = None
        self._urls = None
        self._nurls = None
        self._url = None
        self._actions = None
        self._nactions = None
        self._domain = None
        self._ndomain = None
        self._domains = None
        self._ip_countries = None
        self._nip_countries = None
        self._ip_regions = None
        self._nip_regions = None
        self._response_codes = None
        self._payload = None
        self._hosts = None
        self._instances = None
        self._page = None
        self._pagesize = None
        self._sort_key = None
        self._sort_direction = None
        self._query_mode = None
        self.discriminator = None

        if x_language is not None:
            self.x_language = x_language
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if recent is not None:
            self.recent = recent
        if _from is not None:
            self._from = _from
        if to is not None:
            self.to = to
        if ids is not None:
            self.ids = ids
        if nids is not None:
            self.nids = nids
        if attacks is not None:
            self.attacks = attacks
        if nattacks is not None:
            self.nattacks = nattacks
        if rules is not None:
            self.rules = rules
        if nrules is not None:
            self.nrules = nrules
        if sips is not None:
            self.sips = sips
        if nsips is not None:
            self.nsips = nsips
        if sip is not None:
            self.sip = sip
        if urls is not None:
            self.urls = urls
        if nurls is not None:
            self.nurls = nurls
        if url is not None:
            self.url = url
        if actions is not None:
            self.actions = actions
        if nactions is not None:
            self.nactions = nactions
        if domain is not None:
            self.domain = domain
        if ndomain is not None:
            self.ndomain = ndomain
        if domains is not None:
            self.domains = domains
        if ip_countries is not None:
            self.ip_countries = ip_countries
        if nip_countries is not None:
            self.nip_countries = nip_countries
        if ip_regions is not None:
            self.ip_regions = ip_regions
        if nip_regions is not None:
            self.nip_regions = nip_regions
        if response_codes is not None:
            self.response_codes = response_codes
        if payload is not None:
            self.payload = payload
        if hosts is not None:
            self.hosts = hosts
        if instances is not None:
            self.instances = instances
        if page is not None:
            self.page = page
        if pagesize is not None:
            self.pagesize = pagesize
        if sort_key is not None:
            self.sort_key = sort_key
        if sort_direction is not None:
            self.sort_direction = sort_direction
        if query_mode is not None:
            self.query_mode = query_mode

    @property
    def x_language(self):
        r"""Gets the x_language of this ListEventRequest.

        **参数解释：** 客户端IP所属地理位置展示语言，默认值为en-us **约束限制：** 不涉及 **取值范围：** - zh-cn 中文 - en-us 英文 **默认取值：** en-us

        :return: The x_language of this ListEventRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this ListEventRequest.

        **参数解释：** 客户端IP所属地理位置展示语言，默认值为en-us **约束限制：** 不涉及 **取值范围：** - zh-cn 中文 - en-us 英文 **默认取值：** en-us

        :param x_language: The x_language of this ListEventRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListEventRequest.

        您可以通过调用企业项目管理服务（EPS）的查询企业项目列表接口（ListEnterpriseProject）查询企业项目id。若需要查询当前用户所有企业项目绑定的资源信息，请传参all_granted_eps。

        :return: The enterprise_project_id of this ListEventRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListEventRequest.

        您可以通过调用企业项目管理服务（EPS）的查询企业项目列表接口（ListEnterpriseProject）查询企业项目id。若需要查询当前用户所有企业项目绑定的资源信息，请传参all_granted_eps。

        :param enterprise_project_id: The enterprise_project_id of this ListEventRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def recent(self):
        r"""Gets the recent of this ListEventRequest.

        **参数解释：** 查询日志的时间范围，recent参数与from、to必须使用其中一个。当同时使用recent参数与from、to时，以recent参数为准 **约束限制：** 不涉及 **取值范围：**  - yesterday：昨天  - today：今天  - 3days：近3天   - 1week：近7天   - 1month：近30天  **默认取值：** 不涉及

        :return: The recent of this ListEventRequest.
        :rtype: str
        """
        return self._recent

    @recent.setter
    def recent(self, recent):
        r"""Sets the recent of this ListEventRequest.

        **参数解释：** 查询日志的时间范围，recent参数与from、to必须使用其中一个。当同时使用recent参数与from、to时，以recent参数为准 **约束限制：** 不涉及 **取值范围：**  - yesterday：昨天  - today：今天  - 3days：近3天   - 1week：近7天   - 1month：近30天  **默认取值：** 不涉及

        :param recent: The recent of this ListEventRequest.
        :type recent: str
        """
        self._recent = recent

    @property
    def _from(self):
        r"""Gets the _from of this ListEventRequest.

        **参数解释：** 起始时间(毫秒时间戳)，需要和to同时使用 **约束限制：** from <= to **取值范围：** from ~ to 最大范围30天 **默认取值：** 不涉及

        :return: The _from of this ListEventRequest.
        :rtype: int
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        r"""Sets the _from of this ListEventRequest.

        **参数解释：** 起始时间(毫秒时间戳)，需要和to同时使用 **约束限制：** from <= to **取值范围：** from ~ to 最大范围30天 **默认取值：** 不涉及

        :param _from: The _from of this ListEventRequest.
        :type _from: int
        """
        self.__from = _from

    @property
    def to(self):
        r"""Gets the to of this ListEventRequest.

        **参数解释：** 结束时间(毫秒时间戳)，需要和from同时使用 **约束限制：** from ~ to 最大范围30天 **取值范围：** 不能超过当天的结束时间 **默认取值：** 不涉及

        :return: The to of this ListEventRequest.
        :rtype: int
        """
        return self._to

    @to.setter
    def to(self, to):
        r"""Sets the to of this ListEventRequest.

        **参数解释：** 结束时间(毫秒时间戳)，需要和from同时使用 **约束限制：** from ~ to 最大范围30天 **取值范围：** 不能超过当天的结束时间 **默认取值：** 不涉及

        :param to: The to of this ListEventRequest.
        :type to: int
        """
        self._to = to

    @property
    def ids(self):
        r"""Gets the ids of this ListEventRequest.

        **参数解释：** 防护事件id列表，支持模糊查询 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The ids of this ListEventRequest.
        :rtype: list[str]
        """
        return self._ids

    @ids.setter
    def ids(self, ids):
        r"""Sets the ids of this ListEventRequest.

        **参数解释：** 防护事件id列表，支持模糊查询 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param ids: The ids of this ListEventRequest.
        :type ids: list[str]
        """
        self._ids = ids

    @property
    def nids(self):
        r"""Gets the nids of this ListEventRequest.

        **参数解释：** 防护事件id列表（排除搜索），支持模糊查询 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The nids of this ListEventRequest.
        :rtype: list[str]
        """
        return self._nids

    @nids.setter
    def nids(self, nids):
        r"""Sets the nids of this ListEventRequest.

        **参数解释：** 防护事件id列表（排除搜索），支持模糊查询 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param nids: The nids of this ListEventRequest.
        :type nids: list[str]
        """
        self._nids = nids

    @property
    def attacks(self):
        r"""Gets the attacks of this ListEventRequest.

        **参数解释：** 攻击类型 **约束限制：** 不涉及 **取值范围：** - xss：XSS攻击  - botm：BOT攻击 - webshell：网站木马  - vuln：其他漏洞攻击 - sqli：sql注入攻击  - robot：恶意爬虫  - rfi：远程文件包含  - rce：远程代码执行 - ptr：目录遍历 - lfi：本地文件包含 - antileakage：网站信息泄漏  - iprank：IP信誉库 - custom_whiteblackip：IP黑白名单 - custom_whiteip：白名单 - custom_blackip：黑名单 - custom_robot：扫描器爬虫 - custom_geoip：地理访问控制 - custom_idc_ip：IDC情报 - custom_custom：精准防护  - cmdi：命令注入攻击  - cc：cc攻击  - antitamper：网页防篡改  - anticrawler：网站反爬虫   - third_bot_river：第三方反爬虫 - antiscan_high_freq_scan：高频扫描封禁 - antiscan_dir_traversal：目录遍历防护 - illegal：非法请求 - followed_action：攻击惩罚 - advanced_bot：BOT管理 - llm_prompt_injection：提示词注入攻击 - llm_prompt_sensitive：提示词违规 - llm_response_sensitive：响应违规 **默认取值：** 不涉及

        :return: The attacks of this ListEventRequest.
        :rtype: list[str]
        """
        return self._attacks

    @attacks.setter
    def attacks(self, attacks):
        r"""Sets the attacks of this ListEventRequest.

        **参数解释：** 攻击类型 **约束限制：** 不涉及 **取值范围：** - xss：XSS攻击  - botm：BOT攻击 - webshell：网站木马  - vuln：其他漏洞攻击 - sqli：sql注入攻击  - robot：恶意爬虫  - rfi：远程文件包含  - rce：远程代码执行 - ptr：目录遍历 - lfi：本地文件包含 - antileakage：网站信息泄漏  - iprank：IP信誉库 - custom_whiteblackip：IP黑白名单 - custom_whiteip：白名单 - custom_blackip：黑名单 - custom_robot：扫描器爬虫 - custom_geoip：地理访问控制 - custom_idc_ip：IDC情报 - custom_custom：精准防护  - cmdi：命令注入攻击  - cc：cc攻击  - antitamper：网页防篡改  - anticrawler：网站反爬虫   - third_bot_river：第三方反爬虫 - antiscan_high_freq_scan：高频扫描封禁 - antiscan_dir_traversal：目录遍历防护 - illegal：非法请求 - followed_action：攻击惩罚 - advanced_bot：BOT管理 - llm_prompt_injection：提示词注入攻击 - llm_prompt_sensitive：提示词违规 - llm_response_sensitive：响应违规 **默认取值：** 不涉及

        :param attacks: The attacks of this ListEventRequest.
        :type attacks: list[str]
        """
        self._attacks = attacks

    @property
    def nattacks(self):
        r"""Gets the nattacks of this ListEventRequest.

        **参数解释：** 攻击类型（排除搜索） **约束限制：** 不涉及 **取值范围：** - xss：XSS攻击  - botm：BOT攻击 - webshell：网站木马  - vuln：其他漏洞攻击 - sqli：sql注入攻击  - robot：恶意爬虫  - rfi：远程文件包含  - rce：远程代码执行 - ptr：目录遍历 - lfi：本地文件包含 - antileakage：网站信息泄漏  - iprank：IP信誉库 - custom_whiteblackip：IP黑白名单 - custom_whiteip：白名单 - custom_blackip：黑名单 - custom_robot：扫描器爬虫 - custom_geoip：地理访问控制 - custom_idc_ip：IDC情报 - custom_custom：精准防护  - cmdi：命令注入攻击  - cc：cc攻击  - antitamper：网页防篡改  - anticrawler：网站反爬虫   - third_bot_river：第三方反爬虫 - antiscan_high_freq_scan：高频扫描封禁 - antiscan_dir_traversal：目录遍历防护 - illegal：非法请求 - followed_action：攻击惩罚 - advanced_bot：BOT管理 - llm_prompt_injection：提示词注入攻击 - llm_prompt_sensitive：提示词违规 - llm_response_sensitive：响应违规 **默认取值：** 不涉及

        :return: The nattacks of this ListEventRequest.
        :rtype: list[str]
        """
        return self._nattacks

    @nattacks.setter
    def nattacks(self, nattacks):
        r"""Sets the nattacks of this ListEventRequest.

        **参数解释：** 攻击类型（排除搜索） **约束限制：** 不涉及 **取值范围：** - xss：XSS攻击  - botm：BOT攻击 - webshell：网站木马  - vuln：其他漏洞攻击 - sqli：sql注入攻击  - robot：恶意爬虫  - rfi：远程文件包含  - rce：远程代码执行 - ptr：目录遍历 - lfi：本地文件包含 - antileakage：网站信息泄漏  - iprank：IP信誉库 - custom_whiteblackip：IP黑白名单 - custom_whiteip：白名单 - custom_blackip：黑名单 - custom_robot：扫描器爬虫 - custom_geoip：地理访问控制 - custom_idc_ip：IDC情报 - custom_custom：精准防护  - cmdi：命令注入攻击  - cc：cc攻击  - antitamper：网页防篡改  - anticrawler：网站反爬虫   - third_bot_river：第三方反爬虫 - antiscan_high_freq_scan：高频扫描封禁 - antiscan_dir_traversal：目录遍历防护 - illegal：非法请求 - followed_action：攻击惩罚 - advanced_bot：BOT管理 - llm_prompt_injection：提示词注入攻击 - llm_prompt_sensitive：提示词违规 - llm_response_sensitive：响应违规 **默认取值：** 不涉及

        :param nattacks: The nattacks of this ListEventRequest.
        :type nattacks: list[str]
        """
        self._nattacks = nattacks

    @property
    def rules(self):
        r"""Gets the rules of this ListEventRequest.

        **参数解释：** 规则id列表 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The rules of this ListEventRequest.
        :rtype: list[str]
        """
        return self._rules

    @rules.setter
    def rules(self, rules):
        r"""Sets the rules of this ListEventRequest.

        **参数解释：** 规则id列表 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param rules: The rules of this ListEventRequest.
        :type rules: list[str]
        """
        self._rules = rules

    @property
    def nrules(self):
        r"""Gets the nrules of this ListEventRequest.

        **参数解释：** 规则id列表（排除搜索） **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The nrules of this ListEventRequest.
        :rtype: list[str]
        """
        return self._nrules

    @nrules.setter
    def nrules(self, nrules):
        r"""Sets the nrules of this ListEventRequest.

        **参数解释：** 规则id列表（排除搜索） **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param nrules: The nrules of this ListEventRequest.
        :type nrules: list[str]
        """
        self._nrules = nrules

    @property
    def sips(self):
        r"""Gets the sips of this ListEventRequest.

        **参数解释：** 客户端IP列表 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The sips of this ListEventRequest.
        :rtype: list[str]
        """
        return self._sips

    @sips.setter
    def sips(self, sips):
        r"""Sets the sips of this ListEventRequest.

        **参数解释：** 客户端IP列表 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param sips: The sips of this ListEventRequest.
        :type sips: list[str]
        """
        self._sips = sips

    @property
    def nsips(self):
        r"""Gets the nsips of this ListEventRequest.

        **参数解释：** 客户端IP列表（排除搜索） **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The nsips of this ListEventRequest.
        :rtype: list[str]
        """
        return self._nsips

    @nsips.setter
    def nsips(self, nsips):
        r"""Sets the nsips of this ListEventRequest.

        **参数解释：** 客户端IP列表（排除搜索） **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param nsips: The nsips of this ListEventRequest.
        :type nsips: list[str]
        """
        self._nsips = nsips

    @property
    def sip(self):
        r"""Gets the sip of this ListEventRequest.

        **参数解释：** 客户端IP，当query_mode为\"equal\"时为精确查询，否则模糊查询 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The sip of this ListEventRequest.
        :rtype: str
        """
        return self._sip

    @sip.setter
    def sip(self, sip):
        r"""Sets the sip of this ListEventRequest.

        **参数解释：** 客户端IP，当query_mode为\"equal\"时为精确查询，否则模糊查询 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param sip: The sip of this ListEventRequest.
        :type sip: str
        """
        self._sip = sip

    @property
    def urls(self):
        r"""Gets the urls of this ListEventRequest.

        **参数解释：** url列表 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The urls of this ListEventRequest.
        :rtype: list[str]
        """
        return self._urls

    @urls.setter
    def urls(self, urls):
        r"""Sets the urls of this ListEventRequest.

        **参数解释：** url列表 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param urls: The urls of this ListEventRequest.
        :type urls: list[str]
        """
        self._urls = urls

    @property
    def nurls(self):
        r"""Gets the nurls of this ListEventRequest.

        **参数解释：** url列表（排除搜索） **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The nurls of this ListEventRequest.
        :rtype: list[str]
        """
        return self._nurls

    @nurls.setter
    def nurls(self, nurls):
        r"""Sets the nurls of this ListEventRequest.

        **参数解释：** url列表（排除搜索） **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param nurls: The nurls of this ListEventRequest.
        :type nurls: list[str]
        """
        self._nurls = nurls

    @property
    def url(self):
        r"""Gets the url of this ListEventRequest.

        **参数解释：** URL，当query_mode为\"equal\"时为精确查询，否则模糊查询 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The url of this ListEventRequest.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        r"""Sets the url of this ListEventRequest.

        **参数解释：** URL，当query_mode为\"equal\"时为精确查询，否则模糊查询 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param url: The url of this ListEventRequest.
        :type url: str
        """
        self._url = url

    @property
    def actions(self):
        r"""Gets the actions of this ListEventRequest.

        **参数解释：** 防护动作列表 **约束限制：** 不涉及 **取值范围：** - block：拦截 - pass：放行 - log：仅记录 - captcha：人机验证 - cache：不匹配 - mask：过滤 - js_challenge：JS挑战 - advanced_captcha：高级人机验证 - abort_response：中断响应 - desensitize：脱敏 **默认取值：** 不涉及

        :return: The actions of this ListEventRequest.
        :rtype: list[str]
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        r"""Sets the actions of this ListEventRequest.

        **参数解释：** 防护动作列表 **约束限制：** 不涉及 **取值范围：** - block：拦截 - pass：放行 - log：仅记录 - captcha：人机验证 - cache：不匹配 - mask：过滤 - js_challenge：JS挑战 - advanced_captcha：高级人机验证 - abort_response：中断响应 - desensitize：脱敏 **默认取值：** 不涉及

        :param actions: The actions of this ListEventRequest.
        :type actions: list[str]
        """
        self._actions = actions

    @property
    def nactions(self):
        r"""Gets the nactions of this ListEventRequest.

        **参数解释：** 防护动作列表（排除搜索） **约束限制：** 不涉及 **取值范围：** - block：拦截 - pass：放行 - log：仅记录 - captcha：人机验证 - cache：不匹配 - mask：过滤 - js_challenge：JS挑战 - advanced_captcha：高级人机验证 - abort_response：中断响应 - desensitize：脱敏 **默认取值：** 不涉及

        :return: The nactions of this ListEventRequest.
        :rtype: list[str]
        """
        return self._nactions

    @nactions.setter
    def nactions(self, nactions):
        r"""Sets the nactions of this ListEventRequest.

        **参数解释：** 防护动作列表（排除搜索） **约束限制：** 不涉及 **取值范围：** - block：拦截 - pass：放行 - log：仅记录 - captcha：人机验证 - cache：不匹配 - mask：过滤 - js_challenge：JS挑战 - advanced_captcha：高级人机验证 - abort_response：中断响应 - desensitize：脱敏 **默认取值：** 不涉及

        :param nactions: The nactions of this ListEventRequest.
        :type nactions: list[str]
        """
        self._nactions = nactions

    @property
    def domain(self):
        r"""Gets the domain of this ListEventRequest.

        **参数解释：** 域名，支持模糊查询 **约束限制：** domain和ndomain不可同时查询，当两个都存在时以domain为准 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The domain of this ListEventRequest.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        r"""Sets the domain of this ListEventRequest.

        **参数解释：** 域名，支持模糊查询 **约束限制：** domain和ndomain不可同时查询，当两个都存在时以domain为准 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param domain: The domain of this ListEventRequest.
        :type domain: str
        """
        self._domain = domain

    @property
    def ndomain(self):
        r"""Gets the ndomain of this ListEventRequest.

        **参数解释：** 域名（排除搜索），支持模糊查询 **约束限制：** domain和ndomain不可同时查询，当两个都存在时以domain为准 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The ndomain of this ListEventRequest.
        :rtype: str
        """
        return self._ndomain

    @ndomain.setter
    def ndomain(self, ndomain):
        r"""Sets the ndomain of this ListEventRequest.

        **参数解释：** 域名（排除搜索），支持模糊查询 **约束限制：** domain和ndomain不可同时查询，当两个都存在时以domain为准 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param ndomain: The ndomain of this ListEventRequest.
        :type ndomain: str
        """
        self._ndomain = ndomain

    @property
    def domains(self):
        r"""Gets the domains of this ListEventRequest.

        **参数解释：** 域名列表 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The domains of this ListEventRequest.
        :rtype: list[str]
        """
        return self._domains

    @domains.setter
    def domains(self, domains):
        r"""Sets the domains of this ListEventRequest.

        **参数解释：** 域名列表 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param domains: The domains of this ListEventRequest.
        :type domains: list[str]
        """
        self._domains = domains

    @property
    def ip_countries(self):
        r"""Gets the ip_countries of this ListEventRequest.

        **参数解释：** 客户端IP所属国家列表 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The ip_countries of this ListEventRequest.
        :rtype: list[str]
        """
        return self._ip_countries

    @ip_countries.setter
    def ip_countries(self, ip_countries):
        r"""Sets the ip_countries of this ListEventRequest.

        **参数解释：** 客户端IP所属国家列表 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param ip_countries: The ip_countries of this ListEventRequest.
        :type ip_countries: list[str]
        """
        self._ip_countries = ip_countries

    @property
    def nip_countries(self):
        r"""Gets the nip_countries of this ListEventRequest.

        **参数解释：** 客户端IP所属国家列表（排除搜索） **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The nip_countries of this ListEventRequest.
        :rtype: list[str]
        """
        return self._nip_countries

    @nip_countries.setter
    def nip_countries(self, nip_countries):
        r"""Sets the nip_countries of this ListEventRequest.

        **参数解释：** 客户端IP所属国家列表（排除搜索） **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param nip_countries: The nip_countries of this ListEventRequest.
        :type nip_countries: list[str]
        """
        self._nip_countries = nip_countries

    @property
    def ip_regions(self):
        r"""Gets the ip_regions of this ListEventRequest.

        **参数解释：** 客户端IP所属省份列表，仅中国省份生效 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The ip_regions of this ListEventRequest.
        :rtype: list[str]
        """
        return self._ip_regions

    @ip_regions.setter
    def ip_regions(self, ip_regions):
        r"""Sets the ip_regions of this ListEventRequest.

        **参数解释：** 客户端IP所属省份列表，仅中国省份生效 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param ip_regions: The ip_regions of this ListEventRequest.
        :type ip_regions: list[str]
        """
        self._ip_regions = ip_regions

    @property
    def nip_regions(self):
        r"""Gets the nip_regions of this ListEventRequest.

        **参数解释：** 客户端IP所属身份列表（排除搜索），仅中国省份生效 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The nip_regions of this ListEventRequest.
        :rtype: list[str]
        """
        return self._nip_regions

    @nip_regions.setter
    def nip_regions(self, nip_regions):
        r"""Sets the nip_regions of this ListEventRequest.

        **参数解释：** 客户端IP所属身份列表（排除搜索），仅中国省份生效 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param nip_regions: The nip_regions of this ListEventRequest.
        :type nip_regions: list[str]
        """
        self._nip_regions = nip_regions

    @property
    def response_codes(self):
        r"""Gets the response_codes of this ListEventRequest.

        **参数解释：** 响应码列表 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The response_codes of this ListEventRequest.
        :rtype: list[str]
        """
        return self._response_codes

    @response_codes.setter
    def response_codes(self, response_codes):
        r"""Sets the response_codes of this ListEventRequest.

        **参数解释：** 响应码列表 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param response_codes: The response_codes of this ListEventRequest.
        :type response_codes: list[str]
        """
        self._response_codes = response_codes

    @property
    def payload(self):
        r"""Gets the payload of this ListEventRequest.

        **参数解释：** 恶意负载（被WAF识别的攻击片段）： Web 基础防护(SQL注入、XSS、命令注入等)：被WAF识别的攻击片段 CC 攻击：命中规则的请求次数 精准防护、IP黑白名单、地理访问控制：空 攻击惩罚：命中攻击惩罚的用户标识 恶意爬虫：命中规则的 User-Agent 字段 网页反爬虫：JS 脚本事件：js_verified（JS 脚本验证通过事件）和 js_challenge（发送 JS 验证内容事件）。如果请求验证失败则为空。 网站信息泄露：敏感信息过滤为过滤类型，既电话号码,电子邮箱,身份证号；响应码拦截则为拦截的响应码值。 BOT攻击：命中规则的User-Agent等异常请求特征，或AI行为检测结果的评分细节 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The payload of this ListEventRequest.
        :rtype: str
        """
        return self._payload

    @payload.setter
    def payload(self, payload):
        r"""Sets the payload of this ListEventRequest.

        **参数解释：** 恶意负载（被WAF识别的攻击片段）： Web 基础防护(SQL注入、XSS、命令注入等)：被WAF识别的攻击片段 CC 攻击：命中规则的请求次数 精准防护、IP黑白名单、地理访问控制：空 攻击惩罚：命中攻击惩罚的用户标识 恶意爬虫：命中规则的 User-Agent 字段 网页反爬虫：JS 脚本事件：js_verified（JS 脚本验证通过事件）和 js_challenge（发送 JS 验证内容事件）。如果请求验证失败则为空。 网站信息泄露：敏感信息过滤为过滤类型，既电话号码,电子邮箱,身份证号；响应码拦截则为拦截的响应码值。 BOT攻击：命中规则的User-Agent等异常请求特征，或AI行为检测结果的评分细节 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param payload: The payload of this ListEventRequest.
        :type payload: str
        """
        self._payload = payload

    @property
    def hosts(self):
        r"""Gets the hosts of this ListEventRequest.

        **参数解释：** 域名id列表，从获取防护网站列表（ListHost）接口获取域名id **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The hosts of this ListEventRequest.
        :rtype: list[str]
        """
        return self._hosts

    @hosts.setter
    def hosts(self, hosts):
        r"""Sets the hosts of this ListEventRequest.

        **参数解释：** 域名id列表，从获取防护网站列表（ListHost）接口获取域名id **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param hosts: The hosts of this ListEventRequest.
        :type hosts: list[str]
        """
        self._hosts = hosts

    @property
    def instances(self):
        r"""Gets the instances of this ListEventRequest.

        **参数解释：** 引擎实例id列表 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The instances of this ListEventRequest.
        :rtype: list[str]
        """
        return self._instances

    @instances.setter
    def instances(self, instances):
        r"""Sets the instances of this ListEventRequest.

        **参数解释：** 引擎实例id列表 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param instances: The instances of this ListEventRequest.
        :type instances: list[str]
        """
        self._instances = instances

    @property
    def page(self):
        r"""Gets the page of this ListEventRequest.

        **参数解释：** 分页查询时，返回第几页数据 **约束限制：** 不涉及 **取值范围：** page参数的实际有效范围取决于总数据量和pagesize的取值，不能大于总页数 **默认取值：** 1

        :return: The page of this ListEventRequest.
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        r"""Sets the page of this ListEventRequest.

        **参数解释：** 分页查询时，返回第几页数据 **约束限制：** 不涉及 **取值范围：** page参数的实际有效范围取决于总数据量和pagesize的取值，不能大于总页数 **默认取值：** 1

        :param page: The page of this ListEventRequest.
        :type page: int
        """
        self._page = page

    @property
    def pagesize(self):
        r"""Gets the pagesize of this ListEventRequest.

        **参数解释：** 分页查询时，每页包含的结果条数 **约束限制：** 不涉及 **取值范围：** [0, 总数据量] **默认取值：** 10

        :return: The pagesize of this ListEventRequest.
        :rtype: int
        """
        return self._pagesize

    @pagesize.setter
    def pagesize(self, pagesize):
        r"""Sets the pagesize of this ListEventRequest.

        **参数解释：** 分页查询时，每页包含的结果条数 **约束限制：** 不涉及 **取值范围：** [0, 总数据量] **默认取值：** 10

        :param pagesize: The pagesize of this ListEventRequest.
        :type pagesize: int
        """
        self._pagesize = pagesize

    @property
    def sort_key(self):
        r"""Gets the sort_key of this ListEventRequest.

        **参数解释：** 排序字段，默认attack_time，选择其他字段时，会按照指定字段和attack_time共同排序 **约束限制：** 不涉及 **取值范围：** - attack_time 攻击时间 - sort_ip 客户端IP - host 域名 - geo_str 地理位置 - component 应用组件 - rule 规则ID - attack 事件类型（攻击类型） **默认取值：** attack_time

        :return: The sort_key of this ListEventRequest.
        :rtype: str
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        r"""Sets the sort_key of this ListEventRequest.

        **参数解释：** 排序字段，默认attack_time，选择其他字段时，会按照指定字段和attack_time共同排序 **约束限制：** 不涉及 **取值范围：** - attack_time 攻击时间 - sort_ip 客户端IP - host 域名 - geo_str 地理位置 - component 应用组件 - rule 规则ID - attack 事件类型（攻击类型） **默认取值：** attack_time

        :param sort_key: The sort_key of this ListEventRequest.
        :type sort_key: str
        """
        self._sort_key = sort_key

    @property
    def sort_direction(self):
        r"""Gets the sort_direction of this ListEventRequest.

        **参数解释：** 排序方向 **约束限制：** 不涉及 **取值范围：** - desc 降序 - asc 升序 **默认取值：** desc

        :return: The sort_direction of this ListEventRequest.
        :rtype: str
        """
        return self._sort_direction

    @sort_direction.setter
    def sort_direction(self, sort_direction):
        r"""Sets the sort_direction of this ListEventRequest.

        **参数解释：** 排序方向 **约束限制：** 不涉及 **取值范围：** - desc 降序 - asc 升序 **默认取值：** desc

        :param sort_direction: The sort_direction of this ListEventRequest.
        :type sort_direction: str
        """
        self._sort_direction = sort_direction

    @property
    def query_mode(self):
        r"""Gets the query_mode of this ListEventRequest.

        **参数解释：** 查询模式，仅影响参数sip、url **约束限制：** 不涉及 **取值范围：** - equal 精确查询 - include 模糊查询 **默认取值：** include

        :return: The query_mode of this ListEventRequest.
        :rtype: str
        """
        return self._query_mode

    @query_mode.setter
    def query_mode(self, query_mode):
        r"""Sets the query_mode of this ListEventRequest.

        **参数解释：** 查询模式，仅影响参数sip、url **约束限制：** 不涉及 **取值范围：** - equal 精确查询 - include 模糊查询 **默认取值：** include

        :param query_mode: The query_mode of this ListEventRequest.
        :type query_mode: str
        """
        self._query_mode = query_mode

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
        if not isinstance(other, ListEventRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
