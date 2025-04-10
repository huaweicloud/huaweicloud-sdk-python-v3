# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowBatchTaskRequest:

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
        'task_id': 'str',
        'task_detail_status': 'str',
        'target': 'str',
        'limit': 'int',
        'marker': 'str',
        'offset': 'int'
    }

    attribute_map = {
        'instance_id': 'Instance-Id',
        'task_id': 'task_id',
        'task_detail_status': 'task_detail_status',
        'target': 'target',
        'limit': 'limit',
        'marker': 'marker',
        'offset': 'offset'
    }

    def __init__(self, instance_id=None, task_id=None, task_detail_status=None, target=None, limit=None, marker=None, offset=None):
        r"""ShowBatchTaskRequest

        The model defined in huaweicloud sdk

        :param instance_id: **参数说明**：实例ID。物理多租下各实例的唯一标识，一般华为云租户无需携带该参数，仅在物理多租场景下从管理面访问API时需要携带该参数。您可以在IoTDA管理控制台界面，选择左侧导航栏“总览”页签查看当前实例的ID。
        :type instance_id: str
        :param task_id: **参数说明**：批量任务ID，创建批量任务时由物联网平台分配获得。 **取值范围**：长度不超过24，只允许小写字母a到f、数字的组合。
        :type task_id: str
        :param task_detail_status: **参数说明**：子任务的执行状态，可选参数。 **取值范围**： - Success: 成功。 - Fail: 失败。 - Processing: 执行中。 - FailWaitRetry: 失败重试。 - Stopped: 已停止。 - Waitting: 等待执行。 - Removed: 已移除。
        :type task_detail_status: str
        :param target: **参数说明**：执行批量任务的目标，当task_type为firmwareUpgrade，softwareUpgrade，deleteDevices，freezeDevices，unfreezeDevices，createCommands，createAsyncCommands，createMessages，updateDeviceShadows，此处填写device_id **取值范围**：长度不超过128，只允许字母、数字、下划线（_）、连接符（-）的组合。
        :type target: str
        :param limit: **参数说明**：分页查询时每页显示的记录数。 **取值范围**：1-50的整数，默认值为10。
        :type limit: int
        :param marker: **参数说明**：上一次分页查询结果中最后一条记录的ID，在上一次分页查询时由物联网平台返回获得。分页查询时物联网平台是按marker也就是记录ID降序查询的，越新的数据记录ID也会越大。若填写marker，则本次只查询记录ID小于marker的数据记录。若不填写，则从记录ID最大也就是最新的一条数据开始查询。如果需要依次查询所有数据，则每次查询时必须填写上一次查询响应中的marker值。 **取值范围**：长度为24的十六进制字符串，默认值为ffffffffffffffffffffffff。
        :type marker: str
        :param offset: **参数说明**：表示从marker后偏移offset条记录开始查询。默认为0，取值范围为0-500的整数。当offset为0时，表示从marker后第一条记录开始输出。限制offset最大值是出于API性能考虑，您可以搭配marker使用该参数实现翻页，例如每页50条记录，1-11页内都可以直接使用offset跳转到指定页，但到11页后，由于offset限制为500，您需要使用第11页返回的marker作为下次查询的marker，以实现翻页到12-22页。  **取值范围**：0-500的整数，默认为0。
        :type offset: int
        """
        
        

        self._instance_id = None
        self._task_id = None
        self._task_detail_status = None
        self._target = None
        self._limit = None
        self._marker = None
        self._offset = None
        self.discriminator = None

        if instance_id is not None:
            self.instance_id = instance_id
        self.task_id = task_id
        if task_detail_status is not None:
            self.task_detail_status = task_detail_status
        if target is not None:
            self.target = target
        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if offset is not None:
            self.offset = offset

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ShowBatchTaskRequest.

        **参数说明**：实例ID。物理多租下各实例的唯一标识，一般华为云租户无需携带该参数，仅在物理多租场景下从管理面访问API时需要携带该参数。您可以在IoTDA管理控制台界面，选择左侧导航栏“总览”页签查看当前实例的ID。

        :return: The instance_id of this ShowBatchTaskRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ShowBatchTaskRequest.

        **参数说明**：实例ID。物理多租下各实例的唯一标识，一般华为云租户无需携带该参数，仅在物理多租场景下从管理面访问API时需要携带该参数。您可以在IoTDA管理控制台界面，选择左侧导航栏“总览”页签查看当前实例的ID。

        :param instance_id: The instance_id of this ShowBatchTaskRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def task_id(self):
        r"""Gets the task_id of this ShowBatchTaskRequest.

        **参数说明**：批量任务ID，创建批量任务时由物联网平台分配获得。 **取值范围**：长度不超过24，只允许小写字母a到f、数字的组合。

        :return: The task_id of this ShowBatchTaskRequest.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this ShowBatchTaskRequest.

        **参数说明**：批量任务ID，创建批量任务时由物联网平台分配获得。 **取值范围**：长度不超过24，只允许小写字母a到f、数字的组合。

        :param task_id: The task_id of this ShowBatchTaskRequest.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def task_detail_status(self):
        r"""Gets the task_detail_status of this ShowBatchTaskRequest.

        **参数说明**：子任务的执行状态，可选参数。 **取值范围**： - Success: 成功。 - Fail: 失败。 - Processing: 执行中。 - FailWaitRetry: 失败重试。 - Stopped: 已停止。 - Waitting: 等待执行。 - Removed: 已移除。

        :return: The task_detail_status of this ShowBatchTaskRequest.
        :rtype: str
        """
        return self._task_detail_status

    @task_detail_status.setter
    def task_detail_status(self, task_detail_status):
        r"""Sets the task_detail_status of this ShowBatchTaskRequest.

        **参数说明**：子任务的执行状态，可选参数。 **取值范围**： - Success: 成功。 - Fail: 失败。 - Processing: 执行中。 - FailWaitRetry: 失败重试。 - Stopped: 已停止。 - Waitting: 等待执行。 - Removed: 已移除。

        :param task_detail_status: The task_detail_status of this ShowBatchTaskRequest.
        :type task_detail_status: str
        """
        self._task_detail_status = task_detail_status

    @property
    def target(self):
        r"""Gets the target of this ShowBatchTaskRequest.

        **参数说明**：执行批量任务的目标，当task_type为firmwareUpgrade，softwareUpgrade，deleteDevices，freezeDevices，unfreezeDevices，createCommands，createAsyncCommands，createMessages，updateDeviceShadows，此处填写device_id **取值范围**：长度不超过128，只允许字母、数字、下划线（_）、连接符（-）的组合。

        :return: The target of this ShowBatchTaskRequest.
        :rtype: str
        """
        return self._target

    @target.setter
    def target(self, target):
        r"""Sets the target of this ShowBatchTaskRequest.

        **参数说明**：执行批量任务的目标，当task_type为firmwareUpgrade，softwareUpgrade，deleteDevices，freezeDevices，unfreezeDevices，createCommands，createAsyncCommands，createMessages，updateDeviceShadows，此处填写device_id **取值范围**：长度不超过128，只允许字母、数字、下划线（_）、连接符（-）的组合。

        :param target: The target of this ShowBatchTaskRequest.
        :type target: str
        """
        self._target = target

    @property
    def limit(self):
        r"""Gets the limit of this ShowBatchTaskRequest.

        **参数说明**：分页查询时每页显示的记录数。 **取值范围**：1-50的整数，默认值为10。

        :return: The limit of this ShowBatchTaskRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ShowBatchTaskRequest.

        **参数说明**：分页查询时每页显示的记录数。 **取值范围**：1-50的整数，默认值为10。

        :param limit: The limit of this ShowBatchTaskRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        r"""Gets the marker of this ShowBatchTaskRequest.

        **参数说明**：上一次分页查询结果中最后一条记录的ID，在上一次分页查询时由物联网平台返回获得。分页查询时物联网平台是按marker也就是记录ID降序查询的，越新的数据记录ID也会越大。若填写marker，则本次只查询记录ID小于marker的数据记录。若不填写，则从记录ID最大也就是最新的一条数据开始查询。如果需要依次查询所有数据，则每次查询时必须填写上一次查询响应中的marker值。 **取值范围**：长度为24的十六进制字符串，默认值为ffffffffffffffffffffffff。

        :return: The marker of this ShowBatchTaskRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ShowBatchTaskRequest.

        **参数说明**：上一次分页查询结果中最后一条记录的ID，在上一次分页查询时由物联网平台返回获得。分页查询时物联网平台是按marker也就是记录ID降序查询的，越新的数据记录ID也会越大。若填写marker，则本次只查询记录ID小于marker的数据记录。若不填写，则从记录ID最大也就是最新的一条数据开始查询。如果需要依次查询所有数据，则每次查询时必须填写上一次查询响应中的marker值。 **取值范围**：长度为24的十六进制字符串，默认值为ffffffffffffffffffffffff。

        :param marker: The marker of this ShowBatchTaskRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def offset(self):
        r"""Gets the offset of this ShowBatchTaskRequest.

        **参数说明**：表示从marker后偏移offset条记录开始查询。默认为0，取值范围为0-500的整数。当offset为0时，表示从marker后第一条记录开始输出。限制offset最大值是出于API性能考虑，您可以搭配marker使用该参数实现翻页，例如每页50条记录，1-11页内都可以直接使用offset跳转到指定页，但到11页后，由于offset限制为500，您需要使用第11页返回的marker作为下次查询的marker，以实现翻页到12-22页。  **取值范围**：0-500的整数，默认为0。

        :return: The offset of this ShowBatchTaskRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ShowBatchTaskRequest.

        **参数说明**：表示从marker后偏移offset条记录开始查询。默认为0，取值范围为0-500的整数。当offset为0时，表示从marker后第一条记录开始输出。限制offset最大值是出于API性能考虑，您可以搭配marker使用该参数实现翻页，例如每页50条记录，1-11页内都可以直接使用offset跳转到指定页，但到11页后，由于offset限制为500，您需要使用第11页返回的marker作为下次查询的marker，以实现翻页到12-22页。  **取值范围**：0-500的整数，默认为0。

        :param offset: The offset of this ShowBatchTaskRequest.
        :type offset: int
        """
        self._offset = offset

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
        if not isinstance(other, ShowBatchTaskRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
