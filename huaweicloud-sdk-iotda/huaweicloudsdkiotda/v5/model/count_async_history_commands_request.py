# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CountAsyncHistoryCommandsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'device_id': 'str',
        'instance_id': 'str',
        'start_time': 'str',
        'end_time': 'str',
        'status': 'str',
        'command_name': 'str'
    }

    attribute_map = {
        'device_id': 'device_id',
        'instance_id': 'Instance-Id',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'status': 'status',
        'command_name': 'command_name'
    }

    def __init__(self, device_id=None, instance_id=None, start_time=None, end_time=None, status=None, command_name=None):
        r"""CountAsyncHistoryCommandsRequest

        The model defined in huaweicloud sdk

        :param device_id: **参数说明**：下发命令的设备ID，用于唯一标识一个设备，在注册设备时由物联网平台分配获得。 **取值范围**：长度不超过128，只允许字母、数字、下划线（_）、连接符（-）的组合。
        :type device_id: str
        :param instance_id: **参数说明**：实例ID。物理多租下各实例的唯一标识，建议携带该参数，在使用专业版时必须携带该参数。您可以在IoTDA管理控制台界面，选择左侧导航栏“总览”页签查看当前实例的ID，具体获取方式请参考[[查看实例详情](https://support.huaweicloud.com/usermanual-iothub/iot_01_0079.html#section1)](tag:hws) [[查看实例详情](https://support.huaweicloud.com/intl/zh-cn/usermanual-iothub/iot_01_0079.html#section1)](tag:hws_hk)。
        :type instance_id: str
        :param start_time: **参数说明**：查询命令下发时间在startTime之后的记录，格式：yyyyMMdd&#39;T&#39;HHmmss&#39;Z&#39;，如20151212T121212Z。
        :type start_time: str
        :param end_time: **参数说明**：查询命令下发时间在endTime之前的记录，格式：yyyyMMdd&#39;T&#39;HHmmss&#39;Z&#39;，如20151212T121212Z。
        :type end_time: str
        :param status: **参数说明**：命令状态。
        :type status: str
        :param command_name: **参数说明**：命令名称。
        :type command_name: str
        """
        
        

        self._device_id = None
        self._instance_id = None
        self._start_time = None
        self._end_time = None
        self._status = None
        self._command_name = None
        self.discriminator = None

        self.device_id = device_id
        if instance_id is not None:
            self.instance_id = instance_id
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if status is not None:
            self.status = status
        if command_name is not None:
            self.command_name = command_name

    @property
    def device_id(self):
        r"""Gets the device_id of this CountAsyncHistoryCommandsRequest.

        **参数说明**：下发命令的设备ID，用于唯一标识一个设备，在注册设备时由物联网平台分配获得。 **取值范围**：长度不超过128，只允许字母、数字、下划线（_）、连接符（-）的组合。

        :return: The device_id of this CountAsyncHistoryCommandsRequest.
        :rtype: str
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        r"""Sets the device_id of this CountAsyncHistoryCommandsRequest.

        **参数说明**：下发命令的设备ID，用于唯一标识一个设备，在注册设备时由物联网平台分配获得。 **取值范围**：长度不超过128，只允许字母、数字、下划线（_）、连接符（-）的组合。

        :param device_id: The device_id of this CountAsyncHistoryCommandsRequest.
        :type device_id: str
        """
        self._device_id = device_id

    @property
    def instance_id(self):
        r"""Gets the instance_id of this CountAsyncHistoryCommandsRequest.

        **参数说明**：实例ID。物理多租下各实例的唯一标识，建议携带该参数，在使用专业版时必须携带该参数。您可以在IoTDA管理控制台界面，选择左侧导航栏“总览”页签查看当前实例的ID，具体获取方式请参考[[查看实例详情](https://support.huaweicloud.com/usermanual-iothub/iot_01_0079.html#section1)](tag:hws) [[查看实例详情](https://support.huaweicloud.com/intl/zh-cn/usermanual-iothub/iot_01_0079.html#section1)](tag:hws_hk)。

        :return: The instance_id of this CountAsyncHistoryCommandsRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this CountAsyncHistoryCommandsRequest.

        **参数说明**：实例ID。物理多租下各实例的唯一标识，建议携带该参数，在使用专业版时必须携带该参数。您可以在IoTDA管理控制台界面，选择左侧导航栏“总览”页签查看当前实例的ID，具体获取方式请参考[[查看实例详情](https://support.huaweicloud.com/usermanual-iothub/iot_01_0079.html#section1)](tag:hws) [[查看实例详情](https://support.huaweicloud.com/intl/zh-cn/usermanual-iothub/iot_01_0079.html#section1)](tag:hws_hk)。

        :param instance_id: The instance_id of this CountAsyncHistoryCommandsRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def start_time(self):
        r"""Gets the start_time of this CountAsyncHistoryCommandsRequest.

        **参数说明**：查询命令下发时间在startTime之后的记录，格式：yyyyMMdd'T'HHmmss'Z'，如20151212T121212Z。

        :return: The start_time of this CountAsyncHistoryCommandsRequest.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this CountAsyncHistoryCommandsRequest.

        **参数说明**：查询命令下发时间在startTime之后的记录，格式：yyyyMMdd'T'HHmmss'Z'，如20151212T121212Z。

        :param start_time: The start_time of this CountAsyncHistoryCommandsRequest.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this CountAsyncHistoryCommandsRequest.

        **参数说明**：查询命令下发时间在endTime之前的记录，格式：yyyyMMdd'T'HHmmss'Z'，如20151212T121212Z。

        :return: The end_time of this CountAsyncHistoryCommandsRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this CountAsyncHistoryCommandsRequest.

        **参数说明**：查询命令下发时间在endTime之前的记录，格式：yyyyMMdd'T'HHmmss'Z'，如20151212T121212Z。

        :param end_time: The end_time of this CountAsyncHistoryCommandsRequest.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def status(self):
        r"""Gets the status of this CountAsyncHistoryCommandsRequest.

        **参数说明**：命令状态。

        :return: The status of this CountAsyncHistoryCommandsRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this CountAsyncHistoryCommandsRequest.

        **参数说明**：命令状态。

        :param status: The status of this CountAsyncHistoryCommandsRequest.
        :type status: str
        """
        self._status = status

    @property
    def command_name(self):
        r"""Gets the command_name of this CountAsyncHistoryCommandsRequest.

        **参数说明**：命令名称。

        :return: The command_name of this CountAsyncHistoryCommandsRequest.
        :rtype: str
        """
        return self._command_name

    @command_name.setter
    def command_name(self, command_name):
        r"""Sets the command_name of this CountAsyncHistoryCommandsRequest.

        **参数说明**：命令名称。

        :param command_name: The command_name of this CountAsyncHistoryCommandsRequest.
        :type command_name: str
        """
        self._command_name = command_name

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
        if not isinstance(other, CountAsyncHistoryCommandsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
