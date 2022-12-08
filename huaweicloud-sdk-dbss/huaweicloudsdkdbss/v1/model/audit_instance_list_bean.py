# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AuditInstanceListBean:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'charge_model': 'str',
        'comment': 'str',
        'config_num': 'int',
        'connect_ip': 'str',
        'connect_ipv6': 'str',
        'cpu': 'int',
        'created': 'str',
        'database_limit': 'int',
        'effect': 'int',
        'expired': 'str',
        'id': 'str',
        'keep_days': 'str',
        'name': 'str',
        'new_version': 'str',
        'port_id': 'str',
        'ram': 'int',
        'region': 'str',
        'remain_days': 'str',
        'resource_id': 'str',
        'resource_spec_code': 'str',
        'scene': 'str',
        'security_group_id': 'str',
        'specification': 'str',
        'status': 'str',
        'subnet_id': 'str',
        'task': 'str',
        'version': 'str',
        'vpc_id': 'str',
        'zone': 'str'
    }

    attribute_map = {
        'charge_model': 'charge_model',
        'comment': 'comment',
        'config_num': 'config_num',
        'connect_ip': 'connect_ip',
        'connect_ipv6': 'connect_ipv6',
        'cpu': 'cpu',
        'created': 'created',
        'database_limit': 'database_limit',
        'effect': 'effect',
        'expired': 'expired',
        'id': 'id',
        'keep_days': 'keep_days',
        'name': 'name',
        'new_version': 'new_version',
        'port_id': 'port_id',
        'ram': 'ram',
        'region': 'region',
        'remain_days': 'remain_days',
        'resource_id': 'resource_id',
        'resource_spec_code': 'resource_spec_code',
        'scene': 'scene',
        'security_group_id': 'security_group_id',
        'specification': 'specification',
        'status': 'status',
        'subnet_id': 'subnet_id',
        'task': 'task',
        'version': 'version',
        'vpc_id': 'vpc_id',
        'zone': 'zone'
    }

    def __init__(self, charge_model=None, comment=None, config_num=None, connect_ip=None, connect_ipv6=None, cpu=None, created=None, database_limit=None, effect=None, expired=None, id=None, keep_days=None, name=None, new_version=None, port_id=None, ram=None, region=None, remain_days=None, resource_id=None, resource_spec_code=None, scene=None, security_group_id=None, specification=None, status=None, subnet_id=None, task=None, version=None, vpc_id=None, zone=None):
        """AuditInstanceListBean

        The model defined in huaweicloud sdk

        :param charge_model: 付费模式 Period：包周期 Demand：按需。
        :type charge_model: str
        :param comment: 备注信息。
        :type comment: str
        :param config_num: 配置的数据库总数。
        :type config_num: int
        :param connect_ip: 连接地址。
        :type connect_ip: str
        :param connect_ipv6: ipv6连接地址。
        :type connect_ipv6: str
        :param cpu: CPU个数
        :type cpu: int
        :param created: 创建时间
        :type created: str
        :param database_limit: 支持的数据库总数
        :type database_limit: int
        :param effect: 1.冻结可释放  2.冻结不可释放 3.冻结后不可续费
        :type effect: int
        :param expired: 过期时间
        :type expired: str
        :param id: ID
        :type id: str
        :param keep_days: 剩余天数
        :type keep_days: str
        :param name: 实例别名
        :type name: str
        :param new_version: 如果有返回，则需要升级，如果没有，则为null
        :type new_version: str
        :param port_id: 绑定弹性IP的portID
        :type port_id: str
        :param ram: 内存
        :type ram: int
        :param region: 实例所在region
        :type region: str
        :param remain_days: 到期天数
        :type remain_days: str
        :param resource_id: 资源ID
        :type resource_id: str
        :param resource_spec_code: 实例的规格
        :type resource_spec_code: str
        :param scene: 场景
        :type scene: str
        :param security_group_id: 安全组
        :type security_group_id: str
        :param specification: 实例规格
        :type specification: str
        :param status: 实例状态： SHUTOFF(已关闭) ACTIVE(运行中，允许任何操作) DELETING(删除中，不允许任何操作) BUILD(创建中，不允许任何操作) DELETED(已删除，不需要展示) ERROR(故障，只允许删除) HAWAIT(等待备机创建成功，不允许任何操作) FROZEN(已冻结，只允许续费、绑定/解绑) UPGRADING(升级中，不允许升级操作)
        :type status: str
        :param subnet_id: 子网ID
        :type subnet_id: str
        :param task: 任务状态： powering-on(正在开启，实例可以绑定、解绑) powering-off(正在关闭，实例可以绑定、解绑) rebooting(正在重启，实例可以绑定、解绑) delete_wait(等待删除，集群与实例不允许任何操作) NO_TASK(不展示)
        :type task: str
        :param version: 实例的当前版本
        :type version: str
        :param vpc_id: 虚拟私有云
        :type vpc_id: str
        :param zone: 可用区
        :type zone: str
        """
        
        

        self._charge_model = None
        self._comment = None
        self._config_num = None
        self._connect_ip = None
        self._connect_ipv6 = None
        self._cpu = None
        self._created = None
        self._database_limit = None
        self._effect = None
        self._expired = None
        self._id = None
        self._keep_days = None
        self._name = None
        self._new_version = None
        self._port_id = None
        self._ram = None
        self._region = None
        self._remain_days = None
        self._resource_id = None
        self._resource_spec_code = None
        self._scene = None
        self._security_group_id = None
        self._specification = None
        self._status = None
        self._subnet_id = None
        self._task = None
        self._version = None
        self._vpc_id = None
        self._zone = None
        self.discriminator = None

        self.charge_model = charge_model
        self.comment = comment
        self.config_num = config_num
        self.connect_ip = connect_ip
        self.connect_ipv6 = connect_ipv6
        self.cpu = cpu
        self.created = created
        self.database_limit = database_limit
        self.effect = effect
        self.expired = expired
        self.id = id
        self.keep_days = keep_days
        self.name = name
        self.new_version = new_version
        self.port_id = port_id
        self.ram = ram
        self.region = region
        self.remain_days = remain_days
        self.resource_id = resource_id
        self.resource_spec_code = resource_spec_code
        self.scene = scene
        self.security_group_id = security_group_id
        self.specification = specification
        self.status = status
        self.subnet_id = subnet_id
        self.task = task
        self.version = version
        self.vpc_id = vpc_id
        self.zone = zone

    @property
    def charge_model(self):
        """Gets the charge_model of this AuditInstanceListBean.

        付费模式 Period：包周期 Demand：按需。

        :return: The charge_model of this AuditInstanceListBean.
        :rtype: str
        """
        return self._charge_model

    @charge_model.setter
    def charge_model(self, charge_model):
        """Sets the charge_model of this AuditInstanceListBean.

        付费模式 Period：包周期 Demand：按需。

        :param charge_model: The charge_model of this AuditInstanceListBean.
        :type charge_model: str
        """
        self._charge_model = charge_model

    @property
    def comment(self):
        """Gets the comment of this AuditInstanceListBean.

        备注信息。

        :return: The comment of this AuditInstanceListBean.
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this AuditInstanceListBean.

        备注信息。

        :param comment: The comment of this AuditInstanceListBean.
        :type comment: str
        """
        self._comment = comment

    @property
    def config_num(self):
        """Gets the config_num of this AuditInstanceListBean.

        配置的数据库总数。

        :return: The config_num of this AuditInstanceListBean.
        :rtype: int
        """
        return self._config_num

    @config_num.setter
    def config_num(self, config_num):
        """Sets the config_num of this AuditInstanceListBean.

        配置的数据库总数。

        :param config_num: The config_num of this AuditInstanceListBean.
        :type config_num: int
        """
        self._config_num = config_num

    @property
    def connect_ip(self):
        """Gets the connect_ip of this AuditInstanceListBean.

        连接地址。

        :return: The connect_ip of this AuditInstanceListBean.
        :rtype: str
        """
        return self._connect_ip

    @connect_ip.setter
    def connect_ip(self, connect_ip):
        """Sets the connect_ip of this AuditInstanceListBean.

        连接地址。

        :param connect_ip: The connect_ip of this AuditInstanceListBean.
        :type connect_ip: str
        """
        self._connect_ip = connect_ip

    @property
    def connect_ipv6(self):
        """Gets the connect_ipv6 of this AuditInstanceListBean.

        ipv6连接地址。

        :return: The connect_ipv6 of this AuditInstanceListBean.
        :rtype: str
        """
        return self._connect_ipv6

    @connect_ipv6.setter
    def connect_ipv6(self, connect_ipv6):
        """Sets the connect_ipv6 of this AuditInstanceListBean.

        ipv6连接地址。

        :param connect_ipv6: The connect_ipv6 of this AuditInstanceListBean.
        :type connect_ipv6: str
        """
        self._connect_ipv6 = connect_ipv6

    @property
    def cpu(self):
        """Gets the cpu of this AuditInstanceListBean.

        CPU个数

        :return: The cpu of this AuditInstanceListBean.
        :rtype: int
        """
        return self._cpu

    @cpu.setter
    def cpu(self, cpu):
        """Sets the cpu of this AuditInstanceListBean.

        CPU个数

        :param cpu: The cpu of this AuditInstanceListBean.
        :type cpu: int
        """
        self._cpu = cpu

    @property
    def created(self):
        """Gets the created of this AuditInstanceListBean.

        创建时间

        :return: The created of this AuditInstanceListBean.
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this AuditInstanceListBean.

        创建时间

        :param created: The created of this AuditInstanceListBean.
        :type created: str
        """
        self._created = created

    @property
    def database_limit(self):
        """Gets the database_limit of this AuditInstanceListBean.

        支持的数据库总数

        :return: The database_limit of this AuditInstanceListBean.
        :rtype: int
        """
        return self._database_limit

    @database_limit.setter
    def database_limit(self, database_limit):
        """Sets the database_limit of this AuditInstanceListBean.

        支持的数据库总数

        :param database_limit: The database_limit of this AuditInstanceListBean.
        :type database_limit: int
        """
        self._database_limit = database_limit

    @property
    def effect(self):
        """Gets the effect of this AuditInstanceListBean.

        1.冻结可释放  2.冻结不可释放 3.冻结后不可续费

        :return: The effect of this AuditInstanceListBean.
        :rtype: int
        """
        return self._effect

    @effect.setter
    def effect(self, effect):
        """Sets the effect of this AuditInstanceListBean.

        1.冻结可释放  2.冻结不可释放 3.冻结后不可续费

        :param effect: The effect of this AuditInstanceListBean.
        :type effect: int
        """
        self._effect = effect

    @property
    def expired(self):
        """Gets the expired of this AuditInstanceListBean.

        过期时间

        :return: The expired of this AuditInstanceListBean.
        :rtype: str
        """
        return self._expired

    @expired.setter
    def expired(self, expired):
        """Sets the expired of this AuditInstanceListBean.

        过期时间

        :param expired: The expired of this AuditInstanceListBean.
        :type expired: str
        """
        self._expired = expired

    @property
    def id(self):
        """Gets the id of this AuditInstanceListBean.

        ID

        :return: The id of this AuditInstanceListBean.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AuditInstanceListBean.

        ID

        :param id: The id of this AuditInstanceListBean.
        :type id: str
        """
        self._id = id

    @property
    def keep_days(self):
        """Gets the keep_days of this AuditInstanceListBean.

        剩余天数

        :return: The keep_days of this AuditInstanceListBean.
        :rtype: str
        """
        return self._keep_days

    @keep_days.setter
    def keep_days(self, keep_days):
        """Sets the keep_days of this AuditInstanceListBean.

        剩余天数

        :param keep_days: The keep_days of this AuditInstanceListBean.
        :type keep_days: str
        """
        self._keep_days = keep_days

    @property
    def name(self):
        """Gets the name of this AuditInstanceListBean.

        实例别名

        :return: The name of this AuditInstanceListBean.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AuditInstanceListBean.

        实例别名

        :param name: The name of this AuditInstanceListBean.
        :type name: str
        """
        self._name = name

    @property
    def new_version(self):
        """Gets the new_version of this AuditInstanceListBean.

        如果有返回，则需要升级，如果没有，则为null

        :return: The new_version of this AuditInstanceListBean.
        :rtype: str
        """
        return self._new_version

    @new_version.setter
    def new_version(self, new_version):
        """Sets the new_version of this AuditInstanceListBean.

        如果有返回，则需要升级，如果没有，则为null

        :param new_version: The new_version of this AuditInstanceListBean.
        :type new_version: str
        """
        self._new_version = new_version

    @property
    def port_id(self):
        """Gets the port_id of this AuditInstanceListBean.

        绑定弹性IP的portID

        :return: The port_id of this AuditInstanceListBean.
        :rtype: str
        """
        return self._port_id

    @port_id.setter
    def port_id(self, port_id):
        """Sets the port_id of this AuditInstanceListBean.

        绑定弹性IP的portID

        :param port_id: The port_id of this AuditInstanceListBean.
        :type port_id: str
        """
        self._port_id = port_id

    @property
    def ram(self):
        """Gets the ram of this AuditInstanceListBean.

        内存

        :return: The ram of this AuditInstanceListBean.
        :rtype: int
        """
        return self._ram

    @ram.setter
    def ram(self, ram):
        """Sets the ram of this AuditInstanceListBean.

        内存

        :param ram: The ram of this AuditInstanceListBean.
        :type ram: int
        """
        self._ram = ram

    @property
    def region(self):
        """Gets the region of this AuditInstanceListBean.

        实例所在region

        :return: The region of this AuditInstanceListBean.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this AuditInstanceListBean.

        实例所在region

        :param region: The region of this AuditInstanceListBean.
        :type region: str
        """
        self._region = region

    @property
    def remain_days(self):
        """Gets the remain_days of this AuditInstanceListBean.

        到期天数

        :return: The remain_days of this AuditInstanceListBean.
        :rtype: str
        """
        return self._remain_days

    @remain_days.setter
    def remain_days(self, remain_days):
        """Sets the remain_days of this AuditInstanceListBean.

        到期天数

        :param remain_days: The remain_days of this AuditInstanceListBean.
        :type remain_days: str
        """
        self._remain_days = remain_days

    @property
    def resource_id(self):
        """Gets the resource_id of this AuditInstanceListBean.

        资源ID

        :return: The resource_id of this AuditInstanceListBean.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this AuditInstanceListBean.

        资源ID

        :param resource_id: The resource_id of this AuditInstanceListBean.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def resource_spec_code(self):
        """Gets the resource_spec_code of this AuditInstanceListBean.

        实例的规格

        :return: The resource_spec_code of this AuditInstanceListBean.
        :rtype: str
        """
        return self._resource_spec_code

    @resource_spec_code.setter
    def resource_spec_code(self, resource_spec_code):
        """Sets the resource_spec_code of this AuditInstanceListBean.

        实例的规格

        :param resource_spec_code: The resource_spec_code of this AuditInstanceListBean.
        :type resource_spec_code: str
        """
        self._resource_spec_code = resource_spec_code

    @property
    def scene(self):
        """Gets the scene of this AuditInstanceListBean.

        场景

        :return: The scene of this AuditInstanceListBean.
        :rtype: str
        """
        return self._scene

    @scene.setter
    def scene(self, scene):
        """Sets the scene of this AuditInstanceListBean.

        场景

        :param scene: The scene of this AuditInstanceListBean.
        :type scene: str
        """
        self._scene = scene

    @property
    def security_group_id(self):
        """Gets the security_group_id of this AuditInstanceListBean.

        安全组

        :return: The security_group_id of this AuditInstanceListBean.
        :rtype: str
        """
        return self._security_group_id

    @security_group_id.setter
    def security_group_id(self, security_group_id):
        """Sets the security_group_id of this AuditInstanceListBean.

        安全组

        :param security_group_id: The security_group_id of this AuditInstanceListBean.
        :type security_group_id: str
        """
        self._security_group_id = security_group_id

    @property
    def specification(self):
        """Gets the specification of this AuditInstanceListBean.

        实例规格

        :return: The specification of this AuditInstanceListBean.
        :rtype: str
        """
        return self._specification

    @specification.setter
    def specification(self, specification):
        """Sets the specification of this AuditInstanceListBean.

        实例规格

        :param specification: The specification of this AuditInstanceListBean.
        :type specification: str
        """
        self._specification = specification

    @property
    def status(self):
        """Gets the status of this AuditInstanceListBean.

        实例状态： SHUTOFF(已关闭) ACTIVE(运行中，允许任何操作) DELETING(删除中，不允许任何操作) BUILD(创建中，不允许任何操作) DELETED(已删除，不需要展示) ERROR(故障，只允许删除) HAWAIT(等待备机创建成功，不允许任何操作) FROZEN(已冻结，只允许续费、绑定/解绑) UPGRADING(升级中，不允许升级操作)

        :return: The status of this AuditInstanceListBean.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this AuditInstanceListBean.

        实例状态： SHUTOFF(已关闭) ACTIVE(运行中，允许任何操作) DELETING(删除中，不允许任何操作) BUILD(创建中，不允许任何操作) DELETED(已删除，不需要展示) ERROR(故障，只允许删除) HAWAIT(等待备机创建成功，不允许任何操作) FROZEN(已冻结，只允许续费、绑定/解绑) UPGRADING(升级中，不允许升级操作)

        :param status: The status of this AuditInstanceListBean.
        :type status: str
        """
        self._status = status

    @property
    def subnet_id(self):
        """Gets the subnet_id of this AuditInstanceListBean.

        子网ID

        :return: The subnet_id of this AuditInstanceListBean.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """Sets the subnet_id of this AuditInstanceListBean.

        子网ID

        :param subnet_id: The subnet_id of this AuditInstanceListBean.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def task(self):
        """Gets the task of this AuditInstanceListBean.

        任务状态： powering-on(正在开启，实例可以绑定、解绑) powering-off(正在关闭，实例可以绑定、解绑) rebooting(正在重启，实例可以绑定、解绑) delete_wait(等待删除，集群与实例不允许任何操作) NO_TASK(不展示)

        :return: The task of this AuditInstanceListBean.
        :rtype: str
        """
        return self._task

    @task.setter
    def task(self, task):
        """Sets the task of this AuditInstanceListBean.

        任务状态： powering-on(正在开启，实例可以绑定、解绑) powering-off(正在关闭，实例可以绑定、解绑) rebooting(正在重启，实例可以绑定、解绑) delete_wait(等待删除，集群与实例不允许任何操作) NO_TASK(不展示)

        :param task: The task of this AuditInstanceListBean.
        :type task: str
        """
        self._task = task

    @property
    def version(self):
        """Gets the version of this AuditInstanceListBean.

        实例的当前版本

        :return: The version of this AuditInstanceListBean.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this AuditInstanceListBean.

        实例的当前版本

        :param version: The version of this AuditInstanceListBean.
        :type version: str
        """
        self._version = version

    @property
    def vpc_id(self):
        """Gets the vpc_id of this AuditInstanceListBean.

        虚拟私有云

        :return: The vpc_id of this AuditInstanceListBean.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this AuditInstanceListBean.

        虚拟私有云

        :param vpc_id: The vpc_id of this AuditInstanceListBean.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def zone(self):
        """Gets the zone of this AuditInstanceListBean.

        可用区

        :return: The zone of this AuditInstanceListBean.
        :rtype: str
        """
        return self._zone

    @zone.setter
    def zone(self, zone):
        """Sets the zone of this AuditInstanceListBean.

        可用区

        :param zone: The zone of this AuditInstanceListBean.
        :type zone: str
        """
        self._zone = zone

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
        if not isinstance(other, AuditInstanceListBean):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
