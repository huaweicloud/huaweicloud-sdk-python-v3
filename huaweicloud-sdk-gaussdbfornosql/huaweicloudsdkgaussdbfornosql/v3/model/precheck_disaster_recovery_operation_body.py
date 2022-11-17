# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PrecheckDisasterRecoveryOperationBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'operation': 'str',
        'disaster_recovery_instance': 'PrecheckDisasterRecoveryInstance'
    }

    attribute_map = {
        'operation': 'operation',
        'disaster_recovery_instance': 'disaster_recovery_instance'
    }

    def __init__(self, operation=None, disaster_recovery_instance=None):
        """PrecheckDisasterRecoveryOperationBody

        The model defined in huaweicloud sdk

        :param operation: 指定预校验的具体容灾操作。
        :type operation: str
        :param disaster_recovery_instance: 
        :type disaster_recovery_instance: :class:`huaweicloudsdkgaussdbfornosql.v3.PrecheckDisasterRecoveryInstance`
        """
        
        

        self._operation = None
        self._disaster_recovery_instance = None
        self.discriminator = None

        self.operation = operation
        if disaster_recovery_instance is not None:
            self.disaster_recovery_instance = disaster_recovery_instance

    @property
    def operation(self):
        """Gets the operation of this PrecheckDisasterRecoveryOperationBody.

        指定预校验的具体容灾操作。

        :return: The operation of this PrecheckDisasterRecoveryOperationBody.
        :rtype: str
        """
        return self._operation

    @operation.setter
    def operation(self, operation):
        """Sets the operation of this PrecheckDisasterRecoveryOperationBody.

        指定预校验的具体容灾操作。

        :param operation: The operation of this PrecheckDisasterRecoveryOperationBody.
        :type operation: str
        """
        self._operation = operation

    @property
    def disaster_recovery_instance(self):
        """Gets the disaster_recovery_instance of this PrecheckDisasterRecoveryOperationBody.

        :return: The disaster_recovery_instance of this PrecheckDisasterRecoveryOperationBody.
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.PrecheckDisasterRecoveryInstance`
        """
        return self._disaster_recovery_instance

    @disaster_recovery_instance.setter
    def disaster_recovery_instance(self, disaster_recovery_instance):
        """Sets the disaster_recovery_instance of this PrecheckDisasterRecoveryOperationBody.

        :param disaster_recovery_instance: The disaster_recovery_instance of this PrecheckDisasterRecoveryOperationBody.
        :type disaster_recovery_instance: :class:`huaweicloudsdkgaussdbfornosql.v3.PrecheckDisasterRecoveryInstance`
        """
        self._disaster_recovery_instance = disaster_recovery_instance

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
        if not isinstance(other, PrecheckDisasterRecoveryOperationBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
