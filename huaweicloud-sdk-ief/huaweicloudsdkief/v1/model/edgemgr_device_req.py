# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EdgemgrDeviceReq:

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
        'access_protocol': 'str',
        'description': 'str',
        'attributes': 'dict(str, ValueInAttributes)',
        'twin': 'dict(str, ValueInTwin)',
        'tags': 'ResourceTag',
        'property_visitors': 'dict(str, ValueInPropertyVisitors)'
    }

    attribute_map = {
        'name': 'name',
        'access_protocol': 'access_protocol',
        'description': 'description',
        'attributes': 'attributes',
        'twin': 'twin',
        'tags': 'tags',
        'property_visitors': 'property_visitors'
    }

    def __init__(self, name=None, access_protocol=None, description=None, attributes=None, twin=None, tags=None, property_visitors=None):
        r"""EdgemgrDeviceReq

        The model defined in huaweicloud sdk

        :param name: 终端设备名称，只允许中文字符、英文字母、数字、下划线、中划线，长度限制为1~64
        :type name: str
        :param access_protocol: 访问协议，有如下选项： - userdefine：自定义协议 - modbus：modbus协议 - opc-ua：opc-ua协议 默认为userdefine
        :type access_protocol: str
        :param description: 终端设备描述，最大长度255，不允许^ ~ # $ % &amp; * &lt; &gt; ( ) [ ] { } &#39; \&quot; \\
        :type description: str
        :param attributes: 静态属性
        :type attributes: dict(str, ValueInAttributes)
        :param twin: 终端设备动态属性
        :type twin: dict(str, ValueInTwin)
        :param tags: 
        :type tags: :class:`huaweicloudsdkief.v1.ResourceTag`
        :param property_visitors: 孪生属性配置
        :type property_visitors: dict(str, ValueInPropertyVisitors)
        """
        
        

        self._name = None
        self._access_protocol = None
        self._description = None
        self._attributes = None
        self._twin = None
        self._tags = None
        self._property_visitors = None
        self.discriminator = None

        self.name = name
        if access_protocol is not None:
            self.access_protocol = access_protocol
        if description is not None:
            self.description = description
        if attributes is not None:
            self.attributes = attributes
        if twin is not None:
            self.twin = twin
        if tags is not None:
            self.tags = tags
        if property_visitors is not None:
            self.property_visitors = property_visitors

    @property
    def name(self):
        r"""Gets the name of this EdgemgrDeviceReq.

        终端设备名称，只允许中文字符、英文字母、数字、下划线、中划线，长度限制为1~64

        :return: The name of this EdgemgrDeviceReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this EdgemgrDeviceReq.

        终端设备名称，只允许中文字符、英文字母、数字、下划线、中划线，长度限制为1~64

        :param name: The name of this EdgemgrDeviceReq.
        :type name: str
        """
        self._name = name

    @property
    def access_protocol(self):
        r"""Gets the access_protocol of this EdgemgrDeviceReq.

        访问协议，有如下选项： - userdefine：自定义协议 - modbus：modbus协议 - opc-ua：opc-ua协议 默认为userdefine

        :return: The access_protocol of this EdgemgrDeviceReq.
        :rtype: str
        """
        return self._access_protocol

    @access_protocol.setter
    def access_protocol(self, access_protocol):
        r"""Sets the access_protocol of this EdgemgrDeviceReq.

        访问协议，有如下选项： - userdefine：自定义协议 - modbus：modbus协议 - opc-ua：opc-ua协议 默认为userdefine

        :param access_protocol: The access_protocol of this EdgemgrDeviceReq.
        :type access_protocol: str
        """
        self._access_protocol = access_protocol

    @property
    def description(self):
        r"""Gets the description of this EdgemgrDeviceReq.

        终端设备描述，最大长度255，不允许^ ~ # $ % & * < > ( ) [ ] { } ' \" \\

        :return: The description of this EdgemgrDeviceReq.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this EdgemgrDeviceReq.

        终端设备描述，最大长度255，不允许^ ~ # $ % & * < > ( ) [ ] { } ' \" \\

        :param description: The description of this EdgemgrDeviceReq.
        :type description: str
        """
        self._description = description

    @property
    def attributes(self):
        r"""Gets the attributes of this EdgemgrDeviceReq.

        静态属性

        :return: The attributes of this EdgemgrDeviceReq.
        :rtype: dict(str, ValueInAttributes)
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        r"""Sets the attributes of this EdgemgrDeviceReq.

        静态属性

        :param attributes: The attributes of this EdgemgrDeviceReq.
        :type attributes: dict(str, ValueInAttributes)
        """
        self._attributes = attributes

    @property
    def twin(self):
        r"""Gets the twin of this EdgemgrDeviceReq.

        终端设备动态属性

        :return: The twin of this EdgemgrDeviceReq.
        :rtype: dict(str, ValueInTwin)
        """
        return self._twin

    @twin.setter
    def twin(self, twin):
        r"""Sets the twin of this EdgemgrDeviceReq.

        终端设备动态属性

        :param twin: The twin of this EdgemgrDeviceReq.
        :type twin: dict(str, ValueInTwin)
        """
        self._twin = twin

    @property
    def tags(self):
        r"""Gets the tags of this EdgemgrDeviceReq.

        :return: The tags of this EdgemgrDeviceReq.
        :rtype: :class:`huaweicloudsdkief.v1.ResourceTag`
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this EdgemgrDeviceReq.

        :param tags: The tags of this EdgemgrDeviceReq.
        :type tags: :class:`huaweicloudsdkief.v1.ResourceTag`
        """
        self._tags = tags

    @property
    def property_visitors(self):
        r"""Gets the property_visitors of this EdgemgrDeviceReq.

        孪生属性配置

        :return: The property_visitors of this EdgemgrDeviceReq.
        :rtype: dict(str, ValueInPropertyVisitors)
        """
        return self._property_visitors

    @property_visitors.setter
    def property_visitors(self, property_visitors):
        r"""Sets the property_visitors of this EdgemgrDeviceReq.

        孪生属性配置

        :param property_visitors: The property_visitors of this EdgemgrDeviceReq.
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
        if not isinstance(other, EdgemgrDeviceReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
