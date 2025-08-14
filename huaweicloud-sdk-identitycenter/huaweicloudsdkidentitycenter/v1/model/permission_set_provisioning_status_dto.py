# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PermissionSetProvisioningStatusDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'account_id': 'str',
        'created_date': 'str',
        'failure_reason': 'str',
        'permission_set_id': 'str',
        'request_id': 'str',
        'status': 'str'
    }

    attribute_map = {
        'account_id': 'account_id',
        'created_date': 'created_date',
        'failure_reason': 'failure_reason',
        'permission_set_id': 'permission_set_id',
        'request_id': 'request_id',
        'status': 'status'
    }

    def __init__(self, account_id=None, created_date=None, failure_reason=None, permission_set_id=None, request_id=None, status=None):
        r"""PermissionSetProvisioningStatusDto

        The model defined in huaweicloud sdk

        :param account_id: 指定账户的唯一身份标识.
        :type account_id: str
        :param created_date: 权限集创建日期
        :type created_date: str
        :param failure_reason: 失败原因
        :type failure_reason: str
        :param permission_set_id: 权限集唯一标识
        :type permission_set_id: str
        :param request_id: 请求唯一标识
        :type request_id: str
        :param status: 权限集授权状态
        :type status: str
        """
        
        

        self._account_id = None
        self._created_date = None
        self._failure_reason = None
        self._permission_set_id = None
        self._request_id = None
        self._status = None
        self.discriminator = None

        if account_id is not None:
            self.account_id = account_id
        if created_date is not None:
            self.created_date = created_date
        if failure_reason is not None:
            self.failure_reason = failure_reason
        if permission_set_id is not None:
            self.permission_set_id = permission_set_id
        if request_id is not None:
            self.request_id = request_id
        if status is not None:
            self.status = status

    @property
    def account_id(self):
        r"""Gets the account_id of this PermissionSetProvisioningStatusDto.

        指定账户的唯一身份标识.

        :return: The account_id of this PermissionSetProvisioningStatusDto.
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        r"""Sets the account_id of this PermissionSetProvisioningStatusDto.

        指定账户的唯一身份标识.

        :param account_id: The account_id of this PermissionSetProvisioningStatusDto.
        :type account_id: str
        """
        self._account_id = account_id

    @property
    def created_date(self):
        r"""Gets the created_date of this PermissionSetProvisioningStatusDto.

        权限集创建日期

        :return: The created_date of this PermissionSetProvisioningStatusDto.
        :rtype: str
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        r"""Sets the created_date of this PermissionSetProvisioningStatusDto.

        权限集创建日期

        :param created_date: The created_date of this PermissionSetProvisioningStatusDto.
        :type created_date: str
        """
        self._created_date = created_date

    @property
    def failure_reason(self):
        r"""Gets the failure_reason of this PermissionSetProvisioningStatusDto.

        失败原因

        :return: The failure_reason of this PermissionSetProvisioningStatusDto.
        :rtype: str
        """
        return self._failure_reason

    @failure_reason.setter
    def failure_reason(self, failure_reason):
        r"""Sets the failure_reason of this PermissionSetProvisioningStatusDto.

        失败原因

        :param failure_reason: The failure_reason of this PermissionSetProvisioningStatusDto.
        :type failure_reason: str
        """
        self._failure_reason = failure_reason

    @property
    def permission_set_id(self):
        r"""Gets the permission_set_id of this PermissionSetProvisioningStatusDto.

        权限集唯一标识

        :return: The permission_set_id of this PermissionSetProvisioningStatusDto.
        :rtype: str
        """
        return self._permission_set_id

    @permission_set_id.setter
    def permission_set_id(self, permission_set_id):
        r"""Sets the permission_set_id of this PermissionSetProvisioningStatusDto.

        权限集唯一标识

        :param permission_set_id: The permission_set_id of this PermissionSetProvisioningStatusDto.
        :type permission_set_id: str
        """
        self._permission_set_id = permission_set_id

    @property
    def request_id(self):
        r"""Gets the request_id of this PermissionSetProvisioningStatusDto.

        请求唯一标识

        :return: The request_id of this PermissionSetProvisioningStatusDto.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        r"""Sets the request_id of this PermissionSetProvisioningStatusDto.

        请求唯一标识

        :param request_id: The request_id of this PermissionSetProvisioningStatusDto.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def status(self):
        r"""Gets the status of this PermissionSetProvisioningStatusDto.

        权限集授权状态

        :return: The status of this PermissionSetProvisioningStatusDto.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this PermissionSetProvisioningStatusDto.

        权限集授权状态

        :param status: The status of this PermissionSetProvisioningStatusDto.
        :type status: str
        """
        self._status = status

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
        if not isinstance(other, PermissionSetProvisioningStatusDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
