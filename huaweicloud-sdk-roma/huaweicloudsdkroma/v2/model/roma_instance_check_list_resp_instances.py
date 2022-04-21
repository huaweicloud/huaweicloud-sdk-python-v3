# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RomaInstanceCheckListRespInstances:

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
        'flavor_id': 'str',
        'flavor_type': 'str',
        'cpu_arch': 'str',
        'vpc_id': 'str',
        'subnet_id': 'str',
        'security_group_id': 'str',
        'publicip_enable': 'bool',
        'publicip_id': 'str',
        'publicip_address': 'str',
        'status': 'str',
        'error_code': 'str',
        'error_msg': 'str',
        'charge_type': 'str',
        'project_id': 'str',
        'create_time': 'str',
        'update_time': 'str',
        'maintain_begin': 'str',
        'maintain_end': 'str',
        'available_zone_ids': 'list[str]',
        'enterprise_project_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'flavor_id': 'flavor_id',
        'flavor_type': 'flavor_type',
        'cpu_arch': 'cpu_arch',
        'vpc_id': 'vpc_id',
        'subnet_id': 'subnet_id',
        'security_group_id': 'security_group_id',
        'publicip_enable': 'publicip_enable',
        'publicip_id': 'publicip_id',
        'publicip_address': 'publicip_address',
        'status': 'status',
        'error_code': 'error_code',
        'error_msg': 'error_msg',
        'charge_type': 'charge_type',
        'project_id': 'project_id',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'maintain_begin': 'maintain_begin',
        'maintain_end': 'maintain_end',
        'available_zone_ids': 'available_zone_ids',
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, id=None, name=None, description=None, flavor_id=None, flavor_type=None, cpu_arch=None, vpc_id=None, subnet_id=None, security_group_id=None, publicip_enable=None, publicip_id=None, publicip_address=None, status=None, error_code=None, error_msg=None, charge_type=None, project_id=None, create_time=None, update_time=None, maintain_begin=None, maintain_end=None, available_zone_ids=None, enterprise_project_id=None):
        """RomaInstanceCheckListRespInstances

        The model defined in huaweicloud sdk

        :param id: 实例ID
        :type id: str
        :param name: 实例名称
        :type name: str
        :param description: 实例描述
        :type description: str
        :param flavor_id: 实例规格ID
        :type flavor_id: str
        :param flavor_type: 实例规格类型
        :type flavor_type: str
        :param cpu_arch: CPU架构类型，取值如下： - x86_64: x86架构 - aarch64: arm架构 
        :type cpu_arch: str
        :param vpc_id: 实例指定虚拟私有云ID
        :type vpc_id: str
        :param subnet_id: 实例指定虚拟私有云子网ID
        :type subnet_id: str
        :param security_group_id: 实例指定安全组ID
        :type security_group_id: str
        :param publicip_enable: 是否开启公网访问，开启时publicip_id字段必填。 
        :type publicip_enable: bool
        :param publicip_id: 实例绑定的弹性公网地址ID
        :type publicip_id: str
        :param publicip_address: 实例绑定的弹性公网地址
        :type publicip_address: str
        :param status: 实例运行状态
        :type status: str
        :param error_code: 错误码
        :type error_code: str
        :param error_msg: 错误消息
        :type error_msg: str
        :param charge_type: 实例计费模式
        :type charge_type: str
        :param project_id: 租户项目ID
        :type project_id: str
        :param create_time: 创建时间
        :type create_time: str
        :param update_time: 更新时间
        :type update_time: str
        :param maintain_begin: 运维开始时间
        :type maintain_begin: str
        :param maintain_end: 运维结束时间
        :type maintain_end: str
        :param available_zone_ids: 创实例使用的可用区列表
        :type available_zone_ids: list[str]
        :param enterprise_project_id: 实例所属企业项目ID
        :type enterprise_project_id: str
        """
        
        

        self._id = None
        self._name = None
        self._description = None
        self._flavor_id = None
        self._flavor_type = None
        self._cpu_arch = None
        self._vpc_id = None
        self._subnet_id = None
        self._security_group_id = None
        self._publicip_enable = None
        self._publicip_id = None
        self._publicip_address = None
        self._status = None
        self._error_code = None
        self._error_msg = None
        self._charge_type = None
        self._project_id = None
        self._create_time = None
        self._update_time = None
        self._maintain_begin = None
        self._maintain_end = None
        self._available_zone_ids = None
        self._enterprise_project_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if flavor_id is not None:
            self.flavor_id = flavor_id
        if flavor_type is not None:
            self.flavor_type = flavor_type
        if cpu_arch is not None:
            self.cpu_arch = cpu_arch
        if vpc_id is not None:
            self.vpc_id = vpc_id
        if subnet_id is not None:
            self.subnet_id = subnet_id
        if security_group_id is not None:
            self.security_group_id = security_group_id
        if publicip_enable is not None:
            self.publicip_enable = publicip_enable
        if publicip_id is not None:
            self.publicip_id = publicip_id
        if publicip_address is not None:
            self.publicip_address = publicip_address
        if status is not None:
            self.status = status
        if error_code is not None:
            self.error_code = error_code
        if error_msg is not None:
            self.error_msg = error_msg
        if charge_type is not None:
            self.charge_type = charge_type
        if project_id is not None:
            self.project_id = project_id
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if maintain_begin is not None:
            self.maintain_begin = maintain_begin
        if maintain_end is not None:
            self.maintain_end = maintain_end
        if available_zone_ids is not None:
            self.available_zone_ids = available_zone_ids
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id

    @property
    def id(self):
        """Gets the id of this RomaInstanceCheckListRespInstances.

        实例ID

        :return: The id of this RomaInstanceCheckListRespInstances.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this RomaInstanceCheckListRespInstances.

        实例ID

        :param id: The id of this RomaInstanceCheckListRespInstances.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this RomaInstanceCheckListRespInstances.

        实例名称

        :return: The name of this RomaInstanceCheckListRespInstances.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RomaInstanceCheckListRespInstances.

        实例名称

        :param name: The name of this RomaInstanceCheckListRespInstances.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this RomaInstanceCheckListRespInstances.

        实例描述

        :return: The description of this RomaInstanceCheckListRespInstances.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this RomaInstanceCheckListRespInstances.

        实例描述

        :param description: The description of this RomaInstanceCheckListRespInstances.
        :type description: str
        """
        self._description = description

    @property
    def flavor_id(self):
        """Gets the flavor_id of this RomaInstanceCheckListRespInstances.

        实例规格ID

        :return: The flavor_id of this RomaInstanceCheckListRespInstances.
        :rtype: str
        """
        return self._flavor_id

    @flavor_id.setter
    def flavor_id(self, flavor_id):
        """Sets the flavor_id of this RomaInstanceCheckListRespInstances.

        实例规格ID

        :param flavor_id: The flavor_id of this RomaInstanceCheckListRespInstances.
        :type flavor_id: str
        """
        self._flavor_id = flavor_id

    @property
    def flavor_type(self):
        """Gets the flavor_type of this RomaInstanceCheckListRespInstances.

        实例规格类型

        :return: The flavor_type of this RomaInstanceCheckListRespInstances.
        :rtype: str
        """
        return self._flavor_type

    @flavor_type.setter
    def flavor_type(self, flavor_type):
        """Sets the flavor_type of this RomaInstanceCheckListRespInstances.

        实例规格类型

        :param flavor_type: The flavor_type of this RomaInstanceCheckListRespInstances.
        :type flavor_type: str
        """
        self._flavor_type = flavor_type

    @property
    def cpu_arch(self):
        """Gets the cpu_arch of this RomaInstanceCheckListRespInstances.

        CPU架构类型，取值如下： - x86_64: x86架构 - aarch64: arm架构 

        :return: The cpu_arch of this RomaInstanceCheckListRespInstances.
        :rtype: str
        """
        return self._cpu_arch

    @cpu_arch.setter
    def cpu_arch(self, cpu_arch):
        """Sets the cpu_arch of this RomaInstanceCheckListRespInstances.

        CPU架构类型，取值如下： - x86_64: x86架构 - aarch64: arm架构 

        :param cpu_arch: The cpu_arch of this RomaInstanceCheckListRespInstances.
        :type cpu_arch: str
        """
        self._cpu_arch = cpu_arch

    @property
    def vpc_id(self):
        """Gets the vpc_id of this RomaInstanceCheckListRespInstances.

        实例指定虚拟私有云ID

        :return: The vpc_id of this RomaInstanceCheckListRespInstances.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this RomaInstanceCheckListRespInstances.

        实例指定虚拟私有云ID

        :param vpc_id: The vpc_id of this RomaInstanceCheckListRespInstances.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def subnet_id(self):
        """Gets the subnet_id of this RomaInstanceCheckListRespInstances.

        实例指定虚拟私有云子网ID

        :return: The subnet_id of this RomaInstanceCheckListRespInstances.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """Sets the subnet_id of this RomaInstanceCheckListRespInstances.

        实例指定虚拟私有云子网ID

        :param subnet_id: The subnet_id of this RomaInstanceCheckListRespInstances.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def security_group_id(self):
        """Gets the security_group_id of this RomaInstanceCheckListRespInstances.

        实例指定安全组ID

        :return: The security_group_id of this RomaInstanceCheckListRespInstances.
        :rtype: str
        """
        return self._security_group_id

    @security_group_id.setter
    def security_group_id(self, security_group_id):
        """Sets the security_group_id of this RomaInstanceCheckListRespInstances.

        实例指定安全组ID

        :param security_group_id: The security_group_id of this RomaInstanceCheckListRespInstances.
        :type security_group_id: str
        """
        self._security_group_id = security_group_id

    @property
    def publicip_enable(self):
        """Gets the publicip_enable of this RomaInstanceCheckListRespInstances.

        是否开启公网访问，开启时publicip_id字段必填。 

        :return: The publicip_enable of this RomaInstanceCheckListRespInstances.
        :rtype: bool
        """
        return self._publicip_enable

    @publicip_enable.setter
    def publicip_enable(self, publicip_enable):
        """Sets the publicip_enable of this RomaInstanceCheckListRespInstances.

        是否开启公网访问，开启时publicip_id字段必填。 

        :param publicip_enable: The publicip_enable of this RomaInstanceCheckListRespInstances.
        :type publicip_enable: bool
        """
        self._publicip_enable = publicip_enable

    @property
    def publicip_id(self):
        """Gets the publicip_id of this RomaInstanceCheckListRespInstances.

        实例绑定的弹性公网地址ID

        :return: The publicip_id of this RomaInstanceCheckListRespInstances.
        :rtype: str
        """
        return self._publicip_id

    @publicip_id.setter
    def publicip_id(self, publicip_id):
        """Sets the publicip_id of this RomaInstanceCheckListRespInstances.

        实例绑定的弹性公网地址ID

        :param publicip_id: The publicip_id of this RomaInstanceCheckListRespInstances.
        :type publicip_id: str
        """
        self._publicip_id = publicip_id

    @property
    def publicip_address(self):
        """Gets the publicip_address of this RomaInstanceCheckListRespInstances.

        实例绑定的弹性公网地址

        :return: The publicip_address of this RomaInstanceCheckListRespInstances.
        :rtype: str
        """
        return self._publicip_address

    @publicip_address.setter
    def publicip_address(self, publicip_address):
        """Sets the publicip_address of this RomaInstanceCheckListRespInstances.

        实例绑定的弹性公网地址

        :param publicip_address: The publicip_address of this RomaInstanceCheckListRespInstances.
        :type publicip_address: str
        """
        self._publicip_address = publicip_address

    @property
    def status(self):
        """Gets the status of this RomaInstanceCheckListRespInstances.

        实例运行状态

        :return: The status of this RomaInstanceCheckListRespInstances.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this RomaInstanceCheckListRespInstances.

        实例运行状态

        :param status: The status of this RomaInstanceCheckListRespInstances.
        :type status: str
        """
        self._status = status

    @property
    def error_code(self):
        """Gets the error_code of this RomaInstanceCheckListRespInstances.

        错误码

        :return: The error_code of this RomaInstanceCheckListRespInstances.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this RomaInstanceCheckListRespInstances.

        错误码

        :param error_code: The error_code of this RomaInstanceCheckListRespInstances.
        :type error_code: str
        """
        self._error_code = error_code

    @property
    def error_msg(self):
        """Gets the error_msg of this RomaInstanceCheckListRespInstances.

        错误消息

        :return: The error_msg of this RomaInstanceCheckListRespInstances.
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        """Sets the error_msg of this RomaInstanceCheckListRespInstances.

        错误消息

        :param error_msg: The error_msg of this RomaInstanceCheckListRespInstances.
        :type error_msg: str
        """
        self._error_msg = error_msg

    @property
    def charge_type(self):
        """Gets the charge_type of this RomaInstanceCheckListRespInstances.

        实例计费模式

        :return: The charge_type of this RomaInstanceCheckListRespInstances.
        :rtype: str
        """
        return self._charge_type

    @charge_type.setter
    def charge_type(self, charge_type):
        """Sets the charge_type of this RomaInstanceCheckListRespInstances.

        实例计费模式

        :param charge_type: The charge_type of this RomaInstanceCheckListRespInstances.
        :type charge_type: str
        """
        self._charge_type = charge_type

    @property
    def project_id(self):
        """Gets the project_id of this RomaInstanceCheckListRespInstances.

        租户项目ID

        :return: The project_id of this RomaInstanceCheckListRespInstances.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this RomaInstanceCheckListRespInstances.

        租户项目ID

        :param project_id: The project_id of this RomaInstanceCheckListRespInstances.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def create_time(self):
        """Gets the create_time of this RomaInstanceCheckListRespInstances.

        创建时间

        :return: The create_time of this RomaInstanceCheckListRespInstances.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this RomaInstanceCheckListRespInstances.

        创建时间

        :param create_time: The create_time of this RomaInstanceCheckListRespInstances.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this RomaInstanceCheckListRespInstances.

        更新时间

        :return: The update_time of this RomaInstanceCheckListRespInstances.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this RomaInstanceCheckListRespInstances.

        更新时间

        :param update_time: The update_time of this RomaInstanceCheckListRespInstances.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def maintain_begin(self):
        """Gets the maintain_begin of this RomaInstanceCheckListRespInstances.

        运维开始时间

        :return: The maintain_begin of this RomaInstanceCheckListRespInstances.
        :rtype: str
        """
        return self._maintain_begin

    @maintain_begin.setter
    def maintain_begin(self, maintain_begin):
        """Sets the maintain_begin of this RomaInstanceCheckListRespInstances.

        运维开始时间

        :param maintain_begin: The maintain_begin of this RomaInstanceCheckListRespInstances.
        :type maintain_begin: str
        """
        self._maintain_begin = maintain_begin

    @property
    def maintain_end(self):
        """Gets the maintain_end of this RomaInstanceCheckListRespInstances.

        运维结束时间

        :return: The maintain_end of this RomaInstanceCheckListRespInstances.
        :rtype: str
        """
        return self._maintain_end

    @maintain_end.setter
    def maintain_end(self, maintain_end):
        """Sets the maintain_end of this RomaInstanceCheckListRespInstances.

        运维结束时间

        :param maintain_end: The maintain_end of this RomaInstanceCheckListRespInstances.
        :type maintain_end: str
        """
        self._maintain_end = maintain_end

    @property
    def available_zone_ids(self):
        """Gets the available_zone_ids of this RomaInstanceCheckListRespInstances.

        创实例使用的可用区列表

        :return: The available_zone_ids of this RomaInstanceCheckListRespInstances.
        :rtype: list[str]
        """
        return self._available_zone_ids

    @available_zone_ids.setter
    def available_zone_ids(self, available_zone_ids):
        """Sets the available_zone_ids of this RomaInstanceCheckListRespInstances.

        创实例使用的可用区列表

        :param available_zone_ids: The available_zone_ids of this RomaInstanceCheckListRespInstances.
        :type available_zone_ids: list[str]
        """
        self._available_zone_ids = available_zone_ids

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this RomaInstanceCheckListRespInstances.

        实例所属企业项目ID

        :return: The enterprise_project_id of this RomaInstanceCheckListRespInstances.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this RomaInstanceCheckListRespInstances.

        实例所属企业项目ID

        :param enterprise_project_id: The enterprise_project_id of this RomaInstanceCheckListRespInstances.
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
        if not isinstance(other, RomaInstanceCheckListRespInstances):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
