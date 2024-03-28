# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GlobalConnectionBandwidth:

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
        'domain_id': 'str',
        'bordercross': 'bool',
        'type': 'str',
        'binding_service': 'str',
        'enterprise_project_id': 'str',
        'charge_mode': 'str',
        'size': 'int',
        'sla_level': 'str',
        'local_area': 'str',
        'remote_area': 'str',
        'local_site_code': 'str',
        'remote_site_code': 'str',
        'admin_state': 'str',
        'frozen': 'bool',
        'spec_code_id': 'str',
        'tags': 'list[Tag]',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'enable_share': 'bool',
        'instances': 'list[GlobalConnectionBandwidthAssociatedInstance]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'domain_id': 'domain_id',
        'bordercross': 'bordercross',
        'type': 'type',
        'binding_service': 'binding_service',
        'enterprise_project_id': 'enterprise_project_id',
        'charge_mode': 'charge_mode',
        'size': 'size',
        'sla_level': 'sla_level',
        'local_area': 'local_area',
        'remote_area': 'remote_area',
        'local_site_code': 'local_site_code',
        'remote_site_code': 'remote_site_code',
        'admin_state': 'admin_state',
        'frozen': 'frozen',
        'spec_code_id': 'spec_code_id',
        'tags': 'tags',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'enable_share': 'enable_share',
        'instances': 'instances'
    }

    def __init__(self, id=None, name=None, description=None, domain_id=None, bordercross=None, type=None, binding_service=None, enterprise_project_id=None, charge_mode=None, size=None, sla_level=None, local_area=None, remote_area=None, local_site_code=None, remote_site_code=None, admin_state=None, frozen=None, spec_code_id=None, tags=None, created_at=None, updated_at=None, enable_share=None, instances=None):
        """GlobalConnectionBandwidth

        The model defined in huaweicloud sdk

        :param id: 资源ID标识符。
        :type id: str
        :param name: 实例名字。
        :type name: str
        :param description: 实例描述。不支持 &lt;&gt;。
        :type description: str
        :param domain_id: 实例所属帐号ID。
        :type domain_id: str
        :param bordercross: 功能说明：全域互联带宽是否跨境，判断依据：带宽是否涉及从中国大陆到其他国家。 取值范围：True：跨境；False：非跨境 
        :type bordercross: bool
        :param type: 功能说明：描述带宽类型，对应地理区间的城域、区域、大区、跨区四级： - TrsArea: 跨区带宽 - Area: 大区带宽 - SubArea: 区域带宽 - Region: 城域带宽
        :type type: str
        :param binding_service: 功能说明：绑定的服务类型。实例类型： - CC: 云连接 - GEIP: 全域弹性公网IP - GCN: 中心网络 - GSN: 分支网络 - ALL: 所有实例类型
        :type binding_service: str
        :param enterprise_project_id: 实例所属企业项目ID。
        :type enterprise_project_id: str
        :param charge_mode: 功能说明：描述计费类型，描述可选计费类型。默认开放按带宽计费，传统95计费租户白名单控制。 取值范围：     bwd: 按带宽计费     95: 按传统型95计费
        :type charge_mode: str
        :param size: 功能说明：全域互联带宽实例中的带宽值大小，单位Mbit/s。 取值范围：2-300Mbit/s
        :type size: int
        :param sla_level: 功能说明：描述网络等级，从高到低分为铂金、金、银。默认金，其余租户白名单控制。 - Pt: 铂金 - Au: 金 - Ag: 银
        :type sla_level: str
        :param local_area: 功能说明：本端接入点的中英文名。通过HEADER里面的x-language控制，默认英文，zh-cn返回中文。
        :type local_area: str
        :param remote_area: 功能说明：远端接入点的中英文名。通过HEADER里面的x-language控制，默认英文，zh-cn返回中文。
        :type remote_area: str
        :param local_site_code: 功能说明：本端接入点的编码。
        :type local_site_code: str
        :param remote_site_code: 功能说明：远端接入点的编码。
        :type remote_site_code: str
        :param admin_state: 功能说明: 全域互联带宽状态。 取值范围：     NORMAL-正常     FREEZED-冻结状态
        :type admin_state: str
        :param frozen: 功能说明: 全域互联带宽是否冻结。 取值范围：     true-冻结     false-非冻结
        :type frozen: bool
        :param spec_code_id: 功能说明：线路规格编码UUID。
        :type spec_code_id: str
        :param tags: 实例标签。
        :type tags: list[:class:`huaweicloudsdkcc.v3.Tag`]
        :param created_at: 实例创建时间。UTC时间格式，yyyy-MM-ddTHH:mm:ss。
        :type created_at: datetime
        :param updated_at: 实例更新时间。UTC时间格式，yyyy-MM-ddTHH:mm:ss。
        :type updated_at: datetime
        :param enable_share: 功能说明: 全域互联带宽是否支持绑定多实例。 取值范围：     true-支持     false-不支持
        :type enable_share: bool
        :param instances: 功能说明: 全域互联带宽绑定实例列表。
        :type instances: list[:class:`huaweicloudsdkcc.v3.GlobalConnectionBandwidthAssociatedInstance`]
        """
        
        

        self._id = None
        self._name = None
        self._description = None
        self._domain_id = None
        self._bordercross = None
        self._type = None
        self._binding_service = None
        self._enterprise_project_id = None
        self._charge_mode = None
        self._size = None
        self._sla_level = None
        self._local_area = None
        self._remote_area = None
        self._local_site_code = None
        self._remote_site_code = None
        self._admin_state = None
        self._frozen = None
        self._spec_code_id = None
        self._tags = None
        self._created_at = None
        self._updated_at = None
        self._enable_share = None
        self._instances = None
        self.discriminator = None

        self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        self.domain_id = domain_id
        if bordercross is not None:
            self.bordercross = bordercross
        if type is not None:
            self.type = type
        if binding_service is not None:
            self.binding_service = binding_service
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if charge_mode is not None:
            self.charge_mode = charge_mode
        if size is not None:
            self.size = size
        if sla_level is not None:
            self.sla_level = sla_level
        if local_area is not None:
            self.local_area = local_area
        if remote_area is not None:
            self.remote_area = remote_area
        if local_site_code is not None:
            self.local_site_code = local_site_code
        if remote_site_code is not None:
            self.remote_site_code = remote_site_code
        if admin_state is not None:
            self.admin_state = admin_state
        if frozen is not None:
            self.frozen = frozen
        if spec_code_id is not None:
            self.spec_code_id = spec_code_id
        if tags is not None:
            self.tags = tags
        self.created_at = created_at
        self.updated_at = updated_at
        if enable_share is not None:
            self.enable_share = enable_share
        if instances is not None:
            self.instances = instances

    @property
    def id(self):
        """Gets the id of this GlobalConnectionBandwidth.

        资源ID标识符。

        :return: The id of this GlobalConnectionBandwidth.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GlobalConnectionBandwidth.

        资源ID标识符。

        :param id: The id of this GlobalConnectionBandwidth.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this GlobalConnectionBandwidth.

        实例名字。

        :return: The name of this GlobalConnectionBandwidth.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GlobalConnectionBandwidth.

        实例名字。

        :param name: The name of this GlobalConnectionBandwidth.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this GlobalConnectionBandwidth.

        实例描述。不支持 <>。

        :return: The description of this GlobalConnectionBandwidth.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this GlobalConnectionBandwidth.

        实例描述。不支持 <>。

        :param description: The description of this GlobalConnectionBandwidth.
        :type description: str
        """
        self._description = description

    @property
    def domain_id(self):
        """Gets the domain_id of this GlobalConnectionBandwidth.

        实例所属帐号ID。

        :return: The domain_id of this GlobalConnectionBandwidth.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this GlobalConnectionBandwidth.

        实例所属帐号ID。

        :param domain_id: The domain_id of this GlobalConnectionBandwidth.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def bordercross(self):
        """Gets the bordercross of this GlobalConnectionBandwidth.

        功能说明：全域互联带宽是否跨境，判断依据：带宽是否涉及从中国大陆到其他国家。 取值范围：True：跨境；False：非跨境 

        :return: The bordercross of this GlobalConnectionBandwidth.
        :rtype: bool
        """
        return self._bordercross

    @bordercross.setter
    def bordercross(self, bordercross):
        """Sets the bordercross of this GlobalConnectionBandwidth.

        功能说明：全域互联带宽是否跨境，判断依据：带宽是否涉及从中国大陆到其他国家。 取值范围：True：跨境；False：非跨境 

        :param bordercross: The bordercross of this GlobalConnectionBandwidth.
        :type bordercross: bool
        """
        self._bordercross = bordercross

    @property
    def type(self):
        """Gets the type of this GlobalConnectionBandwidth.

        功能说明：描述带宽类型，对应地理区间的城域、区域、大区、跨区四级： - TrsArea: 跨区带宽 - Area: 大区带宽 - SubArea: 区域带宽 - Region: 城域带宽

        :return: The type of this GlobalConnectionBandwidth.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this GlobalConnectionBandwidth.

        功能说明：描述带宽类型，对应地理区间的城域、区域、大区、跨区四级： - TrsArea: 跨区带宽 - Area: 大区带宽 - SubArea: 区域带宽 - Region: 城域带宽

        :param type: The type of this GlobalConnectionBandwidth.
        :type type: str
        """
        self._type = type

    @property
    def binding_service(self):
        """Gets the binding_service of this GlobalConnectionBandwidth.

        功能说明：绑定的服务类型。实例类型： - CC: 云连接 - GEIP: 全域弹性公网IP - GCN: 中心网络 - GSN: 分支网络 - ALL: 所有实例类型

        :return: The binding_service of this GlobalConnectionBandwidth.
        :rtype: str
        """
        return self._binding_service

    @binding_service.setter
    def binding_service(self, binding_service):
        """Sets the binding_service of this GlobalConnectionBandwidth.

        功能说明：绑定的服务类型。实例类型： - CC: 云连接 - GEIP: 全域弹性公网IP - GCN: 中心网络 - GSN: 分支网络 - ALL: 所有实例类型

        :param binding_service: The binding_service of this GlobalConnectionBandwidth.
        :type binding_service: str
        """
        self._binding_service = binding_service

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this GlobalConnectionBandwidth.

        实例所属企业项目ID。

        :return: The enterprise_project_id of this GlobalConnectionBandwidth.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this GlobalConnectionBandwidth.

        实例所属企业项目ID。

        :param enterprise_project_id: The enterprise_project_id of this GlobalConnectionBandwidth.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def charge_mode(self):
        """Gets the charge_mode of this GlobalConnectionBandwidth.

        功能说明：描述计费类型，描述可选计费类型。默认开放按带宽计费，传统95计费租户白名单控制。 取值范围：     bwd: 按带宽计费     95: 按传统型95计费

        :return: The charge_mode of this GlobalConnectionBandwidth.
        :rtype: str
        """
        return self._charge_mode

    @charge_mode.setter
    def charge_mode(self, charge_mode):
        """Sets the charge_mode of this GlobalConnectionBandwidth.

        功能说明：描述计费类型，描述可选计费类型。默认开放按带宽计费，传统95计费租户白名单控制。 取值范围：     bwd: 按带宽计费     95: 按传统型95计费

        :param charge_mode: The charge_mode of this GlobalConnectionBandwidth.
        :type charge_mode: str
        """
        self._charge_mode = charge_mode

    @property
    def size(self):
        """Gets the size of this GlobalConnectionBandwidth.

        功能说明：全域互联带宽实例中的带宽值大小，单位Mbit/s。 取值范围：2-300Mbit/s

        :return: The size of this GlobalConnectionBandwidth.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this GlobalConnectionBandwidth.

        功能说明：全域互联带宽实例中的带宽值大小，单位Mbit/s。 取值范围：2-300Mbit/s

        :param size: The size of this GlobalConnectionBandwidth.
        :type size: int
        """
        self._size = size

    @property
    def sla_level(self):
        """Gets the sla_level of this GlobalConnectionBandwidth.

        功能说明：描述网络等级，从高到低分为铂金、金、银。默认金，其余租户白名单控制。 - Pt: 铂金 - Au: 金 - Ag: 银

        :return: The sla_level of this GlobalConnectionBandwidth.
        :rtype: str
        """
        return self._sla_level

    @sla_level.setter
    def sla_level(self, sla_level):
        """Sets the sla_level of this GlobalConnectionBandwidth.

        功能说明：描述网络等级，从高到低分为铂金、金、银。默认金，其余租户白名单控制。 - Pt: 铂金 - Au: 金 - Ag: 银

        :param sla_level: The sla_level of this GlobalConnectionBandwidth.
        :type sla_level: str
        """
        self._sla_level = sla_level

    @property
    def local_area(self):
        """Gets the local_area of this GlobalConnectionBandwidth.

        功能说明：本端接入点的中英文名。通过HEADER里面的x-language控制，默认英文，zh-cn返回中文。

        :return: The local_area of this GlobalConnectionBandwidth.
        :rtype: str
        """
        return self._local_area

    @local_area.setter
    def local_area(self, local_area):
        """Sets the local_area of this GlobalConnectionBandwidth.

        功能说明：本端接入点的中英文名。通过HEADER里面的x-language控制，默认英文，zh-cn返回中文。

        :param local_area: The local_area of this GlobalConnectionBandwidth.
        :type local_area: str
        """
        self._local_area = local_area

    @property
    def remote_area(self):
        """Gets the remote_area of this GlobalConnectionBandwidth.

        功能说明：远端接入点的中英文名。通过HEADER里面的x-language控制，默认英文，zh-cn返回中文。

        :return: The remote_area of this GlobalConnectionBandwidth.
        :rtype: str
        """
        return self._remote_area

    @remote_area.setter
    def remote_area(self, remote_area):
        """Sets the remote_area of this GlobalConnectionBandwidth.

        功能说明：远端接入点的中英文名。通过HEADER里面的x-language控制，默认英文，zh-cn返回中文。

        :param remote_area: The remote_area of this GlobalConnectionBandwidth.
        :type remote_area: str
        """
        self._remote_area = remote_area

    @property
    def local_site_code(self):
        """Gets the local_site_code of this GlobalConnectionBandwidth.

        功能说明：本端接入点的编码。

        :return: The local_site_code of this GlobalConnectionBandwidth.
        :rtype: str
        """
        return self._local_site_code

    @local_site_code.setter
    def local_site_code(self, local_site_code):
        """Sets the local_site_code of this GlobalConnectionBandwidth.

        功能说明：本端接入点的编码。

        :param local_site_code: The local_site_code of this GlobalConnectionBandwidth.
        :type local_site_code: str
        """
        self._local_site_code = local_site_code

    @property
    def remote_site_code(self):
        """Gets the remote_site_code of this GlobalConnectionBandwidth.

        功能说明：远端接入点的编码。

        :return: The remote_site_code of this GlobalConnectionBandwidth.
        :rtype: str
        """
        return self._remote_site_code

    @remote_site_code.setter
    def remote_site_code(self, remote_site_code):
        """Sets the remote_site_code of this GlobalConnectionBandwidth.

        功能说明：远端接入点的编码。

        :param remote_site_code: The remote_site_code of this GlobalConnectionBandwidth.
        :type remote_site_code: str
        """
        self._remote_site_code = remote_site_code

    @property
    def admin_state(self):
        """Gets the admin_state of this GlobalConnectionBandwidth.

        功能说明: 全域互联带宽状态。 取值范围：     NORMAL-正常     FREEZED-冻结状态

        :return: The admin_state of this GlobalConnectionBandwidth.
        :rtype: str
        """
        return self._admin_state

    @admin_state.setter
    def admin_state(self, admin_state):
        """Sets the admin_state of this GlobalConnectionBandwidth.

        功能说明: 全域互联带宽状态。 取值范围：     NORMAL-正常     FREEZED-冻结状态

        :param admin_state: The admin_state of this GlobalConnectionBandwidth.
        :type admin_state: str
        """
        self._admin_state = admin_state

    @property
    def frozen(self):
        """Gets the frozen of this GlobalConnectionBandwidth.

        功能说明: 全域互联带宽是否冻结。 取值范围：     true-冻结     false-非冻结

        :return: The frozen of this GlobalConnectionBandwidth.
        :rtype: bool
        """
        return self._frozen

    @frozen.setter
    def frozen(self, frozen):
        """Sets the frozen of this GlobalConnectionBandwidth.

        功能说明: 全域互联带宽是否冻结。 取值范围：     true-冻结     false-非冻结

        :param frozen: The frozen of this GlobalConnectionBandwidth.
        :type frozen: bool
        """
        self._frozen = frozen

    @property
    def spec_code_id(self):
        """Gets the spec_code_id of this GlobalConnectionBandwidth.

        功能说明：线路规格编码UUID。

        :return: The spec_code_id of this GlobalConnectionBandwidth.
        :rtype: str
        """
        return self._spec_code_id

    @spec_code_id.setter
    def spec_code_id(self, spec_code_id):
        """Sets the spec_code_id of this GlobalConnectionBandwidth.

        功能说明：线路规格编码UUID。

        :param spec_code_id: The spec_code_id of this GlobalConnectionBandwidth.
        :type spec_code_id: str
        """
        self._spec_code_id = spec_code_id

    @property
    def tags(self):
        """Gets the tags of this GlobalConnectionBandwidth.

        实例标签。

        :return: The tags of this GlobalConnectionBandwidth.
        :rtype: list[:class:`huaweicloudsdkcc.v3.Tag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this GlobalConnectionBandwidth.

        实例标签。

        :param tags: The tags of this GlobalConnectionBandwidth.
        :type tags: list[:class:`huaweicloudsdkcc.v3.Tag`]
        """
        self._tags = tags

    @property
    def created_at(self):
        """Gets the created_at of this GlobalConnectionBandwidth.

        实例创建时间。UTC时间格式，yyyy-MM-ddTHH:mm:ss。

        :return: The created_at of this GlobalConnectionBandwidth.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this GlobalConnectionBandwidth.

        实例创建时间。UTC时间格式，yyyy-MM-ddTHH:mm:ss。

        :param created_at: The created_at of this GlobalConnectionBandwidth.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this GlobalConnectionBandwidth.

        实例更新时间。UTC时间格式，yyyy-MM-ddTHH:mm:ss。

        :return: The updated_at of this GlobalConnectionBandwidth.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this GlobalConnectionBandwidth.

        实例更新时间。UTC时间格式，yyyy-MM-ddTHH:mm:ss。

        :param updated_at: The updated_at of this GlobalConnectionBandwidth.
        :type updated_at: datetime
        """
        self._updated_at = updated_at

    @property
    def enable_share(self):
        """Gets the enable_share of this GlobalConnectionBandwidth.

        功能说明: 全域互联带宽是否支持绑定多实例。 取值范围：     true-支持     false-不支持

        :return: The enable_share of this GlobalConnectionBandwidth.
        :rtype: bool
        """
        return self._enable_share

    @enable_share.setter
    def enable_share(self, enable_share):
        """Sets the enable_share of this GlobalConnectionBandwidth.

        功能说明: 全域互联带宽是否支持绑定多实例。 取值范围：     true-支持     false-不支持

        :param enable_share: The enable_share of this GlobalConnectionBandwidth.
        :type enable_share: bool
        """
        self._enable_share = enable_share

    @property
    def instances(self):
        """Gets the instances of this GlobalConnectionBandwidth.

        功能说明: 全域互联带宽绑定实例列表。

        :return: The instances of this GlobalConnectionBandwidth.
        :rtype: list[:class:`huaweicloudsdkcc.v3.GlobalConnectionBandwidthAssociatedInstance`]
        """
        return self._instances

    @instances.setter
    def instances(self, instances):
        """Sets the instances of this GlobalConnectionBandwidth.

        功能说明: 全域互联带宽绑定实例列表。

        :param instances: The instances of this GlobalConnectionBandwidth.
        :type instances: list[:class:`huaweicloudsdkcc.v3.GlobalConnectionBandwidthAssociatedInstance`]
        """
        self._instances = instances

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
        if not isinstance(other, GlobalConnectionBandwidth):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
