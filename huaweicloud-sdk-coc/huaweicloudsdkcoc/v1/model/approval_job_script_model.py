# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ApprovalJobScriptModel:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status': 'str',
        'comments': 'str'
    }

    attribute_map = {
        'status': 'status',
        'comments': 'comments'
    }

    def __init__(self, status=None, comments=None):
        r"""ApprovalJobScriptModel

        The model defined in huaweicloud sdk

        :param status: 审批状态 APPROVED:审批通过 REJECTED:审批不通过
        :type status: str
        :param comments: 审批意见
        :type comments: str
        """
        
        

        self._status = None
        self._comments = None
        self.discriminator = None

        self.status = status
        if comments is not None:
            self.comments = comments

    @property
    def status(self):
        r"""Gets the status of this ApprovalJobScriptModel.

        审批状态 APPROVED:审批通过 REJECTED:审批不通过

        :return: The status of this ApprovalJobScriptModel.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ApprovalJobScriptModel.

        审批状态 APPROVED:审批通过 REJECTED:审批不通过

        :param status: The status of this ApprovalJobScriptModel.
        :type status: str
        """
        self._status = status

    @property
    def comments(self):
        r"""Gets the comments of this ApprovalJobScriptModel.

        审批意见

        :return: The comments of this ApprovalJobScriptModel.
        :rtype: str
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        r"""Sets the comments of this ApprovalJobScriptModel.

        审批意见

        :param comments: The comments of this ApprovalJobScriptModel.
        :type comments: str
        """
        self._comments = comments

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
        if not isinstance(other, ApprovalJobScriptModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
