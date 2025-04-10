# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PollingPolicySubscriptionDetails:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'subscription_urn': 'str',
        'endpoint': 'str',
        'remark': 'str',
        'status': 'int'
    }

    attribute_map = {
        'subscription_urn': 'subscription_urn',
        'endpoint': 'endpoint',
        'remark': 'remark',
        'status': 'status'
    }

    def __init__(self, subscription_urn=None, endpoint=None, remark=None, status=None):
        r"""PollingPolicySubscriptionDetails

        The model defined in huaweicloud sdk

        :param subscription_urn: 当前轮询的序号。
        :type subscription_urn: str
        :param endpoint: 订阅终端urn列表。
        :type endpoint: str
        :param remark: 备注。
        :type remark: str
        :param status: 订阅者状态：0表示订阅还未确认，1表示已经确认，3表示已经取消确认。
        :type status: int
        """
        
        

        self._subscription_urn = None
        self._endpoint = None
        self._remark = None
        self._status = None
        self.discriminator = None

        self.subscription_urn = subscription_urn
        self.endpoint = endpoint
        if remark is not None:
            self.remark = remark
        if status is not None:
            self.status = status

    @property
    def subscription_urn(self):
        r"""Gets the subscription_urn of this PollingPolicySubscriptionDetails.

        当前轮询的序号。

        :return: The subscription_urn of this PollingPolicySubscriptionDetails.
        :rtype: str
        """
        return self._subscription_urn

    @subscription_urn.setter
    def subscription_urn(self, subscription_urn):
        r"""Sets the subscription_urn of this PollingPolicySubscriptionDetails.

        当前轮询的序号。

        :param subscription_urn: The subscription_urn of this PollingPolicySubscriptionDetails.
        :type subscription_urn: str
        """
        self._subscription_urn = subscription_urn

    @property
    def endpoint(self):
        r"""Gets the endpoint of this PollingPolicySubscriptionDetails.

        订阅终端urn列表。

        :return: The endpoint of this PollingPolicySubscriptionDetails.
        :rtype: str
        """
        return self._endpoint

    @endpoint.setter
    def endpoint(self, endpoint):
        r"""Sets the endpoint of this PollingPolicySubscriptionDetails.

        订阅终端urn列表。

        :param endpoint: The endpoint of this PollingPolicySubscriptionDetails.
        :type endpoint: str
        """
        self._endpoint = endpoint

    @property
    def remark(self):
        r"""Gets the remark of this PollingPolicySubscriptionDetails.

        备注。

        :return: The remark of this PollingPolicySubscriptionDetails.
        :rtype: str
        """
        return self._remark

    @remark.setter
    def remark(self, remark):
        r"""Sets the remark of this PollingPolicySubscriptionDetails.

        备注。

        :param remark: The remark of this PollingPolicySubscriptionDetails.
        :type remark: str
        """
        self._remark = remark

    @property
    def status(self):
        r"""Gets the status of this PollingPolicySubscriptionDetails.

        订阅者状态：0表示订阅还未确认，1表示已经确认，3表示已经取消确认。

        :return: The status of this PollingPolicySubscriptionDetails.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this PollingPolicySubscriptionDetails.

        订阅者状态：0表示订阅还未确认，1表示已经确认，3表示已经取消确认。

        :param status: The status of this PollingPolicySubscriptionDetails.
        :type status: int
        """
        self._status = status

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
        if not isinstance(other, PollingPolicySubscriptionDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
