# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TaskExtParam:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'delete': 'bool',
        'id': 'str',
        'name': 'str',
        'sensitive_info': 'bool',
        'value': 'str',
        'variable_type': 'str'
    }

    attribute_map = {
        'delete': 'delete',
        'id': 'id',
        'name': 'name',
        'sensitive_info': 'sensitiveInfo',
        'value': 'value',
        'variable_type': 'variableType'
    }

    def __init__(self, delete=None, id=None, name=None, sensitive_info=None, value=None, variable_type=None):
        r"""TaskExtParam

        The model defined in huaweicloud sdk

        :param delete: 是否删除
        :type delete: bool
        :param id: 参数id
        :type id: str
        :param name: 参数名称
        :type name: str
        :param sensitive_info: 是否敏感信息：true-敏感信息，false-非敏感信息
        :type sensitive_info: bool
        :param value: 参数值
        :type value: str
        :param variable_type: 参数类型
        :type variable_type: str
        """
        
        

        self._delete = None
        self._id = None
        self._name = None
        self._sensitive_info = None
        self._value = None
        self._variable_type = None
        self.discriminator = None

        if delete is not None:
            self.delete = delete
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if sensitive_info is not None:
            self.sensitive_info = sensitive_info
        if value is not None:
            self.value = value
        if variable_type is not None:
            self.variable_type = variable_type

    @property
    def delete(self):
        r"""Gets the delete of this TaskExtParam.

        是否删除

        :return: The delete of this TaskExtParam.
        :rtype: bool
        """
        return self._delete

    @delete.setter
    def delete(self, delete):
        r"""Sets the delete of this TaskExtParam.

        是否删除

        :param delete: The delete of this TaskExtParam.
        :type delete: bool
        """
        self._delete = delete

    @property
    def id(self):
        r"""Gets the id of this TaskExtParam.

        参数id

        :return: The id of this TaskExtParam.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this TaskExtParam.

        参数id

        :param id: The id of this TaskExtParam.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this TaskExtParam.

        参数名称

        :return: The name of this TaskExtParam.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this TaskExtParam.

        参数名称

        :param name: The name of this TaskExtParam.
        :type name: str
        """
        self._name = name

    @property
    def sensitive_info(self):
        r"""Gets the sensitive_info of this TaskExtParam.

        是否敏感信息：true-敏感信息，false-非敏感信息

        :return: The sensitive_info of this TaskExtParam.
        :rtype: bool
        """
        return self._sensitive_info

    @sensitive_info.setter
    def sensitive_info(self, sensitive_info):
        r"""Sets the sensitive_info of this TaskExtParam.

        是否敏感信息：true-敏感信息，false-非敏感信息

        :param sensitive_info: The sensitive_info of this TaskExtParam.
        :type sensitive_info: bool
        """
        self._sensitive_info = sensitive_info

    @property
    def value(self):
        r"""Gets the value of this TaskExtParam.

        参数值

        :return: The value of this TaskExtParam.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this TaskExtParam.

        参数值

        :param value: The value of this TaskExtParam.
        :type value: str
        """
        self._value = value

    @property
    def variable_type(self):
        r"""Gets the variable_type of this TaskExtParam.

        参数类型

        :return: The variable_type of this TaskExtParam.
        :rtype: str
        """
        return self._variable_type

    @variable_type.setter
    def variable_type(self, variable_type):
        r"""Sets the variable_type of this TaskExtParam.

        参数类型

        :param variable_type: The variable_type of this TaskExtParam.
        :type variable_type: str
        """
        self._variable_type = variable_type

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
        if not isinstance(other, TaskExtParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
