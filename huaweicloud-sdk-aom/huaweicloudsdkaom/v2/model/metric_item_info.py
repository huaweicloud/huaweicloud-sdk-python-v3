# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MetricItemInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'dimensions': 'list[Dimension2]',
        'namespace': 'str'
    }

    attribute_map = {
        'dimensions': 'dimensions',
        'namespace': 'namespace'
    }

    def __init__(self, dimensions=None, namespace=None):
        r"""MetricItemInfo

        The model defined in huaweicloud sdk

        :param dimensions: 指标维度列表。维度最多允许50个，单个维度为json对象，结构说明如下 dimension.name：长度最短为1，最大为32。 dimension.value：长度最短为1，最大为64。
        :type dimensions: list[:class:`huaweicloudsdkaom.v2.Dimension2`]
        :param namespace: 指标命名空间。 namespace中不允许存在\&quot;:\&quot;符号，取值范围格式为service.item；service和item必须是字符串，必须以字母开头，只能包含0-9/a-z/A-Z/_，总长度最短为3，最大为32，service不能为“PAAS”。
        :type namespace: str
        """
        
        

        self._dimensions = None
        self._namespace = None
        self.discriminator = None

        self.dimensions = dimensions
        self.namespace = namespace

    @property
    def dimensions(self):
        r"""Gets the dimensions of this MetricItemInfo.

        指标维度列表。维度最多允许50个，单个维度为json对象，结构说明如下 dimension.name：长度最短为1，最大为32。 dimension.value：长度最短为1，最大为64。

        :return: The dimensions of this MetricItemInfo.
        :rtype: list[:class:`huaweicloudsdkaom.v2.Dimension2`]
        """
        return self._dimensions

    @dimensions.setter
    def dimensions(self, dimensions):
        r"""Sets the dimensions of this MetricItemInfo.

        指标维度列表。维度最多允许50个，单个维度为json对象，结构说明如下 dimension.name：长度最短为1，最大为32。 dimension.value：长度最短为1，最大为64。

        :param dimensions: The dimensions of this MetricItemInfo.
        :type dimensions: list[:class:`huaweicloudsdkaom.v2.Dimension2`]
        """
        self._dimensions = dimensions

    @property
    def namespace(self):
        r"""Gets the namespace of this MetricItemInfo.

        指标命名空间。 namespace中不允许存在\":\"符号，取值范围格式为service.item；service和item必须是字符串，必须以字母开头，只能包含0-9/a-z/A-Z/_，总长度最短为3，最大为32，service不能为“PAAS”。

        :return: The namespace of this MetricItemInfo.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        r"""Sets the namespace of this MetricItemInfo.

        指标命名空间。 namespace中不允许存在\":\"符号，取值范围格式为service.item；service和item必须是字符串，必须以字母开头，只能包含0-9/a-z/A-Z/_，总长度最短为3，最大为32，service不能为“PAAS”。

        :param namespace: The namespace of this MetricItemInfo.
        :type namespace: str
        """
        self._namespace = namespace

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
        if not isinstance(other, MetricItemInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
