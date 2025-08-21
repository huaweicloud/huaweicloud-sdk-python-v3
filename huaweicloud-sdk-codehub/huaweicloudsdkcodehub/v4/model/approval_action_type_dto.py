# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ApprovalActionTypeDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'action_type': 'str',
        'approver_comment': 'str'
    }

    attribute_map = {
        'action_type': 'action_type',
        'approver_comment': 'approver_comment'
    }

    def __init__(self, action_type=None, approver_comment=None):
        r"""ApprovalActionTypeDto

        The model defined in huaweicloud sdk

        :param action_type: **参数解释：** 审核/检视操作动作 - approve，审核通过 - reject，审核拒绝 - complete，检视通过 - reset，重置审核/检视结果
        :type action_type: str
        :param approver_comment: **参数解释：** 审核备注 **取值范围：** 不涉及。
        :type approver_comment: str
        """
        
        

        self._action_type = None
        self._approver_comment = None
        self.discriminator = None

        if action_type is not None:
            self.action_type = action_type
        if approver_comment is not None:
            self.approver_comment = approver_comment

    @property
    def action_type(self):
        r"""Gets the action_type of this ApprovalActionTypeDto.

        **参数解释：** 审核/检视操作动作 - approve，审核通过 - reject，审核拒绝 - complete，检视通过 - reset，重置审核/检视结果

        :return: The action_type of this ApprovalActionTypeDto.
        :rtype: str
        """
        return self._action_type

    @action_type.setter
    def action_type(self, action_type):
        r"""Sets the action_type of this ApprovalActionTypeDto.

        **参数解释：** 审核/检视操作动作 - approve，审核通过 - reject，审核拒绝 - complete，检视通过 - reset，重置审核/检视结果

        :param action_type: The action_type of this ApprovalActionTypeDto.
        :type action_type: str
        """
        self._action_type = action_type

    @property
    def approver_comment(self):
        r"""Gets the approver_comment of this ApprovalActionTypeDto.

        **参数解释：** 审核备注 **取值范围：** 不涉及。

        :return: The approver_comment of this ApprovalActionTypeDto.
        :rtype: str
        """
        return self._approver_comment

    @approver_comment.setter
    def approver_comment(self, approver_comment):
        r"""Sets the approver_comment of this ApprovalActionTypeDto.

        **参数解释：** 审核备注 **取值范围：** 不涉及。

        :param approver_comment: The approver_comment of this ApprovalActionTypeDto.
        :type approver_comment: str
        """
        self._approver_comment = approver_comment

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
        if not isinstance(other, ApprovalActionTypeDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
