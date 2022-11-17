# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Task:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'task_id': 'str',
        'task_name': 'str',
        'task_type': 'str',
        'targets': 'list[str]',
        'targets_filter': 'dict(str, object)',
        'document': 'object',
        'task_policy': 'TaskPolicy',
        'status': 'str',
        'status_desc': 'str',
        'task_progress': 'TaskProgress',
        'create_time': 'str'
    }

    attribute_map = {
        'task_id': 'task_id',
        'task_name': 'task_name',
        'task_type': 'task_type',
        'targets': 'targets',
        'targets_filter': 'targets_filter',
        'document': 'document',
        'task_policy': 'task_policy',
        'status': 'status',
        'status_desc': 'status_desc',
        'task_progress': 'task_progress',
        'create_time': 'create_time'
    }

    def __init__(self, task_id=None, task_name=None, task_type=None, targets=None, targets_filter=None, document=None, task_policy=None, status=None, status_desc=None, task_progress=None, create_time=None):
        """Task

        The model defined in huaweicloud sdk

        :param task_id: 批量任务ID，创建批量任务时由物联网平台分配获得。
        :type task_id: str
        :param task_name: 批量任务名称。
        :type task_name: str
        :param task_type: 批量任务类型，取值范围：firmwareUpgrade，softwareUpgrade，createDevices，deleteDevices，freezeDevices，unfreezeDevices，createCommands，createAsyncCommands，createMessages，updateDeviceShadows。 - softwareUpgrade: 软件升级任务 - firmwareUpgrade: 固件升级任务 - createDevices: 批量创建设备任务 - deleteDevices: 批量删除设备任务 - freezeDevices: 批量冻结设备任务 - unfreezeDevices: 批量解冻设备任务 - createCommands: 批量创建同步命令任务 - createAsyncCommands: 批量创建异步命令任务 - createMessages: 批量创建消息任务 - updateDeviceShadows: 批量配置设备影子任务
        :type task_type: str
        :param targets: 执行批量任务的目标，当task_type为firmwareUpgrade，softwareUpgrade，deleteDevices，freezeDevices，unfreezeDevices，createCommands，createAsyncCommands，createMessages，updateDeviceShadows，此处填写device_id列表。
        :type targets: list[str]
        :param targets_filter: 任务目标筛选参数。Json格式，里面是一个个键值对，（K,V）格式标识筛选targets需要的参数，目前支持的K有group_ids（V填写group_id数组，eg:[\&quot;e495cf17-ff79-4294-8f64-4d367919d665\&quot;]，任务则会筛选出来符合该群组条件的设备作为目标）
        :type targets_filter: dict(str, object)
        :param document: 执行任务数据文档，Json格式。(当task_type为softwareUpgrade|firmwareUpgrade，也就是软固件升级任务时，Json里面是(K,V)键值对，需要填写key为package_id，value为在平台上传的软固件附件id，id由portal软件库包管理上传并查询获得。当task_type为createCommands，也就是批量创建同步命令任务时，Json里面是命令相关参数，eg：{\&quot;service_id\&quot;:\&quot;water\&quot;,\&quot;command_name\&quot;:\&quot;ON_OFF\&quot;,\&quot;paras\&quot;:{\&quot;value\&quot;:\&quot;ON\&quot;}}，参考[[设备同步命令](https://support.huaweicloud.com/api-iothub/iot_06_v5_0038.html)](tag:hws)[[设备同步命令](https://support.huaweicloud.com/intl/zh-cn/api-iothub/iot_06_v5_0038.html)](tag:hws_hk))。当task_type为createAsyncCommands，也就是批量创建异步命令任务时，Json里面是命令相关参数，eg：{\&quot;service_id\&quot;:\&quot;water\&quot;,\&quot;command_name\&quot;:\&quot;ON_OFF\&quot;,\&quot;paras\&quot;:{\&quot;value\&quot;:\&quot;ON\&quot;},\&quot;expire_time\&quot;:0,\&quot;send_strategy\&quot;:\&quot;immediately\&quot;}，参考[[设备异步命令](https://support.huaweicloud.com/api-iothub/iot_06_v5_0040.html)](tag:hws)[[设备异步命令](https://support.huaweicloud.com/intl/zh-cn/api-iothub/iot_06_v5_0040.html)](tag:hws_hk))。当task_type为updateDeviceShadows，也就是批量配置设备影子任务时，Json里面是命令相关参数，eg：{\&quot;shadow\&quot;: [{\&quot;service_id\&quot;: \&quot;WaterMeter\&quot;,\&quot;desired\&quot;: {\&quot;temperature\&quot;: \&quot;60\&quot;}}]}，参考[[配置设备影子预期数据](https://support.huaweicloud.com/api-iothub/iot_06_v5_0072.html)](tag:hws)[[配置设备影子预期数据](https://support.huaweicloud.com/intl/zh-cn/api-iothub/iot_06_v5_0072.html)](tag:hws_hk))。
        :type document: object
        :param task_policy: 
        :type task_policy: :class:`huaweicloudsdkiotda.v5.TaskPolicy`
        :param status: 批量任务的状态，可选参数，取值范围：Success|Fail|Processing|PartialSuccess|Stopped|Waitting|Initializing。 - Initializing: 初始化中。 - Waitting: 等待中。 - Processing: 执行中。 - Success: 成功。 - Fail: 失败。 - PartialSuccess: 部分成功。 - Stopped: 停止。
        :type status: str
        :param status_desc: 批量任务状态描述(包含主任务失败错误信息)
        :type status_desc: str
        :param task_progress: 
        :type task_progress: :class:`huaweicloudsdkiotda.v5.TaskProgress`
        :param create_time: 批量任务的创建时间。格式：yyyyMMdd&#39;T&#39;HHmmss&#39;Z&#39;，如20151212T121212Z。
        :type create_time: str
        """
        
        

        self._task_id = None
        self._task_name = None
        self._task_type = None
        self._targets = None
        self._targets_filter = None
        self._document = None
        self._task_policy = None
        self._status = None
        self._status_desc = None
        self._task_progress = None
        self._create_time = None
        self.discriminator = None

        if task_id is not None:
            self.task_id = task_id
        if task_name is not None:
            self.task_name = task_name
        if task_type is not None:
            self.task_type = task_type
        if targets is not None:
            self.targets = targets
        if targets_filter is not None:
            self.targets_filter = targets_filter
        if document is not None:
            self.document = document
        if task_policy is not None:
            self.task_policy = task_policy
        if status is not None:
            self.status = status
        if status_desc is not None:
            self.status_desc = status_desc
        if task_progress is not None:
            self.task_progress = task_progress
        if create_time is not None:
            self.create_time = create_time

    @property
    def task_id(self):
        """Gets the task_id of this Task.

        批量任务ID，创建批量任务时由物联网平台分配获得。

        :return: The task_id of this Task.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """Sets the task_id of this Task.

        批量任务ID，创建批量任务时由物联网平台分配获得。

        :param task_id: The task_id of this Task.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def task_name(self):
        """Gets the task_name of this Task.

        批量任务名称。

        :return: The task_name of this Task.
        :rtype: str
        """
        return self._task_name

    @task_name.setter
    def task_name(self, task_name):
        """Sets the task_name of this Task.

        批量任务名称。

        :param task_name: The task_name of this Task.
        :type task_name: str
        """
        self._task_name = task_name

    @property
    def task_type(self):
        """Gets the task_type of this Task.

        批量任务类型，取值范围：firmwareUpgrade，softwareUpgrade，createDevices，deleteDevices，freezeDevices，unfreezeDevices，createCommands，createAsyncCommands，createMessages，updateDeviceShadows。 - softwareUpgrade: 软件升级任务 - firmwareUpgrade: 固件升级任务 - createDevices: 批量创建设备任务 - deleteDevices: 批量删除设备任务 - freezeDevices: 批量冻结设备任务 - unfreezeDevices: 批量解冻设备任务 - createCommands: 批量创建同步命令任务 - createAsyncCommands: 批量创建异步命令任务 - createMessages: 批量创建消息任务 - updateDeviceShadows: 批量配置设备影子任务

        :return: The task_type of this Task.
        :rtype: str
        """
        return self._task_type

    @task_type.setter
    def task_type(self, task_type):
        """Sets the task_type of this Task.

        批量任务类型，取值范围：firmwareUpgrade，softwareUpgrade，createDevices，deleteDevices，freezeDevices，unfreezeDevices，createCommands，createAsyncCommands，createMessages，updateDeviceShadows。 - softwareUpgrade: 软件升级任务 - firmwareUpgrade: 固件升级任务 - createDevices: 批量创建设备任务 - deleteDevices: 批量删除设备任务 - freezeDevices: 批量冻结设备任务 - unfreezeDevices: 批量解冻设备任务 - createCommands: 批量创建同步命令任务 - createAsyncCommands: 批量创建异步命令任务 - createMessages: 批量创建消息任务 - updateDeviceShadows: 批量配置设备影子任务

        :param task_type: The task_type of this Task.
        :type task_type: str
        """
        self._task_type = task_type

    @property
    def targets(self):
        """Gets the targets of this Task.

        执行批量任务的目标，当task_type为firmwareUpgrade，softwareUpgrade，deleteDevices，freezeDevices，unfreezeDevices，createCommands，createAsyncCommands，createMessages，updateDeviceShadows，此处填写device_id列表。

        :return: The targets of this Task.
        :rtype: list[str]
        """
        return self._targets

    @targets.setter
    def targets(self, targets):
        """Sets the targets of this Task.

        执行批量任务的目标，当task_type为firmwareUpgrade，softwareUpgrade，deleteDevices，freezeDevices，unfreezeDevices，createCommands，createAsyncCommands，createMessages，updateDeviceShadows，此处填写device_id列表。

        :param targets: The targets of this Task.
        :type targets: list[str]
        """
        self._targets = targets

    @property
    def targets_filter(self):
        """Gets the targets_filter of this Task.

        任务目标筛选参数。Json格式，里面是一个个键值对，（K,V）格式标识筛选targets需要的参数，目前支持的K有group_ids（V填写group_id数组，eg:[\"e495cf17-ff79-4294-8f64-4d367919d665\"]，任务则会筛选出来符合该群组条件的设备作为目标）

        :return: The targets_filter of this Task.
        :rtype: dict(str, object)
        """
        return self._targets_filter

    @targets_filter.setter
    def targets_filter(self, targets_filter):
        """Sets the targets_filter of this Task.

        任务目标筛选参数。Json格式，里面是一个个键值对，（K,V）格式标识筛选targets需要的参数，目前支持的K有group_ids（V填写group_id数组，eg:[\"e495cf17-ff79-4294-8f64-4d367919d665\"]，任务则会筛选出来符合该群组条件的设备作为目标）

        :param targets_filter: The targets_filter of this Task.
        :type targets_filter: dict(str, object)
        """
        self._targets_filter = targets_filter

    @property
    def document(self):
        """Gets the document of this Task.

        执行任务数据文档，Json格式。(当task_type为softwareUpgrade|firmwareUpgrade，也就是软固件升级任务时，Json里面是(K,V)键值对，需要填写key为package_id，value为在平台上传的软固件附件id，id由portal软件库包管理上传并查询获得。当task_type为createCommands，也就是批量创建同步命令任务时，Json里面是命令相关参数，eg：{\"service_id\":\"water\",\"command_name\":\"ON_OFF\",\"paras\":{\"value\":\"ON\"}}，参考[[设备同步命令](https://support.huaweicloud.com/api-iothub/iot_06_v5_0038.html)](tag:hws)[[设备同步命令](https://support.huaweicloud.com/intl/zh-cn/api-iothub/iot_06_v5_0038.html)](tag:hws_hk))。当task_type为createAsyncCommands，也就是批量创建异步命令任务时，Json里面是命令相关参数，eg：{\"service_id\":\"water\",\"command_name\":\"ON_OFF\",\"paras\":{\"value\":\"ON\"},\"expire_time\":0,\"send_strategy\":\"immediately\"}，参考[[设备异步命令](https://support.huaweicloud.com/api-iothub/iot_06_v5_0040.html)](tag:hws)[[设备异步命令](https://support.huaweicloud.com/intl/zh-cn/api-iothub/iot_06_v5_0040.html)](tag:hws_hk))。当task_type为updateDeviceShadows，也就是批量配置设备影子任务时，Json里面是命令相关参数，eg：{\"shadow\": [{\"service_id\": \"WaterMeter\",\"desired\": {\"temperature\": \"60\"}}]}，参考[[配置设备影子预期数据](https://support.huaweicloud.com/api-iothub/iot_06_v5_0072.html)](tag:hws)[[配置设备影子预期数据](https://support.huaweicloud.com/intl/zh-cn/api-iothub/iot_06_v5_0072.html)](tag:hws_hk))。

        :return: The document of this Task.
        :rtype: object
        """
        return self._document

    @document.setter
    def document(self, document):
        """Sets the document of this Task.

        执行任务数据文档，Json格式。(当task_type为softwareUpgrade|firmwareUpgrade，也就是软固件升级任务时，Json里面是(K,V)键值对，需要填写key为package_id，value为在平台上传的软固件附件id，id由portal软件库包管理上传并查询获得。当task_type为createCommands，也就是批量创建同步命令任务时，Json里面是命令相关参数，eg：{\"service_id\":\"water\",\"command_name\":\"ON_OFF\",\"paras\":{\"value\":\"ON\"}}，参考[[设备同步命令](https://support.huaweicloud.com/api-iothub/iot_06_v5_0038.html)](tag:hws)[[设备同步命令](https://support.huaweicloud.com/intl/zh-cn/api-iothub/iot_06_v5_0038.html)](tag:hws_hk))。当task_type为createAsyncCommands，也就是批量创建异步命令任务时，Json里面是命令相关参数，eg：{\"service_id\":\"water\",\"command_name\":\"ON_OFF\",\"paras\":{\"value\":\"ON\"},\"expire_time\":0,\"send_strategy\":\"immediately\"}，参考[[设备异步命令](https://support.huaweicloud.com/api-iothub/iot_06_v5_0040.html)](tag:hws)[[设备异步命令](https://support.huaweicloud.com/intl/zh-cn/api-iothub/iot_06_v5_0040.html)](tag:hws_hk))。当task_type为updateDeviceShadows，也就是批量配置设备影子任务时，Json里面是命令相关参数，eg：{\"shadow\": [{\"service_id\": \"WaterMeter\",\"desired\": {\"temperature\": \"60\"}}]}，参考[[配置设备影子预期数据](https://support.huaweicloud.com/api-iothub/iot_06_v5_0072.html)](tag:hws)[[配置设备影子预期数据](https://support.huaweicloud.com/intl/zh-cn/api-iothub/iot_06_v5_0072.html)](tag:hws_hk))。

        :param document: The document of this Task.
        :type document: object
        """
        self._document = document

    @property
    def task_policy(self):
        """Gets the task_policy of this Task.

        :return: The task_policy of this Task.
        :rtype: :class:`huaweicloudsdkiotda.v5.TaskPolicy`
        """
        return self._task_policy

    @task_policy.setter
    def task_policy(self, task_policy):
        """Sets the task_policy of this Task.

        :param task_policy: The task_policy of this Task.
        :type task_policy: :class:`huaweicloudsdkiotda.v5.TaskPolicy`
        """
        self._task_policy = task_policy

    @property
    def status(self):
        """Gets the status of this Task.

        批量任务的状态，可选参数，取值范围：Success|Fail|Processing|PartialSuccess|Stopped|Waitting|Initializing。 - Initializing: 初始化中。 - Waitting: 等待中。 - Processing: 执行中。 - Success: 成功。 - Fail: 失败。 - PartialSuccess: 部分成功。 - Stopped: 停止。

        :return: The status of this Task.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Task.

        批量任务的状态，可选参数，取值范围：Success|Fail|Processing|PartialSuccess|Stopped|Waitting|Initializing。 - Initializing: 初始化中。 - Waitting: 等待中。 - Processing: 执行中。 - Success: 成功。 - Fail: 失败。 - PartialSuccess: 部分成功。 - Stopped: 停止。

        :param status: The status of this Task.
        :type status: str
        """
        self._status = status

    @property
    def status_desc(self):
        """Gets the status_desc of this Task.

        批量任务状态描述(包含主任务失败错误信息)

        :return: The status_desc of this Task.
        :rtype: str
        """
        return self._status_desc

    @status_desc.setter
    def status_desc(self, status_desc):
        """Sets the status_desc of this Task.

        批量任务状态描述(包含主任务失败错误信息)

        :param status_desc: The status_desc of this Task.
        :type status_desc: str
        """
        self._status_desc = status_desc

    @property
    def task_progress(self):
        """Gets the task_progress of this Task.

        :return: The task_progress of this Task.
        :rtype: :class:`huaweicloudsdkiotda.v5.TaskProgress`
        """
        return self._task_progress

    @task_progress.setter
    def task_progress(self, task_progress):
        """Sets the task_progress of this Task.

        :param task_progress: The task_progress of this Task.
        :type task_progress: :class:`huaweicloudsdkiotda.v5.TaskProgress`
        """
        self._task_progress = task_progress

    @property
    def create_time(self):
        """Gets the create_time of this Task.

        批量任务的创建时间。格式：yyyyMMdd'T'HHmmss'Z'，如20151212T121212Z。

        :return: The create_time of this Task.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this Task.

        批量任务的创建时间。格式：yyyyMMdd'T'HHmmss'Z'，如20151212T121212Z。

        :param create_time: The create_time of this Task.
        :type create_time: str
        """
        self._create_time = create_time

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
        if not isinstance(other, Task):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
