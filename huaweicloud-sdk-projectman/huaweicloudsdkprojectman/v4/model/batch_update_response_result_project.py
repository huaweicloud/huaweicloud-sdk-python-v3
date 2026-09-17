# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchUpdateResponseResultProject:

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
        'identifier': 'str',
        'total': 'int',
        'close': 'int',
        'role': 'int',
        'type': 'str',
        'archive': 'bool',
        'mem_count': 'int'
    }

    attribute_map = {
        'id': 'id',
        'identifier': 'identifier',
        'total': 'total',
        'close': 'close',
        'role': 'role',
        'type': 'type',
        'archive': 'archive',
        'mem_count': 'mem_count'
    }

    def __init__(self, id=None, identifier=None, total=None, close=None, role=None, type=None, archive=None, mem_count=None):
        r"""BatchUpdateResponseResultProject

        The model defined in huaweicloud sdk

        :param id: **参数解释：** 项目数字id。 **取值范围：** 不涉及。
        :type id: int
        :param identifier: **参数解释：** 项目uuid。 **取值范围：** 不涉及。
        :type identifier: str
        :param total: **参数解释：** 批量编辑工作项的总数。 **取值范围：** 不涉及。
        :type total: int
        :param close: **参数解释：** 项目是否关闭。 **取值范围：** 0（打开） 1（关闭）
        :type close: int
        :param role: **参数解释：** 批量编辑数量。 **取值范围：** 不涉及。
        :type role: int
        :param type: **参数解释：** 工作项类型。 **取值范围：** scrum。
        :type type: str
        :param archive: **参数解释：** 工作项是否归档。 **取值范围：** true(归档) false(未归档)
        :type archive: bool
        :param mem_count: **参数解释：** 项目数量。 **取值范围：** 不涉及。
        :type mem_count: int
        """
        
        

        self._id = None
        self._identifier = None
        self._total = None
        self._close = None
        self._role = None
        self._type = None
        self._archive = None
        self._mem_count = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if identifier is not None:
            self.identifier = identifier
        if total is not None:
            self.total = total
        if close is not None:
            self.close = close
        if role is not None:
            self.role = role
        if type is not None:
            self.type = type
        if archive is not None:
            self.archive = archive
        if mem_count is not None:
            self.mem_count = mem_count

    @property
    def id(self):
        r"""Gets the id of this BatchUpdateResponseResultProject.

        **参数解释：** 项目数字id。 **取值范围：** 不涉及。

        :return: The id of this BatchUpdateResponseResultProject.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this BatchUpdateResponseResultProject.

        **参数解释：** 项目数字id。 **取值范围：** 不涉及。

        :param id: The id of this BatchUpdateResponseResultProject.
        :type id: int
        """
        self._id = id

    @property
    def identifier(self):
        r"""Gets the identifier of this BatchUpdateResponseResultProject.

        **参数解释：** 项目uuid。 **取值范围：** 不涉及。

        :return: The identifier of this BatchUpdateResponseResultProject.
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        r"""Sets the identifier of this BatchUpdateResponseResultProject.

        **参数解释：** 项目uuid。 **取值范围：** 不涉及。

        :param identifier: The identifier of this BatchUpdateResponseResultProject.
        :type identifier: str
        """
        self._identifier = identifier

    @property
    def total(self):
        r"""Gets the total of this BatchUpdateResponseResultProject.

        **参数解释：** 批量编辑工作项的总数。 **取值范围：** 不涉及。

        :return: The total of this BatchUpdateResponseResultProject.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this BatchUpdateResponseResultProject.

        **参数解释：** 批量编辑工作项的总数。 **取值范围：** 不涉及。

        :param total: The total of this BatchUpdateResponseResultProject.
        :type total: int
        """
        self._total = total

    @property
    def close(self):
        r"""Gets the close of this BatchUpdateResponseResultProject.

        **参数解释：** 项目是否关闭。 **取值范围：** 0（打开） 1（关闭）

        :return: The close of this BatchUpdateResponseResultProject.
        :rtype: int
        """
        return self._close

    @close.setter
    def close(self, close):
        r"""Sets the close of this BatchUpdateResponseResultProject.

        **参数解释：** 项目是否关闭。 **取值范围：** 0（打开） 1（关闭）

        :param close: The close of this BatchUpdateResponseResultProject.
        :type close: int
        """
        self._close = close

    @property
    def role(self):
        r"""Gets the role of this BatchUpdateResponseResultProject.

        **参数解释：** 批量编辑数量。 **取值范围：** 不涉及。

        :return: The role of this BatchUpdateResponseResultProject.
        :rtype: int
        """
        return self._role

    @role.setter
    def role(self, role):
        r"""Sets the role of this BatchUpdateResponseResultProject.

        **参数解释：** 批量编辑数量。 **取值范围：** 不涉及。

        :param role: The role of this BatchUpdateResponseResultProject.
        :type role: int
        """
        self._role = role

    @property
    def type(self):
        r"""Gets the type of this BatchUpdateResponseResultProject.

        **参数解释：** 工作项类型。 **取值范围：** scrum。

        :return: The type of this BatchUpdateResponseResultProject.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this BatchUpdateResponseResultProject.

        **参数解释：** 工作项类型。 **取值范围：** scrum。

        :param type: The type of this BatchUpdateResponseResultProject.
        :type type: str
        """
        self._type = type

    @property
    def archive(self):
        r"""Gets the archive of this BatchUpdateResponseResultProject.

        **参数解释：** 工作项是否归档。 **取值范围：** true(归档) false(未归档)

        :return: The archive of this BatchUpdateResponseResultProject.
        :rtype: bool
        """
        return self._archive

    @archive.setter
    def archive(self, archive):
        r"""Sets the archive of this BatchUpdateResponseResultProject.

        **参数解释：** 工作项是否归档。 **取值范围：** true(归档) false(未归档)

        :param archive: The archive of this BatchUpdateResponseResultProject.
        :type archive: bool
        """
        self._archive = archive

    @property
    def mem_count(self):
        r"""Gets the mem_count of this BatchUpdateResponseResultProject.

        **参数解释：** 项目数量。 **取值范围：** 不涉及。

        :return: The mem_count of this BatchUpdateResponseResultProject.
        :rtype: int
        """
        return self._mem_count

    @mem_count.setter
    def mem_count(self, mem_count):
        r"""Sets the mem_count of this BatchUpdateResponseResultProject.

        **参数解释：** 项目数量。 **取值范围：** 不涉及。

        :param mem_count: The mem_count of this BatchUpdateResponseResultProject.
        :type mem_count: int
        """
        self._mem_count = mem_count

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
        if not isinstance(other, BatchUpdateResponseResultProject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
