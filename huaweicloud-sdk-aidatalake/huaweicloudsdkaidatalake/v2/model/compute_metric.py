# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ComputeMetric:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'compute_name': 'str',
        'compute_value': 'float'
    }

    attribute_map = {
        'compute_name': 'compute_name',
        'compute_value': 'compute_value'
    }

    def __init__(self, compute_name=None, compute_value=None):
        r"""ComputeMetric

        The model defined in huaweicloud sdk

        :param compute_name: **参数解释**：资源池名称。 **取值范围**：长度为1~63个字符。 
        :type compute_name: str
        :param compute_value: **参数解释**：资源池指标值。 **取值范围**：0~100。 
        :type compute_value: float
        """
        
        

        self._compute_name = None
        self._compute_value = None
        self.discriminator = None

        if compute_name is not None:
            self.compute_name = compute_name
        if compute_value is not None:
            self.compute_value = compute_value

    @property
    def compute_name(self):
        r"""Gets the compute_name of this ComputeMetric.

        **参数解释**：资源池名称。 **取值范围**：长度为1~63个字符。 

        :return: The compute_name of this ComputeMetric.
        :rtype: str
        """
        return self._compute_name

    @compute_name.setter
    def compute_name(self, compute_name):
        r"""Sets the compute_name of this ComputeMetric.

        **参数解释**：资源池名称。 **取值范围**：长度为1~63个字符。 

        :param compute_name: The compute_name of this ComputeMetric.
        :type compute_name: str
        """
        self._compute_name = compute_name

    @property
    def compute_value(self):
        r"""Gets the compute_value of this ComputeMetric.

        **参数解释**：资源池指标值。 **取值范围**：0~100。 

        :return: The compute_value of this ComputeMetric.
        :rtype: float
        """
        return self._compute_value

    @compute_value.setter
    def compute_value(self, compute_value):
        r"""Sets the compute_value of this ComputeMetric.

        **参数解释**：资源池指标值。 **取值范围**：0~100。 

        :param compute_value: The compute_value of this ComputeMetric.
        :type compute_value: float
        """
        self._compute_value = compute_value

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
        if not isinstance(other, ComputeMetric):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
