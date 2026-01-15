# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SimpleSecurityGroupsInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'description': 'str',
        'name': 'str',
        'id': 'str',
        'security_group_rules': 'str',
        'tenant_id': 'str',
        'project_id': 'str',
        'created_at': 'str',
        'updated_at': 'str'
    }

    attribute_map = {
        'description': 'description',
        'name': 'name',
        'id': 'id',
        'security_group_rules': 'security_group_rules',
        'tenant_id': 'tenant_id',
        'project_id': 'project_id',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, description=None, name=None, id=None, security_group_rules=None, tenant_id=None, project_id=None, created_at=None, updated_at=None):
        r"""SimpleSecurityGroupsInfo

        The model defined in huaweicloud sdk

        :param description: 安全组描述。
        :type description: str
        :param name: 安全组名称。
        :type name: str
        :param id: 安全组的主键。
        :type id: str
        :param security_group_rules: 外部网关信息。
        :type security_group_rules: str
        :param tenant_id: 租户主键。
        :type tenant_id: str
        :param project_id: 资源租户主键。
        :type project_id: str
        :param created_at: 资源创建时间。
        :type created_at: str
        :param updated_at: 资源更新时间。
        :type updated_at: str
        """
        
        

        self._description = None
        self._name = None
        self._id = None
        self._security_group_rules = None
        self._tenant_id = None
        self._project_id = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if name is not None:
            self.name = name
        if id is not None:
            self.id = id
        if security_group_rules is not None:
            self.security_group_rules = security_group_rules
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if project_id is not None:
            self.project_id = project_id
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def description(self):
        r"""Gets the description of this SimpleSecurityGroupsInfo.

        安全组描述。

        :return: The description of this SimpleSecurityGroupsInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this SimpleSecurityGroupsInfo.

        安全组描述。

        :param description: The description of this SimpleSecurityGroupsInfo.
        :type description: str
        """
        self._description = description

    @property
    def name(self):
        r"""Gets the name of this SimpleSecurityGroupsInfo.

        安全组名称。

        :return: The name of this SimpleSecurityGroupsInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this SimpleSecurityGroupsInfo.

        安全组名称。

        :param name: The name of this SimpleSecurityGroupsInfo.
        :type name: str
        """
        self._name = name

    @property
    def id(self):
        r"""Gets the id of this SimpleSecurityGroupsInfo.

        安全组的主键。

        :return: The id of this SimpleSecurityGroupsInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this SimpleSecurityGroupsInfo.

        安全组的主键。

        :param id: The id of this SimpleSecurityGroupsInfo.
        :type id: str
        """
        self._id = id

    @property
    def security_group_rules(self):
        r"""Gets the security_group_rules of this SimpleSecurityGroupsInfo.

        外部网关信息。

        :return: The security_group_rules of this SimpleSecurityGroupsInfo.
        :rtype: str
        """
        return self._security_group_rules

    @security_group_rules.setter
    def security_group_rules(self, security_group_rules):
        r"""Sets the security_group_rules of this SimpleSecurityGroupsInfo.

        外部网关信息。

        :param security_group_rules: The security_group_rules of this SimpleSecurityGroupsInfo.
        :type security_group_rules: str
        """
        self._security_group_rules = security_group_rules

    @property
    def tenant_id(self):
        r"""Gets the tenant_id of this SimpleSecurityGroupsInfo.

        租户主键。

        :return: The tenant_id of this SimpleSecurityGroupsInfo.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        r"""Sets the tenant_id of this SimpleSecurityGroupsInfo.

        租户主键。

        :param tenant_id: The tenant_id of this SimpleSecurityGroupsInfo.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

    @property
    def project_id(self):
        r"""Gets the project_id of this SimpleSecurityGroupsInfo.

        资源租户主键。

        :return: The project_id of this SimpleSecurityGroupsInfo.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this SimpleSecurityGroupsInfo.

        资源租户主键。

        :param project_id: The project_id of this SimpleSecurityGroupsInfo.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def created_at(self):
        r"""Gets the created_at of this SimpleSecurityGroupsInfo.

        资源创建时间。

        :return: The created_at of this SimpleSecurityGroupsInfo.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this SimpleSecurityGroupsInfo.

        资源创建时间。

        :param created_at: The created_at of this SimpleSecurityGroupsInfo.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this SimpleSecurityGroupsInfo.

        资源更新时间。

        :return: The updated_at of this SimpleSecurityGroupsInfo.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this SimpleSecurityGroupsInfo.

        资源更新时间。

        :param updated_at: The updated_at of this SimpleSecurityGroupsInfo.
        :type updated_at: str
        """
        self._updated_at = updated_at

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SimpleSecurityGroupsInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
