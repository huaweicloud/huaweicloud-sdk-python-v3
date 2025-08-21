# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ApprovalReviewerInfoDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'reviewer_ids': 'str'
    }

    attribute_map = {
        'reviewer_ids': 'reviewer_ids'
    }

    def __init__(self, reviewer_ids=None):
        r"""ApprovalReviewerInfoDto

        The model defined in huaweicloud sdk

        :param reviewer_ids: **参数解释：** 需要更新的检视人ID列表 数字以英文逗号分隔 111,222 **取值范围：** 不涉及。
        :type reviewer_ids: str
        """
        
        

        self._reviewer_ids = None
        self.discriminator = None

        if reviewer_ids is not None:
            self.reviewer_ids = reviewer_ids

    @property
    def reviewer_ids(self):
        r"""Gets the reviewer_ids of this ApprovalReviewerInfoDto.

        **参数解释：** 需要更新的检视人ID列表 数字以英文逗号分隔 111,222 **取值范围：** 不涉及。

        :return: The reviewer_ids of this ApprovalReviewerInfoDto.
        :rtype: str
        """
        return self._reviewer_ids

    @reviewer_ids.setter
    def reviewer_ids(self, reviewer_ids):
        r"""Sets the reviewer_ids of this ApprovalReviewerInfoDto.

        **参数解释：** 需要更新的检视人ID列表 数字以英文逗号分隔 111,222 **取值范围：** 不涉及。

        :param reviewer_ids: The reviewer_ids of this ApprovalReviewerInfoDto.
        :type reviewer_ids: str
        """
        self._reviewer_ids = reviewer_ids

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
        if not isinstance(other, ApprovalReviewerInfoDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
