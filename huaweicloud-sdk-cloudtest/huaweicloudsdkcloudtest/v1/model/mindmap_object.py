# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MindmapObject:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'create_time': 'str',
        'creator_name': 'str',
        'creator_num': 'str',
        'folder_id': 'str',
        'folder_root_id': 'str',
        'id': 'str',
        'max_depth': 'int',
        'mindmap': 'str',
        'name': 'str',
        'project_id': 'str',
        'update_time': 'str'
    }

    attribute_map = {
        'create_time': 'create_time',
        'creator_name': 'creator_name',
        'creator_num': 'creator_num',
        'folder_id': 'folder_id',
        'folder_root_id': 'folder_root_id',
        'id': 'id',
        'max_depth': 'max_depth',
        'mindmap': 'mindmap',
        'name': 'name',
        'project_id': 'project_id',
        'update_time': 'update_time'
    }

    def __init__(self, create_time=None, creator_name=None, creator_num=None, folder_id=None, folder_root_id=None, id=None, max_depth=None, mindmap=None, name=None, project_id=None, update_time=None):
        r"""MindmapObject

        The model defined in huaweicloud sdk

        :param create_time: 创建时间
        :type create_time: str
        :param creator_name: 创建人名称
        :type creator_name: str
        :param creator_num: 创建人工号
        :type creator_num: str
        :param folder_id: 文件路径
        :type folder_id: str
        :param folder_root_id: 根目录id
        :type folder_root_id: str
        :param id: id 主键
        :type id: str
        :param max_depth: 脑图最大深度
        :type max_depth: int
        :param mindmap: 脑图JSON
        :type mindmap: str
        :param name: 脑图名称
        :type name: str
        :param project_id: 项目id
        :type project_id: str
        :param update_time: 更新时间
        :type update_time: str
        """
        
        

        self._create_time = None
        self._creator_name = None
        self._creator_num = None
        self._folder_id = None
        self._folder_root_id = None
        self._id = None
        self._max_depth = None
        self._mindmap = None
        self._name = None
        self._project_id = None
        self._update_time = None
        self.discriminator = None

        if create_time is not None:
            self.create_time = create_time
        if creator_name is not None:
            self.creator_name = creator_name
        if creator_num is not None:
            self.creator_num = creator_num
        if folder_id is not None:
            self.folder_id = folder_id
        if folder_root_id is not None:
            self.folder_root_id = folder_root_id
        if id is not None:
            self.id = id
        if max_depth is not None:
            self.max_depth = max_depth
        if mindmap is not None:
            self.mindmap = mindmap
        if name is not None:
            self.name = name
        if project_id is not None:
            self.project_id = project_id
        if update_time is not None:
            self.update_time = update_time

    @property
    def create_time(self):
        r"""Gets the create_time of this MindmapObject.

        创建时间

        :return: The create_time of this MindmapObject.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this MindmapObject.

        创建时间

        :param create_time: The create_time of this MindmapObject.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def creator_name(self):
        r"""Gets the creator_name of this MindmapObject.

        创建人名称

        :return: The creator_name of this MindmapObject.
        :rtype: str
        """
        return self._creator_name

    @creator_name.setter
    def creator_name(self, creator_name):
        r"""Sets the creator_name of this MindmapObject.

        创建人名称

        :param creator_name: The creator_name of this MindmapObject.
        :type creator_name: str
        """
        self._creator_name = creator_name

    @property
    def creator_num(self):
        r"""Gets the creator_num of this MindmapObject.

        创建人工号

        :return: The creator_num of this MindmapObject.
        :rtype: str
        """
        return self._creator_num

    @creator_num.setter
    def creator_num(self, creator_num):
        r"""Sets the creator_num of this MindmapObject.

        创建人工号

        :param creator_num: The creator_num of this MindmapObject.
        :type creator_num: str
        """
        self._creator_num = creator_num

    @property
    def folder_id(self):
        r"""Gets the folder_id of this MindmapObject.

        文件路径

        :return: The folder_id of this MindmapObject.
        :rtype: str
        """
        return self._folder_id

    @folder_id.setter
    def folder_id(self, folder_id):
        r"""Sets the folder_id of this MindmapObject.

        文件路径

        :param folder_id: The folder_id of this MindmapObject.
        :type folder_id: str
        """
        self._folder_id = folder_id

    @property
    def folder_root_id(self):
        r"""Gets the folder_root_id of this MindmapObject.

        根目录id

        :return: The folder_root_id of this MindmapObject.
        :rtype: str
        """
        return self._folder_root_id

    @folder_root_id.setter
    def folder_root_id(self, folder_root_id):
        r"""Sets the folder_root_id of this MindmapObject.

        根目录id

        :param folder_root_id: The folder_root_id of this MindmapObject.
        :type folder_root_id: str
        """
        self._folder_root_id = folder_root_id

    @property
    def id(self):
        r"""Gets the id of this MindmapObject.

        id 主键

        :return: The id of this MindmapObject.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this MindmapObject.

        id 主键

        :param id: The id of this MindmapObject.
        :type id: str
        """
        self._id = id

    @property
    def max_depth(self):
        r"""Gets the max_depth of this MindmapObject.

        脑图最大深度

        :return: The max_depth of this MindmapObject.
        :rtype: int
        """
        return self._max_depth

    @max_depth.setter
    def max_depth(self, max_depth):
        r"""Sets the max_depth of this MindmapObject.

        脑图最大深度

        :param max_depth: The max_depth of this MindmapObject.
        :type max_depth: int
        """
        self._max_depth = max_depth

    @property
    def mindmap(self):
        r"""Gets the mindmap of this MindmapObject.

        脑图JSON

        :return: The mindmap of this MindmapObject.
        :rtype: str
        """
        return self._mindmap

    @mindmap.setter
    def mindmap(self, mindmap):
        r"""Sets the mindmap of this MindmapObject.

        脑图JSON

        :param mindmap: The mindmap of this MindmapObject.
        :type mindmap: str
        """
        self._mindmap = mindmap

    @property
    def name(self):
        r"""Gets the name of this MindmapObject.

        脑图名称

        :return: The name of this MindmapObject.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this MindmapObject.

        脑图名称

        :param name: The name of this MindmapObject.
        :type name: str
        """
        self._name = name

    @property
    def project_id(self):
        r"""Gets the project_id of this MindmapObject.

        项目id

        :return: The project_id of this MindmapObject.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this MindmapObject.

        项目id

        :param project_id: The project_id of this MindmapObject.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def update_time(self):
        r"""Gets the update_time of this MindmapObject.

        更新时间

        :return: The update_time of this MindmapObject.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this MindmapObject.

        更新时间

        :param update_time: The update_time of this MindmapObject.
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
        if not isinstance(other, MindmapObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
