# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateSnapshotResult:

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
        'title': 'str',
        'category': 'str',
        'issue_id': 'str',
        'created_by': 'str',
        'deletable': 'bool',
        'errormsg': 'str'
    }

    attribute_map = {
        'id': 'id',
        'title': 'title',
        'category': 'category',
        'issue_id': 'issue_id',
        'created_by': 'created_by',
        'deletable': 'deletable',
        'errormsg': 'errormsg'
    }

    def __init__(self, id=None, title=None, category=None, issue_id=None, created_by=None, deletable=None, errormsg=None):
        r"""CreateSnapshotResult

        The model defined in huaweicloud sdk

        :param id: 快照ID。
        :type id: str
        :param title: 快照名称。创建时自动生成，工作项快照名称生成规则为：“工作项类型”+“ v” + “年”+“.”+“月”+“.”+“日”+“.”+“当日生成版本次数”。例如工作项类型为IR的工作项在2026年3月25日第一次打快照系统生成的快照名称为：IR v26.03.25.1。
        :type title: str
        :param category: 快照类型。工作项快照固定为：issue_snap_item。
        :type category: str
        :param issue_id: 快照的工作项ID。
        :type issue_id: str
        :param created_by: 快照的创建人ID。
        :type created_by: str
        :param deletable: 快照是否可被删除。
        :type deletable: bool
        :param errormsg: 创建快照失败的原因。
        :type errormsg: str
        """
        
        

        self._id = None
        self._title = None
        self._category = None
        self._issue_id = None
        self._created_by = None
        self._deletable = None
        self._errormsg = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if title is not None:
            self.title = title
        if category is not None:
            self.category = category
        if issue_id is not None:
            self.issue_id = issue_id
        if created_by is not None:
            self.created_by = created_by
        if deletable is not None:
            self.deletable = deletable
        if errormsg is not None:
            self.errormsg = errormsg

    @property
    def id(self):
        r"""Gets the id of this CreateSnapshotResult.

        快照ID。

        :return: The id of this CreateSnapshotResult.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this CreateSnapshotResult.

        快照ID。

        :param id: The id of this CreateSnapshotResult.
        :type id: str
        """
        self._id = id

    @property
    def title(self):
        r"""Gets the title of this CreateSnapshotResult.

        快照名称。创建时自动生成，工作项快照名称生成规则为：“工作项类型”+“ v” + “年”+“.”+“月”+“.”+“日”+“.”+“当日生成版本次数”。例如工作项类型为IR的工作项在2026年3月25日第一次打快照系统生成的快照名称为：IR v26.03.25.1。

        :return: The title of this CreateSnapshotResult.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        r"""Sets the title of this CreateSnapshotResult.

        快照名称。创建时自动生成，工作项快照名称生成规则为：“工作项类型”+“ v” + “年”+“.”+“月”+“.”+“日”+“.”+“当日生成版本次数”。例如工作项类型为IR的工作项在2026年3月25日第一次打快照系统生成的快照名称为：IR v26.03.25.1。

        :param title: The title of this CreateSnapshotResult.
        :type title: str
        """
        self._title = title

    @property
    def category(self):
        r"""Gets the category of this CreateSnapshotResult.

        快照类型。工作项快照固定为：issue_snap_item。

        :return: The category of this CreateSnapshotResult.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this CreateSnapshotResult.

        快照类型。工作项快照固定为：issue_snap_item。

        :param category: The category of this CreateSnapshotResult.
        :type category: str
        """
        self._category = category

    @property
    def issue_id(self):
        r"""Gets the issue_id of this CreateSnapshotResult.

        快照的工作项ID。

        :return: The issue_id of this CreateSnapshotResult.
        :rtype: str
        """
        return self._issue_id

    @issue_id.setter
    def issue_id(self, issue_id):
        r"""Sets the issue_id of this CreateSnapshotResult.

        快照的工作项ID。

        :param issue_id: The issue_id of this CreateSnapshotResult.
        :type issue_id: str
        """
        self._issue_id = issue_id

    @property
    def created_by(self):
        r"""Gets the created_by of this CreateSnapshotResult.

        快照的创建人ID。

        :return: The created_by of this CreateSnapshotResult.
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        r"""Sets the created_by of this CreateSnapshotResult.

        快照的创建人ID。

        :param created_by: The created_by of this CreateSnapshotResult.
        :type created_by: str
        """
        self._created_by = created_by

    @property
    def deletable(self):
        r"""Gets the deletable of this CreateSnapshotResult.

        快照是否可被删除。

        :return: The deletable of this CreateSnapshotResult.
        :rtype: bool
        """
        return self._deletable

    @deletable.setter
    def deletable(self, deletable):
        r"""Sets the deletable of this CreateSnapshotResult.

        快照是否可被删除。

        :param deletable: The deletable of this CreateSnapshotResult.
        :type deletable: bool
        """
        self._deletable = deletable

    @property
    def errormsg(self):
        r"""Gets the errormsg of this CreateSnapshotResult.

        创建快照失败的原因。

        :return: The errormsg of this CreateSnapshotResult.
        :rtype: str
        """
        return self._errormsg

    @errormsg.setter
    def errormsg(self, errormsg):
        r"""Sets the errormsg of this CreateSnapshotResult.

        创建快照失败的原因。

        :param errormsg: The errormsg of this CreateSnapshotResult.
        :type errormsg: str
        """
        self._errormsg = errormsg

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
        if not isinstance(other, CreateSnapshotResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
