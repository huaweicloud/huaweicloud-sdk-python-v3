# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WidgetMetricResp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'namespace': 'str',
        'dimensions': 'DimensionInfoResp',
        'metric_name': 'str',
        'alias': 'list[str]',
        'extra_info': 'ExtraInfoResp',
        'rollup_enable': 'bool',
        'rollup_filter': 'RollupFilterResp',
        'rollup_dimension': 'str',
        'last_week_compare_enable': 'bool',
        'yesterday_compare_enable': 'bool',
        'metric_dimension': 'str',
        'top_num': 'int',
        'unit': 'str',
        'order': 'str',
        'topn_metric_name': 'str'
    }

    attribute_map = {
        'namespace': 'namespace',
        'dimensions': 'dimensions',
        'metric_name': 'metric_name',
        'alias': 'alias',
        'extra_info': 'extra_info',
        'rollup_enable': 'rollup_enable',
        'rollup_filter': 'rollup_filter',
        'rollup_dimension': 'rollup_dimension',
        'last_week_compare_enable': 'last_week_compare_enable',
        'yesterday_compare_enable': 'yesterday_compare_enable',
        'metric_dimension': 'metric_dimension',
        'top_num': 'top_num',
        'unit': 'unit',
        'order': 'order',
        'topn_metric_name': 'topn_metric_name'
    }

    def __init__(self, namespace=None, dimensions=None, metric_name=None, alias=None, extra_info=None, rollup_enable=None, rollup_filter=None, rollup_dimension=None, last_week_compare_enable=None, yesterday_compare_enable=None, metric_dimension=None, top_num=None, unit=None, order=None, topn_metric_name=None):
        r"""WidgetMetricResp

        The model defined in huaweicloud sdk

        :param namespace: **参数解释** 查询服务的命名空间，各服务命名空间请参考“[服务命名空间](ces_03_0059.xml)” **取值范围** 格式为service.item；service和item必须是字符串，必须以字母开头，只能包含0-9/a-z/A-Z/_。字符串的长度必须在 3 到 32个字符之间。 
        :type namespace: str
        :param dimensions: 
        :type dimensions: :class:`huaweicloudsdkces.v2.DimensionInfoResp`
        :param metric_name: **参数解释** 多个指标名称 **取值范围** 长度为[1,1080]个字符，多个指标名称之间用逗号隔开 
        :type metric_name: str
        :param alias: **参数解释** 监控视图的指标别名列表 
        :type alias: list[str]
        :param extra_info: 
        :type extra_info: :class:`huaweicloudsdkces.v2.ExtraInfoResp`
        :param rollup_enable: **参数解释** 是否开启聚合 **取值范围** - true：表示开启聚合 - false：表示不开启聚合 
        :type rollup_enable: bool
        :param rollup_filter: 
        :type rollup_filter: :class:`huaweicloudsdkces.v2.RollupFilterResp`
        :param rollup_dimension: **参数解释** 聚合维度 **取值范围** 长度为[1,32]个字符 
        :type rollup_dimension: str
        :param last_week_compare_enable: **参数解释** 是否展示同比（上周同一时间）数据 **取值范围** - true:展示 - false:不展示 
        :type last_week_compare_enable: bool
        :param yesterday_compare_enable: **参数解释** 是否展示环比（昨天同一时间）数据 **取值范围** - true:展示 - false:不展示 
        :type yesterday_compare_enable: bool
        :param metric_dimension: **参数解释** 维度名称，多维度用逗号分隔，各服务支持的维度可参考：“[服务维度名称](ces_03_0059.xml)”          **取值范围** 必须以字母开头，只能包含0-9/a-z/A-Z/_/-，多维度用\&quot;,\&quot;分隔，每个维度的最大长度为32。总长度为[1,131]个字符。目前最大支持4个维度。举例：单维度场景：instance_id；多维度场景：instance_id,disk 
        :type metric_dimension: str
        :param top_num: **参数解释** 展示数据数量               **取值范围** 最小值为1，最大值为200 
        :type top_num: int
        :param unit: **参数解释** 单位 **取值范围** 长度为[0,32]个字符 
        :type unit: str
        :param order: **参数解释** 排序字段               **取值范围** - asc:正序 - desc:倒序 
        :type order: str
        :param topn_metric_name: **参数解释** 资源的监控指标名称，必须以字母开头，只能包含0-9/a-z/A-Z/_，字符长度最短为1，最大为64；如：弹性云服务器中的监控指标cpu_util，表示弹性服务器的CPU使用率；文档数据库中的指标mongo001_command_ps，表示command执行频率；各服务的指标名称可查看：“[服务指标名称](ces_03_0059.xml)”。 **取值范围** 长度为[1,96]个字符 
        :type topn_metric_name: str
        """
        
        

        self._namespace = None
        self._dimensions = None
        self._metric_name = None
        self._alias = None
        self._extra_info = None
        self._rollup_enable = None
        self._rollup_filter = None
        self._rollup_dimension = None
        self._last_week_compare_enable = None
        self._yesterday_compare_enable = None
        self._metric_dimension = None
        self._top_num = None
        self._unit = None
        self._order = None
        self._topn_metric_name = None
        self.discriminator = None

        if namespace is not None:
            self.namespace = namespace
        if dimensions is not None:
            self.dimensions = dimensions
        if metric_name is not None:
            self.metric_name = metric_name
        if alias is not None:
            self.alias = alias
        if extra_info is not None:
            self.extra_info = extra_info
        if rollup_enable is not None:
            self.rollup_enable = rollup_enable
        if rollup_filter is not None:
            self.rollup_filter = rollup_filter
        if rollup_dimension is not None:
            self.rollup_dimension = rollup_dimension
        if last_week_compare_enable is not None:
            self.last_week_compare_enable = last_week_compare_enable
        if yesterday_compare_enable is not None:
            self.yesterday_compare_enable = yesterday_compare_enable
        if metric_dimension is not None:
            self.metric_dimension = metric_dimension
        if top_num is not None:
            self.top_num = top_num
        if unit is not None:
            self.unit = unit
        if order is not None:
            self.order = order
        if topn_metric_name is not None:
            self.topn_metric_name = topn_metric_name

    @property
    def namespace(self):
        r"""Gets the namespace of this WidgetMetricResp.

        **参数解释** 查询服务的命名空间，各服务命名空间请参考“[服务命名空间](ces_03_0059.xml)” **取值范围** 格式为service.item；service和item必须是字符串，必须以字母开头，只能包含0-9/a-z/A-Z/_。字符串的长度必须在 3 到 32个字符之间。 

        :return: The namespace of this WidgetMetricResp.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        r"""Sets the namespace of this WidgetMetricResp.

        **参数解释** 查询服务的命名空间，各服务命名空间请参考“[服务命名空间](ces_03_0059.xml)” **取值范围** 格式为service.item；service和item必须是字符串，必须以字母开头，只能包含0-9/a-z/A-Z/_。字符串的长度必须在 3 到 32个字符之间。 

        :param namespace: The namespace of this WidgetMetricResp.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def dimensions(self):
        r"""Gets the dimensions of this WidgetMetricResp.

        :return: The dimensions of this WidgetMetricResp.
        :rtype: :class:`huaweicloudsdkces.v2.DimensionInfoResp`
        """
        return self._dimensions

    @dimensions.setter
    def dimensions(self, dimensions):
        r"""Sets the dimensions of this WidgetMetricResp.

        :param dimensions: The dimensions of this WidgetMetricResp.
        :type dimensions: :class:`huaweicloudsdkces.v2.DimensionInfoResp`
        """
        self._dimensions = dimensions

    @property
    def metric_name(self):
        r"""Gets the metric_name of this WidgetMetricResp.

        **参数解释** 多个指标名称 **取值范围** 长度为[1,1080]个字符，多个指标名称之间用逗号隔开 

        :return: The metric_name of this WidgetMetricResp.
        :rtype: str
        """
        return self._metric_name

    @metric_name.setter
    def metric_name(self, metric_name):
        r"""Sets the metric_name of this WidgetMetricResp.

        **参数解释** 多个指标名称 **取值范围** 长度为[1,1080]个字符，多个指标名称之间用逗号隔开 

        :param metric_name: The metric_name of this WidgetMetricResp.
        :type metric_name: str
        """
        self._metric_name = metric_name

    @property
    def alias(self):
        r"""Gets the alias of this WidgetMetricResp.

        **参数解释** 监控视图的指标别名列表 

        :return: The alias of this WidgetMetricResp.
        :rtype: list[str]
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        r"""Sets the alias of this WidgetMetricResp.

        **参数解释** 监控视图的指标别名列表 

        :param alias: The alias of this WidgetMetricResp.
        :type alias: list[str]
        """
        self._alias = alias

    @property
    def extra_info(self):
        r"""Gets the extra_info of this WidgetMetricResp.

        :return: The extra_info of this WidgetMetricResp.
        :rtype: :class:`huaweicloudsdkces.v2.ExtraInfoResp`
        """
        return self._extra_info

    @extra_info.setter
    def extra_info(self, extra_info):
        r"""Sets the extra_info of this WidgetMetricResp.

        :param extra_info: The extra_info of this WidgetMetricResp.
        :type extra_info: :class:`huaweicloudsdkces.v2.ExtraInfoResp`
        """
        self._extra_info = extra_info

    @property
    def rollup_enable(self):
        r"""Gets the rollup_enable of this WidgetMetricResp.

        **参数解释** 是否开启聚合 **取值范围** - true：表示开启聚合 - false：表示不开启聚合 

        :return: The rollup_enable of this WidgetMetricResp.
        :rtype: bool
        """
        return self._rollup_enable

    @rollup_enable.setter
    def rollup_enable(self, rollup_enable):
        r"""Sets the rollup_enable of this WidgetMetricResp.

        **参数解释** 是否开启聚合 **取值范围** - true：表示开启聚合 - false：表示不开启聚合 

        :param rollup_enable: The rollup_enable of this WidgetMetricResp.
        :type rollup_enable: bool
        """
        self._rollup_enable = rollup_enable

    @property
    def rollup_filter(self):
        r"""Gets the rollup_filter of this WidgetMetricResp.

        :return: The rollup_filter of this WidgetMetricResp.
        :rtype: :class:`huaweicloudsdkces.v2.RollupFilterResp`
        """
        return self._rollup_filter

    @rollup_filter.setter
    def rollup_filter(self, rollup_filter):
        r"""Sets the rollup_filter of this WidgetMetricResp.

        :param rollup_filter: The rollup_filter of this WidgetMetricResp.
        :type rollup_filter: :class:`huaweicloudsdkces.v2.RollupFilterResp`
        """
        self._rollup_filter = rollup_filter

    @property
    def rollup_dimension(self):
        r"""Gets the rollup_dimension of this WidgetMetricResp.

        **参数解释** 聚合维度 **取值范围** 长度为[1,32]个字符 

        :return: The rollup_dimension of this WidgetMetricResp.
        :rtype: str
        """
        return self._rollup_dimension

    @rollup_dimension.setter
    def rollup_dimension(self, rollup_dimension):
        r"""Sets the rollup_dimension of this WidgetMetricResp.

        **参数解释** 聚合维度 **取值范围** 长度为[1,32]个字符 

        :param rollup_dimension: The rollup_dimension of this WidgetMetricResp.
        :type rollup_dimension: str
        """
        self._rollup_dimension = rollup_dimension

    @property
    def last_week_compare_enable(self):
        r"""Gets the last_week_compare_enable of this WidgetMetricResp.

        **参数解释** 是否展示同比（上周同一时间）数据 **取值范围** - true:展示 - false:不展示 

        :return: The last_week_compare_enable of this WidgetMetricResp.
        :rtype: bool
        """
        return self._last_week_compare_enable

    @last_week_compare_enable.setter
    def last_week_compare_enable(self, last_week_compare_enable):
        r"""Sets the last_week_compare_enable of this WidgetMetricResp.

        **参数解释** 是否展示同比（上周同一时间）数据 **取值范围** - true:展示 - false:不展示 

        :param last_week_compare_enable: The last_week_compare_enable of this WidgetMetricResp.
        :type last_week_compare_enable: bool
        """
        self._last_week_compare_enable = last_week_compare_enable

    @property
    def yesterday_compare_enable(self):
        r"""Gets the yesterday_compare_enable of this WidgetMetricResp.

        **参数解释** 是否展示环比（昨天同一时间）数据 **取值范围** - true:展示 - false:不展示 

        :return: The yesterday_compare_enable of this WidgetMetricResp.
        :rtype: bool
        """
        return self._yesterday_compare_enable

    @yesterday_compare_enable.setter
    def yesterday_compare_enable(self, yesterday_compare_enable):
        r"""Sets the yesterday_compare_enable of this WidgetMetricResp.

        **参数解释** 是否展示环比（昨天同一时间）数据 **取值范围** - true:展示 - false:不展示 

        :param yesterday_compare_enable: The yesterday_compare_enable of this WidgetMetricResp.
        :type yesterday_compare_enable: bool
        """
        self._yesterday_compare_enable = yesterday_compare_enable

    @property
    def metric_dimension(self):
        r"""Gets the metric_dimension of this WidgetMetricResp.

        **参数解释** 维度名称，多维度用逗号分隔，各服务支持的维度可参考：“[服务维度名称](ces_03_0059.xml)”          **取值范围** 必须以字母开头，只能包含0-9/a-z/A-Z/_/-，多维度用\",\"分隔，每个维度的最大长度为32。总长度为[1,131]个字符。目前最大支持4个维度。举例：单维度场景：instance_id；多维度场景：instance_id,disk 

        :return: The metric_dimension of this WidgetMetricResp.
        :rtype: str
        """
        return self._metric_dimension

    @metric_dimension.setter
    def metric_dimension(self, metric_dimension):
        r"""Sets the metric_dimension of this WidgetMetricResp.

        **参数解释** 维度名称，多维度用逗号分隔，各服务支持的维度可参考：“[服务维度名称](ces_03_0059.xml)”          **取值范围** 必须以字母开头，只能包含0-9/a-z/A-Z/_/-，多维度用\",\"分隔，每个维度的最大长度为32。总长度为[1,131]个字符。目前最大支持4个维度。举例：单维度场景：instance_id；多维度场景：instance_id,disk 

        :param metric_dimension: The metric_dimension of this WidgetMetricResp.
        :type metric_dimension: str
        """
        self._metric_dimension = metric_dimension

    @property
    def top_num(self):
        r"""Gets the top_num of this WidgetMetricResp.

        **参数解释** 展示数据数量               **取值范围** 最小值为1，最大值为200 

        :return: The top_num of this WidgetMetricResp.
        :rtype: int
        """
        return self._top_num

    @top_num.setter
    def top_num(self, top_num):
        r"""Sets the top_num of this WidgetMetricResp.

        **参数解释** 展示数据数量               **取值范围** 最小值为1，最大值为200 

        :param top_num: The top_num of this WidgetMetricResp.
        :type top_num: int
        """
        self._top_num = top_num

    @property
    def unit(self):
        r"""Gets the unit of this WidgetMetricResp.

        **参数解释** 单位 **取值范围** 长度为[0,32]个字符 

        :return: The unit of this WidgetMetricResp.
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        r"""Sets the unit of this WidgetMetricResp.

        **参数解释** 单位 **取值范围** 长度为[0,32]个字符 

        :param unit: The unit of this WidgetMetricResp.
        :type unit: str
        """
        self._unit = unit

    @property
    def order(self):
        r"""Gets the order of this WidgetMetricResp.

        **参数解释** 排序字段               **取值范围** - asc:正序 - desc:倒序 

        :return: The order of this WidgetMetricResp.
        :rtype: str
        """
        return self._order

    @order.setter
    def order(self, order):
        r"""Sets the order of this WidgetMetricResp.

        **参数解释** 排序字段               **取值范围** - asc:正序 - desc:倒序 

        :param order: The order of this WidgetMetricResp.
        :type order: str
        """
        self._order = order

    @property
    def topn_metric_name(self):
        r"""Gets the topn_metric_name of this WidgetMetricResp.

        **参数解释** 资源的监控指标名称，必须以字母开头，只能包含0-9/a-z/A-Z/_，字符长度最短为1，最大为64；如：弹性云服务器中的监控指标cpu_util，表示弹性服务器的CPU使用率；文档数据库中的指标mongo001_command_ps，表示command执行频率；各服务的指标名称可查看：“[服务指标名称](ces_03_0059.xml)”。 **取值范围** 长度为[1,96]个字符 

        :return: The topn_metric_name of this WidgetMetricResp.
        :rtype: str
        """
        return self._topn_metric_name

    @topn_metric_name.setter
    def topn_metric_name(self, topn_metric_name):
        r"""Sets the topn_metric_name of this WidgetMetricResp.

        **参数解释** 资源的监控指标名称，必须以字母开头，只能包含0-9/a-z/A-Z/_，字符长度最短为1，最大为64；如：弹性云服务器中的监控指标cpu_util，表示弹性服务器的CPU使用率；文档数据库中的指标mongo001_command_ps，表示command执行频率；各服务的指标名称可查看：“[服务指标名称](ces_03_0059.xml)”。 **取值范围** 长度为[1,96]个字符 

        :param topn_metric_name: The topn_metric_name of this WidgetMetricResp.
        :type topn_metric_name: str
        """
        self._topn_metric_name = topn_metric_name

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
        if not isinstance(other, WidgetMetricResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
