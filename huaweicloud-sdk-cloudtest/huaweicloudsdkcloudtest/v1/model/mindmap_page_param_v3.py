# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MindmapPageParamV3:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'folder_id_collection': 'list[str]',
        'creator_num_collection': 'list[str]',
        'updater_num_collection': 'list[str]',
        'folder_root_id': 'str',
        'id_collection': 'list[str]',
        'offset': 'int',
        'limit': 'int',
        'name': 'str',
        'project_id': 'str',
        'branch_uri': 'str',
        'is_master': 'int',
        'iterator_uri': 'str'
    }

    attribute_map = {
        'folder_id_collection': 'folder_id_collection',
        'creator_num_collection': 'creator_num_collection',
        'updater_num_collection': 'updater_num_collection',
        'folder_root_id': 'folder_root_id',
        'id_collection': 'id_collection',
        'offset': 'offset',
        'limit': 'limit',
        'name': 'name',
        'project_id': 'project_id',
        'branch_uri': 'branch_uri',
        'is_master': 'is_master',
        'iterator_uri': 'iterator_uri'
    }

    def __init__(self, folder_id_collection=None, creator_num_collection=None, updater_num_collection=None, folder_root_id=None, id_collection=None, offset=None, limit=None, name=None, project_id=None, branch_uri=None, is_master=None, iterator_uri=None):
        r"""MindmapPageParamV3

        The model defined in huaweicloud sdk

        :param folder_id_collection: 目录ID集合
        :type folder_id_collection: list[str]
        :param creator_num_collection: 创建者ID集合
        :type creator_num_collection: list[str]
        :param updater_num_collection: 更新人ID集合
        :type updater_num_collection: list[str]
        :param folder_root_id: 根目录ID
        :type folder_root_id: str
        :param id_collection: 主键ID集合
        :type id_collection: list[str]
        :param offset: 起始偏移量，表示从此偏移量开始查询，offset大于等于0，小于等于100000
        :type offset: int
        :param limit: 每页显示的条目数量，最大支持200条
        :type limit: int
        :param name: 脑图名称
        :type name: str
        :param project_id: 项目ID
        :type project_id: str
        :param branch_uri: 分支uri
        :type branch_uri: str
        :param is_master: 是否基线
        :type is_master: int
        :param iterator_uri: 计划uri
        :type iterator_uri: str
        """
        
        

        self._folder_id_collection = None
        self._creator_num_collection = None
        self._updater_num_collection = None
        self._folder_root_id = None
        self._id_collection = None
        self._offset = None
        self._limit = None
        self._name = None
        self._project_id = None
        self._branch_uri = None
        self._is_master = None
        self._iterator_uri = None
        self.discriminator = None

        if folder_id_collection is not None:
            self.folder_id_collection = folder_id_collection
        if creator_num_collection is not None:
            self.creator_num_collection = creator_num_collection
        if updater_num_collection is not None:
            self.updater_num_collection = updater_num_collection
        if folder_root_id is not None:
            self.folder_root_id = folder_root_id
        if id_collection is not None:
            self.id_collection = id_collection
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if name is not None:
            self.name = name
        self.project_id = project_id
        if branch_uri is not None:
            self.branch_uri = branch_uri
        if is_master is not None:
            self.is_master = is_master
        if iterator_uri is not None:
            self.iterator_uri = iterator_uri

    @property
    def folder_id_collection(self):
        r"""Gets the folder_id_collection of this MindmapPageParamV3.

        目录ID集合

        :return: The folder_id_collection of this MindmapPageParamV3.
        :rtype: list[str]
        """
        return self._folder_id_collection

    @folder_id_collection.setter
    def folder_id_collection(self, folder_id_collection):
        r"""Sets the folder_id_collection of this MindmapPageParamV3.

        目录ID集合

        :param folder_id_collection: The folder_id_collection of this MindmapPageParamV3.
        :type folder_id_collection: list[str]
        """
        self._folder_id_collection = folder_id_collection

    @property
    def creator_num_collection(self):
        r"""Gets the creator_num_collection of this MindmapPageParamV3.

        创建者ID集合

        :return: The creator_num_collection of this MindmapPageParamV3.
        :rtype: list[str]
        """
        return self._creator_num_collection

    @creator_num_collection.setter
    def creator_num_collection(self, creator_num_collection):
        r"""Sets the creator_num_collection of this MindmapPageParamV3.

        创建者ID集合

        :param creator_num_collection: The creator_num_collection of this MindmapPageParamV3.
        :type creator_num_collection: list[str]
        """
        self._creator_num_collection = creator_num_collection

    @property
    def updater_num_collection(self):
        r"""Gets the updater_num_collection of this MindmapPageParamV3.

        更新人ID集合

        :return: The updater_num_collection of this MindmapPageParamV3.
        :rtype: list[str]
        """
        return self._updater_num_collection

    @updater_num_collection.setter
    def updater_num_collection(self, updater_num_collection):
        r"""Sets the updater_num_collection of this MindmapPageParamV3.

        更新人ID集合

        :param updater_num_collection: The updater_num_collection of this MindmapPageParamV3.
        :type updater_num_collection: list[str]
        """
        self._updater_num_collection = updater_num_collection

    @property
    def folder_root_id(self):
        r"""Gets the folder_root_id of this MindmapPageParamV3.

        根目录ID

        :return: The folder_root_id of this MindmapPageParamV3.
        :rtype: str
        """
        return self._folder_root_id

    @folder_root_id.setter
    def folder_root_id(self, folder_root_id):
        r"""Sets the folder_root_id of this MindmapPageParamV3.

        根目录ID

        :param folder_root_id: The folder_root_id of this MindmapPageParamV3.
        :type folder_root_id: str
        """
        self._folder_root_id = folder_root_id

    @property
    def id_collection(self):
        r"""Gets the id_collection of this MindmapPageParamV3.

        主键ID集合

        :return: The id_collection of this MindmapPageParamV3.
        :rtype: list[str]
        """
        return self._id_collection

    @id_collection.setter
    def id_collection(self, id_collection):
        r"""Sets the id_collection of this MindmapPageParamV3.

        主键ID集合

        :param id_collection: The id_collection of this MindmapPageParamV3.
        :type id_collection: list[str]
        """
        self._id_collection = id_collection

    @property
    def offset(self):
        r"""Gets the offset of this MindmapPageParamV3.

        起始偏移量，表示从此偏移量开始查询，offset大于等于0，小于等于100000

        :return: The offset of this MindmapPageParamV3.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this MindmapPageParamV3.

        起始偏移量，表示从此偏移量开始查询，offset大于等于0，小于等于100000

        :param offset: The offset of this MindmapPageParamV3.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this MindmapPageParamV3.

        每页显示的条目数量，最大支持200条

        :return: The limit of this MindmapPageParamV3.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this MindmapPageParamV3.

        每页显示的条目数量，最大支持200条

        :param limit: The limit of this MindmapPageParamV3.
        :type limit: int
        """
        self._limit = limit

    @property
    def name(self):
        r"""Gets the name of this MindmapPageParamV3.

        脑图名称

        :return: The name of this MindmapPageParamV3.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this MindmapPageParamV3.

        脑图名称

        :param name: The name of this MindmapPageParamV3.
        :type name: str
        """
        self._name = name

    @property
    def project_id(self):
        r"""Gets the project_id of this MindmapPageParamV3.

        项目ID

        :return: The project_id of this MindmapPageParamV3.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this MindmapPageParamV3.

        项目ID

        :param project_id: The project_id of this MindmapPageParamV3.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def branch_uri(self):
        r"""Gets the branch_uri of this MindmapPageParamV3.

        分支uri

        :return: The branch_uri of this MindmapPageParamV3.
        :rtype: str
        """
        return self._branch_uri

    @branch_uri.setter
    def branch_uri(self, branch_uri):
        r"""Sets the branch_uri of this MindmapPageParamV3.

        分支uri

        :param branch_uri: The branch_uri of this MindmapPageParamV3.
        :type branch_uri: str
        """
        self._branch_uri = branch_uri

    @property
    def is_master(self):
        r"""Gets the is_master of this MindmapPageParamV3.

        是否基线

        :return: The is_master of this MindmapPageParamV3.
        :rtype: int
        """
        return self._is_master

    @is_master.setter
    def is_master(self, is_master):
        r"""Sets the is_master of this MindmapPageParamV3.

        是否基线

        :param is_master: The is_master of this MindmapPageParamV3.
        :type is_master: int
        """
        self._is_master = is_master

    @property
    def iterator_uri(self):
        r"""Gets the iterator_uri of this MindmapPageParamV3.

        计划uri

        :return: The iterator_uri of this MindmapPageParamV3.
        :rtype: str
        """
        return self._iterator_uri

    @iterator_uri.setter
    def iterator_uri(self, iterator_uri):
        r"""Sets the iterator_uri of this MindmapPageParamV3.

        计划uri

        :param iterator_uri: The iterator_uri of this MindmapPageParamV3.
        :type iterator_uri: str
        """
        self._iterator_uri = iterator_uri

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
        if not isinstance(other, MindmapPageParamV3):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
