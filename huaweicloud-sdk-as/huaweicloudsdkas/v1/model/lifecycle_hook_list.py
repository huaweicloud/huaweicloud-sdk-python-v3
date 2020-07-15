# coding: utf-8

import pprint
import re

import six





class LifecycleHookList:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'lifecycle_hook_name': 'str',
        'lifecycle_hook_type': 'str',
        'default_result': 'str',
        'default_timeout': 'int',
        'notification_topic_urn': 'str',
        'notification_topic_name': 'str',
        'notification_metadata': 'str',
        'create_time': 'datetime'
    }

    attribute_map = {
        'lifecycle_hook_name': 'lifecycle_hook_name',
        'lifecycle_hook_type': 'lifecycle_hook_type',
        'default_result': 'default_result',
        'default_timeout': 'default_timeout',
        'notification_topic_urn': 'notification_topic_urn',
        'notification_topic_name': 'notification_topic_name',
        'notification_metadata': 'notification_metadata',
        'create_time': 'create_time'
    }

    def __init__(self, lifecycle_hook_name=None, lifecycle_hook_type=None, default_result=None, default_timeout=None, notification_topic_urn=None, notification_topic_name=None, notification_metadata=None, create_time=None):
        """LifecycleHookList - a model defined in huaweicloud sdk"""
        
        

        self._lifecycle_hook_name = None
        self._lifecycle_hook_type = None
        self._default_result = None
        self._default_timeout = None
        self._notification_topic_urn = None
        self._notification_topic_name = None
        self._notification_metadata = None
        self._create_time = None
        self.discriminator = None

        if lifecycle_hook_name is not None:
            self.lifecycle_hook_name = lifecycle_hook_name
        if lifecycle_hook_type is not None:
            self.lifecycle_hook_type = lifecycle_hook_type
        if default_result is not None:
            self.default_result = default_result
        if default_timeout is not None:
            self.default_timeout = default_timeout
        if notification_topic_urn is not None:
            self.notification_topic_urn = notification_topic_urn
        if notification_topic_name is not None:
            self.notification_topic_name = notification_topic_name
        if notification_metadata is not None:
            self.notification_metadata = notification_metadata
        if create_time is not None:
            self.create_time = create_time

    @property
    def lifecycle_hook_name(self):
        """Gets the lifecycle_hook_name of this LifecycleHookList.

        生命周期挂钩名称。

        :return: The lifecycle_hook_name of this LifecycleHookList.
        :rtype: str
        """
        return self._lifecycle_hook_name

    @lifecycle_hook_name.setter
    def lifecycle_hook_name(self, lifecycle_hook_name):
        """Sets the lifecycle_hook_name of this LifecycleHookList.

        生命周期挂钩名称。

        :param lifecycle_hook_name: The lifecycle_hook_name of this LifecycleHookList.
        :type: str
        """
        self._lifecycle_hook_name = lifecycle_hook_name

    @property
    def lifecycle_hook_type(self):
        """Gets the lifecycle_hook_type of this LifecycleHookList.

        生命周期挂钩类型。INSTANCE_TERMINATING；INSTANCE_LAUNCHING。

        :return: The lifecycle_hook_type of this LifecycleHookList.
        :rtype: str
        """
        return self._lifecycle_hook_type

    @lifecycle_hook_type.setter
    def lifecycle_hook_type(self, lifecycle_hook_type):
        """Sets the lifecycle_hook_type of this LifecycleHookList.

        生命周期挂钩类型。INSTANCE_TERMINATING；INSTANCE_LAUNCHING。

        :param lifecycle_hook_type: The lifecycle_hook_type of this LifecycleHookList.
        :type: str
        """
        self._lifecycle_hook_type = lifecycle_hook_type

    @property
    def default_result(self):
        """Gets the default_result of this LifecycleHookList.

        生命周期挂钩默认回调操作。ABANDON;CONTINUE。

        :return: The default_result of this LifecycleHookList.
        :rtype: str
        """
        return self._default_result

    @default_result.setter
    def default_result(self, default_result):
        """Sets the default_result of this LifecycleHookList.

        生命周期挂钩默认回调操作。ABANDON;CONTINUE。

        :param default_result: The default_result of this LifecycleHookList.
        :type: str
        """
        self._default_result = default_result

    @property
    def default_timeout(self):
        """Gets the default_timeout of this LifecycleHookList.

        生命周期挂钩超时时间，单位秒。

        :return: The default_timeout of this LifecycleHookList.
        :rtype: int
        """
        return self._default_timeout

    @default_timeout.setter
    def default_timeout(self, default_timeout):
        """Sets the default_timeout of this LifecycleHookList.

        生命周期挂钩超时时间，单位秒。

        :param default_timeout: The default_timeout of this LifecycleHookList.
        :type: int
        """
        self._default_timeout = default_timeout

    @property
    def notification_topic_urn(self):
        """Gets the notification_topic_urn of this LifecycleHookList.

        SMN服务中Topic的唯一的资源标识。

        :return: The notification_topic_urn of this LifecycleHookList.
        :rtype: str
        """
        return self._notification_topic_urn

    @notification_topic_urn.setter
    def notification_topic_urn(self, notification_topic_urn):
        """Sets the notification_topic_urn of this LifecycleHookList.

        SMN服务中Topic的唯一的资源标识。

        :param notification_topic_urn: The notification_topic_urn of this LifecycleHookList.
        :type: str
        """
        self._notification_topic_urn = notification_topic_urn

    @property
    def notification_topic_name(self):
        """Gets the notification_topic_name of this LifecycleHookList.

        SMN服务中Topic的资源名称。

        :return: The notification_topic_name of this LifecycleHookList.
        :rtype: str
        """
        return self._notification_topic_name

    @notification_topic_name.setter
    def notification_topic_name(self, notification_topic_name):
        """Sets the notification_topic_name of this LifecycleHookList.

        SMN服务中Topic的资源名称。

        :param notification_topic_name: The notification_topic_name of this LifecycleHookList.
        :type: str
        """
        self._notification_topic_name = notification_topic_name

    @property
    def notification_metadata(self):
        """Gets the notification_metadata of this LifecycleHookList.

        自定义通知消息。

        :return: The notification_metadata of this LifecycleHookList.
        :rtype: str
        """
        return self._notification_metadata

    @notification_metadata.setter
    def notification_metadata(self, notification_metadata):
        """Sets the notification_metadata of this LifecycleHookList.

        自定义通知消息。

        :param notification_metadata: The notification_metadata of this LifecycleHookList.
        :type: str
        """
        self._notification_metadata = notification_metadata

    @property
    def create_time(self):
        """Gets the create_time of this LifecycleHookList.

        创建生命周期挂钩时间，遵循UTC时间。

        :return: The create_time of this LifecycleHookList.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this LifecycleHookList.

        创建生命周期挂钩时间，遵循UTC时间。

        :param create_time: The create_time of this LifecycleHookList.
        :type: datetime
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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, LifecycleHookList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
