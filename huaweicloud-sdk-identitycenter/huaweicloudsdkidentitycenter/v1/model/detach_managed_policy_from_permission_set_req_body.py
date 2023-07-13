# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DetachManagedPolicyFromPermissionSetReqBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'managed_policy_id': 'str'
    }

    attribute_map = {
        'managed_policy_id': 'managed_policy_id'
    }

    def __init__(self, managed_policy_id=None):
        """DetachManagedPolicyFromPermissionSetReqBody

        The model defined in huaweicloud sdk

        :param managed_policy_id: 管理策略唯一标识
        :type managed_policy_id: str
        """
        
        

        self._managed_policy_id = None
        self.discriminator = None

        self.managed_policy_id = managed_policy_id

    @property
    def managed_policy_id(self):
        """Gets the managed_policy_id of this DetachManagedPolicyFromPermissionSetReqBody.

        管理策略唯一标识

        :return: The managed_policy_id of this DetachManagedPolicyFromPermissionSetReqBody.
        :rtype: str
        """
        return self._managed_policy_id

    @managed_policy_id.setter
    def managed_policy_id(self, managed_policy_id):
        """Sets the managed_policy_id of this DetachManagedPolicyFromPermissionSetReqBody.

        管理策略唯一标识

        :param managed_policy_id: The managed_policy_id of this DetachManagedPolicyFromPermissionSetReqBody.
        :type managed_policy_id: str
        """
        self._managed_policy_id = managed_policy_id

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
        if not isinstance(other, DetachManagedPolicyFromPermissionSetReqBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
