# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateVpcOption:

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
        'cidr': 'str',
        'enterprise_project_id': 'str',
        'tags': 'list[Tag]'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'cidr': 'cidr',
        'enterprise_project_id': 'enterprise_project_id',
        'tags': 'tags'
    }

    def __init__(self, name=None, description=None, cidr=None, enterprise_project_id=None, tags=None):
        """CreateVpcOption

        The model defined in huaweicloud sdk

        :param name: 功能描述：VPC的名称信息 取值范围：1-64个字符，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）
        :type name: str
        :param description: 功能说明：VPC的描述信息 取值范围：0-255个字符，不能包含“&lt;”和“&gt;”。
        :type description: str
        :param cidr: 功能说明：vpc下可用子网的范围 取值范围： −10.0.0.0/8~10.255.255.240/28 −172.16.0.0/12 ~ 172.31.255.240/28 −192.168.0.0/16 ~ 192.168.255.240/28 约束：必须是cidr格式，例如:192.168.0.0/16
        :type cidr: str
        :param enterprise_project_id: 功能说明：企业项目ID。创建vpc时，给vpc绑定企业项目ID。 取值范围：最大长度36字节，带“-”连字符的UUID格式，或者是字符串“0”。“0”表示默认企业项目。 
        :type enterprise_project_id: str
        :param tags: 功能说明：VPC的标签信息，详情参见Tag对象 取值范围：0-10个标签键值对
        :type tags: list[:class:`huaweicloudsdkvpc.v3.Tag`]
        """
        
        

        self._name = None
        self._description = None
        self._cidr = None
        self._enterprise_project_id = None
        self._tags = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        self.cidr = cidr
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if tags is not None:
            self.tags = tags

    @property
    def name(self):
        """Gets the name of this CreateVpcOption.

        功能描述：VPC的名称信息 取值范围：1-64个字符，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）

        :return: The name of this CreateVpcOption.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateVpcOption.

        功能描述：VPC的名称信息 取值范围：1-64个字符，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）

        :param name: The name of this CreateVpcOption.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this CreateVpcOption.

        功能说明：VPC的描述信息 取值范围：0-255个字符，不能包含“<”和“>”。

        :return: The description of this CreateVpcOption.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateVpcOption.

        功能说明：VPC的描述信息 取值范围：0-255个字符，不能包含“<”和“>”。

        :param description: The description of this CreateVpcOption.
        :type description: str
        """
        self._description = description

    @property
    def cidr(self):
        """Gets the cidr of this CreateVpcOption.

        功能说明：vpc下可用子网的范围 取值范围： −10.0.0.0/8~10.255.255.240/28 −172.16.0.0/12 ~ 172.31.255.240/28 −192.168.0.0/16 ~ 192.168.255.240/28 约束：必须是cidr格式，例如:192.168.0.0/16

        :return: The cidr of this CreateVpcOption.
        :rtype: str
        """
        return self._cidr

    @cidr.setter
    def cidr(self, cidr):
        """Sets the cidr of this CreateVpcOption.

        功能说明：vpc下可用子网的范围 取值范围： −10.0.0.0/8~10.255.255.240/28 −172.16.0.0/12 ~ 172.31.255.240/28 −192.168.0.0/16 ~ 192.168.255.240/28 约束：必须是cidr格式，例如:192.168.0.0/16

        :param cidr: The cidr of this CreateVpcOption.
        :type cidr: str
        """
        self._cidr = cidr

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this CreateVpcOption.

        功能说明：企业项目ID。创建vpc时，给vpc绑定企业项目ID。 取值范围：最大长度36字节，带“-”连字符的UUID格式，或者是字符串“0”。“0”表示默认企业项目。 

        :return: The enterprise_project_id of this CreateVpcOption.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this CreateVpcOption.

        功能说明：企业项目ID。创建vpc时，给vpc绑定企业项目ID。 取值范围：最大长度36字节，带“-”连字符的UUID格式，或者是字符串“0”。“0”表示默认企业项目。 

        :param enterprise_project_id: The enterprise_project_id of this CreateVpcOption.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def tags(self):
        """Gets the tags of this CreateVpcOption.

        功能说明：VPC的标签信息，详情参见Tag对象 取值范围：0-10个标签键值对

        :return: The tags of this CreateVpcOption.
        :rtype: list[:class:`huaweicloudsdkvpc.v3.Tag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this CreateVpcOption.

        功能说明：VPC的标签信息，详情参见Tag对象 取值范围：0-10个标签键值对

        :param tags: The tags of this CreateVpcOption.
        :type tags: list[:class:`huaweicloudsdkvpc.v3.Tag`]
        """
        self._tags = tags

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
        if not isinstance(other, CreateVpcOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
