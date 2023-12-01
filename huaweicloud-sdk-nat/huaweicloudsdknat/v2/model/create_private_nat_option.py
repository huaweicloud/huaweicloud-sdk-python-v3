# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreatePrivateNatOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'description': 'str',
        'spec': 'str',
        'downlink_vpcs': 'list[DownlinkVpcOption]',
        'tags': 'list[PrivateTag]',
        'enterprise_project_id': 'str'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'spec': 'spec',
        'downlink_vpcs': 'downlink_vpcs',
        'tags': 'tags',
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, name=None, description=None, spec=None, downlink_vpcs=None, tags=None, enterprise_project_id=None):
        """CreatePrivateNatOption

        The model defined in huaweicloud sdk

        :param name: 私网NAT网关实例的名字。 私网NAT网关实例的名字仅支持数字、字母、_（下划线）、-（中划线）、中文。
        :type name: str
        :param description: 私网NAT网关实例的描述。长度范围小于等于255个字符，不能包含“&lt;”和“&gt;”。
        :type description: str
        :param spec: 私网NAT网关实例的规格。 取值为： \&quot;Small\&quot;：小型 \&quot;Medium\&quot;：中型 \&quot;Large\&quot;：大型 \&quot;Extra-large\&quot;：超大型
        :type spec: str
        :param downlink_vpcs: 私网NAT网关实例所属的VPC实例。
        :type downlink_vpcs: list[:class:`huaweicloudsdknat.v2.DownlinkVpcOption`]
        :param tags: 标签列表
        :type tags: list[:class:`huaweicloudsdknat.v2.PrivateTag`]
        :param enterprise_project_id: 企业项目ID 创建私网NAT网关实例时，关联的企业项目ID。 关于企业项目ID的获取及企业项目特性的详细信息，请参考《企业管理用户指南》。
        :type enterprise_project_id: str
        """
        
        

        self._name = None
        self._description = None
        self._spec = None
        self._downlink_vpcs = None
        self._tags = None
        self._enterprise_project_id = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        if spec is not None:
            self.spec = spec
        self.downlink_vpcs = downlink_vpcs
        if tags is not None:
            self.tags = tags
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id

    @property
    def name(self):
        """Gets the name of this CreatePrivateNatOption.

        私网NAT网关实例的名字。 私网NAT网关实例的名字仅支持数字、字母、_（下划线）、-（中划线）、中文。

        :return: The name of this CreatePrivateNatOption.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreatePrivateNatOption.

        私网NAT网关实例的名字。 私网NAT网关实例的名字仅支持数字、字母、_（下划线）、-（中划线）、中文。

        :param name: The name of this CreatePrivateNatOption.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this CreatePrivateNatOption.

        私网NAT网关实例的描述。长度范围小于等于255个字符，不能包含“<”和“>”。

        :return: The description of this CreatePrivateNatOption.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreatePrivateNatOption.

        私网NAT网关实例的描述。长度范围小于等于255个字符，不能包含“<”和“>”。

        :param description: The description of this CreatePrivateNatOption.
        :type description: str
        """
        self._description = description

    @property
    def spec(self):
        """Gets the spec of this CreatePrivateNatOption.

        私网NAT网关实例的规格。 取值为： \"Small\"：小型 \"Medium\"：中型 \"Large\"：大型 \"Extra-large\"：超大型

        :return: The spec of this CreatePrivateNatOption.
        :rtype: str
        """
        return self._spec

    @spec.setter
    def spec(self, spec):
        """Sets the spec of this CreatePrivateNatOption.

        私网NAT网关实例的规格。 取值为： \"Small\"：小型 \"Medium\"：中型 \"Large\"：大型 \"Extra-large\"：超大型

        :param spec: The spec of this CreatePrivateNatOption.
        :type spec: str
        """
        self._spec = spec

    @property
    def downlink_vpcs(self):
        """Gets the downlink_vpcs of this CreatePrivateNatOption.

        私网NAT网关实例所属的VPC实例。

        :return: The downlink_vpcs of this CreatePrivateNatOption.
        :rtype: list[:class:`huaweicloudsdknat.v2.DownlinkVpcOption`]
        """
        return self._downlink_vpcs

    @downlink_vpcs.setter
    def downlink_vpcs(self, downlink_vpcs):
        """Sets the downlink_vpcs of this CreatePrivateNatOption.

        私网NAT网关实例所属的VPC实例。

        :param downlink_vpcs: The downlink_vpcs of this CreatePrivateNatOption.
        :type downlink_vpcs: list[:class:`huaweicloudsdknat.v2.DownlinkVpcOption`]
        """
        self._downlink_vpcs = downlink_vpcs

    @property
    def tags(self):
        """Gets the tags of this CreatePrivateNatOption.

        标签列表

        :return: The tags of this CreatePrivateNatOption.
        :rtype: list[:class:`huaweicloudsdknat.v2.PrivateTag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this CreatePrivateNatOption.

        标签列表

        :param tags: The tags of this CreatePrivateNatOption.
        :type tags: list[:class:`huaweicloudsdknat.v2.PrivateTag`]
        """
        self._tags = tags

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this CreatePrivateNatOption.

        企业项目ID 创建私网NAT网关实例时，关联的企业项目ID。 关于企业项目ID的获取及企业项目特性的详细信息，请参考《企业管理用户指南》。

        :return: The enterprise_project_id of this CreatePrivateNatOption.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this CreatePrivateNatOption.

        企业项目ID 创建私网NAT网关实例时，关联的企业项目ID。 关于企业项目ID的获取及企业项目特性的详细信息，请参考《企业管理用户指南》。

        :param enterprise_project_id: The enterprise_project_id of this CreatePrivateNatOption.
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
        if not isinstance(other, CreatePrivateNatOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
