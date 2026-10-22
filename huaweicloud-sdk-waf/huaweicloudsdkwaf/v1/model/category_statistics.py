# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CategoryStatistics:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'category_type': 'str',
        'total_count': 'int',
        'risk_count': 'int'
    }

    attribute_map = {
        'category_type': 'category_type',
        'total_count': 'total_count',
        'risk_count': 'risk_count'
    }

    def __init__(self, category_type=None, total_count=None, risk_count=None):
        r"""CategoryStatistics

        The model defined in huaweicloud sdk

        :param category_type: 防护类型
        :type category_type: str
        :param total_count: 累计检测数
        :type total_count: int
        :param risk_count: 检出风险数
        :type risk_count: int
        """
        
        

        self._category_type = None
        self._total_count = None
        self._risk_count = None
        self.discriminator = None

        self.category_type = category_type
        self.total_count = total_count
        self.risk_count = risk_count

    @property
    def category_type(self):
        r"""Gets the category_type of this CategoryStatistics.

        防护类型

        :return: The category_type of this CategoryStatistics.
        :rtype: str
        """
        return self._category_type

    @category_type.setter
    def category_type(self, category_type):
        r"""Sets the category_type of this CategoryStatistics.

        防护类型

        :param category_type: The category_type of this CategoryStatistics.
        :type category_type: str
        """
        self._category_type = category_type

    @property
    def total_count(self):
        r"""Gets the total_count of this CategoryStatistics.

        累计检测数

        :return: The total_count of this CategoryStatistics.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this CategoryStatistics.

        累计检测数

        :param total_count: The total_count of this CategoryStatistics.
        :type total_count: int
        """
        self._total_count = total_count

    @property
    def risk_count(self):
        r"""Gets the risk_count of this CategoryStatistics.

        检出风险数

        :return: The risk_count of this CategoryStatistics.
        :rtype: int
        """
        return self._risk_count

    @risk_count.setter
    def risk_count(self, risk_count):
        r"""Sets the risk_count of this CategoryStatistics.

        检出风险数

        :param risk_count: The risk_count of this CategoryStatistics.
        :type risk_count: int
        """
        self._risk_count = risk_count

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
        if not isinstance(other, CategoryStatistics):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
