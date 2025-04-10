# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateConsumerGroupRequest:

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
        'group': 'str',
        'body': 'UpdateConsumerGroup'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'group': 'group',
        'body': 'body'
    }

    def __init__(self, instance_id=None, group=None, body=None):
        r"""UpdateConsumerGroupRequest

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID。
        :type instance_id: str
        :param group: 消费组名称。
        :type group: str
        :param body: Body of the UpdateConsumerGroupRequest
        :type body: :class:`huaweicloudsdkrocketmq.v2.UpdateConsumerGroup`
        """
        
        

        self._instance_id = None
        self._group = None
        self._body = None
        self.discriminator = None

        self.instance_id = instance_id
        self.group = group
        if body is not None:
            self.body = body

    @property
    def instance_id(self):
        r"""Gets the instance_id of this UpdateConsumerGroupRequest.

        实例ID。

        :return: The instance_id of this UpdateConsumerGroupRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this UpdateConsumerGroupRequest.

        实例ID。

        :param instance_id: The instance_id of this UpdateConsumerGroupRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def group(self):
        r"""Gets the group of this UpdateConsumerGroupRequest.

        消费组名称。

        :return: The group of this UpdateConsumerGroupRequest.
        :rtype: str
        """
        return self._group

    @group.setter
    def group(self, group):
        r"""Sets the group of this UpdateConsumerGroupRequest.

        消费组名称。

        :param group: The group of this UpdateConsumerGroupRequest.
        :type group: str
        """
        self._group = group

    @property
    def body(self):
        r"""Gets the body of this UpdateConsumerGroupRequest.

        :return: The body of this UpdateConsumerGroupRequest.
        :rtype: :class:`huaweicloudsdkrocketmq.v2.UpdateConsumerGroup`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this UpdateConsumerGroupRequest.

        :param body: The body of this UpdateConsumerGroupRequest.
        :type body: :class:`huaweicloudsdkrocketmq.v2.UpdateConsumerGroup`
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
        if not isinstance(other, UpdateConsumerGroupRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
