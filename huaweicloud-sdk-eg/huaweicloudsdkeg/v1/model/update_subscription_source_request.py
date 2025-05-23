# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateSubscriptionSourceRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'subscription_id': 'str',
        'source_id': 'str',
        'enterprise_project_id': 'str',
        'body': 'SubscriptionSource'
    }

    attribute_map = {
        'subscription_id': 'subscription_id',
        'source_id': 'source_id',
        'enterprise_project_id': 'enterprise_project_id',
        'body': 'body'
    }

    def __init__(self, subscription_id=None, source_id=None, enterprise_project_id=None, body=None):
        r"""UpdateSubscriptionSourceRequest

        The model defined in huaweicloud sdk

        :param subscription_id: 事件订阅ID
        :type subscription_id: str
        :param source_id: 事件订阅源ID
        :type source_id: str
        :param enterprise_project_id: 创建订阅时所使用的企业项目id
        :type enterprise_project_id: str
        :param body: Body of the UpdateSubscriptionSourceRequest
        :type body: :class:`huaweicloudsdkeg.v1.SubscriptionSource`
        """
        
        

        self._subscription_id = None
        self._source_id = None
        self._enterprise_project_id = None
        self._body = None
        self.discriminator = None

        self.subscription_id = subscription_id
        self.source_id = source_id
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if body is not None:
            self.body = body

    @property
    def subscription_id(self):
        r"""Gets the subscription_id of this UpdateSubscriptionSourceRequest.

        事件订阅ID

        :return: The subscription_id of this UpdateSubscriptionSourceRequest.
        :rtype: str
        """
        return self._subscription_id

    @subscription_id.setter
    def subscription_id(self, subscription_id):
        r"""Sets the subscription_id of this UpdateSubscriptionSourceRequest.

        事件订阅ID

        :param subscription_id: The subscription_id of this UpdateSubscriptionSourceRequest.
        :type subscription_id: str
        """
        self._subscription_id = subscription_id

    @property
    def source_id(self):
        r"""Gets the source_id of this UpdateSubscriptionSourceRequest.

        事件订阅源ID

        :return: The source_id of this UpdateSubscriptionSourceRequest.
        :rtype: str
        """
        return self._source_id

    @source_id.setter
    def source_id(self, source_id):
        r"""Sets the source_id of this UpdateSubscriptionSourceRequest.

        事件订阅源ID

        :param source_id: The source_id of this UpdateSubscriptionSourceRequest.
        :type source_id: str
        """
        self._source_id = source_id

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this UpdateSubscriptionSourceRequest.

        创建订阅时所使用的企业项目id

        :return: The enterprise_project_id of this UpdateSubscriptionSourceRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this UpdateSubscriptionSourceRequest.

        创建订阅时所使用的企业项目id

        :param enterprise_project_id: The enterprise_project_id of this UpdateSubscriptionSourceRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def body(self):
        r"""Gets the body of this UpdateSubscriptionSourceRequest.

        :return: The body of this UpdateSubscriptionSourceRequest.
        :rtype: :class:`huaweicloudsdkeg.v1.SubscriptionSource`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this UpdateSubscriptionSourceRequest.

        :param body: The body of this UpdateSubscriptionSourceRequest.
        :type body: :class:`huaweicloudsdkeg.v1.SubscriptionSource`
        """
        self._body = body

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
        if not isinstance(other, UpdateSubscriptionSourceRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
