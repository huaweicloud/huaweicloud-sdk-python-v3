# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListBotMRequestDistributionResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'normal_bucket': 'BotRequestDistributionsNormalBucket',
        'bot_classification_bucket': 'BotTypeDistributions',
        'action_bucket': 'ActionDistributions'
    }

    attribute_map = {
        'normal_bucket': 'normal_bucket',
        'bot_classification_bucket': 'bot_classification_bucket',
        'action_bucket': 'action_bucket'
    }

    def __init__(self, normal_bucket=None, bot_classification_bucket=None, action_bucket=None):
        r"""ListBotMRequestDistributionResponse

        The model defined in huaweicloud sdk

        :param normal_bucket: 
        :type normal_bucket: :class:`huaweicloudsdkwaf.v1.BotRequestDistributionsNormalBucket`
        :param bot_classification_bucket: 
        :type bot_classification_bucket: :class:`huaweicloudsdkwaf.v1.BotTypeDistributions`
        :param action_bucket: 
        :type action_bucket: :class:`huaweicloudsdkwaf.v1.ActionDistributions`
        """
        
        super(ListBotMRequestDistributionResponse, self).__init__()

        self._normal_bucket = None
        self._bot_classification_bucket = None
        self._action_bucket = None
        self.discriminator = None

        if normal_bucket is not None:
            self.normal_bucket = normal_bucket
        if bot_classification_bucket is not None:
            self.bot_classification_bucket = bot_classification_bucket
        if action_bucket is not None:
            self.action_bucket = action_bucket

    @property
    def normal_bucket(self):
        r"""Gets the normal_bucket of this ListBotMRequestDistributionResponse.

        :return: The normal_bucket of this ListBotMRequestDistributionResponse.
        :rtype: :class:`huaweicloudsdkwaf.v1.BotRequestDistributionsNormalBucket`
        """
        return self._normal_bucket

    @normal_bucket.setter
    def normal_bucket(self, normal_bucket):
        r"""Sets the normal_bucket of this ListBotMRequestDistributionResponse.

        :param normal_bucket: The normal_bucket of this ListBotMRequestDistributionResponse.
        :type normal_bucket: :class:`huaweicloudsdkwaf.v1.BotRequestDistributionsNormalBucket`
        """
        self._normal_bucket = normal_bucket

    @property
    def bot_classification_bucket(self):
        r"""Gets the bot_classification_bucket of this ListBotMRequestDistributionResponse.

        :return: The bot_classification_bucket of this ListBotMRequestDistributionResponse.
        :rtype: :class:`huaweicloudsdkwaf.v1.BotTypeDistributions`
        """
        return self._bot_classification_bucket

    @bot_classification_bucket.setter
    def bot_classification_bucket(self, bot_classification_bucket):
        r"""Sets the bot_classification_bucket of this ListBotMRequestDistributionResponse.

        :param bot_classification_bucket: The bot_classification_bucket of this ListBotMRequestDistributionResponse.
        :type bot_classification_bucket: :class:`huaweicloudsdkwaf.v1.BotTypeDistributions`
        """
        self._bot_classification_bucket = bot_classification_bucket

    @property
    def action_bucket(self):
        r"""Gets the action_bucket of this ListBotMRequestDistributionResponse.

        :return: The action_bucket of this ListBotMRequestDistributionResponse.
        :rtype: :class:`huaweicloudsdkwaf.v1.ActionDistributions`
        """
        return self._action_bucket

    @action_bucket.setter
    def action_bucket(self, action_bucket):
        r"""Sets the action_bucket of this ListBotMRequestDistributionResponse.

        :param action_bucket: The action_bucket of this ListBotMRequestDistributionResponse.
        :type action_bucket: :class:`huaweicloudsdkwaf.v1.ActionDistributions`
        """
        self._action_bucket = action_bucket

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
        if not isinstance(other, ListBotMRequestDistributionResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
