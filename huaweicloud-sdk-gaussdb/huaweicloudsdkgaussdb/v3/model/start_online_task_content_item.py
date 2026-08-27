# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StartOnlineTaskContentItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'schema': 'str',
        'ddl_info': 'list[StartOnlineDDLInfoItem]'
    }

    attribute_map = {
        'schema': 'schema',
        'ddl_info': 'ddl_info'
    }

    def __init__(self, schema=None, ddl_info=None):
        r"""StartOnlineTaskContentItem

        The model defined in huaweicloud sdk

        :param schema: **参数解释**：  无锁变更的目标数据库。 获取方法请参见[查询数据库列表](https://support.huaweicloud.com/api-taurusdb/ListGaussMySqlDatabase.html)。  **约束限制**：  不涉及。  **取值范围**： 不涉及。  **默认取值**： 不涉及。
        :type schema: str
        :param ddl_info: **参数解释**：  无锁变更的DDL信息。  **约束限制**： 不涉及。
        :type ddl_info: list[:class:`huaweicloudsdkgaussdb.v3.StartOnlineDDLInfoItem`]
        """
        
        

        self._schema = None
        self._ddl_info = None
        self.discriminator = None

        self.schema = schema
        self.ddl_info = ddl_info

    @property
    def schema(self):
        r"""Gets the schema of this StartOnlineTaskContentItem.

        **参数解释**：  无锁变更的目标数据库。 获取方法请参见[查询数据库列表](https://support.huaweicloud.com/api-taurusdb/ListGaussMySqlDatabase.html)。  **约束限制**：  不涉及。  **取值范围**： 不涉及。  **默认取值**： 不涉及。

        :return: The schema of this StartOnlineTaskContentItem.
        :rtype: str
        """
        return self._schema

    @schema.setter
    def schema(self, schema):
        r"""Sets the schema of this StartOnlineTaskContentItem.

        **参数解释**：  无锁变更的目标数据库。 获取方法请参见[查询数据库列表](https://support.huaweicloud.com/api-taurusdb/ListGaussMySqlDatabase.html)。  **约束限制**：  不涉及。  **取值范围**： 不涉及。  **默认取值**： 不涉及。

        :param schema: The schema of this StartOnlineTaskContentItem.
        :type schema: str
        """
        self._schema = schema

    @property
    def ddl_info(self):
        r"""Gets the ddl_info of this StartOnlineTaskContentItem.

        **参数解释**：  无锁变更的DDL信息。  **约束限制**： 不涉及。

        :return: The ddl_info of this StartOnlineTaskContentItem.
        :rtype: list[:class:`huaweicloudsdkgaussdb.v3.StartOnlineDDLInfoItem`]
        """
        return self._ddl_info

    @ddl_info.setter
    def ddl_info(self, ddl_info):
        r"""Sets the ddl_info of this StartOnlineTaskContentItem.

        **参数解释**：  无锁变更的DDL信息。  **约束限制**： 不涉及。

        :param ddl_info: The ddl_info of this StartOnlineTaskContentItem.
        :type ddl_info: list[:class:`huaweicloudsdkgaussdb.v3.StartOnlineDDLInfoItem`]
        """
        self._ddl_info = ddl_info

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
        if not isinstance(other, StartOnlineTaskContentItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
