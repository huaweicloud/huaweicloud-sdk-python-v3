# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchListSpecifiedMetricDataRequestBody:

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
        'metric_name': 'str',
        'metric_dimension': 'str',
        '_from': 'int',
        'to': 'int',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'namespace': 'namespace',
        'metric_name': 'metric_name',
        'metric_dimension': 'metric_dimension',
        '_from': 'from',
        'to': 'to',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, namespace=None, metric_name=None, metric_dimension=None, _from=None, to=None, limit=None, offset=None):
        r"""BatchListSpecifiedMetricDataRequestBody

        The model defined in huaweicloud sdk

        :param namespace: **参数解释**： 查询服务的命名空间，各服务命名空间请参考“[服务命名空间](ces_03_0059.xml)”。 **约束限制**： 不涉及。 **取值范围**： 格式为service.item；service和item必须是字符串，必须以字母开头，只能包含0-9/a-z/A-Z/_。字符串的长度必须在 3 到 32个字符之间。 **默认取值**： 不涉及。 
        :type namespace: str
        :param metric_name: **参数解释**： 资源的监控指标名称，各服务的指标名称可查看：“[服务指标名称](ces_03_0059.xml)”。 **约束限制**： 不涉及。 **取值范围**： 必须以字母开头，只能包含0-9/a-z/A-Z/_/-。字符长度最短为1，最大为64。如：弹性云服务器中的监控指标cpu_util，表示弹性服务器的CPU使用率；文档数据库中的指标mongo001_command_ps，表示command执行频率。         **默认取值**： 不涉及。 
        :type metric_name: str
        :param metric_dimension: **参数解释**: 指标维度, 多维度逗号分隔。 **约束限制**: 不涉及。 **取值范围**: 必须以字母开头，只能包含0-9/a-z/A-Z/_/-/,。每个维度必须以字母开头，每个维度长度最短1，最长32，多个维度直接用,分隔。 **默认取值**: 不涉及。 
        :type metric_dimension: str
        :param _from: **参数解释**: 查询监控数据的开始时间，格式为时间戳, 单位毫秒。 **约束限制**: from必须小于to, to和from的时间间隔必须在5分钟内。 **取值范围**: 最小值为0。 **默认取值**: 不涉及。 
        :type _from: int
        :param to: **参数解释**: 查询监控数据的结束时间，格式为时间戳, 单位毫秒。 **约束限制**: from必须小于to, to和from的时间间隔必须在5分钟内。 **取值范围**: 最小值为0。 **默认取值**: 不涉及。 
        :type to: int
        :param limit: **参数解释**: 分页大小。 **约束限制**: 不涉及。 **取值范围**: 最小值为1，最大值为1000。 **默认取值**: 100。 
        :type limit: int
        :param offset: **参数解释**: 分页偏移量。 **约束限制**: 不涉及。 **取值范围**: 最小值为0，最大值为9999999。 **默认取值**: 0。 
        :type offset: int
        """
        
        

        self._namespace = None
        self._metric_name = None
        self._metric_dimension = None
        self.__from = None
        self._to = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        self.namespace = namespace
        self.metric_name = metric_name
        self.metric_dimension = metric_dimension
        if _from is not None:
            self._from = _from
        if to is not None:
            self.to = to
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def namespace(self):
        r"""Gets the namespace of this BatchListSpecifiedMetricDataRequestBody.

        **参数解释**： 查询服务的命名空间，各服务命名空间请参考“[服务命名空间](ces_03_0059.xml)”。 **约束限制**： 不涉及。 **取值范围**： 格式为service.item；service和item必须是字符串，必须以字母开头，只能包含0-9/a-z/A-Z/_。字符串的长度必须在 3 到 32个字符之间。 **默认取值**： 不涉及。 

        :return: The namespace of this BatchListSpecifiedMetricDataRequestBody.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        r"""Sets the namespace of this BatchListSpecifiedMetricDataRequestBody.

        **参数解释**： 查询服务的命名空间，各服务命名空间请参考“[服务命名空间](ces_03_0059.xml)”。 **约束限制**： 不涉及。 **取值范围**： 格式为service.item；service和item必须是字符串，必须以字母开头，只能包含0-9/a-z/A-Z/_。字符串的长度必须在 3 到 32个字符之间。 **默认取值**： 不涉及。 

        :param namespace: The namespace of this BatchListSpecifiedMetricDataRequestBody.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def metric_name(self):
        r"""Gets the metric_name of this BatchListSpecifiedMetricDataRequestBody.

        **参数解释**： 资源的监控指标名称，各服务的指标名称可查看：“[服务指标名称](ces_03_0059.xml)”。 **约束限制**： 不涉及。 **取值范围**： 必须以字母开头，只能包含0-9/a-z/A-Z/_/-。字符长度最短为1，最大为64。如：弹性云服务器中的监控指标cpu_util，表示弹性服务器的CPU使用率；文档数据库中的指标mongo001_command_ps，表示command执行频率。         **默认取值**： 不涉及。 

        :return: The metric_name of this BatchListSpecifiedMetricDataRequestBody.
        :rtype: str
        """
        return self._metric_name

    @metric_name.setter
    def metric_name(self, metric_name):
        r"""Sets the metric_name of this BatchListSpecifiedMetricDataRequestBody.

        **参数解释**： 资源的监控指标名称，各服务的指标名称可查看：“[服务指标名称](ces_03_0059.xml)”。 **约束限制**： 不涉及。 **取值范围**： 必须以字母开头，只能包含0-9/a-z/A-Z/_/-。字符长度最短为1，最大为64。如：弹性云服务器中的监控指标cpu_util，表示弹性服务器的CPU使用率；文档数据库中的指标mongo001_command_ps，表示command执行频率。         **默认取值**： 不涉及。 

        :param metric_name: The metric_name of this BatchListSpecifiedMetricDataRequestBody.
        :type metric_name: str
        """
        self._metric_name = metric_name

    @property
    def metric_dimension(self):
        r"""Gets the metric_dimension of this BatchListSpecifiedMetricDataRequestBody.

        **参数解释**: 指标维度, 多维度逗号分隔。 **约束限制**: 不涉及。 **取值范围**: 必须以字母开头，只能包含0-9/a-z/A-Z/_/-/,。每个维度必须以字母开头，每个维度长度最短1，最长32，多个维度直接用,分隔。 **默认取值**: 不涉及。 

        :return: The metric_dimension of this BatchListSpecifiedMetricDataRequestBody.
        :rtype: str
        """
        return self._metric_dimension

    @metric_dimension.setter
    def metric_dimension(self, metric_dimension):
        r"""Sets the metric_dimension of this BatchListSpecifiedMetricDataRequestBody.

        **参数解释**: 指标维度, 多维度逗号分隔。 **约束限制**: 不涉及。 **取值范围**: 必须以字母开头，只能包含0-9/a-z/A-Z/_/-/,。每个维度必须以字母开头，每个维度长度最短1，最长32，多个维度直接用,分隔。 **默认取值**: 不涉及。 

        :param metric_dimension: The metric_dimension of this BatchListSpecifiedMetricDataRequestBody.
        :type metric_dimension: str
        """
        self._metric_dimension = metric_dimension

    @property
    def _from(self):
        r"""Gets the _from of this BatchListSpecifiedMetricDataRequestBody.

        **参数解释**: 查询监控数据的开始时间，格式为时间戳, 单位毫秒。 **约束限制**: from必须小于to, to和from的时间间隔必须在5分钟内。 **取值范围**: 最小值为0。 **默认取值**: 不涉及。 

        :return: The _from of this BatchListSpecifiedMetricDataRequestBody.
        :rtype: int
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        r"""Sets the _from of this BatchListSpecifiedMetricDataRequestBody.

        **参数解释**: 查询监控数据的开始时间，格式为时间戳, 单位毫秒。 **约束限制**: from必须小于to, to和from的时间间隔必须在5分钟内。 **取值范围**: 最小值为0。 **默认取值**: 不涉及。 

        :param _from: The _from of this BatchListSpecifiedMetricDataRequestBody.
        :type _from: int
        """
        self.__from = _from

    @property
    def to(self):
        r"""Gets the to of this BatchListSpecifiedMetricDataRequestBody.

        **参数解释**: 查询监控数据的结束时间，格式为时间戳, 单位毫秒。 **约束限制**: from必须小于to, to和from的时间间隔必须在5分钟内。 **取值范围**: 最小值为0。 **默认取值**: 不涉及。 

        :return: The to of this BatchListSpecifiedMetricDataRequestBody.
        :rtype: int
        """
        return self._to

    @to.setter
    def to(self, to):
        r"""Sets the to of this BatchListSpecifiedMetricDataRequestBody.

        **参数解释**: 查询监控数据的结束时间，格式为时间戳, 单位毫秒。 **约束限制**: from必须小于to, to和from的时间间隔必须在5分钟内。 **取值范围**: 最小值为0。 **默认取值**: 不涉及。 

        :param to: The to of this BatchListSpecifiedMetricDataRequestBody.
        :type to: int
        """
        self._to = to

    @property
    def limit(self):
        r"""Gets the limit of this BatchListSpecifiedMetricDataRequestBody.

        **参数解释**: 分页大小。 **约束限制**: 不涉及。 **取值范围**: 最小值为1，最大值为1000。 **默认取值**: 100。 

        :return: The limit of this BatchListSpecifiedMetricDataRequestBody.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this BatchListSpecifiedMetricDataRequestBody.

        **参数解释**: 分页大小。 **约束限制**: 不涉及。 **取值范围**: 最小值为1，最大值为1000。 **默认取值**: 100。 

        :param limit: The limit of this BatchListSpecifiedMetricDataRequestBody.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this BatchListSpecifiedMetricDataRequestBody.

        **参数解释**: 分页偏移量。 **约束限制**: 不涉及。 **取值范围**: 最小值为0，最大值为9999999。 **默认取值**: 0。 

        :return: The offset of this BatchListSpecifiedMetricDataRequestBody.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this BatchListSpecifiedMetricDataRequestBody.

        **参数解释**: 分页偏移量。 **约束限制**: 不涉及。 **取值范围**: 最小值为0，最大值为9999999。 **默认取值**: 0。 

        :param offset: The offset of this BatchListSpecifiedMetricDataRequestBody.
        :type offset: int
        """
        self._offset = offset

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
        if not isinstance(other, BatchListSpecifiedMetricDataRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
