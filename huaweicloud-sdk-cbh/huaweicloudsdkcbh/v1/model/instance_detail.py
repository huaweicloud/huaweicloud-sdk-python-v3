# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InstanceDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'publicip': 'str',
        'exp_time': 'str',
        'start_time': 'str',
        'end_time': 'str',
        'release_time': 'str',
        'name': 'str',
        'instance_id': 'str',
        'private_ip': 'str',
        'task_status': 'str',
        'status': 'str',
        'created': 'str',
        'region': 'str',
        'zone': 'str',
        'availability_zone_display': 'str',
        'vpc_id': 'str',
        'subnet_id': 'str',
        'security_group_id': 'str',
        'specification': 'str',
        'update': 'str',
        'createinstance_status': 'str',
        'fail_reason': 'str',
        'instance_key': 'str',
        'order_id': 'str',
        'period_num': 'str',
        'resource_id': 'str',
        'bastion_type': 'str',
        'public_id': 'str',
        'alter_permit': 'str',
        'bastion_version': 'str',
        'new_bastion_version': 'str',
        'instance_status': 'str',
        'instance_description': 'str'
    }

    attribute_map = {
        'publicip': 'publicip',
        'exp_time': 'exp_time',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'release_time': 'release_time',
        'name': 'name',
        'instance_id': 'instance_id',
        'private_ip': 'private_ip',
        'task_status': 'task_status',
        'status': 'status',
        'created': 'created',
        'region': 'region',
        'zone': 'zone',
        'availability_zone_display': 'availability_zone_display',
        'vpc_id': 'vpc_id',
        'subnet_id': 'subnet_id',
        'security_group_id': 'security_group_id',
        'specification': 'specification',
        'update': 'update',
        'createinstance_status': 'createinstance_status',
        'fail_reason': 'fail_reason',
        'instance_key': 'instance_key',
        'order_id': 'order_id',
        'period_num': 'period_num',
        'resource_id': 'resource_id',
        'bastion_type': 'bastion_type',
        'public_id': 'public_id',
        'alter_permit': 'alter_permit',
        'bastion_version': 'bastion_version',
        'new_bastion_version': 'new_bastion_version',
        'instance_status': 'instance_status',
        'instance_description': 'instance_description'
    }

    def __init__(self, publicip=None, exp_time=None, start_time=None, end_time=None, release_time=None, name=None, instance_id=None, private_ip=None, task_status=None, status=None, created=None, region=None, zone=None, availability_zone_display=None, vpc_id=None, subnet_id=None, security_group_id=None, specification=None, update=None, createinstance_status=None, fail_reason=None, instance_key=None, order_id=None, period_num=None, resource_id=None, bastion_type=None, public_id=None, alter_permit=None, bastion_version=None, new_bastion_version=None, instance_status=None, instance_description=None):
        """InstanceDetail

        The model defined in huaweicloud sdk

        :param publicip: 弹性ip
        :type publicip: str
        :param exp_time: 过期时间
        :type exp_time: str
        :param start_time: 开始时间
        :type start_time: str
        :param end_time: 结束时间
        :type end_time: str
        :param release_time: 释放时间
        :type release_time: str
        :param name: 实例名称
        :type name: str
        :param instance_id: 实例的server id
        :type instance_id: str
        :param private_ip: 实例私有ip
        :type private_ip: str
        :param task_status: 实例当前的任务状态
        :type task_status: str
        :param status: 实例状态
        :type status: str
        :param created: 实例创建时间
        :type created: str
        :param region: 实例所在region
        :type region: str
        :param zone: 实例所在可用区id
        :type zone: str
        :param availability_zone_display: 实例所在可用区名称
        :type availability_zone_display: str
        :param vpc_id: 实例所在vpc的id
        :type vpc_id: str
        :param subnet_id: 实例所在子网的id
        :type subnet_id: str
        :param security_group_id: 实例所属的安全组的id
        :type security_group_id: str
        :param specification: 实例规格
        :type specification: str
        :param update: 实例镜像是否可以升级
        :type update: str
        :param createinstance_status: 在创建实例过程中的过程状态信息
        :type createinstance_status: str
        :param fail_reason: 创建实例失败原因
        :type fail_reason: str
        :param instance_key: 实例ID
        :type instance_key: str
        :param order_id: 订单id
        :type order_id: str
        :param period_num: 租户购买的时长
        :type period_num: str
        :param resource_id: 实例的资源id
        :type resource_id: str
        :param bastion_type: 堡垒机类型
        :type bastion_type: str
        :param public_id: 实例绑定的弹性IP的id
        :type public_id: str
        :param alter_permit: 前端是否显示扩容按钮
        :type alter_permit: str
        :param bastion_version: 实例镜像当前版本号
        :type bastion_version: str
        :param new_bastion_version: 实例镜像最新版本号
        :type new_bastion_version: str
        :param instance_status: 实例状态
        :type instance_status: str
        :param instance_description: 实例描述
        :type instance_description: str
        """
        
        

        self._publicip = None
        self._exp_time = None
        self._start_time = None
        self._end_time = None
        self._release_time = None
        self._name = None
        self._instance_id = None
        self._private_ip = None
        self._task_status = None
        self._status = None
        self._created = None
        self._region = None
        self._zone = None
        self._availability_zone_display = None
        self._vpc_id = None
        self._subnet_id = None
        self._security_group_id = None
        self._specification = None
        self._update = None
        self._createinstance_status = None
        self._fail_reason = None
        self._instance_key = None
        self._order_id = None
        self._period_num = None
        self._resource_id = None
        self._bastion_type = None
        self._public_id = None
        self._alter_permit = None
        self._bastion_version = None
        self._new_bastion_version = None
        self._instance_status = None
        self._instance_description = None
        self.discriminator = None

        self.publicip = publicip
        if exp_time is not None:
            self.exp_time = exp_time
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if release_time is not None:
            self.release_time = release_time
        self.name = name
        if instance_id is not None:
            self.instance_id = instance_id
        if private_ip is not None:
            self.private_ip = private_ip
        if task_status is not None:
            self.task_status = task_status
        self.status = status
        self.created = created
        self.region = region
        self.zone = zone
        self.availability_zone_display = availability_zone_display
        if vpc_id is not None:
            self.vpc_id = vpc_id
        if subnet_id is not None:
            self.subnet_id = subnet_id
        if security_group_id is not None:
            self.security_group_id = security_group_id
        self.specification = specification
        self.update = update
        if createinstance_status is not None:
            self.createinstance_status = createinstance_status
        if fail_reason is not None:
            self.fail_reason = fail_reason
        if instance_key is not None:
            self.instance_key = instance_key
        if order_id is not None:
            self.order_id = order_id
        if period_num is not None:
            self.period_num = period_num
        if resource_id is not None:
            self.resource_id = resource_id
        self.bastion_type = bastion_type
        if public_id is not None:
            self.public_id = public_id
        if alter_permit is not None:
            self.alter_permit = alter_permit
        if bastion_version is not None:
            self.bastion_version = bastion_version
        if new_bastion_version is not None:
            self.new_bastion_version = new_bastion_version
        if instance_status is not None:
            self.instance_status = instance_status
        if instance_description is not None:
            self.instance_description = instance_description

    @property
    def publicip(self):
        """Gets the publicip of this InstanceDetail.

        弹性ip

        :return: The publicip of this InstanceDetail.
        :rtype: str
        """
        return self._publicip

    @publicip.setter
    def publicip(self, publicip):
        """Sets the publicip of this InstanceDetail.

        弹性ip

        :param publicip: The publicip of this InstanceDetail.
        :type publicip: str
        """
        self._publicip = publicip

    @property
    def exp_time(self):
        """Gets the exp_time of this InstanceDetail.

        过期时间

        :return: The exp_time of this InstanceDetail.
        :rtype: str
        """
        return self._exp_time

    @exp_time.setter
    def exp_time(self, exp_time):
        """Sets the exp_time of this InstanceDetail.

        过期时间

        :param exp_time: The exp_time of this InstanceDetail.
        :type exp_time: str
        """
        self._exp_time = exp_time

    @property
    def start_time(self):
        """Gets the start_time of this InstanceDetail.

        开始时间

        :return: The start_time of this InstanceDetail.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this InstanceDetail.

        开始时间

        :param start_time: The start_time of this InstanceDetail.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this InstanceDetail.

        结束时间

        :return: The end_time of this InstanceDetail.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this InstanceDetail.

        结束时间

        :param end_time: The end_time of this InstanceDetail.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def release_time(self):
        """Gets the release_time of this InstanceDetail.

        释放时间

        :return: The release_time of this InstanceDetail.
        :rtype: str
        """
        return self._release_time

    @release_time.setter
    def release_time(self, release_time):
        """Sets the release_time of this InstanceDetail.

        释放时间

        :param release_time: The release_time of this InstanceDetail.
        :type release_time: str
        """
        self._release_time = release_time

    @property
    def name(self):
        """Gets the name of this InstanceDetail.

        实例名称

        :return: The name of this InstanceDetail.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InstanceDetail.

        实例名称

        :param name: The name of this InstanceDetail.
        :type name: str
        """
        self._name = name

    @property
    def instance_id(self):
        """Gets the instance_id of this InstanceDetail.

        实例的server id

        :return: The instance_id of this InstanceDetail.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this InstanceDetail.

        实例的server id

        :param instance_id: The instance_id of this InstanceDetail.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def private_ip(self):
        """Gets the private_ip of this InstanceDetail.

        实例私有ip

        :return: The private_ip of this InstanceDetail.
        :rtype: str
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, private_ip):
        """Sets the private_ip of this InstanceDetail.

        实例私有ip

        :param private_ip: The private_ip of this InstanceDetail.
        :type private_ip: str
        """
        self._private_ip = private_ip

    @property
    def task_status(self):
        """Gets the task_status of this InstanceDetail.

        实例当前的任务状态

        :return: The task_status of this InstanceDetail.
        :rtype: str
        """
        return self._task_status

    @task_status.setter
    def task_status(self, task_status):
        """Sets the task_status of this InstanceDetail.

        实例当前的任务状态

        :param task_status: The task_status of this InstanceDetail.
        :type task_status: str
        """
        self._task_status = task_status

    @property
    def status(self):
        """Gets the status of this InstanceDetail.

        实例状态

        :return: The status of this InstanceDetail.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this InstanceDetail.

        实例状态

        :param status: The status of this InstanceDetail.
        :type status: str
        """
        self._status = status

    @property
    def created(self):
        """Gets the created of this InstanceDetail.

        实例创建时间

        :return: The created of this InstanceDetail.
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this InstanceDetail.

        实例创建时间

        :param created: The created of this InstanceDetail.
        :type created: str
        """
        self._created = created

    @property
    def region(self):
        """Gets the region of this InstanceDetail.

        实例所在region

        :return: The region of this InstanceDetail.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this InstanceDetail.

        实例所在region

        :param region: The region of this InstanceDetail.
        :type region: str
        """
        self._region = region

    @property
    def zone(self):
        """Gets the zone of this InstanceDetail.

        实例所在可用区id

        :return: The zone of this InstanceDetail.
        :rtype: str
        """
        return self._zone

    @zone.setter
    def zone(self, zone):
        """Sets the zone of this InstanceDetail.

        实例所在可用区id

        :param zone: The zone of this InstanceDetail.
        :type zone: str
        """
        self._zone = zone

    @property
    def availability_zone_display(self):
        """Gets the availability_zone_display of this InstanceDetail.

        实例所在可用区名称

        :return: The availability_zone_display of this InstanceDetail.
        :rtype: str
        """
        return self._availability_zone_display

    @availability_zone_display.setter
    def availability_zone_display(self, availability_zone_display):
        """Sets the availability_zone_display of this InstanceDetail.

        实例所在可用区名称

        :param availability_zone_display: The availability_zone_display of this InstanceDetail.
        :type availability_zone_display: str
        """
        self._availability_zone_display = availability_zone_display

    @property
    def vpc_id(self):
        """Gets the vpc_id of this InstanceDetail.

        实例所在vpc的id

        :return: The vpc_id of this InstanceDetail.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this InstanceDetail.

        实例所在vpc的id

        :param vpc_id: The vpc_id of this InstanceDetail.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def subnet_id(self):
        """Gets the subnet_id of this InstanceDetail.

        实例所在子网的id

        :return: The subnet_id of this InstanceDetail.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """Sets the subnet_id of this InstanceDetail.

        实例所在子网的id

        :param subnet_id: The subnet_id of this InstanceDetail.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def security_group_id(self):
        """Gets the security_group_id of this InstanceDetail.

        实例所属的安全组的id

        :return: The security_group_id of this InstanceDetail.
        :rtype: str
        """
        return self._security_group_id

    @security_group_id.setter
    def security_group_id(self, security_group_id):
        """Sets the security_group_id of this InstanceDetail.

        实例所属的安全组的id

        :param security_group_id: The security_group_id of this InstanceDetail.
        :type security_group_id: str
        """
        self._security_group_id = security_group_id

    @property
    def specification(self):
        """Gets the specification of this InstanceDetail.

        实例规格

        :return: The specification of this InstanceDetail.
        :rtype: str
        """
        return self._specification

    @specification.setter
    def specification(self, specification):
        """Sets the specification of this InstanceDetail.

        实例规格

        :param specification: The specification of this InstanceDetail.
        :type specification: str
        """
        self._specification = specification

    @property
    def update(self):
        """Gets the update of this InstanceDetail.

        实例镜像是否可以升级

        :return: The update of this InstanceDetail.
        :rtype: str
        """
        return self._update

    @update.setter
    def update(self, update):
        """Sets the update of this InstanceDetail.

        实例镜像是否可以升级

        :param update: The update of this InstanceDetail.
        :type update: str
        """
        self._update = update

    @property
    def createinstance_status(self):
        """Gets the createinstance_status of this InstanceDetail.

        在创建实例过程中的过程状态信息

        :return: The createinstance_status of this InstanceDetail.
        :rtype: str
        """
        return self._createinstance_status

    @createinstance_status.setter
    def createinstance_status(self, createinstance_status):
        """Sets the createinstance_status of this InstanceDetail.

        在创建实例过程中的过程状态信息

        :param createinstance_status: The createinstance_status of this InstanceDetail.
        :type createinstance_status: str
        """
        self._createinstance_status = createinstance_status

    @property
    def fail_reason(self):
        """Gets the fail_reason of this InstanceDetail.

        创建实例失败原因

        :return: The fail_reason of this InstanceDetail.
        :rtype: str
        """
        return self._fail_reason

    @fail_reason.setter
    def fail_reason(self, fail_reason):
        """Sets the fail_reason of this InstanceDetail.

        创建实例失败原因

        :param fail_reason: The fail_reason of this InstanceDetail.
        :type fail_reason: str
        """
        self._fail_reason = fail_reason

    @property
    def instance_key(self):
        """Gets the instance_key of this InstanceDetail.

        实例ID

        :return: The instance_key of this InstanceDetail.
        :rtype: str
        """
        return self._instance_key

    @instance_key.setter
    def instance_key(self, instance_key):
        """Sets the instance_key of this InstanceDetail.

        实例ID

        :param instance_key: The instance_key of this InstanceDetail.
        :type instance_key: str
        """
        self._instance_key = instance_key

    @property
    def order_id(self):
        """Gets the order_id of this InstanceDetail.

        订单id

        :return: The order_id of this InstanceDetail.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this InstanceDetail.

        订单id

        :param order_id: The order_id of this InstanceDetail.
        :type order_id: str
        """
        self._order_id = order_id

    @property
    def period_num(self):
        """Gets the period_num of this InstanceDetail.

        租户购买的时长

        :return: The period_num of this InstanceDetail.
        :rtype: str
        """
        return self._period_num

    @period_num.setter
    def period_num(self, period_num):
        """Sets the period_num of this InstanceDetail.

        租户购买的时长

        :param period_num: The period_num of this InstanceDetail.
        :type period_num: str
        """
        self._period_num = period_num

    @property
    def resource_id(self):
        """Gets the resource_id of this InstanceDetail.

        实例的资源id

        :return: The resource_id of this InstanceDetail.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this InstanceDetail.

        实例的资源id

        :param resource_id: The resource_id of this InstanceDetail.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def bastion_type(self):
        """Gets the bastion_type of this InstanceDetail.

        堡垒机类型

        :return: The bastion_type of this InstanceDetail.
        :rtype: str
        """
        return self._bastion_type

    @bastion_type.setter
    def bastion_type(self, bastion_type):
        """Sets the bastion_type of this InstanceDetail.

        堡垒机类型

        :param bastion_type: The bastion_type of this InstanceDetail.
        :type bastion_type: str
        """
        self._bastion_type = bastion_type

    @property
    def public_id(self):
        """Gets the public_id of this InstanceDetail.

        实例绑定的弹性IP的id

        :return: The public_id of this InstanceDetail.
        :rtype: str
        """
        return self._public_id

    @public_id.setter
    def public_id(self, public_id):
        """Sets the public_id of this InstanceDetail.

        实例绑定的弹性IP的id

        :param public_id: The public_id of this InstanceDetail.
        :type public_id: str
        """
        self._public_id = public_id

    @property
    def alter_permit(self):
        """Gets the alter_permit of this InstanceDetail.

        前端是否显示扩容按钮

        :return: The alter_permit of this InstanceDetail.
        :rtype: str
        """
        return self._alter_permit

    @alter_permit.setter
    def alter_permit(self, alter_permit):
        """Sets the alter_permit of this InstanceDetail.

        前端是否显示扩容按钮

        :param alter_permit: The alter_permit of this InstanceDetail.
        :type alter_permit: str
        """
        self._alter_permit = alter_permit

    @property
    def bastion_version(self):
        """Gets the bastion_version of this InstanceDetail.

        实例镜像当前版本号

        :return: The bastion_version of this InstanceDetail.
        :rtype: str
        """
        return self._bastion_version

    @bastion_version.setter
    def bastion_version(self, bastion_version):
        """Sets the bastion_version of this InstanceDetail.

        实例镜像当前版本号

        :param bastion_version: The bastion_version of this InstanceDetail.
        :type bastion_version: str
        """
        self._bastion_version = bastion_version

    @property
    def new_bastion_version(self):
        """Gets the new_bastion_version of this InstanceDetail.

        实例镜像最新版本号

        :return: The new_bastion_version of this InstanceDetail.
        :rtype: str
        """
        return self._new_bastion_version

    @new_bastion_version.setter
    def new_bastion_version(self, new_bastion_version):
        """Sets the new_bastion_version of this InstanceDetail.

        实例镜像最新版本号

        :param new_bastion_version: The new_bastion_version of this InstanceDetail.
        :type new_bastion_version: str
        """
        self._new_bastion_version = new_bastion_version

    @property
    def instance_status(self):
        """Gets the instance_status of this InstanceDetail.

        实例状态

        :return: The instance_status of this InstanceDetail.
        :rtype: str
        """
        return self._instance_status

    @instance_status.setter
    def instance_status(self, instance_status):
        """Sets the instance_status of this InstanceDetail.

        实例状态

        :param instance_status: The instance_status of this InstanceDetail.
        :type instance_status: str
        """
        self._instance_status = instance_status

    @property
    def instance_description(self):
        """Gets the instance_description of this InstanceDetail.

        实例描述

        :return: The instance_description of this InstanceDetail.
        :rtype: str
        """
        return self._instance_description

    @instance_description.setter
    def instance_description(self, instance_description):
        """Sets the instance_description of this InstanceDetail.

        实例描述

        :param instance_description: The instance_description of this InstanceDetail.
        :type instance_description: str
        """
        self._instance_description = instance_description

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
        if not isinstance(other, InstanceDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
