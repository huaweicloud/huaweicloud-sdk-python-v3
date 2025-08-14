# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAccountsForProvisionedPermissionSetRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []
    sensitive_list.append('x_security_token')

    openapi_types = {
        'x_security_token': 'str',
        'instance_id': 'str',
        'permission_set_id': 'str',
        'limit': 'int',
        'marker': 'str',
        'provisioning_status': 'str'
    }

    attribute_map = {
        'x_security_token': 'X-Security-Token',
        'instance_id': 'instance_id',
        'permission_set_id': 'permission_set_id',
        'limit': 'limit',
        'marker': 'marker',
        'provisioning_status': 'provisioning_status'
    }

    def __init__(self, x_security_token=None, instance_id=None, permission_set_id=None, limit=None, marker=None, provisioning_status=None):
        r"""ListAccountsForProvisionedPermissionSetRequest

        The model defined in huaweicloud sdk

        :param x_security_token: 如果正在使用临时安全凭据，则此header是必需的，该值是临时安全凭据的安全令牌（会话令牌）。
        :type x_security_token: str
        :param instance_id: IAM Identity Center实例的全局唯一标识符（ID）
        :type instance_id: str
        :param permission_set_id: 权限集的全局唯一标识符（ID）
        :type permission_set_id: str
        :param limit: 每个请求返回的最大结果数。
        :type limit: int
        :param marker: 分页标记
        :type marker: str
        :param provisioning_status: 权限集分配状态。
        :type provisioning_status: str
        """
        
        

        self._x_security_token = None
        self._instance_id = None
        self._permission_set_id = None
        self._limit = None
        self._marker = None
        self._provisioning_status = None
        self.discriminator = None

        if x_security_token is not None:
            self.x_security_token = x_security_token
        self.instance_id = instance_id
        self.permission_set_id = permission_set_id
        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if provisioning_status is not None:
            self.provisioning_status = provisioning_status

    @property
    def x_security_token(self):
        r"""Gets the x_security_token of this ListAccountsForProvisionedPermissionSetRequest.

        如果正在使用临时安全凭据，则此header是必需的，该值是临时安全凭据的安全令牌（会话令牌）。

        :return: The x_security_token of this ListAccountsForProvisionedPermissionSetRequest.
        :rtype: str
        """
        return self._x_security_token

    @x_security_token.setter
    def x_security_token(self, x_security_token):
        r"""Sets the x_security_token of this ListAccountsForProvisionedPermissionSetRequest.

        如果正在使用临时安全凭据，则此header是必需的，该值是临时安全凭据的安全令牌（会话令牌）。

        :param x_security_token: The x_security_token of this ListAccountsForProvisionedPermissionSetRequest.
        :type x_security_token: str
        """
        self._x_security_token = x_security_token

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ListAccountsForProvisionedPermissionSetRequest.

        IAM Identity Center实例的全局唯一标识符（ID）

        :return: The instance_id of this ListAccountsForProvisionedPermissionSetRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ListAccountsForProvisionedPermissionSetRequest.

        IAM Identity Center实例的全局唯一标识符（ID）

        :param instance_id: The instance_id of this ListAccountsForProvisionedPermissionSetRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def permission_set_id(self):
        r"""Gets the permission_set_id of this ListAccountsForProvisionedPermissionSetRequest.

        权限集的全局唯一标识符（ID）

        :return: The permission_set_id of this ListAccountsForProvisionedPermissionSetRequest.
        :rtype: str
        """
        return self._permission_set_id

    @permission_set_id.setter
    def permission_set_id(self, permission_set_id):
        r"""Sets the permission_set_id of this ListAccountsForProvisionedPermissionSetRequest.

        权限集的全局唯一标识符（ID）

        :param permission_set_id: The permission_set_id of this ListAccountsForProvisionedPermissionSetRequest.
        :type permission_set_id: str
        """
        self._permission_set_id = permission_set_id

    @property
    def limit(self):
        r"""Gets the limit of this ListAccountsForProvisionedPermissionSetRequest.

        每个请求返回的最大结果数。

        :return: The limit of this ListAccountsForProvisionedPermissionSetRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListAccountsForProvisionedPermissionSetRequest.

        每个请求返回的最大结果数。

        :param limit: The limit of this ListAccountsForProvisionedPermissionSetRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        r"""Gets the marker of this ListAccountsForProvisionedPermissionSetRequest.

        分页标记

        :return: The marker of this ListAccountsForProvisionedPermissionSetRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListAccountsForProvisionedPermissionSetRequest.

        分页标记

        :param marker: The marker of this ListAccountsForProvisionedPermissionSetRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def provisioning_status(self):
        r"""Gets the provisioning_status of this ListAccountsForProvisionedPermissionSetRequest.

        权限集分配状态。

        :return: The provisioning_status of this ListAccountsForProvisionedPermissionSetRequest.
        :rtype: str
        """
        return self._provisioning_status

    @provisioning_status.setter
    def provisioning_status(self, provisioning_status):
        r"""Sets the provisioning_status of this ListAccountsForProvisionedPermissionSetRequest.

        权限集分配状态。

        :param provisioning_status: The provisioning_status of this ListAccountsForProvisionedPermissionSetRequest.
        :type provisioning_status: str
        """
        self._provisioning_status = provisioning_status

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
        if not isinstance(other, ListAccountsForProvisionedPermissionSetRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
