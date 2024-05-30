# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RelationVO:

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
        'source_table_id': 'str',
        'target_table_id': 'str',
        'name': 'str',
        'source_table_name': 'str',
        'target_table_name': 'str',
        'role': 'str',
        'tenant_id': 'str',
        'source_type': 'RelationType',
        'target_type': 'RelationType',
        'create_by': 'str',
        'update_by': 'str',
        'create_time': 'datetime',
        'update_time': 'datetime',
        'mappings': 'list[RelationMappingVO]'
    }

    attribute_map = {
        'id': 'id',
        'source_table_id': 'source_table_id',
        'target_table_id': 'target_table_id',
        'name': 'name',
        'source_table_name': 'source_table_name',
        'target_table_name': 'target_table_name',
        'role': 'role',
        'tenant_id': 'tenant_id',
        'source_type': 'source_type',
        'target_type': 'target_type',
        'create_by': 'create_by',
        'update_by': 'update_by',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'mappings': 'mappings'
    }

    def __init__(self, id=None, source_table_id=None, target_table_id=None, name=None, source_table_name=None, target_table_name=None, role=None, tenant_id=None, source_type=None, target_type=None, create_by=None, update_by=None, create_time=None, update_time=None, mappings=None):
        """RelationVO

        The model defined in huaweicloud sdk

        :param id: 编码，填写String类型替代Long类型。
        :type id: str
        :param source_table_id: 源表ID，填写String类型替代Long类型。
        :type source_table_id: str
        :param target_table_id: 目标表ID，填写String类型替代Long类型。
        :type target_table_id: str
        :param name: 关系名称。
        :type name: str
        :param source_table_name: 源表名称。
        :type source_table_name: str
        :param target_table_name: 目的表名称。
        :type target_table_name: str
        :param role: 角色。
        :type role: str
        :param tenant_id: 租户ID。
        :type tenant_id: str
        :param source_type: 
        :type source_type: :class:`huaweicloudsdkdataartsstudio.v1.RelationType`
        :param target_type: 
        :type target_type: :class:`huaweicloudsdkdataartsstudio.v1.RelationType`
        :param create_by: 创建人。
        :type create_by: str
        :param update_by: 更新人。
        :type update_by: str
        :param create_time: 创建时间，只读，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。
        :type create_time: datetime
        :param update_time: 更新时间，只读，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。
        :type update_time: datetime
        :param mappings: 表属性信息，只读。
        :type mappings: list[:class:`huaweicloudsdkdataartsstudio.v1.RelationMappingVO`]
        """
        
        

        self._id = None
        self._source_table_id = None
        self._target_table_id = None
        self._name = None
        self._source_table_name = None
        self._target_table_name = None
        self._role = None
        self._tenant_id = None
        self._source_type = None
        self._target_type = None
        self._create_by = None
        self._update_by = None
        self._create_time = None
        self._update_time = None
        self._mappings = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if source_table_id is not None:
            self.source_table_id = source_table_id
        if target_table_id is not None:
            self.target_table_id = target_table_id
        self.name = name
        if source_table_name is not None:
            self.source_table_name = source_table_name
        if target_table_name is not None:
            self.target_table_name = target_table_name
        if role is not None:
            self.role = role
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if source_type is not None:
            self.source_type = source_type
        if target_type is not None:
            self.target_type = target_type
        if create_by is not None:
            self.create_by = create_by
        if update_by is not None:
            self.update_by = update_by
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if mappings is not None:
            self.mappings = mappings

    @property
    def id(self):
        """Gets the id of this RelationVO.

        编码，填写String类型替代Long类型。

        :return: The id of this RelationVO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this RelationVO.

        编码，填写String类型替代Long类型。

        :param id: The id of this RelationVO.
        :type id: str
        """
        self._id = id

    @property
    def source_table_id(self):
        """Gets the source_table_id of this RelationVO.

        源表ID，填写String类型替代Long类型。

        :return: The source_table_id of this RelationVO.
        :rtype: str
        """
        return self._source_table_id

    @source_table_id.setter
    def source_table_id(self, source_table_id):
        """Sets the source_table_id of this RelationVO.

        源表ID，填写String类型替代Long类型。

        :param source_table_id: The source_table_id of this RelationVO.
        :type source_table_id: str
        """
        self._source_table_id = source_table_id

    @property
    def target_table_id(self):
        """Gets the target_table_id of this RelationVO.

        目标表ID，填写String类型替代Long类型。

        :return: The target_table_id of this RelationVO.
        :rtype: str
        """
        return self._target_table_id

    @target_table_id.setter
    def target_table_id(self, target_table_id):
        """Sets the target_table_id of this RelationVO.

        目标表ID，填写String类型替代Long类型。

        :param target_table_id: The target_table_id of this RelationVO.
        :type target_table_id: str
        """
        self._target_table_id = target_table_id

    @property
    def name(self):
        """Gets the name of this RelationVO.

        关系名称。

        :return: The name of this RelationVO.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RelationVO.

        关系名称。

        :param name: The name of this RelationVO.
        :type name: str
        """
        self._name = name

    @property
    def source_table_name(self):
        """Gets the source_table_name of this RelationVO.

        源表名称。

        :return: The source_table_name of this RelationVO.
        :rtype: str
        """
        return self._source_table_name

    @source_table_name.setter
    def source_table_name(self, source_table_name):
        """Sets the source_table_name of this RelationVO.

        源表名称。

        :param source_table_name: The source_table_name of this RelationVO.
        :type source_table_name: str
        """
        self._source_table_name = source_table_name

    @property
    def target_table_name(self):
        """Gets the target_table_name of this RelationVO.

        目的表名称。

        :return: The target_table_name of this RelationVO.
        :rtype: str
        """
        return self._target_table_name

    @target_table_name.setter
    def target_table_name(self, target_table_name):
        """Sets the target_table_name of this RelationVO.

        目的表名称。

        :param target_table_name: The target_table_name of this RelationVO.
        :type target_table_name: str
        """
        self._target_table_name = target_table_name

    @property
    def role(self):
        """Gets the role of this RelationVO.

        角色。

        :return: The role of this RelationVO.
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this RelationVO.

        角色。

        :param role: The role of this RelationVO.
        :type role: str
        """
        self._role = role

    @property
    def tenant_id(self):
        """Gets the tenant_id of this RelationVO.

        租户ID。

        :return: The tenant_id of this RelationVO.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this RelationVO.

        租户ID。

        :param tenant_id: The tenant_id of this RelationVO.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

    @property
    def source_type(self):
        """Gets the source_type of this RelationVO.

        :return: The source_type of this RelationVO.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.RelationType`
        """
        return self._source_type

    @source_type.setter
    def source_type(self, source_type):
        """Sets the source_type of this RelationVO.

        :param source_type: The source_type of this RelationVO.
        :type source_type: :class:`huaweicloudsdkdataartsstudio.v1.RelationType`
        """
        self._source_type = source_type

    @property
    def target_type(self):
        """Gets the target_type of this RelationVO.

        :return: The target_type of this RelationVO.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.RelationType`
        """
        return self._target_type

    @target_type.setter
    def target_type(self, target_type):
        """Sets the target_type of this RelationVO.

        :param target_type: The target_type of this RelationVO.
        :type target_type: :class:`huaweicloudsdkdataartsstudio.v1.RelationType`
        """
        self._target_type = target_type

    @property
    def create_by(self):
        """Gets the create_by of this RelationVO.

        创建人。

        :return: The create_by of this RelationVO.
        :rtype: str
        """
        return self._create_by

    @create_by.setter
    def create_by(self, create_by):
        """Sets the create_by of this RelationVO.

        创建人。

        :param create_by: The create_by of this RelationVO.
        :type create_by: str
        """
        self._create_by = create_by

    @property
    def update_by(self):
        """Gets the update_by of this RelationVO.

        更新人。

        :return: The update_by of this RelationVO.
        :rtype: str
        """
        return self._update_by

    @update_by.setter
    def update_by(self, update_by):
        """Sets the update_by of this RelationVO.

        更新人。

        :param update_by: The update_by of this RelationVO.
        :type update_by: str
        """
        self._update_by = update_by

    @property
    def create_time(self):
        """Gets the create_time of this RelationVO.

        创建时间，只读，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。

        :return: The create_time of this RelationVO.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this RelationVO.

        创建时间，只读，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。

        :param create_time: The create_time of this RelationVO.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this RelationVO.

        更新时间，只读，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。

        :return: The update_time of this RelationVO.
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this RelationVO.

        更新时间，只读，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。

        :param update_time: The update_time of this RelationVO.
        :type update_time: datetime
        """
        self._update_time = update_time

    @property
    def mappings(self):
        """Gets the mappings of this RelationVO.

        表属性信息，只读。

        :return: The mappings of this RelationVO.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.RelationMappingVO`]
        """
        return self._mappings

    @mappings.setter
    def mappings(self, mappings):
        """Sets the mappings of this RelationVO.

        表属性信息，只读。

        :param mappings: The mappings of this RelationVO.
        :type mappings: list[:class:`huaweicloudsdkdataartsstudio.v1.RelationMappingVO`]
        """
        self._mappings = mappings

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
        if not isinstance(other, RelationVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
