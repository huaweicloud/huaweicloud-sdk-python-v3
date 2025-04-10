# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateEndpointGroupOption:

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
        'traffic_dial_percentage': 'int',
        'region_id': 'str',
        'listeners': 'list[Id]'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'traffic_dial_percentage': 'traffic_dial_percentage',
        'region_id': 'region_id',
        'listeners': 'listeners'
    }

    def __init__(self, name=None, description=None, traffic_dial_percentage=None, region_id=None, listeners=None):
        r"""CreateEndpointGroupOption

        The model defined in huaweicloud sdk

        :param name: 终端节点组名称，取值范围：1~64个字符之间，只能由数字、字母、中划线和中文组成。
        :type name: str
        :param description: 终端节点组描述信息，取值范围：0~255个字符之间，禁止输入字符：&lt;&gt;。
        :type description: str
        :param traffic_dial_percentage: 流量拨分到此组的百分比。
        :type traffic_dial_percentage: int
        :param region_id: 终端节点组所属区域ID。
        :type region_id: str
        :param listeners: 关联监听器列表。一个终端节点组下仅支持关联一个监听器。
        :type listeners: list[:class:`huaweicloudsdkga.v1.Id`]
        """
        
        

        self._name = None
        self._description = None
        self._traffic_dial_percentage = None
        self._region_id = None
        self._listeners = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        if traffic_dial_percentage is not None:
            self.traffic_dial_percentage = traffic_dial_percentage
        self.region_id = region_id
        self.listeners = listeners

    @property
    def name(self):
        r"""Gets the name of this CreateEndpointGroupOption.

        终端节点组名称，取值范围：1~64个字符之间，只能由数字、字母、中划线和中文组成。

        :return: The name of this CreateEndpointGroupOption.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateEndpointGroupOption.

        终端节点组名称，取值范围：1~64个字符之间，只能由数字、字母、中划线和中文组成。

        :param name: The name of this CreateEndpointGroupOption.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this CreateEndpointGroupOption.

        终端节点组描述信息，取值范围：0~255个字符之间，禁止输入字符：<>。

        :return: The description of this CreateEndpointGroupOption.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateEndpointGroupOption.

        终端节点组描述信息，取值范围：0~255个字符之间，禁止输入字符：<>。

        :param description: The description of this CreateEndpointGroupOption.
        :type description: str
        """
        self._description = description

    @property
    def traffic_dial_percentage(self):
        r"""Gets the traffic_dial_percentage of this CreateEndpointGroupOption.

        流量拨分到此组的百分比。

        :return: The traffic_dial_percentage of this CreateEndpointGroupOption.
        :rtype: int
        """
        return self._traffic_dial_percentage

    @traffic_dial_percentage.setter
    def traffic_dial_percentage(self, traffic_dial_percentage):
        r"""Sets the traffic_dial_percentage of this CreateEndpointGroupOption.

        流量拨分到此组的百分比。

        :param traffic_dial_percentage: The traffic_dial_percentage of this CreateEndpointGroupOption.
        :type traffic_dial_percentage: int
        """
        self._traffic_dial_percentage = traffic_dial_percentage

    @property
    def region_id(self):
        r"""Gets the region_id of this CreateEndpointGroupOption.

        终端节点组所属区域ID。

        :return: The region_id of this CreateEndpointGroupOption.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        r"""Sets the region_id of this CreateEndpointGroupOption.

        终端节点组所属区域ID。

        :param region_id: The region_id of this CreateEndpointGroupOption.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def listeners(self):
        r"""Gets the listeners of this CreateEndpointGroupOption.

        关联监听器列表。一个终端节点组下仅支持关联一个监听器。

        :return: The listeners of this CreateEndpointGroupOption.
        :rtype: list[:class:`huaweicloudsdkga.v1.Id`]
        """
        return self._listeners

    @listeners.setter
    def listeners(self, listeners):
        r"""Sets the listeners of this CreateEndpointGroupOption.

        关联监听器列表。一个终端节点组下仅支持关联一个监听器。

        :param listeners: The listeners of this CreateEndpointGroupOption.
        :type listeners: list[:class:`huaweicloudsdkga.v1.Id`]
        """
        self._listeners = listeners

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
        if not isinstance(other, CreateEndpointGroupOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
