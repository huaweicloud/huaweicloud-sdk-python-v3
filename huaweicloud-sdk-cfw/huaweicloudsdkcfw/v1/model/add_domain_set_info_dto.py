# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddDomainSetInfoDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'fw_instance_id': 'str',
        'object_id': 'str',
        'name': 'str',
        'description': 'str',
        'domain_names': 'list[DomainSetInfoDto]',
        'domain_set_type': 'int'
    }

    attribute_map = {
        'fw_instance_id': 'fw_instance_id',
        'object_id': 'object_id',
        'name': 'name',
        'description': 'description',
        'domain_names': 'domain_names',
        'domain_set_type': 'domain_set_type'
    }

    def __init__(self, fw_instance_id=None, object_id=None, name=None, description=None, domain_names=None, domain_set_type=None):
        r"""AddDomainSetInfoDto

        The model defined in huaweicloud sdk

        :param fw_instance_id: 防火墙id，可通过[防火墙ID获取方式](cfw_02_0028.xml)获取
        :type fw_instance_id: str
        :param object_id: 防护对象id，是创建云防火墙后用于区分互联网边界防护和VPC边界防护的标志id，可通过调用[查询防火墙实例接口](ListFirewallDetail.xml)获得，通过返回值中的data.records.protect_objects.object_id（.表示各对象之间层级的区分）获得，注意type为0的为互联网边界防护对象id，type为1的为VPC边界防护对象id，type可通过data.records.protect_objects.type（.表示各对象之间层级的区分）获得
        :type object_id: str
        :param name: 域名组名称
        :type name: str
        :param description: 域名组描述
        :type description: str
        :param domain_names: 域名信息列表
        :type domain_names: list[:class:`huaweicloudsdkcfw.v1.DomainSetInfoDto`]
        :param domain_set_type: 域名组类型，0表示应用域名组，1表示网络域名组
        :type domain_set_type: int
        """
        
        

        self._fw_instance_id = None
        self._object_id = None
        self._name = None
        self._description = None
        self._domain_names = None
        self._domain_set_type = None
        self.discriminator = None

        if fw_instance_id is not None:
            self.fw_instance_id = fw_instance_id
        self.object_id = object_id
        self.name = name
        if description is not None:
            self.description = description
        self.domain_names = domain_names
        if domain_set_type is not None:
            self.domain_set_type = domain_set_type

    @property
    def fw_instance_id(self):
        r"""Gets the fw_instance_id of this AddDomainSetInfoDto.

        防火墙id，可通过[防火墙ID获取方式](cfw_02_0028.xml)获取

        :return: The fw_instance_id of this AddDomainSetInfoDto.
        :rtype: str
        """
        return self._fw_instance_id

    @fw_instance_id.setter
    def fw_instance_id(self, fw_instance_id):
        r"""Sets the fw_instance_id of this AddDomainSetInfoDto.

        防火墙id，可通过[防火墙ID获取方式](cfw_02_0028.xml)获取

        :param fw_instance_id: The fw_instance_id of this AddDomainSetInfoDto.
        :type fw_instance_id: str
        """
        self._fw_instance_id = fw_instance_id

    @property
    def object_id(self):
        r"""Gets the object_id of this AddDomainSetInfoDto.

        防护对象id，是创建云防火墙后用于区分互联网边界防护和VPC边界防护的标志id，可通过调用[查询防火墙实例接口](ListFirewallDetail.xml)获得，通过返回值中的data.records.protect_objects.object_id（.表示各对象之间层级的区分）获得，注意type为0的为互联网边界防护对象id，type为1的为VPC边界防护对象id，type可通过data.records.protect_objects.type（.表示各对象之间层级的区分）获得

        :return: The object_id of this AddDomainSetInfoDto.
        :rtype: str
        """
        return self._object_id

    @object_id.setter
    def object_id(self, object_id):
        r"""Sets the object_id of this AddDomainSetInfoDto.

        防护对象id，是创建云防火墙后用于区分互联网边界防护和VPC边界防护的标志id，可通过调用[查询防火墙实例接口](ListFirewallDetail.xml)获得，通过返回值中的data.records.protect_objects.object_id（.表示各对象之间层级的区分）获得，注意type为0的为互联网边界防护对象id，type为1的为VPC边界防护对象id，type可通过data.records.protect_objects.type（.表示各对象之间层级的区分）获得

        :param object_id: The object_id of this AddDomainSetInfoDto.
        :type object_id: str
        """
        self._object_id = object_id

    @property
    def name(self):
        r"""Gets the name of this AddDomainSetInfoDto.

        域名组名称

        :return: The name of this AddDomainSetInfoDto.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this AddDomainSetInfoDto.

        域名组名称

        :param name: The name of this AddDomainSetInfoDto.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this AddDomainSetInfoDto.

        域名组描述

        :return: The description of this AddDomainSetInfoDto.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this AddDomainSetInfoDto.

        域名组描述

        :param description: The description of this AddDomainSetInfoDto.
        :type description: str
        """
        self._description = description

    @property
    def domain_names(self):
        r"""Gets the domain_names of this AddDomainSetInfoDto.

        域名信息列表

        :return: The domain_names of this AddDomainSetInfoDto.
        :rtype: list[:class:`huaweicloudsdkcfw.v1.DomainSetInfoDto`]
        """
        return self._domain_names

    @domain_names.setter
    def domain_names(self, domain_names):
        r"""Sets the domain_names of this AddDomainSetInfoDto.

        域名信息列表

        :param domain_names: The domain_names of this AddDomainSetInfoDto.
        :type domain_names: list[:class:`huaweicloudsdkcfw.v1.DomainSetInfoDto`]
        """
        self._domain_names = domain_names

    @property
    def domain_set_type(self):
        r"""Gets the domain_set_type of this AddDomainSetInfoDto.

        域名组类型，0表示应用域名组，1表示网络域名组

        :return: The domain_set_type of this AddDomainSetInfoDto.
        :rtype: int
        """
        return self._domain_set_type

    @domain_set_type.setter
    def domain_set_type(self, domain_set_type):
        r"""Sets the domain_set_type of this AddDomainSetInfoDto.

        域名组类型，0表示应用域名组，1表示网络域名组

        :param domain_set_type: The domain_set_type of this AddDomainSetInfoDto.
        :type domain_set_type: int
        """
        self._domain_set_type = domain_set_type

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
        if not isinstance(other, AddDomainSetInfoDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
