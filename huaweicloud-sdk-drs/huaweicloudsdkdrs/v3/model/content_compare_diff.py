# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ContentCompareDiff:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'target_select_sql': 'str',
        'source_select_sql': 'str',
        'source_key_value': 'list[str]',
        'target_key_value': 'list[str]'
    }

    attribute_map = {
        'target_select_sql': 'target_select_sql',
        'source_select_sql': 'source_select_sql',
        'source_key_value': 'source_key_value',
        'target_key_value': 'target_key_value'
    }

    def __init__(self, target_select_sql=None, source_select_sql=None, source_key_value=None, target_key_value=None):
        """ContentCompareDiff

        The model defined in huaweicloud sdk

        :param target_select_sql: 查询目标库的SQL。
        :type target_select_sql: str
        :param source_select_sql: 查询源库的SQL。
        :type source_select_sql: str
        :param source_key_value: 源库KEY值列表。
        :type source_key_value: list[str]
        :param target_key_value: 目标库KEY值列表。
        :type target_key_value: list[str]
        """
        
        

        self._target_select_sql = None
        self._source_select_sql = None
        self._source_key_value = None
        self._target_key_value = None
        self.discriminator = None

        if target_select_sql is not None:
            self.target_select_sql = target_select_sql
        if source_select_sql is not None:
            self.source_select_sql = source_select_sql
        self.source_key_value = source_key_value
        self.target_key_value = target_key_value

    @property
    def target_select_sql(self):
        """Gets the target_select_sql of this ContentCompareDiff.

        查询目标库的SQL。

        :return: The target_select_sql of this ContentCompareDiff.
        :rtype: str
        """
        return self._target_select_sql

    @target_select_sql.setter
    def target_select_sql(self, target_select_sql):
        """Sets the target_select_sql of this ContentCompareDiff.

        查询目标库的SQL。

        :param target_select_sql: The target_select_sql of this ContentCompareDiff.
        :type target_select_sql: str
        """
        self._target_select_sql = target_select_sql

    @property
    def source_select_sql(self):
        """Gets the source_select_sql of this ContentCompareDiff.

        查询源库的SQL。

        :return: The source_select_sql of this ContentCompareDiff.
        :rtype: str
        """
        return self._source_select_sql

    @source_select_sql.setter
    def source_select_sql(self, source_select_sql):
        """Sets the source_select_sql of this ContentCompareDiff.

        查询源库的SQL。

        :param source_select_sql: The source_select_sql of this ContentCompareDiff.
        :type source_select_sql: str
        """
        self._source_select_sql = source_select_sql

    @property
    def source_key_value(self):
        """Gets the source_key_value of this ContentCompareDiff.

        源库KEY值列表。

        :return: The source_key_value of this ContentCompareDiff.
        :rtype: list[str]
        """
        return self._source_key_value

    @source_key_value.setter
    def source_key_value(self, source_key_value):
        """Sets the source_key_value of this ContentCompareDiff.

        源库KEY值列表。

        :param source_key_value: The source_key_value of this ContentCompareDiff.
        :type source_key_value: list[str]
        """
        self._source_key_value = source_key_value

    @property
    def target_key_value(self):
        """Gets the target_key_value of this ContentCompareDiff.

        目标库KEY值列表。

        :return: The target_key_value of this ContentCompareDiff.
        :rtype: list[str]
        """
        return self._target_key_value

    @target_key_value.setter
    def target_key_value(self, target_key_value):
        """Sets the target_key_value of this ContentCompareDiff.

        目标库KEY值列表。

        :param target_key_value: The target_key_value of this ContentCompareDiff.
        :type target_key_value: list[str]
        """
        self._target_key_value = target_key_value

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
        if not isinstance(other, ContentCompareDiff):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
