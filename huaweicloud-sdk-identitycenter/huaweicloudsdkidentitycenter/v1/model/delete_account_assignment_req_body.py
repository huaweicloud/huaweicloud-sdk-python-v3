# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteAccountAssignmentReqBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'permission_set_id': 'str',
        'principal_id': 'str',
        'principal_type': 'str',
        'target_id': 'str',
        'target_type': 'str'
    }

    attribute_map = {
        'permission_set_id': 'permission_set_id',
        'principal_id': 'principal_id',
        'principal_type': 'principal_type',
        'target_id': 'target_id',
        'target_type': 'target_type'
    }

    def __init__(self, permission_set_id=None, principal_id=None, principal_type=None, target_id=None, target_type=None):
        """DeleteAccountAssignmentReqBody

        The model defined in huaweicloud sdk

        :param permission_set_id: 权限集唯一标识
        :type permission_set_id: str
        :param principal_id: IAM身份中心中的一个实体身份唯一标识，例如用户或用户组
        :type principal_id: str
        :param principal_type: 实体类型
        :type principal_type: str
        :param target_id: 目标账户身份标识
        :type target_id: str
        :param target_type: 目标类型
        :type target_type: str
        """
        
        

        self._permission_set_id = None
        self._principal_id = None
        self._principal_type = None
        self._target_id = None
        self._target_type = None
        self.discriminator = None

        self.permission_set_id = permission_set_id
        self.principal_id = principal_id
        self.principal_type = principal_type
        self.target_id = target_id
        self.target_type = target_type

    @property
    def permission_set_id(self):
        """Gets the permission_set_id of this DeleteAccountAssignmentReqBody.

        权限集唯一标识

        :return: The permission_set_id of this DeleteAccountAssignmentReqBody.
        :rtype: str
        """
        return self._permission_set_id

    @permission_set_id.setter
    def permission_set_id(self, permission_set_id):
        """Sets the permission_set_id of this DeleteAccountAssignmentReqBody.

        权限集唯一标识

        :param permission_set_id: The permission_set_id of this DeleteAccountAssignmentReqBody.
        :type permission_set_id: str
        """
        self._permission_set_id = permission_set_id

    @property
    def principal_id(self):
        """Gets the principal_id of this DeleteAccountAssignmentReqBody.

        IAM身份中心中的一个实体身份唯一标识，例如用户或用户组

        :return: The principal_id of this DeleteAccountAssignmentReqBody.
        :rtype: str
        """
        return self._principal_id

    @principal_id.setter
    def principal_id(self, principal_id):
        """Sets the principal_id of this DeleteAccountAssignmentReqBody.

        IAM身份中心中的一个实体身份唯一标识，例如用户或用户组

        :param principal_id: The principal_id of this DeleteAccountAssignmentReqBody.
        :type principal_id: str
        """
        self._principal_id = principal_id

    @property
    def principal_type(self):
        """Gets the principal_type of this DeleteAccountAssignmentReqBody.

        实体类型

        :return: The principal_type of this DeleteAccountAssignmentReqBody.
        :rtype: str
        """
        return self._principal_type

    @principal_type.setter
    def principal_type(self, principal_type):
        """Sets the principal_type of this DeleteAccountAssignmentReqBody.

        实体类型

        :param principal_type: The principal_type of this DeleteAccountAssignmentReqBody.
        :type principal_type: str
        """
        self._principal_type = principal_type

    @property
    def target_id(self):
        """Gets the target_id of this DeleteAccountAssignmentReqBody.

        目标账户身份标识

        :return: The target_id of this DeleteAccountAssignmentReqBody.
        :rtype: str
        """
        return self._target_id

    @target_id.setter
    def target_id(self, target_id):
        """Sets the target_id of this DeleteAccountAssignmentReqBody.

        目标账户身份标识

        :param target_id: The target_id of this DeleteAccountAssignmentReqBody.
        :type target_id: str
        """
        self._target_id = target_id

    @property
    def target_type(self):
        """Gets the target_type of this DeleteAccountAssignmentReqBody.

        目标类型

        :return: The target_type of this DeleteAccountAssignmentReqBody.
        :rtype: str
        """
        return self._target_type

    @target_type.setter
    def target_type(self, target_type):
        """Sets the target_type of this DeleteAccountAssignmentReqBody.

        目标类型

        :param target_type: The target_type of this DeleteAccountAssignmentReqBody.
        :type target_type: str
        """
        self._target_type = target_type

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
        if not isinstance(other, DeleteAccountAssignmentReqBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
