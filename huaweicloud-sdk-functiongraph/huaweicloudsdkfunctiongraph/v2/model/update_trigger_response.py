# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateTriggerResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'trigger_id': 'str',
        'trigger_type_code': 'str',
        'trigger_status': 'str',
        'event_data': 'object',
        'last_updated_time': 'datetime',
        'created_time': 'datetime'
    }

    attribute_map = {
        'trigger_id': 'trigger_id',
        'trigger_type_code': 'trigger_type_code',
        'trigger_status': 'trigger_status',
        'event_data': 'event_data',
        'last_updated_time': 'last_updated_time',
        'created_time': 'created_time'
    }

    def __init__(self, trigger_id=None, trigger_type_code=None, trigger_status=None, event_data=None, last_updated_time=None, created_time=None):
        """UpdateTriggerResponse

        The model defined in huaweicloud sdk

        :param trigger_id: 触发器ID。
        :type trigger_id: str
        :param trigger_type_code: 触发器类型。  - TIMER: \&quot;定时触发器。\&quot; - APIG: \&quot;APIG触发器。\&quot; - CTS: \&quot;云审计服务触发器。\&quot; - DDS: \&quot;文档数据库服务触发器。\&quot; - DMS: \&quot;分布式服务触发器。\&quot; - DIS: \&quot;数据接入服务触发器。\&quot; - LTS: \&quot;云日志服务触发器。\&quot; - OBS: \&quot;对象存储触发器。\&quot; - SMN: \&quot;消息通知服务触发器。\&quot; - KAFKA: \&quot;专享版消息通知服务触发器。\&quot;
        :type trigger_type_code: str
        :param trigger_status: \&quot;触发器状态\&quot;  - ACTIVE: 启用状态。 - DISABLED: 禁用状态。
        :type trigger_status: str
        :param event_data: 触发器源事件。
        :type event_data: object
        :param last_updated_time: 最后更新时间。
        :type last_updated_time: datetime
        :param created_time: 触发器创建时间。
        :type created_time: datetime
        """
        
        super(UpdateTriggerResponse, self).__init__()

        self._trigger_id = None
        self._trigger_type_code = None
        self._trigger_status = None
        self._event_data = None
        self._last_updated_time = None
        self._created_time = None
        self.discriminator = None

        if trigger_id is not None:
            self.trigger_id = trigger_id
        if trigger_type_code is not None:
            self.trigger_type_code = trigger_type_code
        if trigger_status is not None:
            self.trigger_status = trigger_status
        if event_data is not None:
            self.event_data = event_data
        if last_updated_time is not None:
            self.last_updated_time = last_updated_time
        if created_time is not None:
            self.created_time = created_time

    @property
    def trigger_id(self):
        """Gets the trigger_id of this UpdateTriggerResponse.

        触发器ID。

        :return: The trigger_id of this UpdateTriggerResponse.
        :rtype: str
        """
        return self._trigger_id

    @trigger_id.setter
    def trigger_id(self, trigger_id):
        """Sets the trigger_id of this UpdateTriggerResponse.

        触发器ID。

        :param trigger_id: The trigger_id of this UpdateTriggerResponse.
        :type trigger_id: str
        """
        self._trigger_id = trigger_id

    @property
    def trigger_type_code(self):
        """Gets the trigger_type_code of this UpdateTriggerResponse.

        触发器类型。  - TIMER: \"定时触发器。\" - APIG: \"APIG触发器。\" - CTS: \"云审计服务触发器。\" - DDS: \"文档数据库服务触发器。\" - DMS: \"分布式服务触发器。\" - DIS: \"数据接入服务触发器。\" - LTS: \"云日志服务触发器。\" - OBS: \"对象存储触发器。\" - SMN: \"消息通知服务触发器。\" - KAFKA: \"专享版消息通知服务触发器。\"

        :return: The trigger_type_code of this UpdateTriggerResponse.
        :rtype: str
        """
        return self._trigger_type_code

    @trigger_type_code.setter
    def trigger_type_code(self, trigger_type_code):
        """Sets the trigger_type_code of this UpdateTriggerResponse.

        触发器类型。  - TIMER: \"定时触发器。\" - APIG: \"APIG触发器。\" - CTS: \"云审计服务触发器。\" - DDS: \"文档数据库服务触发器。\" - DMS: \"分布式服务触发器。\" - DIS: \"数据接入服务触发器。\" - LTS: \"云日志服务触发器。\" - OBS: \"对象存储触发器。\" - SMN: \"消息通知服务触发器。\" - KAFKA: \"专享版消息通知服务触发器。\"

        :param trigger_type_code: The trigger_type_code of this UpdateTriggerResponse.
        :type trigger_type_code: str
        """
        self._trigger_type_code = trigger_type_code

    @property
    def trigger_status(self):
        """Gets the trigger_status of this UpdateTriggerResponse.

        \"触发器状态\"  - ACTIVE: 启用状态。 - DISABLED: 禁用状态。

        :return: The trigger_status of this UpdateTriggerResponse.
        :rtype: str
        """
        return self._trigger_status

    @trigger_status.setter
    def trigger_status(self, trigger_status):
        """Sets the trigger_status of this UpdateTriggerResponse.

        \"触发器状态\"  - ACTIVE: 启用状态。 - DISABLED: 禁用状态。

        :param trigger_status: The trigger_status of this UpdateTriggerResponse.
        :type trigger_status: str
        """
        self._trigger_status = trigger_status

    @property
    def event_data(self):
        """Gets the event_data of this UpdateTriggerResponse.

        触发器源事件。

        :return: The event_data of this UpdateTriggerResponse.
        :rtype: object
        """
        return self._event_data

    @event_data.setter
    def event_data(self, event_data):
        """Sets the event_data of this UpdateTriggerResponse.

        触发器源事件。

        :param event_data: The event_data of this UpdateTriggerResponse.
        :type event_data: object
        """
        self._event_data = event_data

    @property
    def last_updated_time(self):
        """Gets the last_updated_time of this UpdateTriggerResponse.

        最后更新时间。

        :return: The last_updated_time of this UpdateTriggerResponse.
        :rtype: datetime
        """
        return self._last_updated_time

    @last_updated_time.setter
    def last_updated_time(self, last_updated_time):
        """Sets the last_updated_time of this UpdateTriggerResponse.

        最后更新时间。

        :param last_updated_time: The last_updated_time of this UpdateTriggerResponse.
        :type last_updated_time: datetime
        """
        self._last_updated_time = last_updated_time

    @property
    def created_time(self):
        """Gets the created_time of this UpdateTriggerResponse.

        触发器创建时间。

        :return: The created_time of this UpdateTriggerResponse.
        :rtype: datetime
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this UpdateTriggerResponse.

        触发器创建时间。

        :param created_time: The created_time of this UpdateTriggerResponse.
        :type created_time: datetime
        """
        self._created_time = created_time

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
        if not isinstance(other, UpdateTriggerResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
