# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OperationPreferencesTypeHolder:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'operation_preferences': 'OperationPreferences'
    }

    attribute_map = {
        'operation_preferences': 'operation_preferences'
    }

    def __init__(self, operation_preferences=None):
        r"""OperationPreferencesTypeHolder

        The model defined in huaweicloud sdk

        :param operation_preferences: 
        :type operation_preferences: :class:`huaweicloudsdkaos.v1.OperationPreferences`
        """
        
        

        self._operation_preferences = None
        self.discriminator = None

        if operation_preferences is not None:
            self.operation_preferences = operation_preferences

    @property
    def operation_preferences(self):
        r"""Gets the operation_preferences of this OperationPreferencesTypeHolder.

        :return: The operation_preferences of this OperationPreferencesTypeHolder.
        :rtype: :class:`huaweicloudsdkaos.v1.OperationPreferences`
        """
        return self._operation_preferences

    @operation_preferences.setter
    def operation_preferences(self, operation_preferences):
        r"""Sets the operation_preferences of this OperationPreferencesTypeHolder.

        :param operation_preferences: The operation_preferences of this OperationPreferencesTypeHolder.
        :type operation_preferences: :class:`huaweicloudsdkaos.v1.OperationPreferences`
        """
        self._operation_preferences = operation_preferences

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
        if not isinstance(other, OperationPreferencesTypeHolder):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
