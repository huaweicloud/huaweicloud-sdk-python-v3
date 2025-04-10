# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MindmapRecycle:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'app': 'str',
        'create_time': 'str',
        'creator_name': 'str',
        'creator_num': 'str',
        'folder_id': 'str',
        'folder_root_id': 'str',
        'id': 'str',
        'map_version': 'str',
        'mindmap': 'str',
        'name': 'str',
        'privacy': 'str',
        'project_id': 'str',
        'update_time': 'str'
    }

    attribute_map = {
        'app': 'app',
        'create_time': 'create_time',
        'creator_name': 'creator_name',
        'creator_num': 'creator_num',
        'folder_id': 'folder_id',
        'folder_root_id': 'folder_root_id',
        'id': 'id',
        'map_version': 'map_version',
        'mindmap': 'mindmap',
        'name': 'name',
        'privacy': 'privacy',
        'project_id': 'project_id',
        'update_time': 'update_time'
    }

    def __init__(self, app=None, create_time=None, creator_name=None, creator_num=None, folder_id=None, folder_root_id=None, id=None, map_version=None, mindmap=None, name=None, privacy=None, project_id=None, update_time=None):
        r"""MindmapRecycle

        The model defined in huaweicloud sdk

        :param app: app
        :type app: str
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
        :param map_version: 脑图版本
        :type map_version: str
        :param mindmap: 脑图JSON
        :type mindmap: str
        :param name: 脑图名称
        :type name: str
        :param privacy: 脑图是否私有
        :type privacy: str
        :param project_id: 项目id
        :type project_id: str
        :param update_time: 更新时间
        :type update_time: str
        """
        
        

        self._app = None
        self._create_time = None
        self._creator_name = None
        self._creator_num = None
        self._folder_id = None
        self._folder_root_id = None
        self._id = None
        self._map_version = None
        self._mindmap = None
        self._name = None
        self._privacy = None
        self._project_id = None
        self._update_time = None
        self.discriminator = None

        if app is not None:
            self.app = app
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
        if map_version is not None:
            self.map_version = map_version
        if mindmap is not None:
            self.mindmap = mindmap
        if name is not None:
            self.name = name
        if privacy is not None:
            self.privacy = privacy
        if project_id is not None:
            self.project_id = project_id
        if update_time is not None:
            self.update_time = update_time

    @property
    def app(self):
        r"""Gets the app of this MindmapRecycle.

        app

        :return: The app of this MindmapRecycle.
        :rtype: str
        """
        return self._app

    @app.setter
    def app(self, app):
        r"""Sets the app of this MindmapRecycle.

        app

        :param app: The app of this MindmapRecycle.
        :type app: str
        """
        self._app = app

    @property
    def create_time(self):
        r"""Gets the create_time of this MindmapRecycle.

        创建时间

        :return: The create_time of this MindmapRecycle.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this MindmapRecycle.

        创建时间

        :param create_time: The create_time of this MindmapRecycle.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def creator_name(self):
        r"""Gets the creator_name of this MindmapRecycle.

        创建人名称

        :return: The creator_name of this MindmapRecycle.
        :rtype: str
        """
        return self._creator_name

    @creator_name.setter
    def creator_name(self, creator_name):
        r"""Sets the creator_name of this MindmapRecycle.

        创建人名称

        :param creator_name: The creator_name of this MindmapRecycle.
        :type creator_name: str
        """
        self._creator_name = creator_name

    @property
    def creator_num(self):
        r"""Gets the creator_num of this MindmapRecycle.

        创建人工号

        :return: The creator_num of this MindmapRecycle.
        :rtype: str
        """
        return self._creator_num

    @creator_num.setter
    def creator_num(self, creator_num):
        r"""Sets the creator_num of this MindmapRecycle.

        创建人工号

        :param creator_num: The creator_num of this MindmapRecycle.
        :type creator_num: str
        """
        self._creator_num = creator_num

    @property
    def folder_id(self):
        r"""Gets the folder_id of this MindmapRecycle.

        文件路径

        :return: The folder_id of this MindmapRecycle.
        :rtype: str
        """
        return self._folder_id

    @folder_id.setter
    def folder_id(self, folder_id):
        r"""Sets the folder_id of this MindmapRecycle.

        文件路径

        :param folder_id: The folder_id of this MindmapRecycle.
        :type folder_id: str
        """
        self._folder_id = folder_id

    @property
    def folder_root_id(self):
        r"""Gets the folder_root_id of this MindmapRecycle.

        根目录id

        :return: The folder_root_id of this MindmapRecycle.
        :rtype: str
        """
        return self._folder_root_id

    @folder_root_id.setter
    def folder_root_id(self, folder_root_id):
        r"""Sets the folder_root_id of this MindmapRecycle.

        根目录id

        :param folder_root_id: The folder_root_id of this MindmapRecycle.
        :type folder_root_id: str
        """
        self._folder_root_id = folder_root_id

    @property
    def id(self):
        r"""Gets the id of this MindmapRecycle.

        id 主键

        :return: The id of this MindmapRecycle.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this MindmapRecycle.

        id 主键

        :param id: The id of this MindmapRecycle.
        :type id: str
        """
        self._id = id

    @property
    def map_version(self):
        r"""Gets the map_version of this MindmapRecycle.

        脑图版本

        :return: The map_version of this MindmapRecycle.
        :rtype: str
        """
        return self._map_version

    @map_version.setter
    def map_version(self, map_version):
        r"""Sets the map_version of this MindmapRecycle.

        脑图版本

        :param map_version: The map_version of this MindmapRecycle.
        :type map_version: str
        """
        self._map_version = map_version

    @property
    def mindmap(self):
        r"""Gets the mindmap of this MindmapRecycle.

        脑图JSON

        :return: The mindmap of this MindmapRecycle.
        :rtype: str
        """
        return self._mindmap

    @mindmap.setter
    def mindmap(self, mindmap):
        r"""Sets the mindmap of this MindmapRecycle.

        脑图JSON

        :param mindmap: The mindmap of this MindmapRecycle.
        :type mindmap: str
        """
        self._mindmap = mindmap

    @property
    def name(self):
        r"""Gets the name of this MindmapRecycle.

        脑图名称

        :return: The name of this MindmapRecycle.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this MindmapRecycle.

        脑图名称

        :param name: The name of this MindmapRecycle.
        :type name: str
        """
        self._name = name

    @property
    def privacy(self):
        r"""Gets the privacy of this MindmapRecycle.

        脑图是否私有

        :return: The privacy of this MindmapRecycle.
        :rtype: str
        """
        return self._privacy

    @privacy.setter
    def privacy(self, privacy):
        r"""Sets the privacy of this MindmapRecycle.

        脑图是否私有

        :param privacy: The privacy of this MindmapRecycle.
        :type privacy: str
        """
        self._privacy = privacy

    @property
    def project_id(self):
        r"""Gets the project_id of this MindmapRecycle.

        项目id

        :return: The project_id of this MindmapRecycle.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this MindmapRecycle.

        项目id

        :param project_id: The project_id of this MindmapRecycle.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def update_time(self):
        r"""Gets the update_time of this MindmapRecycle.

        更新时间

        :return: The update_time of this MindmapRecycle.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this MindmapRecycle.

        更新时间

        :param update_time: The update_time of this MindmapRecycle.
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
        if not isinstance(other, MindmapRecycle):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
