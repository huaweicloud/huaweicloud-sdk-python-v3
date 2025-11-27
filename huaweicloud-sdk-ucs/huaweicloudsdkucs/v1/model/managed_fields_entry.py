# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ManagedFieldsEntry:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'manager': 'str',
        'operation': 'str',
        'api_version': 'str',
        'time': 'str',
        'fields_type': 'str',
        'fields_v1': 'object'
    }

    attribute_map = {
        'manager': 'manager',
        'operation': 'operation',
        'api_version': 'apiVersion',
        'time': 'time',
        'fields_type': 'fieldsType',
        'fields_v1': 'fieldsV1'
    }

    def __init__(self, manager=None, operation=None, api_version=None, time=None, fields_type=None, fields_v1=None):
        r"""ManagedFieldsEntry

        The model defined in huaweicloud sdk

        :param manager: 管理者的名称
        :type manager: str
        :param operation: 记录导致此条目创建的操作类型，只能是 Apply 或 Update 两种操作类型
        :type operation: str
        :param api_version: 该管理者定义字段时所依据的资源 API 版本
        :type api_version: str
        :param time: 此管理条目被创建或最后一次更新的时间戳
        :type time: str
        :param fields_type: 固定为 \&quot;FieldsV1\&quot;，标记字段结构格式
        :type fields_type: str
        :param fields_v1: 用于存储实际被管理的字段信息
        :type fields_v1: object
        """
        
        

        self._manager = None
        self._operation = None
        self._api_version = None
        self._time = None
        self._fields_type = None
        self._fields_v1 = None
        self.discriminator = None

        if manager is not None:
            self.manager = manager
        if operation is not None:
            self.operation = operation
        if api_version is not None:
            self.api_version = api_version
        if time is not None:
            self.time = time
        if fields_type is not None:
            self.fields_type = fields_type
        if fields_v1 is not None:
            self.fields_v1 = fields_v1

    @property
    def manager(self):
        r"""Gets the manager of this ManagedFieldsEntry.

        管理者的名称

        :return: The manager of this ManagedFieldsEntry.
        :rtype: str
        """
        return self._manager

    @manager.setter
    def manager(self, manager):
        r"""Sets the manager of this ManagedFieldsEntry.

        管理者的名称

        :param manager: The manager of this ManagedFieldsEntry.
        :type manager: str
        """
        self._manager = manager

    @property
    def operation(self):
        r"""Gets the operation of this ManagedFieldsEntry.

        记录导致此条目创建的操作类型，只能是 Apply 或 Update 两种操作类型

        :return: The operation of this ManagedFieldsEntry.
        :rtype: str
        """
        return self._operation

    @operation.setter
    def operation(self, operation):
        r"""Sets the operation of this ManagedFieldsEntry.

        记录导致此条目创建的操作类型，只能是 Apply 或 Update 两种操作类型

        :param operation: The operation of this ManagedFieldsEntry.
        :type operation: str
        """
        self._operation = operation

    @property
    def api_version(self):
        r"""Gets the api_version of this ManagedFieldsEntry.

        该管理者定义字段时所依据的资源 API 版本

        :return: The api_version of this ManagedFieldsEntry.
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        r"""Sets the api_version of this ManagedFieldsEntry.

        该管理者定义字段时所依据的资源 API 版本

        :param api_version: The api_version of this ManagedFieldsEntry.
        :type api_version: str
        """
        self._api_version = api_version

    @property
    def time(self):
        r"""Gets the time of this ManagedFieldsEntry.

        此管理条目被创建或最后一次更新的时间戳

        :return: The time of this ManagedFieldsEntry.
        :rtype: str
        """
        return self._time

    @time.setter
    def time(self, time):
        r"""Sets the time of this ManagedFieldsEntry.

        此管理条目被创建或最后一次更新的时间戳

        :param time: The time of this ManagedFieldsEntry.
        :type time: str
        """
        self._time = time

    @property
    def fields_type(self):
        r"""Gets the fields_type of this ManagedFieldsEntry.

        固定为 \"FieldsV1\"，标记字段结构格式

        :return: The fields_type of this ManagedFieldsEntry.
        :rtype: str
        """
        return self._fields_type

    @fields_type.setter
    def fields_type(self, fields_type):
        r"""Sets the fields_type of this ManagedFieldsEntry.

        固定为 \"FieldsV1\"，标记字段结构格式

        :param fields_type: The fields_type of this ManagedFieldsEntry.
        :type fields_type: str
        """
        self._fields_type = fields_type

    @property
    def fields_v1(self):
        r"""Gets the fields_v1 of this ManagedFieldsEntry.

        用于存储实际被管理的字段信息

        :return: The fields_v1 of this ManagedFieldsEntry.
        :rtype: object
        """
        return self._fields_v1

    @fields_v1.setter
    def fields_v1(self, fields_v1):
        r"""Sets the fields_v1 of this ManagedFieldsEntry.

        用于存储实际被管理的字段信息

        :param fields_v1: The fields_v1 of this ManagedFieldsEntry.
        :type fields_v1: object
        """
        self._fields_v1 = fields_v1

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ManagedFieldsEntry):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
