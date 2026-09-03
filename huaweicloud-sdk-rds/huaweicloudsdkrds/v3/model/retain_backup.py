# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RetainBackup:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'id': 'str',
        'type': 'str',
        'begin_time': 'str',
        'end_time': 'str',
        'size': 'str',
        'describe': 'str',
        'backup_method': 'str',
        'tde': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'id': 'id',
        'type': 'type',
        'begin_time': 'begin_time',
        'end_time': 'end_time',
        'size': 'size',
        'describe': 'describe',
        'backup_method': 'backup_method',
        'tde': 'tde'
    }

    def __init__(self, name=None, id=None, type=None, begin_time=None, end_time=None, size=None, describe=None, backup_method=None, tde=None):
        r"""RetainBackup

        The model defined in huaweicloud sdk

        :param name: **参数解释**：  备份名字  **约束限制**  不涉及  **取值范围**  不涉及  **默认取值**  不涉及
        :type name: str
        :param id: **参数解释**：  备份ID  **约束限制**  不涉及  **取值范围**  不涉及  **默认取值**  不涉及
        :type id: str
        :param type: **参数解释**：  备份类型。Db表示自动备份、Snapshot表示手动备份  **约束限制**  不涉及  **取值范围**  Db、Snapshot  **默认取值**  不涉及
        :type type: str
        :param begin_time: **参数解释**：  备份开始时间  **约束限制**  不涉及  **取值范围**  不涉及  **默认取值**  不涉及
        :type begin_time: str
        :param end_time: **参数解释**：  备份结束时间  **约束限制**  不涉及  **取值范围**  不涉及  **默认取值**  不涉及
        :type end_time: str
        :param size: **参数解释**：  备份大小  **约束限制**  不涉及  **取值范围**  不涉及  **默认取值**  不涉及
        :type size: str
        :param describe: **参数解释**：  备份描述信息  **约束限制**  不涉及  **取值范围**  不涉及  **默认取值**  不涉及
        :type describe: str
        :param backup_method: **参数解释**：  备份方式。Physics表示物理备份、Snapshot表示快照备份  **约束限制**  不涉及  **取值范围**  Physics、Snapshot  **默认取值**  不涉及
        :type backup_method: str
        :param tde: **参数解释**：  备份是否tde加密  **约束限制**  不涉及  **取值范围**  false、true  **默认取值**  不涉及
        :type tde: bool
        """
        
        

        self._name = None
        self._id = None
        self._type = None
        self._begin_time = None
        self._end_time = None
        self._size = None
        self._describe = None
        self._backup_method = None
        self._tde = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if id is not None:
            self.id = id
        if type is not None:
            self.type = type
        if begin_time is not None:
            self.begin_time = begin_time
        if end_time is not None:
            self.end_time = end_time
        if size is not None:
            self.size = size
        if describe is not None:
            self.describe = describe
        if backup_method is not None:
            self.backup_method = backup_method
        if tde is not None:
            self.tde = tde

    @property
    def name(self):
        r"""Gets the name of this RetainBackup.

        **参数解释**：  备份名字  **约束限制**  不涉及  **取值范围**  不涉及  **默认取值**  不涉及

        :return: The name of this RetainBackup.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this RetainBackup.

        **参数解释**：  备份名字  **约束限制**  不涉及  **取值范围**  不涉及  **默认取值**  不涉及

        :param name: The name of this RetainBackup.
        :type name: str
        """
        self._name = name

    @property
    def id(self):
        r"""Gets the id of this RetainBackup.

        **参数解释**：  备份ID  **约束限制**  不涉及  **取值范围**  不涉及  **默认取值**  不涉及

        :return: The id of this RetainBackup.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this RetainBackup.

        **参数解释**：  备份ID  **约束限制**  不涉及  **取值范围**  不涉及  **默认取值**  不涉及

        :param id: The id of this RetainBackup.
        :type id: str
        """
        self._id = id

    @property
    def type(self):
        r"""Gets the type of this RetainBackup.

        **参数解释**：  备份类型。Db表示自动备份、Snapshot表示手动备份  **约束限制**  不涉及  **取值范围**  Db、Snapshot  **默认取值**  不涉及

        :return: The type of this RetainBackup.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this RetainBackup.

        **参数解释**：  备份类型。Db表示自动备份、Snapshot表示手动备份  **约束限制**  不涉及  **取值范围**  Db、Snapshot  **默认取值**  不涉及

        :param type: The type of this RetainBackup.
        :type type: str
        """
        self._type = type

    @property
    def begin_time(self):
        r"""Gets the begin_time of this RetainBackup.

        **参数解释**：  备份开始时间  **约束限制**  不涉及  **取值范围**  不涉及  **默认取值**  不涉及

        :return: The begin_time of this RetainBackup.
        :rtype: str
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        r"""Sets the begin_time of this RetainBackup.

        **参数解释**：  备份开始时间  **约束限制**  不涉及  **取值范围**  不涉及  **默认取值**  不涉及

        :param begin_time: The begin_time of this RetainBackup.
        :type begin_time: str
        """
        self._begin_time = begin_time

    @property
    def end_time(self):
        r"""Gets the end_time of this RetainBackup.

        **参数解释**：  备份结束时间  **约束限制**  不涉及  **取值范围**  不涉及  **默认取值**  不涉及

        :return: The end_time of this RetainBackup.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this RetainBackup.

        **参数解释**：  备份结束时间  **约束限制**  不涉及  **取值范围**  不涉及  **默认取值**  不涉及

        :param end_time: The end_time of this RetainBackup.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def size(self):
        r"""Gets the size of this RetainBackup.

        **参数解释**：  备份大小  **约束限制**  不涉及  **取值范围**  不涉及  **默认取值**  不涉及

        :return: The size of this RetainBackup.
        :rtype: str
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this RetainBackup.

        **参数解释**：  备份大小  **约束限制**  不涉及  **取值范围**  不涉及  **默认取值**  不涉及

        :param size: The size of this RetainBackup.
        :type size: str
        """
        self._size = size

    @property
    def describe(self):
        r"""Gets the describe of this RetainBackup.

        **参数解释**：  备份描述信息  **约束限制**  不涉及  **取值范围**  不涉及  **默认取值**  不涉及

        :return: The describe of this RetainBackup.
        :rtype: str
        """
        return self._describe

    @describe.setter
    def describe(self, describe):
        r"""Sets the describe of this RetainBackup.

        **参数解释**：  备份描述信息  **约束限制**  不涉及  **取值范围**  不涉及  **默认取值**  不涉及

        :param describe: The describe of this RetainBackup.
        :type describe: str
        """
        self._describe = describe

    @property
    def backup_method(self):
        r"""Gets the backup_method of this RetainBackup.

        **参数解释**：  备份方式。Physics表示物理备份、Snapshot表示快照备份  **约束限制**  不涉及  **取值范围**  Physics、Snapshot  **默认取值**  不涉及

        :return: The backup_method of this RetainBackup.
        :rtype: str
        """
        return self._backup_method

    @backup_method.setter
    def backup_method(self, backup_method):
        r"""Sets the backup_method of this RetainBackup.

        **参数解释**：  备份方式。Physics表示物理备份、Snapshot表示快照备份  **约束限制**  不涉及  **取值范围**  Physics、Snapshot  **默认取值**  不涉及

        :param backup_method: The backup_method of this RetainBackup.
        :type backup_method: str
        """
        self._backup_method = backup_method

    @property
    def tde(self):
        r"""Gets the tde of this RetainBackup.

        **参数解释**：  备份是否tde加密  **约束限制**  不涉及  **取值范围**  false、true  **默认取值**  不涉及

        :return: The tde of this RetainBackup.
        :rtype: bool
        """
        return self._tde

    @tde.setter
    def tde(self, tde):
        r"""Sets the tde of this RetainBackup.

        **参数解释**：  备份是否tde加密  **约束限制**  不涉及  **取值范围**  false、true  **默认取值**  不涉及

        :param tde: The tde of this RetainBackup.
        :type tde: bool
        """
        self._tde = tde

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
        if not isinstance(other, RetainBackup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
