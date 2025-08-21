# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowNotificationSubscriptionsStatusResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'internal_message': 'RepoNotificationSubscriptionStateDto',
        'email': 'RepoNotificationSubscriptionStateDto',
        'qyweixin': 'RepoNotificationSubscriptionStateDto',
        'feishu': 'RepoNotificationSubscriptionStateDto',
        'dingding': 'RepoNotificationSubscriptionStateDto'
    }

    attribute_map = {
        'internal_message': 'internal_message',
        'email': 'email',
        'qyweixin': 'qyweixin',
        'feishu': 'feishu',
        'dingding': 'dingding'
    }

    def __init__(self, internal_message=None, email=None, qyweixin=None, feishu=None, dingding=None):
        r"""ShowNotificationSubscriptionsStatusResponse

        The model defined in huaweicloud sdk

        :param internal_message: 
        :type internal_message: :class:`huaweicloudsdkcodehub.v4.RepoNotificationSubscriptionStateDto`
        :param email: 
        :type email: :class:`huaweicloudsdkcodehub.v4.RepoNotificationSubscriptionStateDto`
        :param qyweixin: 
        :type qyweixin: :class:`huaweicloudsdkcodehub.v4.RepoNotificationSubscriptionStateDto`
        :param feishu: 
        :type feishu: :class:`huaweicloudsdkcodehub.v4.RepoNotificationSubscriptionStateDto`
        :param dingding: 
        :type dingding: :class:`huaweicloudsdkcodehub.v4.RepoNotificationSubscriptionStateDto`
        """
        
        super(ShowNotificationSubscriptionsStatusResponse, self).__init__()

        self._internal_message = None
        self._email = None
        self._qyweixin = None
        self._feishu = None
        self._dingding = None
        self.discriminator = None

        if internal_message is not None:
            self.internal_message = internal_message
        if email is not None:
            self.email = email
        if qyweixin is not None:
            self.qyweixin = qyweixin
        if feishu is not None:
            self.feishu = feishu
        if dingding is not None:
            self.dingding = dingding

    @property
    def internal_message(self):
        r"""Gets the internal_message of this ShowNotificationSubscriptionsStatusResponse.

        :return: The internal_message of this ShowNotificationSubscriptionsStatusResponse.
        :rtype: :class:`huaweicloudsdkcodehub.v4.RepoNotificationSubscriptionStateDto`
        """
        return self._internal_message

    @internal_message.setter
    def internal_message(self, internal_message):
        r"""Sets the internal_message of this ShowNotificationSubscriptionsStatusResponse.

        :param internal_message: The internal_message of this ShowNotificationSubscriptionsStatusResponse.
        :type internal_message: :class:`huaweicloudsdkcodehub.v4.RepoNotificationSubscriptionStateDto`
        """
        self._internal_message = internal_message

    @property
    def email(self):
        r"""Gets the email of this ShowNotificationSubscriptionsStatusResponse.

        :return: The email of this ShowNotificationSubscriptionsStatusResponse.
        :rtype: :class:`huaweicloudsdkcodehub.v4.RepoNotificationSubscriptionStateDto`
        """
        return self._email

    @email.setter
    def email(self, email):
        r"""Sets the email of this ShowNotificationSubscriptionsStatusResponse.

        :param email: The email of this ShowNotificationSubscriptionsStatusResponse.
        :type email: :class:`huaweicloudsdkcodehub.v4.RepoNotificationSubscriptionStateDto`
        """
        self._email = email

    @property
    def qyweixin(self):
        r"""Gets the qyweixin of this ShowNotificationSubscriptionsStatusResponse.

        :return: The qyweixin of this ShowNotificationSubscriptionsStatusResponse.
        :rtype: :class:`huaweicloudsdkcodehub.v4.RepoNotificationSubscriptionStateDto`
        """
        return self._qyweixin

    @qyweixin.setter
    def qyweixin(self, qyweixin):
        r"""Sets the qyweixin of this ShowNotificationSubscriptionsStatusResponse.

        :param qyweixin: The qyweixin of this ShowNotificationSubscriptionsStatusResponse.
        :type qyweixin: :class:`huaweicloudsdkcodehub.v4.RepoNotificationSubscriptionStateDto`
        """
        self._qyweixin = qyweixin

    @property
    def feishu(self):
        r"""Gets the feishu of this ShowNotificationSubscriptionsStatusResponse.

        :return: The feishu of this ShowNotificationSubscriptionsStatusResponse.
        :rtype: :class:`huaweicloudsdkcodehub.v4.RepoNotificationSubscriptionStateDto`
        """
        return self._feishu

    @feishu.setter
    def feishu(self, feishu):
        r"""Sets the feishu of this ShowNotificationSubscriptionsStatusResponse.

        :param feishu: The feishu of this ShowNotificationSubscriptionsStatusResponse.
        :type feishu: :class:`huaweicloudsdkcodehub.v4.RepoNotificationSubscriptionStateDto`
        """
        self._feishu = feishu

    @property
    def dingding(self):
        r"""Gets the dingding of this ShowNotificationSubscriptionsStatusResponse.

        :return: The dingding of this ShowNotificationSubscriptionsStatusResponse.
        :rtype: :class:`huaweicloudsdkcodehub.v4.RepoNotificationSubscriptionStateDto`
        """
        return self._dingding

    @dingding.setter
    def dingding(self, dingding):
        r"""Sets the dingding of this ShowNotificationSubscriptionsStatusResponse.

        :param dingding: The dingding of this ShowNotificationSubscriptionsStatusResponse.
        :type dingding: :class:`huaweicloudsdkcodehub.v4.RepoNotificationSubscriptionStateDto`
        """
        self._dingding = dingding

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
        if not isinstance(other, ShowNotificationSubscriptionsStatusResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
