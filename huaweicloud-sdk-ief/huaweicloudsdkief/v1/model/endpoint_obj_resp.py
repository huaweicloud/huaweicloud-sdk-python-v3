# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EndpointObjResp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'created_at': 'str',
        'description': 'str',
        'id': 'str',
        'ief_instance_id': 'str',
        'is_shared': 'bool',
        'name': 'str',
        'project_id': 'str',
        'properties': 'dict(str, object)',
        'type': 'str',
        'updated_at': 'str'
    }

    attribute_map = {
        'created_at': 'created_at',
        'description': 'description',
        'id': 'id',
        'ief_instance_id': 'ief_instance_id',
        'is_shared': 'is_shared',
        'name': 'name',
        'project_id': 'project_id',
        'properties': 'properties',
        'type': 'type',
        'updated_at': 'updated_at'
    }

    def __init__(self, created_at=None, description=None, id=None, ief_instance_id=None, is_shared=None, name=None, project_id=None, properties=None, type=None, updated_at=None):
        """EndpointObjResp

        The model defined in huaweicloud sdk

        :param created_at: 创建时间
        :type created_at: str
        :param description: 端点描述，最大长度255，不允许^~#$%&amp;*&lt;&gt;()[]{}&#39;\&quot;\\
        :type description: str
        :param id: 端点ID
        :type id: str
        :param ief_instance_id: 铂金版实例ID，如果为空则表示是专业版实例。
        :type ief_instance_id: str
        :param is_shared: 是否共享
        :type is_shared: bool
        :param name: 端点名称，只允许中文字符、英文字符、数字、下划线、中划线，最大长度64 同一个帐号中创建的端点名唯一
        :type name: str
        :param project_id: 项目ID
        :type project_id: str
        :param properties: 端点的属性，端点需要对外展示的属性，示例： - dis: {\&quot;domain_id\&quot;:\&quot;user&#39;s domain id\&quot;} - servicebus: {\&quot;service_port\&quot;:8080} - apigw: {\&quot;domain_id\&quot;:\&quot;user&#39;s domain id\&quot;}
        :type properties: dict(str, object)
        :param type: 端点类型。枚举值： - dis - servicebus - apigw
        :type type: str
        :param updated_at: 更新时间
        :type updated_at: str
        """
        
        

        self._created_at = None
        self._description = None
        self._id = None
        self._ief_instance_id = None
        self._is_shared = None
        self._name = None
        self._project_id = None
        self._properties = None
        self._type = None
        self._updated_at = None
        self.discriminator = None

        self.created_at = created_at
        self.description = description
        self.id = id
        self.ief_instance_id = ief_instance_id
        self.is_shared = is_shared
        self.name = name
        self.project_id = project_id
        self.properties = properties
        self.type = type
        self.updated_at = updated_at

    @property
    def created_at(self):
        """Gets the created_at of this EndpointObjResp.

        创建时间

        :return: The created_at of this EndpointObjResp.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this EndpointObjResp.

        创建时间

        :param created_at: The created_at of this EndpointObjResp.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def description(self):
        """Gets the description of this EndpointObjResp.

        端点描述，最大长度255，不允许^~#$%&*<>()[]{}'\"\\

        :return: The description of this EndpointObjResp.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this EndpointObjResp.

        端点描述，最大长度255，不允许^~#$%&*<>()[]{}'\"\\

        :param description: The description of this EndpointObjResp.
        :type description: str
        """
        self._description = description

    @property
    def id(self):
        """Gets the id of this EndpointObjResp.

        端点ID

        :return: The id of this EndpointObjResp.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EndpointObjResp.

        端点ID

        :param id: The id of this EndpointObjResp.
        :type id: str
        """
        self._id = id

    @property
    def ief_instance_id(self):
        """Gets the ief_instance_id of this EndpointObjResp.

        铂金版实例ID，如果为空则表示是专业版实例。

        :return: The ief_instance_id of this EndpointObjResp.
        :rtype: str
        """
        return self._ief_instance_id

    @ief_instance_id.setter
    def ief_instance_id(self, ief_instance_id):
        """Sets the ief_instance_id of this EndpointObjResp.

        铂金版实例ID，如果为空则表示是专业版实例。

        :param ief_instance_id: The ief_instance_id of this EndpointObjResp.
        :type ief_instance_id: str
        """
        self._ief_instance_id = ief_instance_id

    @property
    def is_shared(self):
        """Gets the is_shared of this EndpointObjResp.

        是否共享

        :return: The is_shared of this EndpointObjResp.
        :rtype: bool
        """
        return self._is_shared

    @is_shared.setter
    def is_shared(self, is_shared):
        """Sets the is_shared of this EndpointObjResp.

        是否共享

        :param is_shared: The is_shared of this EndpointObjResp.
        :type is_shared: bool
        """
        self._is_shared = is_shared

    @property
    def name(self):
        """Gets the name of this EndpointObjResp.

        端点名称，只允许中文字符、英文字符、数字、下划线、中划线，最大长度64 同一个帐号中创建的端点名唯一

        :return: The name of this EndpointObjResp.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EndpointObjResp.

        端点名称，只允许中文字符、英文字符、数字、下划线、中划线，最大长度64 同一个帐号中创建的端点名唯一

        :param name: The name of this EndpointObjResp.
        :type name: str
        """
        self._name = name

    @property
    def project_id(self):
        """Gets the project_id of this EndpointObjResp.

        项目ID

        :return: The project_id of this EndpointObjResp.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this EndpointObjResp.

        项目ID

        :param project_id: The project_id of this EndpointObjResp.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def properties(self):
        """Gets the properties of this EndpointObjResp.

        端点的属性，端点需要对外展示的属性，示例： - dis: {\"domain_id\":\"user's domain id\"} - servicebus: {\"service_port\":8080} - apigw: {\"domain_id\":\"user's domain id\"}

        :return: The properties of this EndpointObjResp.
        :rtype: dict(str, object)
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this EndpointObjResp.

        端点的属性，端点需要对外展示的属性，示例： - dis: {\"domain_id\":\"user's domain id\"} - servicebus: {\"service_port\":8080} - apigw: {\"domain_id\":\"user's domain id\"}

        :param properties: The properties of this EndpointObjResp.
        :type properties: dict(str, object)
        """
        self._properties = properties

    @property
    def type(self):
        """Gets the type of this EndpointObjResp.

        端点类型。枚举值： - dis - servicebus - apigw

        :return: The type of this EndpointObjResp.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this EndpointObjResp.

        端点类型。枚举值： - dis - servicebus - apigw

        :param type: The type of this EndpointObjResp.
        :type type: str
        """
        self._type = type

    @property
    def updated_at(self):
        """Gets the updated_at of this EndpointObjResp.

        更新时间

        :return: The updated_at of this EndpointObjResp.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this EndpointObjResp.

        更新时间

        :param updated_at: The updated_at of this EndpointObjResp.
        :type updated_at: str
        """
        self._updated_at = updated_at

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
        if not isinstance(other, EndpointObjResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
