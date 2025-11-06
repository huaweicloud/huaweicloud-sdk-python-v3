# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PolicyStatesStatistics:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total_resource_count': 'int',
        'non_compliant_resource_count': 'int',
        'total_policy_count': 'int',
        'non_compliant_policy_count': 'int',
        'statistic_date': 'str'
    }

    attribute_map = {
        'total_resource_count': 'total_resource_count',
        'non_compliant_resource_count': 'non_compliant_resource_count',
        'total_policy_count': 'total_policy_count',
        'non_compliant_policy_count': 'non_compliant_policy_count',
        'statistic_date': 'statistic_date'
    }

    def __init__(self, total_resource_count=None, non_compliant_resource_count=None, total_policy_count=None, non_compliant_policy_count=None, statistic_date=None):
        r"""PolicyStatesStatistics

        The model defined in huaweicloud sdk

        :param total_resource_count: 资源总数
        :type total_resource_count: int
        :param non_compliant_resource_count: 不合规资源数量
        :type non_compliant_resource_count: int
        :param total_policy_count: 合规规则总数
        :type total_policy_count: int
        :param non_compliant_policy_count: 不合规规则数量
        :type non_compliant_policy_count: int
        :param statistic_date: 统计日期
        :type statistic_date: str
        """
        
        

        self._total_resource_count = None
        self._non_compliant_resource_count = None
        self._total_policy_count = None
        self._non_compliant_policy_count = None
        self._statistic_date = None
        self.discriminator = None

        if total_resource_count is not None:
            self.total_resource_count = total_resource_count
        if non_compliant_resource_count is not None:
            self.non_compliant_resource_count = non_compliant_resource_count
        if total_policy_count is not None:
            self.total_policy_count = total_policy_count
        if non_compliant_policy_count is not None:
            self.non_compliant_policy_count = non_compliant_policy_count
        if statistic_date is not None:
            self.statistic_date = statistic_date

    @property
    def total_resource_count(self):
        r"""Gets the total_resource_count of this PolicyStatesStatistics.

        资源总数

        :return: The total_resource_count of this PolicyStatesStatistics.
        :rtype: int
        """
        return self._total_resource_count

    @total_resource_count.setter
    def total_resource_count(self, total_resource_count):
        r"""Sets the total_resource_count of this PolicyStatesStatistics.

        资源总数

        :param total_resource_count: The total_resource_count of this PolicyStatesStatistics.
        :type total_resource_count: int
        """
        self._total_resource_count = total_resource_count

    @property
    def non_compliant_resource_count(self):
        r"""Gets the non_compliant_resource_count of this PolicyStatesStatistics.

        不合规资源数量

        :return: The non_compliant_resource_count of this PolicyStatesStatistics.
        :rtype: int
        """
        return self._non_compliant_resource_count

    @non_compliant_resource_count.setter
    def non_compliant_resource_count(self, non_compliant_resource_count):
        r"""Sets the non_compliant_resource_count of this PolicyStatesStatistics.

        不合规资源数量

        :param non_compliant_resource_count: The non_compliant_resource_count of this PolicyStatesStatistics.
        :type non_compliant_resource_count: int
        """
        self._non_compliant_resource_count = non_compliant_resource_count

    @property
    def total_policy_count(self):
        r"""Gets the total_policy_count of this PolicyStatesStatistics.

        合规规则总数

        :return: The total_policy_count of this PolicyStatesStatistics.
        :rtype: int
        """
        return self._total_policy_count

    @total_policy_count.setter
    def total_policy_count(self, total_policy_count):
        r"""Sets the total_policy_count of this PolicyStatesStatistics.

        合规规则总数

        :param total_policy_count: The total_policy_count of this PolicyStatesStatistics.
        :type total_policy_count: int
        """
        self._total_policy_count = total_policy_count

    @property
    def non_compliant_policy_count(self):
        r"""Gets the non_compliant_policy_count of this PolicyStatesStatistics.

        不合规规则数量

        :return: The non_compliant_policy_count of this PolicyStatesStatistics.
        :rtype: int
        """
        return self._non_compliant_policy_count

    @non_compliant_policy_count.setter
    def non_compliant_policy_count(self, non_compliant_policy_count):
        r"""Sets the non_compliant_policy_count of this PolicyStatesStatistics.

        不合规规则数量

        :param non_compliant_policy_count: The non_compliant_policy_count of this PolicyStatesStatistics.
        :type non_compliant_policy_count: int
        """
        self._non_compliant_policy_count = non_compliant_policy_count

    @property
    def statistic_date(self):
        r"""Gets the statistic_date of this PolicyStatesStatistics.

        统计日期

        :return: The statistic_date of this PolicyStatesStatistics.
        :rtype: str
        """
        return self._statistic_date

    @statistic_date.setter
    def statistic_date(self, statistic_date):
        r"""Sets the statistic_date of this PolicyStatesStatistics.

        统计日期

        :param statistic_date: The statistic_date of this PolicyStatesStatistics.
        :type statistic_date: str
        """
        self._statistic_date = statistic_date

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
        if not isinstance(other, PolicyStatesStatistics):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
