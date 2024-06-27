# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TestCasePageParam:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'offset': 'int',
        'limit': 'int',
        'deleted': 'str',
        'id_collection': 'list[str]',
        'mindmap_id': 'str',
        'node_id': 'str',
        'node_id_collection': 'list[str]',
        'project_id': 'str',
        'is_archive': 'bool',
        'case_name': 'str',
        'has_sub_mindmap': 'bool',
        'sub_mindmap_id': 'list[str]'
    }

    attribute_map = {
        'offset': 'offset',
        'limit': 'limit',
        'deleted': 'deleted',
        'id_collection': 'id_collection',
        'mindmap_id': 'mindmap_id',
        'node_id': 'node_id',
        'node_id_collection': 'node_id_collection',
        'project_id': 'project_id',
        'is_archive': 'is_archive',
        'case_name': 'case_name',
        'has_sub_mindmap': 'has_sub_mindmap',
        'sub_mindmap_id': 'sub_mindmap_id'
    }

    def __init__(self, offset=None, limit=None, deleted=None, id_collection=None, mindmap_id=None, node_id=None, node_id_collection=None, project_id=None, is_archive=None, case_name=None, has_sub_mindmap=None, sub_mindmap_id=None):
        """TestCasePageParam

        The model defined in huaweicloud sdk

        :param offset: 
        :type offset: int
        :param limit: 
        :type limit: int
        :param deleted: 
        :type deleted: str
        :param id_collection: 
        :type id_collection: list[str]
        :param mindmap_id: 
        :type mindmap_id: str
        :param node_id: 
        :type node_id: str
        :param node_id_collection: 
        :type node_id_collection: list[str]
        :param project_id: 
        :type project_id: str
        :param is_archive: 
        :type is_archive: bool
        :param case_name: 
        :type case_name: str
        :param has_sub_mindmap: 
        :type has_sub_mindmap: bool
        :param sub_mindmap_id: 
        :type sub_mindmap_id: list[str]
        """
        
        

        self._offset = None
        self._limit = None
        self._deleted = None
        self._id_collection = None
        self._mindmap_id = None
        self._node_id = None
        self._node_id_collection = None
        self._project_id = None
        self._is_archive = None
        self._case_name = None
        self._has_sub_mindmap = None
        self._sub_mindmap_id = None
        self.discriminator = None

        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if deleted is not None:
            self.deleted = deleted
        if id_collection is not None:
            self.id_collection = id_collection
        if mindmap_id is not None:
            self.mindmap_id = mindmap_id
        if node_id is not None:
            self.node_id = node_id
        if node_id_collection is not None:
            self.node_id_collection = node_id_collection
        if project_id is not None:
            self.project_id = project_id
        if is_archive is not None:
            self.is_archive = is_archive
        if case_name is not None:
            self.case_name = case_name
        if has_sub_mindmap is not None:
            self.has_sub_mindmap = has_sub_mindmap
        if sub_mindmap_id is not None:
            self.sub_mindmap_id = sub_mindmap_id

    @property
    def offset(self):
        """Gets the offset of this TestCasePageParam.

        :return: The offset of this TestCasePageParam.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this TestCasePageParam.

        :param offset: The offset of this TestCasePageParam.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this TestCasePageParam.

        :return: The limit of this TestCasePageParam.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this TestCasePageParam.

        :param limit: The limit of this TestCasePageParam.
        :type limit: int
        """
        self._limit = limit

    @property
    def deleted(self):
        """Gets the deleted of this TestCasePageParam.

        :return: The deleted of this TestCasePageParam.
        :rtype: str
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this TestCasePageParam.

        :param deleted: The deleted of this TestCasePageParam.
        :type deleted: str
        """
        self._deleted = deleted

    @property
    def id_collection(self):
        """Gets the id_collection of this TestCasePageParam.

        :return: The id_collection of this TestCasePageParam.
        :rtype: list[str]
        """
        return self._id_collection

    @id_collection.setter
    def id_collection(self, id_collection):
        """Sets the id_collection of this TestCasePageParam.

        :param id_collection: The id_collection of this TestCasePageParam.
        :type id_collection: list[str]
        """
        self._id_collection = id_collection

    @property
    def mindmap_id(self):
        """Gets the mindmap_id of this TestCasePageParam.

        :return: The mindmap_id of this TestCasePageParam.
        :rtype: str
        """
        return self._mindmap_id

    @mindmap_id.setter
    def mindmap_id(self, mindmap_id):
        """Sets the mindmap_id of this TestCasePageParam.

        :param mindmap_id: The mindmap_id of this TestCasePageParam.
        :type mindmap_id: str
        """
        self._mindmap_id = mindmap_id

    @property
    def node_id(self):
        """Gets the node_id of this TestCasePageParam.

        :return: The node_id of this TestCasePageParam.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """Sets the node_id of this TestCasePageParam.

        :param node_id: The node_id of this TestCasePageParam.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def node_id_collection(self):
        """Gets the node_id_collection of this TestCasePageParam.

        :return: The node_id_collection of this TestCasePageParam.
        :rtype: list[str]
        """
        return self._node_id_collection

    @node_id_collection.setter
    def node_id_collection(self, node_id_collection):
        """Sets the node_id_collection of this TestCasePageParam.

        :param node_id_collection: The node_id_collection of this TestCasePageParam.
        :type node_id_collection: list[str]
        """
        self._node_id_collection = node_id_collection

    @property
    def project_id(self):
        """Gets the project_id of this TestCasePageParam.

        :return: The project_id of this TestCasePageParam.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this TestCasePageParam.

        :param project_id: The project_id of this TestCasePageParam.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def is_archive(self):
        """Gets the is_archive of this TestCasePageParam.

        :return: The is_archive of this TestCasePageParam.
        :rtype: bool
        """
        return self._is_archive

    @is_archive.setter
    def is_archive(self, is_archive):
        """Sets the is_archive of this TestCasePageParam.

        :param is_archive: The is_archive of this TestCasePageParam.
        :type is_archive: bool
        """
        self._is_archive = is_archive

    @property
    def case_name(self):
        """Gets the case_name of this TestCasePageParam.

        :return: The case_name of this TestCasePageParam.
        :rtype: str
        """
        return self._case_name

    @case_name.setter
    def case_name(self, case_name):
        """Sets the case_name of this TestCasePageParam.

        :param case_name: The case_name of this TestCasePageParam.
        :type case_name: str
        """
        self._case_name = case_name

    @property
    def has_sub_mindmap(self):
        """Gets the has_sub_mindmap of this TestCasePageParam.

        :return: The has_sub_mindmap of this TestCasePageParam.
        :rtype: bool
        """
        return self._has_sub_mindmap

    @has_sub_mindmap.setter
    def has_sub_mindmap(self, has_sub_mindmap):
        """Sets the has_sub_mindmap of this TestCasePageParam.

        :param has_sub_mindmap: The has_sub_mindmap of this TestCasePageParam.
        :type has_sub_mindmap: bool
        """
        self._has_sub_mindmap = has_sub_mindmap

    @property
    def sub_mindmap_id(self):
        """Gets the sub_mindmap_id of this TestCasePageParam.

        :return: The sub_mindmap_id of this TestCasePageParam.
        :rtype: list[str]
        """
        return self._sub_mindmap_id

    @sub_mindmap_id.setter
    def sub_mindmap_id(self, sub_mindmap_id):
        """Sets the sub_mindmap_id of this TestCasePageParam.

        :param sub_mindmap_id: The sub_mindmap_id of this TestCasePageParam.
        :type sub_mindmap_id: list[str]
        """
        self._sub_mindmap_id = sub_mindmap_id

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
        if not isinstance(other, TestCasePageParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
