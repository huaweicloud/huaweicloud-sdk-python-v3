# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CostDataByDimension:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'dimensions': 'list[DimensionGroup]',
        'costs': 'list[Cost]',
        'amount_by_costs': 'str',
        'official_amount_by_costs': 'str'
    }

    attribute_map = {
        'dimensions': 'dimensions',
        'costs': 'costs',
        'amount_by_costs': 'amount_by_costs',
        'official_amount_by_costs': 'official_amount_by_costs'
    }

    def __init__(self, dimensions=None, costs=None, amount_by_costs=None, official_amount_by_costs=None):
        """CostDataByDimension

        The model defined in huaweicloud sdk

        :param dimensions: 维度列表。
        :type dimensions: list[:class:`huaweicloudsdkbssintl.v2.DimensionGroup`]
        :param costs: 成本值。
        :type costs: list[:class:`huaweicloudsdkbssintl.v2.Cost`]
        :param amount_by_costs: 此维度值对应整个时间跨度的成本汇总金额。
        :type amount_by_costs: str
        :param official_amount_by_costs: 此维度值对应整个时间跨度的官网价汇总金额。
        :type official_amount_by_costs: str
        """
        
        

        self._dimensions = None
        self._costs = None
        self._amount_by_costs = None
        self._official_amount_by_costs = None
        self.discriminator = None

        if dimensions is not None:
            self.dimensions = dimensions
        if costs is not None:
            self.costs = costs
        if amount_by_costs is not None:
            self.amount_by_costs = amount_by_costs
        if official_amount_by_costs is not None:
            self.official_amount_by_costs = official_amount_by_costs

    @property
    def dimensions(self):
        """Gets the dimensions of this CostDataByDimension.

        维度列表。

        :return: The dimensions of this CostDataByDimension.
        :rtype: list[:class:`huaweicloudsdkbssintl.v2.DimensionGroup`]
        """
        return self._dimensions

    @dimensions.setter
    def dimensions(self, dimensions):
        """Sets the dimensions of this CostDataByDimension.

        维度列表。

        :param dimensions: The dimensions of this CostDataByDimension.
        :type dimensions: list[:class:`huaweicloudsdkbssintl.v2.DimensionGroup`]
        """
        self._dimensions = dimensions

    @property
    def costs(self):
        """Gets the costs of this CostDataByDimension.

        成本值。

        :return: The costs of this CostDataByDimension.
        :rtype: list[:class:`huaweicloudsdkbssintl.v2.Cost`]
        """
        return self._costs

    @costs.setter
    def costs(self, costs):
        """Sets the costs of this CostDataByDimension.

        成本值。

        :param costs: The costs of this CostDataByDimension.
        :type costs: list[:class:`huaweicloudsdkbssintl.v2.Cost`]
        """
        self._costs = costs

    @property
    def amount_by_costs(self):
        """Gets the amount_by_costs of this CostDataByDimension.

        此维度值对应整个时间跨度的成本汇总金额。

        :return: The amount_by_costs of this CostDataByDimension.
        :rtype: str
        """
        return self._amount_by_costs

    @amount_by_costs.setter
    def amount_by_costs(self, amount_by_costs):
        """Sets the amount_by_costs of this CostDataByDimension.

        此维度值对应整个时间跨度的成本汇总金额。

        :param amount_by_costs: The amount_by_costs of this CostDataByDimension.
        :type amount_by_costs: str
        """
        self._amount_by_costs = amount_by_costs

    @property
    def official_amount_by_costs(self):
        """Gets the official_amount_by_costs of this CostDataByDimension.

        此维度值对应整个时间跨度的官网价汇总金额。

        :return: The official_amount_by_costs of this CostDataByDimension.
        :rtype: str
        """
        return self._official_amount_by_costs

    @official_amount_by_costs.setter
    def official_amount_by_costs(self, official_amount_by_costs):
        """Sets the official_amount_by_costs of this CostDataByDimension.

        此维度值对应整个时间跨度的官网价汇总金额。

        :param official_amount_by_costs: The official_amount_by_costs of this CostDataByDimension.
        :type official_amount_by_costs: str
        """
        self._official_amount_by_costs = official_amount_by_costs

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
        if not isinstance(other, CostDataByDimension):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
