# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SparkSqlCatalogContext:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'catalog_name': 'str',
        'database_name': 'str'
    }

    attribute_map = {
        'catalog_name': 'catalog_name',
        'database_name': 'database_name'
    }

    def __init__(self, catalog_name=None, database_name=None):
        r"""SparkSqlCatalogContext

        The model defined in huaweicloud sdk

        :param catalog_name: **参数解释**：Catalog名称，用于指定作业使用的数据目录。可在控制台的Catalog管理页面查看，或通过查询Catalog列表接口获取。 **约束限制**：不涉及。 **取值范围**：不超过128个字符。 **默认取值**：不涉及。 
        :type catalog_name: str
        :param database_name: **参数解释**：默认数据库名称，用于指定作业默认操作的数据库。如果未指定，则使用Catalog的默认数据库。 **约束限制**：不涉及。 **取值范围**：不超过128个字符。 **默认取值**：不涉及。 
        :type database_name: str
        """
        
        

        self._catalog_name = None
        self._database_name = None
        self.discriminator = None

        self.catalog_name = catalog_name
        if database_name is not None:
            self.database_name = database_name

    @property
    def catalog_name(self):
        r"""Gets the catalog_name of this SparkSqlCatalogContext.

        **参数解释**：Catalog名称，用于指定作业使用的数据目录。可在控制台的Catalog管理页面查看，或通过查询Catalog列表接口获取。 **约束限制**：不涉及。 **取值范围**：不超过128个字符。 **默认取值**：不涉及。 

        :return: The catalog_name of this SparkSqlCatalogContext.
        :rtype: str
        """
        return self._catalog_name

    @catalog_name.setter
    def catalog_name(self, catalog_name):
        r"""Sets the catalog_name of this SparkSqlCatalogContext.

        **参数解释**：Catalog名称，用于指定作业使用的数据目录。可在控制台的Catalog管理页面查看，或通过查询Catalog列表接口获取。 **约束限制**：不涉及。 **取值范围**：不超过128个字符。 **默认取值**：不涉及。 

        :param catalog_name: The catalog_name of this SparkSqlCatalogContext.
        :type catalog_name: str
        """
        self._catalog_name = catalog_name

    @property
    def database_name(self):
        r"""Gets the database_name of this SparkSqlCatalogContext.

        **参数解释**：默认数据库名称，用于指定作业默认操作的数据库。如果未指定，则使用Catalog的默认数据库。 **约束限制**：不涉及。 **取值范围**：不超过128个字符。 **默认取值**：不涉及。 

        :return: The database_name of this SparkSqlCatalogContext.
        :rtype: str
        """
        return self._database_name

    @database_name.setter
    def database_name(self, database_name):
        r"""Sets the database_name of this SparkSqlCatalogContext.

        **参数解释**：默认数据库名称，用于指定作业默认操作的数据库。如果未指定，则使用Catalog的默认数据库。 **约束限制**：不涉及。 **取值范围**：不超过128个字符。 **默认取值**：不涉及。 

        :param database_name: The database_name of this SparkSqlCatalogContext.
        :type database_name: str
        """
        self._database_name = database_name

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
        if not isinstance(other, SparkSqlCatalogContext):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
