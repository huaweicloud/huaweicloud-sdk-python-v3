# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SendKafkaMessageRequest:

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
        'action_id': 'str',
        'body': 'SendKafkaMessageRequestBody'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'action_id': 'action_id',
        'body': 'body'
    }

    def __init__(self, instance_id=None, action_id=None, body=None):
        r"""SendKafkaMessageRequest

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID
        :type instance_id: str
        :param action_id: 动作ID，生产消息对应的action_id为send。
        :type action_id: str
        :param body: Body of the SendKafkaMessageRequest
        :type body: :class:`huaweicloudsdkkafka.v2.SendKafkaMessageRequestBody`
        """
        
        

        self._instance_id = None
        self._action_id = None
        self._body = None
        self.discriminator = None

        self.instance_id = instance_id
        self.action_id = action_id
        if body is not None:
            self.body = body

    @property
    def instance_id(self):
        r"""Gets the instance_id of this SendKafkaMessageRequest.

        实例ID

        :return: The instance_id of this SendKafkaMessageRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this SendKafkaMessageRequest.

        实例ID

        :param instance_id: The instance_id of this SendKafkaMessageRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def action_id(self):
        r"""Gets the action_id of this SendKafkaMessageRequest.

        动作ID，生产消息对应的action_id为send。

        :return: The action_id of this SendKafkaMessageRequest.
        :rtype: str
        """
        return self._action_id

    @action_id.setter
    def action_id(self, action_id):
        r"""Sets the action_id of this SendKafkaMessageRequest.

        动作ID，生产消息对应的action_id为send。

        :param action_id: The action_id of this SendKafkaMessageRequest.
        :type action_id: str
        """
        self._action_id = action_id

    @property
    def body(self):
        r"""Gets the body of this SendKafkaMessageRequest.

        :return: The body of this SendKafkaMessageRequest.
        :rtype: :class:`huaweicloudsdkkafka.v2.SendKafkaMessageRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this SendKafkaMessageRequest.

        :param body: The body of this SendKafkaMessageRequest.
        :type body: :class:`huaweicloudsdkkafka.v2.SendKafkaMessageRequestBody`
        """
        self._body = body

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
        if not isinstance(other, SendKafkaMessageRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
