# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MappingInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'source_column': 'str',
        'source_column_type': 'str',
        'source_column_length': 'str',
        'target_column': 'str',
        'target_column_type': 'str',
        'target_column_length': 'str'
    }

    attribute_map = {
        'source_column': 'source_column',
        'source_column_type': 'source_column_type',
        'source_column_length': 'source_column_length',
        'target_column': 'target_column',
        'target_column_type': 'target_column_type',
        'target_column_length': 'target_column_length'
    }

    def __init__(self, source_column=None, source_column_type=None, source_column_length=None, target_column=None, target_column_type=None, target_column_length=None):
        """MappingInfo

        The model defined in huaweicloud sdk

        :param source_column: 源端字段
        :type source_column: str
        :param source_column_type: 源端字段类型
        :type source_column_type: str
        :param source_column_length: 源端字段长度
        :type source_column_length: str
        :param target_column: 目标端字段
        :type target_column: str
        :param target_column_type: 目标端字段类型
        :type target_column_type: str
        :param target_column_length: 目标端字段长度
        :type target_column_length: str
        """
        
        

        self._source_column = None
        self._source_column_type = None
        self._source_column_length = None
        self._target_column = None
        self._target_column_type = None
        self._target_column_length = None
        self.discriminator = None

        if source_column is not None:
            self.source_column = source_column
        if source_column_type is not None:
            self.source_column_type = source_column_type
        if source_column_length is not None:
            self.source_column_length = source_column_length
        if target_column is not None:
            self.target_column = target_column
        if target_column_type is not None:
            self.target_column_type = target_column_type
        if target_column_length is not None:
            self.target_column_length = target_column_length

    @property
    def source_column(self):
        """Gets the source_column of this MappingInfo.

        源端字段

        :return: The source_column of this MappingInfo.
        :rtype: str
        """
        return self._source_column

    @source_column.setter
    def source_column(self, source_column):
        """Sets the source_column of this MappingInfo.

        源端字段

        :param source_column: The source_column of this MappingInfo.
        :type source_column: str
        """
        self._source_column = source_column

    @property
    def source_column_type(self):
        """Gets the source_column_type of this MappingInfo.

        源端字段类型

        :return: The source_column_type of this MappingInfo.
        :rtype: str
        """
        return self._source_column_type

    @source_column_type.setter
    def source_column_type(self, source_column_type):
        """Sets the source_column_type of this MappingInfo.

        源端字段类型

        :param source_column_type: The source_column_type of this MappingInfo.
        :type source_column_type: str
        """
        self._source_column_type = source_column_type

    @property
    def source_column_length(self):
        """Gets the source_column_length of this MappingInfo.

        源端字段长度

        :return: The source_column_length of this MappingInfo.
        :rtype: str
        """
        return self._source_column_length

    @source_column_length.setter
    def source_column_length(self, source_column_length):
        """Sets the source_column_length of this MappingInfo.

        源端字段长度

        :param source_column_length: The source_column_length of this MappingInfo.
        :type source_column_length: str
        """
        self._source_column_length = source_column_length

    @property
    def target_column(self):
        """Gets the target_column of this MappingInfo.

        目标端字段

        :return: The target_column of this MappingInfo.
        :rtype: str
        """
        return self._target_column

    @target_column.setter
    def target_column(self, target_column):
        """Sets the target_column of this MappingInfo.

        目标端字段

        :param target_column: The target_column of this MappingInfo.
        :type target_column: str
        """
        self._target_column = target_column

    @property
    def target_column_type(self):
        """Gets the target_column_type of this MappingInfo.

        目标端字段类型

        :return: The target_column_type of this MappingInfo.
        :rtype: str
        """
        return self._target_column_type

    @target_column_type.setter
    def target_column_type(self, target_column_type):
        """Sets the target_column_type of this MappingInfo.

        目标端字段类型

        :param target_column_type: The target_column_type of this MappingInfo.
        :type target_column_type: str
        """
        self._target_column_type = target_column_type

    @property
    def target_column_length(self):
        """Gets the target_column_length of this MappingInfo.

        目标端字段长度

        :return: The target_column_length of this MappingInfo.
        :rtype: str
        """
        return self._target_column_length

    @target_column_length.setter
    def target_column_length(self, target_column_length):
        """Sets the target_column_length of this MappingInfo.

        目标端字段长度

        :param target_column_length: The target_column_length of this MappingInfo.
        :type target_column_length: str
        """
        self._target_column_length = target_column_length

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
        if not isinstance(other, MappingInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
