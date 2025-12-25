# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HwcSubnet:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'description': 'str',
        'project_id': 'str',
        'created_at': 'str',
        'updated_at': 'str',
        'enterprise_project_id': 'str',
        'security_group_rules': 'list[HwcSubnetSecurityGroupRule]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'project_id': 'project_id',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'enterprise_project_id': 'enterprise_project_id',
        'security_group_rules': 'security_group_rules'
    }

    def __init__(self, id=None, name=None, description=None, project_id=None, created_at=None, updated_at=None, enterprise_project_id=None, security_group_rules=None):
        r"""HwcSubnet

        The model defined in huaweicloud sdk

        :param id: 安全组对应的唯一标识
        :type id: str
        :param name: 安全组名称
        :type name: str
        :param description: 安全组的描述信息
        :type description: str
        :param project_id: 安全组所属的项目ID
        :type project_id: str
        :param created_at: 安全组创建时间 取值范围：UTC时间格式，yyyy-MM-ddTHH:mm:ss
        :type created_at: str
        :param updated_at: 安全组更新时间 取值范围：UTC时间格式，yyyy-MM-ddTHH:mm:ss
        :type updated_at: str
        :param enterprise_project_id: 安全组所属的企业项目ID。 取值范围：最大长度36字节，带“-”连字符的UUID格式，或者是字符串“0”。“0”表示默认企业项目。
        :type enterprise_project_id: str
        :param security_group_rules: 安全组规则
        :type security_group_rules: list[:class:`huaweicloudsdksecmaster.v1.HwcSubnetSecurityGroupRule`]
        """
        
        

        self._id = None
        self._name = None
        self._description = None
        self._project_id = None
        self._created_at = None
        self._updated_at = None
        self._enterprise_project_id = None
        self._security_group_rules = None
        self.discriminator = None

        self.id = id
        self.name = name
        if description is not None:
            self.description = description
        self.project_id = project_id
        self.created_at = created_at
        self.updated_at = updated_at
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if security_group_rules is not None:
            self.security_group_rules = security_group_rules

    @property
    def id(self):
        r"""Gets the id of this HwcSubnet.

        安全组对应的唯一标识

        :return: The id of this HwcSubnet.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this HwcSubnet.

        安全组对应的唯一标识

        :param id: The id of this HwcSubnet.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this HwcSubnet.

        安全组名称

        :return: The name of this HwcSubnet.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this HwcSubnet.

        安全组名称

        :param name: The name of this HwcSubnet.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this HwcSubnet.

        安全组的描述信息

        :return: The description of this HwcSubnet.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this HwcSubnet.

        安全组的描述信息

        :param description: The description of this HwcSubnet.
        :type description: str
        """
        self._description = description

    @property
    def project_id(self):
        r"""Gets the project_id of this HwcSubnet.

        安全组所属的项目ID

        :return: The project_id of this HwcSubnet.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this HwcSubnet.

        安全组所属的项目ID

        :param project_id: The project_id of this HwcSubnet.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def created_at(self):
        r"""Gets the created_at of this HwcSubnet.

        安全组创建时间 取值范围：UTC时间格式，yyyy-MM-ddTHH:mm:ss

        :return: The created_at of this HwcSubnet.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this HwcSubnet.

        安全组创建时间 取值范围：UTC时间格式，yyyy-MM-ddTHH:mm:ss

        :param created_at: The created_at of this HwcSubnet.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this HwcSubnet.

        安全组更新时间 取值范围：UTC时间格式，yyyy-MM-ddTHH:mm:ss

        :return: The updated_at of this HwcSubnet.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this HwcSubnet.

        安全组更新时间 取值范围：UTC时间格式，yyyy-MM-ddTHH:mm:ss

        :param updated_at: The updated_at of this HwcSubnet.
        :type updated_at: str
        """
        self._updated_at = updated_at

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this HwcSubnet.

        安全组所属的企业项目ID。 取值范围：最大长度36字节，带“-”连字符的UUID格式，或者是字符串“0”。“0”表示默认企业项目。

        :return: The enterprise_project_id of this HwcSubnet.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this HwcSubnet.

        安全组所属的企业项目ID。 取值范围：最大长度36字节，带“-”连字符的UUID格式，或者是字符串“0”。“0”表示默认企业项目。

        :param enterprise_project_id: The enterprise_project_id of this HwcSubnet.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def security_group_rules(self):
        r"""Gets the security_group_rules of this HwcSubnet.

        安全组规则

        :return: The security_group_rules of this HwcSubnet.
        :rtype: list[:class:`huaweicloudsdksecmaster.v1.HwcSubnetSecurityGroupRule`]
        """
        return self._security_group_rules

    @security_group_rules.setter
    def security_group_rules(self, security_group_rules):
        r"""Sets the security_group_rules of this HwcSubnet.

        安全组规则

        :param security_group_rules: The security_group_rules of this HwcSubnet.
        :type security_group_rules: list[:class:`huaweicloudsdksecmaster.v1.HwcSubnetSecurityGroupRule`]
        """
        self._security_group_rules = security_group_rules

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
        if not isinstance(other, HwcSubnet):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
