# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateMergeRequestApprovalStateRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'repository_id': 'str',
        'merge_request_iid': 'int',
        'body': 'ApprovalActionTypeDto'
    }

    attribute_map = {
        'repository_id': 'repository_id',
        'merge_request_iid': 'merge_request_iid',
        'body': 'body'
    }

    def __init__(self, repository_id=None, merge_request_iid=None, body=None):
        r"""UpdateMergeRequestApprovalStateRequest

        The model defined in huaweicloud sdk

        :param repository_id: 仓库的主键id
        :type repository_id: str
        :param merge_request_iid: 合并请求的短id
        :type merge_request_iid: int
        :param body: Body of the UpdateMergeRequestApprovalStateRequest
        :type body: :class:`huaweicloudsdkcodehub.v3.ApprovalActionTypeDto`
        """
        
        

        self._repository_id = None
        self._merge_request_iid = None
        self._body = None
        self.discriminator = None

        self.repository_id = repository_id
        self.merge_request_iid = merge_request_iid
        if body is not None:
            self.body = body

    @property
    def repository_id(self):
        r"""Gets the repository_id of this UpdateMergeRequestApprovalStateRequest.

        仓库的主键id

        :return: The repository_id of this UpdateMergeRequestApprovalStateRequest.
        :rtype: str
        """
        return self._repository_id

    @repository_id.setter
    def repository_id(self, repository_id):
        r"""Sets the repository_id of this UpdateMergeRequestApprovalStateRequest.

        仓库的主键id

        :param repository_id: The repository_id of this UpdateMergeRequestApprovalStateRequest.
        :type repository_id: str
        """
        self._repository_id = repository_id

    @property
    def merge_request_iid(self):
        r"""Gets the merge_request_iid of this UpdateMergeRequestApprovalStateRequest.

        合并请求的短id

        :return: The merge_request_iid of this UpdateMergeRequestApprovalStateRequest.
        :rtype: int
        """
        return self._merge_request_iid

    @merge_request_iid.setter
    def merge_request_iid(self, merge_request_iid):
        r"""Sets the merge_request_iid of this UpdateMergeRequestApprovalStateRequest.

        合并请求的短id

        :param merge_request_iid: The merge_request_iid of this UpdateMergeRequestApprovalStateRequest.
        :type merge_request_iid: int
        """
        self._merge_request_iid = merge_request_iid

    @property
    def body(self):
        r"""Gets the body of this UpdateMergeRequestApprovalStateRequest.

        :return: The body of this UpdateMergeRequestApprovalStateRequest.
        :rtype: :class:`huaweicloudsdkcodehub.v3.ApprovalActionTypeDto`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this UpdateMergeRequestApprovalStateRequest.

        :param body: The body of this UpdateMergeRequestApprovalStateRequest.
        :type body: :class:`huaweicloudsdkcodehub.v3.ApprovalActionTypeDto`
        """
        self._body = body

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
        if not isinstance(other, UpdateMergeRequestApprovalStateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
