# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ReviewerInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'reviewer_name': 'str',
        'reviewer_id': 'str'
    }

    attribute_map = {
        'reviewer_name': 'reviewer_name',
        'reviewer_id': 'reviewer_id'
    }

    def __init__(self, reviewer_name=None, reviewer_id=None):
        r"""ReviewerInfo

        The model defined in huaweicloud sdk

        :param reviewer_name: 审批人名称（IAM用户名）
        :type reviewer_name: str
        :param reviewer_id: 审批人ID（IAM用户Id）
        :type reviewer_id: str
        """
        
        

        self._reviewer_name = None
        self._reviewer_id = None
        self.discriminator = None

        self.reviewer_name = reviewer_name
        self.reviewer_id = reviewer_id

    @property
    def reviewer_name(self):
        r"""Gets the reviewer_name of this ReviewerInfo.

        审批人名称（IAM用户名）

        :return: The reviewer_name of this ReviewerInfo.
        :rtype: str
        """
        return self._reviewer_name

    @reviewer_name.setter
    def reviewer_name(self, reviewer_name):
        r"""Sets the reviewer_name of this ReviewerInfo.

        审批人名称（IAM用户名）

        :param reviewer_name: The reviewer_name of this ReviewerInfo.
        :type reviewer_name: str
        """
        self._reviewer_name = reviewer_name

    @property
    def reviewer_id(self):
        r"""Gets the reviewer_id of this ReviewerInfo.

        审批人ID（IAM用户Id）

        :return: The reviewer_id of this ReviewerInfo.
        :rtype: str
        """
        return self._reviewer_id

    @reviewer_id.setter
    def reviewer_id(self, reviewer_id):
        r"""Sets the reviewer_id of this ReviewerInfo.

        审批人ID（IAM用户Id）

        :param reviewer_id: The reviewer_id of this ReviewerInfo.
        :type reviewer_id: str
        """
        self._reviewer_id = reviewer_id

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
        if not isinstance(other, ReviewerInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
