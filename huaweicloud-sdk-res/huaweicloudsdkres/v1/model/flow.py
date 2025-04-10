# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Flow:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'flow_id': 'str',
        'attr_pair_rules_filter': 'list[AttrPairRules]',
        'attr_pair_rules_reserve': 'list[AttrPairRules]',
        'deduplication_list': 'list[Deduplication]',
        'attribute_info': 'AttributeInfo',
        'bloom_filter_conf': 'BloomFilterConf',
        'group_attr': 'str',
        'pre_deal': 'bool',
        'rank_setting': 'str',
        'rules': 'Rule',
        'filter_sets': 'list[str]',
        'attr_value_rules_filter': 'list[AttrValueRules]',
        'attr_value_rules_reserve': 'list[AttrValueRules]',
        'ctr_job': 'str',
        'ratio': 'int',
        'toppings': 'list[str]'
    }

    attribute_map = {
        'flow_id': 'flow_id',
        'attr_pair_rules_filter': 'attr_pair_rules_filter',
        'attr_pair_rules_reserve': 'attr_pair_rules_reserve',
        'deduplication_list': 'deduplication_list',
        'attribute_info': 'attribute_info',
        'bloom_filter_conf': 'bloom_filter_conf',
        'group_attr': 'group_attr',
        'pre_deal': 'pre_deal',
        'rank_setting': 'rank_setting',
        'rules': 'rules',
        'filter_sets': 'filter_sets',
        'attr_value_rules_filter': 'attr_value_rules_filter',
        'attr_value_rules_reserve': 'attr_value_rules_reserve',
        'ctr_job': 'ctr_job',
        'ratio': 'ratio',
        'toppings': 'toppings'
    }

    def __init__(self, flow_id=None, attr_pair_rules_filter=None, attr_pair_rules_reserve=None, deduplication_list=None, attribute_info=None, bloom_filter_conf=None, group_attr=None, pre_deal=None, rank_setting=None, rules=None, filter_sets=None, attr_value_rules_filter=None, attr_value_rules_reserve=None, ctr_job=None, ratio=None, toppings=None):
        r"""Flow

        The model defined in huaweicloud sdk

        :param flow_id: 流程id。
        :type flow_id: str
        :param attr_pair_rules_filter: 属性对过滤。
        :type attr_pair_rules_filter: list[:class:`huaweicloudsdkres.v1.AttrPairRules`]
        :param attr_pair_rules_reserve: 属性对保留。
        :type attr_pair_rules_reserve: list[:class:`huaweicloudsdkres.v1.AttrPairRules`]
        :param deduplication_list: 属性去重。
        :type deduplication_list: list[:class:`huaweicloudsdkres.v1.Deduplication`]
        :param attribute_info: 
        :type attribute_info: :class:`huaweicloudsdkres.v1.AttributeInfo`
        :param bloom_filter_conf: 
        :type bloom_filter_conf: :class:`huaweicloudsdkres.v1.BloomFilterConf`
        :param group_attr: 分组打散属性。
        :type group_attr: str
        :param pre_deal: 在排序前去重。
        :type pre_deal: bool
        :param rank_setting: 排序配置信息。
        :type rank_setting: str
        :param rules: 
        :type rules: :class:`huaweicloudsdkres.v1.Rule`
        :param filter_sets: 过滤配置信息。
        :type filter_sets: list[str]
        :param attr_value_rules_filter: 属性值过滤。
        :type attr_value_rules_filter: list[:class:`huaweicloudsdkres.v1.AttrValueRules`]
        :param attr_value_rules_reserve: 属性值保留。
        :type attr_value_rules_reserve: list[:class:`huaweicloudsdkres.v1.AttrValueRules`]
        :param ctr_job: 排序作业（使用点击率预估时需要提供此参数）。
        :type ctr_job: str
        :param ratio: 流量占比。
        :type ratio: int
        :param toppings: 需要置顶的候选集列表。
        :type toppings: list[str]
        """
        
        

        self._flow_id = None
        self._attr_pair_rules_filter = None
        self._attr_pair_rules_reserve = None
        self._deduplication_list = None
        self._attribute_info = None
        self._bloom_filter_conf = None
        self._group_attr = None
        self._pre_deal = None
        self._rank_setting = None
        self._rules = None
        self._filter_sets = None
        self._attr_value_rules_filter = None
        self._attr_value_rules_reserve = None
        self._ctr_job = None
        self._ratio = None
        self._toppings = None
        self.discriminator = None

        self.flow_id = flow_id
        if attr_pair_rules_filter is not None:
            self.attr_pair_rules_filter = attr_pair_rules_filter
        if attr_pair_rules_reserve is not None:
            self.attr_pair_rules_reserve = attr_pair_rules_reserve
        if deduplication_list is not None:
            self.deduplication_list = deduplication_list
        if attribute_info is not None:
            self.attribute_info = attribute_info
        if bloom_filter_conf is not None:
            self.bloom_filter_conf = bloom_filter_conf
        if group_attr is not None:
            self.group_attr = group_attr
        if pre_deal is not None:
            self.pre_deal = pre_deal
        if rank_setting is not None:
            self.rank_setting = rank_setting
        if rules is not None:
            self.rules = rules
        if filter_sets is not None:
            self.filter_sets = filter_sets
        if attr_value_rules_filter is not None:
            self.attr_value_rules_filter = attr_value_rules_filter
        if attr_value_rules_reserve is not None:
            self.attr_value_rules_reserve = attr_value_rules_reserve
        if ctr_job is not None:
            self.ctr_job = ctr_job
        if ratio is not None:
            self.ratio = ratio
        if toppings is not None:
            self.toppings = toppings

    @property
    def flow_id(self):
        r"""Gets the flow_id of this Flow.

        流程id。

        :return: The flow_id of this Flow.
        :rtype: str
        """
        return self._flow_id

    @flow_id.setter
    def flow_id(self, flow_id):
        r"""Sets the flow_id of this Flow.

        流程id。

        :param flow_id: The flow_id of this Flow.
        :type flow_id: str
        """
        self._flow_id = flow_id

    @property
    def attr_pair_rules_filter(self):
        r"""Gets the attr_pair_rules_filter of this Flow.

        属性对过滤。

        :return: The attr_pair_rules_filter of this Flow.
        :rtype: list[:class:`huaweicloudsdkres.v1.AttrPairRules`]
        """
        return self._attr_pair_rules_filter

    @attr_pair_rules_filter.setter
    def attr_pair_rules_filter(self, attr_pair_rules_filter):
        r"""Sets the attr_pair_rules_filter of this Flow.

        属性对过滤。

        :param attr_pair_rules_filter: The attr_pair_rules_filter of this Flow.
        :type attr_pair_rules_filter: list[:class:`huaweicloudsdkres.v1.AttrPairRules`]
        """
        self._attr_pair_rules_filter = attr_pair_rules_filter

    @property
    def attr_pair_rules_reserve(self):
        r"""Gets the attr_pair_rules_reserve of this Flow.

        属性对保留。

        :return: The attr_pair_rules_reserve of this Flow.
        :rtype: list[:class:`huaweicloudsdkres.v1.AttrPairRules`]
        """
        return self._attr_pair_rules_reserve

    @attr_pair_rules_reserve.setter
    def attr_pair_rules_reserve(self, attr_pair_rules_reserve):
        r"""Sets the attr_pair_rules_reserve of this Flow.

        属性对保留。

        :param attr_pair_rules_reserve: The attr_pair_rules_reserve of this Flow.
        :type attr_pair_rules_reserve: list[:class:`huaweicloudsdkres.v1.AttrPairRules`]
        """
        self._attr_pair_rules_reserve = attr_pair_rules_reserve

    @property
    def deduplication_list(self):
        r"""Gets the deduplication_list of this Flow.

        属性去重。

        :return: The deduplication_list of this Flow.
        :rtype: list[:class:`huaweicloudsdkres.v1.Deduplication`]
        """
        return self._deduplication_list

    @deduplication_list.setter
    def deduplication_list(self, deduplication_list):
        r"""Sets the deduplication_list of this Flow.

        属性去重。

        :param deduplication_list: The deduplication_list of this Flow.
        :type deduplication_list: list[:class:`huaweicloudsdkres.v1.Deduplication`]
        """
        self._deduplication_list = deduplication_list

    @property
    def attribute_info(self):
        r"""Gets the attribute_info of this Flow.

        :return: The attribute_info of this Flow.
        :rtype: :class:`huaweicloudsdkres.v1.AttributeInfo`
        """
        return self._attribute_info

    @attribute_info.setter
    def attribute_info(self, attribute_info):
        r"""Sets the attribute_info of this Flow.

        :param attribute_info: The attribute_info of this Flow.
        :type attribute_info: :class:`huaweicloudsdkres.v1.AttributeInfo`
        """
        self._attribute_info = attribute_info

    @property
    def bloom_filter_conf(self):
        r"""Gets the bloom_filter_conf of this Flow.

        :return: The bloom_filter_conf of this Flow.
        :rtype: :class:`huaweicloudsdkres.v1.BloomFilterConf`
        """
        return self._bloom_filter_conf

    @bloom_filter_conf.setter
    def bloom_filter_conf(self, bloom_filter_conf):
        r"""Sets the bloom_filter_conf of this Flow.

        :param bloom_filter_conf: The bloom_filter_conf of this Flow.
        :type bloom_filter_conf: :class:`huaweicloudsdkres.v1.BloomFilterConf`
        """
        self._bloom_filter_conf = bloom_filter_conf

    @property
    def group_attr(self):
        r"""Gets the group_attr of this Flow.

        分组打散属性。

        :return: The group_attr of this Flow.
        :rtype: str
        """
        return self._group_attr

    @group_attr.setter
    def group_attr(self, group_attr):
        r"""Sets the group_attr of this Flow.

        分组打散属性。

        :param group_attr: The group_attr of this Flow.
        :type group_attr: str
        """
        self._group_attr = group_attr

    @property
    def pre_deal(self):
        r"""Gets the pre_deal of this Flow.

        在排序前去重。

        :return: The pre_deal of this Flow.
        :rtype: bool
        """
        return self._pre_deal

    @pre_deal.setter
    def pre_deal(self, pre_deal):
        r"""Sets the pre_deal of this Flow.

        在排序前去重。

        :param pre_deal: The pre_deal of this Flow.
        :type pre_deal: bool
        """
        self._pre_deal = pre_deal

    @property
    def rank_setting(self):
        r"""Gets the rank_setting of this Flow.

        排序配置信息。

        :return: The rank_setting of this Flow.
        :rtype: str
        """
        return self._rank_setting

    @rank_setting.setter
    def rank_setting(self, rank_setting):
        r"""Sets the rank_setting of this Flow.

        排序配置信息。

        :param rank_setting: The rank_setting of this Flow.
        :type rank_setting: str
        """
        self._rank_setting = rank_setting

    @property
    def rules(self):
        r"""Gets the rules of this Flow.

        :return: The rules of this Flow.
        :rtype: :class:`huaweicloudsdkres.v1.Rule`
        """
        return self._rules

    @rules.setter
    def rules(self, rules):
        r"""Sets the rules of this Flow.

        :param rules: The rules of this Flow.
        :type rules: :class:`huaweicloudsdkres.v1.Rule`
        """
        self._rules = rules

    @property
    def filter_sets(self):
        r"""Gets the filter_sets of this Flow.

        过滤配置信息。

        :return: The filter_sets of this Flow.
        :rtype: list[str]
        """
        return self._filter_sets

    @filter_sets.setter
    def filter_sets(self, filter_sets):
        r"""Sets the filter_sets of this Flow.

        过滤配置信息。

        :param filter_sets: The filter_sets of this Flow.
        :type filter_sets: list[str]
        """
        self._filter_sets = filter_sets

    @property
    def attr_value_rules_filter(self):
        r"""Gets the attr_value_rules_filter of this Flow.

        属性值过滤。

        :return: The attr_value_rules_filter of this Flow.
        :rtype: list[:class:`huaweicloudsdkres.v1.AttrValueRules`]
        """
        return self._attr_value_rules_filter

    @attr_value_rules_filter.setter
    def attr_value_rules_filter(self, attr_value_rules_filter):
        r"""Sets the attr_value_rules_filter of this Flow.

        属性值过滤。

        :param attr_value_rules_filter: The attr_value_rules_filter of this Flow.
        :type attr_value_rules_filter: list[:class:`huaweicloudsdkres.v1.AttrValueRules`]
        """
        self._attr_value_rules_filter = attr_value_rules_filter

    @property
    def attr_value_rules_reserve(self):
        r"""Gets the attr_value_rules_reserve of this Flow.

        属性值保留。

        :return: The attr_value_rules_reserve of this Flow.
        :rtype: list[:class:`huaweicloudsdkres.v1.AttrValueRules`]
        """
        return self._attr_value_rules_reserve

    @attr_value_rules_reserve.setter
    def attr_value_rules_reserve(self, attr_value_rules_reserve):
        r"""Sets the attr_value_rules_reserve of this Flow.

        属性值保留。

        :param attr_value_rules_reserve: The attr_value_rules_reserve of this Flow.
        :type attr_value_rules_reserve: list[:class:`huaweicloudsdkres.v1.AttrValueRules`]
        """
        self._attr_value_rules_reserve = attr_value_rules_reserve

    @property
    def ctr_job(self):
        r"""Gets the ctr_job of this Flow.

        排序作业（使用点击率预估时需要提供此参数）。

        :return: The ctr_job of this Flow.
        :rtype: str
        """
        return self._ctr_job

    @ctr_job.setter
    def ctr_job(self, ctr_job):
        r"""Sets the ctr_job of this Flow.

        排序作业（使用点击率预估时需要提供此参数）。

        :param ctr_job: The ctr_job of this Flow.
        :type ctr_job: str
        """
        self._ctr_job = ctr_job

    @property
    def ratio(self):
        r"""Gets the ratio of this Flow.

        流量占比。

        :return: The ratio of this Flow.
        :rtype: int
        """
        return self._ratio

    @ratio.setter
    def ratio(self, ratio):
        r"""Sets the ratio of this Flow.

        流量占比。

        :param ratio: The ratio of this Flow.
        :type ratio: int
        """
        self._ratio = ratio

    @property
    def toppings(self):
        r"""Gets the toppings of this Flow.

        需要置顶的候选集列表。

        :return: The toppings of this Flow.
        :rtype: list[str]
        """
        return self._toppings

    @toppings.setter
    def toppings(self, toppings):
        r"""Sets the toppings of this Flow.

        需要置顶的候选集列表。

        :param toppings: The toppings of this Flow.
        :type toppings: list[str]
        """
        self._toppings = toppings

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
        if not isinstance(other, Flow):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
