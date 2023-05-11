# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateTestSuitByRepoFileInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'testsuite_name': 'str',
        'repository_id': 'str',
        'repository_branch': 'str',
        'file_path': 'str'
    }

    attribute_map = {
        'testsuite_name': 'testsuite_name',
        'repository_id': 'repository_id',
        'repository_branch': 'repository_branch',
        'file_path': 'file_path'
    }

    def __init__(self, testsuite_name=None, repository_id=None, repository_branch=None, file_path=None):
        """CreateTestSuitByRepoFileInfo

        The model defined in huaweicloud sdk

        :param testsuite_name: 要生成的测试套名称
        :type testsuite_name: str
        :param repository_id: 仓库id
        :type repository_id: str
        :param repository_branch: 仓库分支
        :type repository_branch: str
        :param file_path: 仓库中yaml或json文件的相对路径，仅支持swagger 2.0版本的yaml和json文件
        :type file_path: str
        """
        
        

        self._testsuite_name = None
        self._repository_id = None
        self._repository_branch = None
        self._file_path = None
        self.discriminator = None

        self.testsuite_name = testsuite_name
        self.repository_id = repository_id
        self.repository_branch = repository_branch
        self.file_path = file_path

    @property
    def testsuite_name(self):
        """Gets the testsuite_name of this CreateTestSuitByRepoFileInfo.

        要生成的测试套名称

        :return: The testsuite_name of this CreateTestSuitByRepoFileInfo.
        :rtype: str
        """
        return self._testsuite_name

    @testsuite_name.setter
    def testsuite_name(self, testsuite_name):
        """Sets the testsuite_name of this CreateTestSuitByRepoFileInfo.

        要生成的测试套名称

        :param testsuite_name: The testsuite_name of this CreateTestSuitByRepoFileInfo.
        :type testsuite_name: str
        """
        self._testsuite_name = testsuite_name

    @property
    def repository_id(self):
        """Gets the repository_id of this CreateTestSuitByRepoFileInfo.

        仓库id

        :return: The repository_id of this CreateTestSuitByRepoFileInfo.
        :rtype: str
        """
        return self._repository_id

    @repository_id.setter
    def repository_id(self, repository_id):
        """Sets the repository_id of this CreateTestSuitByRepoFileInfo.

        仓库id

        :param repository_id: The repository_id of this CreateTestSuitByRepoFileInfo.
        :type repository_id: str
        """
        self._repository_id = repository_id

    @property
    def repository_branch(self):
        """Gets the repository_branch of this CreateTestSuitByRepoFileInfo.

        仓库分支

        :return: The repository_branch of this CreateTestSuitByRepoFileInfo.
        :rtype: str
        """
        return self._repository_branch

    @repository_branch.setter
    def repository_branch(self, repository_branch):
        """Sets the repository_branch of this CreateTestSuitByRepoFileInfo.

        仓库分支

        :param repository_branch: The repository_branch of this CreateTestSuitByRepoFileInfo.
        :type repository_branch: str
        """
        self._repository_branch = repository_branch

    @property
    def file_path(self):
        """Gets the file_path of this CreateTestSuitByRepoFileInfo.

        仓库中yaml或json文件的相对路径，仅支持swagger 2.0版本的yaml和json文件

        :return: The file_path of this CreateTestSuitByRepoFileInfo.
        :rtype: str
        """
        return self._file_path

    @file_path.setter
    def file_path(self, file_path):
        """Sets the file_path of this CreateTestSuitByRepoFileInfo.

        仓库中yaml或json文件的相对路径，仅支持swagger 2.0版本的yaml和json文件

        :param file_path: The file_path of this CreateTestSuitByRepoFileInfo.
        :type file_path: str
        """
        self._file_path = file_path

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
        if not isinstance(other, CreateTestSuitByRepoFileInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
