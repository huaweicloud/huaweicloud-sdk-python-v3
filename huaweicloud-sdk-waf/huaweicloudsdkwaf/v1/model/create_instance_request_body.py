# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateInstanceRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'chargemode': 'int',
        'region': 'str',
        'available_zone': 'str',
        'arch': 'str',
        'instancename': 'str',
        'specification': 'str',
        'cpu_flavor': 'str',
        'vpc_id': 'str',
        'subnet_id': 'str',
        'security_group': 'list[str]',
        'count': 'int',
        'res_tenant': 'bool',
        'anti_affinity': 'bool',
        'tags': 'list[TmsResourceTag]'
    }

    attribute_map = {
        'chargemode': 'chargemode',
        'region': 'region',
        'available_zone': 'available_zone',
        'arch': 'arch',
        'instancename': 'instancename',
        'specification': 'specification',
        'cpu_flavor': 'cpu_flavor',
        'vpc_id': 'vpc_id',
        'subnet_id': 'subnet_id',
        'security_group': 'security_group',
        'count': 'count',
        'res_tenant': 'res_tenant',
        'anti_affinity': 'anti_affinity',
        'tags': 'tags'
    }

    def __init__(self, chargemode=None, region=None, available_zone=None, arch=None, instancename=None, specification=None, cpu_flavor=None, vpc_id=None, subnet_id=None, security_group=None, count=None, res_tenant=None, anti_affinity=None, tags=None):
        r"""CreateInstanceRequestBody

        The model defined in huaweicloud sdk

        :param chargemode: 收费模式，当前仅支持按需收费（30）
        :type chargemode: int
        :param region: 需要创建独享引擎的局点，例如：北京四（cn-north-4）
        :type region: str
        :param available_zone: 需要创建独享引擎的可用区，例如：北京四可用区1（cn-north-4a）
        :type available_zone: str
        :param arch: 独享引擎CPU架构，例如：x86与arm
        :type arch: str
        :param instancename: 独享引擎名称前缀
        :type instancename: str
        :param specification: 独享引擎版本规格   - waf.instance.enterprise：企业版，对应控制台WI-500规格   - waf.instance.professional：专业版，对应控制台WI-100规格
        :type specification: str
        :param cpu_flavor: 独享引擎ECS规格，实例规格。创建资源租户类独享引擎可不填该参数，创建普通资源租户独享引擎必填该参数。普通租户类独享引擎具体支持的规格以waf控制台上支持的规格为准，企业版对应8U16G的ecs规格，专业版对应2U4G的ecs规格。
        :type cpu_flavor: str
        :param vpc_id: 独享引擎所在VPC的ID（通过调用虚拟私有云ListVpcs接口获取所有的VPC列表查询VPC的ID，如果需要关联企业项目，则调用虚拟私有云的接口也需要关联企业项目ID）
        :type vpc_id: str
        :param subnet_id: 独享引擎所在VPC内的子网ID（通过调用虚拟私有云ListSubnets接口获取所有的子网列表查询子网的ID，如果需要关联企业项目，则调用虚拟私有云的接口也需要关联企业项目ID）
        :type subnet_id: str
        :param security_group: 独享引擎需要绑定的安全组ID（通过调用虚拟私有云ListSecurityGroups接口获取所有的安全组列表查询安全组的ID，如果需要关联企业项目，则调用虚拟私有云的接口也需要关联企业项目ID）
        :type security_group: list[str]
        :param count: 申请的独享引擎数量
        :type count: int
        :param res_tenant: 是否为资源租户类，默认值为false。   - true: 资源租户类   - false: 普通租户类
        :type res_tenant: bool
        :param anti_affinity: 是否开启反亲和。仅资源租户独享实例支持该特性。
        :type anti_affinity: bool
        :param tags: TMS标签信息
        :type tags: list[:class:`huaweicloudsdkwaf.v1.TmsResourceTag`]
        """
        
        

        self._chargemode = None
        self._region = None
        self._available_zone = None
        self._arch = None
        self._instancename = None
        self._specification = None
        self._cpu_flavor = None
        self._vpc_id = None
        self._subnet_id = None
        self._security_group = None
        self._count = None
        self._res_tenant = None
        self._anti_affinity = None
        self._tags = None
        self.discriminator = None

        if chargemode is not None:
            self.chargemode = chargemode
        self.region = region
        self.available_zone = available_zone
        self.arch = arch
        self.instancename = instancename
        self.specification = specification
        if cpu_flavor is not None:
            self.cpu_flavor = cpu_flavor
        self.vpc_id = vpc_id
        self.subnet_id = subnet_id
        self.security_group = security_group
        self.count = count
        if res_tenant is not None:
            self.res_tenant = res_tenant
        if anti_affinity is not None:
            self.anti_affinity = anti_affinity
        if tags is not None:
            self.tags = tags

    @property
    def chargemode(self):
        r"""Gets the chargemode of this CreateInstanceRequestBody.

        收费模式，当前仅支持按需收费（30）

        :return: The chargemode of this CreateInstanceRequestBody.
        :rtype: int
        """
        return self._chargemode

    @chargemode.setter
    def chargemode(self, chargemode):
        r"""Sets the chargemode of this CreateInstanceRequestBody.

        收费模式，当前仅支持按需收费（30）

        :param chargemode: The chargemode of this CreateInstanceRequestBody.
        :type chargemode: int
        """
        self._chargemode = chargemode

    @property
    def region(self):
        r"""Gets the region of this CreateInstanceRequestBody.

        需要创建独享引擎的局点，例如：北京四（cn-north-4）

        :return: The region of this CreateInstanceRequestBody.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this CreateInstanceRequestBody.

        需要创建独享引擎的局点，例如：北京四（cn-north-4）

        :param region: The region of this CreateInstanceRequestBody.
        :type region: str
        """
        self._region = region

    @property
    def available_zone(self):
        r"""Gets the available_zone of this CreateInstanceRequestBody.

        需要创建独享引擎的可用区，例如：北京四可用区1（cn-north-4a）

        :return: The available_zone of this CreateInstanceRequestBody.
        :rtype: str
        """
        return self._available_zone

    @available_zone.setter
    def available_zone(self, available_zone):
        r"""Sets the available_zone of this CreateInstanceRequestBody.

        需要创建独享引擎的可用区，例如：北京四可用区1（cn-north-4a）

        :param available_zone: The available_zone of this CreateInstanceRequestBody.
        :type available_zone: str
        """
        self._available_zone = available_zone

    @property
    def arch(self):
        r"""Gets the arch of this CreateInstanceRequestBody.

        独享引擎CPU架构，例如：x86与arm

        :return: The arch of this CreateInstanceRequestBody.
        :rtype: str
        """
        return self._arch

    @arch.setter
    def arch(self, arch):
        r"""Sets the arch of this CreateInstanceRequestBody.

        独享引擎CPU架构，例如：x86与arm

        :param arch: The arch of this CreateInstanceRequestBody.
        :type arch: str
        """
        self._arch = arch

    @property
    def instancename(self):
        r"""Gets the instancename of this CreateInstanceRequestBody.

        独享引擎名称前缀

        :return: The instancename of this CreateInstanceRequestBody.
        :rtype: str
        """
        return self._instancename

    @instancename.setter
    def instancename(self, instancename):
        r"""Sets the instancename of this CreateInstanceRequestBody.

        独享引擎名称前缀

        :param instancename: The instancename of this CreateInstanceRequestBody.
        :type instancename: str
        """
        self._instancename = instancename

    @property
    def specification(self):
        r"""Gets the specification of this CreateInstanceRequestBody.

        独享引擎版本规格   - waf.instance.enterprise：企业版，对应控制台WI-500规格   - waf.instance.professional：专业版，对应控制台WI-100规格

        :return: The specification of this CreateInstanceRequestBody.
        :rtype: str
        """
        return self._specification

    @specification.setter
    def specification(self, specification):
        r"""Sets the specification of this CreateInstanceRequestBody.

        独享引擎版本规格   - waf.instance.enterprise：企业版，对应控制台WI-500规格   - waf.instance.professional：专业版，对应控制台WI-100规格

        :param specification: The specification of this CreateInstanceRequestBody.
        :type specification: str
        """
        self._specification = specification

    @property
    def cpu_flavor(self):
        r"""Gets the cpu_flavor of this CreateInstanceRequestBody.

        独享引擎ECS规格，实例规格。创建资源租户类独享引擎可不填该参数，创建普通资源租户独享引擎必填该参数。普通租户类独享引擎具体支持的规格以waf控制台上支持的规格为准，企业版对应8U16G的ecs规格，专业版对应2U4G的ecs规格。

        :return: The cpu_flavor of this CreateInstanceRequestBody.
        :rtype: str
        """
        return self._cpu_flavor

    @cpu_flavor.setter
    def cpu_flavor(self, cpu_flavor):
        r"""Sets the cpu_flavor of this CreateInstanceRequestBody.

        独享引擎ECS规格，实例规格。创建资源租户类独享引擎可不填该参数，创建普通资源租户独享引擎必填该参数。普通租户类独享引擎具体支持的规格以waf控制台上支持的规格为准，企业版对应8U16G的ecs规格，专业版对应2U4G的ecs规格。

        :param cpu_flavor: The cpu_flavor of this CreateInstanceRequestBody.
        :type cpu_flavor: str
        """
        self._cpu_flavor = cpu_flavor

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this CreateInstanceRequestBody.

        独享引擎所在VPC的ID（通过调用虚拟私有云ListVpcs接口获取所有的VPC列表查询VPC的ID，如果需要关联企业项目，则调用虚拟私有云的接口也需要关联企业项目ID）

        :return: The vpc_id of this CreateInstanceRequestBody.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this CreateInstanceRequestBody.

        独享引擎所在VPC的ID（通过调用虚拟私有云ListVpcs接口获取所有的VPC列表查询VPC的ID，如果需要关联企业项目，则调用虚拟私有云的接口也需要关联企业项目ID）

        :param vpc_id: The vpc_id of this CreateInstanceRequestBody.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def subnet_id(self):
        r"""Gets the subnet_id of this CreateInstanceRequestBody.

        独享引擎所在VPC内的子网ID（通过调用虚拟私有云ListSubnets接口获取所有的子网列表查询子网的ID，如果需要关联企业项目，则调用虚拟私有云的接口也需要关联企业项目ID）

        :return: The subnet_id of this CreateInstanceRequestBody.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        r"""Sets the subnet_id of this CreateInstanceRequestBody.

        独享引擎所在VPC内的子网ID（通过调用虚拟私有云ListSubnets接口获取所有的子网列表查询子网的ID，如果需要关联企业项目，则调用虚拟私有云的接口也需要关联企业项目ID）

        :param subnet_id: The subnet_id of this CreateInstanceRequestBody.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def security_group(self):
        r"""Gets the security_group of this CreateInstanceRequestBody.

        独享引擎需要绑定的安全组ID（通过调用虚拟私有云ListSecurityGroups接口获取所有的安全组列表查询安全组的ID，如果需要关联企业项目，则调用虚拟私有云的接口也需要关联企业项目ID）

        :return: The security_group of this CreateInstanceRequestBody.
        :rtype: list[str]
        """
        return self._security_group

    @security_group.setter
    def security_group(self, security_group):
        r"""Sets the security_group of this CreateInstanceRequestBody.

        独享引擎需要绑定的安全组ID（通过调用虚拟私有云ListSecurityGroups接口获取所有的安全组列表查询安全组的ID，如果需要关联企业项目，则调用虚拟私有云的接口也需要关联企业项目ID）

        :param security_group: The security_group of this CreateInstanceRequestBody.
        :type security_group: list[str]
        """
        self._security_group = security_group

    @property
    def count(self):
        r"""Gets the count of this CreateInstanceRequestBody.

        申请的独享引擎数量

        :return: The count of this CreateInstanceRequestBody.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this CreateInstanceRequestBody.

        申请的独享引擎数量

        :param count: The count of this CreateInstanceRequestBody.
        :type count: int
        """
        self._count = count

    @property
    def res_tenant(self):
        r"""Gets the res_tenant of this CreateInstanceRequestBody.

        是否为资源租户类，默认值为false。   - true: 资源租户类   - false: 普通租户类

        :return: The res_tenant of this CreateInstanceRequestBody.
        :rtype: bool
        """
        return self._res_tenant

    @res_tenant.setter
    def res_tenant(self, res_tenant):
        r"""Sets the res_tenant of this CreateInstanceRequestBody.

        是否为资源租户类，默认值为false。   - true: 资源租户类   - false: 普通租户类

        :param res_tenant: The res_tenant of this CreateInstanceRequestBody.
        :type res_tenant: bool
        """
        self._res_tenant = res_tenant

    @property
    def anti_affinity(self):
        r"""Gets the anti_affinity of this CreateInstanceRequestBody.

        是否开启反亲和。仅资源租户独享实例支持该特性。

        :return: The anti_affinity of this CreateInstanceRequestBody.
        :rtype: bool
        """
        return self._anti_affinity

    @anti_affinity.setter
    def anti_affinity(self, anti_affinity):
        r"""Sets the anti_affinity of this CreateInstanceRequestBody.

        是否开启反亲和。仅资源租户独享实例支持该特性。

        :param anti_affinity: The anti_affinity of this CreateInstanceRequestBody.
        :type anti_affinity: bool
        """
        self._anti_affinity = anti_affinity

    @property
    def tags(self):
        r"""Gets the tags of this CreateInstanceRequestBody.

        TMS标签信息

        :return: The tags of this CreateInstanceRequestBody.
        :rtype: list[:class:`huaweicloudsdkwaf.v1.TmsResourceTag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this CreateInstanceRequestBody.

        TMS标签信息

        :param tags: The tags of this CreateInstanceRequestBody.
        :type tags: list[:class:`huaweicloudsdkwaf.v1.TmsResourceTag`]
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
        if not isinstance(other, CreateInstanceRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
