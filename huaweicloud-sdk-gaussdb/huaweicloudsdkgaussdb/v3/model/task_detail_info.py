# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TaskDetailInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'instance_name': 'str',
        'instance_status': 'str',
        'job_id': 'str',
        'order_id': 'str',
        'job_name': 'str',
        'status': 'str',
        'process': 'str',
        'created_time': 'str',
        'ended_time': 'str',
        'fail_reason': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'instance_name': 'instance_name',
        'instance_status': 'instance_status',
        'job_id': 'job_id',
        'order_id': 'order_id',
        'job_name': 'job_name',
        'status': 'status',
        'process': 'process',
        'created_time': 'created_time',
        'ended_time': 'ended_time',
        'fail_reason': 'fail_reason'
    }

    def __init__(self, instance_id=None, instance_name=None, instance_status=None, job_id=None, order_id=None, job_name=None, status=None, process=None, created_time=None, ended_time=None, fail_reason=None):
        r"""TaskDetailInfo

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID。
        :type instance_id: str
        :param instance_name: 实例名称。
        :type instance_name: str
        :param instance_status: 实例状态。 取值： - 值为“createfail”，表示实例创建失败。 - 值为“creating”，表示实例创建中。 - 值为“normal”，表示实例正常。 - 值为“abnormal”，表示实例异常。 - 值为“deleted”，表示实例已删除。
        :type instance_status: str
        :param job_id: 任务ID。
        :type job_id: str
        :param order_id: 订单ID。
        :type order_id: str
        :param job_name: 任务名称。取值有：    - \&quot;CreateGaussDBforMySQLInstance\&quot;表示创建实例。    - \&quot;RestoreGaussDBforMySQLNewInstance\&quot;表示恢复新实例。    - \&quot;AddGaussDBforMySQLNodes\&quot;表示添加节点。    - \&quot;DeleteGaussDBforMySQLNode\&quot;表示删除节点。    - \&quot;RebootGaussDBforMySQLInstance\&quot;表示重启实例。    - \&quot;ModifyGaussDBforMySQLPort\&quot;表示修改实例端口。    - \&quot;ModifyGaussDBforMySQLSecurityGroup\&quot;表示修改实例安全组。    - \&quot;ResizeGaussDBforMySQLFlavor\&quot;表示实例规格变更。    - \&quot;SwitchoverGaussDBforMySQLMasterNode\&quot;表示只读升主。    - \&quot;GaussDBforMySQLBindEIP\&quot;表示绑定弹性公网IP。    - \&quot;GaussDBforMySQLUnbindEIP\&quot;表示解绑弹性公网IP。    - \&quot;RenameGaussDBforMySQLInstance\&quot;表示修改实例名称。    - \&quot;DeleteGaussDBforMySQLInstance\&quot;表示删除实例集群。    - \&quot;UpgradeGaussDBforMySQLDatabaseVersion\&quot;表示版本升级。    - \&quot;EnlargeGaussDBforMySQLProxy\&quot;表示实例的数据库代理节点扩容。    - \&quot;OpenGaussDBforMySQLProxy\&quot;表示开启实例的数据库代理。    - \&quot;CloseGaussDBforMySQLProxy\&quot;表示关闭实例的数据库代理。    - \&quot;GaussdbforMySQLModifyProxyIp\&quot;表示修改数据库代理ip。    - \&quot;ScaleGaussDBforMySQLProxy\&quot;表示实例的数据库代理节点规格变更。    - \&quot;GaussDBforMySQLModifyInstanceMetricExtend\&quot;表示实例秒级监控。    - \&quot;GaussDBforMySQLModifyInstanceDataVip\&quot;表示修改实例数据Vip。    - \&quot;GaussDBforMySQLSwitchSSL\&quot;表示切换实例SSL开关。    - \&quot;GaussDBforMySQLModifyProxyConsist\&quot;表示修改代理一致性。    - \&quot;GaussDBforMySQLModifyProxyWeight\&quot;表示修改代理权重。
        :type job_name: str
        :param status: 任务执行状态。 取值： - 值为“Pending”，表示延时任务，未执行。 - 值为“Running”，表示任务正在执行。 - 值为“Completed”，表示任务执行成功。 - 值为“Failed”，表示任务执行失败。
        :type status: str
        :param process: 任务进度。
        :type process: str
        :param created_time: 任务创建时间。格式为\&quot;yyyy-mm-ddThh:mm:ssZ\&quot;。 其中，T指某个时间的开始；Z指时区偏移量，例如偏移1个小时显示为+0100。
        :type created_time: str
        :param ended_time: 任务结束时间。格式为\&quot;yyyy-mm-ddThh:mm:ssZ\&quot;。 其中，T指某个时间的开始；Z指时区偏移量，例如偏移1个小时显示为+0100。
        :type ended_time: str
        :param fail_reason: 任务失败原因。
        :type fail_reason: str
        """
        
        

        self._instance_id = None
        self._instance_name = None
        self._instance_status = None
        self._job_id = None
        self._order_id = None
        self._job_name = None
        self._status = None
        self._process = None
        self._created_time = None
        self._ended_time = None
        self._fail_reason = None
        self.discriminator = None

        if instance_id is not None:
            self.instance_id = instance_id
        if instance_name is not None:
            self.instance_name = instance_name
        if instance_status is not None:
            self.instance_status = instance_status
        if job_id is not None:
            self.job_id = job_id
        if order_id is not None:
            self.order_id = order_id
        if job_name is not None:
            self.job_name = job_name
        if status is not None:
            self.status = status
        if process is not None:
            self.process = process
        if created_time is not None:
            self.created_time = created_time
        if ended_time is not None:
            self.ended_time = ended_time
        if fail_reason is not None:
            self.fail_reason = fail_reason

    @property
    def instance_id(self):
        r"""Gets the instance_id of this TaskDetailInfo.

        实例ID。

        :return: The instance_id of this TaskDetailInfo.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this TaskDetailInfo.

        实例ID。

        :param instance_id: The instance_id of this TaskDetailInfo.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def instance_name(self):
        r"""Gets the instance_name of this TaskDetailInfo.

        实例名称。

        :return: The instance_name of this TaskDetailInfo.
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        r"""Sets the instance_name of this TaskDetailInfo.

        实例名称。

        :param instance_name: The instance_name of this TaskDetailInfo.
        :type instance_name: str
        """
        self._instance_name = instance_name

    @property
    def instance_status(self):
        r"""Gets the instance_status of this TaskDetailInfo.

        实例状态。 取值： - 值为“createfail”，表示实例创建失败。 - 值为“creating”，表示实例创建中。 - 值为“normal”，表示实例正常。 - 值为“abnormal”，表示实例异常。 - 值为“deleted”，表示实例已删除。

        :return: The instance_status of this TaskDetailInfo.
        :rtype: str
        """
        return self._instance_status

    @instance_status.setter
    def instance_status(self, instance_status):
        r"""Sets the instance_status of this TaskDetailInfo.

        实例状态。 取值： - 值为“createfail”，表示实例创建失败。 - 值为“creating”，表示实例创建中。 - 值为“normal”，表示实例正常。 - 值为“abnormal”，表示实例异常。 - 值为“deleted”，表示实例已删除。

        :param instance_status: The instance_status of this TaskDetailInfo.
        :type instance_status: str
        """
        self._instance_status = instance_status

    @property
    def job_id(self):
        r"""Gets the job_id of this TaskDetailInfo.

        任务ID。

        :return: The job_id of this TaskDetailInfo.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this TaskDetailInfo.

        任务ID。

        :param job_id: The job_id of this TaskDetailInfo.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def order_id(self):
        r"""Gets the order_id of this TaskDetailInfo.

        订单ID。

        :return: The order_id of this TaskDetailInfo.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        r"""Sets the order_id of this TaskDetailInfo.

        订单ID。

        :param order_id: The order_id of this TaskDetailInfo.
        :type order_id: str
        """
        self._order_id = order_id

    @property
    def job_name(self):
        r"""Gets the job_name of this TaskDetailInfo.

        任务名称。取值有：    - \"CreateGaussDBforMySQLInstance\"表示创建实例。    - \"RestoreGaussDBforMySQLNewInstance\"表示恢复新实例。    - \"AddGaussDBforMySQLNodes\"表示添加节点。    - \"DeleteGaussDBforMySQLNode\"表示删除节点。    - \"RebootGaussDBforMySQLInstance\"表示重启实例。    - \"ModifyGaussDBforMySQLPort\"表示修改实例端口。    - \"ModifyGaussDBforMySQLSecurityGroup\"表示修改实例安全组。    - \"ResizeGaussDBforMySQLFlavor\"表示实例规格变更。    - \"SwitchoverGaussDBforMySQLMasterNode\"表示只读升主。    - \"GaussDBforMySQLBindEIP\"表示绑定弹性公网IP。    - \"GaussDBforMySQLUnbindEIP\"表示解绑弹性公网IP。    - \"RenameGaussDBforMySQLInstance\"表示修改实例名称。    - \"DeleteGaussDBforMySQLInstance\"表示删除实例集群。    - \"UpgradeGaussDBforMySQLDatabaseVersion\"表示版本升级。    - \"EnlargeGaussDBforMySQLProxy\"表示实例的数据库代理节点扩容。    - \"OpenGaussDBforMySQLProxy\"表示开启实例的数据库代理。    - \"CloseGaussDBforMySQLProxy\"表示关闭实例的数据库代理。    - \"GaussdbforMySQLModifyProxyIp\"表示修改数据库代理ip。    - \"ScaleGaussDBforMySQLProxy\"表示实例的数据库代理节点规格变更。    - \"GaussDBforMySQLModifyInstanceMetricExtend\"表示实例秒级监控。    - \"GaussDBforMySQLModifyInstanceDataVip\"表示修改实例数据Vip。    - \"GaussDBforMySQLSwitchSSL\"表示切换实例SSL开关。    - \"GaussDBforMySQLModifyProxyConsist\"表示修改代理一致性。    - \"GaussDBforMySQLModifyProxyWeight\"表示修改代理权重。

        :return: The job_name of this TaskDetailInfo.
        :rtype: str
        """
        return self._job_name

    @job_name.setter
    def job_name(self, job_name):
        r"""Sets the job_name of this TaskDetailInfo.

        任务名称。取值有：    - \"CreateGaussDBforMySQLInstance\"表示创建实例。    - \"RestoreGaussDBforMySQLNewInstance\"表示恢复新实例。    - \"AddGaussDBforMySQLNodes\"表示添加节点。    - \"DeleteGaussDBforMySQLNode\"表示删除节点。    - \"RebootGaussDBforMySQLInstance\"表示重启实例。    - \"ModifyGaussDBforMySQLPort\"表示修改实例端口。    - \"ModifyGaussDBforMySQLSecurityGroup\"表示修改实例安全组。    - \"ResizeGaussDBforMySQLFlavor\"表示实例规格变更。    - \"SwitchoverGaussDBforMySQLMasterNode\"表示只读升主。    - \"GaussDBforMySQLBindEIP\"表示绑定弹性公网IP。    - \"GaussDBforMySQLUnbindEIP\"表示解绑弹性公网IP。    - \"RenameGaussDBforMySQLInstance\"表示修改实例名称。    - \"DeleteGaussDBforMySQLInstance\"表示删除实例集群。    - \"UpgradeGaussDBforMySQLDatabaseVersion\"表示版本升级。    - \"EnlargeGaussDBforMySQLProxy\"表示实例的数据库代理节点扩容。    - \"OpenGaussDBforMySQLProxy\"表示开启实例的数据库代理。    - \"CloseGaussDBforMySQLProxy\"表示关闭实例的数据库代理。    - \"GaussdbforMySQLModifyProxyIp\"表示修改数据库代理ip。    - \"ScaleGaussDBforMySQLProxy\"表示实例的数据库代理节点规格变更。    - \"GaussDBforMySQLModifyInstanceMetricExtend\"表示实例秒级监控。    - \"GaussDBforMySQLModifyInstanceDataVip\"表示修改实例数据Vip。    - \"GaussDBforMySQLSwitchSSL\"表示切换实例SSL开关。    - \"GaussDBforMySQLModifyProxyConsist\"表示修改代理一致性。    - \"GaussDBforMySQLModifyProxyWeight\"表示修改代理权重。

        :param job_name: The job_name of this TaskDetailInfo.
        :type job_name: str
        """
        self._job_name = job_name

    @property
    def status(self):
        r"""Gets the status of this TaskDetailInfo.

        任务执行状态。 取值： - 值为“Pending”，表示延时任务，未执行。 - 值为“Running”，表示任务正在执行。 - 值为“Completed”，表示任务执行成功。 - 值为“Failed”，表示任务执行失败。

        :return: The status of this TaskDetailInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this TaskDetailInfo.

        任务执行状态。 取值： - 值为“Pending”，表示延时任务，未执行。 - 值为“Running”，表示任务正在执行。 - 值为“Completed”，表示任务执行成功。 - 值为“Failed”，表示任务执行失败。

        :param status: The status of this TaskDetailInfo.
        :type status: str
        """
        self._status = status

    @property
    def process(self):
        r"""Gets the process of this TaskDetailInfo.

        任务进度。

        :return: The process of this TaskDetailInfo.
        :rtype: str
        """
        return self._process

    @process.setter
    def process(self, process):
        r"""Sets the process of this TaskDetailInfo.

        任务进度。

        :param process: The process of this TaskDetailInfo.
        :type process: str
        """
        self._process = process

    @property
    def created_time(self):
        r"""Gets the created_time of this TaskDetailInfo.

        任务创建时间。格式为\"yyyy-mm-ddThh:mm:ssZ\"。 其中，T指某个时间的开始；Z指时区偏移量，例如偏移1个小时显示为+0100。

        :return: The created_time of this TaskDetailInfo.
        :rtype: str
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        r"""Sets the created_time of this TaskDetailInfo.

        任务创建时间。格式为\"yyyy-mm-ddThh:mm:ssZ\"。 其中，T指某个时间的开始；Z指时区偏移量，例如偏移1个小时显示为+0100。

        :param created_time: The created_time of this TaskDetailInfo.
        :type created_time: str
        """
        self._created_time = created_time

    @property
    def ended_time(self):
        r"""Gets the ended_time of this TaskDetailInfo.

        任务结束时间。格式为\"yyyy-mm-ddThh:mm:ssZ\"。 其中，T指某个时间的开始；Z指时区偏移量，例如偏移1个小时显示为+0100。

        :return: The ended_time of this TaskDetailInfo.
        :rtype: str
        """
        return self._ended_time

    @ended_time.setter
    def ended_time(self, ended_time):
        r"""Sets the ended_time of this TaskDetailInfo.

        任务结束时间。格式为\"yyyy-mm-ddThh:mm:ssZ\"。 其中，T指某个时间的开始；Z指时区偏移量，例如偏移1个小时显示为+0100。

        :param ended_time: The ended_time of this TaskDetailInfo.
        :type ended_time: str
        """
        self._ended_time = ended_time

    @property
    def fail_reason(self):
        r"""Gets the fail_reason of this TaskDetailInfo.

        任务失败原因。

        :return: The fail_reason of this TaskDetailInfo.
        :rtype: str
        """
        return self._fail_reason

    @fail_reason.setter
    def fail_reason(self, fail_reason):
        r"""Sets the fail_reason of this TaskDetailInfo.

        任务失败原因。

        :param fail_reason: The fail_reason of this TaskDetailInfo.
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
        if not isinstance(other, TaskDetailInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
