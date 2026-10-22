# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class V2EndpointMetrics:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'collection_time': 'int',
        'values': 'list[V2EndpointMetric]'
    }

    attribute_map = {
        'collection_time': 'collection_time',
        'values': 'values'
    }

    def __init__(self, collection_time=None, values=None):
        r"""V2EndpointMetrics

        The model defined in huaweicloud sdk

        :param collection_time: **参数解释**：数据时间（秒）。 **取值范围**：不涉及。 
        :type collection_time: int
        :param values: **参数解释**：端点指标值列表，列表元素为端点指标信息对象。 
        :type values: list[:class:`huaweicloudsdkaidatalake.v2.V2EndpointMetric`]
        """
        
        

        self._collection_time = None
        self._values = None
        self.discriminator = None

        if collection_time is not None:
            self.collection_time = collection_time
        if values is not None:
            self.values = values

    @property
    def collection_time(self):
        r"""Gets the collection_time of this V2EndpointMetrics.

        **参数解释**：数据时间（秒）。 **取值范围**：不涉及。 

        :return: The collection_time of this V2EndpointMetrics.
        :rtype: int
        """
        return self._collection_time

    @collection_time.setter
    def collection_time(self, collection_time):
        r"""Sets the collection_time of this V2EndpointMetrics.

        **参数解释**：数据时间（秒）。 **取值范围**：不涉及。 

        :param collection_time: The collection_time of this V2EndpointMetrics.
        :type collection_time: int
        """
        self._collection_time = collection_time

    @property
    def values(self):
        r"""Gets the values of this V2EndpointMetrics.

        **参数解释**：端点指标值列表，列表元素为端点指标信息对象。 

        :return: The values of this V2EndpointMetrics.
        :rtype: list[:class:`huaweicloudsdkaidatalake.v2.V2EndpointMetric`]
        """
        return self._values

    @values.setter
    def values(self, values):
        r"""Sets the values of this V2EndpointMetrics.

        **参数解释**：端点指标值列表，列表元素为端点指标信息对象。 

        :param values: The values of this V2EndpointMetrics.
        :type values: list[:class:`huaweicloudsdkaidatalake.v2.V2EndpointMetric`]
        """
        self._values = values

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
        if not isinstance(other, V2EndpointMetrics):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
