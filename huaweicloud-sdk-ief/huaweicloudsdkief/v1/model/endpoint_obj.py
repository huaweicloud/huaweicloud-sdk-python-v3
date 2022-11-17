# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EndpointObj:

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
        'ief_instance_id': 'str',
        'name': 'str',
        'properties': 'dict(str, str)',
        'type': 'str'
    }

    attribute_map = {
        'description': 'description',
        'ief_instance_id': 'ief_instance_id',
        'name': 'name',
        'properties': 'properties',
        'type': 'type'
    }

    def __init__(self, description=None, ief_instance_id=None, name=None, properties=None, type=None):
        """EndpointObj

        The model defined in huaweicloud sdk

        :param description: 端点描述，最大长度255，不允许^~#$%&amp;*&lt;&gt;()[]{}&#39;\&quot;\\
        :type description: str
        :param ief_instance_id: 铂金版实例ID，如果为空则表示是专业版实例。
        :type ief_instance_id: str
        :param name: 端点名称，只允许中文字符、英文字符、数字、下划线、中划线，最大长度64 同一个帐号中创建的端点名唯一
        :type name: str
        :param properties: 端点的属性，端点需要对外展示的属性，示例： - dis: {\&quot;domain_id\&quot;:\&quot;user&#39;s domain id\&quot;} - servicebus: {\&quot;service_port\&quot;:8080} - apigw: {\&quot;domain_id\&quot;:\&quot;user&#39;s domain id\&quot;}
        :type properties: dict(str, str)
        :param type: 端点类型 枚举值： - dis - servicebus - apigw
        :type type: str
        """
        
        

        self._description = None
        self._ief_instance_id = None
        self._name = None
        self._properties = None
        self._type = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if ief_instance_id is not None:
            self.ief_instance_id = ief_instance_id
        self.name = name
        self.properties = properties
        self.type = type

    @property
    def description(self):
        """Gets the description of this EndpointObj.

        端点描述，最大长度255，不允许^~#$%&*<>()[]{}'\"\\

        :return: The description of this EndpointObj.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this EndpointObj.

        端点描述，最大长度255，不允许^~#$%&*<>()[]{}'\"\\

        :param description: The description of this EndpointObj.
        :type description: str
        """
        self._description = description

    @property
    def ief_instance_id(self):
        """Gets the ief_instance_id of this EndpointObj.

        铂金版实例ID，如果为空则表示是专业版实例。

        :return: The ief_instance_id of this EndpointObj.
        :rtype: str
        """
        return self._ief_instance_id

    @ief_instance_id.setter
    def ief_instance_id(self, ief_instance_id):
        """Sets the ief_instance_id of this EndpointObj.

        铂金版实例ID，如果为空则表示是专业版实例。

        :param ief_instance_id: The ief_instance_id of this EndpointObj.
        :type ief_instance_id: str
        """
        self._ief_instance_id = ief_instance_id

    @property
    def name(self):
        """Gets the name of this EndpointObj.

        端点名称，只允许中文字符、英文字符、数字、下划线、中划线，最大长度64 同一个帐号中创建的端点名唯一

        :return: The name of this EndpointObj.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EndpointObj.

        端点名称，只允许中文字符、英文字符、数字、下划线、中划线，最大长度64 同一个帐号中创建的端点名唯一

        :param name: The name of this EndpointObj.
        :type name: str
        """
        self._name = name

    @property
    def properties(self):
        """Gets the properties of this EndpointObj.

        端点的属性，端点需要对外展示的属性，示例： - dis: {\"domain_id\":\"user's domain id\"} - servicebus: {\"service_port\":8080} - apigw: {\"domain_id\":\"user's domain id\"}

        :return: The properties of this EndpointObj.
        :rtype: dict(str, str)
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this EndpointObj.

        端点的属性，端点需要对外展示的属性，示例： - dis: {\"domain_id\":\"user's domain id\"} - servicebus: {\"service_port\":8080} - apigw: {\"domain_id\":\"user's domain id\"}

        :param properties: The properties of this EndpointObj.
        :type properties: dict(str, str)
        """
        self._properties = properties

    @property
    def type(self):
        """Gets the type of this EndpointObj.

        端点类型 枚举值： - dis - servicebus - apigw

        :return: The type of this EndpointObj.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this EndpointObj.

        端点类型 枚举值： - dis - servicebus - apigw

        :param type: The type of this EndpointObj.
        :type type: str
        """
        self._type = type

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
        if not isinstance(other, EndpointObj):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
