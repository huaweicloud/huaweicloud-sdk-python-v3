# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateEndpointGroupOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'description': 'str',
        'traffic_dial_percentage': 'int'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'traffic_dial_percentage': 'traffic_dial_percentage'
    }

    def __init__(self, name=None, description=None, traffic_dial_percentage=None):
        """UpdateEndpointGroupOption

        The model defined in huaweicloud sdk

        :param name: 终端节点组名称，取值范围：1~64个字符之间，只能由数字、字母、中划线和中文组成。
        :type name: str
        :param description: 终端节点组描述信息，取值范围：0~255个字符之间，禁止输入字符：&lt;&gt;。
        :type description: str
        :param traffic_dial_percentage: 流量拨分到此组的百分比。
        :type traffic_dial_percentage: int
        """
        
        

        self._name = None
        self._description = None
        self._traffic_dial_percentage = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if traffic_dial_percentage is not None:
            self.traffic_dial_percentage = traffic_dial_percentage

    @property
    def name(self):
        """Gets the name of this UpdateEndpointGroupOption.

        终端节点组名称，取值范围：1~64个字符之间，只能由数字、字母、中划线和中文组成。

        :return: The name of this UpdateEndpointGroupOption.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateEndpointGroupOption.

        终端节点组名称，取值范围：1~64个字符之间，只能由数字、字母、中划线和中文组成。

        :param name: The name of this UpdateEndpointGroupOption.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this UpdateEndpointGroupOption.

        终端节点组描述信息，取值范围：0~255个字符之间，禁止输入字符：<>。

        :return: The description of this UpdateEndpointGroupOption.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateEndpointGroupOption.

        终端节点组描述信息，取值范围：0~255个字符之间，禁止输入字符：<>。

        :param description: The description of this UpdateEndpointGroupOption.
        :type description: str
        """
        self._description = description

    @property
    def traffic_dial_percentage(self):
        """Gets the traffic_dial_percentage of this UpdateEndpointGroupOption.

        流量拨分到此组的百分比。

        :return: The traffic_dial_percentage of this UpdateEndpointGroupOption.
        :rtype: int
        """
        return self._traffic_dial_percentage

    @traffic_dial_percentage.setter
    def traffic_dial_percentage(self, traffic_dial_percentage):
        """Sets the traffic_dial_percentage of this UpdateEndpointGroupOption.

        流量拨分到此组的百分比。

        :param traffic_dial_percentage: The traffic_dial_percentage of this UpdateEndpointGroupOption.
        :type traffic_dial_percentage: int
        """
        self._traffic_dial_percentage = traffic_dial_percentage

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
        if not isinstance(other, UpdateEndpointGroupOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
