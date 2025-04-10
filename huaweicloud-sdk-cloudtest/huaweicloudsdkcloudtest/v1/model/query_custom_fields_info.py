# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QueryCustomFieldsInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'int',
        'values': 'list[str]',
        'field_name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'values': 'values',
        'field_name': 'field_name'
    }

    def __init__(self, id=None, values=None, field_name=None):
        r"""QueryCustomFieldsInfo

        The model defined in huaweicloud sdk

        :param id: 测试用例自定义字段Id
        :type id: int
        :param values: 测试用例自定义字段值
        :type values: list[str]
        :param field_name: 自定义字段名，优先取id再取fieldName
        :type field_name: str
        """
        
        

        self._id = None
        self._values = None
        self._field_name = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if values is not None:
            self.values = values
        if field_name is not None:
            self.field_name = field_name

    @property
    def id(self):
        r"""Gets the id of this QueryCustomFieldsInfo.

        测试用例自定义字段Id

        :return: The id of this QueryCustomFieldsInfo.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this QueryCustomFieldsInfo.

        测试用例自定义字段Id

        :param id: The id of this QueryCustomFieldsInfo.
        :type id: int
        """
        self._id = id

    @property
    def values(self):
        r"""Gets the values of this QueryCustomFieldsInfo.

        测试用例自定义字段值

        :return: The values of this QueryCustomFieldsInfo.
        :rtype: list[str]
        """
        return self._values

    @values.setter
    def values(self, values):
        r"""Sets the values of this QueryCustomFieldsInfo.

        测试用例自定义字段值

        :param values: The values of this QueryCustomFieldsInfo.
        :type values: list[str]
        """
        self._values = values

    @property
    def field_name(self):
        r"""Gets the field_name of this QueryCustomFieldsInfo.

        自定义字段名，优先取id再取fieldName

        :return: The field_name of this QueryCustomFieldsInfo.
        :rtype: str
        """
        return self._field_name

    @field_name.setter
    def field_name(self, field_name):
        r"""Sets the field_name of this QueryCustomFieldsInfo.

        自定义字段名，优先取id再取fieldName

        :param field_name: The field_name of this QueryCustomFieldsInfo.
        :type field_name: str
        """
        self._field_name = field_name

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
        if not isinstance(other, QueryCustomFieldsInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
