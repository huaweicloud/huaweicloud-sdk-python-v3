# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchApproveRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'reason': 'str',
        'ids': 'list[str]'
    }

    attribute_map = {
        'reason': 'reason',
        'ids': 'ids'
    }

    def __init__(self, reason=None, ids=None):
        r"""BatchApproveRequestBody

        The model defined in huaweicloud sdk

        :param reason: 通过/拒绝原因
        :type reason: str
        :param ids: 工单id列表
        :type ids: list[str]
        """
        
        

        self._reason = None
        self._ids = None
        self.discriminator = None

        if reason is not None:
            self.reason = reason
        if ids is not None:
            self.ids = ids

    @property
    def reason(self):
        r"""Gets the reason of this BatchApproveRequestBody.

        通过/拒绝原因

        :return: The reason of this BatchApproveRequestBody.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        r"""Sets the reason of this BatchApproveRequestBody.

        通过/拒绝原因

        :param reason: The reason of this BatchApproveRequestBody.
        :type reason: str
        """
        self._reason = reason

    @property
    def ids(self):
        r"""Gets the ids of this BatchApproveRequestBody.

        工单id列表

        :return: The ids of this BatchApproveRequestBody.
        :rtype: list[str]
        """
        return self._ids

    @ids.setter
    def ids(self, ids):
        r"""Sets the ids of this BatchApproveRequestBody.

        工单id列表

        :param ids: The ids of this BatchApproveRequestBody.
        :type ids: list[str]
        """
        self._ids = ids

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
        if not isinstance(other, BatchApproveRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
