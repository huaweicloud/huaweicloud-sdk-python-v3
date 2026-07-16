# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CompareColumns:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'parameters': 'list[str]',
        'metrics': 'list[str]'
    }

    attribute_map = {
        'parameters': 'parameters',
        'metrics': 'metrics'
    }

    def __init__(self, parameters=None, metrics=None):
        r"""CompareColumns

        The model defined in huaweicloud sdk

        :param parameters: **参数解释**：参数字段。
        :type parameters: list[str]
        :param metrics: **参数解释**：度量字段。
        :type metrics: list[str]
        """
        
        

        self._parameters = None
        self._metrics = None
        self.discriminator = None

        if parameters is not None:
            self.parameters = parameters
        if metrics is not None:
            self.metrics = metrics

    @property
    def parameters(self):
        r"""Gets the parameters of this CompareColumns.

        **参数解释**：参数字段。

        :return: The parameters of this CompareColumns.
        :rtype: list[str]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        r"""Sets the parameters of this CompareColumns.

        **参数解释**：参数字段。

        :param parameters: The parameters of this CompareColumns.
        :type parameters: list[str]
        """
        self._parameters = parameters

    @property
    def metrics(self):
        r"""Gets the metrics of this CompareColumns.

        **参数解释**：度量字段。

        :return: The metrics of this CompareColumns.
        :rtype: list[str]
        """
        return self._metrics

    @metrics.setter
    def metrics(self, metrics):
        r"""Sets the metrics of this CompareColumns.

        **参数解释**：度量字段。

        :param metrics: The metrics of this CompareColumns.
        :type metrics: list[str]
        """
        self._metrics = metrics

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
        if not isinstance(other, CompareColumns):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
