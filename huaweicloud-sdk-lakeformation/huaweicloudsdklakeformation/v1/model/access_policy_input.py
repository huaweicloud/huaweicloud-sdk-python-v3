# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AccessPolicyInput:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'principal_list': 'list[Principal]',
        'resource': 'ResourceInfo',
        'effect': 'bool',
        'permissions': 'list[str]',
        'grant_able_permissions': 'list[str]',
        'conditions': 'str',
        'data_filter': 'str',
        'data_mask': 'str'
    }

    attribute_map = {
        'principal_list': 'principal_list',
        'resource': 'resource',
        'effect': 'effect',
        'permissions': 'permissions',
        'grant_able_permissions': 'grant_able_permissions',
        'conditions': 'conditions',
        'data_filter': 'data_filter',
        'data_mask': 'data_mask'
    }

    def __init__(self, principal_list=None, resource=None, effect=None, permissions=None, grant_able_permissions=None, conditions=None, data_filter=None, data_mask=None):
        """AccessPolicyInput

        The model defined in huaweicloud sdk

        :param principal_list: 主体信息
        :type principal_list: list[:class:`huaweicloudsdklakeformation.v1.Principal`]
        :param resource: 
        :type resource: :class:`huaweicloudsdklakeformation.v1.ResourceInfo`
        :param effect: 拒绝/允许
        :type effect: bool
        :param permissions: 权限列表
        :type permissions: list[str]
        :param grant_able_permissions: 可传递的权限列表
        :type grant_able_permissions: list[str]
        :param conditions: 条件
        :type conditions: str
        :param data_filter: 行过滤
        :type data_filter: str
        :param data_mask: 列掩码
        :type data_mask: str
        """
        
        

        self._principal_list = None
        self._resource = None
        self._effect = None
        self._permissions = None
        self._grant_able_permissions = None
        self._conditions = None
        self._data_filter = None
        self._data_mask = None
        self.discriminator = None

        self.principal_list = principal_list
        self.resource = resource
        self.effect = effect
        self.permissions = permissions
        if grant_able_permissions is not None:
            self.grant_able_permissions = grant_able_permissions
        if conditions is not None:
            self.conditions = conditions
        if data_filter is not None:
            self.data_filter = data_filter
        if data_mask is not None:
            self.data_mask = data_mask

    @property
    def principal_list(self):
        """Gets the principal_list of this AccessPolicyInput.

        主体信息

        :return: The principal_list of this AccessPolicyInput.
        :rtype: list[:class:`huaweicloudsdklakeformation.v1.Principal`]
        """
        return self._principal_list

    @principal_list.setter
    def principal_list(self, principal_list):
        """Sets the principal_list of this AccessPolicyInput.

        主体信息

        :param principal_list: The principal_list of this AccessPolicyInput.
        :type principal_list: list[:class:`huaweicloudsdklakeformation.v1.Principal`]
        """
        self._principal_list = principal_list

    @property
    def resource(self):
        """Gets the resource of this AccessPolicyInput.

        :return: The resource of this AccessPolicyInput.
        :rtype: :class:`huaweicloudsdklakeformation.v1.ResourceInfo`
        """
        return self._resource

    @resource.setter
    def resource(self, resource):
        """Sets the resource of this AccessPolicyInput.

        :param resource: The resource of this AccessPolicyInput.
        :type resource: :class:`huaweicloudsdklakeformation.v1.ResourceInfo`
        """
        self._resource = resource

    @property
    def effect(self):
        """Gets the effect of this AccessPolicyInput.

        拒绝/允许

        :return: The effect of this AccessPolicyInput.
        :rtype: bool
        """
        return self._effect

    @effect.setter
    def effect(self, effect):
        """Sets the effect of this AccessPolicyInput.

        拒绝/允许

        :param effect: The effect of this AccessPolicyInput.
        :type effect: bool
        """
        self._effect = effect

    @property
    def permissions(self):
        """Gets the permissions of this AccessPolicyInput.

        权限列表

        :return: The permissions of this AccessPolicyInput.
        :rtype: list[str]
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        """Sets the permissions of this AccessPolicyInput.

        权限列表

        :param permissions: The permissions of this AccessPolicyInput.
        :type permissions: list[str]
        """
        self._permissions = permissions

    @property
    def grant_able_permissions(self):
        """Gets the grant_able_permissions of this AccessPolicyInput.

        可传递的权限列表

        :return: The grant_able_permissions of this AccessPolicyInput.
        :rtype: list[str]
        """
        return self._grant_able_permissions

    @grant_able_permissions.setter
    def grant_able_permissions(self, grant_able_permissions):
        """Sets the grant_able_permissions of this AccessPolicyInput.

        可传递的权限列表

        :param grant_able_permissions: The grant_able_permissions of this AccessPolicyInput.
        :type grant_able_permissions: list[str]
        """
        self._grant_able_permissions = grant_able_permissions

    @property
    def conditions(self):
        """Gets the conditions of this AccessPolicyInput.

        条件

        :return: The conditions of this AccessPolicyInput.
        :rtype: str
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        """Sets the conditions of this AccessPolicyInput.

        条件

        :param conditions: The conditions of this AccessPolicyInput.
        :type conditions: str
        """
        self._conditions = conditions

    @property
    def data_filter(self):
        """Gets the data_filter of this AccessPolicyInput.

        行过滤

        :return: The data_filter of this AccessPolicyInput.
        :rtype: str
        """
        return self._data_filter

    @data_filter.setter
    def data_filter(self, data_filter):
        """Sets the data_filter of this AccessPolicyInput.

        行过滤

        :param data_filter: The data_filter of this AccessPolicyInput.
        :type data_filter: str
        """
        self._data_filter = data_filter

    @property
    def data_mask(self):
        """Gets the data_mask of this AccessPolicyInput.

        列掩码

        :return: The data_mask of this AccessPolicyInput.
        :rtype: str
        """
        return self._data_mask

    @data_mask.setter
    def data_mask(self, data_mask):
        """Sets the data_mask of this AccessPolicyInput.

        列掩码

        :param data_mask: The data_mask of this AccessPolicyInput.
        :type data_mask: str
        """
        self._data_mask = data_mask

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
        if not isinstance(other, AccessPolicyInput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
