# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListFilesRequest:

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
        'path': 'str'
    }

    attribute_map = {
        'repository_uuid': 'repository_uuid',
        'branch_name': 'branch_name',
        'path': 'path'
    }

    def __init__(self, repository_uuid=None, branch_name=None, path=None):
        """ListFilesRequest

        The model defined in huaweicloud sdk

        :param repository_uuid: 仓库id
        :type repository_uuid: str
        :param branch_name: 分支名称
        :type branch_name: str
        :param path: 文件路径
        :type path: str
        """
        
        

        self._repository_uuid = None
        self._branch_name = None
        self._path = None
        self.discriminator = None

        self.repository_uuid = repository_uuid
        self.branch_name = branch_name
        self.path = path

    @property
    def repository_uuid(self):
        """Gets the repository_uuid of this ListFilesRequest.

        仓库id

        :return: The repository_uuid of this ListFilesRequest.
        :rtype: str
        """
        return self._repository_uuid

    @repository_uuid.setter
    def repository_uuid(self, repository_uuid):
        """Sets the repository_uuid of this ListFilesRequest.

        仓库id

        :param repository_uuid: The repository_uuid of this ListFilesRequest.
        :type repository_uuid: str
        """
        self._repository_uuid = repository_uuid

    @property
    def branch_name(self):
        """Gets the branch_name of this ListFilesRequest.

        分支名称

        :return: The branch_name of this ListFilesRequest.
        :rtype: str
        """
        return self._branch_name

    @branch_name.setter
    def branch_name(self, branch_name):
        """Sets the branch_name of this ListFilesRequest.

        分支名称

        :param branch_name: The branch_name of this ListFilesRequest.
        :type branch_name: str
        """
        self._branch_name = branch_name

    @property
    def path(self):
        """Gets the path of this ListFilesRequest.

        文件路径

        :return: The path of this ListFilesRequest.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this ListFilesRequest.

        文件路径

        :param path: The path of this ListFilesRequest.
        :type path: str
        """
        self._path = path

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
        if not isinstance(other, ListFilesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
