# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateEdgeApplicationRequestDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'edge_app_id': 'str',
        'edge_app_name': 'str',
        'description': 'str',
        'function_type': 'str',
        'protocol': 'str'
    }

    attribute_map = {
        'edge_app_id': 'edge_app_id',
        'edge_app_name': 'edge_app_name',
        'description': 'description',
        'function_type': 'function_type',
        'protocol': 'protocol'
    }

    def __init__(self, edge_app_id=None, edge_app_name=None, description=None, function_type=None, protocol=None):
        """CreateEdgeApplicationRequestDTO

        The model defined in huaweicloud sdk

        :param edge_app_id: 应用ID
        :type edge_app_id: str
        :param edge_app_name: 应用名称
        :type edge_app_name: str
        :param description: 应用描述
        :type description: str
        :param function_type: 功能类型,分为数据处理（DATA_PROCESSING）、协议解析（PROTOCOL_PARSING）、IT集成（ON_PREMISE_INTEGRATION）和混合应用（COMPOSITE_APPLICATION），数据默认为DATA_PROCESSING，数据处理模块可以传输消息，协议解析为驱动类型，IT集成为部署南向3rdIA使用，混合应用可同时实现数据处理和协议解析。
        :type function_type: str
        :param protocol: 驱动协议类型OPCUA|Modbus-TCP
        :type protocol: str
        """
        
        

        self._edge_app_id = None
        self._edge_app_name = None
        self._description = None
        self._function_type = None
        self._protocol = None
        self.discriminator = None

        self.edge_app_id = edge_app_id
        if edge_app_name is not None:
            self.edge_app_name = edge_app_name
        if description is not None:
            self.description = description
        if function_type is not None:
            self.function_type = function_type
        if protocol is not None:
            self.protocol = protocol

    @property
    def edge_app_id(self):
        """Gets the edge_app_id of this CreateEdgeApplicationRequestDTO.

        应用ID

        :return: The edge_app_id of this CreateEdgeApplicationRequestDTO.
        :rtype: str
        """
        return self._edge_app_id

    @edge_app_id.setter
    def edge_app_id(self, edge_app_id):
        """Sets the edge_app_id of this CreateEdgeApplicationRequestDTO.

        应用ID

        :param edge_app_id: The edge_app_id of this CreateEdgeApplicationRequestDTO.
        :type edge_app_id: str
        """
        self._edge_app_id = edge_app_id

    @property
    def edge_app_name(self):
        """Gets the edge_app_name of this CreateEdgeApplicationRequestDTO.

        应用名称

        :return: The edge_app_name of this CreateEdgeApplicationRequestDTO.
        :rtype: str
        """
        return self._edge_app_name

    @edge_app_name.setter
    def edge_app_name(self, edge_app_name):
        """Sets the edge_app_name of this CreateEdgeApplicationRequestDTO.

        应用名称

        :param edge_app_name: The edge_app_name of this CreateEdgeApplicationRequestDTO.
        :type edge_app_name: str
        """
        self._edge_app_name = edge_app_name

    @property
    def description(self):
        """Gets the description of this CreateEdgeApplicationRequestDTO.

        应用描述

        :return: The description of this CreateEdgeApplicationRequestDTO.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateEdgeApplicationRequestDTO.

        应用描述

        :param description: The description of this CreateEdgeApplicationRequestDTO.
        :type description: str
        """
        self._description = description

    @property
    def function_type(self):
        """Gets the function_type of this CreateEdgeApplicationRequestDTO.

        功能类型,分为数据处理（DATA_PROCESSING）、协议解析（PROTOCOL_PARSING）、IT集成（ON_PREMISE_INTEGRATION）和混合应用（COMPOSITE_APPLICATION），数据默认为DATA_PROCESSING，数据处理模块可以传输消息，协议解析为驱动类型，IT集成为部署南向3rdIA使用，混合应用可同时实现数据处理和协议解析。

        :return: The function_type of this CreateEdgeApplicationRequestDTO.
        :rtype: str
        """
        return self._function_type

    @function_type.setter
    def function_type(self, function_type):
        """Sets the function_type of this CreateEdgeApplicationRequestDTO.

        功能类型,分为数据处理（DATA_PROCESSING）、协议解析（PROTOCOL_PARSING）、IT集成（ON_PREMISE_INTEGRATION）和混合应用（COMPOSITE_APPLICATION），数据默认为DATA_PROCESSING，数据处理模块可以传输消息，协议解析为驱动类型，IT集成为部署南向3rdIA使用，混合应用可同时实现数据处理和协议解析。

        :param function_type: The function_type of this CreateEdgeApplicationRequestDTO.
        :type function_type: str
        """
        self._function_type = function_type

    @property
    def protocol(self):
        """Gets the protocol of this CreateEdgeApplicationRequestDTO.

        驱动协议类型OPCUA|Modbus-TCP

        :return: The protocol of this CreateEdgeApplicationRequestDTO.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this CreateEdgeApplicationRequestDTO.

        驱动协议类型OPCUA|Modbus-TCP

        :param protocol: The protocol of this CreateEdgeApplicationRequestDTO.
        :type protocol: str
        """
        self._protocol = protocol

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
        if not isinstance(other, CreateEdgeApplicationRequestDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
