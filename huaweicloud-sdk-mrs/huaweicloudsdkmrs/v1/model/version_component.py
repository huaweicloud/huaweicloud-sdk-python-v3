# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VersionComponent:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'other': 'dict(str, object)',
        'name': 'str',
        'version': 'str',
        'depend_on': 'list[str]',
        'description': 'str',
        'available_cluster_types': 'list[str]',
        'external_datasources': 'list[ComponentExternalDatasource]',
        'resource_requirement': 'list[str]',
        'valid_roles': 'list[str]',
        'visible': 'bool',
        'children_components': 'list[str]',
        'multi_az_support_status': 'str'
    }

    attribute_map = {
        'other': 'other',
        'name': 'name',
        'version': 'version',
        'depend_on': 'depend_on',
        'description': 'description',
        'available_cluster_types': 'available_cluster_types',
        'external_datasources': 'external_datasources',
        'resource_requirement': 'resource_requirement',
        'valid_roles': 'valid_roles',
        'visible': 'visible',
        'children_components': 'children_components',
        'multi_az_support_status': 'multi_az_support_status'
    }

    def __init__(self, other=None, name=None, version=None, depend_on=None, description=None, available_cluster_types=None, external_datasources=None, resource_requirement=None, valid_roles=None, visible=None, children_components=None, multi_az_support_status=None):
        r"""VersionComponent

        The model defined in huaweicloud sdk

        :param other: 其他
        :type other: dict(str, object)
        :param name: 组件名称
        :type name: str
        :param version: 支持版本
        :type version: str
        :param depend_on: 组件依赖项
        :type depend_on: list[str]
        :param description: 组件描述
        :type description: str
        :param available_cluster_types: 支持该组件的集群类型
        :type available_cluster_types: list[str]
        :param external_datasources: 外部数据源
        :type external_datasources: list[:class:`huaweicloudsdkmrs.v1.ComponentExternalDatasource`]
        :param resource_requirement: 所需的ip等资源说明
        :type resource_requirement: list[str]
        :param valid_roles: 有效角色
        :type valid_roles: list[str]
        :param visible: 是否可见
        :type visible: bool
        :param children_components: 子组件
        :type children_components: list[str]
        :param multi_az_support_status: 多az支持状态
        :type multi_az_support_status: str
        """
        
        

        self._other = None
        self._name = None
        self._version = None
        self._depend_on = None
        self._description = None
        self._available_cluster_types = None
        self._external_datasources = None
        self._resource_requirement = None
        self._valid_roles = None
        self._visible = None
        self._children_components = None
        self._multi_az_support_status = None
        self.discriminator = None

        if other is not None:
            self.other = other
        if name is not None:
            self.name = name
        if version is not None:
            self.version = version
        if depend_on is not None:
            self.depend_on = depend_on
        if description is not None:
            self.description = description
        if available_cluster_types is not None:
            self.available_cluster_types = available_cluster_types
        if external_datasources is not None:
            self.external_datasources = external_datasources
        if resource_requirement is not None:
            self.resource_requirement = resource_requirement
        if valid_roles is not None:
            self.valid_roles = valid_roles
        if visible is not None:
            self.visible = visible
        if children_components is not None:
            self.children_components = children_components
        if multi_az_support_status is not None:
            self.multi_az_support_status = multi_az_support_status

    @property
    def other(self):
        r"""Gets the other of this VersionComponent.

        其他

        :return: The other of this VersionComponent.
        :rtype: dict(str, object)
        """
        return self._other

    @other.setter
    def other(self, other):
        r"""Sets the other of this VersionComponent.

        其他

        :param other: The other of this VersionComponent.
        :type other: dict(str, object)
        """
        self._other = other

    @property
    def name(self):
        r"""Gets the name of this VersionComponent.

        组件名称

        :return: The name of this VersionComponent.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this VersionComponent.

        组件名称

        :param name: The name of this VersionComponent.
        :type name: str
        """
        self._name = name

    @property
    def version(self):
        r"""Gets the version of this VersionComponent.

        支持版本

        :return: The version of this VersionComponent.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this VersionComponent.

        支持版本

        :param version: The version of this VersionComponent.
        :type version: str
        """
        self._version = version

    @property
    def depend_on(self):
        r"""Gets the depend_on of this VersionComponent.

        组件依赖项

        :return: The depend_on of this VersionComponent.
        :rtype: list[str]
        """
        return self._depend_on

    @depend_on.setter
    def depend_on(self, depend_on):
        r"""Sets the depend_on of this VersionComponent.

        组件依赖项

        :param depend_on: The depend_on of this VersionComponent.
        :type depend_on: list[str]
        """
        self._depend_on = depend_on

    @property
    def description(self):
        r"""Gets the description of this VersionComponent.

        组件描述

        :return: The description of this VersionComponent.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this VersionComponent.

        组件描述

        :param description: The description of this VersionComponent.
        :type description: str
        """
        self._description = description

    @property
    def available_cluster_types(self):
        r"""Gets the available_cluster_types of this VersionComponent.

        支持该组件的集群类型

        :return: The available_cluster_types of this VersionComponent.
        :rtype: list[str]
        """
        return self._available_cluster_types

    @available_cluster_types.setter
    def available_cluster_types(self, available_cluster_types):
        r"""Sets the available_cluster_types of this VersionComponent.

        支持该组件的集群类型

        :param available_cluster_types: The available_cluster_types of this VersionComponent.
        :type available_cluster_types: list[str]
        """
        self._available_cluster_types = available_cluster_types

    @property
    def external_datasources(self):
        r"""Gets the external_datasources of this VersionComponent.

        外部数据源

        :return: The external_datasources of this VersionComponent.
        :rtype: list[:class:`huaweicloudsdkmrs.v1.ComponentExternalDatasource`]
        """
        return self._external_datasources

    @external_datasources.setter
    def external_datasources(self, external_datasources):
        r"""Sets the external_datasources of this VersionComponent.

        外部数据源

        :param external_datasources: The external_datasources of this VersionComponent.
        :type external_datasources: list[:class:`huaweicloudsdkmrs.v1.ComponentExternalDatasource`]
        """
        self._external_datasources = external_datasources

    @property
    def resource_requirement(self):
        r"""Gets the resource_requirement of this VersionComponent.

        所需的ip等资源说明

        :return: The resource_requirement of this VersionComponent.
        :rtype: list[str]
        """
        return self._resource_requirement

    @resource_requirement.setter
    def resource_requirement(self, resource_requirement):
        r"""Sets the resource_requirement of this VersionComponent.

        所需的ip等资源说明

        :param resource_requirement: The resource_requirement of this VersionComponent.
        :type resource_requirement: list[str]
        """
        self._resource_requirement = resource_requirement

    @property
    def valid_roles(self):
        r"""Gets the valid_roles of this VersionComponent.

        有效角色

        :return: The valid_roles of this VersionComponent.
        :rtype: list[str]
        """
        return self._valid_roles

    @valid_roles.setter
    def valid_roles(self, valid_roles):
        r"""Sets the valid_roles of this VersionComponent.

        有效角色

        :param valid_roles: The valid_roles of this VersionComponent.
        :type valid_roles: list[str]
        """
        self._valid_roles = valid_roles

    @property
    def visible(self):
        r"""Gets the visible of this VersionComponent.

        是否可见

        :return: The visible of this VersionComponent.
        :rtype: bool
        """
        return self._visible

    @visible.setter
    def visible(self, visible):
        r"""Sets the visible of this VersionComponent.

        是否可见

        :param visible: The visible of this VersionComponent.
        :type visible: bool
        """
        self._visible = visible

    @property
    def children_components(self):
        r"""Gets the children_components of this VersionComponent.

        子组件

        :return: The children_components of this VersionComponent.
        :rtype: list[str]
        """
        return self._children_components

    @children_components.setter
    def children_components(self, children_components):
        r"""Sets the children_components of this VersionComponent.

        子组件

        :param children_components: The children_components of this VersionComponent.
        :type children_components: list[str]
        """
        self._children_components = children_components

    @property
    def multi_az_support_status(self):
        r"""Gets the multi_az_support_status of this VersionComponent.

        多az支持状态

        :return: The multi_az_support_status of this VersionComponent.
        :rtype: str
        """
        return self._multi_az_support_status

    @multi_az_support_status.setter
    def multi_az_support_status(self, multi_az_support_status):
        r"""Sets the multi_az_support_status of this VersionComponent.

        多az支持状态

        :param multi_az_support_status: The multi_az_support_status of this VersionComponent.
        :type multi_az_support_status: str
        """
        self._multi_az_support_status = multi_az_support_status

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
        if not isinstance(other, VersionComponent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
