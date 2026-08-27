# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OnlineDDLTaskContentItem:

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
        'ddl_info': 'list[OnlineDDLInfoItem]'
    }

    attribute_map = {
        'schema': 'schema',
        'ddl_info': 'ddl_info'
    }

    def __init__(self, schema=None, ddl_info=None):
        r"""OnlineDDLTaskContentItem

        The model defined in huaweicloud sdk

        :param schema: **参数解释**：  无锁变更的目标数据库。  **取值范围**： 不涉及。
        :type schema: str
        :param ddl_info: **参数解释**：  无锁变更的DDL信息。
        :type ddl_info: list[:class:`huaweicloudsdkgaussdb.v3.OnlineDDLInfoItem`]
        """
        
        

        self._schema = None
        self._ddl_info = None
        self.discriminator = None

        if schema is not None:
            self.schema = schema
        if ddl_info is not None:
            self.ddl_info = ddl_info

    @property
    def schema(self):
        r"""Gets the schema of this OnlineDDLTaskContentItem.

        **参数解释**：  无锁变更的目标数据库。  **取值范围**： 不涉及。

        :return: The schema of this OnlineDDLTaskContentItem.
        :rtype: str
        """
        return self._schema

    @schema.setter
    def schema(self, schema):
        r"""Sets the schema of this OnlineDDLTaskContentItem.

        **参数解释**：  无锁变更的目标数据库。  **取值范围**： 不涉及。

        :param schema: The schema of this OnlineDDLTaskContentItem.
        :type schema: str
        """
        self._schema = schema

    @property
    def ddl_info(self):
        r"""Gets the ddl_info of this OnlineDDLTaskContentItem.

        **参数解释**：  无锁变更的DDL信息。

        :return: The ddl_info of this OnlineDDLTaskContentItem.
        :rtype: list[:class:`huaweicloudsdkgaussdb.v3.OnlineDDLInfoItem`]
        """
        return self._ddl_info

    @ddl_info.setter
    def ddl_info(self, ddl_info):
        r"""Sets the ddl_info of this OnlineDDLTaskContentItem.

        **参数解释**：  无锁变更的DDL信息。

        :param ddl_info: The ddl_info of this OnlineDDLTaskContentItem.
        :type ddl_info: list[:class:`huaweicloudsdkgaussdb.v3.OnlineDDLInfoItem`]
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
        if not isinstance(other, OnlineDDLTaskContentItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
