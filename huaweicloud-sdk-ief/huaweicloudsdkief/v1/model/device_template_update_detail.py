# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeviceTemplateUpdateDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'description': 'str',
        'attributes': 'dict(str, ValueInAttributes)',
        'twin': 'dict(str, ValueInTwin)',
        'tags': 'DeviceTemplateUpdateDetailTags',
        'access_protocol': 'str',
        'property_visitors': 'dict(str, ValueInPropertyVisitors)'
    }

    attribute_map = {
        'description': 'description',
        'attributes': 'attributes',
        'twin': 'twin',
        'tags': 'tags',
        'access_protocol': 'access_protocol',
        'property_visitors': 'property_visitors'
    }

    def __init__(self, description=None, attributes=None, twin=None, tags=None, access_protocol=None, property_visitors=None):
        """DeviceTemplateUpdateDetail

        The model defined in huaweicloud sdk

        :param description: 设备模板描述，最大长度255
        :type description: str
        :param attributes: 终端设备静态属性，最多64个键值。
        :type attributes: dict(str, ValueInAttributes)
        :param twin: 终端设备动态属性
        :type twin: dict(str, ValueInTwin)
        :param tags: 
        :type tags: :class:`huaweicloudsdkief.v1.DeviceTemplateUpdateDetailTags`
        :param access_protocol: - userdefine：自定义协议 - modbus：modbus协议 - opc-ua：opc-ua协议
        :type access_protocol: str
        :param property_visitors: 孪生属性配置，与access_protocol关联。
        :type property_visitors: dict(str, ValueInPropertyVisitors)
        """
        
        

        self._description = None
        self._attributes = None
        self._twin = None
        self._tags = None
        self._access_protocol = None
        self._property_visitors = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if attributes is not None:
            self.attributes = attributes
        if twin is not None:
            self.twin = twin
        if tags is not None:
            self.tags = tags
        if access_protocol is not None:
            self.access_protocol = access_protocol
        if property_visitors is not None:
            self.property_visitors = property_visitors

    @property
    def description(self):
        """Gets the description of this DeviceTemplateUpdateDetail.

        设备模板描述，最大长度255

        :return: The description of this DeviceTemplateUpdateDetail.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this DeviceTemplateUpdateDetail.

        设备模板描述，最大长度255

        :param description: The description of this DeviceTemplateUpdateDetail.
        :type description: str
        """
        self._description = description

    @property
    def attributes(self):
        """Gets the attributes of this DeviceTemplateUpdateDetail.

        终端设备静态属性，最多64个键值。

        :return: The attributes of this DeviceTemplateUpdateDetail.
        :rtype: dict(str, ValueInAttributes)
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this DeviceTemplateUpdateDetail.

        终端设备静态属性，最多64个键值。

        :param attributes: The attributes of this DeviceTemplateUpdateDetail.
        :type attributes: dict(str, ValueInAttributes)
        """
        self._attributes = attributes

    @property
    def twin(self):
        """Gets the twin of this DeviceTemplateUpdateDetail.

        终端设备动态属性

        :return: The twin of this DeviceTemplateUpdateDetail.
        :rtype: dict(str, ValueInTwin)
        """
        return self._twin

    @twin.setter
    def twin(self, twin):
        """Sets the twin of this DeviceTemplateUpdateDetail.

        终端设备动态属性

        :param twin: The twin of this DeviceTemplateUpdateDetail.
        :type twin: dict(str, ValueInTwin)
        """
        self._twin = twin

    @property
    def tags(self):
        """Gets the tags of this DeviceTemplateUpdateDetail.

        :return: The tags of this DeviceTemplateUpdateDetail.
        :rtype: :class:`huaweicloudsdkief.v1.DeviceTemplateUpdateDetailTags`
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this DeviceTemplateUpdateDetail.

        :param tags: The tags of this DeviceTemplateUpdateDetail.
        :type tags: :class:`huaweicloudsdkief.v1.DeviceTemplateUpdateDetailTags`
        """
        self._tags = tags

    @property
    def access_protocol(self):
        """Gets the access_protocol of this DeviceTemplateUpdateDetail.

        - userdefine：自定义协议 - modbus：modbus协议 - opc-ua：opc-ua协议

        :return: The access_protocol of this DeviceTemplateUpdateDetail.
        :rtype: str
        """
        return self._access_protocol

    @access_protocol.setter
    def access_protocol(self, access_protocol):
        """Sets the access_protocol of this DeviceTemplateUpdateDetail.

        - userdefine：自定义协议 - modbus：modbus协议 - opc-ua：opc-ua协议

        :param access_protocol: The access_protocol of this DeviceTemplateUpdateDetail.
        :type access_protocol: str
        """
        self._access_protocol = access_protocol

    @property
    def property_visitors(self):
        """Gets the property_visitors of this DeviceTemplateUpdateDetail.

        孪生属性配置，与access_protocol关联。

        :return: The property_visitors of this DeviceTemplateUpdateDetail.
        :rtype: dict(str, ValueInPropertyVisitors)
        """
        return self._property_visitors

    @property_visitors.setter
    def property_visitors(self, property_visitors):
        """Sets the property_visitors of this DeviceTemplateUpdateDetail.

        孪生属性配置，与access_protocol关联。

        :param property_visitors: The property_visitors of this DeviceTemplateUpdateDetail.
        :type property_visitors: dict(str, ValueInPropertyVisitors)
        """
        self._property_visitors = property_visitors

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
        if not isinstance(other, DeviceTemplateUpdateDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
