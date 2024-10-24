# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListMessageNotificationPolicyResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total': 'int',
        'policies': 'list[MessageNotificationPolicy]'
    }

    attribute_map = {
        'total': 'total',
        'policies': 'policies'
    }

    def __init__(self, total=None, policies=None):
        """ListMessageNotificationPolicyResponse

        The model defined in huaweicloud sdk

        :param total: 符合条件的消息通知策略总数
        :type total: int
        :param policies: 消息通知策略列表信息
        :type policies: list[:class:`huaweicloudsdkdataartsfabric.v1.MessageNotificationPolicy`]
        """
        
        super(ListMessageNotificationPolicyResponse, self).__init__()

        self._total = None
        self._policies = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if policies is not None:
            self.policies = policies

    @property
    def total(self):
        """Gets the total of this ListMessageNotificationPolicyResponse.

        符合条件的消息通知策略总数

        :return: The total of this ListMessageNotificationPolicyResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ListMessageNotificationPolicyResponse.

        符合条件的消息通知策略总数

        :param total: The total of this ListMessageNotificationPolicyResponse.
        :type total: int
        """
        self._total = total

    @property
    def policies(self):
        """Gets the policies of this ListMessageNotificationPolicyResponse.

        消息通知策略列表信息

        :return: The policies of this ListMessageNotificationPolicyResponse.
        :rtype: list[:class:`huaweicloudsdkdataartsfabric.v1.MessageNotificationPolicy`]
        """
        return self._policies

    @policies.setter
    def policies(self, policies):
        """Sets the policies of this ListMessageNotificationPolicyResponse.

        消息通知策略列表信息

        :param policies: The policies of this ListMessageNotificationPolicyResponse.
        :type policies: list[:class:`huaweicloudsdkdataartsfabric.v1.MessageNotificationPolicy`]
        """
        self._policies = policies

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
        if not isinstance(other, ListMessageNotificationPolicyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
