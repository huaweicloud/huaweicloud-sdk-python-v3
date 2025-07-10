# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDesktopOperationsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'record_id': 'str',
        'event_type': 'str',
        'event_id': 'str',
        'event_level': 'str',
        'event_data': 'str',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'record_id': 'record_id',
        'event_type': 'event_type',
        'event_id': 'event_id',
        'event_level': 'event_level',
        'event_data': 'event_data',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, record_id=None, event_type=None, event_id=None, event_level=None, event_data=None, limit=None, offset=None):
        r"""ListDesktopOperationsRequest

        The model defined in huaweicloud sdk

        :param record_id: 录屏记录UUID。
        :type record_id: str
        :param event_type: 事件类型。 - APP：应用监控。 - FILE：文件监控。 - REG：注册表监控。 - HDP：协议行为监控。
        :type event_type: str
        :param event_id: 事件ID。 - APP_START：应用程序启动 - APP_STOP：应用程序结束 - APP_CRASH：应用程序异常退出 - APP_HANG：应用程序无响应 - APP_INSTALL：应用安装 - APP_UNINSTALL：应用卸裁 - FILE_CREATE：文件创建 - FILE_DELETE：文件删除 - FILE_RENAME：文件改名 - HDP_FILE：文件重定向 - HDP_USB：USB插拔事件 - HDP_CLIPBOARD：剪切板操作 - HDP_INPUTIDLE：空闲无操作 - HDP_PRINT：文件打印
        :type event_id: str
        :param event_level: 事件级别。 - INFO：提示。 - ALARM：告警。 - ERROR：异常。
        :type event_level: str
        :param event_data: 事件内容。
        :type event_data: str
        :param limit: 用于分页查询，返回录屏记录数量的限制。默认100。范围0~1000。
        :type limit: int
        :param offset: 用于分页查询，查询的起始记录序号，从0开始。
        :type offset: int
        """
        
        

        self._record_id = None
        self._event_type = None
        self._event_id = None
        self._event_level = None
        self._event_data = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        self.record_id = record_id
        if event_type is not None:
            self.event_type = event_type
        if event_id is not None:
            self.event_id = event_id
        if event_level is not None:
            self.event_level = event_level
        if event_data is not None:
            self.event_data = event_data
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def record_id(self):
        r"""Gets the record_id of this ListDesktopOperationsRequest.

        录屏记录UUID。

        :return: The record_id of this ListDesktopOperationsRequest.
        :rtype: str
        """
        return self._record_id

    @record_id.setter
    def record_id(self, record_id):
        r"""Sets the record_id of this ListDesktopOperationsRequest.

        录屏记录UUID。

        :param record_id: The record_id of this ListDesktopOperationsRequest.
        :type record_id: str
        """
        self._record_id = record_id

    @property
    def event_type(self):
        r"""Gets the event_type of this ListDesktopOperationsRequest.

        事件类型。 - APP：应用监控。 - FILE：文件监控。 - REG：注册表监控。 - HDP：协议行为监控。

        :return: The event_type of this ListDesktopOperationsRequest.
        :rtype: str
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        r"""Sets the event_type of this ListDesktopOperationsRequest.

        事件类型。 - APP：应用监控。 - FILE：文件监控。 - REG：注册表监控。 - HDP：协议行为监控。

        :param event_type: The event_type of this ListDesktopOperationsRequest.
        :type event_type: str
        """
        self._event_type = event_type

    @property
    def event_id(self):
        r"""Gets the event_id of this ListDesktopOperationsRequest.

        事件ID。 - APP_START：应用程序启动 - APP_STOP：应用程序结束 - APP_CRASH：应用程序异常退出 - APP_HANG：应用程序无响应 - APP_INSTALL：应用安装 - APP_UNINSTALL：应用卸裁 - FILE_CREATE：文件创建 - FILE_DELETE：文件删除 - FILE_RENAME：文件改名 - HDP_FILE：文件重定向 - HDP_USB：USB插拔事件 - HDP_CLIPBOARD：剪切板操作 - HDP_INPUTIDLE：空闲无操作 - HDP_PRINT：文件打印

        :return: The event_id of this ListDesktopOperationsRequest.
        :rtype: str
        """
        return self._event_id

    @event_id.setter
    def event_id(self, event_id):
        r"""Sets the event_id of this ListDesktopOperationsRequest.

        事件ID。 - APP_START：应用程序启动 - APP_STOP：应用程序结束 - APP_CRASH：应用程序异常退出 - APP_HANG：应用程序无响应 - APP_INSTALL：应用安装 - APP_UNINSTALL：应用卸裁 - FILE_CREATE：文件创建 - FILE_DELETE：文件删除 - FILE_RENAME：文件改名 - HDP_FILE：文件重定向 - HDP_USB：USB插拔事件 - HDP_CLIPBOARD：剪切板操作 - HDP_INPUTIDLE：空闲无操作 - HDP_PRINT：文件打印

        :param event_id: The event_id of this ListDesktopOperationsRequest.
        :type event_id: str
        """
        self._event_id = event_id

    @property
    def event_level(self):
        r"""Gets the event_level of this ListDesktopOperationsRequest.

        事件级别。 - INFO：提示。 - ALARM：告警。 - ERROR：异常。

        :return: The event_level of this ListDesktopOperationsRequest.
        :rtype: str
        """
        return self._event_level

    @event_level.setter
    def event_level(self, event_level):
        r"""Sets the event_level of this ListDesktopOperationsRequest.

        事件级别。 - INFO：提示。 - ALARM：告警。 - ERROR：异常。

        :param event_level: The event_level of this ListDesktopOperationsRequest.
        :type event_level: str
        """
        self._event_level = event_level

    @property
    def event_data(self):
        r"""Gets the event_data of this ListDesktopOperationsRequest.

        事件内容。

        :return: The event_data of this ListDesktopOperationsRequest.
        :rtype: str
        """
        return self._event_data

    @event_data.setter
    def event_data(self, event_data):
        r"""Sets the event_data of this ListDesktopOperationsRequest.

        事件内容。

        :param event_data: The event_data of this ListDesktopOperationsRequest.
        :type event_data: str
        """
        self._event_data = event_data

    @property
    def limit(self):
        r"""Gets the limit of this ListDesktopOperationsRequest.

        用于分页查询，返回录屏记录数量的限制。默认100。范围0~1000。

        :return: The limit of this ListDesktopOperationsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListDesktopOperationsRequest.

        用于分页查询，返回录屏记录数量的限制。默认100。范围0~1000。

        :param limit: The limit of this ListDesktopOperationsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListDesktopOperationsRequest.

        用于分页查询，查询的起始记录序号，从0开始。

        :return: The offset of this ListDesktopOperationsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListDesktopOperationsRequest.

        用于分页查询，查询的起始记录序号，从0开始。

        :param offset: The offset of this ListDesktopOperationsRequest.
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
        if not isinstance(other, ListDesktopOperationsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
