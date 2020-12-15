# coding: utf-8

import pprint
import re

import six





class CreateFunctionTriggerRequestBody:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'trigger_type_code': 'str',
        'trigger_status': 'str',
        'event_type_code': 'str',
        'event_data': 'object'
    }

    attribute_map = {
        'trigger_type_code': 'trigger_type_code',
        'trigger_status': 'trigger_status',
        'event_type_code': 'event_type_code',
        'event_data': 'event_data'
    }

    def __init__(self, trigger_type_code=None, trigger_status=None, event_type_code=None, event_data=None):
        """CreateFunctionTriggerRequestBody - a model defined in huaweicloud sdk"""
        
        

        self._trigger_type_code = None
        self._trigger_status = None
        self._event_type_code = None
        self._event_data = None
        self.discriminator = None

        self.trigger_type_code = trigger_type_code
        if trigger_status is not None:
            self.trigger_status = trigger_status
        if event_type_code is not None:
            self.event_type_code = event_type_code
        self.event_data = event_data

    @property
    def trigger_type_code(self):
        """Gets the trigger_type_code of this CreateFunctionTriggerRequestBody.

        触发器类型。  - TIMER: 定时触发器。 - APIG: APIGW触发器。 - CTS: 云审计触发器，需要先开通云审计服务。 - DDS: 文档数据库触发器，需要开启函数vpc。 - DMS: 分布式消息服务触发器，需要配置dms委托。 - DIS: 数据接入服务触发器，需要配置dis委托。 - LTS: 云审计日志服务触发器，需要配置lts委托。 - OBS: 对象存储服务触发器。 - KAFKA: 专享版本kafka触发器。

        :return: The trigger_type_code of this CreateFunctionTriggerRequestBody.
        :rtype: str
        """
        return self._trigger_type_code

    @trigger_type_code.setter
    def trigger_type_code(self, trigger_type_code):
        """Sets the trigger_type_code of this CreateFunctionTriggerRequestBody.

        触发器类型。  - TIMER: 定时触发器。 - APIG: APIGW触发器。 - CTS: 云审计触发器，需要先开通云审计服务。 - DDS: 文档数据库触发器，需要开启函数vpc。 - DMS: 分布式消息服务触发器，需要配置dms委托。 - DIS: 数据接入服务触发器，需要配置dis委托。 - LTS: 云审计日志服务触发器，需要配置lts委托。 - OBS: 对象存储服务触发器。 - KAFKA: 专享版本kafka触发器。

        :param trigger_type_code: The trigger_type_code of this CreateFunctionTriggerRequestBody.
        :type: str
        """
        self._trigger_type_code = trigger_type_code

    @property
    def trigger_status(self):
        """Gets the trigger_status of this CreateFunctionTriggerRequestBody.

        触发器状态，取值为ACTIVE,DISABLED。

        :return: The trigger_status of this CreateFunctionTriggerRequestBody.
        :rtype: str
        """
        return self._trigger_status

    @trigger_status.setter
    def trigger_status(self, trigger_status):
        """Sets the trigger_status of this CreateFunctionTriggerRequestBody.

        触发器状态，取值为ACTIVE,DISABLED。

        :param trigger_status: The trigger_status of this CreateFunctionTriggerRequestBody.
        :type: str
        """
        self._trigger_status = trigger_status

    @property
    def event_type_code(self):
        """Gets the event_type_code of this CreateFunctionTriggerRequestBody.

        消息代码。

        :return: The event_type_code of this CreateFunctionTriggerRequestBody.
        :rtype: str
        """
        return self._event_type_code

    @event_type_code.setter
    def event_type_code(self, event_type_code):
        """Sets the event_type_code of this CreateFunctionTriggerRequestBody.

        消息代码。

        :param event_type_code: The event_type_code of this CreateFunctionTriggerRequestBody.
        :type: str
        """
        self._event_type_code = event_type_code

    @property
    def event_data(self):
        """Gets the event_data of this CreateFunctionTriggerRequestBody.

        事件结构体。

        :return: The event_data of this CreateFunctionTriggerRequestBody.
        :rtype: object
        """
        return self._event_data

    @event_data.setter
    def event_data(self, event_data):
        """Sets the event_data of this CreateFunctionTriggerRequestBody.

        事件结构体。

        :param event_data: The event_data of this CreateFunctionTriggerRequestBody.
        :type: object
        """
        self._event_data = event_data

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CreateFunctionTriggerRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
