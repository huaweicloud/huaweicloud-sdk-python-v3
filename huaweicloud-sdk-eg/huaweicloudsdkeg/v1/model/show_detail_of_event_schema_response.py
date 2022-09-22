# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDetailOfEventSchemaResponse(SdkResponse):

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
        'data_sample': 'str',
        'version': 'int',
        'definition': 'str'
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
        'data_sample': 'data_sample',
        'version': 'version',
        'definition': 'definition'
    }

    def __init__(self, id=None, name=None, description=None, compatibility=None, provider_type=None, format=None, number_of_versions=None, created_time=None, updated_time=None, data_sample=None, version=None, definition=None):
        """ShowDetailOfEventSchemaResponse

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
        :param data_sample: 事件示例
        :type data_sample: str
        :param version: 事件模型当前版本号
        :type version: int
        :param definition: 事件模型内容定义
        :type definition: str
        """
        
        super(ShowDetailOfEventSchemaResponse, self).__init__()

        self._id = None
        self._name = None
        self._description = None
        self._compatibility = None
        self._provider_type = None
        self._format = None
        self._number_of_versions = None
        self._created_time = None
        self._updated_time = None
        self._data_sample = None
        self._version = None
        self._definition = None
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
        if data_sample is not None:
            self.data_sample = data_sample
        if version is not None:
            self.version = version
        if definition is not None:
            self.definition = definition

    @property
    def id(self):
        """Gets the id of this ShowDetailOfEventSchemaResponse.

        事件模型ID

        :return: The id of this ShowDetailOfEventSchemaResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ShowDetailOfEventSchemaResponse.

        事件模型ID

        :param id: The id of this ShowDetailOfEventSchemaResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ShowDetailOfEventSchemaResponse.

        事件模型名称，租户下唯一

        :return: The name of this ShowDetailOfEventSchemaResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ShowDetailOfEventSchemaResponse.

        事件模型名称，租户下唯一

        :param name: The name of this ShowDetailOfEventSchemaResponse.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this ShowDetailOfEventSchemaResponse.

        事件模型描述

        :return: The description of this ShowDetailOfEventSchemaResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ShowDetailOfEventSchemaResponse.

        事件模型描述

        :param description: The description of this ShowDetailOfEventSchemaResponse.
        :type description: str
        """
        self._description = description

    @property
    def compatibility(self):
        """Gets the compatibility of this ShowDetailOfEventSchemaResponse.

        事件模型兼容性

        :return: The compatibility of this ShowDetailOfEventSchemaResponse.
        :rtype: str
        """
        return self._compatibility

    @compatibility.setter
    def compatibility(self, compatibility):
        """Sets the compatibility of this ShowDetailOfEventSchemaResponse.

        事件模型兼容性

        :param compatibility: The compatibility of this ShowDetailOfEventSchemaResponse.
        :type compatibility: str
        """
        self._compatibility = compatibility

    @property
    def provider_type(self):
        """Gets the provider_type of this ShowDetailOfEventSchemaResponse.

        提供方类型，OFFICIAL：官方事件源；CUSTOM：自定义事件源

        :return: The provider_type of this ShowDetailOfEventSchemaResponse.
        :rtype: str
        """
        return self._provider_type

    @provider_type.setter
    def provider_type(self, provider_type):
        """Sets the provider_type of this ShowDetailOfEventSchemaResponse.

        提供方类型，OFFICIAL：官方事件源；CUSTOM：自定义事件源

        :param provider_type: The provider_type of this ShowDetailOfEventSchemaResponse.
        :type provider_type: str
        """
        self._provider_type = provider_type

    @property
    def format(self):
        """Gets the format of this ShowDetailOfEventSchemaResponse.

        事件模型格式

        :return: The format of this ShowDetailOfEventSchemaResponse.
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this ShowDetailOfEventSchemaResponse.

        事件模型格式

        :param format: The format of this ShowDetailOfEventSchemaResponse.
        :type format: str
        """
        self._format = format

    @property
    def number_of_versions(self):
        """Gets the number_of_versions of this ShowDetailOfEventSchemaResponse.

        事件模型版本数

        :return: The number_of_versions of this ShowDetailOfEventSchemaResponse.
        :rtype: int
        """
        return self._number_of_versions

    @number_of_versions.setter
    def number_of_versions(self, number_of_versions):
        """Sets the number_of_versions of this ShowDetailOfEventSchemaResponse.

        事件模型版本数

        :param number_of_versions: The number_of_versions of this ShowDetailOfEventSchemaResponse.
        :type number_of_versions: int
        """
        self._number_of_versions = number_of_versions

    @property
    def created_time(self):
        """Gets the created_time of this ShowDetailOfEventSchemaResponse.

        创建时间

        :return: The created_time of this ShowDetailOfEventSchemaResponse.
        :rtype: str
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this ShowDetailOfEventSchemaResponse.

        创建时间

        :param created_time: The created_time of this ShowDetailOfEventSchemaResponse.
        :type created_time: str
        """
        self._created_time = created_time

    @property
    def updated_time(self):
        """Gets the updated_time of this ShowDetailOfEventSchemaResponse.

        更新时间

        :return: The updated_time of this ShowDetailOfEventSchemaResponse.
        :rtype: str
        """
        return self._updated_time

    @updated_time.setter
    def updated_time(self, updated_time):
        """Sets the updated_time of this ShowDetailOfEventSchemaResponse.

        更新时间

        :param updated_time: The updated_time of this ShowDetailOfEventSchemaResponse.
        :type updated_time: str
        """
        self._updated_time = updated_time

    @property
    def data_sample(self):
        """Gets the data_sample of this ShowDetailOfEventSchemaResponse.

        事件示例

        :return: The data_sample of this ShowDetailOfEventSchemaResponse.
        :rtype: str
        """
        return self._data_sample

    @data_sample.setter
    def data_sample(self, data_sample):
        """Sets the data_sample of this ShowDetailOfEventSchemaResponse.

        事件示例

        :param data_sample: The data_sample of this ShowDetailOfEventSchemaResponse.
        :type data_sample: str
        """
        self._data_sample = data_sample

    @property
    def version(self):
        """Gets the version of this ShowDetailOfEventSchemaResponse.

        事件模型当前版本号

        :return: The version of this ShowDetailOfEventSchemaResponse.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ShowDetailOfEventSchemaResponse.

        事件模型当前版本号

        :param version: The version of this ShowDetailOfEventSchemaResponse.
        :type version: int
        """
        self._version = version

    @property
    def definition(self):
        """Gets the definition of this ShowDetailOfEventSchemaResponse.

        事件模型内容定义

        :return: The definition of this ShowDetailOfEventSchemaResponse.
        :rtype: str
        """
        return self._definition

    @definition.setter
    def definition(self, definition):
        """Sets the definition of this ShowDetailOfEventSchemaResponse.

        事件模型内容定义

        :param definition: The definition of this ShowDetailOfEventSchemaResponse.
        :type definition: str
        """
        self._definition = definition

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
        if not isinstance(other, ShowDetailOfEventSchemaResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
