# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowConsumerListOrDetailsRequest:

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
        'topic': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'group': 'group',
        'topic': 'topic'
    }

    def __init__(self, instance_id=None, group=None, topic=None):
        """ShowConsumerListOrDetailsRequest

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID。
        :type instance_id: str
        :param group: 消费组名称。
        :type group: str
        :param topic: 待查询的topic，不指定时查询topic列表，指定时查询详情。
        :type topic: str
        """
        
        

        self._instance_id = None
        self._group = None
        self._topic = None
        self.discriminator = None

        self.instance_id = instance_id
        self.group = group
        if topic is not None:
            self.topic = topic

    @property
    def instance_id(self):
        """Gets the instance_id of this ShowConsumerListOrDetailsRequest.

        实例ID。

        :return: The instance_id of this ShowConsumerListOrDetailsRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ShowConsumerListOrDetailsRequest.

        实例ID。

        :param instance_id: The instance_id of this ShowConsumerListOrDetailsRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def group(self):
        """Gets the group of this ShowConsumerListOrDetailsRequest.

        消费组名称。

        :return: The group of this ShowConsumerListOrDetailsRequest.
        :rtype: str
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this ShowConsumerListOrDetailsRequest.

        消费组名称。

        :param group: The group of this ShowConsumerListOrDetailsRequest.
        :type group: str
        """
        self._group = group

    @property
    def topic(self):
        """Gets the topic of this ShowConsumerListOrDetailsRequest.

        待查询的topic，不指定时查询topic列表，指定时查询详情。

        :return: The topic of this ShowConsumerListOrDetailsRequest.
        :rtype: str
        """
        return self._topic

    @topic.setter
    def topic(self, topic):
        """Sets the topic of this ShowConsumerListOrDetailsRequest.

        待查询的topic，不指定时查询topic列表，指定时查询详情。

        :param topic: The topic of this ShowConsumerListOrDetailsRequest.
        :type topic: str
        """
        self._topic = topic

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
        if not isinstance(other, ShowConsumerListOrDetailsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
