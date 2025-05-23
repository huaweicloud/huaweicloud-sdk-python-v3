# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GetMetricsValue:

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
        'transform': 'TransformMetricsRequest',
        'aggregate': 'AggregateMetricsRequest'
    }

    attribute_map = {
        'type': 'type',
        'transform': 'transform',
        'aggregate': 'aggregate'
    }

    def __init__(self, type=None, transform=None, aggregate=None):
        r"""GetMetricsValue

        The model defined in huaweicloud sdk

        :param type: 查询类型，经过转换计算的序列值（transform）、经过聚合计算的序列值（aggregate）
        :type type: str
        :param transform: 
        :type transform: :class:`huaweicloudsdkiotanalytics.v1.TransformMetricsRequest`
        :param aggregate: 
        :type aggregate: :class:`huaweicloudsdkiotanalytics.v1.AggregateMetricsRequest`
        """
        
        

        self._type = None
        self._transform = None
        self._aggregate = None
        self.discriminator = None

        self.type = type
        if transform is not None:
            self.transform = transform
        if aggregate is not None:
            self.aggregate = aggregate

    @property
    def type(self):
        r"""Gets the type of this GetMetricsValue.

        查询类型，经过转换计算的序列值（transform）、经过聚合计算的序列值（aggregate）

        :return: The type of this GetMetricsValue.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this GetMetricsValue.

        查询类型，经过转换计算的序列值（transform）、经过聚合计算的序列值（aggregate）

        :param type: The type of this GetMetricsValue.
        :type type: str
        """
        self._type = type

    @property
    def transform(self):
        r"""Gets the transform of this GetMetricsValue.

        :return: The transform of this GetMetricsValue.
        :rtype: :class:`huaweicloudsdkiotanalytics.v1.TransformMetricsRequest`
        """
        return self._transform

    @transform.setter
    def transform(self, transform):
        r"""Sets the transform of this GetMetricsValue.

        :param transform: The transform of this GetMetricsValue.
        :type transform: :class:`huaweicloudsdkiotanalytics.v1.TransformMetricsRequest`
        """
        self._transform = transform

    @property
    def aggregate(self):
        r"""Gets the aggregate of this GetMetricsValue.

        :return: The aggregate of this GetMetricsValue.
        :rtype: :class:`huaweicloudsdkiotanalytics.v1.AggregateMetricsRequest`
        """
        return self._aggregate

    @aggregate.setter
    def aggregate(self, aggregate):
        r"""Sets the aggregate of this GetMetricsValue.

        :param aggregate: The aggregate of this GetMetricsValue.
        :type aggregate: :class:`huaweicloudsdkiotanalytics.v1.AggregateMetricsRequest`
        """
        self._aggregate = aggregate

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
        if not isinstance(other, GetMetricsValue):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
