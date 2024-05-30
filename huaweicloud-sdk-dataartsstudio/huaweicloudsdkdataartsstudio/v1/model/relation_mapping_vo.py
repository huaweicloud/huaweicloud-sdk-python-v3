# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RelationMappingVO:

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
        'relation_id': 'str',
        'source_field_id': 'str',
        'target_field_id': 'str',
        'source_field_name': 'str',
        'target_field_name': 'str',
        'create_by': 'str',
        'update_by': 'str',
        'create_time': 'datetime',
        'update_time': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'relation_id': 'relation_id',
        'source_field_id': 'source_field_id',
        'target_field_id': 'target_field_id',
        'source_field_name': 'source_field_name',
        'target_field_name': 'target_field_name',
        'create_by': 'create_by',
        'update_by': 'update_by',
        'create_time': 'create_time',
        'update_time': 'update_time'
    }

    def __init__(self, id=None, relation_id=None, source_field_id=None, target_field_id=None, source_field_name=None, target_field_name=None, create_by=None, update_by=None, create_time=None, update_time=None):
        """RelationMappingVO

        The model defined in huaweicloud sdk

        :param id: 编码，填写String类型替代Long类型。
        :type id: str
        :param relation_id: 关系ID，填写String类型替代Long类型。
        :type relation_id: str
        :param source_field_id: 源字段ID，填写String类型替代Long类型。
        :type source_field_id: str
        :param target_field_id: 目标字段ID，填写String类型替代Long类型。
        :type target_field_id: str
        :param source_field_name: 源表名称。
        :type source_field_name: str
        :param target_field_name: 目的表名称。
        :type target_field_name: str
        :param create_by: 创建人。
        :type create_by: str
        :param update_by: 更新人。
        :type update_by: str
        :param create_time: 创建时间，只读，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。
        :type create_time: datetime
        :param update_time: 更新时间，只读，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。
        :type update_time: datetime
        """
        
        

        self._id = None
        self._relation_id = None
        self._source_field_id = None
        self._target_field_id = None
        self._source_field_name = None
        self._target_field_name = None
        self._create_by = None
        self._update_by = None
        self._create_time = None
        self._update_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if relation_id is not None:
            self.relation_id = relation_id
        if source_field_id is not None:
            self.source_field_id = source_field_id
        if target_field_id is not None:
            self.target_field_id = target_field_id
        if source_field_name is not None:
            self.source_field_name = source_field_name
        if target_field_name is not None:
            self.target_field_name = target_field_name
        if create_by is not None:
            self.create_by = create_by
        if update_by is not None:
            self.update_by = update_by
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time

    @property
    def id(self):
        """Gets the id of this RelationMappingVO.

        编码，填写String类型替代Long类型。

        :return: The id of this RelationMappingVO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this RelationMappingVO.

        编码，填写String类型替代Long类型。

        :param id: The id of this RelationMappingVO.
        :type id: str
        """
        self._id = id

    @property
    def relation_id(self):
        """Gets the relation_id of this RelationMappingVO.

        关系ID，填写String类型替代Long类型。

        :return: The relation_id of this RelationMappingVO.
        :rtype: str
        """
        return self._relation_id

    @relation_id.setter
    def relation_id(self, relation_id):
        """Sets the relation_id of this RelationMappingVO.

        关系ID，填写String类型替代Long类型。

        :param relation_id: The relation_id of this RelationMappingVO.
        :type relation_id: str
        """
        self._relation_id = relation_id

    @property
    def source_field_id(self):
        """Gets the source_field_id of this RelationMappingVO.

        源字段ID，填写String类型替代Long类型。

        :return: The source_field_id of this RelationMappingVO.
        :rtype: str
        """
        return self._source_field_id

    @source_field_id.setter
    def source_field_id(self, source_field_id):
        """Sets the source_field_id of this RelationMappingVO.

        源字段ID，填写String类型替代Long类型。

        :param source_field_id: The source_field_id of this RelationMappingVO.
        :type source_field_id: str
        """
        self._source_field_id = source_field_id

    @property
    def target_field_id(self):
        """Gets the target_field_id of this RelationMappingVO.

        目标字段ID，填写String类型替代Long类型。

        :return: The target_field_id of this RelationMappingVO.
        :rtype: str
        """
        return self._target_field_id

    @target_field_id.setter
    def target_field_id(self, target_field_id):
        """Sets the target_field_id of this RelationMappingVO.

        目标字段ID，填写String类型替代Long类型。

        :param target_field_id: The target_field_id of this RelationMappingVO.
        :type target_field_id: str
        """
        self._target_field_id = target_field_id

    @property
    def source_field_name(self):
        """Gets the source_field_name of this RelationMappingVO.

        源表名称。

        :return: The source_field_name of this RelationMappingVO.
        :rtype: str
        """
        return self._source_field_name

    @source_field_name.setter
    def source_field_name(self, source_field_name):
        """Sets the source_field_name of this RelationMappingVO.

        源表名称。

        :param source_field_name: The source_field_name of this RelationMappingVO.
        :type source_field_name: str
        """
        self._source_field_name = source_field_name

    @property
    def target_field_name(self):
        """Gets the target_field_name of this RelationMappingVO.

        目的表名称。

        :return: The target_field_name of this RelationMappingVO.
        :rtype: str
        """
        return self._target_field_name

    @target_field_name.setter
    def target_field_name(self, target_field_name):
        """Sets the target_field_name of this RelationMappingVO.

        目的表名称。

        :param target_field_name: The target_field_name of this RelationMappingVO.
        :type target_field_name: str
        """
        self._target_field_name = target_field_name

    @property
    def create_by(self):
        """Gets the create_by of this RelationMappingVO.

        创建人。

        :return: The create_by of this RelationMappingVO.
        :rtype: str
        """
        return self._create_by

    @create_by.setter
    def create_by(self, create_by):
        """Sets the create_by of this RelationMappingVO.

        创建人。

        :param create_by: The create_by of this RelationMappingVO.
        :type create_by: str
        """
        self._create_by = create_by

    @property
    def update_by(self):
        """Gets the update_by of this RelationMappingVO.

        更新人。

        :return: The update_by of this RelationMappingVO.
        :rtype: str
        """
        return self._update_by

    @update_by.setter
    def update_by(self, update_by):
        """Sets the update_by of this RelationMappingVO.

        更新人。

        :param update_by: The update_by of this RelationMappingVO.
        :type update_by: str
        """
        self._update_by = update_by

    @property
    def create_time(self):
        """Gets the create_time of this RelationMappingVO.

        创建时间，只读，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。

        :return: The create_time of this RelationMappingVO.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this RelationMappingVO.

        创建时间，只读，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。

        :param create_time: The create_time of this RelationMappingVO.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this RelationMappingVO.

        更新时间，只读，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。

        :return: The update_time of this RelationMappingVO.
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this RelationMappingVO.

        更新时间，只读，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。

        :param update_time: The update_time of this RelationMappingVO.
        :type update_time: datetime
        """
        self._update_time = update_time

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
        if not isinstance(other, RelationMappingVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
