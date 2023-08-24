# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FirewallDetail:

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
        'admin_state_up': 'bool',
        'status': 'str',
        'enterprise_project_id': 'str',
        'tags': 'list[ResourceTag]',
        'associations': 'list[FirewallAssociation]',
        'ingress_rules': 'list[FirewallRuleDetail]',
        'egress_rules': 'list[FirewallRuleDetail]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'project_id': 'project_id',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'admin_state_up': 'admin_state_up',
        'status': 'status',
        'enterprise_project_id': 'enterprise_project_id',
        'tags': 'tags',
        'associations': 'associations',
        'ingress_rules': 'ingress_rules',
        'egress_rules': 'egress_rules'
    }

    def __init__(self, id=None, name=None, description=None, project_id=None, created_at=None, updated_at=None, admin_state_up=None, status=None, enterprise_project_id=None, tags=None, associations=None, ingress_rules=None, egress_rules=None):
        """FirewallDetail

        The model defined in huaweicloud sdk

        :param id: 功能说明：ACL唯一标识 取值范围：合法UUID的字符串
        :type id: str
        :param name: 功能说明：ACL名称 取值范围：0-64个字符，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）
        :type name: str
        :param description: 功能说明：ACL描述信息 取值范围：0-255个字符 约束：不能包含“&lt;”和“&gt;”。
        :type description: str
        :param project_id: 功能说明：资源所属项目ID
        :type project_id: str
        :param created_at: 功能说明：ACL创建时间 取值范围：UTC时间格式：yyyy-MM-ddTHH:mm:ss；系统自动生成
        :type created_at: str
        :param updated_at: 功能描述：ACL最近一次更新资源的时间 取值范围：UTC时间格式：yyyy-MM-ddTHH:mm:ss；系统自动生成
        :type updated_at: str
        :param admin_state_up: 功能说明：ACL是否开启 取值范围：true表示ACL开启；false表示ACL关闭
        :type admin_state_up: bool
        :param status: 功能说明：网络ACL的状态
        :type status: str
        :param enterprise_project_id: 功能说明：ACL企业项目ID。 取值范围：最大长度36字节，带“-”连字符的UUID格式，或者是字符串“0”。“0”表示默认企业项目。
        :type enterprise_project_id: str
        :param tags: 功能描述：ACL资源标签
        :type tags: list[:class:`huaweicloudsdkvpc.v3.ResourceTag`]
        :param associations: 功能说明：ACL绑定的子网列表
        :type associations: list[:class:`huaweicloudsdkvpc.v3.FirewallAssociation`]
        :param ingress_rules: 功能说明：ACL入方向规则列表
        :type ingress_rules: list[:class:`huaweicloudsdkvpc.v3.FirewallRuleDetail`]
        :param egress_rules: 功能说明：ACL出方向规则列表
        :type egress_rules: list[:class:`huaweicloudsdkvpc.v3.FirewallRuleDetail`]
        """
        
        

        self._id = None
        self._name = None
        self._description = None
        self._project_id = None
        self._created_at = None
        self._updated_at = None
        self._admin_state_up = None
        self._status = None
        self._enterprise_project_id = None
        self._tags = None
        self._associations = None
        self._ingress_rules = None
        self._egress_rules = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.description = description
        self.project_id = project_id
        self.created_at = created_at
        self.updated_at = updated_at
        self.admin_state_up = admin_state_up
        self.status = status
        self.enterprise_project_id = enterprise_project_id
        self.tags = tags
        self.associations = associations
        self.ingress_rules = ingress_rules
        self.egress_rules = egress_rules

    @property
    def id(self):
        """Gets the id of this FirewallDetail.

        功能说明：ACL唯一标识 取值范围：合法UUID的字符串

        :return: The id of this FirewallDetail.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this FirewallDetail.

        功能说明：ACL唯一标识 取值范围：合法UUID的字符串

        :param id: The id of this FirewallDetail.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this FirewallDetail.

        功能说明：ACL名称 取值范围：0-64个字符，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）

        :return: The name of this FirewallDetail.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this FirewallDetail.

        功能说明：ACL名称 取值范围：0-64个字符，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）

        :param name: The name of this FirewallDetail.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this FirewallDetail.

        功能说明：ACL描述信息 取值范围：0-255个字符 约束：不能包含“<”和“>”。

        :return: The description of this FirewallDetail.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this FirewallDetail.

        功能说明：ACL描述信息 取值范围：0-255个字符 约束：不能包含“<”和“>”。

        :param description: The description of this FirewallDetail.
        :type description: str
        """
        self._description = description

    @property
    def project_id(self):
        """Gets the project_id of this FirewallDetail.

        功能说明：资源所属项目ID

        :return: The project_id of this FirewallDetail.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this FirewallDetail.

        功能说明：资源所属项目ID

        :param project_id: The project_id of this FirewallDetail.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def created_at(self):
        """Gets the created_at of this FirewallDetail.

        功能说明：ACL创建时间 取值范围：UTC时间格式：yyyy-MM-ddTHH:mm:ss；系统自动生成

        :return: The created_at of this FirewallDetail.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this FirewallDetail.

        功能说明：ACL创建时间 取值范围：UTC时间格式：yyyy-MM-ddTHH:mm:ss；系统自动生成

        :param created_at: The created_at of this FirewallDetail.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this FirewallDetail.

        功能描述：ACL最近一次更新资源的时间 取值范围：UTC时间格式：yyyy-MM-ddTHH:mm:ss；系统自动生成

        :return: The updated_at of this FirewallDetail.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this FirewallDetail.

        功能描述：ACL最近一次更新资源的时间 取值范围：UTC时间格式：yyyy-MM-ddTHH:mm:ss；系统自动生成

        :param updated_at: The updated_at of this FirewallDetail.
        :type updated_at: str
        """
        self._updated_at = updated_at

    @property
    def admin_state_up(self):
        """Gets the admin_state_up of this FirewallDetail.

        功能说明：ACL是否开启 取值范围：true表示ACL开启；false表示ACL关闭

        :return: The admin_state_up of this FirewallDetail.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        """Sets the admin_state_up of this FirewallDetail.

        功能说明：ACL是否开启 取值范围：true表示ACL开启；false表示ACL关闭

        :param admin_state_up: The admin_state_up of this FirewallDetail.
        :type admin_state_up: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def status(self):
        """Gets the status of this FirewallDetail.

        功能说明：网络ACL的状态

        :return: The status of this FirewallDetail.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this FirewallDetail.

        功能说明：网络ACL的状态

        :param status: The status of this FirewallDetail.
        :type status: str
        """
        self._status = status

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this FirewallDetail.

        功能说明：ACL企业项目ID。 取值范围：最大长度36字节，带“-”连字符的UUID格式，或者是字符串“0”。“0”表示默认企业项目。

        :return: The enterprise_project_id of this FirewallDetail.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this FirewallDetail.

        功能说明：ACL企业项目ID。 取值范围：最大长度36字节，带“-”连字符的UUID格式，或者是字符串“0”。“0”表示默认企业项目。

        :param enterprise_project_id: The enterprise_project_id of this FirewallDetail.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def tags(self):
        """Gets the tags of this FirewallDetail.

        功能描述：ACL资源标签

        :return: The tags of this FirewallDetail.
        :rtype: list[:class:`huaweicloudsdkvpc.v3.ResourceTag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this FirewallDetail.

        功能描述：ACL资源标签

        :param tags: The tags of this FirewallDetail.
        :type tags: list[:class:`huaweicloudsdkvpc.v3.ResourceTag`]
        """
        self._tags = tags

    @property
    def associations(self):
        """Gets the associations of this FirewallDetail.

        功能说明：ACL绑定的子网列表

        :return: The associations of this FirewallDetail.
        :rtype: list[:class:`huaweicloudsdkvpc.v3.FirewallAssociation`]
        """
        return self._associations

    @associations.setter
    def associations(self, associations):
        """Sets the associations of this FirewallDetail.

        功能说明：ACL绑定的子网列表

        :param associations: The associations of this FirewallDetail.
        :type associations: list[:class:`huaweicloudsdkvpc.v3.FirewallAssociation`]
        """
        self._associations = associations

    @property
    def ingress_rules(self):
        """Gets the ingress_rules of this FirewallDetail.

        功能说明：ACL入方向规则列表

        :return: The ingress_rules of this FirewallDetail.
        :rtype: list[:class:`huaweicloudsdkvpc.v3.FirewallRuleDetail`]
        """
        return self._ingress_rules

    @ingress_rules.setter
    def ingress_rules(self, ingress_rules):
        """Sets the ingress_rules of this FirewallDetail.

        功能说明：ACL入方向规则列表

        :param ingress_rules: The ingress_rules of this FirewallDetail.
        :type ingress_rules: list[:class:`huaweicloudsdkvpc.v3.FirewallRuleDetail`]
        """
        self._ingress_rules = ingress_rules

    @property
    def egress_rules(self):
        """Gets the egress_rules of this FirewallDetail.

        功能说明：ACL出方向规则列表

        :return: The egress_rules of this FirewallDetail.
        :rtype: list[:class:`huaweicloudsdkvpc.v3.FirewallRuleDetail`]
        """
        return self._egress_rules

    @egress_rules.setter
    def egress_rules(self, egress_rules):
        """Sets the egress_rules of this FirewallDetail.

        功能说明：ACL出方向规则列表

        :param egress_rules: The egress_rules of this FirewallDetail.
        :type egress_rules: list[:class:`huaweicloudsdkvpc.v3.FirewallRuleDetail`]
        """
        self._egress_rules = egress_rules

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
        if not isinstance(other, FirewallDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
