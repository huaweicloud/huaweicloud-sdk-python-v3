# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PreferredSchedulingTerm:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'preference': 'PreferredSchedulingTermPreference',
        'weight': 'int'
    }

    attribute_map = {
        'preference': 'preference',
        'weight': 'weight'
    }

    def __init__(self, preference=None, weight=None):
        """PreferredSchedulingTerm

        The model defined in huaweicloud sdk

        :param preference: 
        :type preference: :class:`huaweicloudsdkief.v1.PreferredSchedulingTermPreference`
        :param weight: 权重，范围为1-100
        :type weight: int
        """
        
        

        self._preference = None
        self._weight = None
        self.discriminator = None

        if preference is not None:
            self.preference = preference
        if weight is not None:
            self.weight = weight

    @property
    def preference(self):
        """Gets the preference of this PreferredSchedulingTerm.

        :return: The preference of this PreferredSchedulingTerm.
        :rtype: :class:`huaweicloudsdkief.v1.PreferredSchedulingTermPreference`
        """
        return self._preference

    @preference.setter
    def preference(self, preference):
        """Sets the preference of this PreferredSchedulingTerm.

        :param preference: The preference of this PreferredSchedulingTerm.
        :type preference: :class:`huaweicloudsdkief.v1.PreferredSchedulingTermPreference`
        """
        self._preference = preference

    @property
    def weight(self):
        """Gets the weight of this PreferredSchedulingTerm.

        权重，范围为1-100

        :return: The weight of this PreferredSchedulingTerm.
        :rtype: int
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """Sets the weight of this PreferredSchedulingTerm.

        权重，范围为1-100

        :param weight: The weight of this PreferredSchedulingTerm.
        :type weight: int
        """
        self._weight = weight

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
        if not isinstance(other, PreferredSchedulingTerm):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
