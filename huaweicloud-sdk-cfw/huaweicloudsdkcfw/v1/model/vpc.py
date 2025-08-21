# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Vpc:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'protected': 'ChangedVO',
        'total': 'int'
    }

    attribute_map = {
        'protected': 'protected',
        'total': 'total'
    }

    def __init__(self, protected=None, total=None):
        r"""Vpc

        The model defined in huaweicloud sdk

        :param protected: 
        :type protected: :class:`huaweicloudsdkcfw.v1.ChangedVO`
        :param total: **参数解释**： 总数 **取值范围**： 不涉及
        :type total: int
        """
        
        

        self._protected = None
        self._total = None
        self.discriminator = None

        if protected is not None:
            self.protected = protected
        if total is not None:
            self.total = total

    @property
    def protected(self):
        r"""Gets the protected of this Vpc.

        :return: The protected of this Vpc.
        :rtype: :class:`huaweicloudsdkcfw.v1.ChangedVO`
        """
        return self._protected

    @protected.setter
    def protected(self, protected):
        r"""Sets the protected of this Vpc.

        :param protected: The protected of this Vpc.
        :type protected: :class:`huaweicloudsdkcfw.v1.ChangedVO`
        """
        self._protected = protected

    @property
    def total(self):
        r"""Gets the total of this Vpc.

        **参数解释**： 总数 **取值范围**： 不涉及

        :return: The total of this Vpc.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this Vpc.

        **参数解释**： 总数 **取值范围**： 不涉及

        :param total: The total of this Vpc.
        :type total: int
        """
        self._total = total

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
        if not isinstance(other, Vpc):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
