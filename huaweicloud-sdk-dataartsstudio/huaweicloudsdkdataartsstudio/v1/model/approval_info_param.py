# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ApprovalInfoParam:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ids': 'list[str]',
        'msg': 'str'
    }

    attribute_map = {
        'ids': 'ids',
        'msg': 'msg'
    }

    def __init__(self, ids=None, msg=None):
        """ApprovalInfoParam

        The model defined in huaweicloud sdk

        :param ids: 审批单ID列表，填写String类型替代Long类型。
        :type ids: list[str]
        :param msg: 审批单信息，审批人填写的审批意见。
        :type msg: str
        """
        
        

        self._ids = None
        self._msg = None
        self.discriminator = None

        self.ids = ids
        self.msg = msg

    @property
    def ids(self):
        """Gets the ids of this ApprovalInfoParam.

        审批单ID列表，填写String类型替代Long类型。

        :return: The ids of this ApprovalInfoParam.
        :rtype: list[str]
        """
        return self._ids

    @ids.setter
    def ids(self, ids):
        """Sets the ids of this ApprovalInfoParam.

        审批单ID列表，填写String类型替代Long类型。

        :param ids: The ids of this ApprovalInfoParam.
        :type ids: list[str]
        """
        self._ids = ids

    @property
    def msg(self):
        """Gets the msg of this ApprovalInfoParam.

        审批单信息，审批人填写的审批意见。

        :return: The msg of this ApprovalInfoParam.
        :rtype: str
        """
        return self._msg

    @msg.setter
    def msg(self, msg):
        """Sets the msg of this ApprovalInfoParam.

        审批单信息，审批人填写的审批意见。

        :param msg: The msg of this ApprovalInfoParam.
        :type msg: str
        """
        self._msg = msg

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
        if not isinstance(other, ApprovalInfoParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
