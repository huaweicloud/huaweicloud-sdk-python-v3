# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PrivateNat:

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
        'project_id': 'str',
        'name': 'str',
        'description': 'str',
        'spec': 'str',
        'status': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'downlink_vpcs': 'list[DownlinkVpc]',
        'tags': 'list[PrivateTag]',
        'enterprise_project_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'project_id': 'project_id',
        'name': 'name',
        'description': 'description',
        'spec': 'spec',
        'status': 'status',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'downlink_vpcs': 'downlink_vpcs',
        'tags': 'tags',
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, id=None, project_id=None, name=None, description=None, spec=None, status=None, created_at=None, updated_at=None, downlink_vpcs=None, tags=None, enterprise_project_id=None):
        """PrivateNat

        The model defined in huaweicloud sdk

        :param id: 私网NAT网关实例的ID。
        :type id: str
        :param project_id: 项目的ID。
        :type project_id: str
        :param name: 私网NAT网关实例的名字。
        :type name: str
        :param description: 私网NAT网关实例的描述。长度范围小于等于255个字符，不能包含“&lt;”和“&gt;”。
        :type description: str
        :param spec: 私网NAT网关实例的规格。 取值为： \&quot;Small\&quot;：小型 \&quot;Medium\&quot;：中型 \&quot;Large\&quot;：大型 \&quot;Extra-large\&quot;：超大型
        :type spec: str
        :param status: 私网NAT网关实例的状态。 取值为： \&quot;ACTIVE\&quot;：正常运行 \&quot;FROZEN\&quot;：冻结
        :type status: str
        :param created_at: 私网NAT网关实例的创建时间，遵循UTC时间，格式是yyyy-mm-ddThh:mm:ssZ。
        :type created_at: datetime
        :param updated_at: 私网NAT网关实例的更新时间，遵循UTC时间，格式是yyyy-mm-ddThh:mm:ssZ。
        :type updated_at: datetime
        :param downlink_vpcs: 私网NAT网关实例所属的VPC实例。
        :type downlink_vpcs: list[:class:`huaweicloudsdknat.v2.DownlinkVpc`]
        :param tags: 标签列表。
        :type tags: list[:class:`huaweicloudsdknat.v2.PrivateTag`]
        :param enterprise_project_id: 企业项目ID。 创建私网NAT网关实例时，关联的企业项目ID。
        :type enterprise_project_id: str
        """
        
        

        self._id = None
        self._project_id = None
        self._name = None
        self._description = None
        self._spec = None
        self._status = None
        self._created_at = None
        self._updated_at = None
        self._downlink_vpcs = None
        self._tags = None
        self._enterprise_project_id = None
        self.discriminator = None

        self.id = id
        self.project_id = project_id
        self.name = name
        self.description = description
        self.spec = spec
        self.status = status
        self.created_at = created_at
        self.updated_at = updated_at
        self.downlink_vpcs = downlink_vpcs
        if tags is not None:
            self.tags = tags
        self.enterprise_project_id = enterprise_project_id

    @property
    def id(self):
        """Gets the id of this PrivateNat.

        私网NAT网关实例的ID。

        :return: The id of this PrivateNat.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PrivateNat.

        私网NAT网关实例的ID。

        :param id: The id of this PrivateNat.
        :type id: str
        """
        self._id = id

    @property
    def project_id(self):
        """Gets the project_id of this PrivateNat.

        项目的ID。

        :return: The project_id of this PrivateNat.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this PrivateNat.

        项目的ID。

        :param project_id: The project_id of this PrivateNat.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def name(self):
        """Gets the name of this PrivateNat.

        私网NAT网关实例的名字。

        :return: The name of this PrivateNat.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PrivateNat.

        私网NAT网关实例的名字。

        :param name: The name of this PrivateNat.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this PrivateNat.

        私网NAT网关实例的描述。长度范围小于等于255个字符，不能包含“<”和“>”。

        :return: The description of this PrivateNat.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PrivateNat.

        私网NAT网关实例的描述。长度范围小于等于255个字符，不能包含“<”和“>”。

        :param description: The description of this PrivateNat.
        :type description: str
        """
        self._description = description

    @property
    def spec(self):
        """Gets the spec of this PrivateNat.

        私网NAT网关实例的规格。 取值为： \"Small\"：小型 \"Medium\"：中型 \"Large\"：大型 \"Extra-large\"：超大型

        :return: The spec of this PrivateNat.
        :rtype: str
        """
        return self._spec

    @spec.setter
    def spec(self, spec):
        """Sets the spec of this PrivateNat.

        私网NAT网关实例的规格。 取值为： \"Small\"：小型 \"Medium\"：中型 \"Large\"：大型 \"Extra-large\"：超大型

        :param spec: The spec of this PrivateNat.
        :type spec: str
        """
        self._spec = spec

    @property
    def status(self):
        """Gets the status of this PrivateNat.

        私网NAT网关实例的状态。 取值为： \"ACTIVE\"：正常运行 \"FROZEN\"：冻结

        :return: The status of this PrivateNat.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this PrivateNat.

        私网NAT网关实例的状态。 取值为： \"ACTIVE\"：正常运行 \"FROZEN\"：冻结

        :param status: The status of this PrivateNat.
        :type status: str
        """
        self._status = status

    @property
    def created_at(self):
        """Gets the created_at of this PrivateNat.

        私网NAT网关实例的创建时间，遵循UTC时间，格式是yyyy-mm-ddThh:mm:ssZ。

        :return: The created_at of this PrivateNat.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this PrivateNat.

        私网NAT网关实例的创建时间，遵循UTC时间，格式是yyyy-mm-ddThh:mm:ssZ。

        :param created_at: The created_at of this PrivateNat.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this PrivateNat.

        私网NAT网关实例的更新时间，遵循UTC时间，格式是yyyy-mm-ddThh:mm:ssZ。

        :return: The updated_at of this PrivateNat.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this PrivateNat.

        私网NAT网关实例的更新时间，遵循UTC时间，格式是yyyy-mm-ddThh:mm:ssZ。

        :param updated_at: The updated_at of this PrivateNat.
        :type updated_at: datetime
        """
        self._updated_at = updated_at

    @property
    def downlink_vpcs(self):
        """Gets the downlink_vpcs of this PrivateNat.

        私网NAT网关实例所属的VPC实例。

        :return: The downlink_vpcs of this PrivateNat.
        :rtype: list[:class:`huaweicloudsdknat.v2.DownlinkVpc`]
        """
        return self._downlink_vpcs

    @downlink_vpcs.setter
    def downlink_vpcs(self, downlink_vpcs):
        """Sets the downlink_vpcs of this PrivateNat.

        私网NAT网关实例所属的VPC实例。

        :param downlink_vpcs: The downlink_vpcs of this PrivateNat.
        :type downlink_vpcs: list[:class:`huaweicloudsdknat.v2.DownlinkVpc`]
        """
        self._downlink_vpcs = downlink_vpcs

    @property
    def tags(self):
        """Gets the tags of this PrivateNat.

        标签列表。

        :return: The tags of this PrivateNat.
        :rtype: list[:class:`huaweicloudsdknat.v2.PrivateTag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this PrivateNat.

        标签列表。

        :param tags: The tags of this PrivateNat.
        :type tags: list[:class:`huaweicloudsdknat.v2.PrivateTag`]
        """
        self._tags = tags

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this PrivateNat.

        企业项目ID。 创建私网NAT网关实例时，关联的企业项目ID。

        :return: The enterprise_project_id of this PrivateNat.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this PrivateNat.

        企业项目ID。 创建私网NAT网关实例时，关联的企业项目ID。

        :param enterprise_project_id: The enterprise_project_id of this PrivateNat.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

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
        if not isinstance(other, PrivateNat):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
