# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListMergeRequestVersionsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'int',
        'head_commit_sha': 'str',
        'base_commit_sha': 'str',
        'start_commit_sha': 'str',
        'created_at': 'str',
        'merge_request_id': 'int',
        'state': 'str',
        'real_size': 'str'
    }

    attribute_map = {
        'id': 'id',
        'head_commit_sha': 'head_commit_sha',
        'base_commit_sha': 'base_commit_sha',
        'start_commit_sha': 'start_commit_sha',
        'created_at': 'created_at',
        'merge_request_id': 'merge_request_id',
        'state': 'state',
        'real_size': 'real_size'
    }

    def __init__(self, id=None, head_commit_sha=None, base_commit_sha=None, start_commit_sha=None, created_at=None, merge_request_id=None, state=None, real_size=None):
        r"""ListMergeRequestVersionsResponse

        The model defined in huaweicloud sdk

        :param id: **参数解释：** diff主键ID。    
        :type id: int
        :param head_commit_sha: **参数解释：** head commit节点。
        :type head_commit_sha: str
        :param base_commit_sha: **参数解释：** base commit节点。
        :type base_commit_sha: str
        :param start_commit_sha: **参数解释：** tart commit节点。
        :type start_commit_sha: str
        :param created_at: **参数解释：** 创建时间。 
        :type created_at: str
        :param merge_request_id: **参数解释：** MR主键ID。
        :type merge_request_id: int
        :param state: **参数解释：** 状态。
        :type state: str
        :param real_size: **参数解释：** diff大小。
        :type real_size: str
        """
        
        super().__init__()

        self._id = None
        self._head_commit_sha = None
        self._base_commit_sha = None
        self._start_commit_sha = None
        self._created_at = None
        self._merge_request_id = None
        self._state = None
        self._real_size = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if head_commit_sha is not None:
            self.head_commit_sha = head_commit_sha
        if base_commit_sha is not None:
            self.base_commit_sha = base_commit_sha
        if start_commit_sha is not None:
            self.start_commit_sha = start_commit_sha
        if created_at is not None:
            self.created_at = created_at
        if merge_request_id is not None:
            self.merge_request_id = merge_request_id
        if state is not None:
            self.state = state
        if real_size is not None:
            self.real_size = real_size

    @property
    def id(self):
        r"""Gets the id of this ListMergeRequestVersionsResponse.

        **参数解释：** diff主键ID。    

        :return: The id of this ListMergeRequestVersionsResponse.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ListMergeRequestVersionsResponse.

        **参数解释：** diff主键ID。    

        :param id: The id of this ListMergeRequestVersionsResponse.
        :type id: int
        """
        self._id = id

    @property
    def head_commit_sha(self):
        r"""Gets the head_commit_sha of this ListMergeRequestVersionsResponse.

        **参数解释：** head commit节点。

        :return: The head_commit_sha of this ListMergeRequestVersionsResponse.
        :rtype: str
        """
        return self._head_commit_sha

    @head_commit_sha.setter
    def head_commit_sha(self, head_commit_sha):
        r"""Sets the head_commit_sha of this ListMergeRequestVersionsResponse.

        **参数解释：** head commit节点。

        :param head_commit_sha: The head_commit_sha of this ListMergeRequestVersionsResponse.
        :type head_commit_sha: str
        """
        self._head_commit_sha = head_commit_sha

    @property
    def base_commit_sha(self):
        r"""Gets the base_commit_sha of this ListMergeRequestVersionsResponse.

        **参数解释：** base commit节点。

        :return: The base_commit_sha of this ListMergeRequestVersionsResponse.
        :rtype: str
        """
        return self._base_commit_sha

    @base_commit_sha.setter
    def base_commit_sha(self, base_commit_sha):
        r"""Sets the base_commit_sha of this ListMergeRequestVersionsResponse.

        **参数解释：** base commit节点。

        :param base_commit_sha: The base_commit_sha of this ListMergeRequestVersionsResponse.
        :type base_commit_sha: str
        """
        self._base_commit_sha = base_commit_sha

    @property
    def start_commit_sha(self):
        r"""Gets the start_commit_sha of this ListMergeRequestVersionsResponse.

        **参数解释：** tart commit节点。

        :return: The start_commit_sha of this ListMergeRequestVersionsResponse.
        :rtype: str
        """
        return self._start_commit_sha

    @start_commit_sha.setter
    def start_commit_sha(self, start_commit_sha):
        r"""Sets the start_commit_sha of this ListMergeRequestVersionsResponse.

        **参数解释：** tart commit节点。

        :param start_commit_sha: The start_commit_sha of this ListMergeRequestVersionsResponse.
        :type start_commit_sha: str
        """
        self._start_commit_sha = start_commit_sha

    @property
    def created_at(self):
        r"""Gets the created_at of this ListMergeRequestVersionsResponse.

        **参数解释：** 创建时间。 

        :return: The created_at of this ListMergeRequestVersionsResponse.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this ListMergeRequestVersionsResponse.

        **参数解释：** 创建时间。 

        :param created_at: The created_at of this ListMergeRequestVersionsResponse.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def merge_request_id(self):
        r"""Gets the merge_request_id of this ListMergeRequestVersionsResponse.

        **参数解释：** MR主键ID。

        :return: The merge_request_id of this ListMergeRequestVersionsResponse.
        :rtype: int
        """
        return self._merge_request_id

    @merge_request_id.setter
    def merge_request_id(self, merge_request_id):
        r"""Sets the merge_request_id of this ListMergeRequestVersionsResponse.

        **参数解释：** MR主键ID。

        :param merge_request_id: The merge_request_id of this ListMergeRequestVersionsResponse.
        :type merge_request_id: int
        """
        self._merge_request_id = merge_request_id

    @property
    def state(self):
        r"""Gets the state of this ListMergeRequestVersionsResponse.

        **参数解释：** 状态。

        :return: The state of this ListMergeRequestVersionsResponse.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this ListMergeRequestVersionsResponse.

        **参数解释：** 状态。

        :param state: The state of this ListMergeRequestVersionsResponse.
        :type state: str
        """
        self._state = state

    @property
    def real_size(self):
        r"""Gets the real_size of this ListMergeRequestVersionsResponse.

        **参数解释：** diff大小。

        :return: The real_size of this ListMergeRequestVersionsResponse.
        :rtype: str
        """
        return self._real_size

    @real_size.setter
    def real_size(self, real_size):
        r"""Sets the real_size of this ListMergeRequestVersionsResponse.

        **参数解释：** diff大小。

        :param real_size: The real_size of this ListMergeRequestVersionsResponse.
        :type real_size: str
        """
        self._real_size = real_size

    def to_dict(self):
        import warnings
        warnings.warn("ListMergeRequestVersionsResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, ListMergeRequestVersionsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
