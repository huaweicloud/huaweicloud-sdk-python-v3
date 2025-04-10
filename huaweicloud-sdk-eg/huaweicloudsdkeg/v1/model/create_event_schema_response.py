# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateEventSchemaResponse(SdkResponse):

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
        'compatibility': 'str',
        'provider_type': 'str',
        'format': 'str',
        'number_of_versions': 'int',
        'created_time': 'str',
        'updated_time': 'str',
        'version': 'int',
        'definition': 'str',
        'x_request_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'compatibility': 'compatibility',
        'provider_type': 'provider_type',
        'format': 'format',
        'number_of_versions': 'number_of_versions',
        'created_time': 'created_time',
        'updated_time': 'updated_time',
        'version': 'version',
        'definition': 'definition',
        'x_request_id': 'X-Request-Id'
    }

    def __init__(self, id=None, name=None, description=None, compatibility=None, provider_type=None, format=None, number_of_versions=None, created_time=None, updated_time=None, version=None, definition=None, x_request_id=None):
        r"""CreateEventSchemaResponse

        The model defined in huaweicloud sdk

        :param id: 事件模型ID
        :type id: str
        :param name: 事件模型名称，租户下唯一
        :type name: str
        :param description: 事件模型描述
        :type description: str
        :param compatibility: 事件模型兼容性
        :type compatibility: str
        :param provider_type: 提供方类型，OFFICIAL：官方事件源；CUSTOM：自定义事件源
        :type provider_type: str
        :param format: 事件模型格式
        :type format: str
        :param number_of_versions: 事件模型版本数
        :type number_of_versions: int
        :param created_time: 创建时间
        :type created_time: str
        :param updated_time: 更新时间
        :type updated_time: str
        :param version: 事件模型当前版本号
        :type version: int
        :param definition: 事件模型内容定义
        :type definition: str
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(CreateEventSchemaResponse, self).__init__()

        self._id = None
        self._name = None
        self._description = None
        self._compatibility = None
        self._provider_type = None
        self._format = None
        self._number_of_versions = None
        self._created_time = None
        self._updated_time = None
        self._version = None
        self._definition = None
        self._x_request_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if compatibility is not None:
            self.compatibility = compatibility
        if provider_type is not None:
            self.provider_type = provider_type
        if format is not None:
            self.format = format
        if number_of_versions is not None:
            self.number_of_versions = number_of_versions
        if created_time is not None:
            self.created_time = created_time
        if updated_time is not None:
            self.updated_time = updated_time
        if version is not None:
            self.version = version
        if definition is not None:
            self.definition = definition
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def id(self):
        r"""Gets the id of this CreateEventSchemaResponse.

        事件模型ID

        :return: The id of this CreateEventSchemaResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this CreateEventSchemaResponse.

        事件模型ID

        :param id: The id of this CreateEventSchemaResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this CreateEventSchemaResponse.

        事件模型名称，租户下唯一

        :return: The name of this CreateEventSchemaResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateEventSchemaResponse.

        事件模型名称，租户下唯一

        :param name: The name of this CreateEventSchemaResponse.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this CreateEventSchemaResponse.

        事件模型描述

        :return: The description of this CreateEventSchemaResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateEventSchemaResponse.

        事件模型描述

        :param description: The description of this CreateEventSchemaResponse.
        :type description: str
        """
        self._description = description

    @property
    def compatibility(self):
        r"""Gets the compatibility of this CreateEventSchemaResponse.

        事件模型兼容性

        :return: The compatibility of this CreateEventSchemaResponse.
        :rtype: str
        """
        return self._compatibility

    @compatibility.setter
    def compatibility(self, compatibility):
        r"""Sets the compatibility of this CreateEventSchemaResponse.

        事件模型兼容性

        :param compatibility: The compatibility of this CreateEventSchemaResponse.
        :type compatibility: str
        """
        self._compatibility = compatibility

    @property
    def provider_type(self):
        r"""Gets the provider_type of this CreateEventSchemaResponse.

        提供方类型，OFFICIAL：官方事件源；CUSTOM：自定义事件源

        :return: The provider_type of this CreateEventSchemaResponse.
        :rtype: str
        """
        return self._provider_type

    @provider_type.setter
    def provider_type(self, provider_type):
        r"""Sets the provider_type of this CreateEventSchemaResponse.

        提供方类型，OFFICIAL：官方事件源；CUSTOM：自定义事件源

        :param provider_type: The provider_type of this CreateEventSchemaResponse.
        :type provider_type: str
        """
        self._provider_type = provider_type

    @property
    def format(self):
        r"""Gets the format of this CreateEventSchemaResponse.

        事件模型格式

        :return: The format of this CreateEventSchemaResponse.
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        r"""Sets the format of this CreateEventSchemaResponse.

        事件模型格式

        :param format: The format of this CreateEventSchemaResponse.
        :type format: str
        """
        self._format = format

    @property
    def number_of_versions(self):
        r"""Gets the number_of_versions of this CreateEventSchemaResponse.

        事件模型版本数

        :return: The number_of_versions of this CreateEventSchemaResponse.
        :rtype: int
        """
        return self._number_of_versions

    @number_of_versions.setter
    def number_of_versions(self, number_of_versions):
        r"""Sets the number_of_versions of this CreateEventSchemaResponse.

        事件模型版本数

        :param number_of_versions: The number_of_versions of this CreateEventSchemaResponse.
        :type number_of_versions: int
        """
        self._number_of_versions = number_of_versions

    @property
    def created_time(self):
        r"""Gets the created_time of this CreateEventSchemaResponse.

        创建时间

        :return: The created_time of this CreateEventSchemaResponse.
        :rtype: str
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        r"""Sets the created_time of this CreateEventSchemaResponse.

        创建时间

        :param created_time: The created_time of this CreateEventSchemaResponse.
        :type created_time: str
        """
        self._created_time = created_time

    @property
    def updated_time(self):
        r"""Gets the updated_time of this CreateEventSchemaResponse.

        更新时间

        :return: The updated_time of this CreateEventSchemaResponse.
        :rtype: str
        """
        return self._updated_time

    @updated_time.setter
    def updated_time(self, updated_time):
        r"""Sets the updated_time of this CreateEventSchemaResponse.

        更新时间

        :param updated_time: The updated_time of this CreateEventSchemaResponse.
        :type updated_time: str
        """
        self._updated_time = updated_time

    @property
    def version(self):
        r"""Gets the version of this CreateEventSchemaResponse.

        事件模型当前版本号

        :return: The version of this CreateEventSchemaResponse.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this CreateEventSchemaResponse.

        事件模型当前版本号

        :param version: The version of this CreateEventSchemaResponse.
        :type version: int
        """
        self._version = version

    @property
    def definition(self):
        r"""Gets the definition of this CreateEventSchemaResponse.

        事件模型内容定义

        :return: The definition of this CreateEventSchemaResponse.
        :rtype: str
        """
        return self._definition

    @definition.setter
    def definition(self, definition):
        r"""Sets the definition of this CreateEventSchemaResponse.

        事件模型内容定义

        :param definition: The definition of this CreateEventSchemaResponse.
        :type definition: str
        """
        self._definition = definition

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this CreateEventSchemaResponse.

        :return: The x_request_id of this CreateEventSchemaResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this CreateEventSchemaResponse.

        :param x_request_id: The x_request_id of this CreateEventSchemaResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

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
        if not isinstance(other, CreateEventSchemaResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
