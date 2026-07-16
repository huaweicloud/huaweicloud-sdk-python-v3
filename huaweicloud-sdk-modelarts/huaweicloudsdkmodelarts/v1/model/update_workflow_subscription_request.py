# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateWorkflowSubscriptionRequest:

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
        'workflow_id': 'str',
        'body': 'Subscription'
    }

    attribute_map = {
        'subscription_id': 'subscription_id',
        'workflow_id': 'workflow_id',
        'body': 'body'
    }

    def __init__(self, subscription_id=None, workflow_id=None, body=None):
        r"""UpdateWorkflowSubscriptionRequest

        The model defined in huaweicloud sdk

        :param subscription_id: 消息订阅ID。
        :type subscription_id: str
        :param workflow_id: 工作流的ID。
        :type workflow_id: str
        :param body: Body of the UpdateWorkflowSubscriptionRequest
        :type body: :class:`huaweicloudsdkmodelarts.v1.Subscription`
        """
        
        

        self._subscription_id = None
        self._workflow_id = None
        self._body = None
        self.discriminator = None

        self.subscription_id = subscription_id
        self.workflow_id = workflow_id
        if body is not None:
            self.body = body

    @property
    def subscription_id(self):
        r"""Gets the subscription_id of this UpdateWorkflowSubscriptionRequest.

        消息订阅ID。

        :return: The subscription_id of this UpdateWorkflowSubscriptionRequest.
        :rtype: str
        """
        return self._subscription_id

    @subscription_id.setter
    def subscription_id(self, subscription_id):
        r"""Sets the subscription_id of this UpdateWorkflowSubscriptionRequest.

        消息订阅ID。

        :param subscription_id: The subscription_id of this UpdateWorkflowSubscriptionRequest.
        :type subscription_id: str
        """
        self._subscription_id = subscription_id

    @property
    def workflow_id(self):
        r"""Gets the workflow_id of this UpdateWorkflowSubscriptionRequest.

        工作流的ID。

        :return: The workflow_id of this UpdateWorkflowSubscriptionRequest.
        :rtype: str
        """
        return self._workflow_id

    @workflow_id.setter
    def workflow_id(self, workflow_id):
        r"""Sets the workflow_id of this UpdateWorkflowSubscriptionRequest.

        工作流的ID。

        :param workflow_id: The workflow_id of this UpdateWorkflowSubscriptionRequest.
        :type workflow_id: str
        """
        self._workflow_id = workflow_id

    @property
    def body(self):
        r"""Gets the body of this UpdateWorkflowSubscriptionRequest.

        :return: The body of this UpdateWorkflowSubscriptionRequest.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.Subscription`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this UpdateWorkflowSubscriptionRequest.

        :param body: The body of this UpdateWorkflowSubscriptionRequest.
        :type body: :class:`huaweicloudsdkmodelarts.v1.Subscription`
        """
        self._body = body

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UpdateWorkflowSubscriptionRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
