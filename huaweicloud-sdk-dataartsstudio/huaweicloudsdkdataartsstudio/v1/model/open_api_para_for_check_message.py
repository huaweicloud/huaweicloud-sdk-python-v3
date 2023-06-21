# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OpenApiParaForCheckMessage:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'message_id': 'str',
        'action': 'int',
        'time': 'str'
    }

    attribute_map = {
        'message_id': 'message_id',
        'action': 'action',
        'time': 'time'
    }

    def __init__(self, message_id=None, action=None, time=None):
        """OpenApiParaForCheckMessage

        The model defined in huaweicloud sdk

        :param message_id: 消息编号
        :type message_id: str
        :param action: 执行动作。0&#x3D;立刻执行, 1&#x3D;定期执行。
        :type action: int
        :param time: 使用截止时间。仅定期执行需要此参数，默认服务器当前时间三天后。
        :type time: str
        """
        
        

        self._message_id = None
        self._action = None
        self._time = None
        self.discriminator = None

        if message_id is not None:
            self.message_id = message_id
        if action is not None:
            self.action = action
        if time is not None:
            self.time = time

    @property
    def message_id(self):
        """Gets the message_id of this OpenApiParaForCheckMessage.

        消息编号

        :return: The message_id of this OpenApiParaForCheckMessage.
        :rtype: str
        """
        return self._message_id

    @message_id.setter
    def message_id(self, message_id):
        """Sets the message_id of this OpenApiParaForCheckMessage.

        消息编号

        :param message_id: The message_id of this OpenApiParaForCheckMessage.
        :type message_id: str
        """
        self._message_id = message_id

    @property
    def action(self):
        """Gets the action of this OpenApiParaForCheckMessage.

        执行动作。0=立刻执行, 1=定期执行。

        :return: The action of this OpenApiParaForCheckMessage.
        :rtype: int
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this OpenApiParaForCheckMessage.

        执行动作。0=立刻执行, 1=定期执行。

        :param action: The action of this OpenApiParaForCheckMessage.
        :type action: int
        """
        self._action = action

    @property
    def time(self):
        """Gets the time of this OpenApiParaForCheckMessage.

        使用截止时间。仅定期执行需要此参数，默认服务器当前时间三天后。

        :return: The time of this OpenApiParaForCheckMessage.
        :rtype: str
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this OpenApiParaForCheckMessage.

        使用截止时间。仅定期执行需要此参数，默认服务器当前时间三天后。

        :param time: The time of this OpenApiParaForCheckMessage.
        :type time: str
        """
        self._time = time

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
        if not isinstance(other, OpenApiParaForCheckMessage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
