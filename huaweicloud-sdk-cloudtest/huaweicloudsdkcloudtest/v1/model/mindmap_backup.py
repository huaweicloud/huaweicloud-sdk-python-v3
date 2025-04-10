# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MindmapBackup:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'bak_name': 'str',
        'create_time': 'str',
        'creator_name': 'str',
        'creator_num': 'str',
        'id': 'str',
        'memo': 'str',
        'mindmap': 'str',
        'mindmap_id': 'str',
        'type': 'str',
        'update_time': 'str'
    }

    attribute_map = {
        'bak_name': 'bak_name',
        'create_time': 'create_time',
        'creator_name': 'creator_name',
        'creator_num': 'creator_num',
        'id': 'id',
        'memo': 'memo',
        'mindmap': 'mindmap',
        'mindmap_id': 'mindmap_id',
        'type': 'type',
        'update_time': 'update_time'
    }

    def __init__(self, bak_name=None, create_time=None, creator_name=None, creator_num=None, id=None, memo=None, mindmap=None, mindmap_id=None, type=None, update_time=None):
        r"""MindmapBackup

        The model defined in huaweicloud sdk

        :param bak_name: 备份名称
        :type bak_name: str
        :param create_time: 创建时间
        :type create_time: str
        :param creator_name: 创建人名称
        :type creator_name: str
        :param creator_num: 创建人工号
        :type creator_num: str
        :param id: id 主键
        :type id: str
        :param memo: 备注
        :type memo: str
        :param mindmap: 脑图JSON
        :type mindmap: str
        :param mindmap_id: 脑图Id
        :type mindmap_id: str
        :param type: 备份类型
        :type type: str
        :param update_time: 更新时间
        :type update_time: str
        """
        
        

        self._bak_name = None
        self._create_time = None
        self._creator_name = None
        self._creator_num = None
        self._id = None
        self._memo = None
        self._mindmap = None
        self._mindmap_id = None
        self._type = None
        self._update_time = None
        self.discriminator = None

        if bak_name is not None:
            self.bak_name = bak_name
        if create_time is not None:
            self.create_time = create_time
        if creator_name is not None:
            self.creator_name = creator_name
        if creator_num is not None:
            self.creator_num = creator_num
        if id is not None:
            self.id = id
        if memo is not None:
            self.memo = memo
        if mindmap is not None:
            self.mindmap = mindmap
        if mindmap_id is not None:
            self.mindmap_id = mindmap_id
        if type is not None:
            self.type = type
        if update_time is not None:
            self.update_time = update_time

    @property
    def bak_name(self):
        r"""Gets the bak_name of this MindmapBackup.

        备份名称

        :return: The bak_name of this MindmapBackup.
        :rtype: str
        """
        return self._bak_name

    @bak_name.setter
    def bak_name(self, bak_name):
        r"""Sets the bak_name of this MindmapBackup.

        备份名称

        :param bak_name: The bak_name of this MindmapBackup.
        :type bak_name: str
        """
        self._bak_name = bak_name

    @property
    def create_time(self):
        r"""Gets the create_time of this MindmapBackup.

        创建时间

        :return: The create_time of this MindmapBackup.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this MindmapBackup.

        创建时间

        :param create_time: The create_time of this MindmapBackup.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def creator_name(self):
        r"""Gets the creator_name of this MindmapBackup.

        创建人名称

        :return: The creator_name of this MindmapBackup.
        :rtype: str
        """
        return self._creator_name

    @creator_name.setter
    def creator_name(self, creator_name):
        r"""Sets the creator_name of this MindmapBackup.

        创建人名称

        :param creator_name: The creator_name of this MindmapBackup.
        :type creator_name: str
        """
        self._creator_name = creator_name

    @property
    def creator_num(self):
        r"""Gets the creator_num of this MindmapBackup.

        创建人工号

        :return: The creator_num of this MindmapBackup.
        :rtype: str
        """
        return self._creator_num

    @creator_num.setter
    def creator_num(self, creator_num):
        r"""Sets the creator_num of this MindmapBackup.

        创建人工号

        :param creator_num: The creator_num of this MindmapBackup.
        :type creator_num: str
        """
        self._creator_num = creator_num

    @property
    def id(self):
        r"""Gets the id of this MindmapBackup.

        id 主键

        :return: The id of this MindmapBackup.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this MindmapBackup.

        id 主键

        :param id: The id of this MindmapBackup.
        :type id: str
        """
        self._id = id

    @property
    def memo(self):
        r"""Gets the memo of this MindmapBackup.

        备注

        :return: The memo of this MindmapBackup.
        :rtype: str
        """
        return self._memo

    @memo.setter
    def memo(self, memo):
        r"""Sets the memo of this MindmapBackup.

        备注

        :param memo: The memo of this MindmapBackup.
        :type memo: str
        """
        self._memo = memo

    @property
    def mindmap(self):
        r"""Gets the mindmap of this MindmapBackup.

        脑图JSON

        :return: The mindmap of this MindmapBackup.
        :rtype: str
        """
        return self._mindmap

    @mindmap.setter
    def mindmap(self, mindmap):
        r"""Sets the mindmap of this MindmapBackup.

        脑图JSON

        :param mindmap: The mindmap of this MindmapBackup.
        :type mindmap: str
        """
        self._mindmap = mindmap

    @property
    def mindmap_id(self):
        r"""Gets the mindmap_id of this MindmapBackup.

        脑图Id

        :return: The mindmap_id of this MindmapBackup.
        :rtype: str
        """
        return self._mindmap_id

    @mindmap_id.setter
    def mindmap_id(self, mindmap_id):
        r"""Sets the mindmap_id of this MindmapBackup.

        脑图Id

        :param mindmap_id: The mindmap_id of this MindmapBackup.
        :type mindmap_id: str
        """
        self._mindmap_id = mindmap_id

    @property
    def type(self):
        r"""Gets the type of this MindmapBackup.

        备份类型

        :return: The type of this MindmapBackup.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this MindmapBackup.

        备份类型

        :param type: The type of this MindmapBackup.
        :type type: str
        """
        self._type = type

    @property
    def update_time(self):
        r"""Gets the update_time of this MindmapBackup.

        更新时间

        :return: The update_time of this MindmapBackup.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this MindmapBackup.

        更新时间

        :param update_time: The update_time of this MindmapBackup.
        :type update_time: str
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
        if not isinstance(other, MindmapBackup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
