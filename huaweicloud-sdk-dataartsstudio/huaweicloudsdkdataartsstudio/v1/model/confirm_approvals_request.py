# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ConfirmApprovalsRequest:

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
        'action_id': 'str',
        'body': 'ApprovalInfoParam'
    }

    attribute_map = {
        'workspace': 'workspace',
        'action_id': 'action-id',
        'body': 'body'
    }

    def __init__(self, workspace=None, action_id=None, body=None):
        """ConfirmApprovalsRequest

        The model defined in huaweicloud sdk

        :param workspace: DataArts Studio工作空间ID
        :type workspace: str
        :param action_id: 处理审批单结果类型
        :type action_id: str
        :param body: Body of the ConfirmApprovalsRequest
        :type body: :class:`huaweicloudsdkdataartsstudio.v1.ApprovalInfoParam`
        """
        
        

        self._workspace = None
        self._action_id = None
        self._body = None
        self.discriminator = None

        self.workspace = workspace
        self.action_id = action_id
        if body is not None:
            self.body = body

    @property
    def workspace(self):
        """Gets the workspace of this ConfirmApprovalsRequest.

        DataArts Studio工作空间ID

        :return: The workspace of this ConfirmApprovalsRequest.
        :rtype: str
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        """Sets the workspace of this ConfirmApprovalsRequest.

        DataArts Studio工作空间ID

        :param workspace: The workspace of this ConfirmApprovalsRequest.
        :type workspace: str
        """
        self._workspace = workspace

    @property
    def action_id(self):
        """Gets the action_id of this ConfirmApprovalsRequest.

        处理审批单结果类型

        :return: The action_id of this ConfirmApprovalsRequest.
        :rtype: str
        """
        return self._action_id

    @action_id.setter
    def action_id(self, action_id):
        """Sets the action_id of this ConfirmApprovalsRequest.

        处理审批单结果类型

        :param action_id: The action_id of this ConfirmApprovalsRequest.
        :type action_id: str
        """
        self._action_id = action_id

    @property
    def body(self):
        """Gets the body of this ConfirmApprovalsRequest.

        :return: The body of this ConfirmApprovalsRequest.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ApprovalInfoParam`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this ConfirmApprovalsRequest.

        :param body: The body of this ConfirmApprovalsRequest.
        :type body: :class:`huaweicloudsdkdataartsstudio.v1.ApprovalInfoParam`
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
        if not isinstance(other, ConfirmApprovalsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
