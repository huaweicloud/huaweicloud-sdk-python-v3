# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListFileBuildArchivesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'parent_id': 'str',
        'build_id': 'str',
        'build_no': 'str',
        'page_no': 'int',
        'page_size': 'int',
        'repo_branch': 'str'
    }

    attribute_map = {
        'parent_id': 'parent_id',
        'build_id': 'build_id',
        'build_no': 'build_no',
        'page_no': 'page_no',
        'page_size': 'page_size',
        'repo_branch': 'repo_branch'
    }

    def __init__(self, parent_id=None, build_id=None, build_no=None, page_no=None, page_size=None, repo_branch=None):
        r"""ListFileBuildArchivesRequest

        The model defined in huaweicloud sdk

        :param parent_id: 父节点id
        :type parent_id: str
        :param build_id: 构建id
        :type build_id: str
        :param build_no: 构建序号
        :type build_no: str
        :param page_no: 页数
        :type page_no: int
        :param page_size: 每页数据量
        :type page_size: int
        :param repo_branch: codehub仓库分支
        :type repo_branch: str
        """
        
        

        self._parent_id = None
        self._build_id = None
        self._build_no = None
        self._page_no = None
        self._page_size = None
        self._repo_branch = None
        self.discriminator = None

        if parent_id is not None:
            self.parent_id = parent_id
        if build_id is not None:
            self.build_id = build_id
        if build_no is not None:
            self.build_no = build_no
        if page_no is not None:
            self.page_no = page_no
        if page_size is not None:
            self.page_size = page_size
        if repo_branch is not None:
            self.repo_branch = repo_branch

    @property
    def parent_id(self):
        r"""Gets the parent_id of this ListFileBuildArchivesRequest.

        父节点id

        :return: The parent_id of this ListFileBuildArchivesRequest.
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        r"""Sets the parent_id of this ListFileBuildArchivesRequest.

        父节点id

        :param parent_id: The parent_id of this ListFileBuildArchivesRequest.
        :type parent_id: str
        """
        self._parent_id = parent_id

    @property
    def build_id(self):
        r"""Gets the build_id of this ListFileBuildArchivesRequest.

        构建id

        :return: The build_id of this ListFileBuildArchivesRequest.
        :rtype: str
        """
        return self._build_id

    @build_id.setter
    def build_id(self, build_id):
        r"""Sets the build_id of this ListFileBuildArchivesRequest.

        构建id

        :param build_id: The build_id of this ListFileBuildArchivesRequest.
        :type build_id: str
        """
        self._build_id = build_id

    @property
    def build_no(self):
        r"""Gets the build_no of this ListFileBuildArchivesRequest.

        构建序号

        :return: The build_no of this ListFileBuildArchivesRequest.
        :rtype: str
        """
        return self._build_no

    @build_no.setter
    def build_no(self, build_no):
        r"""Sets the build_no of this ListFileBuildArchivesRequest.

        构建序号

        :param build_no: The build_no of this ListFileBuildArchivesRequest.
        :type build_no: str
        """
        self._build_no = build_no

    @property
    def page_no(self):
        r"""Gets the page_no of this ListFileBuildArchivesRequest.

        页数

        :return: The page_no of this ListFileBuildArchivesRequest.
        :rtype: int
        """
        return self._page_no

    @page_no.setter
    def page_no(self, page_no):
        r"""Sets the page_no of this ListFileBuildArchivesRequest.

        页数

        :param page_no: The page_no of this ListFileBuildArchivesRequest.
        :type page_no: int
        """
        self._page_no = page_no

    @property
    def page_size(self):
        r"""Gets the page_size of this ListFileBuildArchivesRequest.

        每页数据量

        :return: The page_size of this ListFileBuildArchivesRequest.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        r"""Sets the page_size of this ListFileBuildArchivesRequest.

        每页数据量

        :param page_size: The page_size of this ListFileBuildArchivesRequest.
        :type page_size: int
        """
        self._page_size = page_size

    @property
    def repo_branch(self):
        r"""Gets the repo_branch of this ListFileBuildArchivesRequest.

        codehub仓库分支

        :return: The repo_branch of this ListFileBuildArchivesRequest.
        :rtype: str
        """
        return self._repo_branch

    @repo_branch.setter
    def repo_branch(self, repo_branch):
        r"""Sets the repo_branch of this ListFileBuildArchivesRequest.

        codehub仓库分支

        :param repo_branch: The repo_branch of this ListFileBuildArchivesRequest.
        :type repo_branch: str
        """
        self._repo_branch = repo_branch

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
        if not isinstance(other, ListFileBuildArchivesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
