# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OperateAuthorizationV2Req:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'reject_reason': 'str',
        'group_id': 'str'
    }

    attribute_map = {
        'reject_reason': 'reject_reason',
        'group_id': 'group_id'
    }

    def __init__(self, reject_reason=None, group_id=None):
        """OperateAuthorizationV2Req

        The model defined in huaweicloud sdk

        :param reject_reason: 拒绝理由
        :type reject_reason: str
        :param group_id: 组id
        :type group_id: str
        """
        
        

        self._reject_reason = None
        self._group_id = None
        self.discriminator = None

        if reject_reason is not None:
            self.reject_reason = reject_reason
        if group_id is not None:
            self.group_id = group_id

    @property
    def reject_reason(self):
        """Gets the reject_reason of this OperateAuthorizationV2Req.

        拒绝理由

        :return: The reject_reason of this OperateAuthorizationV2Req.
        :rtype: str
        """
        return self._reject_reason

    @reject_reason.setter
    def reject_reason(self, reject_reason):
        """Sets the reject_reason of this OperateAuthorizationV2Req.

        拒绝理由

        :param reject_reason: The reject_reason of this OperateAuthorizationV2Req.
        :type reject_reason: str
        """
        self._reject_reason = reject_reason

    @property
    def group_id(self):
        """Gets the group_id of this OperateAuthorizationV2Req.

        组id

        :return: The group_id of this OperateAuthorizationV2Req.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this OperateAuthorizationV2Req.

        组id

        :param group_id: The group_id of this OperateAuthorizationV2Req.
        :type group_id: str
        """
        self._group_id = group_id

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
        if not isinstance(other, OperateAuthorizationV2Req):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
