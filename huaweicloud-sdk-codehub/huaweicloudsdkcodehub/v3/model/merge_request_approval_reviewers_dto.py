# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MergeRequestApprovalReviewersDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'approval_merge_request_reviewers': 'list[ApprovalUserDto]'
    }

    attribute_map = {
        'approval_merge_request_reviewers': 'approval_merge_request_reviewers'
    }

    def __init__(self, approval_merge_request_reviewers=None):
        r"""MergeRequestApprovalReviewersDto

        The model defined in huaweicloud sdk

        :param approval_merge_request_reviewers: 
        :type approval_merge_request_reviewers: list[:class:`huaweicloudsdkcodehub.v3.ApprovalUserDto`]
        """
        
        

        self._approval_merge_request_reviewers = None
        self.discriminator = None

        if approval_merge_request_reviewers is not None:
            self.approval_merge_request_reviewers = approval_merge_request_reviewers

    @property
    def approval_merge_request_reviewers(self):
        r"""Gets the approval_merge_request_reviewers of this MergeRequestApprovalReviewersDto.

        :return: The approval_merge_request_reviewers of this MergeRequestApprovalReviewersDto.
        :rtype: list[:class:`huaweicloudsdkcodehub.v3.ApprovalUserDto`]
        """
        return self._approval_merge_request_reviewers

    @approval_merge_request_reviewers.setter
    def approval_merge_request_reviewers(self, approval_merge_request_reviewers):
        r"""Sets the approval_merge_request_reviewers of this MergeRequestApprovalReviewersDto.

        :param approval_merge_request_reviewers: The approval_merge_request_reviewers of this MergeRequestApprovalReviewersDto.
        :type approval_merge_request_reviewers: list[:class:`huaweicloudsdkcodehub.v3.ApprovalUserDto`]
        """
        self._approval_merge_request_reviewers = approval_merge_request_reviewers

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
        if not isinstance(other, MergeRequestApprovalReviewersDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
