# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CompareResultItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'benchmark_group': 'list[CompareGroupItem]',
        'control_group': 'list[CompareGroupItem]'
    }

    attribute_map = {
        'benchmark_group': 'benchmark_group',
        'control_group': 'control_group'
    }

    def __init__(self, benchmark_group=None, control_group=None):
        r"""CompareResultItem

        The model defined in huaweicloud sdk

        :param benchmark_group: 基准组评估结果列表，通常是被测系统的标准输出或对比基线。
        :type benchmark_group: list[:class:`huaweicloudsdkagentarts.v1.CompareGroupItem`]
        :param control_group: 对照组评估结果列表，通常是实验系统的输出或待评估的变体。
        :type control_group: list[:class:`huaweicloudsdkagentarts.v1.CompareGroupItem`]
        """
        
        

        self._benchmark_group = None
        self._control_group = None
        self.discriminator = None

        if benchmark_group is not None:
            self.benchmark_group = benchmark_group
        if control_group is not None:
            self.control_group = control_group

    @property
    def benchmark_group(self):
        r"""Gets the benchmark_group of this CompareResultItem.

        基准组评估结果列表，通常是被测系统的标准输出或对比基线。

        :return: The benchmark_group of this CompareResultItem.
        :rtype: list[:class:`huaweicloudsdkagentarts.v1.CompareGroupItem`]
        """
        return self._benchmark_group

    @benchmark_group.setter
    def benchmark_group(self, benchmark_group):
        r"""Sets the benchmark_group of this CompareResultItem.

        基准组评估结果列表，通常是被测系统的标准输出或对比基线。

        :param benchmark_group: The benchmark_group of this CompareResultItem.
        :type benchmark_group: list[:class:`huaweicloudsdkagentarts.v1.CompareGroupItem`]
        """
        self._benchmark_group = benchmark_group

    @property
    def control_group(self):
        r"""Gets the control_group of this CompareResultItem.

        对照组评估结果列表，通常是实验系统的输出或待评估的变体。

        :return: The control_group of this CompareResultItem.
        :rtype: list[:class:`huaweicloudsdkagentarts.v1.CompareGroupItem`]
        """
        return self._control_group

    @control_group.setter
    def control_group(self, control_group):
        r"""Sets the control_group of this CompareResultItem.

        对照组评估结果列表，通常是实验系统的输出或待评估的变体。

        :param control_group: The control_group of this CompareResultItem.
        :type control_group: list[:class:`huaweicloudsdkagentarts.v1.CompareGroupItem`]
        """
        self._control_group = control_group

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
        if not isinstance(other, CompareResultItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
