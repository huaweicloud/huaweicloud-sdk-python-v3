# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UnusedAnalysisRule:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'exclusions': 'list[UnusedAnalysisRuleCriteria]'
    }

    attribute_map = {
        'exclusions': 'exclusions'
    }

    def __init__(self, exclusions=None):
        r"""UnusedAnalysisRule

        The model defined in huaweicloud sdk

        :param exclusions: 排除规则。
        :type exclusions: list[:class:`huaweicloudsdkiamaccessanalyzer.v1.UnusedAnalysisRuleCriteria`]
        """
        
        

        self._exclusions = None
        self.discriminator = None

        if exclusions is not None:
            self.exclusions = exclusions

    @property
    def exclusions(self):
        r"""Gets the exclusions of this UnusedAnalysisRule.

        排除规则。

        :return: The exclusions of this UnusedAnalysisRule.
        :rtype: list[:class:`huaweicloudsdkiamaccessanalyzer.v1.UnusedAnalysisRuleCriteria`]
        """
        return self._exclusions

    @exclusions.setter
    def exclusions(self, exclusions):
        r"""Sets the exclusions of this UnusedAnalysisRule.

        排除规则。

        :param exclusions: The exclusions of this UnusedAnalysisRule.
        :type exclusions: list[:class:`huaweicloudsdkiamaccessanalyzer.v1.UnusedAnalysisRuleCriteria`]
        """
        self._exclusions = exclusions

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
        if not isinstance(other, UnusedAnalysisRule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
