# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LakeFormationPolicy:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'project_id': 'str',
        'instance_id': 'str',
        'principal_type': 'str',
        'principal_source': 'str',
        'principal_name': 'str',
        'resource': 'ResourceInfo',
        'resource_name': 'str',
        'permissions': 'list[str]',
        'grant_able_permissions': 'list[str]',
        'created_time': 'int',
        'condition': 'str',
        'obligation': 'str',
        'authorization_paths': 'list[str]'
    }

    attribute_map = {
        'project_id': 'project_id',
        'instance_id': 'instance_id',
        'principal_type': 'principal_type',
        'principal_source': 'principal_source',
        'principal_name': 'principal_name',
        'resource': 'resource',
        'resource_name': 'resource_name',
        'permissions': 'permissions',
        'grant_able_permissions': 'grant_able_permissions',
        'created_time': 'created_time',
        'condition': 'condition',
        'obligation': 'obligation',
        'authorization_paths': 'authorization_paths'
    }

    def __init__(self, project_id=None, instance_id=None, principal_type=None, principal_source=None, principal_name=None, resource=None, resource_name=None, permissions=None, grant_able_permissions=None, created_time=None, condition=None, obligation=None, authorization_paths=None):
        r"""LakeFormationPolicy

        The model defined in huaweicloud sdk

        :param project_id: 项目id
        :type project_id: str
        :param instance_id: 实例id
        :type instance_id: str
        :param principal_type: 主体类型，USER-用户,GROUP-组,ROLE-角色,SHARE-共享,OTHER-其它
        :type principal_type: str
        :param principal_source: 主体来源，IAM-云,SAML-联邦,LDAP-权限策略,LOCAL-本地,OTHER-其它
        :type principal_source: str
        :param principal_name: 主体名
        :type principal_name: str
        :param resource: 
        :type resource: :class:`huaweicloudsdklakeformation.v1.ResourceInfo`
        :param resource_name: 要求用点分格式进行分割
        :type resource_name: str
        :param permissions: 权限列表
        :type permissions: list[str]
        :param grant_able_permissions: 可以传递的权限列表
        :type grant_able_permissions: list[str]
        :param created_time: 创建时间
        :type created_time: int
        :param condition: 条件信息
        :type condition: str
        :param obligation: obligation，义务，当前包含data filter和data mask
        :type obligation: str
        :param authorization_paths: 授权路径列表
        :type authorization_paths: list[str]
        """
        
        

        self._project_id = None
        self._instance_id = None
        self._principal_type = None
        self._principal_source = None
        self._principal_name = None
        self._resource = None
        self._resource_name = None
        self._permissions = None
        self._grant_able_permissions = None
        self._created_time = None
        self._condition = None
        self._obligation = None
        self._authorization_paths = None
        self.discriminator = None

        self.project_id = project_id
        if instance_id is not None:
            self.instance_id = instance_id
        self.principal_type = principal_type
        self.principal_source = principal_source
        self.principal_name = principal_name
        if resource is not None:
            self.resource = resource
        self.resource_name = resource_name
        self.permissions = permissions
        if grant_able_permissions is not None:
            self.grant_able_permissions = grant_able_permissions
        self.created_time = created_time
        if condition is not None:
            self.condition = condition
        if obligation is not None:
            self.obligation = obligation
        if authorization_paths is not None:
            self.authorization_paths = authorization_paths

    @property
    def project_id(self):
        r"""Gets the project_id of this LakeFormationPolicy.

        项目id

        :return: The project_id of this LakeFormationPolicy.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this LakeFormationPolicy.

        项目id

        :param project_id: The project_id of this LakeFormationPolicy.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def instance_id(self):
        r"""Gets the instance_id of this LakeFormationPolicy.

        实例id

        :return: The instance_id of this LakeFormationPolicy.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this LakeFormationPolicy.

        实例id

        :param instance_id: The instance_id of this LakeFormationPolicy.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def principal_type(self):
        r"""Gets the principal_type of this LakeFormationPolicy.

        主体类型，USER-用户,GROUP-组,ROLE-角色,SHARE-共享,OTHER-其它

        :return: The principal_type of this LakeFormationPolicy.
        :rtype: str
        """
        return self._principal_type

    @principal_type.setter
    def principal_type(self, principal_type):
        r"""Sets the principal_type of this LakeFormationPolicy.

        主体类型，USER-用户,GROUP-组,ROLE-角色,SHARE-共享,OTHER-其它

        :param principal_type: The principal_type of this LakeFormationPolicy.
        :type principal_type: str
        """
        self._principal_type = principal_type

    @property
    def principal_source(self):
        r"""Gets the principal_source of this LakeFormationPolicy.

        主体来源，IAM-云,SAML-联邦,LDAP-权限策略,LOCAL-本地,OTHER-其它

        :return: The principal_source of this LakeFormationPolicy.
        :rtype: str
        """
        return self._principal_source

    @principal_source.setter
    def principal_source(self, principal_source):
        r"""Sets the principal_source of this LakeFormationPolicy.

        主体来源，IAM-云,SAML-联邦,LDAP-权限策略,LOCAL-本地,OTHER-其它

        :param principal_source: The principal_source of this LakeFormationPolicy.
        :type principal_source: str
        """
        self._principal_source = principal_source

    @property
    def principal_name(self):
        r"""Gets the principal_name of this LakeFormationPolicy.

        主体名

        :return: The principal_name of this LakeFormationPolicy.
        :rtype: str
        """
        return self._principal_name

    @principal_name.setter
    def principal_name(self, principal_name):
        r"""Sets the principal_name of this LakeFormationPolicy.

        主体名

        :param principal_name: The principal_name of this LakeFormationPolicy.
        :type principal_name: str
        """
        self._principal_name = principal_name

    @property
    def resource(self):
        r"""Gets the resource of this LakeFormationPolicy.

        :return: The resource of this LakeFormationPolicy.
        :rtype: :class:`huaweicloudsdklakeformation.v1.ResourceInfo`
        """
        return self._resource

    @resource.setter
    def resource(self, resource):
        r"""Sets the resource of this LakeFormationPolicy.

        :param resource: The resource of this LakeFormationPolicy.
        :type resource: :class:`huaweicloudsdklakeformation.v1.ResourceInfo`
        """
        self._resource = resource

    @property
    def resource_name(self):
        r"""Gets the resource_name of this LakeFormationPolicy.

        要求用点分格式进行分割

        :return: The resource_name of this LakeFormationPolicy.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        r"""Sets the resource_name of this LakeFormationPolicy.

        要求用点分格式进行分割

        :param resource_name: The resource_name of this LakeFormationPolicy.
        :type resource_name: str
        """
        self._resource_name = resource_name

    @property
    def permissions(self):
        r"""Gets the permissions of this LakeFormationPolicy.

        权限列表

        :return: The permissions of this LakeFormationPolicy.
        :rtype: list[str]
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        r"""Sets the permissions of this LakeFormationPolicy.

        权限列表

        :param permissions: The permissions of this LakeFormationPolicy.
        :type permissions: list[str]
        """
        self._permissions = permissions

    @property
    def grant_able_permissions(self):
        r"""Gets the grant_able_permissions of this LakeFormationPolicy.

        可以传递的权限列表

        :return: The grant_able_permissions of this LakeFormationPolicy.
        :rtype: list[str]
        """
        return self._grant_able_permissions

    @grant_able_permissions.setter
    def grant_able_permissions(self, grant_able_permissions):
        r"""Sets the grant_able_permissions of this LakeFormationPolicy.

        可以传递的权限列表

        :param grant_able_permissions: The grant_able_permissions of this LakeFormationPolicy.
        :type grant_able_permissions: list[str]
        """
        self._grant_able_permissions = grant_able_permissions

    @property
    def created_time(self):
        r"""Gets the created_time of this LakeFormationPolicy.

        创建时间

        :return: The created_time of this LakeFormationPolicy.
        :rtype: int
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        r"""Sets the created_time of this LakeFormationPolicy.

        创建时间

        :param created_time: The created_time of this LakeFormationPolicy.
        :type created_time: int
        """
        self._created_time = created_time

    @property
    def condition(self):
        r"""Gets the condition of this LakeFormationPolicy.

        条件信息

        :return: The condition of this LakeFormationPolicy.
        :rtype: str
        """
        return self._condition

    @condition.setter
    def condition(self, condition):
        r"""Sets the condition of this LakeFormationPolicy.

        条件信息

        :param condition: The condition of this LakeFormationPolicy.
        :type condition: str
        """
        self._condition = condition

    @property
    def obligation(self):
        r"""Gets the obligation of this LakeFormationPolicy.

        obligation，义务，当前包含data filter和data mask

        :return: The obligation of this LakeFormationPolicy.
        :rtype: str
        """
        return self._obligation

    @obligation.setter
    def obligation(self, obligation):
        r"""Sets the obligation of this LakeFormationPolicy.

        obligation，义务，当前包含data filter和data mask

        :param obligation: The obligation of this LakeFormationPolicy.
        :type obligation: str
        """
        self._obligation = obligation

    @property
    def authorization_paths(self):
        r"""Gets the authorization_paths of this LakeFormationPolicy.

        授权路径列表

        :return: The authorization_paths of this LakeFormationPolicy.
        :rtype: list[str]
        """
        return self._authorization_paths

    @authorization_paths.setter
    def authorization_paths(self, authorization_paths):
        r"""Sets the authorization_paths of this LakeFormationPolicy.

        授权路径列表

        :param authorization_paths: The authorization_paths of this LakeFormationPolicy.
        :type authorization_paths: list[str]
        """
        self._authorization_paths = authorization_paths

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
        if not isinstance(other, LakeFormationPolicy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
