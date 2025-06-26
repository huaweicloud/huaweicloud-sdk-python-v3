# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SimulationEvaluationMetricSrlz:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'status': 'str',
        'display_name': 'str',
        'importance': 'str',
        'source': 'str',
        'module': 'str',
        'performance': 'str'
    }

    attribute_map = {
        'type': 'type',
        'status': 'status',
        'display_name': 'displayName',
        'importance': 'importance',
        'source': 'source',
        'module': 'module',
        'performance': 'performance'
    }

    def __init__(self, type=None, status=None, display_name=None, importance=None, source=None, module=None, performance=None):
        r"""SimulationEvaluationMetricSrlz

        The model defined in huaweicloud sdk

        :param type: 评测指标类型
        :type type: str
        :param status: 评测结果状态
        :type status: str
        :param display_name: 评测指标名称
        :type display_name: str
        :param importance: 评测指标重要度
        :type importance: str
        :param source: 评测指标来源
        :type source: str
        :param module: 评测算法模块
        :type module: str
        :param performance: 评测性能类别
        :type performance: str
        """
        
        

        self._type = None
        self._status = None
        self._display_name = None
        self._importance = None
        self._source = None
        self._module = None
        self._performance = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if status is not None:
            self.status = status
        if display_name is not None:
            self.display_name = display_name
        if importance is not None:
            self.importance = importance
        if source is not None:
            self.source = source
        if module is not None:
            self.module = module
        if performance is not None:
            self.performance = performance

    @property
    def type(self):
        r"""Gets the type of this SimulationEvaluationMetricSrlz.

        评测指标类型

        :return: The type of this SimulationEvaluationMetricSrlz.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this SimulationEvaluationMetricSrlz.

        评测指标类型

        :param type: The type of this SimulationEvaluationMetricSrlz.
        :type type: str
        """
        self._type = type

    @property
    def status(self):
        r"""Gets the status of this SimulationEvaluationMetricSrlz.

        评测结果状态

        :return: The status of this SimulationEvaluationMetricSrlz.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this SimulationEvaluationMetricSrlz.

        评测结果状态

        :param status: The status of this SimulationEvaluationMetricSrlz.
        :type status: str
        """
        self._status = status

    @property
    def display_name(self):
        r"""Gets the display_name of this SimulationEvaluationMetricSrlz.

        评测指标名称

        :return: The display_name of this SimulationEvaluationMetricSrlz.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        r"""Sets the display_name of this SimulationEvaluationMetricSrlz.

        评测指标名称

        :param display_name: The display_name of this SimulationEvaluationMetricSrlz.
        :type display_name: str
        """
        self._display_name = display_name

    @property
    def importance(self):
        r"""Gets the importance of this SimulationEvaluationMetricSrlz.

        评测指标重要度

        :return: The importance of this SimulationEvaluationMetricSrlz.
        :rtype: str
        """
        return self._importance

    @importance.setter
    def importance(self, importance):
        r"""Sets the importance of this SimulationEvaluationMetricSrlz.

        评测指标重要度

        :param importance: The importance of this SimulationEvaluationMetricSrlz.
        :type importance: str
        """
        self._importance = importance

    @property
    def source(self):
        r"""Gets the source of this SimulationEvaluationMetricSrlz.

        评测指标来源

        :return: The source of this SimulationEvaluationMetricSrlz.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        r"""Sets the source of this SimulationEvaluationMetricSrlz.

        评测指标来源

        :param source: The source of this SimulationEvaluationMetricSrlz.
        :type source: str
        """
        self._source = source

    @property
    def module(self):
        r"""Gets the module of this SimulationEvaluationMetricSrlz.

        评测算法模块

        :return: The module of this SimulationEvaluationMetricSrlz.
        :rtype: str
        """
        return self._module

    @module.setter
    def module(self, module):
        r"""Sets the module of this SimulationEvaluationMetricSrlz.

        评测算法模块

        :param module: The module of this SimulationEvaluationMetricSrlz.
        :type module: str
        """
        self._module = module

    @property
    def performance(self):
        r"""Gets the performance of this SimulationEvaluationMetricSrlz.

        评测性能类别

        :return: The performance of this SimulationEvaluationMetricSrlz.
        :rtype: str
        """
        return self._performance

    @performance.setter
    def performance(self, performance):
        r"""Sets the performance of this SimulationEvaluationMetricSrlz.

        评测性能类别

        :param performance: The performance of this SimulationEvaluationMetricSrlz.
        :type performance: str
        """
        self._performance = performance

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
        if not isinstance(other, SimulationEvaluationMetricSrlz):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
