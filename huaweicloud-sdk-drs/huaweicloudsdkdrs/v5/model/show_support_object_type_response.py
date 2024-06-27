# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowSupportObjectTypeResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'is_full_trans_support_object': 'bool',
        'is_incre_trans_support_object': 'bool',
        'is_full_incre_trans_support_object': 'bool',
        'support_object_import_engine': 'list[str]',
        'is_support_column_mapping': 'bool',
        'is_database_support_search': 'bool',
        'is_schema_support_search': 'bool',
        'is_table_support_search': 'bool',
        'file_size': 'str',
        'previous_select': 'str',
        'import_level': 'str',
        'is_import_cloumn': 'bool'
    }

    attribute_map = {
        'is_full_trans_support_object': 'is_full_trans_support_object',
        'is_incre_trans_support_object': 'is_incre_trans_support_object',
        'is_full_incre_trans_support_object': 'is_full_incre_trans_support_object',
        'support_object_import_engine': 'support_object_import_engine',
        'is_support_column_mapping': 'is_support_column_mapping',
        'is_database_support_search': 'is_database_support_search',
        'is_schema_support_search': 'is_schema_support_search',
        'is_table_support_search': 'is_table_support_search',
        'file_size': 'file_size',
        'previous_select': 'previous_select',
        'import_level': 'import_level',
        'is_import_cloumn': 'is_import_cloumn'
    }

    def __init__(self, is_full_trans_support_object=None, is_incre_trans_support_object=None, is_full_incre_trans_support_object=None, support_object_import_engine=None, is_support_column_mapping=None, is_database_support_search=None, is_schema_support_search=None, is_table_support_search=None, file_size=None, previous_select=None, import_level=None, is_import_cloumn=None):
        """ShowSupportObjectTypeResponse

        The model defined in huaweicloud sdk

        :param is_full_trans_support_object: 全量任务是否支持对象选择。
        :type is_full_trans_support_object: bool
        :param is_incre_trans_support_object: 增量任务是否支持对象选择。
        :type is_incre_trans_support_object: bool
        :param is_full_incre_trans_support_object: 全量加增量任务是否支持对象选择。
        :type is_full_incre_trans_support_object: bool
        :param support_object_import_engine: 支持对象导入的引引擎。
        :type support_object_import_engine: list[str]
        :param is_support_column_mapping: 是否支持列映射。
        :type is_support_column_mapping: bool
        :param is_database_support_search: 库是否支持搜索。
        :type is_database_support_search: bool
        :param is_schema_support_search: schema是否支持搜索。
        :type is_schema_support_search: bool
        :param is_table_support_search: 表是否支持搜索。
        :type is_table_support_search: bool
        :param file_size: 对象导入支持的文件大小。
        :type file_size: str
        :param previous_select: 上一次选择迁移对象或者同步对象的方式。 - srcImportObject：当前任务上次选择的方式为导入方式
        :type previous_select: str
        :param import_level: 对象导入类型。 - table：表级 - database：库级
        :type import_level: str
        :param is_import_cloumn: 取值： - true： 当前任务上次选择列加工方式为导入方式 - false 或者 空：当前任务上次选择列加工方式为手动选择方式
        :type is_import_cloumn: bool
        """
        
        super(ShowSupportObjectTypeResponse, self).__init__()

        self._is_full_trans_support_object = None
        self._is_incre_trans_support_object = None
        self._is_full_incre_trans_support_object = None
        self._support_object_import_engine = None
        self._is_support_column_mapping = None
        self._is_database_support_search = None
        self._is_schema_support_search = None
        self._is_table_support_search = None
        self._file_size = None
        self._previous_select = None
        self._import_level = None
        self._is_import_cloumn = None
        self.discriminator = None

        if is_full_trans_support_object is not None:
            self.is_full_trans_support_object = is_full_trans_support_object
        if is_incre_trans_support_object is not None:
            self.is_incre_trans_support_object = is_incre_trans_support_object
        if is_full_incre_trans_support_object is not None:
            self.is_full_incre_trans_support_object = is_full_incre_trans_support_object
        if support_object_import_engine is not None:
            self.support_object_import_engine = support_object_import_engine
        if is_support_column_mapping is not None:
            self.is_support_column_mapping = is_support_column_mapping
        if is_database_support_search is not None:
            self.is_database_support_search = is_database_support_search
        if is_schema_support_search is not None:
            self.is_schema_support_search = is_schema_support_search
        if is_table_support_search is not None:
            self.is_table_support_search = is_table_support_search
        if file_size is not None:
            self.file_size = file_size
        if previous_select is not None:
            self.previous_select = previous_select
        if import_level is not None:
            self.import_level = import_level
        if is_import_cloumn is not None:
            self.is_import_cloumn = is_import_cloumn

    @property
    def is_full_trans_support_object(self):
        """Gets the is_full_trans_support_object of this ShowSupportObjectTypeResponse.

        全量任务是否支持对象选择。

        :return: The is_full_trans_support_object of this ShowSupportObjectTypeResponse.
        :rtype: bool
        """
        return self._is_full_trans_support_object

    @is_full_trans_support_object.setter
    def is_full_trans_support_object(self, is_full_trans_support_object):
        """Sets the is_full_trans_support_object of this ShowSupportObjectTypeResponse.

        全量任务是否支持对象选择。

        :param is_full_trans_support_object: The is_full_trans_support_object of this ShowSupportObjectTypeResponse.
        :type is_full_trans_support_object: bool
        """
        self._is_full_trans_support_object = is_full_trans_support_object

    @property
    def is_incre_trans_support_object(self):
        """Gets the is_incre_trans_support_object of this ShowSupportObjectTypeResponse.

        增量任务是否支持对象选择。

        :return: The is_incre_trans_support_object of this ShowSupportObjectTypeResponse.
        :rtype: bool
        """
        return self._is_incre_trans_support_object

    @is_incre_trans_support_object.setter
    def is_incre_trans_support_object(self, is_incre_trans_support_object):
        """Sets the is_incre_trans_support_object of this ShowSupportObjectTypeResponse.

        增量任务是否支持对象选择。

        :param is_incre_trans_support_object: The is_incre_trans_support_object of this ShowSupportObjectTypeResponse.
        :type is_incre_trans_support_object: bool
        """
        self._is_incre_trans_support_object = is_incre_trans_support_object

    @property
    def is_full_incre_trans_support_object(self):
        """Gets the is_full_incre_trans_support_object of this ShowSupportObjectTypeResponse.

        全量加增量任务是否支持对象选择。

        :return: The is_full_incre_trans_support_object of this ShowSupportObjectTypeResponse.
        :rtype: bool
        """
        return self._is_full_incre_trans_support_object

    @is_full_incre_trans_support_object.setter
    def is_full_incre_trans_support_object(self, is_full_incre_trans_support_object):
        """Sets the is_full_incre_trans_support_object of this ShowSupportObjectTypeResponse.

        全量加增量任务是否支持对象选择。

        :param is_full_incre_trans_support_object: The is_full_incre_trans_support_object of this ShowSupportObjectTypeResponse.
        :type is_full_incre_trans_support_object: bool
        """
        self._is_full_incre_trans_support_object = is_full_incre_trans_support_object

    @property
    def support_object_import_engine(self):
        """Gets the support_object_import_engine of this ShowSupportObjectTypeResponse.

        支持对象导入的引引擎。

        :return: The support_object_import_engine of this ShowSupportObjectTypeResponse.
        :rtype: list[str]
        """
        return self._support_object_import_engine

    @support_object_import_engine.setter
    def support_object_import_engine(self, support_object_import_engine):
        """Sets the support_object_import_engine of this ShowSupportObjectTypeResponse.

        支持对象导入的引引擎。

        :param support_object_import_engine: The support_object_import_engine of this ShowSupportObjectTypeResponse.
        :type support_object_import_engine: list[str]
        """
        self._support_object_import_engine = support_object_import_engine

    @property
    def is_support_column_mapping(self):
        """Gets the is_support_column_mapping of this ShowSupportObjectTypeResponse.

        是否支持列映射。

        :return: The is_support_column_mapping of this ShowSupportObjectTypeResponse.
        :rtype: bool
        """
        return self._is_support_column_mapping

    @is_support_column_mapping.setter
    def is_support_column_mapping(self, is_support_column_mapping):
        """Sets the is_support_column_mapping of this ShowSupportObjectTypeResponse.

        是否支持列映射。

        :param is_support_column_mapping: The is_support_column_mapping of this ShowSupportObjectTypeResponse.
        :type is_support_column_mapping: bool
        """
        self._is_support_column_mapping = is_support_column_mapping

    @property
    def is_database_support_search(self):
        """Gets the is_database_support_search of this ShowSupportObjectTypeResponse.

        库是否支持搜索。

        :return: The is_database_support_search of this ShowSupportObjectTypeResponse.
        :rtype: bool
        """
        return self._is_database_support_search

    @is_database_support_search.setter
    def is_database_support_search(self, is_database_support_search):
        """Sets the is_database_support_search of this ShowSupportObjectTypeResponse.

        库是否支持搜索。

        :param is_database_support_search: The is_database_support_search of this ShowSupportObjectTypeResponse.
        :type is_database_support_search: bool
        """
        self._is_database_support_search = is_database_support_search

    @property
    def is_schema_support_search(self):
        """Gets the is_schema_support_search of this ShowSupportObjectTypeResponse.

        schema是否支持搜索。

        :return: The is_schema_support_search of this ShowSupportObjectTypeResponse.
        :rtype: bool
        """
        return self._is_schema_support_search

    @is_schema_support_search.setter
    def is_schema_support_search(self, is_schema_support_search):
        """Sets the is_schema_support_search of this ShowSupportObjectTypeResponse.

        schema是否支持搜索。

        :param is_schema_support_search: The is_schema_support_search of this ShowSupportObjectTypeResponse.
        :type is_schema_support_search: bool
        """
        self._is_schema_support_search = is_schema_support_search

    @property
    def is_table_support_search(self):
        """Gets the is_table_support_search of this ShowSupportObjectTypeResponse.

        表是否支持搜索。

        :return: The is_table_support_search of this ShowSupportObjectTypeResponse.
        :rtype: bool
        """
        return self._is_table_support_search

    @is_table_support_search.setter
    def is_table_support_search(self, is_table_support_search):
        """Sets the is_table_support_search of this ShowSupportObjectTypeResponse.

        表是否支持搜索。

        :param is_table_support_search: The is_table_support_search of this ShowSupportObjectTypeResponse.
        :type is_table_support_search: bool
        """
        self._is_table_support_search = is_table_support_search

    @property
    def file_size(self):
        """Gets the file_size of this ShowSupportObjectTypeResponse.

        对象导入支持的文件大小。

        :return: The file_size of this ShowSupportObjectTypeResponse.
        :rtype: str
        """
        return self._file_size

    @file_size.setter
    def file_size(self, file_size):
        """Sets the file_size of this ShowSupportObjectTypeResponse.

        对象导入支持的文件大小。

        :param file_size: The file_size of this ShowSupportObjectTypeResponse.
        :type file_size: str
        """
        self._file_size = file_size

    @property
    def previous_select(self):
        """Gets the previous_select of this ShowSupportObjectTypeResponse.

        上一次选择迁移对象或者同步对象的方式。 - srcImportObject：当前任务上次选择的方式为导入方式

        :return: The previous_select of this ShowSupportObjectTypeResponse.
        :rtype: str
        """
        return self._previous_select

    @previous_select.setter
    def previous_select(self, previous_select):
        """Sets the previous_select of this ShowSupportObjectTypeResponse.

        上一次选择迁移对象或者同步对象的方式。 - srcImportObject：当前任务上次选择的方式为导入方式

        :param previous_select: The previous_select of this ShowSupportObjectTypeResponse.
        :type previous_select: str
        """
        self._previous_select = previous_select

    @property
    def import_level(self):
        """Gets the import_level of this ShowSupportObjectTypeResponse.

        对象导入类型。 - table：表级 - database：库级

        :return: The import_level of this ShowSupportObjectTypeResponse.
        :rtype: str
        """
        return self._import_level

    @import_level.setter
    def import_level(self, import_level):
        """Sets the import_level of this ShowSupportObjectTypeResponse.

        对象导入类型。 - table：表级 - database：库级

        :param import_level: The import_level of this ShowSupportObjectTypeResponse.
        :type import_level: str
        """
        self._import_level = import_level

    @property
    def is_import_cloumn(self):
        """Gets the is_import_cloumn of this ShowSupportObjectTypeResponse.

        取值： - true： 当前任务上次选择列加工方式为导入方式 - false 或者 空：当前任务上次选择列加工方式为手动选择方式

        :return: The is_import_cloumn of this ShowSupportObjectTypeResponse.
        :rtype: bool
        """
        return self._is_import_cloumn

    @is_import_cloumn.setter
    def is_import_cloumn(self, is_import_cloumn):
        """Sets the is_import_cloumn of this ShowSupportObjectTypeResponse.

        取值： - true： 当前任务上次选择列加工方式为导入方式 - false 或者 空：当前任务上次选择列加工方式为手动选择方式

        :param is_import_cloumn: The is_import_cloumn of this ShowSupportObjectTypeResponse.
        :type is_import_cloumn: bool
        """
        self._is_import_cloumn = is_import_cloumn

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
        if not isinstance(other, ShowSupportObjectTypeResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
