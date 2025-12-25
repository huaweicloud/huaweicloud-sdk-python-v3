# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateTableRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'table_name': 'str',
        'table_alias': 'str',
        'table_alias_en': 'str',
        'table_alias_fr': 'str',
        'category': 'str',
        'format': 'str',
        'description': 'str',
        'description_en': 'str',
        'description_fr': 'str',
        'directory': 'str',
        'directory_en': 'str',
        'directory_fr': 'str',
        'data_classification': 'str',
        'schema': 'IsapTableSchema',
        'storage_setting': 'TableStorageSetting',
        'display_setting': 'TableDisplaySetting',
        'create_policy': 'str'
    }

    attribute_map = {
        'table_name': 'table_name',
        'table_alias': 'table_alias',
        'table_alias_en': 'table_alias_en',
        'table_alias_fr': 'table_alias_fr',
        'category': 'category',
        'format': 'format',
        'description': 'description',
        'description_en': 'description_en',
        'description_fr': 'description_fr',
        'directory': 'directory',
        'directory_en': 'directory_en',
        'directory_fr': 'directory_fr',
        'data_classification': 'data_classification',
        'schema': 'schema',
        'storage_setting': 'storage_setting',
        'display_setting': 'display_setting',
        'create_policy': 'create_policy'
    }

    def __init__(self, table_name=None, table_alias=None, table_alias_en=None, table_alias_fr=None, category=None, format=None, description=None, description_en=None, description_fr=None, directory=None, directory_en=None, directory_fr=None, data_classification=None, schema=None, storage_setting=None, display_setting=None, create_policy=None):
        r"""CreateTableRequestBody

        The model defined in huaweicloud sdk

        :param table_name: 表名称
        :type table_name: str
        :param table_alias: 表别名
        :type table_alias: str
        :param table_alias_en: 表别名
        :type table_alias_en: str
        :param table_alias_fr: 表别名
        :type table_alias_fr: str
        :param category: **参数解释**: 目录类型 - STREAMING 实时流 - INDEX 索引 - APPLICATION 应用 - TENANT_BUCKET 租户桶 - LAKE 数据湖  **约束限制** 不涉及 **取值范围**: - STREAMING - INDEX - APPLICATION - TENANT_BUCKET - LAKE  **默认值** 不涉及    
        :type category: str
        :param format: **参数解释**: 表格式 - JSON Json格式 - DEBEZIUM_JSON Debezium JSON 格式 - CSV CSV格式 - PARQUET PARQUET格式 - ORC ORC格式  **约束限制** 不涉及 **取值范围**: - JSON - DEBEZIUM_JSON - CSV - PARQUET - ORC  **默认值** 不涉及            
        :type format: str
        :param description: 表相关描述
        :type description: str
        :param description_en: 表相关描述
        :type description_en: str
        :param description_fr: 表相关描述
        :type description_fr: str
        :param directory: 目录分组
        :type directory: str
        :param directory_en: 目录分组
        :type directory_en: str
        :param directory_fr: 目录分组
        :type directory_fr: str
        :param data_classification: **参数解释**: 数据分类 - FACTUAL_DATA 事实数据 - DIMENSION_DATA 维度数据  **约束限制** 不涉及 **取值范围**: - FACTUAL_DATA - DIMENSION_DATA  **默认值** 不涉及      
        :type data_classification: str
        :param schema: 
        :type schema: :class:`huaweicloudsdksecmaster.v2.IsapTableSchema`
        :param storage_setting: 
        :type storage_setting: :class:`huaweicloudsdksecmaster.v2.TableStorageSetting`
        :param display_setting: 
        :type display_setting: :class:`huaweicloudsdksecmaster.v2.TableDisplaySetting`
        :param create_policy: **参数解释**: 创建政策 - SYS_INIT_INDEX_APP_TBL 系统初始化索引应用表 - DEFAULT 默认  **约束限制** 不涉及 **取值范围**: - SYS_INIT_INDEX_APP_TBL - DEFAULT  **默认值** 不涉及            
        :type create_policy: str
        """
        
        

        self._table_name = None
        self._table_alias = None
        self._table_alias_en = None
        self._table_alias_fr = None
        self._category = None
        self._format = None
        self._description = None
        self._description_en = None
        self._description_fr = None
        self._directory = None
        self._directory_en = None
        self._directory_fr = None
        self._data_classification = None
        self._schema = None
        self._storage_setting = None
        self._display_setting = None
        self._create_policy = None
        self.discriminator = None

        self.table_name = table_name
        self.table_alias = table_alias
        if table_alias_en is not None:
            self.table_alias_en = table_alias_en
        if table_alias_fr is not None:
            self.table_alias_fr = table_alias_fr
        self.category = category
        self.format = format
        if description is not None:
            self.description = description
        if description_en is not None:
            self.description_en = description_en
        if description_fr is not None:
            self.description_fr = description_fr
        if directory is not None:
            self.directory = directory
        if directory_en is not None:
            self.directory_en = directory_en
        if directory_fr is not None:
            self.directory_fr = directory_fr
        if data_classification is not None:
            self.data_classification = data_classification
        self.schema = schema
        self.storage_setting = storage_setting
        self.display_setting = display_setting
        if create_policy is not None:
            self.create_policy = create_policy

    @property
    def table_name(self):
        r"""Gets the table_name of this CreateTableRequestBody.

        表名称

        :return: The table_name of this CreateTableRequestBody.
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        r"""Sets the table_name of this CreateTableRequestBody.

        表名称

        :param table_name: The table_name of this CreateTableRequestBody.
        :type table_name: str
        """
        self._table_name = table_name

    @property
    def table_alias(self):
        r"""Gets the table_alias of this CreateTableRequestBody.

        表别名

        :return: The table_alias of this CreateTableRequestBody.
        :rtype: str
        """
        return self._table_alias

    @table_alias.setter
    def table_alias(self, table_alias):
        r"""Sets the table_alias of this CreateTableRequestBody.

        表别名

        :param table_alias: The table_alias of this CreateTableRequestBody.
        :type table_alias: str
        """
        self._table_alias = table_alias

    @property
    def table_alias_en(self):
        r"""Gets the table_alias_en of this CreateTableRequestBody.

        表别名

        :return: The table_alias_en of this CreateTableRequestBody.
        :rtype: str
        """
        return self._table_alias_en

    @table_alias_en.setter
    def table_alias_en(self, table_alias_en):
        r"""Sets the table_alias_en of this CreateTableRequestBody.

        表别名

        :param table_alias_en: The table_alias_en of this CreateTableRequestBody.
        :type table_alias_en: str
        """
        self._table_alias_en = table_alias_en

    @property
    def table_alias_fr(self):
        r"""Gets the table_alias_fr of this CreateTableRequestBody.

        表别名

        :return: The table_alias_fr of this CreateTableRequestBody.
        :rtype: str
        """
        return self._table_alias_fr

    @table_alias_fr.setter
    def table_alias_fr(self, table_alias_fr):
        r"""Sets the table_alias_fr of this CreateTableRequestBody.

        表别名

        :param table_alias_fr: The table_alias_fr of this CreateTableRequestBody.
        :type table_alias_fr: str
        """
        self._table_alias_fr = table_alias_fr

    @property
    def category(self):
        r"""Gets the category of this CreateTableRequestBody.

        **参数解释**: 目录类型 - STREAMING 实时流 - INDEX 索引 - APPLICATION 应用 - TENANT_BUCKET 租户桶 - LAKE 数据湖  **约束限制** 不涉及 **取值范围**: - STREAMING - INDEX - APPLICATION - TENANT_BUCKET - LAKE  **默认值** 不涉及    

        :return: The category of this CreateTableRequestBody.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this CreateTableRequestBody.

        **参数解释**: 目录类型 - STREAMING 实时流 - INDEX 索引 - APPLICATION 应用 - TENANT_BUCKET 租户桶 - LAKE 数据湖  **约束限制** 不涉及 **取值范围**: - STREAMING - INDEX - APPLICATION - TENANT_BUCKET - LAKE  **默认值** 不涉及    

        :param category: The category of this CreateTableRequestBody.
        :type category: str
        """
        self._category = category

    @property
    def format(self):
        r"""Gets the format of this CreateTableRequestBody.

        **参数解释**: 表格式 - JSON Json格式 - DEBEZIUM_JSON Debezium JSON 格式 - CSV CSV格式 - PARQUET PARQUET格式 - ORC ORC格式  **约束限制** 不涉及 **取值范围**: - JSON - DEBEZIUM_JSON - CSV - PARQUET - ORC  **默认值** 不涉及            

        :return: The format of this CreateTableRequestBody.
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        r"""Sets the format of this CreateTableRequestBody.

        **参数解释**: 表格式 - JSON Json格式 - DEBEZIUM_JSON Debezium JSON 格式 - CSV CSV格式 - PARQUET PARQUET格式 - ORC ORC格式  **约束限制** 不涉及 **取值范围**: - JSON - DEBEZIUM_JSON - CSV - PARQUET - ORC  **默认值** 不涉及            

        :param format: The format of this CreateTableRequestBody.
        :type format: str
        """
        self._format = format

    @property
    def description(self):
        r"""Gets the description of this CreateTableRequestBody.

        表相关描述

        :return: The description of this CreateTableRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateTableRequestBody.

        表相关描述

        :param description: The description of this CreateTableRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def description_en(self):
        r"""Gets the description_en of this CreateTableRequestBody.

        表相关描述

        :return: The description_en of this CreateTableRequestBody.
        :rtype: str
        """
        return self._description_en

    @description_en.setter
    def description_en(self, description_en):
        r"""Sets the description_en of this CreateTableRequestBody.

        表相关描述

        :param description_en: The description_en of this CreateTableRequestBody.
        :type description_en: str
        """
        self._description_en = description_en

    @property
    def description_fr(self):
        r"""Gets the description_fr of this CreateTableRequestBody.

        表相关描述

        :return: The description_fr of this CreateTableRequestBody.
        :rtype: str
        """
        return self._description_fr

    @description_fr.setter
    def description_fr(self, description_fr):
        r"""Sets the description_fr of this CreateTableRequestBody.

        表相关描述

        :param description_fr: The description_fr of this CreateTableRequestBody.
        :type description_fr: str
        """
        self._description_fr = description_fr

    @property
    def directory(self):
        r"""Gets the directory of this CreateTableRequestBody.

        目录分组

        :return: The directory of this CreateTableRequestBody.
        :rtype: str
        """
        return self._directory

    @directory.setter
    def directory(self, directory):
        r"""Sets the directory of this CreateTableRequestBody.

        目录分组

        :param directory: The directory of this CreateTableRequestBody.
        :type directory: str
        """
        self._directory = directory

    @property
    def directory_en(self):
        r"""Gets the directory_en of this CreateTableRequestBody.

        目录分组

        :return: The directory_en of this CreateTableRequestBody.
        :rtype: str
        """
        return self._directory_en

    @directory_en.setter
    def directory_en(self, directory_en):
        r"""Sets the directory_en of this CreateTableRequestBody.

        目录分组

        :param directory_en: The directory_en of this CreateTableRequestBody.
        :type directory_en: str
        """
        self._directory_en = directory_en

    @property
    def directory_fr(self):
        r"""Gets the directory_fr of this CreateTableRequestBody.

        目录分组

        :return: The directory_fr of this CreateTableRequestBody.
        :rtype: str
        """
        return self._directory_fr

    @directory_fr.setter
    def directory_fr(self, directory_fr):
        r"""Sets the directory_fr of this CreateTableRequestBody.

        目录分组

        :param directory_fr: The directory_fr of this CreateTableRequestBody.
        :type directory_fr: str
        """
        self._directory_fr = directory_fr

    @property
    def data_classification(self):
        r"""Gets the data_classification of this CreateTableRequestBody.

        **参数解释**: 数据分类 - FACTUAL_DATA 事实数据 - DIMENSION_DATA 维度数据  **约束限制** 不涉及 **取值范围**: - FACTUAL_DATA - DIMENSION_DATA  **默认值** 不涉及      

        :return: The data_classification of this CreateTableRequestBody.
        :rtype: str
        """
        return self._data_classification

    @data_classification.setter
    def data_classification(self, data_classification):
        r"""Sets the data_classification of this CreateTableRequestBody.

        **参数解释**: 数据分类 - FACTUAL_DATA 事实数据 - DIMENSION_DATA 维度数据  **约束限制** 不涉及 **取值范围**: - FACTUAL_DATA - DIMENSION_DATA  **默认值** 不涉及      

        :param data_classification: The data_classification of this CreateTableRequestBody.
        :type data_classification: str
        """
        self._data_classification = data_classification

    @property
    def schema(self):
        r"""Gets the schema of this CreateTableRequestBody.

        :return: The schema of this CreateTableRequestBody.
        :rtype: :class:`huaweicloudsdksecmaster.v2.IsapTableSchema`
        """
        return self._schema

    @schema.setter
    def schema(self, schema):
        r"""Sets the schema of this CreateTableRequestBody.

        :param schema: The schema of this CreateTableRequestBody.
        :type schema: :class:`huaweicloudsdksecmaster.v2.IsapTableSchema`
        """
        self._schema = schema

    @property
    def storage_setting(self):
        r"""Gets the storage_setting of this CreateTableRequestBody.

        :return: The storage_setting of this CreateTableRequestBody.
        :rtype: :class:`huaweicloudsdksecmaster.v2.TableStorageSetting`
        """
        return self._storage_setting

    @storage_setting.setter
    def storage_setting(self, storage_setting):
        r"""Sets the storage_setting of this CreateTableRequestBody.

        :param storage_setting: The storage_setting of this CreateTableRequestBody.
        :type storage_setting: :class:`huaweicloudsdksecmaster.v2.TableStorageSetting`
        """
        self._storage_setting = storage_setting

    @property
    def display_setting(self):
        r"""Gets the display_setting of this CreateTableRequestBody.

        :return: The display_setting of this CreateTableRequestBody.
        :rtype: :class:`huaweicloudsdksecmaster.v2.TableDisplaySetting`
        """
        return self._display_setting

    @display_setting.setter
    def display_setting(self, display_setting):
        r"""Sets the display_setting of this CreateTableRequestBody.

        :param display_setting: The display_setting of this CreateTableRequestBody.
        :type display_setting: :class:`huaweicloudsdksecmaster.v2.TableDisplaySetting`
        """
        self._display_setting = display_setting

    @property
    def create_policy(self):
        r"""Gets the create_policy of this CreateTableRequestBody.

        **参数解释**: 创建政策 - SYS_INIT_INDEX_APP_TBL 系统初始化索引应用表 - DEFAULT 默认  **约束限制** 不涉及 **取值范围**: - SYS_INIT_INDEX_APP_TBL - DEFAULT  **默认值** 不涉及            

        :return: The create_policy of this CreateTableRequestBody.
        :rtype: str
        """
        return self._create_policy

    @create_policy.setter
    def create_policy(self, create_policy):
        r"""Sets the create_policy of this CreateTableRequestBody.

        **参数解释**: 创建政策 - SYS_INIT_INDEX_APP_TBL 系统初始化索引应用表 - DEFAULT 默认  **约束限制** 不涉及 **取值范围**: - SYS_INIT_INDEX_APP_TBL - DEFAULT  **默认值** 不涉及            

        :param create_policy: The create_policy of this CreateTableRequestBody.
        :type create_policy: str
        """
        self._create_policy = create_policy

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
        if not isinstance(other, CreateTableRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
