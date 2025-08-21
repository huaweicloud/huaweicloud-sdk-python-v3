# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowBranchConflictResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'source_repository_id': 'int',
        'target_repository_id': 'int',
        'source_branch': 'str',
        'target_branch': 'str',
        'is_conflict': 'bool'
    }

    attribute_map = {
        'source_repository_id': 'source_repository_id',
        'target_repository_id': 'target_repository_id',
        'source_branch': 'source_branch',
        'target_branch': 'target_branch',
        'is_conflict': 'is_conflict'
    }

    def __init__(self, source_repository_id=None, target_repository_id=None, source_branch=None, target_branch=None, is_conflict=None):
        r"""ShowBranchConflictResponse

        The model defined in huaweicloud sdk

        :param source_repository_id: 源仓库id
        :type source_repository_id: int
        :param target_repository_id: 目标仓库id
        :type target_repository_id: int
        :param source_branch: 源分支
        :type source_branch: str
        :param target_branch: 目标分支
        :type target_branch: str
        :param is_conflict: 是否有冲突
        :type is_conflict: bool
        """
        
        super(ShowBranchConflictResponse, self).__init__()

        self._source_repository_id = None
        self._target_repository_id = None
        self._source_branch = None
        self._target_branch = None
        self._is_conflict = None
        self.discriminator = None

        if source_repository_id is not None:
            self.source_repository_id = source_repository_id
        if target_repository_id is not None:
            self.target_repository_id = target_repository_id
        if source_branch is not None:
            self.source_branch = source_branch
        if target_branch is not None:
            self.target_branch = target_branch
        if is_conflict is not None:
            self.is_conflict = is_conflict

    @property
    def source_repository_id(self):
        r"""Gets the source_repository_id of this ShowBranchConflictResponse.

        源仓库id

        :return: The source_repository_id of this ShowBranchConflictResponse.
        :rtype: int
        """
        return self._source_repository_id

    @source_repository_id.setter
    def source_repository_id(self, source_repository_id):
        r"""Sets the source_repository_id of this ShowBranchConflictResponse.

        源仓库id

        :param source_repository_id: The source_repository_id of this ShowBranchConflictResponse.
        :type source_repository_id: int
        """
        self._source_repository_id = source_repository_id

    @property
    def target_repository_id(self):
        r"""Gets the target_repository_id of this ShowBranchConflictResponse.

        目标仓库id

        :return: The target_repository_id of this ShowBranchConflictResponse.
        :rtype: int
        """
        return self._target_repository_id

    @target_repository_id.setter
    def target_repository_id(self, target_repository_id):
        r"""Sets the target_repository_id of this ShowBranchConflictResponse.

        目标仓库id

        :param target_repository_id: The target_repository_id of this ShowBranchConflictResponse.
        :type target_repository_id: int
        """
        self._target_repository_id = target_repository_id

    @property
    def source_branch(self):
        r"""Gets the source_branch of this ShowBranchConflictResponse.

        源分支

        :return: The source_branch of this ShowBranchConflictResponse.
        :rtype: str
        """
        return self._source_branch

    @source_branch.setter
    def source_branch(self, source_branch):
        r"""Sets the source_branch of this ShowBranchConflictResponse.

        源分支

        :param source_branch: The source_branch of this ShowBranchConflictResponse.
        :type source_branch: str
        """
        self._source_branch = source_branch

    @property
    def target_branch(self):
        r"""Gets the target_branch of this ShowBranchConflictResponse.

        目标分支

        :return: The target_branch of this ShowBranchConflictResponse.
        :rtype: str
        """
        return self._target_branch

    @target_branch.setter
    def target_branch(self, target_branch):
        r"""Sets the target_branch of this ShowBranchConflictResponse.

        目标分支

        :param target_branch: The target_branch of this ShowBranchConflictResponse.
        :type target_branch: str
        """
        self._target_branch = target_branch

    @property
    def is_conflict(self):
        r"""Gets the is_conflict of this ShowBranchConflictResponse.

        是否有冲突

        :return: The is_conflict of this ShowBranchConflictResponse.
        :rtype: bool
        """
        return self._is_conflict

    @is_conflict.setter
    def is_conflict(self, is_conflict):
        r"""Sets the is_conflict of this ShowBranchConflictResponse.

        是否有冲突

        :param is_conflict: The is_conflict of this ShowBranchConflictResponse.
        :type is_conflict: bool
        """
        self._is_conflict = is_conflict

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
        if not isinstance(other, ShowBranchConflictResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
