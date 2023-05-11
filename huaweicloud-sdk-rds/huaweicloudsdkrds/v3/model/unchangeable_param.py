# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UnchangeableParam:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'lower_case_table_names': 'str'
    }

    attribute_map = {
        'lower_case_table_names': 'lower_case_table_names'
    }

    def __init__(self, lower_case_table_names=None):
        """UnchangeableParam

        The model defined in huaweicloud sdk

        :param lower_case_table_names: 表名大小写是否敏感，默认值是“1”，当前仅MySQL 8.0支持。 取值范围： - 0：表名被存储成固定且表名称大小写敏感。 - 1：表名将被存储成小写且表名称大小写不敏感。
        :type lower_case_table_names: str
        """
        
        

        self._lower_case_table_names = None
        self.discriminator = None

        if lower_case_table_names is not None:
            self.lower_case_table_names = lower_case_table_names

    @property
    def lower_case_table_names(self):
        """Gets the lower_case_table_names of this UnchangeableParam.

        表名大小写是否敏感，默认值是“1”，当前仅MySQL 8.0支持。 取值范围： - 0：表名被存储成固定且表名称大小写敏感。 - 1：表名将被存储成小写且表名称大小写不敏感。

        :return: The lower_case_table_names of this UnchangeableParam.
        :rtype: str
        """
        return self._lower_case_table_names

    @lower_case_table_names.setter
    def lower_case_table_names(self, lower_case_table_names):
        """Sets the lower_case_table_names of this UnchangeableParam.

        表名大小写是否敏感，默认值是“1”，当前仅MySQL 8.0支持。 取值范围： - 0：表名被存储成固定且表名称大小写敏感。 - 1：表名将被存储成小写且表名称大小写不敏感。

        :param lower_case_table_names: The lower_case_table_names of this UnchangeableParam.
        :type lower_case_table_names: str
        """
        self._lower_case_table_names = lower_case_table_names

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
        if not isinstance(other, UnchangeableParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
