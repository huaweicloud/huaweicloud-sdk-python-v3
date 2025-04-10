# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowMrsVersionMetadataResponse(SdkResponse):

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
        'template_type': 'str',
        'image_id': 'str',
        'status': 'str',
        'features': 'list[str]',
        'cluster_types': 'list[str]',
        'version_type': 'str',
        'components': 'list[VersionComponent]',
        'resource_requirement': 'list[str]',
        'constraints': 'VersionConstraint',
        'flavors': 'FlavorLists',
        'role_deploy_meta': 'list[RoleDeployMeta]'
    }

    attribute_map = {
        'other': 'other',
        'name': 'name',
        'template_type': 'template_type',
        'image_id': 'image_id',
        'status': 'status',
        'features': 'features',
        'cluster_types': 'cluster_types',
        'version_type': 'version_type',
        'components': 'components',
        'resource_requirement': 'resource_requirement',
        'constraints': 'constraints',
        'flavors': 'flavors',
        'role_deploy_meta': 'role_deploy_meta'
    }

    def __init__(self, other=None, name=None, template_type=None, image_id=None, status=None, features=None, cluster_types=None, version_type=None, components=None, resource_requirement=None, constraints=None, flavors=None, role_deploy_meta=None):
        r"""ShowMrsVersionMetadataResponse

        The model defined in huaweicloud sdk

        :param other: 其他
        :type other: dict(str, object)
        :param name: 镜像版本名称
        :type name: str
        :param template_type: 模板类型
        :type template_type: str
        :param image_id: 镜像ID
        :type image_id: str
        :param status: 版本状态
        :type status: str
        :param features: 特性列表
        :type features: list[str]
        :param cluster_types: 集群类型列表
        :type cluster_types: list[str]
        :param version_type: 版本类型
        :type version_type: str
        :param components: 组件列表
        :type components: list[:class:`huaweicloudsdkmrs.v1.VersionComponent`]
        :param resource_requirement: 版本所需的ip等资源说明
        :type resource_requirement: list[str]
        :param constraints: 
        :type constraints: :class:`huaweicloudsdkmrs.v1.VersionConstraint`
        :param flavors: 
        :type flavors: :class:`huaweicloudsdkmrs.v1.FlavorLists`
        :param role_deploy_meta: 版本组件实例角色部署策略
        :type role_deploy_meta: list[:class:`huaweicloudsdkmrs.v1.RoleDeployMeta`]
        """
        
        super(ShowMrsVersionMetadataResponse, self).__init__()

        self._other = None
        self._name = None
        self._template_type = None
        self._image_id = None
        self._status = None
        self._features = None
        self._cluster_types = None
        self._version_type = None
        self._components = None
        self._resource_requirement = None
        self._constraints = None
        self._flavors = None
        self._role_deploy_meta = None
        self.discriminator = None

        if other is not None:
            self.other = other
        if name is not None:
            self.name = name
        if template_type is not None:
            self.template_type = template_type
        if image_id is not None:
            self.image_id = image_id
        if status is not None:
            self.status = status
        if features is not None:
            self.features = features
        if cluster_types is not None:
            self.cluster_types = cluster_types
        if version_type is not None:
            self.version_type = version_type
        if components is not None:
            self.components = components
        if resource_requirement is not None:
            self.resource_requirement = resource_requirement
        if constraints is not None:
            self.constraints = constraints
        if flavors is not None:
            self.flavors = flavors
        if role_deploy_meta is not None:
            self.role_deploy_meta = role_deploy_meta

    @property
    def other(self):
        r"""Gets the other of this ShowMrsVersionMetadataResponse.

        其他

        :return: The other of this ShowMrsVersionMetadataResponse.
        :rtype: dict(str, object)
        """
        return self._other

    @other.setter
    def other(self, other):
        r"""Sets the other of this ShowMrsVersionMetadataResponse.

        其他

        :param other: The other of this ShowMrsVersionMetadataResponse.
        :type other: dict(str, object)
        """
        self._other = other

    @property
    def name(self):
        r"""Gets the name of this ShowMrsVersionMetadataResponse.

        镜像版本名称

        :return: The name of this ShowMrsVersionMetadataResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ShowMrsVersionMetadataResponse.

        镜像版本名称

        :param name: The name of this ShowMrsVersionMetadataResponse.
        :type name: str
        """
        self._name = name

    @property
    def template_type(self):
        r"""Gets the template_type of this ShowMrsVersionMetadataResponse.

        模板类型

        :return: The template_type of this ShowMrsVersionMetadataResponse.
        :rtype: str
        """
        return self._template_type

    @template_type.setter
    def template_type(self, template_type):
        r"""Sets the template_type of this ShowMrsVersionMetadataResponse.

        模板类型

        :param template_type: The template_type of this ShowMrsVersionMetadataResponse.
        :type template_type: str
        """
        self._template_type = template_type

    @property
    def image_id(self):
        r"""Gets the image_id of this ShowMrsVersionMetadataResponse.

        镜像ID

        :return: The image_id of this ShowMrsVersionMetadataResponse.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        r"""Sets the image_id of this ShowMrsVersionMetadataResponse.

        镜像ID

        :param image_id: The image_id of this ShowMrsVersionMetadataResponse.
        :type image_id: str
        """
        self._image_id = image_id

    @property
    def status(self):
        r"""Gets the status of this ShowMrsVersionMetadataResponse.

        版本状态

        :return: The status of this ShowMrsVersionMetadataResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ShowMrsVersionMetadataResponse.

        版本状态

        :param status: The status of this ShowMrsVersionMetadataResponse.
        :type status: str
        """
        self._status = status

    @property
    def features(self):
        r"""Gets the features of this ShowMrsVersionMetadataResponse.

        特性列表

        :return: The features of this ShowMrsVersionMetadataResponse.
        :rtype: list[str]
        """
        return self._features

    @features.setter
    def features(self, features):
        r"""Sets the features of this ShowMrsVersionMetadataResponse.

        特性列表

        :param features: The features of this ShowMrsVersionMetadataResponse.
        :type features: list[str]
        """
        self._features = features

    @property
    def cluster_types(self):
        r"""Gets the cluster_types of this ShowMrsVersionMetadataResponse.

        集群类型列表

        :return: The cluster_types of this ShowMrsVersionMetadataResponse.
        :rtype: list[str]
        """
        return self._cluster_types

    @cluster_types.setter
    def cluster_types(self, cluster_types):
        r"""Sets the cluster_types of this ShowMrsVersionMetadataResponse.

        集群类型列表

        :param cluster_types: The cluster_types of this ShowMrsVersionMetadataResponse.
        :type cluster_types: list[str]
        """
        self._cluster_types = cluster_types

    @property
    def version_type(self):
        r"""Gets the version_type of this ShowMrsVersionMetadataResponse.

        版本类型

        :return: The version_type of this ShowMrsVersionMetadataResponse.
        :rtype: str
        """
        return self._version_type

    @version_type.setter
    def version_type(self, version_type):
        r"""Sets the version_type of this ShowMrsVersionMetadataResponse.

        版本类型

        :param version_type: The version_type of this ShowMrsVersionMetadataResponse.
        :type version_type: str
        """
        self._version_type = version_type

    @property
    def components(self):
        r"""Gets the components of this ShowMrsVersionMetadataResponse.

        组件列表

        :return: The components of this ShowMrsVersionMetadataResponse.
        :rtype: list[:class:`huaweicloudsdkmrs.v1.VersionComponent`]
        """
        return self._components

    @components.setter
    def components(self, components):
        r"""Sets the components of this ShowMrsVersionMetadataResponse.

        组件列表

        :param components: The components of this ShowMrsVersionMetadataResponse.
        :type components: list[:class:`huaweicloudsdkmrs.v1.VersionComponent`]
        """
        self._components = components

    @property
    def resource_requirement(self):
        r"""Gets the resource_requirement of this ShowMrsVersionMetadataResponse.

        版本所需的ip等资源说明

        :return: The resource_requirement of this ShowMrsVersionMetadataResponse.
        :rtype: list[str]
        """
        return self._resource_requirement

    @resource_requirement.setter
    def resource_requirement(self, resource_requirement):
        r"""Sets the resource_requirement of this ShowMrsVersionMetadataResponse.

        版本所需的ip等资源说明

        :param resource_requirement: The resource_requirement of this ShowMrsVersionMetadataResponse.
        :type resource_requirement: list[str]
        """
        self._resource_requirement = resource_requirement

    @property
    def constraints(self):
        r"""Gets the constraints of this ShowMrsVersionMetadataResponse.

        :return: The constraints of this ShowMrsVersionMetadataResponse.
        :rtype: :class:`huaweicloudsdkmrs.v1.VersionConstraint`
        """
        return self._constraints

    @constraints.setter
    def constraints(self, constraints):
        r"""Sets the constraints of this ShowMrsVersionMetadataResponse.

        :param constraints: The constraints of this ShowMrsVersionMetadataResponse.
        :type constraints: :class:`huaweicloudsdkmrs.v1.VersionConstraint`
        """
        self._constraints = constraints

    @property
    def flavors(self):
        r"""Gets the flavors of this ShowMrsVersionMetadataResponse.

        :return: The flavors of this ShowMrsVersionMetadataResponse.
        :rtype: :class:`huaweicloudsdkmrs.v1.FlavorLists`
        """
        return self._flavors

    @flavors.setter
    def flavors(self, flavors):
        r"""Sets the flavors of this ShowMrsVersionMetadataResponse.

        :param flavors: The flavors of this ShowMrsVersionMetadataResponse.
        :type flavors: :class:`huaweicloudsdkmrs.v1.FlavorLists`
        """
        self._flavors = flavors

    @property
    def role_deploy_meta(self):
        r"""Gets the role_deploy_meta of this ShowMrsVersionMetadataResponse.

        版本组件实例角色部署策略

        :return: The role_deploy_meta of this ShowMrsVersionMetadataResponse.
        :rtype: list[:class:`huaweicloudsdkmrs.v1.RoleDeployMeta`]
        """
        return self._role_deploy_meta

    @role_deploy_meta.setter
    def role_deploy_meta(self, role_deploy_meta):
        r"""Sets the role_deploy_meta of this ShowMrsVersionMetadataResponse.

        版本组件实例角色部署策略

        :param role_deploy_meta: The role_deploy_meta of this ShowMrsVersionMetadataResponse.
        :type role_deploy_meta: list[:class:`huaweicloudsdkmrs.v1.RoleDeployMeta`]
        """
        self._role_deploy_meta = role_deploy_meta

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
        if not isinstance(other, ShowMrsVersionMetadataResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
