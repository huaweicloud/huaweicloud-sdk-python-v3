# coding: utf-8

import pprint
import re

import six





class InitialDesired:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'service_id': 'str',
        'desired': 'object'
    }

    attribute_map = {
        'service_id': 'service_id',
        'desired': 'desired'
    }

    def __init__(self, service_id=None, desired=None):
        """InitialDesired - a model defined in huaweicloud sdk"""
        
        

        self._service_id = None
        self._desired = None
        self.discriminator = None

        self.service_id = service_id
        self.desired = desired

    @property
    def service_id(self):
        """Gets the service_id of this InitialDesired.

        设备的服务ID，在设备关联的产品模型中定义。

        :return: The service_id of this InitialDesired.
        :rtype: str
        """
        return self._service_id

    @service_id.setter
    def service_id(self, service_id):
        """Sets the service_id of this InitialDesired.

        设备的服务ID，在设备关联的产品模型中定义。

        :param service_id: The service_id of this InitialDesired.
        :type: str
        """
        self._service_id = service_id

    @property
    def desired(self):
        """Gets the desired of this InitialDesired.

        设备初始配置属性数据，Json格式，里面是一个个键值对，每个键都是产品模型中属性的参数名(property_name)，目前如样例所示只支持一层结构；这里设置的属性值与产品中对应属性的默认值比对，如果不同，则将以该字段中设置的属性值为准写入到设备影子中；如果想要删除整个desired可以填写空object(例如\"desired\":{})，如果想要删除某一个属性期望值可以将属性置位null(例如{\"temperature\":null})

        :return: The desired of this InitialDesired.
        :rtype: object
        """
        return self._desired

    @desired.setter
    def desired(self, desired):
        """Sets the desired of this InitialDesired.

        设备初始配置属性数据，Json格式，里面是一个个键值对，每个键都是产品模型中属性的参数名(property_name)，目前如样例所示只支持一层结构；这里设置的属性值与产品中对应属性的默认值比对，如果不同，则将以该字段中设置的属性值为准写入到设备影子中；如果想要删除整个desired可以填写空object(例如\"desired\":{})，如果想要删除某一个属性期望值可以将属性置位null(例如{\"temperature\":null})

        :param desired: The desired of this InitialDesired.
        :type: object
        """
        self._desired = desired

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
        if not isinstance(other, InitialDesired):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
