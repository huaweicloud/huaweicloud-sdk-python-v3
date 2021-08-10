# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QuerySeriesOptionParam:


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
        'dimensions': 'list[Dimension]'
    }

    attribute_map = {
        'namespace': 'namespace',
        'metric_name': 'metric_name',
        'dimensions': 'dimensions'
    }

    def __init__(self, namespace=None, metric_name=None, dimensions=None):
        """QuerySeriesOptionParam - a model defined in huaweicloud sdk"""
        
        

        self._namespace = None
        self._metric_name = None
        self._dimensions = None
        self.discriminator = None

        self.namespace = namespace
        if metric_name is not None:
            self.metric_name = metric_name
        if dimensions is not None:
            self.dimensions = dimensions

    @property
    def namespace(self):
        """Gets the namespace of this QuerySeriesOptionParam.

        取值范围 PAAS.CONTAINER、PAAS.NODE、PAAS.SLA、PAAS.AGGR、CUSTOMMETRICS等 时间序列命名空间。 PAAS.CONTAINER：应用时间序列； PAAS.NODE：节时间序列； PAAS.SLA：SLA时间序列； PAAS.AGGR：集群时间序列； CUSTOMMETRICS：自定义时间序列 

        :return: The namespace of this QuerySeriesOptionParam.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this QuerySeriesOptionParam.

        取值范围 PAAS.CONTAINER、PAAS.NODE、PAAS.SLA、PAAS.AGGR、CUSTOMMETRICS等 时间序列命名空间。 PAAS.CONTAINER：应用时间序列； PAAS.NODE：节时间序列； PAAS.SLA：SLA时间序列； PAAS.AGGR：集群时间序列； CUSTOMMETRICS：自定义时间序列 

        :param namespace: The namespace of this QuerySeriesOptionParam.
        :type: str
        """
        self._namespace = namespace

    @property
    def metric_name(self):
        """Gets the metric_name of this QuerySeriesOptionParam.

         | 取值范围 名称长度为1~255个字符 时间序列名称。

        :return: The metric_name of this QuerySeriesOptionParam.
        :rtype: str
        """
        return self._metric_name

    @metric_name.setter
    def metric_name(self, metric_name):
        """Sets the metric_name of this QuerySeriesOptionParam.

         | 取值范围 名称长度为1~255个字符 时间序列名称。

        :param metric_name: The metric_name of this QuerySeriesOptionParam.
        :type: str
        """
        self._metric_name = metric_name

    @property
    def dimensions(self):
        """Gets the dimensions of this QuerySeriesOptionParam.

        时间序列维度列表。

        :return: The dimensions of this QuerySeriesOptionParam.
        :rtype: list[Dimension]
        """
        return self._dimensions

    @dimensions.setter
    def dimensions(self, dimensions):
        """Sets the dimensions of this QuerySeriesOptionParam.

        时间序列维度列表。

        :param dimensions: The dimensions of this QuerySeriesOptionParam.
        :type: list[Dimension]
        """
        self._dimensions = dimensions

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
        if not isinstance(other, QuerySeriesOptionParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
