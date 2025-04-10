# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateNotificationResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'notification_id': 'int',
        'type': 'int',
        'status': 'int',
        'topic': 'str',
        'instance_id': 'str',
        'app_id': 'str'
    }

    attribute_map = {
        'notification_id': 'notification_id',
        'type': 'type',
        'status': 'status',
        'topic': 'topic',
        'instance_id': 'instance_id',
        'app_id': 'app_id'
    }

    def __init__(self, notification_id=None, type=None, status=None, topic=None, instance_id=None, app_id=None):
        r"""CreateNotificationResponse

        The model defined in huaweicloud sdk

        :param notification_id: 订阅ID
        :type notification_id: int
        :param type: 订阅类型, 0:设备上线通知类型, 1:设备下线通知类型, 2:设备添加通知类型, 3:设备删除通知类型, 4:设备变更通知类型
        :type type: int
        :param status: 订阅管理状态，0：启用，1：停用
        :type status: int
        :param topic: 订阅的topic名称
        :type topic: str
        :param instance_id: 实例ID
        :type instance_id: str
        :param app_id: 应用ID
        :type app_id: str
        """
        
        super(CreateNotificationResponse, self).__init__()

        self._notification_id = None
        self._type = None
        self._status = None
        self._topic = None
        self._instance_id = None
        self._app_id = None
        self.discriminator = None

        if notification_id is not None:
            self.notification_id = notification_id
        if type is not None:
            self.type = type
        if status is not None:
            self.status = status
        if topic is not None:
            self.topic = topic
        if instance_id is not None:
            self.instance_id = instance_id
        if app_id is not None:
            self.app_id = app_id

    @property
    def notification_id(self):
        r"""Gets the notification_id of this CreateNotificationResponse.

        订阅ID

        :return: The notification_id of this CreateNotificationResponse.
        :rtype: int
        """
        return self._notification_id

    @notification_id.setter
    def notification_id(self, notification_id):
        r"""Sets the notification_id of this CreateNotificationResponse.

        订阅ID

        :param notification_id: The notification_id of this CreateNotificationResponse.
        :type notification_id: int
        """
        self._notification_id = notification_id

    @property
    def type(self):
        r"""Gets the type of this CreateNotificationResponse.

        订阅类型, 0:设备上线通知类型, 1:设备下线通知类型, 2:设备添加通知类型, 3:设备删除通知类型, 4:设备变更通知类型

        :return: The type of this CreateNotificationResponse.
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this CreateNotificationResponse.

        订阅类型, 0:设备上线通知类型, 1:设备下线通知类型, 2:设备添加通知类型, 3:设备删除通知类型, 4:设备变更通知类型

        :param type: The type of this CreateNotificationResponse.
        :type type: int
        """
        self._type = type

    @property
    def status(self):
        r"""Gets the status of this CreateNotificationResponse.

        订阅管理状态，0：启用，1：停用

        :return: The status of this CreateNotificationResponse.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this CreateNotificationResponse.

        订阅管理状态，0：启用，1：停用

        :param status: The status of this CreateNotificationResponse.
        :type status: int
        """
        self._status = status

    @property
    def topic(self):
        r"""Gets the topic of this CreateNotificationResponse.

        订阅的topic名称

        :return: The topic of this CreateNotificationResponse.
        :rtype: str
        """
        return self._topic

    @topic.setter
    def topic(self, topic):
        r"""Sets the topic of this CreateNotificationResponse.

        订阅的topic名称

        :param topic: The topic of this CreateNotificationResponse.
        :type topic: str
        """
        self._topic = topic

    @property
    def instance_id(self):
        r"""Gets the instance_id of this CreateNotificationResponse.

        实例ID

        :return: The instance_id of this CreateNotificationResponse.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this CreateNotificationResponse.

        实例ID

        :param instance_id: The instance_id of this CreateNotificationResponse.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def app_id(self):
        r"""Gets the app_id of this CreateNotificationResponse.

        应用ID

        :return: The app_id of this CreateNotificationResponse.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        r"""Sets the app_id of this CreateNotificationResponse.

        应用ID

        :param app_id: The app_id of this CreateNotificationResponse.
        :type app_id: str
        """
        self._app_id = app_id

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
        if not isinstance(other, CreateNotificationResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
