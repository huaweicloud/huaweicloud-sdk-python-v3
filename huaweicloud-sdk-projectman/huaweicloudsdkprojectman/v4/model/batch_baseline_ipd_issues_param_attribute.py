# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchBaselineIpdIssuesParamAttribute:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'baseline': 'str'
    }

    attribute_map = {
        'baseline': 'baseline'
    }

    def __init__(self, baseline=None):
        r"""BatchBaselineIpdIssuesParamAttribute

        The model defined in huaweicloud sdk

        :param baseline: 工作项基线标识。
        :type baseline: str
        """
        
        

        self._baseline = None
        self.discriminator = None

        self.baseline = baseline

    @property
    def baseline(self):
        r"""Gets the baseline of this BatchBaselineIpdIssuesParamAttribute.

        工作项基线标识。

        :return: The baseline of this BatchBaselineIpdIssuesParamAttribute.
        :rtype: str
        """
        return self._baseline

    @baseline.setter
    def baseline(self, baseline):
        r"""Sets the baseline of this BatchBaselineIpdIssuesParamAttribute.

        工作项基线标识。

        :param baseline: The baseline of this BatchBaselineIpdIssuesParamAttribute.
        :type baseline: str
        """
        self._baseline = baseline

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
        if not isinstance(other, BatchBaselineIpdIssuesParamAttribute):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
