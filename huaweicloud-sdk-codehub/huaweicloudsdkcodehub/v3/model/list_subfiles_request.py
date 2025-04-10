# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSubfilesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'repository_uuid': 'str',
        'branch_name': 'str',
        'path': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'repository_uuid': 'repository_uuid',
        'branch_name': 'branch_name',
        'path': 'path',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, repository_uuid=None, branch_name=None, path=None, offset=None, limit=None):
        r"""ListSubfilesRequest

        The model defined in huaweicloud sdk

        :param repository_uuid: 仓库id
        :type repository_uuid: str
        :param branch_name: 分支名称
        :type branch_name: str
        :param path: 文件路径
        :type path: str
        :param offset: 偏移量
        :type offset: int
        :param limit: 记录数量
        :type limit: int
        """
        
        

        self._repository_uuid = None
        self._branch_name = None
        self._path = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        self.repository_uuid = repository_uuid
        self.branch_name = branch_name
        if path is not None:
            self.path = path
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def repository_uuid(self):
        r"""Gets the repository_uuid of this ListSubfilesRequest.

        仓库id

        :return: The repository_uuid of this ListSubfilesRequest.
        :rtype: str
        """
        return self._repository_uuid

    @repository_uuid.setter
    def repository_uuid(self, repository_uuid):
        r"""Sets the repository_uuid of this ListSubfilesRequest.

        仓库id

        :param repository_uuid: The repository_uuid of this ListSubfilesRequest.
        :type repository_uuid: str
        """
        self._repository_uuid = repository_uuid

    @property
    def branch_name(self):
        r"""Gets the branch_name of this ListSubfilesRequest.

        分支名称

        :return: The branch_name of this ListSubfilesRequest.
        :rtype: str
        """
        return self._branch_name

    @branch_name.setter
    def branch_name(self, branch_name):
        r"""Sets the branch_name of this ListSubfilesRequest.

        分支名称

        :param branch_name: The branch_name of this ListSubfilesRequest.
        :type branch_name: str
        """
        self._branch_name = branch_name

    @property
    def path(self):
        r"""Gets the path of this ListSubfilesRequest.

        文件路径

        :return: The path of this ListSubfilesRequest.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        r"""Sets the path of this ListSubfilesRequest.

        文件路径

        :param path: The path of this ListSubfilesRequest.
        :type path: str
        """
        self._path = path

    @property
    def offset(self):
        r"""Gets the offset of this ListSubfilesRequest.

        偏移量

        :return: The offset of this ListSubfilesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListSubfilesRequest.

        偏移量

        :param offset: The offset of this ListSubfilesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListSubfilesRequest.

        记录数量

        :return: The limit of this ListSubfilesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListSubfilesRequest.

        记录数量

        :param limit: The limit of this ListSubfilesRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ListSubfilesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
