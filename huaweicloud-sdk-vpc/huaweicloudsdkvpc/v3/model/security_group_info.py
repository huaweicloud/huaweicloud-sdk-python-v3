# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SecurityGroupInfo:

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
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'enterprise_project_id': 'str',
        'tags': 'list[ResourceTag]',
        'security_group_rules': 'list[SecurityGroupRule]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'project_id': 'project_id',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'enterprise_project_id': 'enterprise_project_id',
        'tags': 'tags',
        'security_group_rules': 'security_group_rules'
    }

    def __init__(self, id=None, name=None, description=None, project_id=None, created_at=None, updated_at=None, enterprise_project_id=None, tags=None, security_group_rules=None):
        r"""SecurityGroupInfo

        The model defined in huaweicloud sdk

        :param id: 功能描述：安全组对应的唯一标识 取值范围：带“-”的标准UUID格式
        :type id: str
        :param name: 功能说明：安全组名称 取值范围：1-64个字符，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）
        :type name: str
        :param description: 功能说明：安全组的描述信息 取值范围：0-255个字符，不能包含“&lt;”和“&gt;”
        :type description: str
        :param project_id: 功能说明：安全组所属的项目ID
        :type project_id: str
        :param created_at: 功能说明：安全组创建时间 取值范围：UTC时间格式：yyyy-MM-ddTHH:mm:ss
        :type created_at: datetime
        :param updated_at: 功能说明：安全组更新时间 取值范围：UTC时间格式：yyyy-MM-ddTHH:mm:ss
        :type updated_at: datetime
        :param enterprise_project_id: 功能说明：安全组所属的企业项目ID。 取值范围：最大长度36字节，带“-”连字符的UUID格式，或者是字符串“0”。“0”表示默认企业项目。
        :type enterprise_project_id: str
        :param tags: 功能描述：安全组的标签信息
        :type tags: list[:class:`huaweicloudsdkvpc.v3.ResourceTag`]
        :param security_group_rules: 安全组规则
        :type security_group_rules: list[:class:`huaweicloudsdkvpc.v3.SecurityGroupRule`]
        """
        
        

        self._id = None
        self._name = None
        self._description = None
        self._project_id = None
        self._created_at = None
        self._updated_at = None
        self._enterprise_project_id = None
        self._tags = None
        self._security_group_rules = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.description = description
        self.project_id = project_id
        self.created_at = created_at
        self.updated_at = updated_at
        self.enterprise_project_id = enterprise_project_id
        self.tags = tags
        self.security_group_rules = security_group_rules

    @property
    def id(self):
        r"""Gets the id of this SecurityGroupInfo.

        功能描述：安全组对应的唯一标识 取值范围：带“-”的标准UUID格式

        :return: The id of this SecurityGroupInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this SecurityGroupInfo.

        功能描述：安全组对应的唯一标识 取值范围：带“-”的标准UUID格式

        :param id: The id of this SecurityGroupInfo.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this SecurityGroupInfo.

        功能说明：安全组名称 取值范围：1-64个字符，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）

        :return: The name of this SecurityGroupInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this SecurityGroupInfo.

        功能说明：安全组名称 取值范围：1-64个字符，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）

        :param name: The name of this SecurityGroupInfo.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this SecurityGroupInfo.

        功能说明：安全组的描述信息 取值范围：0-255个字符，不能包含“<”和“>”

        :return: The description of this SecurityGroupInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this SecurityGroupInfo.

        功能说明：安全组的描述信息 取值范围：0-255个字符，不能包含“<”和“>”

        :param description: The description of this SecurityGroupInfo.
        :type description: str
        """
        self._description = description

    @property
    def project_id(self):
        r"""Gets the project_id of this SecurityGroupInfo.

        功能说明：安全组所属的项目ID

        :return: The project_id of this SecurityGroupInfo.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this SecurityGroupInfo.

        功能说明：安全组所属的项目ID

        :param project_id: The project_id of this SecurityGroupInfo.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def created_at(self):
        r"""Gets the created_at of this SecurityGroupInfo.

        功能说明：安全组创建时间 取值范围：UTC时间格式：yyyy-MM-ddTHH:mm:ss

        :return: The created_at of this SecurityGroupInfo.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this SecurityGroupInfo.

        功能说明：安全组创建时间 取值范围：UTC时间格式：yyyy-MM-ddTHH:mm:ss

        :param created_at: The created_at of this SecurityGroupInfo.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this SecurityGroupInfo.

        功能说明：安全组更新时间 取值范围：UTC时间格式：yyyy-MM-ddTHH:mm:ss

        :return: The updated_at of this SecurityGroupInfo.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this SecurityGroupInfo.

        功能说明：安全组更新时间 取值范围：UTC时间格式：yyyy-MM-ddTHH:mm:ss

        :param updated_at: The updated_at of this SecurityGroupInfo.
        :type updated_at: datetime
        """
        self._updated_at = updated_at

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this SecurityGroupInfo.

        功能说明：安全组所属的企业项目ID。 取值范围：最大长度36字节，带“-”连字符的UUID格式，或者是字符串“0”。“0”表示默认企业项目。

        :return: The enterprise_project_id of this SecurityGroupInfo.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this SecurityGroupInfo.

        功能说明：安全组所属的企业项目ID。 取值范围：最大长度36字节，带“-”连字符的UUID格式，或者是字符串“0”。“0”表示默认企业项目。

        :param enterprise_project_id: The enterprise_project_id of this SecurityGroupInfo.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def tags(self):
        r"""Gets the tags of this SecurityGroupInfo.

        功能描述：安全组的标签信息

        :return: The tags of this SecurityGroupInfo.
        :rtype: list[:class:`huaweicloudsdkvpc.v3.ResourceTag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this SecurityGroupInfo.

        功能描述：安全组的标签信息

        :param tags: The tags of this SecurityGroupInfo.
        :type tags: list[:class:`huaweicloudsdkvpc.v3.ResourceTag`]
        """
        self._tags = tags

    @property
    def security_group_rules(self):
        r"""Gets the security_group_rules of this SecurityGroupInfo.

        安全组规则

        :return: The security_group_rules of this SecurityGroupInfo.
        :rtype: list[:class:`huaweicloudsdkvpc.v3.SecurityGroupRule`]
        """
        return self._security_group_rules

    @security_group_rules.setter
    def security_group_rules(self, security_group_rules):
        r"""Sets the security_group_rules of this SecurityGroupInfo.

        安全组规则

        :param security_group_rules: The security_group_rules of this SecurityGroupInfo.
        :type security_group_rules: list[:class:`huaweicloudsdkvpc.v3.SecurityGroupRule`]
        """
        self._security_group_rules = security_group_rules

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
        if not isinstance(other, SecurityGroupInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
