# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteApproverRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'workspace': 'str',
        'approver_ids': 'str'
    }

    attribute_map = {
        'workspace': 'workspace',
        'approver_ids': 'approver_ids'
    }

    def __init__(self, workspace=None, approver_ids=None):
        """DeleteApproverRequest

        The model defined in huaweicloud sdk

        :param workspace: DataArts Studio工作空间ID
        :type workspace: str
        :param approver_ids: 审批人id
        :type approver_ids: str
        """
        
        

        self._workspace = None
        self._approver_ids = None
        self.discriminator = None

        self.workspace = workspace
        self.approver_ids = approver_ids

    @property
    def workspace(self):
        """Gets the workspace of this DeleteApproverRequest.

        DataArts Studio工作空间ID

        :return: The workspace of this DeleteApproverRequest.
        :rtype: str
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        """Sets the workspace of this DeleteApproverRequest.

        DataArts Studio工作空间ID

        :param workspace: The workspace of this DeleteApproverRequest.
        :type workspace: str
        """
        self._workspace = workspace

    @property
    def approver_ids(self):
        """Gets the approver_ids of this DeleteApproverRequest.

        审批人id

        :return: The approver_ids of this DeleteApproverRequest.
        :rtype: str
        """
        return self._approver_ids

    @approver_ids.setter
    def approver_ids(self, approver_ids):
        """Sets the approver_ids of this DeleteApproverRequest.

        审批人id

        :param approver_ids: The approver_ids of this DeleteApproverRequest.
        :type approver_ids: str
        """
        self._approver_ids = approver_ids

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
        if not isinstance(other, DeleteApproverRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
