# coding: utf-8

import pprint
import re

import six





class DeviceMessageCondition:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'product_id': 'str',
        'topic': 'str'
    }

    attribute_map = {
        'product_id': 'product_id',
        'topic': 'topic'
    }

    def __init__(self, product_id=None, topic=None):
        """DeviceMessageCondition - a model defined in huaweicloud sdk"""
        
        

        self._product_id = None
        self._topic = None
        self.discriminator = None

        if product_id is not None:
            self.product_id = product_id
        if topic is not None:
            self.topic = topic

    @property
    def product_id(self):
        """Gets the product_id of this DeviceMessageCondition.

        设备关联的产品ID，用于唯一标识一个产品模型，在管理门户导入产品模型后由平台分配获得。

        :return: The product_id of this DeviceMessageCondition.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """Sets the product_id of this DeviceMessageCondition.

        设备关联的产品ID，用于唯一标识一个产品模型，在管理门户导入产品模型后由平台分配获得。

        :param product_id: The product_id of this DeviceMessageCondition.
        :type: str
        """
        self._product_id = product_id

    @property
    def topic(self):
        """Gets the topic of this DeviceMessageCondition.

        产品关联的topic信息，用于过滤消息中指定topic消息。

        :return: The topic of this DeviceMessageCondition.
        :rtype: str
        """
        return self._topic

    @topic.setter
    def topic(self, topic):
        """Sets the topic of this DeviceMessageCondition.

        产品关联的topic信息，用于过滤消息中指定topic消息。

        :param topic: The topic of this DeviceMessageCondition.
        :type: str
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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DeviceMessageCondition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
