# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QueryDataBaseRequestV3:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'databases': 'list[str]',
        'source_instance_id': 'str'
    }

    attribute_map = {
        'databases': 'databases',
        'source_instance_id': 'source_instance_id'
    }

    def __init__(self, databases=None, source_instance_id=None):
        r"""QueryDataBaseRequestV3

        The model defined in huaweicloud sdk

        :param databases: **参数解释**：  查询的数据库名称。  **约束限制**：  仅支持英文大小写字母、数字以及下划线，模糊搜索时列表元素数目必须为1。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type databases: list[str]
        :param source_instance_id: **参数解释**：  需要查询数据库的源实例ID，严格匹配UUID规则。  **约束限制**：  只能由英文字母、数字组成，且长度为36个字符。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type source_instance_id: str
        """
        
        

        self._databases = None
        self._source_instance_id = None
        self.discriminator = None

        if databases is not None:
            self.databases = databases
        if source_instance_id is not None:
            self.source_instance_id = source_instance_id

    @property
    def databases(self):
        r"""Gets the databases of this QueryDataBaseRequestV3.

        **参数解释**：  查询的数据库名称。  **约束限制**：  仅支持英文大小写字母、数字以及下划线，模糊搜索时列表元素数目必须为1。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The databases of this QueryDataBaseRequestV3.
        :rtype: list[str]
        """
        return self._databases

    @databases.setter
    def databases(self, databases):
        r"""Sets the databases of this QueryDataBaseRequestV3.

        **参数解释**：  查询的数据库名称。  **约束限制**：  仅支持英文大小写字母、数字以及下划线，模糊搜索时列表元素数目必须为1。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param databases: The databases of this QueryDataBaseRequestV3.
        :type databases: list[str]
        """
        self._databases = databases

    @property
    def source_instance_id(self):
        r"""Gets the source_instance_id of this QueryDataBaseRequestV3.

        **参数解释**：  需要查询数据库的源实例ID，严格匹配UUID规则。  **约束限制**：  只能由英文字母、数字组成，且长度为36个字符。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The source_instance_id of this QueryDataBaseRequestV3.
        :rtype: str
        """
        return self._source_instance_id

    @source_instance_id.setter
    def source_instance_id(self, source_instance_id):
        r"""Sets the source_instance_id of this QueryDataBaseRequestV3.

        **参数解释**：  需要查询数据库的源实例ID，严格匹配UUID规则。  **约束限制**：  只能由英文字母、数字组成，且长度为36个字符。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param source_instance_id: The source_instance_id of this QueryDataBaseRequestV3.
        :type source_instance_id: str
        """
        self._source_instance_id = source_instance_id

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
        if not isinstance(other, QueryDataBaseRequestV3):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
