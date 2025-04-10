# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListMergeChangesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'repository_id': 'int',
        'merge_request_iid': 'str',
        'file_path': 'str',
        'ignore_whitespace_change': 'bool',
        'force_encode': 'bool',
        'view': 'str',
        'commit_id': 'str'
    }

    attribute_map = {
        'repository_id': 'repository_id',
        'merge_request_iid': 'merge_request_iid',
        'file_path': 'file_path',
        'ignore_whitespace_change': 'ignore_whitespace_change',
        'force_encode': 'force_encode',
        'view': 'view',
        'commit_id': 'commit_id'
    }

    def __init__(self, repository_id=None, merge_request_iid=None, file_path=None, ignore_whitespace_change=None, force_encode=None, view=None, commit_id=None):
        r"""ListMergeChangesRequest

        The model defined in huaweicloud sdk

        :param repository_id: 仓库主键id
        :type repository_id: int
        :param merge_request_iid: MR长id
        :type merge_request_iid: str
        :param file_path: 文件路径
        :type file_path: str
        :param ignore_whitespace_change: 是否无视空格
        :type ignore_whitespace_change: bool
        :param force_encode: 是否需要编码
        :type force_encode: bool
        :param view: 是否为建议视图
        :type view: str
        :param commit_id: commit的id
        :type commit_id: str
        """
        
        

        self._repository_id = None
        self._merge_request_iid = None
        self._file_path = None
        self._ignore_whitespace_change = None
        self._force_encode = None
        self._view = None
        self._commit_id = None
        self.discriminator = None

        self.repository_id = repository_id
        self.merge_request_iid = merge_request_iid
        if file_path is not None:
            self.file_path = file_path
        if ignore_whitespace_change is not None:
            self.ignore_whitespace_change = ignore_whitespace_change
        if force_encode is not None:
            self.force_encode = force_encode
        if view is not None:
            self.view = view
        if commit_id is not None:
            self.commit_id = commit_id

    @property
    def repository_id(self):
        r"""Gets the repository_id of this ListMergeChangesRequest.

        仓库主键id

        :return: The repository_id of this ListMergeChangesRequest.
        :rtype: int
        """
        return self._repository_id

    @repository_id.setter
    def repository_id(self, repository_id):
        r"""Sets the repository_id of this ListMergeChangesRequest.

        仓库主键id

        :param repository_id: The repository_id of this ListMergeChangesRequest.
        :type repository_id: int
        """
        self._repository_id = repository_id

    @property
    def merge_request_iid(self):
        r"""Gets the merge_request_iid of this ListMergeChangesRequest.

        MR长id

        :return: The merge_request_iid of this ListMergeChangesRequest.
        :rtype: str
        """
        return self._merge_request_iid

    @merge_request_iid.setter
    def merge_request_iid(self, merge_request_iid):
        r"""Sets the merge_request_iid of this ListMergeChangesRequest.

        MR长id

        :param merge_request_iid: The merge_request_iid of this ListMergeChangesRequest.
        :type merge_request_iid: str
        """
        self._merge_request_iid = merge_request_iid

    @property
    def file_path(self):
        r"""Gets the file_path of this ListMergeChangesRequest.

        文件路径

        :return: The file_path of this ListMergeChangesRequest.
        :rtype: str
        """
        return self._file_path

    @file_path.setter
    def file_path(self, file_path):
        r"""Sets the file_path of this ListMergeChangesRequest.

        文件路径

        :param file_path: The file_path of this ListMergeChangesRequest.
        :type file_path: str
        """
        self._file_path = file_path

    @property
    def ignore_whitespace_change(self):
        r"""Gets the ignore_whitespace_change of this ListMergeChangesRequest.

        是否无视空格

        :return: The ignore_whitespace_change of this ListMergeChangesRequest.
        :rtype: bool
        """
        return self._ignore_whitespace_change

    @ignore_whitespace_change.setter
    def ignore_whitespace_change(self, ignore_whitespace_change):
        r"""Sets the ignore_whitespace_change of this ListMergeChangesRequest.

        是否无视空格

        :param ignore_whitespace_change: The ignore_whitespace_change of this ListMergeChangesRequest.
        :type ignore_whitespace_change: bool
        """
        self._ignore_whitespace_change = ignore_whitespace_change

    @property
    def force_encode(self):
        r"""Gets the force_encode of this ListMergeChangesRequest.

        是否需要编码

        :return: The force_encode of this ListMergeChangesRequest.
        :rtype: bool
        """
        return self._force_encode

    @force_encode.setter
    def force_encode(self, force_encode):
        r"""Sets the force_encode of this ListMergeChangesRequest.

        是否需要编码

        :param force_encode: The force_encode of this ListMergeChangesRequest.
        :type force_encode: bool
        """
        self._force_encode = force_encode

    @property
    def view(self):
        r"""Gets the view of this ListMergeChangesRequest.

        是否为建议视图

        :return: The view of this ListMergeChangesRequest.
        :rtype: str
        """
        return self._view

    @view.setter
    def view(self, view):
        r"""Sets the view of this ListMergeChangesRequest.

        是否为建议视图

        :param view: The view of this ListMergeChangesRequest.
        :type view: str
        """
        self._view = view

    @property
    def commit_id(self):
        r"""Gets the commit_id of this ListMergeChangesRequest.

        commit的id

        :return: The commit_id of this ListMergeChangesRequest.
        :rtype: str
        """
        return self._commit_id

    @commit_id.setter
    def commit_id(self, commit_id):
        r"""Sets the commit_id of this ListMergeChangesRequest.

        commit的id

        :param commit_id: The commit_id of this ListMergeChangesRequest.
        :type commit_id: str
        """
        self._commit_id = commit_id

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
        if not isinstance(other, ListMergeChangesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
