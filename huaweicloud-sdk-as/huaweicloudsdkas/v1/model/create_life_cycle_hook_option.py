# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateLifeCycleHookOption:

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
        'notification_metadata': 'str'
    }

    attribute_map = {
        'lifecycle_hook_name': 'lifecycle_hook_name',
        'lifecycle_hook_type': 'lifecycle_hook_type',
        'default_result': 'default_result',
        'default_timeout': 'default_timeout',
        'notification_topic_urn': 'notification_topic_urn',
        'notification_metadata': 'notification_metadata'
    }

    def __init__(self, lifecycle_hook_name=None, lifecycle_hook_type=None, default_result=None, default_timeout=None, notification_topic_urn=None, notification_metadata=None):
        """CreateLifeCycleHookOption

        The model defined in huaweicloud sdk

        :param lifecycle_hook_name: 生命周期挂钩名称(1-32个字符)，只能包含字母、数字、下划线或中划线。
        :type lifecycle_hook_name: str
        :param lifecycle_hook_type: 生命周期挂钩类型。INSTANCE_TERMINATING。INSTANCE_LAUNCHING。INSTANCE_TERMINATING 类型的挂钩负责在实例终止时将实例挂起，INSTANCE_LAUNCHING 类型的挂钩则是在实例启动时将实例挂起。
        :type lifecycle_hook_type: str
        :param default_result: 生命周期挂钩默认回调操作。默认情况下，到达超时时间后执行的操作。ABANDON；CONTINUE；如果实例正在启动，则 CONTINUE 表示用户自定义操作已成功，可将实例投入使用。否则，ABANDON 表示用户自定义操作未成功，终止实例，伸缩活动置为失败，重新创建新实例。如果实例正在终止，则 ABANDON 和 CONTINUE 都允许终止实例。不过，ABANDON 将停止其他生命周期挂钩，而 CONTINUE 将允许完成其他生命周期挂钩。该字段缺省时默认为 ABANDON。
        :type default_result: str
        :param default_timeout: 生命周期挂钩超时时间，取值范围300-86400，默认为3600，单位是秒。默认情况下，实例保持等待状态的时间。您可以延长超时时间，也可以在超时时间结束前进行 CONTINUE 或 ABANDON 操作。
        :type default_timeout: int
        :param notification_topic_urn: SMN 服务中 Topic 的唯一的资源标识。为生命周期挂钩定义一个通知目标，当实例被生命周期挂钩挂起时向该通知目标发送消息。该消息包含实例的基本信息、用户自定义通知消息，以及可用于控制生命周期操作的令牌信息。
        :type notification_topic_urn: str
        :param notification_metadata: 自定义通知消息，长度不超过256位，不能包含字符&lt; &gt; &amp; &#39; ( )当配置了通知目标时，可向其发送用户自定义的通知内容。
        :type notification_metadata: str
        """
        
        

        self._lifecycle_hook_name = None
        self._lifecycle_hook_type = None
        self._default_result = None
        self._default_timeout = None
        self._notification_topic_urn = None
        self._notification_metadata = None
        self.discriminator = None

        self.lifecycle_hook_name = lifecycle_hook_name
        self.lifecycle_hook_type = lifecycle_hook_type
        if default_result is not None:
            self.default_result = default_result
        if default_timeout is not None:
            self.default_timeout = default_timeout
        self.notification_topic_urn = notification_topic_urn
        if notification_metadata is not None:
            self.notification_metadata = notification_metadata

    @property
    def lifecycle_hook_name(self):
        """Gets the lifecycle_hook_name of this CreateLifeCycleHookOption.

        生命周期挂钩名称(1-32个字符)，只能包含字母、数字、下划线或中划线。

        :return: The lifecycle_hook_name of this CreateLifeCycleHookOption.
        :rtype: str
        """
        return self._lifecycle_hook_name

    @lifecycle_hook_name.setter
    def lifecycle_hook_name(self, lifecycle_hook_name):
        """Sets the lifecycle_hook_name of this CreateLifeCycleHookOption.

        生命周期挂钩名称(1-32个字符)，只能包含字母、数字、下划线或中划线。

        :param lifecycle_hook_name: The lifecycle_hook_name of this CreateLifeCycleHookOption.
        :type lifecycle_hook_name: str
        """
        self._lifecycle_hook_name = lifecycle_hook_name

    @property
    def lifecycle_hook_type(self):
        """Gets the lifecycle_hook_type of this CreateLifeCycleHookOption.

        生命周期挂钩类型。INSTANCE_TERMINATING。INSTANCE_LAUNCHING。INSTANCE_TERMINATING 类型的挂钩负责在实例终止时将实例挂起，INSTANCE_LAUNCHING 类型的挂钩则是在实例启动时将实例挂起。

        :return: The lifecycle_hook_type of this CreateLifeCycleHookOption.
        :rtype: str
        """
        return self._lifecycle_hook_type

    @lifecycle_hook_type.setter
    def lifecycle_hook_type(self, lifecycle_hook_type):
        """Sets the lifecycle_hook_type of this CreateLifeCycleHookOption.

        生命周期挂钩类型。INSTANCE_TERMINATING。INSTANCE_LAUNCHING。INSTANCE_TERMINATING 类型的挂钩负责在实例终止时将实例挂起，INSTANCE_LAUNCHING 类型的挂钩则是在实例启动时将实例挂起。

        :param lifecycle_hook_type: The lifecycle_hook_type of this CreateLifeCycleHookOption.
        :type lifecycle_hook_type: str
        """
        self._lifecycle_hook_type = lifecycle_hook_type

    @property
    def default_result(self):
        """Gets the default_result of this CreateLifeCycleHookOption.

        生命周期挂钩默认回调操作。默认情况下，到达超时时间后执行的操作。ABANDON；CONTINUE；如果实例正在启动，则 CONTINUE 表示用户自定义操作已成功，可将实例投入使用。否则，ABANDON 表示用户自定义操作未成功，终止实例，伸缩活动置为失败，重新创建新实例。如果实例正在终止，则 ABANDON 和 CONTINUE 都允许终止实例。不过，ABANDON 将停止其他生命周期挂钩，而 CONTINUE 将允许完成其他生命周期挂钩。该字段缺省时默认为 ABANDON。

        :return: The default_result of this CreateLifeCycleHookOption.
        :rtype: str
        """
        return self._default_result

    @default_result.setter
    def default_result(self, default_result):
        """Sets the default_result of this CreateLifeCycleHookOption.

        生命周期挂钩默认回调操作。默认情况下，到达超时时间后执行的操作。ABANDON；CONTINUE；如果实例正在启动，则 CONTINUE 表示用户自定义操作已成功，可将实例投入使用。否则，ABANDON 表示用户自定义操作未成功，终止实例，伸缩活动置为失败，重新创建新实例。如果实例正在终止，则 ABANDON 和 CONTINUE 都允许终止实例。不过，ABANDON 将停止其他生命周期挂钩，而 CONTINUE 将允许完成其他生命周期挂钩。该字段缺省时默认为 ABANDON。

        :param default_result: The default_result of this CreateLifeCycleHookOption.
        :type default_result: str
        """
        self._default_result = default_result

    @property
    def default_timeout(self):
        """Gets the default_timeout of this CreateLifeCycleHookOption.

        生命周期挂钩超时时间，取值范围300-86400，默认为3600，单位是秒。默认情况下，实例保持等待状态的时间。您可以延长超时时间，也可以在超时时间结束前进行 CONTINUE 或 ABANDON 操作。

        :return: The default_timeout of this CreateLifeCycleHookOption.
        :rtype: int
        """
        return self._default_timeout

    @default_timeout.setter
    def default_timeout(self, default_timeout):
        """Sets the default_timeout of this CreateLifeCycleHookOption.

        生命周期挂钩超时时间，取值范围300-86400，默认为3600，单位是秒。默认情况下，实例保持等待状态的时间。您可以延长超时时间，也可以在超时时间结束前进行 CONTINUE 或 ABANDON 操作。

        :param default_timeout: The default_timeout of this CreateLifeCycleHookOption.
        :type default_timeout: int
        """
        self._default_timeout = default_timeout

    @property
    def notification_topic_urn(self):
        """Gets the notification_topic_urn of this CreateLifeCycleHookOption.

        SMN 服务中 Topic 的唯一的资源标识。为生命周期挂钩定义一个通知目标，当实例被生命周期挂钩挂起时向该通知目标发送消息。该消息包含实例的基本信息、用户自定义通知消息，以及可用于控制生命周期操作的令牌信息。

        :return: The notification_topic_urn of this CreateLifeCycleHookOption.
        :rtype: str
        """
        return self._notification_topic_urn

    @notification_topic_urn.setter
    def notification_topic_urn(self, notification_topic_urn):
        """Sets the notification_topic_urn of this CreateLifeCycleHookOption.

        SMN 服务中 Topic 的唯一的资源标识。为生命周期挂钩定义一个通知目标，当实例被生命周期挂钩挂起时向该通知目标发送消息。该消息包含实例的基本信息、用户自定义通知消息，以及可用于控制生命周期操作的令牌信息。

        :param notification_topic_urn: The notification_topic_urn of this CreateLifeCycleHookOption.
        :type notification_topic_urn: str
        """
        self._notification_topic_urn = notification_topic_urn

    @property
    def notification_metadata(self):
        """Gets the notification_metadata of this CreateLifeCycleHookOption.

        自定义通知消息，长度不超过256位，不能包含字符< > & ' ( )当配置了通知目标时，可向其发送用户自定义的通知内容。

        :return: The notification_metadata of this CreateLifeCycleHookOption.
        :rtype: str
        """
        return self._notification_metadata

    @notification_metadata.setter
    def notification_metadata(self, notification_metadata):
        """Sets the notification_metadata of this CreateLifeCycleHookOption.

        自定义通知消息，长度不超过256位，不能包含字符< > & ' ( )当配置了通知目标时，可向其发送用户自定义的通知内容。

        :param notification_metadata: The notification_metadata of this CreateLifeCycleHookOption.
        :type notification_metadata: str
        """
        self._notification_metadata = notification_metadata

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
        if not isinstance(other, CreateLifeCycleHookOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
