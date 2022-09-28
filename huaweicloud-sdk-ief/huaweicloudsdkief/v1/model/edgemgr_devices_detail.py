# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EdgemgrDevicesDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'description': 'str',
        'attributes': 'dict(str, ValueInAttributes)',
        'connection_type': 'str',
        'access_protocol': 'str',
        'twin': 'dict(str, ValueInTwin)',
        'access_config': 'AccessConfig',
        'property_visitors': 'dict(str, ValueInPropertyVisitors)'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'attributes': 'attributes',
        'connection_type': 'connection_type',
        'access_protocol': 'access_protocol',
        'twin': 'twin',
        'access_config': 'access_config',
        'property_visitors': 'property_visitors'
    }

    def __init__(self, id=None, name=None, description=None, attributes=None, connection_type=None, access_protocol=None, twin=None, access_config=None, property_visitors=None):
        """EdgemgrDevicesDetail

        The model defined in huaweicloud sdk

        :param id: 终端设备ID，只允许英文字母、数字、下划线、中划线，必须以英文字母和数字开头，长度限制为24~64之间
        :type id: str
        :param name: 终端设备名称，只允许中文字符、英文字母、数字、下划线、中划线，长度限制为1~64
        :type name: str
        :param description: 终端设备描述，最大长度255，不允许^ ~ # $ % &amp; * &lt; &gt; ( ) [ ] { } &#39; \&quot; \\
        :type description: str
        :param attributes: 终端设备静态属性
        :type attributes: dict(str, ValueInAttributes)
        :param connection_type: 连接类型，默认为edge
        :type connection_type: str
        :param access_protocol: 访问协议，有如下选项： - userdefine：自定义协议 - modbus：modbus协议 - opc-ua：opc-ua协议 默认为userdefine
        :type access_protocol: str
        :param twin: 终端设备动态属性
        :type twin: dict(str, ValueInTwin)
        :param access_config: 
        :type access_config: :class:`huaweicloudsdkief.v1.AccessConfig`
        :param property_visitors: 孪生属性配置
        :type property_visitors: dict(str, ValueInPropertyVisitors)
        """
        
        

        self._id = None
        self._name = None
        self._description = None
        self._attributes = None
        self._connection_type = None
        self._access_protocol = None
        self._twin = None
        self._access_config = None
        self._property_visitors = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.name = name
        if description is not None:
            self.description = description
        if attributes is not None:
            self.attributes = attributes
        if connection_type is not None:
            self.connection_type = connection_type
        if access_protocol is not None:
            self.access_protocol = access_protocol
        if twin is not None:
            self.twin = twin
        if access_config is not None:
            self.access_config = access_config
        if property_visitors is not None:
            self.property_visitors = property_visitors

    @property
    def id(self):
        """Gets the id of this EdgemgrDevicesDetail.

        终端设备ID，只允许英文字母、数字、下划线、中划线，必须以英文字母和数字开头，长度限制为24~64之间

        :return: The id of this EdgemgrDevicesDetail.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EdgemgrDevicesDetail.

        终端设备ID，只允许英文字母、数字、下划线、中划线，必须以英文字母和数字开头，长度限制为24~64之间

        :param id: The id of this EdgemgrDevicesDetail.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this EdgemgrDevicesDetail.

        终端设备名称，只允许中文字符、英文字母、数字、下划线、中划线，长度限制为1~64

        :return: The name of this EdgemgrDevicesDetail.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EdgemgrDevicesDetail.

        终端设备名称，只允许中文字符、英文字母、数字、下划线、中划线，长度限制为1~64

        :param name: The name of this EdgemgrDevicesDetail.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this EdgemgrDevicesDetail.

        终端设备描述，最大长度255，不允许^ ~ # $ % & * < > ( ) [ ] { } ' \" \\

        :return: The description of this EdgemgrDevicesDetail.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this EdgemgrDevicesDetail.

        终端设备描述，最大长度255，不允许^ ~ # $ % & * < > ( ) [ ] { } ' \" \\

        :param description: The description of this EdgemgrDevicesDetail.
        :type description: str
        """
        self._description = description

    @property
    def attributes(self):
        """Gets the attributes of this EdgemgrDevicesDetail.

        终端设备静态属性

        :return: The attributes of this EdgemgrDevicesDetail.
        :rtype: dict(str, ValueInAttributes)
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this EdgemgrDevicesDetail.

        终端设备静态属性

        :param attributes: The attributes of this EdgemgrDevicesDetail.
        :type attributes: dict(str, ValueInAttributes)
        """
        self._attributes = attributes

    @property
    def connection_type(self):
        """Gets the connection_type of this EdgemgrDevicesDetail.

        连接类型，默认为edge

        :return: The connection_type of this EdgemgrDevicesDetail.
        :rtype: str
        """
        return self._connection_type

    @connection_type.setter
    def connection_type(self, connection_type):
        """Sets the connection_type of this EdgemgrDevicesDetail.

        连接类型，默认为edge

        :param connection_type: The connection_type of this EdgemgrDevicesDetail.
        :type connection_type: str
        """
        self._connection_type = connection_type

    @property
    def access_protocol(self):
        """Gets the access_protocol of this EdgemgrDevicesDetail.

        访问协议，有如下选项： - userdefine：自定义协议 - modbus：modbus协议 - opc-ua：opc-ua协议 默认为userdefine

        :return: The access_protocol of this EdgemgrDevicesDetail.
        :rtype: str
        """
        return self._access_protocol

    @access_protocol.setter
    def access_protocol(self, access_protocol):
        """Sets the access_protocol of this EdgemgrDevicesDetail.

        访问协议，有如下选项： - userdefine：自定义协议 - modbus：modbus协议 - opc-ua：opc-ua协议 默认为userdefine

        :param access_protocol: The access_protocol of this EdgemgrDevicesDetail.
        :type access_protocol: str
        """
        self._access_protocol = access_protocol

    @property
    def twin(self):
        """Gets the twin of this EdgemgrDevicesDetail.

        终端设备动态属性

        :return: The twin of this EdgemgrDevicesDetail.
        :rtype: dict(str, ValueInTwin)
        """
        return self._twin

    @twin.setter
    def twin(self, twin):
        """Sets the twin of this EdgemgrDevicesDetail.

        终端设备动态属性

        :param twin: The twin of this EdgemgrDevicesDetail.
        :type twin: dict(str, ValueInTwin)
        """
        self._twin = twin

    @property
    def access_config(self):
        """Gets the access_config of this EdgemgrDevicesDetail.


        :return: The access_config of this EdgemgrDevicesDetail.
        :rtype: :class:`huaweicloudsdkief.v1.AccessConfig`
        """
        return self._access_config

    @access_config.setter
    def access_config(self, access_config):
        """Sets the access_config of this EdgemgrDevicesDetail.


        :param access_config: The access_config of this EdgemgrDevicesDetail.
        :type access_config: :class:`huaweicloudsdkief.v1.AccessConfig`
        """
        self._access_config = access_config

    @property
    def property_visitors(self):
        """Gets the property_visitors of this EdgemgrDevicesDetail.

        孪生属性配置

        :return: The property_visitors of this EdgemgrDevicesDetail.
        :rtype: dict(str, ValueInPropertyVisitors)
        """
        return self._property_visitors

    @property_visitors.setter
    def property_visitors(self, property_visitors):
        """Sets the property_visitors of this EdgemgrDevicesDetail.

        孪生属性配置

        :param property_visitors: The property_visitors of this EdgemgrDevicesDetail.
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
        if not isinstance(other, EdgemgrDevicesDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
