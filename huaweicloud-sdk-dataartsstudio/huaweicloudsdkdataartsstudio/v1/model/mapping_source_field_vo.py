# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MappingSourceFieldVO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'target_field_id': 'int',
        'target_field_name': 'str',
        'field_ids': 'str',
        'transform_expression': 'str',
        'field_names': 'list[str]',
        'changed': 'bool'
    }

    attribute_map = {
        'target_field_id': 'target_field_id',
        'target_field_name': 'target_field_name',
        'field_ids': 'field_ids',
        'transform_expression': 'transform_expression',
        'field_names': 'field_names',
        'changed': 'changed'
    }

    def __init__(self, target_field_id=None, target_field_name=None, field_ids=None, transform_expression=None, field_names=None, changed=None):
        """MappingSourceFieldVO

        The model defined in huaweicloud sdk

        :param target_field_id: 目标字段ID,当前表的某个字段
        :type target_field_id: int
        :param target_field_name: 目标字段编码
        :type target_field_name: str
        :param field_ids: 来源字段id,多个id以逗号分隔
        :type field_ids: str
        :param transform_expression: 转换表达式
        :type transform_expression: str
        :param field_names: 来源字段名称列表
        :type field_names: list[str]
        :param changed: 字段是否发生变化
        :type changed: bool
        """
        
        

        self._target_field_id = None
        self._target_field_name = None
        self._field_ids = None
        self._transform_expression = None
        self._field_names = None
        self._changed = None
        self.discriminator = None

        if target_field_id is not None:
            self.target_field_id = target_field_id
        self.target_field_name = target_field_name
        if field_ids is not None:
            self.field_ids = field_ids
        if transform_expression is not None:
            self.transform_expression = transform_expression
        if field_names is not None:
            self.field_names = field_names
        if changed is not None:
            self.changed = changed

    @property
    def target_field_id(self):
        """Gets the target_field_id of this MappingSourceFieldVO.

        目标字段ID,当前表的某个字段

        :return: The target_field_id of this MappingSourceFieldVO.
        :rtype: int
        """
        return self._target_field_id

    @target_field_id.setter
    def target_field_id(self, target_field_id):
        """Sets the target_field_id of this MappingSourceFieldVO.

        目标字段ID,当前表的某个字段

        :param target_field_id: The target_field_id of this MappingSourceFieldVO.
        :type target_field_id: int
        """
        self._target_field_id = target_field_id

    @property
    def target_field_name(self):
        """Gets the target_field_name of this MappingSourceFieldVO.

        目标字段编码

        :return: The target_field_name of this MappingSourceFieldVO.
        :rtype: str
        """
        return self._target_field_name

    @target_field_name.setter
    def target_field_name(self, target_field_name):
        """Sets the target_field_name of this MappingSourceFieldVO.

        目标字段编码

        :param target_field_name: The target_field_name of this MappingSourceFieldVO.
        :type target_field_name: str
        """
        self._target_field_name = target_field_name

    @property
    def field_ids(self):
        """Gets the field_ids of this MappingSourceFieldVO.

        来源字段id,多个id以逗号分隔

        :return: The field_ids of this MappingSourceFieldVO.
        :rtype: str
        """
        return self._field_ids

    @field_ids.setter
    def field_ids(self, field_ids):
        """Sets the field_ids of this MappingSourceFieldVO.

        来源字段id,多个id以逗号分隔

        :param field_ids: The field_ids of this MappingSourceFieldVO.
        :type field_ids: str
        """
        self._field_ids = field_ids

    @property
    def transform_expression(self):
        """Gets the transform_expression of this MappingSourceFieldVO.

        转换表达式

        :return: The transform_expression of this MappingSourceFieldVO.
        :rtype: str
        """
        return self._transform_expression

    @transform_expression.setter
    def transform_expression(self, transform_expression):
        """Sets the transform_expression of this MappingSourceFieldVO.

        转换表达式

        :param transform_expression: The transform_expression of this MappingSourceFieldVO.
        :type transform_expression: str
        """
        self._transform_expression = transform_expression

    @property
    def field_names(self):
        """Gets the field_names of this MappingSourceFieldVO.

        来源字段名称列表

        :return: The field_names of this MappingSourceFieldVO.
        :rtype: list[str]
        """
        return self._field_names

    @field_names.setter
    def field_names(self, field_names):
        """Sets the field_names of this MappingSourceFieldVO.

        来源字段名称列表

        :param field_names: The field_names of this MappingSourceFieldVO.
        :type field_names: list[str]
        """
        self._field_names = field_names

    @property
    def changed(self):
        """Gets the changed of this MappingSourceFieldVO.

        字段是否发生变化

        :return: The changed of this MappingSourceFieldVO.
        :rtype: bool
        """
        return self._changed

    @changed.setter
    def changed(self, changed):
        """Sets the changed of this MappingSourceFieldVO.

        字段是否发生变化

        :param changed: The changed of this MappingSourceFieldVO.
        :type changed: bool
        """
        self._changed = changed

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
        if not isinstance(other, MappingSourceFieldVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
