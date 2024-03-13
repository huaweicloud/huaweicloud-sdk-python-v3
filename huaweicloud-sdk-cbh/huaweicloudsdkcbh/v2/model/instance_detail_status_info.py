# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InstanceDetailStatusInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status': 'str',
        'task_status': 'str',
        'create_instance_status': 'str',
        'instance_status': 'str',
        'instance_description': 'str',
        'fail_reason': 'str'
    }

    attribute_map = {
        'status': 'status',
        'task_status': 'task_status',
        'create_instance_status': 'create_instance_status',
        'instance_status': 'instance_status',
        'instance_description': 'instance_description',
        'fail_reason': 'fail_reason'
    }

    def __init__(self, status=None, task_status=None, create_instance_status=None, instance_status=None, instance_description=None, fail_reason=None):
        """InstanceDetailStatusInfo

        The model defined in huaweicloud sdk

        :param status: 云堡垒机实例状态。 - SHUTOFF：已关闭 - ACTIVE：运行中 - DELETING：删除中 - BUILD：创建中 - DELETED：已删除 - ERROR：故障 - HAWAIT：等待备机创建成功 - FROZEN：已冻结 - UPGRADING：升级中 - UNPAID：待支付 - RESIZE：规格变更中 - DILATATION：扩容中 - HA：配置HA中
        :type status: str
        :param task_status: 云堡垒机实例当前的任务状态。 - powering-on：开启 - powering-off：关闭 - rebooting：重启 - delete_wait：删除 - frozen：冻结 - NO_TASK：运行 - unfrozen：解冻 - alter：变更 - updating：升级中 - configuring-ha：配置HA - data-migrating：数据迁移中 - rollback：版本回滚中 - traffic-switchover：流量切换中
        :type task_status: str
        :param create_instance_status: 云堡垒机实例在创建实例过程中的状态信息。 - Waiting for payment：等待支付 - creating-network：创建网络 - creating-server：创建服务 - tranfering-horizontal-network：网络打通 - adding-policy-route：添加路由策略 - configing-dns：配置DNS - starting-cbs-service：服务运行中 - setting-init-conf：初始化 - buying-EIP：购买弹性公网IP
        :type create_instance_status: str
        :param instance_status: 云堡垒机实例状态。 - building：创建中 - deleting：删除中 - deleted：删除了 - unpaid：未支付 - upgrading：升级中 - resizing：扩容中 - abnormal：异常 - error：故障 - ok：正常
        :type instance_status: str
        :param instance_description: 云堡垒机实例信息描述。
        :type instance_description: str
        :param fail_reason: 云堡垒机实例创建实例失败原因。
        :type fail_reason: str
        """
        
        

        self._status = None
        self._task_status = None
        self._create_instance_status = None
        self._instance_status = None
        self._instance_description = None
        self._fail_reason = None
        self.discriminator = None

        self.status = status
        self.task_status = task_status
        self.create_instance_status = create_instance_status
        self.instance_status = instance_status
        self.instance_description = instance_description
        self.fail_reason = fail_reason

    @property
    def status(self):
        """Gets the status of this InstanceDetailStatusInfo.

        云堡垒机实例状态。 - SHUTOFF：已关闭 - ACTIVE：运行中 - DELETING：删除中 - BUILD：创建中 - DELETED：已删除 - ERROR：故障 - HAWAIT：等待备机创建成功 - FROZEN：已冻结 - UPGRADING：升级中 - UNPAID：待支付 - RESIZE：规格变更中 - DILATATION：扩容中 - HA：配置HA中

        :return: The status of this InstanceDetailStatusInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this InstanceDetailStatusInfo.

        云堡垒机实例状态。 - SHUTOFF：已关闭 - ACTIVE：运行中 - DELETING：删除中 - BUILD：创建中 - DELETED：已删除 - ERROR：故障 - HAWAIT：等待备机创建成功 - FROZEN：已冻结 - UPGRADING：升级中 - UNPAID：待支付 - RESIZE：规格变更中 - DILATATION：扩容中 - HA：配置HA中

        :param status: The status of this InstanceDetailStatusInfo.
        :type status: str
        """
        self._status = status

    @property
    def task_status(self):
        """Gets the task_status of this InstanceDetailStatusInfo.

        云堡垒机实例当前的任务状态。 - powering-on：开启 - powering-off：关闭 - rebooting：重启 - delete_wait：删除 - frozen：冻结 - NO_TASK：运行 - unfrozen：解冻 - alter：变更 - updating：升级中 - configuring-ha：配置HA - data-migrating：数据迁移中 - rollback：版本回滚中 - traffic-switchover：流量切换中

        :return: The task_status of this InstanceDetailStatusInfo.
        :rtype: str
        """
        return self._task_status

    @task_status.setter
    def task_status(self, task_status):
        """Sets the task_status of this InstanceDetailStatusInfo.

        云堡垒机实例当前的任务状态。 - powering-on：开启 - powering-off：关闭 - rebooting：重启 - delete_wait：删除 - frozen：冻结 - NO_TASK：运行 - unfrozen：解冻 - alter：变更 - updating：升级中 - configuring-ha：配置HA - data-migrating：数据迁移中 - rollback：版本回滚中 - traffic-switchover：流量切换中

        :param task_status: The task_status of this InstanceDetailStatusInfo.
        :type task_status: str
        """
        self._task_status = task_status

    @property
    def create_instance_status(self):
        """Gets the create_instance_status of this InstanceDetailStatusInfo.

        云堡垒机实例在创建实例过程中的状态信息。 - Waiting for payment：等待支付 - creating-network：创建网络 - creating-server：创建服务 - tranfering-horizontal-network：网络打通 - adding-policy-route：添加路由策略 - configing-dns：配置DNS - starting-cbs-service：服务运行中 - setting-init-conf：初始化 - buying-EIP：购买弹性公网IP

        :return: The create_instance_status of this InstanceDetailStatusInfo.
        :rtype: str
        """
        return self._create_instance_status

    @create_instance_status.setter
    def create_instance_status(self, create_instance_status):
        """Sets the create_instance_status of this InstanceDetailStatusInfo.

        云堡垒机实例在创建实例过程中的状态信息。 - Waiting for payment：等待支付 - creating-network：创建网络 - creating-server：创建服务 - tranfering-horizontal-network：网络打通 - adding-policy-route：添加路由策略 - configing-dns：配置DNS - starting-cbs-service：服务运行中 - setting-init-conf：初始化 - buying-EIP：购买弹性公网IP

        :param create_instance_status: The create_instance_status of this InstanceDetailStatusInfo.
        :type create_instance_status: str
        """
        self._create_instance_status = create_instance_status

    @property
    def instance_status(self):
        """Gets the instance_status of this InstanceDetailStatusInfo.

        云堡垒机实例状态。 - building：创建中 - deleting：删除中 - deleted：删除了 - unpaid：未支付 - upgrading：升级中 - resizing：扩容中 - abnormal：异常 - error：故障 - ok：正常

        :return: The instance_status of this InstanceDetailStatusInfo.
        :rtype: str
        """
        return self._instance_status

    @instance_status.setter
    def instance_status(self, instance_status):
        """Sets the instance_status of this InstanceDetailStatusInfo.

        云堡垒机实例状态。 - building：创建中 - deleting：删除中 - deleted：删除了 - unpaid：未支付 - upgrading：升级中 - resizing：扩容中 - abnormal：异常 - error：故障 - ok：正常

        :param instance_status: The instance_status of this InstanceDetailStatusInfo.
        :type instance_status: str
        """
        self._instance_status = instance_status

    @property
    def instance_description(self):
        """Gets the instance_description of this InstanceDetailStatusInfo.

        云堡垒机实例信息描述。

        :return: The instance_description of this InstanceDetailStatusInfo.
        :rtype: str
        """
        return self._instance_description

    @instance_description.setter
    def instance_description(self, instance_description):
        """Sets the instance_description of this InstanceDetailStatusInfo.

        云堡垒机实例信息描述。

        :param instance_description: The instance_description of this InstanceDetailStatusInfo.
        :type instance_description: str
        """
        self._instance_description = instance_description

    @property
    def fail_reason(self):
        """Gets the fail_reason of this InstanceDetailStatusInfo.

        云堡垒机实例创建实例失败原因。

        :return: The fail_reason of this InstanceDetailStatusInfo.
        :rtype: str
        """
        return self._fail_reason

    @fail_reason.setter
    def fail_reason(self, fail_reason):
        """Sets the fail_reason of this InstanceDetailStatusInfo.

        云堡垒机实例创建实例失败原因。

        :param fail_reason: The fail_reason of this InstanceDetailStatusInfo.
        :type fail_reason: str
        """
        self._fail_reason = fail_reason

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
        if not isinstance(other, InstanceDetailStatusInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
