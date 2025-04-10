# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RoleDeployMeta:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'other': 'dict(str, object)',
        'name': 'str',
        'code_name': 'str',
        'component': 'str',
        'node_preference': 'str',
        'count': 'str',
        'affinity': 'str',
        'affinity_target': 'str',
        'multi_instance': 'int',
        'role_kind': 'str',
        'constraints': 'list[str]',
        'multi_az_placement': 'str',
        'arbitration_deployment': 'bool',
        'support_elb': 'bool',
        'multi_affinity_group_enable': 'bool',
        'local_disks_anti_affinity': 'bool',
        'multi_instance_name_pattern': 'str',
        'private_ip': 'str',
        'weight': 'str'
    }

    attribute_map = {
        'other': 'other',
        'name': 'name',
        'code_name': 'code_name',
        'component': 'component',
        'node_preference': 'node_preference',
        'count': 'count',
        'affinity': 'affinity',
        'affinity_target': 'affinity_target',
        'multi_instance': 'multi_instance',
        'role_kind': 'role_kind',
        'constraints': 'constraints',
        'multi_az_placement': 'multi_az_placement',
        'arbitration_deployment': 'arbitration_deployment',
        'support_elb': 'support_elb',
        'multi_affinity_group_enable': 'multi_affinity_group_enable',
        'local_disks_anti_affinity': 'local_disks_anti_affinity',
        'multi_instance_name_pattern': 'multi_instance_name_pattern',
        'private_ip': 'private_ip',
        'weight': 'weight'
    }

    def __init__(self, other=None, name=None, code_name=None, component=None, node_preference=None, count=None, affinity=None, affinity_target=None, multi_instance=None, role_kind=None, constraints=None, multi_az_placement=None, arbitration_deployment=None, support_elb=None, multi_affinity_group_enable=None, local_disks_anti_affinity=None, multi_instance_name_pattern=None, private_ip=None, weight=None):
        r"""RoleDeployMeta

        The model defined in huaweicloud sdk

        :param other: 其他扩展属性
        :type other: dict(str, object)
        :param name: 角色名称
        :type name: str
        :param code_name: 角色简称
        :type code_name: str
        :param component: 角色所属组件
        :type component: str
        :param node_preference: 部署倾向
        :type node_preference: str
        :param count: 角色数量限制
        :type count: str
        :param affinity: 亲和
        :type affinity: str
        :param affinity_target: 亲和目标
        :type affinity_target: str
        :param multi_instance: 多实例
        :type multi_instance: int
        :param role_kind: 角色类型
        :type role_kind: str
        :param constraints: 角色限制，包含当前组件角色的一些功能限制，例如：\&quot;no_scale_in\&quot;
        :type constraints: list[str]
        :param multi_az_placement: 多az部署
        :type multi_az_placement: str
        :param arbitration_deployment: 仲裁部署
        :type arbitration_deployment: bool
        :param support_elb: 支持ELB
        :type support_elb: bool
        :param multi_affinity_group_enable: 启用多亲和组
        :type multi_affinity_group_enable: bool
        :param local_disks_anti_affinity: 本地盘反亲和
        :type local_disks_anti_affinity: bool
        :param multi_instance_name_pattern: 多实例名称模式
        :type multi_instance_name_pattern: str
        :param private_ip: 私有IP
        :type private_ip: str
        :param weight: 权重
        :type weight: str
        """
        
        

        self._other = None
        self._name = None
        self._code_name = None
        self._component = None
        self._node_preference = None
        self._count = None
        self._affinity = None
        self._affinity_target = None
        self._multi_instance = None
        self._role_kind = None
        self._constraints = None
        self._multi_az_placement = None
        self._arbitration_deployment = None
        self._support_elb = None
        self._multi_affinity_group_enable = None
        self._local_disks_anti_affinity = None
        self._multi_instance_name_pattern = None
        self._private_ip = None
        self._weight = None
        self.discriminator = None

        if other is not None:
            self.other = other
        if name is not None:
            self.name = name
        if code_name is not None:
            self.code_name = code_name
        if component is not None:
            self.component = component
        if node_preference is not None:
            self.node_preference = node_preference
        if count is not None:
            self.count = count
        if affinity is not None:
            self.affinity = affinity
        if affinity_target is not None:
            self.affinity_target = affinity_target
        if multi_instance is not None:
            self.multi_instance = multi_instance
        if role_kind is not None:
            self.role_kind = role_kind
        if constraints is not None:
            self.constraints = constraints
        if multi_az_placement is not None:
            self.multi_az_placement = multi_az_placement
        if arbitration_deployment is not None:
            self.arbitration_deployment = arbitration_deployment
        if support_elb is not None:
            self.support_elb = support_elb
        if multi_affinity_group_enable is not None:
            self.multi_affinity_group_enable = multi_affinity_group_enable
        if local_disks_anti_affinity is not None:
            self.local_disks_anti_affinity = local_disks_anti_affinity
        if multi_instance_name_pattern is not None:
            self.multi_instance_name_pattern = multi_instance_name_pattern
        if private_ip is not None:
            self.private_ip = private_ip
        if weight is not None:
            self.weight = weight

    @property
    def other(self):
        r"""Gets the other of this RoleDeployMeta.

        其他扩展属性

        :return: The other of this RoleDeployMeta.
        :rtype: dict(str, object)
        """
        return self._other

    @other.setter
    def other(self, other):
        r"""Sets the other of this RoleDeployMeta.

        其他扩展属性

        :param other: The other of this RoleDeployMeta.
        :type other: dict(str, object)
        """
        self._other = other

    @property
    def name(self):
        r"""Gets the name of this RoleDeployMeta.

        角色名称

        :return: The name of this RoleDeployMeta.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this RoleDeployMeta.

        角色名称

        :param name: The name of this RoleDeployMeta.
        :type name: str
        """
        self._name = name

    @property
    def code_name(self):
        r"""Gets the code_name of this RoleDeployMeta.

        角色简称

        :return: The code_name of this RoleDeployMeta.
        :rtype: str
        """
        return self._code_name

    @code_name.setter
    def code_name(self, code_name):
        r"""Sets the code_name of this RoleDeployMeta.

        角色简称

        :param code_name: The code_name of this RoleDeployMeta.
        :type code_name: str
        """
        self._code_name = code_name

    @property
    def component(self):
        r"""Gets the component of this RoleDeployMeta.

        角色所属组件

        :return: The component of this RoleDeployMeta.
        :rtype: str
        """
        return self._component

    @component.setter
    def component(self, component):
        r"""Sets the component of this RoleDeployMeta.

        角色所属组件

        :param component: The component of this RoleDeployMeta.
        :type component: str
        """
        self._component = component

    @property
    def node_preference(self):
        r"""Gets the node_preference of this RoleDeployMeta.

        部署倾向

        :return: The node_preference of this RoleDeployMeta.
        :rtype: str
        """
        return self._node_preference

    @node_preference.setter
    def node_preference(self, node_preference):
        r"""Sets the node_preference of this RoleDeployMeta.

        部署倾向

        :param node_preference: The node_preference of this RoleDeployMeta.
        :type node_preference: str
        """
        self._node_preference = node_preference

    @property
    def count(self):
        r"""Gets the count of this RoleDeployMeta.

        角色数量限制

        :return: The count of this RoleDeployMeta.
        :rtype: str
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this RoleDeployMeta.

        角色数量限制

        :param count: The count of this RoleDeployMeta.
        :type count: str
        """
        self._count = count

    @property
    def affinity(self):
        r"""Gets the affinity of this RoleDeployMeta.

        亲和

        :return: The affinity of this RoleDeployMeta.
        :rtype: str
        """
        return self._affinity

    @affinity.setter
    def affinity(self, affinity):
        r"""Sets the affinity of this RoleDeployMeta.

        亲和

        :param affinity: The affinity of this RoleDeployMeta.
        :type affinity: str
        """
        self._affinity = affinity

    @property
    def affinity_target(self):
        r"""Gets the affinity_target of this RoleDeployMeta.

        亲和目标

        :return: The affinity_target of this RoleDeployMeta.
        :rtype: str
        """
        return self._affinity_target

    @affinity_target.setter
    def affinity_target(self, affinity_target):
        r"""Sets the affinity_target of this RoleDeployMeta.

        亲和目标

        :param affinity_target: The affinity_target of this RoleDeployMeta.
        :type affinity_target: str
        """
        self._affinity_target = affinity_target

    @property
    def multi_instance(self):
        r"""Gets the multi_instance of this RoleDeployMeta.

        多实例

        :return: The multi_instance of this RoleDeployMeta.
        :rtype: int
        """
        return self._multi_instance

    @multi_instance.setter
    def multi_instance(self, multi_instance):
        r"""Sets the multi_instance of this RoleDeployMeta.

        多实例

        :param multi_instance: The multi_instance of this RoleDeployMeta.
        :type multi_instance: int
        """
        self._multi_instance = multi_instance

    @property
    def role_kind(self):
        r"""Gets the role_kind of this RoleDeployMeta.

        角色类型

        :return: The role_kind of this RoleDeployMeta.
        :rtype: str
        """
        return self._role_kind

    @role_kind.setter
    def role_kind(self, role_kind):
        r"""Sets the role_kind of this RoleDeployMeta.

        角色类型

        :param role_kind: The role_kind of this RoleDeployMeta.
        :type role_kind: str
        """
        self._role_kind = role_kind

    @property
    def constraints(self):
        r"""Gets the constraints of this RoleDeployMeta.

        角色限制，包含当前组件角色的一些功能限制，例如：\"no_scale_in\"

        :return: The constraints of this RoleDeployMeta.
        :rtype: list[str]
        """
        return self._constraints

    @constraints.setter
    def constraints(self, constraints):
        r"""Sets the constraints of this RoleDeployMeta.

        角色限制，包含当前组件角色的一些功能限制，例如：\"no_scale_in\"

        :param constraints: The constraints of this RoleDeployMeta.
        :type constraints: list[str]
        """
        self._constraints = constraints

    @property
    def multi_az_placement(self):
        r"""Gets the multi_az_placement of this RoleDeployMeta.

        多az部署

        :return: The multi_az_placement of this RoleDeployMeta.
        :rtype: str
        """
        return self._multi_az_placement

    @multi_az_placement.setter
    def multi_az_placement(self, multi_az_placement):
        r"""Sets the multi_az_placement of this RoleDeployMeta.

        多az部署

        :param multi_az_placement: The multi_az_placement of this RoleDeployMeta.
        :type multi_az_placement: str
        """
        self._multi_az_placement = multi_az_placement

    @property
    def arbitration_deployment(self):
        r"""Gets the arbitration_deployment of this RoleDeployMeta.

        仲裁部署

        :return: The arbitration_deployment of this RoleDeployMeta.
        :rtype: bool
        """
        return self._arbitration_deployment

    @arbitration_deployment.setter
    def arbitration_deployment(self, arbitration_deployment):
        r"""Sets the arbitration_deployment of this RoleDeployMeta.

        仲裁部署

        :param arbitration_deployment: The arbitration_deployment of this RoleDeployMeta.
        :type arbitration_deployment: bool
        """
        self._arbitration_deployment = arbitration_deployment

    @property
    def support_elb(self):
        r"""Gets the support_elb of this RoleDeployMeta.

        支持ELB

        :return: The support_elb of this RoleDeployMeta.
        :rtype: bool
        """
        return self._support_elb

    @support_elb.setter
    def support_elb(self, support_elb):
        r"""Sets the support_elb of this RoleDeployMeta.

        支持ELB

        :param support_elb: The support_elb of this RoleDeployMeta.
        :type support_elb: bool
        """
        self._support_elb = support_elb

    @property
    def multi_affinity_group_enable(self):
        r"""Gets the multi_affinity_group_enable of this RoleDeployMeta.

        启用多亲和组

        :return: The multi_affinity_group_enable of this RoleDeployMeta.
        :rtype: bool
        """
        return self._multi_affinity_group_enable

    @multi_affinity_group_enable.setter
    def multi_affinity_group_enable(self, multi_affinity_group_enable):
        r"""Sets the multi_affinity_group_enable of this RoleDeployMeta.

        启用多亲和组

        :param multi_affinity_group_enable: The multi_affinity_group_enable of this RoleDeployMeta.
        :type multi_affinity_group_enable: bool
        """
        self._multi_affinity_group_enable = multi_affinity_group_enable

    @property
    def local_disks_anti_affinity(self):
        r"""Gets the local_disks_anti_affinity of this RoleDeployMeta.

        本地盘反亲和

        :return: The local_disks_anti_affinity of this RoleDeployMeta.
        :rtype: bool
        """
        return self._local_disks_anti_affinity

    @local_disks_anti_affinity.setter
    def local_disks_anti_affinity(self, local_disks_anti_affinity):
        r"""Sets the local_disks_anti_affinity of this RoleDeployMeta.

        本地盘反亲和

        :param local_disks_anti_affinity: The local_disks_anti_affinity of this RoleDeployMeta.
        :type local_disks_anti_affinity: bool
        """
        self._local_disks_anti_affinity = local_disks_anti_affinity

    @property
    def multi_instance_name_pattern(self):
        r"""Gets the multi_instance_name_pattern of this RoleDeployMeta.

        多实例名称模式

        :return: The multi_instance_name_pattern of this RoleDeployMeta.
        :rtype: str
        """
        return self._multi_instance_name_pattern

    @multi_instance_name_pattern.setter
    def multi_instance_name_pattern(self, multi_instance_name_pattern):
        r"""Sets the multi_instance_name_pattern of this RoleDeployMeta.

        多实例名称模式

        :param multi_instance_name_pattern: The multi_instance_name_pattern of this RoleDeployMeta.
        :type multi_instance_name_pattern: str
        """
        self._multi_instance_name_pattern = multi_instance_name_pattern

    @property
    def private_ip(self):
        r"""Gets the private_ip of this RoleDeployMeta.

        私有IP

        :return: The private_ip of this RoleDeployMeta.
        :rtype: str
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, private_ip):
        r"""Sets the private_ip of this RoleDeployMeta.

        私有IP

        :param private_ip: The private_ip of this RoleDeployMeta.
        :type private_ip: str
        """
        self._private_ip = private_ip

    @property
    def weight(self):
        r"""Gets the weight of this RoleDeployMeta.

        权重

        :return: The weight of this RoleDeployMeta.
        :rtype: str
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        r"""Sets the weight of this RoleDeployMeta.

        权重

        :param weight: The weight of this RoleDeployMeta.
        :type weight: str
        """
        self._weight = weight

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
        if not isinstance(other, RoleDeployMeta):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
