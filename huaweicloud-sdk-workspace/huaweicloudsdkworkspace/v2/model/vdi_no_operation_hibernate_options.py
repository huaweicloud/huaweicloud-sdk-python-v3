# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VdiNoOperationHibernateOptions:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'no_operation_hibernate_minutes': 'int'
    }

    attribute_map = {
        'no_operation_hibernate_minutes': 'no_operation_hibernate_minutes'
    }

    def __init__(self, no_operation_hibernate_minutes=None):
        r"""VdiNoOperationHibernateOptions

        The model defined in huaweicloud sdk

        :param no_operation_hibernate_minutes: 策略组ID。
        :type no_operation_hibernate_minutes: int
        """
        
        

        self._no_operation_hibernate_minutes = None
        self.discriminator = None

        if no_operation_hibernate_minutes is not None:
            self.no_operation_hibernate_minutes = no_operation_hibernate_minutes

    @property
    def no_operation_hibernate_minutes(self):
        r"""Gets the no_operation_hibernate_minutes of this VdiNoOperationHibernateOptions.

        策略组ID。

        :return: The no_operation_hibernate_minutes of this VdiNoOperationHibernateOptions.
        :rtype: int
        """
        return self._no_operation_hibernate_minutes

    @no_operation_hibernate_minutes.setter
    def no_operation_hibernate_minutes(self, no_operation_hibernate_minutes):
        r"""Sets the no_operation_hibernate_minutes of this VdiNoOperationHibernateOptions.

        策略组ID。

        :param no_operation_hibernate_minutes: The no_operation_hibernate_minutes of this VdiNoOperationHibernateOptions.
        :type no_operation_hibernate_minutes: int
        """
        self._no_operation_hibernate_minutes = no_operation_hibernate_minutes

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
        if not isinstance(other, VdiNoOperationHibernateOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
