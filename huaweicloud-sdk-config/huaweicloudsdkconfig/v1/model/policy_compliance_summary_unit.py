# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PolicyComplianceSummaryUnit:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'compliant_count': 'int',
        'non_compliant_count': 'int'
    }

    attribute_map = {
        'compliant_count': 'compliant_count',
        'non_compliant_count': 'non_compliant_count'
    }

    def __init__(self, compliant_count=None, non_compliant_count=None):
        r"""PolicyComplianceSummaryUnit

        The model defined in huaweicloud sdk

        :param compliant_count: 合规数量
        :type compliant_count: int
        :param non_compliant_count: 不合规数量
        :type non_compliant_count: int
        """
        
        

        self._compliant_count = None
        self._non_compliant_count = None
        self.discriminator = None

        if compliant_count is not None:
            self.compliant_count = compliant_count
        if non_compliant_count is not None:
            self.non_compliant_count = non_compliant_count

    @property
    def compliant_count(self):
        r"""Gets the compliant_count of this PolicyComplianceSummaryUnit.

        合规数量

        :return: The compliant_count of this PolicyComplianceSummaryUnit.
        :rtype: int
        """
        return self._compliant_count

    @compliant_count.setter
    def compliant_count(self, compliant_count):
        r"""Sets the compliant_count of this PolicyComplianceSummaryUnit.

        合规数量

        :param compliant_count: The compliant_count of this PolicyComplianceSummaryUnit.
        :type compliant_count: int
        """
        self._compliant_count = compliant_count

    @property
    def non_compliant_count(self):
        r"""Gets the non_compliant_count of this PolicyComplianceSummaryUnit.

        不合规数量

        :return: The non_compliant_count of this PolicyComplianceSummaryUnit.
        :rtype: int
        """
        return self._non_compliant_count

    @non_compliant_count.setter
    def non_compliant_count(self, non_compliant_count):
        r"""Sets the non_compliant_count of this PolicyComplianceSummaryUnit.

        不合规数量

        :param non_compliant_count: The non_compliant_count of this PolicyComplianceSummaryUnit.
        :type non_compliant_count: int
        """
        self._non_compliant_count = non_compliant_count

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
        if not isinstance(other, PolicyComplianceSummaryUnit):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
