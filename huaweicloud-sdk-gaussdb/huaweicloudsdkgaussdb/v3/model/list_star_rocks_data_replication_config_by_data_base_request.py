# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListStarRocksDataReplicationConfigByDataBaseRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'x_language': 'str',
        'database': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'x_language': 'X-Language',
        'database': 'database'
    }

    def __init__(self, instance_id=None, x_language=None, database=None):
        r"""ListStarRocksDataReplicationConfigByDataBaseRequest

        The model defined in huaweicloud sdk

        :param instance_id: **参数解释**：  StarRocks实例ID，严格匹配UUID规则。  **约束限制**：  不涉及。  **取值范围**：  只能由英文字母、数字组成，后缀为in17，且长度为36个字符。  **默认值**：  不涉及。
        :type instance_id: str
        :param x_language: **参数解释**：  请求语言类型。  **约束限制**：  不涉及。  **取值范围**：  - en-us - zh-cn  **默认值**：  en-us。
        :type x_language: str
        :param database: **参数解释**：  目标数据库名。  **约束限制**：  不涉及。  **取值范围**：  字符长度限制3~128位，仅支持英文大小写字母、数字以及下划线。  **默认值**：  不涉及。
        :type database: str
        """
        
        

        self._instance_id = None
        self._x_language = None
        self._database = None
        self.discriminator = None

        self.instance_id = instance_id
        self.x_language = x_language
        self.database = database

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ListStarRocksDataReplicationConfigByDataBaseRequest.

        **参数解释**：  StarRocks实例ID，严格匹配UUID规则。  **约束限制**：  不涉及。  **取值范围**：  只能由英文字母、数字组成，后缀为in17，且长度为36个字符。  **默认值**：  不涉及。

        :return: The instance_id of this ListStarRocksDataReplicationConfigByDataBaseRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ListStarRocksDataReplicationConfigByDataBaseRequest.

        **参数解释**：  StarRocks实例ID，严格匹配UUID规则。  **约束限制**：  不涉及。  **取值范围**：  只能由英文字母、数字组成，后缀为in17，且长度为36个字符。  **默认值**：  不涉及。

        :param instance_id: The instance_id of this ListStarRocksDataReplicationConfigByDataBaseRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def x_language(self):
        r"""Gets the x_language of this ListStarRocksDataReplicationConfigByDataBaseRequest.

        **参数解释**：  请求语言类型。  **约束限制**：  不涉及。  **取值范围**：  - en-us - zh-cn  **默认值**：  en-us。

        :return: The x_language of this ListStarRocksDataReplicationConfigByDataBaseRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this ListStarRocksDataReplicationConfigByDataBaseRequest.

        **参数解释**：  请求语言类型。  **约束限制**：  不涉及。  **取值范围**：  - en-us - zh-cn  **默认值**：  en-us。

        :param x_language: The x_language of this ListStarRocksDataReplicationConfigByDataBaseRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def database(self):
        r"""Gets the database of this ListStarRocksDataReplicationConfigByDataBaseRequest.

        **参数解释**：  目标数据库名。  **约束限制**：  不涉及。  **取值范围**：  字符长度限制3~128位，仅支持英文大小写字母、数字以及下划线。  **默认值**：  不涉及。

        :return: The database of this ListStarRocksDataReplicationConfigByDataBaseRequest.
        :rtype: str
        """
        return self._database

    @database.setter
    def database(self, database):
        r"""Sets the database of this ListStarRocksDataReplicationConfigByDataBaseRequest.

        **参数解释**：  目标数据库名。  **约束限制**：  不涉及。  **取值范围**：  字符长度限制3~128位，仅支持英文大小写字母、数字以及下划线。  **默认值**：  不涉及。

        :param database: The database of this ListStarRocksDataReplicationConfigByDataBaseRequest.
        :type database: str
        """
        self._database = database

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
        if not isinstance(other, ListStarRocksDataReplicationConfigByDataBaseRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
