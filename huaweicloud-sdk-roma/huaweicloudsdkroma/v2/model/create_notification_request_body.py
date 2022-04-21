# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateNotificationRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'app_id': 'str',
        'type': 'int',
        'topic': 'str',
        'status': 'int'
    }

    attribute_map = {
        'app_id': 'app_id',
        'type': 'type',
        'topic': 'topic',
        'status': 'status'
    }

    def __init__(self, app_id=None, type=None, topic=None, status=None):
        """CreateNotificationRequestBody

        The model defined in huaweicloud sdk

        :param app_id: 通知归属的应用ID
        :type app_id: str
        :param type: 通知类型 0-设备上线通知 1-设备下线通知 2-设备添加通知 3-设备删除通知 4-设备变更通知
        :type type: int
        :param topic: 通知发送的主题名，该主题需要在MQS存在
        :type topic: str
        :param status: 启停状态 0-启用 1-停用
        :type status: int
        """
        
        

        self._app_id = None
        self._type = None
        self._topic = None
        self._status = None
        self.discriminator = None

        self.app_id = app_id
        self.type = type
        self.topic = topic
        self.status = status

    @property
    def app_id(self):
        """Gets the app_id of this CreateNotificationRequestBody.

        通知归属的应用ID

        :return: The app_id of this CreateNotificationRequestBody.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this CreateNotificationRequestBody.

        通知归属的应用ID

        :param app_id: The app_id of this CreateNotificationRequestBody.
        :type app_id: str
        """
        self._app_id = app_id

    @property
    def type(self):
        """Gets the type of this CreateNotificationRequestBody.

        通知类型 0-设备上线通知 1-设备下线通知 2-设备添加通知 3-设备删除通知 4-设备变更通知

        :return: The type of this CreateNotificationRequestBody.
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CreateNotificationRequestBody.

        通知类型 0-设备上线通知 1-设备下线通知 2-设备添加通知 3-设备删除通知 4-设备变更通知

        :param type: The type of this CreateNotificationRequestBody.
        :type type: int
        """
        self._type = type

    @property
    def topic(self):
        """Gets the topic of this CreateNotificationRequestBody.

        通知发送的主题名，该主题需要在MQS存在

        :return: The topic of this CreateNotificationRequestBody.
        :rtype: str
        """
        return self._topic

    @topic.setter
    def topic(self, topic):
        """Sets the topic of this CreateNotificationRequestBody.

        通知发送的主题名，该主题需要在MQS存在

        :param topic: The topic of this CreateNotificationRequestBody.
        :type topic: str
        """
        self._topic = topic

    @property
    def status(self):
        """Gets the status of this CreateNotificationRequestBody.

        启停状态 0-启用 1-停用

        :return: The status of this CreateNotificationRequestBody.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CreateNotificationRequestBody.

        启停状态 0-启用 1-停用

        :param status: The status of this CreateNotificationRequestBody.
        :type status: int
        """
        self._status = status

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
        if not isinstance(other, CreateNotificationRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
