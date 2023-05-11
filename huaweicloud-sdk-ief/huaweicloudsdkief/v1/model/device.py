# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Device:

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
        'access_protocol': 'str',
        'description': 'str',
        'project_id': 'str',
        'created_at': 'str',
        'updated_at': 'str',
        'attributes': 'dict(str, ValueInAttributes)',
        'connection_type': 'str',
        'twin': 'dict(str, ValueInTwinResponse)',
        'access_config': 'AccessConfig',
        'property_visitors': 'dict(str, ValueInPropertyVisitors)'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'access_protocol': 'access_protocol',
        'description': 'description',
        'project_id': 'project_id',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'attributes': 'attributes',
        'connection_type': 'connection_type',
        'twin': 'twin',
        'access_config': 'access_config',
        'property_visitors': 'property_visitors'
    }

    def __init__(self, id=None, name=None, access_protocol=None, description=None, project_id=None, created_at=None, updated_at=None, attributes=None, connection_type=None, twin=None, access_config=None, property_visitors=None):
        """Device

        The model defined in huaweicloud sdk

        :param id: 终端设备ID，只允许英文字母、数字、下划线、中划线，必须以英文字母和数字开头，长度限制为24~64之间
        :type id: str
        :param name: 终端设备名称，只允许中文字符、英文字母、数字、下划线、中划线，长度限制为1~64
        :type name: str
        :param access_protocol: 访问协议，有如下选项： - userdefine：自定义协议 - modbus：modbus协议 - opc-ua：opc-ua协议 默认为userdefine
        :type access_protocol: str
        :param description: 终端设备描述，最大长度255，不允许^ ~ # $ % &amp; * &lt; &gt; ( ) [ ] { } &#39; \&quot; \\
        :type description: str
        :param project_id: 项目ID
        :type project_id: str
        :param created_at: 创建时间
        :type created_at: str
        :param updated_at: 更新时间
        :type updated_at: str
        :param attributes: 终端设备静态属性信息
        :type attributes: dict(str, ValueInAttributes)
        :param connection_type: 连接类型，默认为edge
        :type connection_type: str
        :param twin: 终端设备孪生属性信息
        :type twin: dict(str, ValueInTwinResponse)
        :param access_config: 
        :type access_config: :class:`huaweicloudsdkief.v1.AccessConfig`
        :param property_visitors: 孪生属性配置
        :type property_visitors: dict(str, ValueInPropertyVisitors)
        """
        
        

        self._id = None
        self._name = None
        self._access_protocol = None
        self._description = None
        self._project_id = None
        self._created_at = None
        self._updated_at = None
        self._attributes = None
        self._connection_type = None
        self._twin = None
        self._access_config = None
        self._property_visitors = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.access_protocol = access_protocol
        self.description = description
        self.project_id = project_id
        self.created_at = created_at
        self.updated_at = updated_at
        self.attributes = attributes
        self.connection_type = connection_type
        self.twin = twin
        self.access_config = access_config
        self.property_visitors = property_visitors

    @property
    def id(self):
        """Gets the id of this Device.

        终端设备ID，只允许英文字母、数字、下划线、中划线，必须以英文字母和数字开头，长度限制为24~64之间

        :return: The id of this Device.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Device.

        终端设备ID，只允许英文字母、数字、下划线、中划线，必须以英文字母和数字开头，长度限制为24~64之间

        :param id: The id of this Device.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this Device.

        终端设备名称，只允许中文字符、英文字母、数字、下划线、中划线，长度限制为1~64

        :return: The name of this Device.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Device.

        终端设备名称，只允许中文字符、英文字母、数字、下划线、中划线，长度限制为1~64

        :param name: The name of this Device.
        :type name: str
        """
        self._name = name

    @property
    def access_protocol(self):
        """Gets the access_protocol of this Device.

        访问协议，有如下选项： - userdefine：自定义协议 - modbus：modbus协议 - opc-ua：opc-ua协议 默认为userdefine

        :return: The access_protocol of this Device.
        :rtype: str
        """
        return self._access_protocol

    @access_protocol.setter
    def access_protocol(self, access_protocol):
        """Sets the access_protocol of this Device.

        访问协议，有如下选项： - userdefine：自定义协议 - modbus：modbus协议 - opc-ua：opc-ua协议 默认为userdefine

        :param access_protocol: The access_protocol of this Device.
        :type access_protocol: str
        """
        self._access_protocol = access_protocol

    @property
    def description(self):
        """Gets the description of this Device.

        终端设备描述，最大长度255，不允许^ ~ # $ % & * < > ( ) [ ] { } ' \" \\

        :return: The description of this Device.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Device.

        终端设备描述，最大长度255，不允许^ ~ # $ % & * < > ( ) [ ] { } ' \" \\

        :param description: The description of this Device.
        :type description: str
        """
        self._description = description

    @property
    def project_id(self):
        """Gets the project_id of this Device.

        项目ID

        :return: The project_id of this Device.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this Device.

        项目ID

        :param project_id: The project_id of this Device.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def created_at(self):
        """Gets the created_at of this Device.

        创建时间

        :return: The created_at of this Device.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Device.

        创建时间

        :param created_at: The created_at of this Device.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this Device.

        更新时间

        :return: The updated_at of this Device.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this Device.

        更新时间

        :param updated_at: The updated_at of this Device.
        :type updated_at: str
        """
        self._updated_at = updated_at

    @property
    def attributes(self):
        """Gets the attributes of this Device.

        终端设备静态属性信息

        :return: The attributes of this Device.
        :rtype: dict(str, ValueInAttributes)
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this Device.

        终端设备静态属性信息

        :param attributes: The attributes of this Device.
        :type attributes: dict(str, ValueInAttributes)
        """
        self._attributes = attributes

    @property
    def connection_type(self):
        """Gets the connection_type of this Device.

        连接类型，默认为edge

        :return: The connection_type of this Device.
        :rtype: str
        """
        return self._connection_type

    @connection_type.setter
    def connection_type(self, connection_type):
        """Sets the connection_type of this Device.

        连接类型，默认为edge

        :param connection_type: The connection_type of this Device.
        :type connection_type: str
        """
        self._connection_type = connection_type

    @property
    def twin(self):
        """Gets the twin of this Device.

        终端设备孪生属性信息

        :return: The twin of this Device.
        :rtype: dict(str, ValueInTwinResponse)
        """
        return self._twin

    @twin.setter
    def twin(self, twin):
        """Sets the twin of this Device.

        终端设备孪生属性信息

        :param twin: The twin of this Device.
        :type twin: dict(str, ValueInTwinResponse)
        """
        self._twin = twin

    @property
    def access_config(self):
        """Gets the access_config of this Device.

        :return: The access_config of this Device.
        :rtype: :class:`huaweicloudsdkief.v1.AccessConfig`
        """
        return self._access_config

    @access_config.setter
    def access_config(self, access_config):
        """Sets the access_config of this Device.

        :param access_config: The access_config of this Device.
        :type access_config: :class:`huaweicloudsdkief.v1.AccessConfig`
        """
        self._access_config = access_config

    @property
    def property_visitors(self):
        """Gets the property_visitors of this Device.

        孪生属性配置

        :return: The property_visitors of this Device.
        :rtype: dict(str, ValueInPropertyVisitors)
        """
        return self._property_visitors

    @property_visitors.setter
    def property_visitors(self, property_visitors):
        """Sets the property_visitors of this Device.

        孪生属性配置

        :param property_visitors: The property_visitors of this Device.
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
        if not isinstance(other, Device):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
