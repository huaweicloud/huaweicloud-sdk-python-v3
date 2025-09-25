# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AsyncJobReqBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'recent': 'str',
        'ids': 'list[str]',
        'nids': 'list[str]',
        'attacks': 'list[str]',
        'nattacks': 'list[str]',
        'rules': 'list[str]',
        'nrules': 'list[str]',
        'sip': 'str',
        'url': 'str',
        'sips': 'list[str]',
        'nsips': 'list[str]',
        'urls': 'list[str]',
        'nurls': 'list[str]',
        'actions': 'list[str]',
        'nactions': 'list[str]',
        'hosts': 'list[str]',
        'instances': 'list[str]',
        'dump_columns': 'list[str]'
    }

    attribute_map = {
        'recent': 'recent',
        'ids': 'ids',
        'nids': 'nids',
        'attacks': 'attacks',
        'nattacks': 'nattacks',
        'rules': 'rules',
        'nrules': 'nrules',
        'sip': 'sip',
        'url': 'url',
        'sips': 'sips',
        'nsips': 'nsips',
        'urls': 'urls',
        'nurls': 'nurls',
        'actions': 'actions',
        'nactions': 'nactions',
        'hosts': 'hosts',
        'instances': 'instances',
        'dump_columns': 'dump_columns'
    }

    def __init__(self, recent=None, ids=None, nids=None, attacks=None, nattacks=None, rules=None, nrules=None, sip=None, url=None, sips=None, nsips=None, urls=None, nurls=None, actions=None, nactions=None, hosts=None, instances=None, dump_columns=None):
        r"""AsyncJobReqBody

        The model defined in huaweicloud sdk

        :param recent: **参数解释：** 查询日志的时间范围，如1day（1天）、1week（1周）、1month（1个月） **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type recent: str
        :param ids: **参数解释：** 查询指定事件ID列表的日志，仅导出包含这些ID的攻击事件 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type ids: list[str]
        :param nids: **参数解释：** 查询不包含事件ID列表的日志，排除这些ID对应的攻击事件 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type nids: list[str]
        :param attacks: **参数解释：** 查询指定攻击类型列表的日志，仅导出这些类型的攻击事件（如SQL注入、XSS等） **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type attacks: list[str]
        :param nattacks: **参数解释：** 查询不包含攻击类型列表的日志，排除这些类型的攻击事件 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type nattacks: list[str]
        :param rules: **参数解释：** 查询指定命中的规则id列表的日志，仅导出命中这些规则的攻击事件 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type rules: list[str]
        :param nrules: **参数解释：** 查询不包含命中的规则id列表的日志，排除命中这些规则的攻击事件 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type nrules: list[str]
        :param sip: **参数解释：** 查询指定源ip(模糊查询)，导出包含该IP（模糊匹配）的攻击事件 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type sip: str
        :param url: **参数解释：** 查询指定攻击的url(模糊查询)，导出包含该URL（模糊匹配）的攻击事件 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type url: str
        :param sips: **参数解释：** 查询指定源ip列表的日志，仅导出这些IP对应的攻击事件 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type sips: list[str]
        :param nsips: **参数解释：** 查询不包含源ip列表的日志，排除这些IP对应的攻击事件 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type nsips: list[str]
        :param urls: **参数解释：** 查询指定攻击的url链接列表的日志，仅导出这些URL对应的攻击事件 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type urls: list[str]
        :param nurls: **参数解释：** 查询不包含攻击的url链接列表的日志，排除这些URL对应的攻击事件 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type nurls: list[str]
        :param actions: **参数解释：** 查询指定防护动作列表的日志，仅导出执行这些动作的攻击事件（如block-拦截、log-日志） **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type actions: list[str]
        :param nactions: **参数解释：** 查询不包含防护动作列表的日志，排除执行这些动作的攻击事件 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type nactions: list[str]
        :param hosts: **参数解释：** 查询指定host列表的日志，仅导出这些域名对应的攻击事件 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type hosts: list[str]
        :param instances: **参数解释：** 查询指定instance列表的日志，仅导出这些实例对应的攻击事件 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type instances: list[str]
        :param dump_columns: **参数解释：** 需要导出的列名称，指定攻击事件日志中需要导出的字段（如时间、事件ID、攻击类型等） **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type dump_columns: list[str]
        """
        
        

        self._recent = None
        self._ids = None
        self._nids = None
        self._attacks = None
        self._nattacks = None
        self._rules = None
        self._nrules = None
        self._sip = None
        self._url = None
        self._sips = None
        self._nsips = None
        self._urls = None
        self._nurls = None
        self._actions = None
        self._nactions = None
        self._hosts = None
        self._instances = None
        self._dump_columns = None
        self.discriminator = None

        self.recent = recent
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
        if sip is not None:
            self.sip = sip
        if url is not None:
            self.url = url
        if sips is not None:
            self.sips = sips
        if nsips is not None:
            self.nsips = nsips
        if urls is not None:
            self.urls = urls
        if nurls is not None:
            self.nurls = nurls
        if actions is not None:
            self.actions = actions
        if nactions is not None:
            self.nactions = nactions
        if hosts is not None:
            self.hosts = hosts
        if instances is not None:
            self.instances = instances
        self.dump_columns = dump_columns

    @property
    def recent(self):
        r"""Gets the recent of this AsyncJobReqBody.

        **参数解释：** 查询日志的时间范围，如1day（1天）、1week（1周）、1month（1个月） **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The recent of this AsyncJobReqBody.
        :rtype: str
        """
        return self._recent

    @recent.setter
    def recent(self, recent):
        r"""Sets the recent of this AsyncJobReqBody.

        **参数解释：** 查询日志的时间范围，如1day（1天）、1week（1周）、1month（1个月） **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param recent: The recent of this AsyncJobReqBody.
        :type recent: str
        """
        self._recent = recent

    @property
    def ids(self):
        r"""Gets the ids of this AsyncJobReqBody.

        **参数解释：** 查询指定事件ID列表的日志，仅导出包含这些ID的攻击事件 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The ids of this AsyncJobReqBody.
        :rtype: list[str]
        """
        return self._ids

    @ids.setter
    def ids(self, ids):
        r"""Sets the ids of this AsyncJobReqBody.

        **参数解释：** 查询指定事件ID列表的日志，仅导出包含这些ID的攻击事件 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param ids: The ids of this AsyncJobReqBody.
        :type ids: list[str]
        """
        self._ids = ids

    @property
    def nids(self):
        r"""Gets the nids of this AsyncJobReqBody.

        **参数解释：** 查询不包含事件ID列表的日志，排除这些ID对应的攻击事件 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The nids of this AsyncJobReqBody.
        :rtype: list[str]
        """
        return self._nids

    @nids.setter
    def nids(self, nids):
        r"""Sets the nids of this AsyncJobReqBody.

        **参数解释：** 查询不包含事件ID列表的日志，排除这些ID对应的攻击事件 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param nids: The nids of this AsyncJobReqBody.
        :type nids: list[str]
        """
        self._nids = nids

    @property
    def attacks(self):
        r"""Gets the attacks of this AsyncJobReqBody.

        **参数解释：** 查询指定攻击类型列表的日志，仅导出这些类型的攻击事件（如SQL注入、XSS等） **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The attacks of this AsyncJobReqBody.
        :rtype: list[str]
        """
        return self._attacks

    @attacks.setter
    def attacks(self, attacks):
        r"""Sets the attacks of this AsyncJobReqBody.

        **参数解释：** 查询指定攻击类型列表的日志，仅导出这些类型的攻击事件（如SQL注入、XSS等） **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param attacks: The attacks of this AsyncJobReqBody.
        :type attacks: list[str]
        """
        self._attacks = attacks

    @property
    def nattacks(self):
        r"""Gets the nattacks of this AsyncJobReqBody.

        **参数解释：** 查询不包含攻击类型列表的日志，排除这些类型的攻击事件 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The nattacks of this AsyncJobReqBody.
        :rtype: list[str]
        """
        return self._nattacks

    @nattacks.setter
    def nattacks(self, nattacks):
        r"""Sets the nattacks of this AsyncJobReqBody.

        **参数解释：** 查询不包含攻击类型列表的日志，排除这些类型的攻击事件 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param nattacks: The nattacks of this AsyncJobReqBody.
        :type nattacks: list[str]
        """
        self._nattacks = nattacks

    @property
    def rules(self):
        r"""Gets the rules of this AsyncJobReqBody.

        **参数解释：** 查询指定命中的规则id列表的日志，仅导出命中这些规则的攻击事件 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The rules of this AsyncJobReqBody.
        :rtype: list[str]
        """
        return self._rules

    @rules.setter
    def rules(self, rules):
        r"""Sets the rules of this AsyncJobReqBody.

        **参数解释：** 查询指定命中的规则id列表的日志，仅导出命中这些规则的攻击事件 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param rules: The rules of this AsyncJobReqBody.
        :type rules: list[str]
        """
        self._rules = rules

    @property
    def nrules(self):
        r"""Gets the nrules of this AsyncJobReqBody.

        **参数解释：** 查询不包含命中的规则id列表的日志，排除命中这些规则的攻击事件 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The nrules of this AsyncJobReqBody.
        :rtype: list[str]
        """
        return self._nrules

    @nrules.setter
    def nrules(self, nrules):
        r"""Sets the nrules of this AsyncJobReqBody.

        **参数解释：** 查询不包含命中的规则id列表的日志，排除命中这些规则的攻击事件 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param nrules: The nrules of this AsyncJobReqBody.
        :type nrules: list[str]
        """
        self._nrules = nrules

    @property
    def sip(self):
        r"""Gets the sip of this AsyncJobReqBody.

        **参数解释：** 查询指定源ip(模糊查询)，导出包含该IP（模糊匹配）的攻击事件 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The sip of this AsyncJobReqBody.
        :rtype: str
        """
        return self._sip

    @sip.setter
    def sip(self, sip):
        r"""Sets the sip of this AsyncJobReqBody.

        **参数解释：** 查询指定源ip(模糊查询)，导出包含该IP（模糊匹配）的攻击事件 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param sip: The sip of this AsyncJobReqBody.
        :type sip: str
        """
        self._sip = sip

    @property
    def url(self):
        r"""Gets the url of this AsyncJobReqBody.

        **参数解释：** 查询指定攻击的url(模糊查询)，导出包含该URL（模糊匹配）的攻击事件 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The url of this AsyncJobReqBody.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        r"""Sets the url of this AsyncJobReqBody.

        **参数解释：** 查询指定攻击的url(模糊查询)，导出包含该URL（模糊匹配）的攻击事件 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param url: The url of this AsyncJobReqBody.
        :type url: str
        """
        self._url = url

    @property
    def sips(self):
        r"""Gets the sips of this AsyncJobReqBody.

        **参数解释：** 查询指定源ip列表的日志，仅导出这些IP对应的攻击事件 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The sips of this AsyncJobReqBody.
        :rtype: list[str]
        """
        return self._sips

    @sips.setter
    def sips(self, sips):
        r"""Sets the sips of this AsyncJobReqBody.

        **参数解释：** 查询指定源ip列表的日志，仅导出这些IP对应的攻击事件 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param sips: The sips of this AsyncJobReqBody.
        :type sips: list[str]
        """
        self._sips = sips

    @property
    def nsips(self):
        r"""Gets the nsips of this AsyncJobReqBody.

        **参数解释：** 查询不包含源ip列表的日志，排除这些IP对应的攻击事件 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The nsips of this AsyncJobReqBody.
        :rtype: list[str]
        """
        return self._nsips

    @nsips.setter
    def nsips(self, nsips):
        r"""Sets the nsips of this AsyncJobReqBody.

        **参数解释：** 查询不包含源ip列表的日志，排除这些IP对应的攻击事件 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param nsips: The nsips of this AsyncJobReqBody.
        :type nsips: list[str]
        """
        self._nsips = nsips

    @property
    def urls(self):
        r"""Gets the urls of this AsyncJobReqBody.

        **参数解释：** 查询指定攻击的url链接列表的日志，仅导出这些URL对应的攻击事件 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The urls of this AsyncJobReqBody.
        :rtype: list[str]
        """
        return self._urls

    @urls.setter
    def urls(self, urls):
        r"""Sets the urls of this AsyncJobReqBody.

        **参数解释：** 查询指定攻击的url链接列表的日志，仅导出这些URL对应的攻击事件 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param urls: The urls of this AsyncJobReqBody.
        :type urls: list[str]
        """
        self._urls = urls

    @property
    def nurls(self):
        r"""Gets the nurls of this AsyncJobReqBody.

        **参数解释：** 查询不包含攻击的url链接列表的日志，排除这些URL对应的攻击事件 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The nurls of this AsyncJobReqBody.
        :rtype: list[str]
        """
        return self._nurls

    @nurls.setter
    def nurls(self, nurls):
        r"""Sets the nurls of this AsyncJobReqBody.

        **参数解释：** 查询不包含攻击的url链接列表的日志，排除这些URL对应的攻击事件 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param nurls: The nurls of this AsyncJobReqBody.
        :type nurls: list[str]
        """
        self._nurls = nurls

    @property
    def actions(self):
        r"""Gets the actions of this AsyncJobReqBody.

        **参数解释：** 查询指定防护动作列表的日志，仅导出执行这些动作的攻击事件（如block-拦截、log-日志） **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The actions of this AsyncJobReqBody.
        :rtype: list[str]
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        r"""Sets the actions of this AsyncJobReqBody.

        **参数解释：** 查询指定防护动作列表的日志，仅导出执行这些动作的攻击事件（如block-拦截、log-日志） **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param actions: The actions of this AsyncJobReqBody.
        :type actions: list[str]
        """
        self._actions = actions

    @property
    def nactions(self):
        r"""Gets the nactions of this AsyncJobReqBody.

        **参数解释：** 查询不包含防护动作列表的日志，排除执行这些动作的攻击事件 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The nactions of this AsyncJobReqBody.
        :rtype: list[str]
        """
        return self._nactions

    @nactions.setter
    def nactions(self, nactions):
        r"""Sets the nactions of this AsyncJobReqBody.

        **参数解释：** 查询不包含防护动作列表的日志，排除执行这些动作的攻击事件 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param nactions: The nactions of this AsyncJobReqBody.
        :type nactions: list[str]
        """
        self._nactions = nactions

    @property
    def hosts(self):
        r"""Gets the hosts of this AsyncJobReqBody.

        **参数解释：** 查询指定host列表的日志，仅导出这些域名对应的攻击事件 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The hosts of this AsyncJobReqBody.
        :rtype: list[str]
        """
        return self._hosts

    @hosts.setter
    def hosts(self, hosts):
        r"""Sets the hosts of this AsyncJobReqBody.

        **参数解释：** 查询指定host列表的日志，仅导出这些域名对应的攻击事件 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param hosts: The hosts of this AsyncJobReqBody.
        :type hosts: list[str]
        """
        self._hosts = hosts

    @property
    def instances(self):
        r"""Gets the instances of this AsyncJobReqBody.

        **参数解释：** 查询指定instance列表的日志，仅导出这些实例对应的攻击事件 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The instances of this AsyncJobReqBody.
        :rtype: list[str]
        """
        return self._instances

    @instances.setter
    def instances(self, instances):
        r"""Sets the instances of this AsyncJobReqBody.

        **参数解释：** 查询指定instance列表的日志，仅导出这些实例对应的攻击事件 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param instances: The instances of this AsyncJobReqBody.
        :type instances: list[str]
        """
        self._instances = instances

    @property
    def dump_columns(self):
        r"""Gets the dump_columns of this AsyncJobReqBody.

        **参数解释：** 需要导出的列名称，指定攻击事件日志中需要导出的字段（如时间、事件ID、攻击类型等） **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The dump_columns of this AsyncJobReqBody.
        :rtype: list[str]
        """
        return self._dump_columns

    @dump_columns.setter
    def dump_columns(self, dump_columns):
        r"""Sets the dump_columns of this AsyncJobReqBody.

        **参数解释：** 需要导出的列名称，指定攻击事件日志中需要导出的字段（如时间、事件ID、攻击类型等） **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param dump_columns: The dump_columns of this AsyncJobReqBody.
        :type dump_columns: list[str]
        """
        self._dump_columns = dump_columns

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
        if not isinstance(other, AsyncJobReqBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
