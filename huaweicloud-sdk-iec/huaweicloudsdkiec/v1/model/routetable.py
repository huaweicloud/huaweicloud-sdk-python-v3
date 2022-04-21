# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Routetable:

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
        'subnets': 'list[BaseId]',
        'vpc_id': 'str',
        'domain_id': 'str',
        'description': 'str',
        'default': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'subnets': 'subnets',
        'vpc_id': 'vpc_id',
        'domain_id': 'domain_id',
        'description': 'description',
        'default': 'default'
    }

    def __init__(self, id=None, name=None, subnets=None, vpc_id=None, domain_id=None, description=None, default=None):
        """Routetable

        The model defined in huaweicloud sdk

        :param id: 路由表ID  取值范围：标准UUID
        :type id: str
        :param name: 路由表名称  取值范围：1-64个字符，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）
        :type name: str
        :param subnets: 路由表所关联的子网  约束：只能关联路由表所属VPC下的子网
        :type subnets: list[:class:`huaweicloudsdkiec.v1.BaseId`]
        :param vpc_id: 路由表所在的虚拟私有云ID
        :type vpc_id: str
        :param domain_id: 帐号ID
        :type domain_id: str
        :param description: 路由表描述信息  取值范围：0-255个字符，不能包含“&lt;”和“&gt;”
        :type description: str
        :param default: 是否为默认路由表  取值范围：true表示默认路由表；false表示自定义路由表
        :type default: bool
        """
        
        

        self._id = None
        self._name = None
        self._subnets = None
        self._vpc_id = None
        self._domain_id = None
        self._description = None
        self._default = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if subnets is not None:
            self.subnets = subnets
        if vpc_id is not None:
            self.vpc_id = vpc_id
        if domain_id is not None:
            self.domain_id = domain_id
        if description is not None:
            self.description = description
        if default is not None:
            self.default = default

    @property
    def id(self):
        """Gets the id of this Routetable.

        路由表ID  取值范围：标准UUID

        :return: The id of this Routetable.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Routetable.

        路由表ID  取值范围：标准UUID

        :param id: The id of this Routetable.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this Routetable.

        路由表名称  取值范围：1-64个字符，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）

        :return: The name of this Routetable.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Routetable.

        路由表名称  取值范围：1-64个字符，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）

        :param name: The name of this Routetable.
        :type name: str
        """
        self._name = name

    @property
    def subnets(self):
        """Gets the subnets of this Routetable.

        路由表所关联的子网  约束：只能关联路由表所属VPC下的子网

        :return: The subnets of this Routetable.
        :rtype: list[:class:`huaweicloudsdkiec.v1.BaseId`]
        """
        return self._subnets

    @subnets.setter
    def subnets(self, subnets):
        """Sets the subnets of this Routetable.

        路由表所关联的子网  约束：只能关联路由表所属VPC下的子网

        :param subnets: The subnets of this Routetable.
        :type subnets: list[:class:`huaweicloudsdkiec.v1.BaseId`]
        """
        self._subnets = subnets

    @property
    def vpc_id(self):
        """Gets the vpc_id of this Routetable.

        路由表所在的虚拟私有云ID

        :return: The vpc_id of this Routetable.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this Routetable.

        路由表所在的虚拟私有云ID

        :param vpc_id: The vpc_id of this Routetable.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def domain_id(self):
        """Gets the domain_id of this Routetable.

        帐号ID

        :return: The domain_id of this Routetable.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this Routetable.

        帐号ID

        :param domain_id: The domain_id of this Routetable.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def description(self):
        """Gets the description of this Routetable.

        路由表描述信息  取值范围：0-255个字符，不能包含“<”和“>”

        :return: The description of this Routetable.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Routetable.

        路由表描述信息  取值范围：0-255个字符，不能包含“<”和“>”

        :param description: The description of this Routetable.
        :type description: str
        """
        self._description = description

    @property
    def default(self):
        """Gets the default of this Routetable.

        是否为默认路由表  取值范围：true表示默认路由表；false表示自定义路由表

        :return: The default of this Routetable.
        :rtype: bool
        """
        return self._default

    @default.setter
    def default(self, default):
        """Sets the default of this Routetable.

        是否为默认路由表  取值范围：true表示默认路由表；false表示自定义路由表

        :param default: The default of this Routetable.
        :type default: bool
        """
        self._default = default

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
        if not isinstance(other, Routetable):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
