# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TableMappingDetailVO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'mapping_id': 'str',
        'target_attr_id': 'str',
        'target_attr_name': 'str',
        'src_table_ids': 'str',
        'src_table_names': 'list[str]',
        'src_table_db_names': 'list[str]',
        'src_table_model_ids': 'list[str]',
        'src_table_id_list': 'list[str]',
        'src_attr_ids': 'str',
        'src_attr_names': 'list[str]',
        'src_attr_id_list': 'list[str]',
        'remark': 'str',
        'create_time': 'datetime',
        'update_time': 'datetime',
        'create_by': 'str',
        'update_by': 'str',
        'target_attr': 'object'
    }

    attribute_map = {
        'id': 'id',
        'mapping_id': 'mapping_id',
        'target_attr_id': 'target_attr_id',
        'target_attr_name': 'target_attr_name',
        'src_table_ids': 'src_table_ids',
        'src_table_names': 'src_table_names',
        'src_table_db_names': 'src_table_db_names',
        'src_table_model_ids': 'src_table_model_ids',
        'src_table_id_list': 'src_table_id_list',
        'src_attr_ids': 'src_attr_ids',
        'src_attr_names': 'src_attr_names',
        'src_attr_id_list': 'src_attr_id_list',
        'remark': 'remark',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'create_by': 'create_by',
        'update_by': 'update_by',
        'target_attr': 'target_attr'
    }

    def __init__(self, id=None, mapping_id=None, target_attr_id=None, target_attr_name=None, src_table_ids=None, src_table_names=None, src_table_db_names=None, src_table_model_ids=None, src_table_id_list=None, src_attr_ids=None, src_attr_names=None, src_attr_id_list=None, remark=None, create_time=None, update_time=None, create_by=None, update_by=None, target_attr=None):
        r"""TableMappingDetailVO

        The model defined in huaweicloud sdk

        :param id: 编码，ID字符串。
        :type id: str
        :param mapping_id: 名称。
        :type mapping_id: str
        :param target_attr_id: 目的字段ID，ID字符串。
        :type target_attr_id: str
        :param target_attr_name: 目的字段排序。
        :type target_attr_name: str
        :param src_table_ids: 源表ID。
        :type src_table_ids: str
        :param src_table_names: 源表名称数组，只读。
        :type src_table_names: list[str]
        :param src_table_db_names: 源表db名称数组，只读。
        :type src_table_db_names: list[str]
        :param src_table_model_ids: 源表在关系建模中的模型ID数组，只读，ID字符串。
        :type src_table_model_ids: list[str]
        :param src_table_id_list: 源表ID数组，只读，ID字符串。
        :type src_table_id_list: list[str]
        :param src_attr_ids: 源表字段ID。
        :type src_attr_ids: str
        :param src_attr_names: 源表字段名称数组，只读。
        :type src_attr_names: list[str]
        :param src_attr_id_list: 源表字段ID数组，只读，ID字符串。
        :type src_attr_id_list: list[str]
        :param remark: 备注。
        :type remark: str
        :param create_time: 创建时间，只读，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。
        :type create_time: datetime
        :param update_time: 更新时间，只读，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。
        :type update_time: datetime
        :param create_by: 创建人。
        :type create_by: str
        :param update_by: 更新人。
        :type update_by: str
        :param target_attr: 目标属性。
        :type target_attr: object
        """
        
        

        self._id = None
        self._mapping_id = None
        self._target_attr_id = None
        self._target_attr_name = None
        self._src_table_ids = None
        self._src_table_names = None
        self._src_table_db_names = None
        self._src_table_model_ids = None
        self._src_table_id_list = None
        self._src_attr_ids = None
        self._src_attr_names = None
        self._src_attr_id_list = None
        self._remark = None
        self._create_time = None
        self._update_time = None
        self._create_by = None
        self._update_by = None
        self._target_attr = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if mapping_id is not None:
            self.mapping_id = mapping_id
        if target_attr_id is not None:
            self.target_attr_id = target_attr_id
        self.target_attr_name = target_attr_name
        if src_table_ids is not None:
            self.src_table_ids = src_table_ids
        if src_table_names is not None:
            self.src_table_names = src_table_names
        if src_table_db_names is not None:
            self.src_table_db_names = src_table_db_names
        if src_table_model_ids is not None:
            self.src_table_model_ids = src_table_model_ids
        if src_table_id_list is not None:
            self.src_table_id_list = src_table_id_list
        if src_attr_ids is not None:
            self.src_attr_ids = src_attr_ids
        if src_attr_names is not None:
            self.src_attr_names = src_attr_names
        if src_attr_id_list is not None:
            self.src_attr_id_list = src_attr_id_list
        if remark is not None:
            self.remark = remark
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if create_by is not None:
            self.create_by = create_by
        if update_by is not None:
            self.update_by = update_by
        if target_attr is not None:
            self.target_attr = target_attr

    @property
    def id(self):
        r"""Gets the id of this TableMappingDetailVO.

        编码，ID字符串。

        :return: The id of this TableMappingDetailVO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this TableMappingDetailVO.

        编码，ID字符串。

        :param id: The id of this TableMappingDetailVO.
        :type id: str
        """
        self._id = id

    @property
    def mapping_id(self):
        r"""Gets the mapping_id of this TableMappingDetailVO.

        名称。

        :return: The mapping_id of this TableMappingDetailVO.
        :rtype: str
        """
        return self._mapping_id

    @mapping_id.setter
    def mapping_id(self, mapping_id):
        r"""Sets the mapping_id of this TableMappingDetailVO.

        名称。

        :param mapping_id: The mapping_id of this TableMappingDetailVO.
        :type mapping_id: str
        """
        self._mapping_id = mapping_id

    @property
    def target_attr_id(self):
        r"""Gets the target_attr_id of this TableMappingDetailVO.

        目的字段ID，ID字符串。

        :return: The target_attr_id of this TableMappingDetailVO.
        :rtype: str
        """
        return self._target_attr_id

    @target_attr_id.setter
    def target_attr_id(self, target_attr_id):
        r"""Sets the target_attr_id of this TableMappingDetailVO.

        目的字段ID，ID字符串。

        :param target_attr_id: The target_attr_id of this TableMappingDetailVO.
        :type target_attr_id: str
        """
        self._target_attr_id = target_attr_id

    @property
    def target_attr_name(self):
        r"""Gets the target_attr_name of this TableMappingDetailVO.

        目的字段排序。

        :return: The target_attr_name of this TableMappingDetailVO.
        :rtype: str
        """
        return self._target_attr_name

    @target_attr_name.setter
    def target_attr_name(self, target_attr_name):
        r"""Sets the target_attr_name of this TableMappingDetailVO.

        目的字段排序。

        :param target_attr_name: The target_attr_name of this TableMappingDetailVO.
        :type target_attr_name: str
        """
        self._target_attr_name = target_attr_name

    @property
    def src_table_ids(self):
        r"""Gets the src_table_ids of this TableMappingDetailVO.

        源表ID。

        :return: The src_table_ids of this TableMappingDetailVO.
        :rtype: str
        """
        return self._src_table_ids

    @src_table_ids.setter
    def src_table_ids(self, src_table_ids):
        r"""Sets the src_table_ids of this TableMappingDetailVO.

        源表ID。

        :param src_table_ids: The src_table_ids of this TableMappingDetailVO.
        :type src_table_ids: str
        """
        self._src_table_ids = src_table_ids

    @property
    def src_table_names(self):
        r"""Gets the src_table_names of this TableMappingDetailVO.

        源表名称数组，只读。

        :return: The src_table_names of this TableMappingDetailVO.
        :rtype: list[str]
        """
        return self._src_table_names

    @src_table_names.setter
    def src_table_names(self, src_table_names):
        r"""Sets the src_table_names of this TableMappingDetailVO.

        源表名称数组，只读。

        :param src_table_names: The src_table_names of this TableMappingDetailVO.
        :type src_table_names: list[str]
        """
        self._src_table_names = src_table_names

    @property
    def src_table_db_names(self):
        r"""Gets the src_table_db_names of this TableMappingDetailVO.

        源表db名称数组，只读。

        :return: The src_table_db_names of this TableMappingDetailVO.
        :rtype: list[str]
        """
        return self._src_table_db_names

    @src_table_db_names.setter
    def src_table_db_names(self, src_table_db_names):
        r"""Sets the src_table_db_names of this TableMappingDetailVO.

        源表db名称数组，只读。

        :param src_table_db_names: The src_table_db_names of this TableMappingDetailVO.
        :type src_table_db_names: list[str]
        """
        self._src_table_db_names = src_table_db_names

    @property
    def src_table_model_ids(self):
        r"""Gets the src_table_model_ids of this TableMappingDetailVO.

        源表在关系建模中的模型ID数组，只读，ID字符串。

        :return: The src_table_model_ids of this TableMappingDetailVO.
        :rtype: list[str]
        """
        return self._src_table_model_ids

    @src_table_model_ids.setter
    def src_table_model_ids(self, src_table_model_ids):
        r"""Sets the src_table_model_ids of this TableMappingDetailVO.

        源表在关系建模中的模型ID数组，只读，ID字符串。

        :param src_table_model_ids: The src_table_model_ids of this TableMappingDetailVO.
        :type src_table_model_ids: list[str]
        """
        self._src_table_model_ids = src_table_model_ids

    @property
    def src_table_id_list(self):
        r"""Gets the src_table_id_list of this TableMappingDetailVO.

        源表ID数组，只读，ID字符串。

        :return: The src_table_id_list of this TableMappingDetailVO.
        :rtype: list[str]
        """
        return self._src_table_id_list

    @src_table_id_list.setter
    def src_table_id_list(self, src_table_id_list):
        r"""Sets the src_table_id_list of this TableMappingDetailVO.

        源表ID数组，只读，ID字符串。

        :param src_table_id_list: The src_table_id_list of this TableMappingDetailVO.
        :type src_table_id_list: list[str]
        """
        self._src_table_id_list = src_table_id_list

    @property
    def src_attr_ids(self):
        r"""Gets the src_attr_ids of this TableMappingDetailVO.

        源表字段ID。

        :return: The src_attr_ids of this TableMappingDetailVO.
        :rtype: str
        """
        return self._src_attr_ids

    @src_attr_ids.setter
    def src_attr_ids(self, src_attr_ids):
        r"""Sets the src_attr_ids of this TableMappingDetailVO.

        源表字段ID。

        :param src_attr_ids: The src_attr_ids of this TableMappingDetailVO.
        :type src_attr_ids: str
        """
        self._src_attr_ids = src_attr_ids

    @property
    def src_attr_names(self):
        r"""Gets the src_attr_names of this TableMappingDetailVO.

        源表字段名称数组，只读。

        :return: The src_attr_names of this TableMappingDetailVO.
        :rtype: list[str]
        """
        return self._src_attr_names

    @src_attr_names.setter
    def src_attr_names(self, src_attr_names):
        r"""Sets the src_attr_names of this TableMappingDetailVO.

        源表字段名称数组，只读。

        :param src_attr_names: The src_attr_names of this TableMappingDetailVO.
        :type src_attr_names: list[str]
        """
        self._src_attr_names = src_attr_names

    @property
    def src_attr_id_list(self):
        r"""Gets the src_attr_id_list of this TableMappingDetailVO.

        源表字段ID数组，只读，ID字符串。

        :return: The src_attr_id_list of this TableMappingDetailVO.
        :rtype: list[str]
        """
        return self._src_attr_id_list

    @src_attr_id_list.setter
    def src_attr_id_list(self, src_attr_id_list):
        r"""Sets the src_attr_id_list of this TableMappingDetailVO.

        源表字段ID数组，只读，ID字符串。

        :param src_attr_id_list: The src_attr_id_list of this TableMappingDetailVO.
        :type src_attr_id_list: list[str]
        """
        self._src_attr_id_list = src_attr_id_list

    @property
    def remark(self):
        r"""Gets the remark of this TableMappingDetailVO.

        备注。

        :return: The remark of this TableMappingDetailVO.
        :rtype: str
        """
        return self._remark

    @remark.setter
    def remark(self, remark):
        r"""Sets the remark of this TableMappingDetailVO.

        备注。

        :param remark: The remark of this TableMappingDetailVO.
        :type remark: str
        """
        self._remark = remark

    @property
    def create_time(self):
        r"""Gets the create_time of this TableMappingDetailVO.

        创建时间，只读，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。

        :return: The create_time of this TableMappingDetailVO.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this TableMappingDetailVO.

        创建时间，只读，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。

        :param create_time: The create_time of this TableMappingDetailVO.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this TableMappingDetailVO.

        更新时间，只读，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。

        :return: The update_time of this TableMappingDetailVO.
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this TableMappingDetailVO.

        更新时间，只读，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。

        :param update_time: The update_time of this TableMappingDetailVO.
        :type update_time: datetime
        """
        self._update_time = update_time

    @property
    def create_by(self):
        r"""Gets the create_by of this TableMappingDetailVO.

        创建人。

        :return: The create_by of this TableMappingDetailVO.
        :rtype: str
        """
        return self._create_by

    @create_by.setter
    def create_by(self, create_by):
        r"""Sets the create_by of this TableMappingDetailVO.

        创建人。

        :param create_by: The create_by of this TableMappingDetailVO.
        :type create_by: str
        """
        self._create_by = create_by

    @property
    def update_by(self):
        r"""Gets the update_by of this TableMappingDetailVO.

        更新人。

        :return: The update_by of this TableMappingDetailVO.
        :rtype: str
        """
        return self._update_by

    @update_by.setter
    def update_by(self, update_by):
        r"""Sets the update_by of this TableMappingDetailVO.

        更新人。

        :param update_by: The update_by of this TableMappingDetailVO.
        :type update_by: str
        """
        self._update_by = update_by

    @property
    def target_attr(self):
        r"""Gets the target_attr of this TableMappingDetailVO.

        目标属性。

        :return: The target_attr of this TableMappingDetailVO.
        :rtype: object
        """
        return self._target_attr

    @target_attr.setter
    def target_attr(self, target_attr):
        r"""Sets the target_attr of this TableMappingDetailVO.

        目标属性。

        :param target_attr: The target_attr of this TableMappingDetailVO.
        :type target_attr: object
        """
        self._target_attr = target_attr

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
        if not isinstance(other, TableMappingDetailVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
