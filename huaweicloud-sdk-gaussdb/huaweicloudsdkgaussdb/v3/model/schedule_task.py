# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ScheduleTask:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'job_id': 'str',
        'instance_id': 'str',
        'instance_name': 'str',
        'instance_status': 'str',
        'project_id': 'str',
        'job_name': 'str',
        'create_time': 'str',
        'start_time': 'str',
        'end_time': 'str',
        'job_status': 'str',
        'datastore_type': 'str',
        'target_config': 'object'
    }

    attribute_map = {
        'job_id': 'job_id',
        'instance_id': 'instance_id',
        'instance_name': 'instance_name',
        'instance_status': 'instance_status',
        'project_id': 'project_id',
        'job_name': 'job_name',
        'create_time': 'create_time',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'job_status': 'job_status',
        'datastore_type': 'datastore_type',
        'target_config': 'target_config'
    }

    def __init__(self, job_id=None, instance_id=None, instance_name=None, instance_status=None, project_id=None, job_name=None, create_time=None, start_time=None, end_time=None, job_status=None, datastore_type=None, target_config=None):
        """ScheduleTask

        The model defined in huaweicloud sdk

        :param job_id: 任务ID。
        :type job_id: str
        :param instance_id: 实例ID。
        :type instance_id: str
        :param instance_name: 实例名称。
        :type instance_name: str
        :param instance_status: 实例状态。 取值： - 值为“createfail”，表示实例创建失败。 - 值为“creating”，表示实例创建中。 - 值为“normal”，表示实例正常。 - 值为“abnormal”，表示实例异常。 - 值为“deleted”，表示实例已删除。
        :type instance_status: str
        :param project_id: 租户在某一region下的project ID。
        :type project_id: str
        :param job_name: 任务名称。取值有：    - \&quot;CreateGaussDBforMySQLInstance\&quot;表示创建实例。    - \&quot;RestoreGaussDBforMySQLNewInstance\&quot;表示恢复新实例。    - \&quot;AddGaussDBforMySQLNodes\&quot;表示添加节点。    - \&quot;DeleteGaussDBforMySQLNode\&quot;表示删除节点。    - \&quot;RebootGaussDBforMySQLInstance\&quot;表示重启实例。    - \&quot;ModifyGaussDBforMySQLPort\&quot;表示修改实例端口。    - \&quot;ModifyGaussDBforMySQLSecurityGroup\&quot;表示修改实例安全组。    - \&quot;ResizeGaussDBforMySQLFlavor\&quot;表示实例规格变更。    - \&quot;SwitchoverGaussDBforMySQLMasterNode\&quot;表示只读升主。    - \&quot;GaussDBforMySQLBindEIP\&quot;表示绑定弹性公网IP。    - \&quot;GaussDBforMySQLUnbindEIP\&quot;表示解绑弹性公网IP。    - \&quot;RenameGaussDBforMySQLInstance\&quot;表示修改实例名称。    - \&quot;DeleteGaussDBforMySQLInstance\&quot;表示删除实例集群。    - \&quot;UpgradeGaussDBforMySQLDatabaseVersion\&quot;表示版本升级。    - \&quot;EnlargeGaussDBforMySQLProxy\&quot;表示实例的数据库代理节点扩容。    - \&quot;ReduceGaussDBforMySQLProxy\&quot;表示实例的数据库代理节点缩容。    - \&quot;OpenGaussDBforMySQLProxy\&quot;表示开启实例的数据库代理。    - \&quot;CloseGaussDBforMySQLProxy\&quot;表示关闭实例的数据库代理。    - \&quot;GaussdbforMySQLModifyProxyIp\&quot;表示修改数据库代理ip。    - \&quot;ScaleGaussDBforMySQLProxy\&quot;表示实例的数据库代理节点规格变更。    - \&quot;GaussDBforMySQLModifyInstanceMetricExtend\&quot;表示实例秒级监控。    - \&quot;GaussDBforMySQLModifyInstanceDataVip\&quot;表示修改实例数据Vip。    - \&quot;GaussDBforMySQLSwitchSSL\&quot;表示切换实例SSL开关。    - \&quot;GaussDBforMySQLModifyProxyConsist\&quot;表示修改代理一致性。    - \&quot;GaussDBforMySQLModifyProxyWeight\&quot;表示修改代理权重。
        :type job_name: str
        :param create_time: 任务创建时间，格式为\&quot;yyyy-mm-ddThh:mm:ssZ\&quot;。 其中，T指某个时间的开始；Z指时区偏移量，例如偏移1个小时显示为+0100。 说明：创建时返回值为空，数据库实例创建成功后该值不为空
        :type create_time: str
        :param start_time: 任务开始时间，格式为\&quot;yyyy-mm-ddThh:mm:ssZ\&quot;。 其中，T指某个时间的开始；Z指时区偏移量，例如偏移1个小时显示为+0100。 说明：创建时返回值为空，数据库实例创建成功后该值不为空
        :type start_time: str
        :param end_time: 任务结束时间，格式为\&quot;yyyy-mm-ddThh:mm:ssZ\&quot;。 其中，T指某个时间的开始；Z指时区偏移量，例如偏移1个小时显示为+0100。 说明：创建时返回值为空，数据库实例创建成功后该值不为空
        :type end_time: str
        :param job_status: 任务执行状态。 取值： - 值为“Pending”，表示延时任务，未执行。 - 值为“Running”，表示任务正在执行。 - 值为“Completed”，表示任务执行成功。 - 值为“Failed”，表示任务执行失败。
        :type job_status: str
        :param datastore_type: 数据库类型。
        :type datastore_type: str
        :param target_config: 实例配置相关信息，比如规格等。
        :type target_config: object
        """
        
        

        self._job_id = None
        self._instance_id = None
        self._instance_name = None
        self._instance_status = None
        self._project_id = None
        self._job_name = None
        self._create_time = None
        self._start_time = None
        self._end_time = None
        self._job_status = None
        self._datastore_type = None
        self._target_config = None
        self.discriminator = None

        if job_id is not None:
            self.job_id = job_id
        if instance_id is not None:
            self.instance_id = instance_id
        if instance_name is not None:
            self.instance_name = instance_name
        if instance_status is not None:
            self.instance_status = instance_status
        if project_id is not None:
            self.project_id = project_id
        if job_name is not None:
            self.job_name = job_name
        if create_time is not None:
            self.create_time = create_time
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if job_status is not None:
            self.job_status = job_status
        if datastore_type is not None:
            self.datastore_type = datastore_type
        if target_config is not None:
            self.target_config = target_config

    @property
    def job_id(self):
        """Gets the job_id of this ScheduleTask.

        任务ID。

        :return: The job_id of this ScheduleTask.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this ScheduleTask.

        任务ID。

        :param job_id: The job_id of this ScheduleTask.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def instance_id(self):
        """Gets the instance_id of this ScheduleTask.

        实例ID。

        :return: The instance_id of this ScheduleTask.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ScheduleTask.

        实例ID。

        :param instance_id: The instance_id of this ScheduleTask.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def instance_name(self):
        """Gets the instance_name of this ScheduleTask.

        实例名称。

        :return: The instance_name of this ScheduleTask.
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        """Sets the instance_name of this ScheduleTask.

        实例名称。

        :param instance_name: The instance_name of this ScheduleTask.
        :type instance_name: str
        """
        self._instance_name = instance_name

    @property
    def instance_status(self):
        """Gets the instance_status of this ScheduleTask.

        实例状态。 取值： - 值为“createfail”，表示实例创建失败。 - 值为“creating”，表示实例创建中。 - 值为“normal”，表示实例正常。 - 值为“abnormal”，表示实例异常。 - 值为“deleted”，表示实例已删除。

        :return: The instance_status of this ScheduleTask.
        :rtype: str
        """
        return self._instance_status

    @instance_status.setter
    def instance_status(self, instance_status):
        """Sets the instance_status of this ScheduleTask.

        实例状态。 取值： - 值为“createfail”，表示实例创建失败。 - 值为“creating”，表示实例创建中。 - 值为“normal”，表示实例正常。 - 值为“abnormal”，表示实例异常。 - 值为“deleted”，表示实例已删除。

        :param instance_status: The instance_status of this ScheduleTask.
        :type instance_status: str
        """
        self._instance_status = instance_status

    @property
    def project_id(self):
        """Gets the project_id of this ScheduleTask.

        租户在某一region下的project ID。

        :return: The project_id of this ScheduleTask.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this ScheduleTask.

        租户在某一region下的project ID。

        :param project_id: The project_id of this ScheduleTask.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def job_name(self):
        """Gets the job_name of this ScheduleTask.

        任务名称。取值有：    - \"CreateGaussDBforMySQLInstance\"表示创建实例。    - \"RestoreGaussDBforMySQLNewInstance\"表示恢复新实例。    - \"AddGaussDBforMySQLNodes\"表示添加节点。    - \"DeleteGaussDBforMySQLNode\"表示删除节点。    - \"RebootGaussDBforMySQLInstance\"表示重启实例。    - \"ModifyGaussDBforMySQLPort\"表示修改实例端口。    - \"ModifyGaussDBforMySQLSecurityGroup\"表示修改实例安全组。    - \"ResizeGaussDBforMySQLFlavor\"表示实例规格变更。    - \"SwitchoverGaussDBforMySQLMasterNode\"表示只读升主。    - \"GaussDBforMySQLBindEIP\"表示绑定弹性公网IP。    - \"GaussDBforMySQLUnbindEIP\"表示解绑弹性公网IP。    - \"RenameGaussDBforMySQLInstance\"表示修改实例名称。    - \"DeleteGaussDBforMySQLInstance\"表示删除实例集群。    - \"UpgradeGaussDBforMySQLDatabaseVersion\"表示版本升级。    - \"EnlargeGaussDBforMySQLProxy\"表示实例的数据库代理节点扩容。    - \"ReduceGaussDBforMySQLProxy\"表示实例的数据库代理节点缩容。    - \"OpenGaussDBforMySQLProxy\"表示开启实例的数据库代理。    - \"CloseGaussDBforMySQLProxy\"表示关闭实例的数据库代理。    - \"GaussdbforMySQLModifyProxyIp\"表示修改数据库代理ip。    - \"ScaleGaussDBforMySQLProxy\"表示实例的数据库代理节点规格变更。    - \"GaussDBforMySQLModifyInstanceMetricExtend\"表示实例秒级监控。    - \"GaussDBforMySQLModifyInstanceDataVip\"表示修改实例数据Vip。    - \"GaussDBforMySQLSwitchSSL\"表示切换实例SSL开关。    - \"GaussDBforMySQLModifyProxyConsist\"表示修改代理一致性。    - \"GaussDBforMySQLModifyProxyWeight\"表示修改代理权重。

        :return: The job_name of this ScheduleTask.
        :rtype: str
        """
        return self._job_name

    @job_name.setter
    def job_name(self, job_name):
        """Sets the job_name of this ScheduleTask.

        任务名称。取值有：    - \"CreateGaussDBforMySQLInstance\"表示创建实例。    - \"RestoreGaussDBforMySQLNewInstance\"表示恢复新实例。    - \"AddGaussDBforMySQLNodes\"表示添加节点。    - \"DeleteGaussDBforMySQLNode\"表示删除节点。    - \"RebootGaussDBforMySQLInstance\"表示重启实例。    - \"ModifyGaussDBforMySQLPort\"表示修改实例端口。    - \"ModifyGaussDBforMySQLSecurityGroup\"表示修改实例安全组。    - \"ResizeGaussDBforMySQLFlavor\"表示实例规格变更。    - \"SwitchoverGaussDBforMySQLMasterNode\"表示只读升主。    - \"GaussDBforMySQLBindEIP\"表示绑定弹性公网IP。    - \"GaussDBforMySQLUnbindEIP\"表示解绑弹性公网IP。    - \"RenameGaussDBforMySQLInstance\"表示修改实例名称。    - \"DeleteGaussDBforMySQLInstance\"表示删除实例集群。    - \"UpgradeGaussDBforMySQLDatabaseVersion\"表示版本升级。    - \"EnlargeGaussDBforMySQLProxy\"表示实例的数据库代理节点扩容。    - \"ReduceGaussDBforMySQLProxy\"表示实例的数据库代理节点缩容。    - \"OpenGaussDBforMySQLProxy\"表示开启实例的数据库代理。    - \"CloseGaussDBforMySQLProxy\"表示关闭实例的数据库代理。    - \"GaussdbforMySQLModifyProxyIp\"表示修改数据库代理ip。    - \"ScaleGaussDBforMySQLProxy\"表示实例的数据库代理节点规格变更。    - \"GaussDBforMySQLModifyInstanceMetricExtend\"表示实例秒级监控。    - \"GaussDBforMySQLModifyInstanceDataVip\"表示修改实例数据Vip。    - \"GaussDBforMySQLSwitchSSL\"表示切换实例SSL开关。    - \"GaussDBforMySQLModifyProxyConsist\"表示修改代理一致性。    - \"GaussDBforMySQLModifyProxyWeight\"表示修改代理权重。

        :param job_name: The job_name of this ScheduleTask.
        :type job_name: str
        """
        self._job_name = job_name

    @property
    def create_time(self):
        """Gets the create_time of this ScheduleTask.

        任务创建时间，格式为\"yyyy-mm-ddThh:mm:ssZ\"。 其中，T指某个时间的开始；Z指时区偏移量，例如偏移1个小时显示为+0100。 说明：创建时返回值为空，数据库实例创建成功后该值不为空

        :return: The create_time of this ScheduleTask.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this ScheduleTask.

        任务创建时间，格式为\"yyyy-mm-ddThh:mm:ssZ\"。 其中，T指某个时间的开始；Z指时区偏移量，例如偏移1个小时显示为+0100。 说明：创建时返回值为空，数据库实例创建成功后该值不为空

        :param create_time: The create_time of this ScheduleTask.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def start_time(self):
        """Gets the start_time of this ScheduleTask.

        任务开始时间，格式为\"yyyy-mm-ddThh:mm:ssZ\"。 其中，T指某个时间的开始；Z指时区偏移量，例如偏移1个小时显示为+0100。 说明：创建时返回值为空，数据库实例创建成功后该值不为空

        :return: The start_time of this ScheduleTask.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ScheduleTask.

        任务开始时间，格式为\"yyyy-mm-ddThh:mm:ssZ\"。 其中，T指某个时间的开始；Z指时区偏移量，例如偏移1个小时显示为+0100。 说明：创建时返回值为空，数据库实例创建成功后该值不为空

        :param start_time: The start_time of this ScheduleTask.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this ScheduleTask.

        任务结束时间，格式为\"yyyy-mm-ddThh:mm:ssZ\"。 其中，T指某个时间的开始；Z指时区偏移量，例如偏移1个小时显示为+0100。 说明：创建时返回值为空，数据库实例创建成功后该值不为空

        :return: The end_time of this ScheduleTask.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ScheduleTask.

        任务结束时间，格式为\"yyyy-mm-ddThh:mm:ssZ\"。 其中，T指某个时间的开始；Z指时区偏移量，例如偏移1个小时显示为+0100。 说明：创建时返回值为空，数据库实例创建成功后该值不为空

        :param end_time: The end_time of this ScheduleTask.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def job_status(self):
        """Gets the job_status of this ScheduleTask.

        任务执行状态。 取值： - 值为“Pending”，表示延时任务，未执行。 - 值为“Running”，表示任务正在执行。 - 值为“Completed”，表示任务执行成功。 - 值为“Failed”，表示任务执行失败。

        :return: The job_status of this ScheduleTask.
        :rtype: str
        """
        return self._job_status

    @job_status.setter
    def job_status(self, job_status):
        """Sets the job_status of this ScheduleTask.

        任务执行状态。 取值： - 值为“Pending”，表示延时任务，未执行。 - 值为“Running”，表示任务正在执行。 - 值为“Completed”，表示任务执行成功。 - 值为“Failed”，表示任务执行失败。

        :param job_status: The job_status of this ScheduleTask.
        :type job_status: str
        """
        self._job_status = job_status

    @property
    def datastore_type(self):
        """Gets the datastore_type of this ScheduleTask.

        数据库类型。

        :return: The datastore_type of this ScheduleTask.
        :rtype: str
        """
        return self._datastore_type

    @datastore_type.setter
    def datastore_type(self, datastore_type):
        """Sets the datastore_type of this ScheduleTask.

        数据库类型。

        :param datastore_type: The datastore_type of this ScheduleTask.
        :type datastore_type: str
        """
        self._datastore_type = datastore_type

    @property
    def target_config(self):
        """Gets the target_config of this ScheduleTask.

        实例配置相关信息，比如规格等。

        :return: The target_config of this ScheduleTask.
        :rtype: object
        """
        return self._target_config

    @target_config.setter
    def target_config(self, target_config):
        """Sets the target_config of this ScheduleTask.

        实例配置相关信息，比如规格等。

        :param target_config: The target_config of this ScheduleTask.
        :type target_config: object
        """
        self._target_config = target_config

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
        if not isinstance(other, ScheduleTask):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
