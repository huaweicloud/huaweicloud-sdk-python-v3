# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TableMappingVO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'int',
        'name': 'str',
        'description': 'str',
        'target_table_id': 'int',
        'src_model_id': 'int',
        'src_model_name': 'str',
        'view_text': 'str',
        'target_table_name': 'str',
        'details': 'list[TableMappingDetailVO]',
        'source_tables': 'list[MappingSourceTableVO]',
        'source_fields': 'list[MappingSourceFieldVO]',
        'create_time': 'datetime',
        'update_time': 'datetime',
        'create_by': 'str',
        'update_by': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'target_table_id': 'target_table_id',
        'src_model_id': 'src_model_id',
        'src_model_name': 'src_model_name',
        'view_text': 'view_text',
        'target_table_name': 'target_table_name',
        'details': 'details',
        'source_tables': 'source_tables',
        'source_fields': 'source_fields',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'create_by': 'create_by',
        'update_by': 'update_by'
    }

    def __init__(self, id=None, name=None, description=None, target_table_id=None, src_model_id=None, src_model_name=None, view_text=None, target_table_name=None, details=None, source_tables=None, source_fields=None, create_time=None, update_time=None, create_by=None, update_by=None):
        """TableMappingVO

        The model defined in huaweicloud sdk

        :param id: 编码
        :type id: int
        :param name: 名称
        :type name: str
        :param description: 
        :type description: str
        :param target_table_id: 目的表id
        :type target_table_id: int
        :param src_model_id: 来源表所属模型id
        :type src_model_id: int
        :param src_model_name: 来源模型名称
        :type src_model_name: str
        :param view_text: 采集的视图来源，dws视图逆向使用
        :type view_text: str
        :param target_table_name: 目的表名称
        :type target_table_name: str
        :param details: 详情
        :type details: list[:class:`huaweicloudsdkdataartsstudio.v1.TableMappingDetailVO`]
        :param source_tables: 映射的表信息
        :type source_tables: list[:class:`huaweicloudsdkdataartsstudio.v1.MappingSourceTableVO`]
        :param source_fields: 映射的字段信息
        :type source_fields: list[:class:`huaweicloudsdkdataartsstudio.v1.MappingSourceFieldVO`]
        :param create_time: 创建时间
        :type create_time: datetime
        :param update_time: 更新时间
        :type update_time: datetime
        :param create_by: 创建人
        :type create_by: str
        :param update_by: 更新人
        :type update_by: str
        """
        
        

        self._id = None
        self._name = None
        self._description = None
        self._target_table_id = None
        self._src_model_id = None
        self._src_model_name = None
        self._view_text = None
        self._target_table_name = None
        self._details = None
        self._source_tables = None
        self._source_fields = None
        self._create_time = None
        self._update_time = None
        self._create_by = None
        self._update_by = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.name = name
        if description is not None:
            self.description = description
        if target_table_id is not None:
            self.target_table_id = target_table_id
        if src_model_id is not None:
            self.src_model_id = src_model_id
        if src_model_name is not None:
            self.src_model_name = src_model_name
        if view_text is not None:
            self.view_text = view_text
        if target_table_name is not None:
            self.target_table_name = target_table_name
        if details is not None:
            self.details = details
        if source_tables is not None:
            self.source_tables = source_tables
        if source_fields is not None:
            self.source_fields = source_fields
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if create_by is not None:
            self.create_by = create_by
        if update_by is not None:
            self.update_by = update_by

    @property
    def id(self):
        """Gets the id of this TableMappingVO.

        编码

        :return: The id of this TableMappingVO.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TableMappingVO.

        编码

        :param id: The id of this TableMappingVO.
        :type id: int
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this TableMappingVO.

        名称

        :return: The name of this TableMappingVO.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TableMappingVO.

        名称

        :param name: The name of this TableMappingVO.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this TableMappingVO.

        :return: The description of this TableMappingVO.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this TableMappingVO.

        :param description: The description of this TableMappingVO.
        :type description: str
        """
        self._description = description

    @property
    def target_table_id(self):
        """Gets the target_table_id of this TableMappingVO.

        目的表id

        :return: The target_table_id of this TableMappingVO.
        :rtype: int
        """
        return self._target_table_id

    @target_table_id.setter
    def target_table_id(self, target_table_id):
        """Sets the target_table_id of this TableMappingVO.

        目的表id

        :param target_table_id: The target_table_id of this TableMappingVO.
        :type target_table_id: int
        """
        self._target_table_id = target_table_id

    @property
    def src_model_id(self):
        """Gets the src_model_id of this TableMappingVO.

        来源表所属模型id

        :return: The src_model_id of this TableMappingVO.
        :rtype: int
        """
        return self._src_model_id

    @src_model_id.setter
    def src_model_id(self, src_model_id):
        """Sets the src_model_id of this TableMappingVO.

        来源表所属模型id

        :param src_model_id: The src_model_id of this TableMappingVO.
        :type src_model_id: int
        """
        self._src_model_id = src_model_id

    @property
    def src_model_name(self):
        """Gets the src_model_name of this TableMappingVO.

        来源模型名称

        :return: The src_model_name of this TableMappingVO.
        :rtype: str
        """
        return self._src_model_name

    @src_model_name.setter
    def src_model_name(self, src_model_name):
        """Sets the src_model_name of this TableMappingVO.

        来源模型名称

        :param src_model_name: The src_model_name of this TableMappingVO.
        :type src_model_name: str
        """
        self._src_model_name = src_model_name

    @property
    def view_text(self):
        """Gets the view_text of this TableMappingVO.

        采集的视图来源，dws视图逆向使用

        :return: The view_text of this TableMappingVO.
        :rtype: str
        """
        return self._view_text

    @view_text.setter
    def view_text(self, view_text):
        """Sets the view_text of this TableMappingVO.

        采集的视图来源，dws视图逆向使用

        :param view_text: The view_text of this TableMappingVO.
        :type view_text: str
        """
        self._view_text = view_text

    @property
    def target_table_name(self):
        """Gets the target_table_name of this TableMappingVO.

        目的表名称

        :return: The target_table_name of this TableMappingVO.
        :rtype: str
        """
        return self._target_table_name

    @target_table_name.setter
    def target_table_name(self, target_table_name):
        """Sets the target_table_name of this TableMappingVO.

        目的表名称

        :param target_table_name: The target_table_name of this TableMappingVO.
        :type target_table_name: str
        """
        self._target_table_name = target_table_name

    @property
    def details(self):
        """Gets the details of this TableMappingVO.

        详情

        :return: The details of this TableMappingVO.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.TableMappingDetailVO`]
        """
        return self._details

    @details.setter
    def details(self, details):
        """Sets the details of this TableMappingVO.

        详情

        :param details: The details of this TableMappingVO.
        :type details: list[:class:`huaweicloudsdkdataartsstudio.v1.TableMappingDetailVO`]
        """
        self._details = details

    @property
    def source_tables(self):
        """Gets the source_tables of this TableMappingVO.

        映射的表信息

        :return: The source_tables of this TableMappingVO.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.MappingSourceTableVO`]
        """
        return self._source_tables

    @source_tables.setter
    def source_tables(self, source_tables):
        """Sets the source_tables of this TableMappingVO.

        映射的表信息

        :param source_tables: The source_tables of this TableMappingVO.
        :type source_tables: list[:class:`huaweicloudsdkdataartsstudio.v1.MappingSourceTableVO`]
        """
        self._source_tables = source_tables

    @property
    def source_fields(self):
        """Gets the source_fields of this TableMappingVO.

        映射的字段信息

        :return: The source_fields of this TableMappingVO.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.MappingSourceFieldVO`]
        """
        return self._source_fields

    @source_fields.setter
    def source_fields(self, source_fields):
        """Sets the source_fields of this TableMappingVO.

        映射的字段信息

        :param source_fields: The source_fields of this TableMappingVO.
        :type source_fields: list[:class:`huaweicloudsdkdataartsstudio.v1.MappingSourceFieldVO`]
        """
        self._source_fields = source_fields

    @property
    def create_time(self):
        """Gets the create_time of this TableMappingVO.

        创建时间

        :return: The create_time of this TableMappingVO.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this TableMappingVO.

        创建时间

        :param create_time: The create_time of this TableMappingVO.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this TableMappingVO.

        更新时间

        :return: The update_time of this TableMappingVO.
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this TableMappingVO.

        更新时间

        :param update_time: The update_time of this TableMappingVO.
        :type update_time: datetime
        """
        self._update_time = update_time

    @property
    def create_by(self):
        """Gets the create_by of this TableMappingVO.

        创建人

        :return: The create_by of this TableMappingVO.
        :rtype: str
        """
        return self._create_by

    @create_by.setter
    def create_by(self, create_by):
        """Sets the create_by of this TableMappingVO.

        创建人

        :param create_by: The create_by of this TableMappingVO.
        :type create_by: str
        """
        self._create_by = create_by

    @property
    def update_by(self):
        """Gets the update_by of this TableMappingVO.

        更新人

        :return: The update_by of this TableMappingVO.
        :rtype: str
        """
        return self._update_by

    @update_by.setter
    def update_by(self, update_by):
        """Sets the update_by of this TableMappingVO.

        更新人

        :param update_by: The update_by of this TableMappingVO.
        :type update_by: str
        """
        self._update_by = update_by

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
        if not isinstance(other, TableMappingVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
