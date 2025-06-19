# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CheckWebhookUrlRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'job_id': 'str',
        'notice_type': 'str',
        'webhook_url': 'str'
    }

    attribute_map = {
        'job_id': 'job_id',
        'notice_type': 'notice_type',
        'webhook_url': 'webhook_url'
    }

    def __init__(self, job_id=None, notice_type=None, webhook_url=None):
        r"""CheckWebhookUrlRequestBody

        The model defined in huaweicloud sdk

        :param job_id: 任务ID
        :type job_id: str
        :param notice_type: 通知的类型,分为消息，邮件，钉钉，飞书和微信
        :type notice_type: str
        :param webhook_url: Webhook地址
        :type webhook_url: str
        """
        
        

        self._job_id = None
        self._notice_type = None
        self._webhook_url = None
        self.discriminator = None

        self.job_id = job_id
        self.notice_type = notice_type
        self.webhook_url = webhook_url

    @property
    def job_id(self):
        r"""Gets the job_id of this CheckWebhookUrlRequestBody.

        任务ID

        :return: The job_id of this CheckWebhookUrlRequestBody.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this CheckWebhookUrlRequestBody.

        任务ID

        :param job_id: The job_id of this CheckWebhookUrlRequestBody.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def notice_type(self):
        r"""Gets the notice_type of this CheckWebhookUrlRequestBody.

        通知的类型,分为消息，邮件，钉钉，飞书和微信

        :return: The notice_type of this CheckWebhookUrlRequestBody.
        :rtype: str
        """
        return self._notice_type

    @notice_type.setter
    def notice_type(self, notice_type):
        r"""Sets the notice_type of this CheckWebhookUrlRequestBody.

        通知的类型,分为消息，邮件，钉钉，飞书和微信

        :param notice_type: The notice_type of this CheckWebhookUrlRequestBody.
        :type notice_type: str
        """
        self._notice_type = notice_type

    @property
    def webhook_url(self):
        r"""Gets the webhook_url of this CheckWebhookUrlRequestBody.

        Webhook地址

        :return: The webhook_url of this CheckWebhookUrlRequestBody.
        :rtype: str
        """
        return self._webhook_url

    @webhook_url.setter
    def webhook_url(self, webhook_url):
        r"""Sets the webhook_url of this CheckWebhookUrlRequestBody.

        Webhook地址

        :param webhook_url: The webhook_url of this CheckWebhookUrlRequestBody.
        :type webhook_url: str
        """
        self._webhook_url = webhook_url

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
        if not isinstance(other, CheckWebhookUrlRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
