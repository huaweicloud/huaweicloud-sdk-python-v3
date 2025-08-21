# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ApprovalApproverInfoDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'approver_ids': 'str'
    }

    attribute_map = {
        'approver_ids': 'approver_ids'
    }

    def __init__(self, approver_ids=None):
        r"""ApprovalApproverInfoDto

        The model defined in huaweicloud sdk

        :param approver_ids: **参数解释：** 需要更新的审核人ID列表 数字以英文逗号分隔 111,222 **取值范围：** 不涉及。
        :type approver_ids: str
        """
        
        

        self._approver_ids = None
        self.discriminator = None

        if approver_ids is not None:
            self.approver_ids = approver_ids

    @property
    def approver_ids(self):
        r"""Gets the approver_ids of this ApprovalApproverInfoDto.

        **参数解释：** 需要更新的审核人ID列表 数字以英文逗号分隔 111,222 **取值范围：** 不涉及。

        :return: The approver_ids of this ApprovalApproverInfoDto.
        :rtype: str
        """
        return self._approver_ids

    @approver_ids.setter
    def approver_ids(self, approver_ids):
        r"""Sets the approver_ids of this ApprovalApproverInfoDto.

        **参数解释：** 需要更新的审核人ID列表 数字以英文逗号分隔 111,222 **取值范围：** 不涉及。

        :param approver_ids: The approver_ids of this ApprovalApproverInfoDto.
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
        if not isinstance(other, ApprovalApproverInfoDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
