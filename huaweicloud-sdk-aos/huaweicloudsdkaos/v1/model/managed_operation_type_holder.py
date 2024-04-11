# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ManagedOperationTypeHolder:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'managed_operation': 'ManagedOperation'
    }

    attribute_map = {
        'managed_operation': 'managed_operation'
    }

    def __init__(self, managed_operation=None):
        """ManagedOperationTypeHolder

        The model defined in huaweicloud sdk

        :param managed_operation: 
        :type managed_operation: :class:`huaweicloudsdkaos.v1.ManagedOperation`
        """
        
        

        self._managed_operation = None
        self.discriminator = None

        if managed_operation is not None:
            self.managed_operation = managed_operation

    @property
    def managed_operation(self):
        """Gets the managed_operation of this ManagedOperationTypeHolder.

        :return: The managed_operation of this ManagedOperationTypeHolder.
        :rtype: :class:`huaweicloudsdkaos.v1.ManagedOperation`
        """
        return self._managed_operation

    @managed_operation.setter
    def managed_operation(self, managed_operation):
        """Sets the managed_operation of this ManagedOperationTypeHolder.

        :param managed_operation: The managed_operation of this ManagedOperationTypeHolder.
        :type managed_operation: :class:`huaweicloudsdkaos.v1.ManagedOperation`
        """
        self._managed_operation = managed_operation

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
        if not isinstance(other, ManagedOperationTypeHolder):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
