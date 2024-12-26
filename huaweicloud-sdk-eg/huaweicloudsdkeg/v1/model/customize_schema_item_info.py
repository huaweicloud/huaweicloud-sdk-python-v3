# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CustomizeSchemaItemInfo:

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
        'event_type_id': 'str',
        'event_type_name': 'str',
        'event_source_id': 'str',
        'event_source_name': 'str',
        'event_source_label': 'str',
        'created_time': 'str',
        'updated_time': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'compatibility': 'compatibility',
        'provider_type': 'provider_type',
        'format': 'format',
        'number_of_versions': 'number_of_versions',
        'event_type_id': 'event_type_id',
        'event_type_name': 'event_type_name',
        'event_source_id': 'event_source_id',
        'event_source_name': 'event_source_name',
        'event_source_label': 'event_source_label',
        'created_time': 'created_time',
        'updated_time': 'updated_time'
    }

    def __init__(self, id=None, name=None, description=None, compatibility=None, provider_type=None, format=None, number_of_versions=None, event_type_id=None, event_type_name=None, event_source_id=None, event_source_name=None, event_source_label=None, created_time=None, updated_time=None):
        """CustomizeSchemaItemInfo

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
        :param event_type_id: 事件类型ID
        :type event_type_id: str
        :param event_type_name: 事件类型名称
        :type event_type_name: str
        :param event_source_id: 事件源ID
        :type event_source_id: str
        :param event_source_name: 事件源名称
        :type event_source_name: str
        :param event_source_label: 事件源标签
        :type event_source_label: str
        :param created_time: 创建时间
        :type created_time: str
        :param updated_time: 更新时间
        :type updated_time: str
        """
        
        

        self._id = None
        self._name = None
        self._description = None
        self._compatibility = None
        self._provider_type = None
        self._format = None
        self._number_of_versions = None
        self._event_type_id = None
        self._event_type_name = None
        self._event_source_id = None
        self._event_source_name = None
        self._event_source_label = None
        self._created_time = None
        self._updated_time = None
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
        if event_type_id is not None:
            self.event_type_id = event_type_id
        if event_type_name is not None:
            self.event_type_name = event_type_name
        if event_source_id is not None:
            self.event_source_id = event_source_id
        if event_source_name is not None:
            self.event_source_name = event_source_name
        if event_source_label is not None:
            self.event_source_label = event_source_label
        if created_time is not None:
            self.created_time = created_time
        if updated_time is not None:
            self.updated_time = updated_time

    @property
    def id(self):
        """Gets the id of this CustomizeSchemaItemInfo.

        事件模型ID

        :return: The id of this CustomizeSchemaItemInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CustomizeSchemaItemInfo.

        事件模型ID

        :param id: The id of this CustomizeSchemaItemInfo.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this CustomizeSchemaItemInfo.

        事件模型名称，租户下唯一

        :return: The name of this CustomizeSchemaItemInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CustomizeSchemaItemInfo.

        事件模型名称，租户下唯一

        :param name: The name of this CustomizeSchemaItemInfo.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this CustomizeSchemaItemInfo.

        事件模型描述

        :return: The description of this CustomizeSchemaItemInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CustomizeSchemaItemInfo.

        事件模型描述

        :param description: The description of this CustomizeSchemaItemInfo.
        :type description: str
        """
        self._description = description

    @property
    def compatibility(self):
        """Gets the compatibility of this CustomizeSchemaItemInfo.

        事件模型兼容性

        :return: The compatibility of this CustomizeSchemaItemInfo.
        :rtype: str
        """
        return self._compatibility

    @compatibility.setter
    def compatibility(self, compatibility):
        """Sets the compatibility of this CustomizeSchemaItemInfo.

        事件模型兼容性

        :param compatibility: The compatibility of this CustomizeSchemaItemInfo.
        :type compatibility: str
        """
        self._compatibility = compatibility

    @property
    def provider_type(self):
        """Gets the provider_type of this CustomizeSchemaItemInfo.

        提供方类型，OFFICIAL：官方事件源；CUSTOM：自定义事件源

        :return: The provider_type of this CustomizeSchemaItemInfo.
        :rtype: str
        """
        return self._provider_type

    @provider_type.setter
    def provider_type(self, provider_type):
        """Sets the provider_type of this CustomizeSchemaItemInfo.

        提供方类型，OFFICIAL：官方事件源；CUSTOM：自定义事件源

        :param provider_type: The provider_type of this CustomizeSchemaItemInfo.
        :type provider_type: str
        """
        self._provider_type = provider_type

    @property
    def format(self):
        """Gets the format of this CustomizeSchemaItemInfo.

        事件模型格式

        :return: The format of this CustomizeSchemaItemInfo.
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this CustomizeSchemaItemInfo.

        事件模型格式

        :param format: The format of this CustomizeSchemaItemInfo.
        :type format: str
        """
        self._format = format

    @property
    def number_of_versions(self):
        """Gets the number_of_versions of this CustomizeSchemaItemInfo.

        事件模型版本数

        :return: The number_of_versions of this CustomizeSchemaItemInfo.
        :rtype: int
        """
        return self._number_of_versions

    @number_of_versions.setter
    def number_of_versions(self, number_of_versions):
        """Sets the number_of_versions of this CustomizeSchemaItemInfo.

        事件模型版本数

        :param number_of_versions: The number_of_versions of this CustomizeSchemaItemInfo.
        :type number_of_versions: int
        """
        self._number_of_versions = number_of_versions

    @property
    def event_type_id(self):
        """Gets the event_type_id of this CustomizeSchemaItemInfo.

        事件类型ID

        :return: The event_type_id of this CustomizeSchemaItemInfo.
        :rtype: str
        """
        return self._event_type_id

    @event_type_id.setter
    def event_type_id(self, event_type_id):
        """Sets the event_type_id of this CustomizeSchemaItemInfo.

        事件类型ID

        :param event_type_id: The event_type_id of this CustomizeSchemaItemInfo.
        :type event_type_id: str
        """
        self._event_type_id = event_type_id

    @property
    def event_type_name(self):
        """Gets the event_type_name of this CustomizeSchemaItemInfo.

        事件类型名称

        :return: The event_type_name of this CustomizeSchemaItemInfo.
        :rtype: str
        """
        return self._event_type_name

    @event_type_name.setter
    def event_type_name(self, event_type_name):
        """Sets the event_type_name of this CustomizeSchemaItemInfo.

        事件类型名称

        :param event_type_name: The event_type_name of this CustomizeSchemaItemInfo.
        :type event_type_name: str
        """
        self._event_type_name = event_type_name

    @property
    def event_source_id(self):
        """Gets the event_source_id of this CustomizeSchemaItemInfo.

        事件源ID

        :return: The event_source_id of this CustomizeSchemaItemInfo.
        :rtype: str
        """
        return self._event_source_id

    @event_source_id.setter
    def event_source_id(self, event_source_id):
        """Sets the event_source_id of this CustomizeSchemaItemInfo.

        事件源ID

        :param event_source_id: The event_source_id of this CustomizeSchemaItemInfo.
        :type event_source_id: str
        """
        self._event_source_id = event_source_id

    @property
    def event_source_name(self):
        """Gets the event_source_name of this CustomizeSchemaItemInfo.

        事件源名称

        :return: The event_source_name of this CustomizeSchemaItemInfo.
        :rtype: str
        """
        return self._event_source_name

    @event_source_name.setter
    def event_source_name(self, event_source_name):
        """Sets the event_source_name of this CustomizeSchemaItemInfo.

        事件源名称

        :param event_source_name: The event_source_name of this CustomizeSchemaItemInfo.
        :type event_source_name: str
        """
        self._event_source_name = event_source_name

    @property
    def event_source_label(self):
        """Gets the event_source_label of this CustomizeSchemaItemInfo.

        事件源标签

        :return: The event_source_label of this CustomizeSchemaItemInfo.
        :rtype: str
        """
        return self._event_source_label

    @event_source_label.setter
    def event_source_label(self, event_source_label):
        """Sets the event_source_label of this CustomizeSchemaItemInfo.

        事件源标签

        :param event_source_label: The event_source_label of this CustomizeSchemaItemInfo.
        :type event_source_label: str
        """
        self._event_source_label = event_source_label

    @property
    def created_time(self):
        """Gets the created_time of this CustomizeSchemaItemInfo.

        创建时间

        :return: The created_time of this CustomizeSchemaItemInfo.
        :rtype: str
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this CustomizeSchemaItemInfo.

        创建时间

        :param created_time: The created_time of this CustomizeSchemaItemInfo.
        :type created_time: str
        """
        self._created_time = created_time

    @property
    def updated_time(self):
        """Gets the updated_time of this CustomizeSchemaItemInfo.

        更新时间

        :return: The updated_time of this CustomizeSchemaItemInfo.
        :rtype: str
        """
        return self._updated_time

    @updated_time.setter
    def updated_time(self, updated_time):
        """Sets the updated_time of this CustomizeSchemaItemInfo.

        更新时间

        :param updated_time: The updated_time of this CustomizeSchemaItemInfo.
        :type updated_time: str
        """
        self._updated_time = updated_time

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
        if not isinstance(other, CustomizeSchemaItemInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
