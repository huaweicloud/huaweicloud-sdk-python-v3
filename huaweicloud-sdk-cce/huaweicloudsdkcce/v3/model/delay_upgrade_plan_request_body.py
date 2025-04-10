# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DelayUpgradePlanRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'not_before': 'date'
    }

    attribute_map = {
        'not_before': 'notBefore'
    }

    def __init__(self, not_before=None):
        r"""DelayUpgradePlanRequestBody

        The model defined in huaweicloud sdk

        :param not_before: 新的自动升级计划启动时间，必须早于notBeforeDeadline
        :type not_before: date
        """
        
        

        self._not_before = None
        self.discriminator = None

        self.not_before = not_before

    @property
    def not_before(self):
        r"""Gets the not_before of this DelayUpgradePlanRequestBody.

        新的自动升级计划启动时间，必须早于notBeforeDeadline

        :return: The not_before of this DelayUpgradePlanRequestBody.
        :rtype: date
        """
        return self._not_before

    @not_before.setter
    def not_before(self, not_before):
        r"""Sets the not_before of this DelayUpgradePlanRequestBody.

        新的自动升级计划启动时间，必须早于notBeforeDeadline

        :param not_before: The not_before of this DelayUpgradePlanRequestBody.
        :type not_before: date
        """
        self._not_before = not_before

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
        if not isinstance(other, DelayUpgradePlanRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
