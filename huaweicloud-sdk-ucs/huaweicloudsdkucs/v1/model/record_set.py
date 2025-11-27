# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RecordSet:

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
        'description': 'str',
        'zone_id': 'str',
        'zone_name': 'str',
        'type': 'str',
        'project_id': 'str',
        'name': 'str',
        'ttl': 'int',
        'records': 'list[str]',
        'weight': 'int',
        'line': 'str',
        'create_at': 'str',
        'update_at': 'str',
        'default': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'description': 'description',
        'zone_id': 'zone_id',
        'zone_name': 'zone_name',
        'type': 'type',
        'project_id': 'project_id',
        'name': 'name',
        'ttl': 'ttl',
        'records': 'records',
        'weight': 'weight',
        'line': 'line',
        'create_at': 'create_at',
        'update_at': 'update_at',
        'default': 'default'
    }

    def __init__(self, id=None, description=None, zone_id=None, zone_name=None, type=None, project_id=None, name=None, ttl=None, records=None, weight=None, line=None, create_at=None, update_at=None, default=None):
        r"""RecordSet

        The model defined in huaweicloud sdk

        :param id: 记录集id
        :type id: str
        :param description: 描述信息
        :type description: str
        :param zone_id: 可用区id
        :type zone_id: str
        :param zone_name: 可用区名称
        :type zone_name: str
        :param type: 记录类型
        :type type: str
        :param project_id: 项目id
        :type project_id: str
        :param name: 记录集名称
        :type name: str
        :param ttl: 生存时间
        :type ttl: int
        :param records: 记录信息
        :type records: list[str]
        :param weight: 比例
        :type weight: int
        :param line: 解析线路ID
        :type line: str
        :param create_at: 创建时间
        :type create_at: str
        :param update_at: 更新时间
        :type update_at: str
        :param default: 是否为默认记录集合
        :type default: bool
        """
        
        

        self._id = None
        self._description = None
        self._zone_id = None
        self._zone_name = None
        self._type = None
        self._project_id = None
        self._name = None
        self._ttl = None
        self._records = None
        self._weight = None
        self._line = None
        self._create_at = None
        self._update_at = None
        self._default = None
        self.discriminator = None

        self.id = id
        if description is not None:
            self.description = description
        if zone_id is not None:
            self.zone_id = zone_id
        if zone_name is not None:
            self.zone_name = zone_name
        if type is not None:
            self.type = type
        if project_id is not None:
            self.project_id = project_id
        self.name = name
        self.ttl = ttl
        self.records = records
        self.weight = weight
        self.line = line
        if create_at is not None:
            self.create_at = create_at
        if update_at is not None:
            self.update_at = update_at
        if default is not None:
            self.default = default

    @property
    def id(self):
        r"""Gets the id of this RecordSet.

        记录集id

        :return: The id of this RecordSet.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this RecordSet.

        记录集id

        :param id: The id of this RecordSet.
        :type id: str
        """
        self._id = id

    @property
    def description(self):
        r"""Gets the description of this RecordSet.

        描述信息

        :return: The description of this RecordSet.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this RecordSet.

        描述信息

        :param description: The description of this RecordSet.
        :type description: str
        """
        self._description = description

    @property
    def zone_id(self):
        r"""Gets the zone_id of this RecordSet.

        可用区id

        :return: The zone_id of this RecordSet.
        :rtype: str
        """
        return self._zone_id

    @zone_id.setter
    def zone_id(self, zone_id):
        r"""Sets the zone_id of this RecordSet.

        可用区id

        :param zone_id: The zone_id of this RecordSet.
        :type zone_id: str
        """
        self._zone_id = zone_id

    @property
    def zone_name(self):
        r"""Gets the zone_name of this RecordSet.

        可用区名称

        :return: The zone_name of this RecordSet.
        :rtype: str
        """
        return self._zone_name

    @zone_name.setter
    def zone_name(self, zone_name):
        r"""Sets the zone_name of this RecordSet.

        可用区名称

        :param zone_name: The zone_name of this RecordSet.
        :type zone_name: str
        """
        self._zone_name = zone_name

    @property
    def type(self):
        r"""Gets the type of this RecordSet.

        记录类型

        :return: The type of this RecordSet.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this RecordSet.

        记录类型

        :param type: The type of this RecordSet.
        :type type: str
        """
        self._type = type

    @property
    def project_id(self):
        r"""Gets the project_id of this RecordSet.

        项目id

        :return: The project_id of this RecordSet.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this RecordSet.

        项目id

        :param project_id: The project_id of this RecordSet.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def name(self):
        r"""Gets the name of this RecordSet.

        记录集名称

        :return: The name of this RecordSet.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this RecordSet.

        记录集名称

        :param name: The name of this RecordSet.
        :type name: str
        """
        self._name = name

    @property
    def ttl(self):
        r"""Gets the ttl of this RecordSet.

        生存时间

        :return: The ttl of this RecordSet.
        :rtype: int
        """
        return self._ttl

    @ttl.setter
    def ttl(self, ttl):
        r"""Sets the ttl of this RecordSet.

        生存时间

        :param ttl: The ttl of this RecordSet.
        :type ttl: int
        """
        self._ttl = ttl

    @property
    def records(self):
        r"""Gets the records of this RecordSet.

        记录信息

        :return: The records of this RecordSet.
        :rtype: list[str]
        """
        return self._records

    @records.setter
    def records(self, records):
        r"""Sets the records of this RecordSet.

        记录信息

        :param records: The records of this RecordSet.
        :type records: list[str]
        """
        self._records = records

    @property
    def weight(self):
        r"""Gets the weight of this RecordSet.

        比例

        :return: The weight of this RecordSet.
        :rtype: int
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        r"""Sets the weight of this RecordSet.

        比例

        :param weight: The weight of this RecordSet.
        :type weight: int
        """
        self._weight = weight

    @property
    def line(self):
        r"""Gets the line of this RecordSet.

        解析线路ID

        :return: The line of this RecordSet.
        :rtype: str
        """
        return self._line

    @line.setter
    def line(self, line):
        r"""Sets the line of this RecordSet.

        解析线路ID

        :param line: The line of this RecordSet.
        :type line: str
        """
        self._line = line

    @property
    def create_at(self):
        r"""Gets the create_at of this RecordSet.

        创建时间

        :return: The create_at of this RecordSet.
        :rtype: str
        """
        return self._create_at

    @create_at.setter
    def create_at(self, create_at):
        r"""Sets the create_at of this RecordSet.

        创建时间

        :param create_at: The create_at of this RecordSet.
        :type create_at: str
        """
        self._create_at = create_at

    @property
    def update_at(self):
        r"""Gets the update_at of this RecordSet.

        更新时间

        :return: The update_at of this RecordSet.
        :rtype: str
        """
        return self._update_at

    @update_at.setter
    def update_at(self, update_at):
        r"""Sets the update_at of this RecordSet.

        更新时间

        :param update_at: The update_at of this RecordSet.
        :type update_at: str
        """
        self._update_at = update_at

    @property
    def default(self):
        r"""Gets the default of this RecordSet.

        是否为默认记录集合

        :return: The default of this RecordSet.
        :rtype: bool
        """
        return self._default

    @default.setter
    def default(self, default):
        r"""Sets the default of this RecordSet.

        是否为默认记录集合

        :param default: The default of this RecordSet.
        :type default: bool
        """
        self._default = default

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
        if not isinstance(other, RecordSet):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
