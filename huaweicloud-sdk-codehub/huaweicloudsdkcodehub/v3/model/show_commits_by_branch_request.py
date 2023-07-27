# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowCommitsByBranchRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'group_name': 'str',
        'page_index': 'int',
        'page_size': 'int',
        'ref_name': 'str',
        'repository_name': 'str'
    }

    attribute_map = {
        'group_name': 'group_name',
        'page_index': 'page_index',
        'page_size': 'page_size',
        'ref_name': 'ref_name',
        'repository_name': 'repository_name'
    }

    def __init__(self, group_name=None, page_index=None, page_size=None, ref_name=None, repository_name=None):
        """ShowCommitsByBranchRequest

        The model defined in huaweicloud sdk

        :param group_name: 仓库组名(克隆地址中域名后面仓库名前的一段 示例：git@repo.alpha.devcloud.inhuawei.com:Demo00228/testword.git  组名：Demo00228 )
        :type group_name: str
        :param page_index: 分页索引
        :type page_index: int
        :param page_size: 分页索引
        :type page_size: int
        :param ref_name: 分支或标签名，支持SHA格式
        :type ref_name: str
        :param repository_name: 仓库名
        :type repository_name: str
        """
        
        

        self._group_name = None
        self._page_index = None
        self._page_size = None
        self._ref_name = None
        self._repository_name = None
        self.discriminator = None

        self.group_name = group_name
        if page_index is not None:
            self.page_index = page_index
        if page_size is not None:
            self.page_size = page_size
        self.ref_name = ref_name
        self.repository_name = repository_name

    @property
    def group_name(self):
        """Gets the group_name of this ShowCommitsByBranchRequest.

        仓库组名(克隆地址中域名后面仓库名前的一段 示例：git@repo.alpha.devcloud.inhuawei.com:Demo00228/testword.git  组名：Demo00228 )

        :return: The group_name of this ShowCommitsByBranchRequest.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        """Sets the group_name of this ShowCommitsByBranchRequest.

        仓库组名(克隆地址中域名后面仓库名前的一段 示例：git@repo.alpha.devcloud.inhuawei.com:Demo00228/testword.git  组名：Demo00228 )

        :param group_name: The group_name of this ShowCommitsByBranchRequest.
        :type group_name: str
        """
        self._group_name = group_name

    @property
    def page_index(self):
        """Gets the page_index of this ShowCommitsByBranchRequest.

        分页索引

        :return: The page_index of this ShowCommitsByBranchRequest.
        :rtype: int
        """
        return self._page_index

    @page_index.setter
    def page_index(self, page_index):
        """Sets the page_index of this ShowCommitsByBranchRequest.

        分页索引

        :param page_index: The page_index of this ShowCommitsByBranchRequest.
        :type page_index: int
        """
        self._page_index = page_index

    @property
    def page_size(self):
        """Gets the page_size of this ShowCommitsByBranchRequest.

        分页索引

        :return: The page_size of this ShowCommitsByBranchRequest.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this ShowCommitsByBranchRequest.

        分页索引

        :param page_size: The page_size of this ShowCommitsByBranchRequest.
        :type page_size: int
        """
        self._page_size = page_size

    @property
    def ref_name(self):
        """Gets the ref_name of this ShowCommitsByBranchRequest.

        分支或标签名，支持SHA格式

        :return: The ref_name of this ShowCommitsByBranchRequest.
        :rtype: str
        """
        return self._ref_name

    @ref_name.setter
    def ref_name(self, ref_name):
        """Sets the ref_name of this ShowCommitsByBranchRequest.

        分支或标签名，支持SHA格式

        :param ref_name: The ref_name of this ShowCommitsByBranchRequest.
        :type ref_name: str
        """
        self._ref_name = ref_name

    @property
    def repository_name(self):
        """Gets the repository_name of this ShowCommitsByBranchRequest.

        仓库名

        :return: The repository_name of this ShowCommitsByBranchRequest.
        :rtype: str
        """
        return self._repository_name

    @repository_name.setter
    def repository_name(self, repository_name):
        """Sets the repository_name of this ShowCommitsByBranchRequest.

        仓库名

        :param repository_name: The repository_name of this ShowCommitsByBranchRequest.
        :type repository_name: str
        """
        self._repository_name = repository_name

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
        if not isinstance(other, ShowCommitsByBranchRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
