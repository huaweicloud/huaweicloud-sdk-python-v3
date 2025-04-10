# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CompareJobContentDetailInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'source_key_value': 'list[str]',
        'target_key_value': 'list[str]',
        'select_sql': 'str',
        'target_select_sql': 'str'
    }

    attribute_map = {
        'source_key_value': 'source_key_value',
        'target_key_value': 'target_key_value',
        'select_sql': 'select_sql',
        'target_select_sql': 'target_select_sql'
    }

    def __init__(self, source_key_value=None, target_key_value=None, select_sql=None, target_select_sql=None):
        r"""CompareJobContentDetailInfo

        The model defined in huaweicloud sdk

        :param source_key_value: 源库KEY值列表。
        :type source_key_value: list[str]
        :param target_key_value: 目标库KEY值列表。
        :type target_key_value: list[str]
        :param select_sql: 查询源库的SQL。
        :type select_sql: str
        :param target_select_sql: 查询目标库的SQL。
        :type target_select_sql: str
        """
        
        

        self._source_key_value = None
        self._target_key_value = None
        self._select_sql = None
        self._target_select_sql = None
        self.discriminator = None

        if source_key_value is not None:
            self.source_key_value = source_key_value
        if target_key_value is not None:
            self.target_key_value = target_key_value
        if select_sql is not None:
            self.select_sql = select_sql
        if target_select_sql is not None:
            self.target_select_sql = target_select_sql

    @property
    def source_key_value(self):
        r"""Gets the source_key_value of this CompareJobContentDetailInfo.

        源库KEY值列表。

        :return: The source_key_value of this CompareJobContentDetailInfo.
        :rtype: list[str]
        """
        return self._source_key_value

    @source_key_value.setter
    def source_key_value(self, source_key_value):
        r"""Sets the source_key_value of this CompareJobContentDetailInfo.

        源库KEY值列表。

        :param source_key_value: The source_key_value of this CompareJobContentDetailInfo.
        :type source_key_value: list[str]
        """
        self._source_key_value = source_key_value

    @property
    def target_key_value(self):
        r"""Gets the target_key_value of this CompareJobContentDetailInfo.

        目标库KEY值列表。

        :return: The target_key_value of this CompareJobContentDetailInfo.
        :rtype: list[str]
        """
        return self._target_key_value

    @target_key_value.setter
    def target_key_value(self, target_key_value):
        r"""Sets the target_key_value of this CompareJobContentDetailInfo.

        目标库KEY值列表。

        :param target_key_value: The target_key_value of this CompareJobContentDetailInfo.
        :type target_key_value: list[str]
        """
        self._target_key_value = target_key_value

    @property
    def select_sql(self):
        r"""Gets the select_sql of this CompareJobContentDetailInfo.

        查询源库的SQL。

        :return: The select_sql of this CompareJobContentDetailInfo.
        :rtype: str
        """
        return self._select_sql

    @select_sql.setter
    def select_sql(self, select_sql):
        r"""Sets the select_sql of this CompareJobContentDetailInfo.

        查询源库的SQL。

        :param select_sql: The select_sql of this CompareJobContentDetailInfo.
        :type select_sql: str
        """
        self._select_sql = select_sql

    @property
    def target_select_sql(self):
        r"""Gets the target_select_sql of this CompareJobContentDetailInfo.

        查询目标库的SQL。

        :return: The target_select_sql of this CompareJobContentDetailInfo.
        :rtype: str
        """
        return self._target_select_sql

    @target_select_sql.setter
    def target_select_sql(self, target_select_sql):
        r"""Sets the target_select_sql of this CompareJobContentDetailInfo.

        查询目标库的SQL。

        :param target_select_sql: The target_select_sql of this CompareJobContentDetailInfo.
        :type target_select_sql: str
        """
        self._target_select_sql = target_select_sql

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
        if not isinstance(other, CompareJobContentDetailInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
