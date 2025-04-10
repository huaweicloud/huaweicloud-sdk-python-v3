# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AccountAssignmentOperationStatusDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'created_date': 'int',
        'failure_reason': 'str',
        'permission_set_id': 'str',
        'principal_id': 'str',
        'principal_type': 'str',
        'request_id': 'str',
        'status': 'str',
        'target_id': 'str',
        'target_type': 'str'
    }

    attribute_map = {
        'created_date': 'created_date',
        'failure_reason': 'failure_reason',
        'permission_set_id': 'permission_set_id',
        'principal_id': 'principal_id',
        'principal_type': 'principal_type',
        'request_id': 'request_id',
        'status': 'status',
        'target_id': 'target_id',
        'target_type': 'target_type'
    }

    def __init__(self, created_date=None, failure_reason=None, permission_set_id=None, principal_id=None, principal_type=None, request_id=None, status=None, target_id=None, target_type=None):
        r"""AccountAssignmentOperationStatusDto

        The model defined in huaweicloud sdk

        :param created_date: 创建日期
        :type created_date: int
        :param failure_reason: 失败原因
        :type failure_reason: str
        :param permission_set_id: 权限集唯一标识
        :type permission_set_id: str
        :param principal_id: IAM身份中心中的一个实体身份唯一标识，例如用户或用户组
        :type principal_id: str
        :param principal_type: 操作的实体类型
        :type principal_type: str
        :param request_id: 请求唯一标识
        :type request_id: str
        :param status: 权限集授权状态
        :type status: str
        :param target_id: 目标实体的唯一标识
        :type target_id: str
        :param target_type: 实体类型
        :type target_type: str
        """
        
        

        self._created_date = None
        self._failure_reason = None
        self._permission_set_id = None
        self._principal_id = None
        self._principal_type = None
        self._request_id = None
        self._status = None
        self._target_id = None
        self._target_type = None
        self.discriminator = None

        if created_date is not None:
            self.created_date = created_date
        if failure_reason is not None:
            self.failure_reason = failure_reason
        if permission_set_id is not None:
            self.permission_set_id = permission_set_id
        if principal_id is not None:
            self.principal_id = principal_id
        if principal_type is not None:
            self.principal_type = principal_type
        if request_id is not None:
            self.request_id = request_id
        if status is not None:
            self.status = status
        if target_id is not None:
            self.target_id = target_id
        if target_type is not None:
            self.target_type = target_type

    @property
    def created_date(self):
        r"""Gets the created_date of this AccountAssignmentOperationStatusDto.

        创建日期

        :return: The created_date of this AccountAssignmentOperationStatusDto.
        :rtype: int
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        r"""Sets the created_date of this AccountAssignmentOperationStatusDto.

        创建日期

        :param created_date: The created_date of this AccountAssignmentOperationStatusDto.
        :type created_date: int
        """
        self._created_date = created_date

    @property
    def failure_reason(self):
        r"""Gets the failure_reason of this AccountAssignmentOperationStatusDto.

        失败原因

        :return: The failure_reason of this AccountAssignmentOperationStatusDto.
        :rtype: str
        """
        return self._failure_reason

    @failure_reason.setter
    def failure_reason(self, failure_reason):
        r"""Sets the failure_reason of this AccountAssignmentOperationStatusDto.

        失败原因

        :param failure_reason: The failure_reason of this AccountAssignmentOperationStatusDto.
        :type failure_reason: str
        """
        self._failure_reason = failure_reason

    @property
    def permission_set_id(self):
        r"""Gets the permission_set_id of this AccountAssignmentOperationStatusDto.

        权限集唯一标识

        :return: The permission_set_id of this AccountAssignmentOperationStatusDto.
        :rtype: str
        """
        return self._permission_set_id

    @permission_set_id.setter
    def permission_set_id(self, permission_set_id):
        r"""Sets the permission_set_id of this AccountAssignmentOperationStatusDto.

        权限集唯一标识

        :param permission_set_id: The permission_set_id of this AccountAssignmentOperationStatusDto.
        :type permission_set_id: str
        """
        self._permission_set_id = permission_set_id

    @property
    def principal_id(self):
        r"""Gets the principal_id of this AccountAssignmentOperationStatusDto.

        IAM身份中心中的一个实体身份唯一标识，例如用户或用户组

        :return: The principal_id of this AccountAssignmentOperationStatusDto.
        :rtype: str
        """
        return self._principal_id

    @principal_id.setter
    def principal_id(self, principal_id):
        r"""Sets the principal_id of this AccountAssignmentOperationStatusDto.

        IAM身份中心中的一个实体身份唯一标识，例如用户或用户组

        :param principal_id: The principal_id of this AccountAssignmentOperationStatusDto.
        :type principal_id: str
        """
        self._principal_id = principal_id

    @property
    def principal_type(self):
        r"""Gets the principal_type of this AccountAssignmentOperationStatusDto.

        操作的实体类型

        :return: The principal_type of this AccountAssignmentOperationStatusDto.
        :rtype: str
        """
        return self._principal_type

    @principal_type.setter
    def principal_type(self, principal_type):
        r"""Sets the principal_type of this AccountAssignmentOperationStatusDto.

        操作的实体类型

        :param principal_type: The principal_type of this AccountAssignmentOperationStatusDto.
        :type principal_type: str
        """
        self._principal_type = principal_type

    @property
    def request_id(self):
        r"""Gets the request_id of this AccountAssignmentOperationStatusDto.

        请求唯一标识

        :return: The request_id of this AccountAssignmentOperationStatusDto.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        r"""Sets the request_id of this AccountAssignmentOperationStatusDto.

        请求唯一标识

        :param request_id: The request_id of this AccountAssignmentOperationStatusDto.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def status(self):
        r"""Gets the status of this AccountAssignmentOperationStatusDto.

        权限集授权状态

        :return: The status of this AccountAssignmentOperationStatusDto.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this AccountAssignmentOperationStatusDto.

        权限集授权状态

        :param status: The status of this AccountAssignmentOperationStatusDto.
        :type status: str
        """
        self._status = status

    @property
    def target_id(self):
        r"""Gets the target_id of this AccountAssignmentOperationStatusDto.

        目标实体的唯一标识

        :return: The target_id of this AccountAssignmentOperationStatusDto.
        :rtype: str
        """
        return self._target_id

    @target_id.setter
    def target_id(self, target_id):
        r"""Sets the target_id of this AccountAssignmentOperationStatusDto.

        目标实体的唯一标识

        :param target_id: The target_id of this AccountAssignmentOperationStatusDto.
        :type target_id: str
        """
        self._target_id = target_id

    @property
    def target_type(self):
        r"""Gets the target_type of this AccountAssignmentOperationStatusDto.

        实体类型

        :return: The target_type of this AccountAssignmentOperationStatusDto.
        :rtype: str
        """
        return self._target_type

    @target_type.setter
    def target_type(self, target_type):
        r"""Sets the target_type of this AccountAssignmentOperationStatusDto.

        实体类型

        :param target_type: The target_type of this AccountAssignmentOperationStatusDto.
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
        if not isinstance(other, AccountAssignmentOperationStatusDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
