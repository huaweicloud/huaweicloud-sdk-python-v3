# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSecurityResourcePermissionsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'workspace': 'str',
        'limit': 'int',
        'offset': 'int',
        'policy_name': 'str',
        'resource_name': 'str',
        'member_name': 'str',
        'order_by': 'str',
        'order_by_asc': 'bool'
    }

    attribute_map = {
        'workspace': 'workspace',
        'limit': 'limit',
        'offset': 'offset',
        'policy_name': 'policy_name',
        'resource_name': 'resource_name',
        'member_name': 'member_name',
        'order_by': 'order_by',
        'order_by_asc': 'order_by_asc'
    }

    def __init__(self, workspace=None, limit=None, offset=None, policy_name=None, resource_name=None, member_name=None, order_by=None, order_by_asc=None):
        r"""ListSecurityResourcePermissionsRequest

        The model defined in huaweicloud sdk

        :param workspace: DataArts Studio工作空间ID
        :type workspace: str
        :param limit: limit
        :type limit: int
        :param offset: offset
        :type offset: int
        :param policy_name: 策略名称。
        :type policy_name: str
        :param resource_name: 授权资源名称。
        :type resource_name: str
        :param member_name: 成员名称
        :type member_name: str
        :param order_by: 排序参数, NAME,UPDATE_TIME。
        :type order_by: str
        :param order_by_asc: 是否升序（仅指定排序参数时有效）
        :type order_by_asc: bool
        """
        
        

        self._workspace = None
        self._limit = None
        self._offset = None
        self._policy_name = None
        self._resource_name = None
        self._member_name = None
        self._order_by = None
        self._order_by_asc = None
        self.discriminator = None

        self.workspace = workspace
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if policy_name is not None:
            self.policy_name = policy_name
        if resource_name is not None:
            self.resource_name = resource_name
        if member_name is not None:
            self.member_name = member_name
        if order_by is not None:
            self.order_by = order_by
        if order_by_asc is not None:
            self.order_by_asc = order_by_asc

    @property
    def workspace(self):
        r"""Gets the workspace of this ListSecurityResourcePermissionsRequest.

        DataArts Studio工作空间ID

        :return: The workspace of this ListSecurityResourcePermissionsRequest.
        :rtype: str
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        r"""Sets the workspace of this ListSecurityResourcePermissionsRequest.

        DataArts Studio工作空间ID

        :param workspace: The workspace of this ListSecurityResourcePermissionsRequest.
        :type workspace: str
        """
        self._workspace = workspace

    @property
    def limit(self):
        r"""Gets the limit of this ListSecurityResourcePermissionsRequest.

        limit

        :return: The limit of this ListSecurityResourcePermissionsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListSecurityResourcePermissionsRequest.

        limit

        :param limit: The limit of this ListSecurityResourcePermissionsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListSecurityResourcePermissionsRequest.

        offset

        :return: The offset of this ListSecurityResourcePermissionsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListSecurityResourcePermissionsRequest.

        offset

        :param offset: The offset of this ListSecurityResourcePermissionsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def policy_name(self):
        r"""Gets the policy_name of this ListSecurityResourcePermissionsRequest.

        策略名称。

        :return: The policy_name of this ListSecurityResourcePermissionsRequest.
        :rtype: str
        """
        return self._policy_name

    @policy_name.setter
    def policy_name(self, policy_name):
        r"""Sets the policy_name of this ListSecurityResourcePermissionsRequest.

        策略名称。

        :param policy_name: The policy_name of this ListSecurityResourcePermissionsRequest.
        :type policy_name: str
        """
        self._policy_name = policy_name

    @property
    def resource_name(self):
        r"""Gets the resource_name of this ListSecurityResourcePermissionsRequest.

        授权资源名称。

        :return: The resource_name of this ListSecurityResourcePermissionsRequest.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        r"""Sets the resource_name of this ListSecurityResourcePermissionsRequest.

        授权资源名称。

        :param resource_name: The resource_name of this ListSecurityResourcePermissionsRequest.
        :type resource_name: str
        """
        self._resource_name = resource_name

    @property
    def member_name(self):
        r"""Gets the member_name of this ListSecurityResourcePermissionsRequest.

        成员名称

        :return: The member_name of this ListSecurityResourcePermissionsRequest.
        :rtype: str
        """
        return self._member_name

    @member_name.setter
    def member_name(self, member_name):
        r"""Sets the member_name of this ListSecurityResourcePermissionsRequest.

        成员名称

        :param member_name: The member_name of this ListSecurityResourcePermissionsRequest.
        :type member_name: str
        """
        self._member_name = member_name

    @property
    def order_by(self):
        r"""Gets the order_by of this ListSecurityResourcePermissionsRequest.

        排序参数, NAME,UPDATE_TIME。

        :return: The order_by of this ListSecurityResourcePermissionsRequest.
        :rtype: str
        """
        return self._order_by

    @order_by.setter
    def order_by(self, order_by):
        r"""Sets the order_by of this ListSecurityResourcePermissionsRequest.

        排序参数, NAME,UPDATE_TIME。

        :param order_by: The order_by of this ListSecurityResourcePermissionsRequest.
        :type order_by: str
        """
        self._order_by = order_by

    @property
    def order_by_asc(self):
        r"""Gets the order_by_asc of this ListSecurityResourcePermissionsRequest.

        是否升序（仅指定排序参数时有效）

        :return: The order_by_asc of this ListSecurityResourcePermissionsRequest.
        :rtype: bool
        """
        return self._order_by_asc

    @order_by_asc.setter
    def order_by_asc(self, order_by_asc):
        r"""Sets the order_by_asc of this ListSecurityResourcePermissionsRequest.

        是否升序（仅指定排序参数时有效）

        :param order_by_asc: The order_by_asc of this ListSecurityResourcePermissionsRequest.
        :type order_by_asc: bool
        """
        self._order_by_asc = order_by_asc

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
        if not isinstance(other, ListSecurityResourcePermissionsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
