# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CBHInstances:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'flavor_ref': 'str',
        'instance_name': 'str',
        'vpc_id': 'str',
        'nics': 'list[Nics]',
        'public_ip': 'PublicIp',
        'security_groups': 'list[SecurityGroup]',
        'availability_zone': 'str',
        'slave_availability_zone': 'str',
        'comment': 'str',
        'region': 'str',
        'hx_password': 'str',
        'bastion_type': 'str',
        'ipv6_enable': 'bool',
        'enterprise_project_id': 'str'
    }

    attribute_map = {
        'flavor_ref': 'flavor_ref',
        'instance_name': 'instance_name',
        'vpc_id': 'vpc_id',
        'nics': 'nics',
        'public_ip': 'public_ip',
        'security_groups': 'security_groups',
        'availability_zone': 'availability_zone',
        'slave_availability_zone': 'slave_availability_zone',
        'comment': 'comment',
        'region': 'region',
        'hx_password': 'hx_password',
        'bastion_type': 'bastion_type',
        'ipv6_enable': 'ipv6_enable',
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, flavor_ref=None, instance_name=None, vpc_id=None, nics=None, public_ip=None, security_groups=None, availability_zone=None, slave_availability_zone=None, comment=None, region=None, hx_password=None, bastion_type=None, ipv6_enable=None, enterprise_project_id=None):
        r"""CBHInstances

        The model defined in huaweicloud sdk

        :param flavor_ref: 待创建云堡垒机规格ID，例如： - cbh.basic.50 - cbh.enhance.50 已上线的规格请参见《云堡垒机产品介绍》的[服务版本差异](https://support.huaweicloud.com/productdesc-cbh/cbh_01_0010.html)章节。
        :type flavor_ref: str
        :param instance_name: 云堡垒机实例名称，取值范围： - 只能由中文字符、英文字母、数字及“_”、“-”组成，且长度为[1-64]个字符。 例如：CBH-6b8e
        :type instance_name: str
        :param vpc_id: 待创建云服务器所属虚拟私有云（简称VPC），需要指定已创建VPC的ID，UUID格式。 VPC的ID可以从控制台或者参考《虚拟私有云接口参考》的“查询VPC”章节获取。 例如：03211ecf-697e-4306-a7a0-6e939bf948de
        :type vpc_id: str
        :param nics: 
        :type nics: list[:class:`huaweicloudsdkcbh.v1.Nics`]
        :param public_ip: 
        :type public_ip: :class:`huaweicloudsdkcbh.v1.PublicIp`
        :param security_groups: 
        :type security_groups: list[:class:`huaweicloudsdkcbh.v1.SecurityGroup`]
        :param availability_zone: 创建云堡垒机所在的可用区，需要指定可用区名称。 可参考[地区和终端节点](https://developer.huaweicloud.com/endpoint)获取
        :type availability_zone: str
        :param slave_availability_zone: 创建云堡垒机所在的备机可用区，需要指定备机可用区名称。(当前字段未启用,填写默认值null) 可参考[地区和终端节点](https://developer.huaweicloud.com/endpoint)获取
        :type slave_availability_zone: str
        :param comment: 云堡垒机实例描述信息。
        :type comment: str
        :param region: 云服务所在局点ID。
        :type region: str
        :param hx_password: 堡垒机实例前端登录密码。密码规则：8-32位,不能包含amdin或nidma及其大写形式,必须包含大小写数字特殊字符四种类型中的三种。
        :type hx_password: str
        :param bastion_type: 堡垒机实例类型，填写“OEM”即可。
        :type bastion_type: str
        :param ipv6_enable: 是否支持IPV6，不填默认为false。
        :type ipv6_enable: bool
        :param enterprise_project_id: 企业项目ID，不填默认为0。
        :type enterprise_project_id: str
        """
        
        

        self._flavor_ref = None
        self._instance_name = None
        self._vpc_id = None
        self._nics = None
        self._public_ip = None
        self._security_groups = None
        self._availability_zone = None
        self._slave_availability_zone = None
        self._comment = None
        self._region = None
        self._hx_password = None
        self._bastion_type = None
        self._ipv6_enable = None
        self._enterprise_project_id = None
        self.discriminator = None

        self.flavor_ref = flavor_ref
        self.instance_name = instance_name
        self.vpc_id = vpc_id
        self.nics = nics
        self.public_ip = public_ip
        self.security_groups = security_groups
        self.availability_zone = availability_zone
        if slave_availability_zone is not None:
            self.slave_availability_zone = slave_availability_zone
        if comment is not None:
            self.comment = comment
        self.region = region
        self.hx_password = hx_password
        self.bastion_type = bastion_type
        if ipv6_enable is not None:
            self.ipv6_enable = ipv6_enable
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id

    @property
    def flavor_ref(self):
        r"""Gets the flavor_ref of this CBHInstances.

        待创建云堡垒机规格ID，例如： - cbh.basic.50 - cbh.enhance.50 已上线的规格请参见《云堡垒机产品介绍》的[服务版本差异](https://support.huaweicloud.com/productdesc-cbh/cbh_01_0010.html)章节。

        :return: The flavor_ref of this CBHInstances.
        :rtype: str
        """
        return self._flavor_ref

    @flavor_ref.setter
    def flavor_ref(self, flavor_ref):
        r"""Sets the flavor_ref of this CBHInstances.

        待创建云堡垒机规格ID，例如： - cbh.basic.50 - cbh.enhance.50 已上线的规格请参见《云堡垒机产品介绍》的[服务版本差异](https://support.huaweicloud.com/productdesc-cbh/cbh_01_0010.html)章节。

        :param flavor_ref: The flavor_ref of this CBHInstances.
        :type flavor_ref: str
        """
        self._flavor_ref = flavor_ref

    @property
    def instance_name(self):
        r"""Gets the instance_name of this CBHInstances.

        云堡垒机实例名称，取值范围： - 只能由中文字符、英文字母、数字及“_”、“-”组成，且长度为[1-64]个字符。 例如：CBH-6b8e

        :return: The instance_name of this CBHInstances.
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        r"""Sets the instance_name of this CBHInstances.

        云堡垒机实例名称，取值范围： - 只能由中文字符、英文字母、数字及“_”、“-”组成，且长度为[1-64]个字符。 例如：CBH-6b8e

        :param instance_name: The instance_name of this CBHInstances.
        :type instance_name: str
        """
        self._instance_name = instance_name

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this CBHInstances.

        待创建云服务器所属虚拟私有云（简称VPC），需要指定已创建VPC的ID，UUID格式。 VPC的ID可以从控制台或者参考《虚拟私有云接口参考》的“查询VPC”章节获取。 例如：03211ecf-697e-4306-a7a0-6e939bf948de

        :return: The vpc_id of this CBHInstances.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this CBHInstances.

        待创建云服务器所属虚拟私有云（简称VPC），需要指定已创建VPC的ID，UUID格式。 VPC的ID可以从控制台或者参考《虚拟私有云接口参考》的“查询VPC”章节获取。 例如：03211ecf-697e-4306-a7a0-6e939bf948de

        :param vpc_id: The vpc_id of this CBHInstances.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def nics(self):
        r"""Gets the nics of this CBHInstances.

        :return: The nics of this CBHInstances.
        :rtype: list[:class:`huaweicloudsdkcbh.v1.Nics`]
        """
        return self._nics

    @nics.setter
    def nics(self, nics):
        r"""Sets the nics of this CBHInstances.

        :param nics: The nics of this CBHInstances.
        :type nics: list[:class:`huaweicloudsdkcbh.v1.Nics`]
        """
        self._nics = nics

    @property
    def public_ip(self):
        r"""Gets the public_ip of this CBHInstances.

        :return: The public_ip of this CBHInstances.
        :rtype: :class:`huaweicloudsdkcbh.v1.PublicIp`
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        r"""Sets the public_ip of this CBHInstances.

        :param public_ip: The public_ip of this CBHInstances.
        :type public_ip: :class:`huaweicloudsdkcbh.v1.PublicIp`
        """
        self._public_ip = public_ip

    @property
    def security_groups(self):
        r"""Gets the security_groups of this CBHInstances.

        :return: The security_groups of this CBHInstances.
        :rtype: list[:class:`huaweicloudsdkcbh.v1.SecurityGroup`]
        """
        return self._security_groups

    @security_groups.setter
    def security_groups(self, security_groups):
        r"""Sets the security_groups of this CBHInstances.

        :param security_groups: The security_groups of this CBHInstances.
        :type security_groups: list[:class:`huaweicloudsdkcbh.v1.SecurityGroup`]
        """
        self._security_groups = security_groups

    @property
    def availability_zone(self):
        r"""Gets the availability_zone of this CBHInstances.

        创建云堡垒机所在的可用区，需要指定可用区名称。 可参考[地区和终端节点](https://developer.huaweicloud.com/endpoint)获取

        :return: The availability_zone of this CBHInstances.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        r"""Sets the availability_zone of this CBHInstances.

        创建云堡垒机所在的可用区，需要指定可用区名称。 可参考[地区和终端节点](https://developer.huaweicloud.com/endpoint)获取

        :param availability_zone: The availability_zone of this CBHInstances.
        :type availability_zone: str
        """
        self._availability_zone = availability_zone

    @property
    def slave_availability_zone(self):
        r"""Gets the slave_availability_zone of this CBHInstances.

        创建云堡垒机所在的备机可用区，需要指定备机可用区名称。(当前字段未启用,填写默认值null) 可参考[地区和终端节点](https://developer.huaweicloud.com/endpoint)获取

        :return: The slave_availability_zone of this CBHInstances.
        :rtype: str
        """
        return self._slave_availability_zone

    @slave_availability_zone.setter
    def slave_availability_zone(self, slave_availability_zone):
        r"""Sets the slave_availability_zone of this CBHInstances.

        创建云堡垒机所在的备机可用区，需要指定备机可用区名称。(当前字段未启用,填写默认值null) 可参考[地区和终端节点](https://developer.huaweicloud.com/endpoint)获取

        :param slave_availability_zone: The slave_availability_zone of this CBHInstances.
        :type slave_availability_zone: str
        """
        self._slave_availability_zone = slave_availability_zone

    @property
    def comment(self):
        r"""Gets the comment of this CBHInstances.

        云堡垒机实例描述信息。

        :return: The comment of this CBHInstances.
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        r"""Sets the comment of this CBHInstances.

        云堡垒机实例描述信息。

        :param comment: The comment of this CBHInstances.
        :type comment: str
        """
        self._comment = comment

    @property
    def region(self):
        r"""Gets the region of this CBHInstances.

        云服务所在局点ID。

        :return: The region of this CBHInstances.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this CBHInstances.

        云服务所在局点ID。

        :param region: The region of this CBHInstances.
        :type region: str
        """
        self._region = region

    @property
    def hx_password(self):
        r"""Gets the hx_password of this CBHInstances.

        堡垒机实例前端登录密码。密码规则：8-32位,不能包含amdin或nidma及其大写形式,必须包含大小写数字特殊字符四种类型中的三种。

        :return: The hx_password of this CBHInstances.
        :rtype: str
        """
        return self._hx_password

    @hx_password.setter
    def hx_password(self, hx_password):
        r"""Sets the hx_password of this CBHInstances.

        堡垒机实例前端登录密码。密码规则：8-32位,不能包含amdin或nidma及其大写形式,必须包含大小写数字特殊字符四种类型中的三种。

        :param hx_password: The hx_password of this CBHInstances.
        :type hx_password: str
        """
        self._hx_password = hx_password

    @property
    def bastion_type(self):
        r"""Gets the bastion_type of this CBHInstances.

        堡垒机实例类型，填写“OEM”即可。

        :return: The bastion_type of this CBHInstances.
        :rtype: str
        """
        return self._bastion_type

    @bastion_type.setter
    def bastion_type(self, bastion_type):
        r"""Sets the bastion_type of this CBHInstances.

        堡垒机实例类型，填写“OEM”即可。

        :param bastion_type: The bastion_type of this CBHInstances.
        :type bastion_type: str
        """
        self._bastion_type = bastion_type

    @property
    def ipv6_enable(self):
        r"""Gets the ipv6_enable of this CBHInstances.

        是否支持IPV6，不填默认为false。

        :return: The ipv6_enable of this CBHInstances.
        :rtype: bool
        """
        return self._ipv6_enable

    @ipv6_enable.setter
    def ipv6_enable(self, ipv6_enable):
        r"""Sets the ipv6_enable of this CBHInstances.

        是否支持IPV6，不填默认为false。

        :param ipv6_enable: The ipv6_enable of this CBHInstances.
        :type ipv6_enable: bool
        """
        self._ipv6_enable = ipv6_enable

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this CBHInstances.

        企业项目ID，不填默认为0。

        :return: The enterprise_project_id of this CBHInstances.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this CBHInstances.

        企业项目ID，不填默认为0。

        :param enterprise_project_id: The enterprise_project_id of this CBHInstances.
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
        if not isinstance(other, CBHInstances):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
