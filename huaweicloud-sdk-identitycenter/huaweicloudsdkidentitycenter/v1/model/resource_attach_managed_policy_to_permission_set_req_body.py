# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResourceAttachManagedPolicyToPermissionSetReqBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'managed_role_id': 'str',
        'managed_role_name': 'str'
    }

    attribute_map = {
        'managed_role_id': 'managed_role_id',
        'managed_role_name': 'managed_role_name'
    }

    def __init__(self, managed_role_id=None, managed_role_name=None):
        r"""ResourceAttachManagedPolicyToPermissionSetReqBody

        The model defined in huaweicloud sdk

        :param managed_role_id: IAM系统策略唯一标识
        :type managed_role_id: str
        :param managed_role_name: IAM系统策略名称
        :type managed_role_name: str
        """
        
        

        self._managed_role_id = None
        self._managed_role_name = None
        self.discriminator = None

        self.managed_role_id = managed_role_id
        if managed_role_name is not None:
            self.managed_role_name = managed_role_name

    @property
    def managed_role_id(self):
        r"""Gets the managed_role_id of this ResourceAttachManagedPolicyToPermissionSetReqBody.

        IAM系统策略唯一标识

        :return: The managed_role_id of this ResourceAttachManagedPolicyToPermissionSetReqBody.
        :rtype: str
        """
        return self._managed_role_id

    @managed_role_id.setter
    def managed_role_id(self, managed_role_id):
        r"""Sets the managed_role_id of this ResourceAttachManagedPolicyToPermissionSetReqBody.

        IAM系统策略唯一标识

        :param managed_role_id: The managed_role_id of this ResourceAttachManagedPolicyToPermissionSetReqBody.
        :type managed_role_id: str
        """
        self._managed_role_id = managed_role_id

    @property
    def managed_role_name(self):
        r"""Gets the managed_role_name of this ResourceAttachManagedPolicyToPermissionSetReqBody.

        IAM系统策略名称

        :return: The managed_role_name of this ResourceAttachManagedPolicyToPermissionSetReqBody.
        :rtype: str
        """
        return self._managed_role_name

    @managed_role_name.setter
    def managed_role_name(self, managed_role_name):
        r"""Sets the managed_role_name of this ResourceAttachManagedPolicyToPermissionSetReqBody.

        IAM系统策略名称

        :param managed_role_name: The managed_role_name of this ResourceAttachManagedPolicyToPermissionSetReqBody.
        :type managed_role_name: str
        """
        self._managed_role_name = managed_role_name

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
        if not isinstance(other, ResourceAttachManagedPolicyToPermissionSetReqBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
