# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TaskOutputForDisplay:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'obs': 'TaskOutputObs',
        'dis': 'TaskOutputDis',
        'webhook': 'TaskOutputWebhook',
        'hosting': 'TaskOutputHostingForDisplay',
        'localpath': 'TaskOutputLocalpath'
    }

    attribute_map = {
        'obs': 'obs',
        'dis': 'dis',
        'webhook': 'webhook',
        'hosting': 'hosting',
        'localpath': 'localpath'
    }

    def __init__(self, obs=None, dis=None, webhook=None, hosting=None, localpath=None):
        """TaskOutputForDisplay

        The model defined in huaweicloud sdk

        :param obs: 
        :type obs: :class:`huaweicloudsdkvas.v2.TaskOutputObs`
        :param dis: 
        :type dis: :class:`huaweicloudsdkvas.v2.TaskOutputDis`
        :param webhook: 
        :type webhook: :class:`huaweicloudsdkvas.v2.TaskOutputWebhook`
        :param hosting: 
        :type hosting: :class:`huaweicloudsdkvas.v2.TaskOutputHostingForDisplay`
        :param localpath: 
        :type localpath: :class:`huaweicloudsdkvas.v2.TaskOutputLocalpath`
        """
        
        

        self._obs = None
        self._dis = None
        self._webhook = None
        self._hosting = None
        self._localpath = None
        self.discriminator = None

        if obs is not None:
            self.obs = obs
        if dis is not None:
            self.dis = dis
        if webhook is not None:
            self.webhook = webhook
        if hosting is not None:
            self.hosting = hosting
        if localpath is not None:
            self.localpath = localpath

    @property
    def obs(self):
        """Gets the obs of this TaskOutputForDisplay.

        :return: The obs of this TaskOutputForDisplay.
        :rtype: :class:`huaweicloudsdkvas.v2.TaskOutputObs`
        """
        return self._obs

    @obs.setter
    def obs(self, obs):
        """Sets the obs of this TaskOutputForDisplay.

        :param obs: The obs of this TaskOutputForDisplay.
        :type obs: :class:`huaweicloudsdkvas.v2.TaskOutputObs`
        """
        self._obs = obs

    @property
    def dis(self):
        """Gets the dis of this TaskOutputForDisplay.

        :return: The dis of this TaskOutputForDisplay.
        :rtype: :class:`huaweicloudsdkvas.v2.TaskOutputDis`
        """
        return self._dis

    @dis.setter
    def dis(self, dis):
        """Sets the dis of this TaskOutputForDisplay.

        :param dis: The dis of this TaskOutputForDisplay.
        :type dis: :class:`huaweicloudsdkvas.v2.TaskOutputDis`
        """
        self._dis = dis

    @property
    def webhook(self):
        """Gets the webhook of this TaskOutputForDisplay.

        :return: The webhook of this TaskOutputForDisplay.
        :rtype: :class:`huaweicloudsdkvas.v2.TaskOutputWebhook`
        """
        return self._webhook

    @webhook.setter
    def webhook(self, webhook):
        """Sets the webhook of this TaskOutputForDisplay.

        :param webhook: The webhook of this TaskOutputForDisplay.
        :type webhook: :class:`huaweicloudsdkvas.v2.TaskOutputWebhook`
        """
        self._webhook = webhook

    @property
    def hosting(self):
        """Gets the hosting of this TaskOutputForDisplay.

        :return: The hosting of this TaskOutputForDisplay.
        :rtype: :class:`huaweicloudsdkvas.v2.TaskOutputHostingForDisplay`
        """
        return self._hosting

    @hosting.setter
    def hosting(self, hosting):
        """Sets the hosting of this TaskOutputForDisplay.

        :param hosting: The hosting of this TaskOutputForDisplay.
        :type hosting: :class:`huaweicloudsdkvas.v2.TaskOutputHostingForDisplay`
        """
        self._hosting = hosting

    @property
    def localpath(self):
        """Gets the localpath of this TaskOutputForDisplay.

        :return: The localpath of this TaskOutputForDisplay.
        :rtype: :class:`huaweicloudsdkvas.v2.TaskOutputLocalpath`
        """
        return self._localpath

    @localpath.setter
    def localpath(self, localpath):
        """Sets the localpath of this TaskOutputForDisplay.

        :param localpath: The localpath of this TaskOutputForDisplay.
        :type localpath: :class:`huaweicloudsdkvas.v2.TaskOutputLocalpath`
        """
        self._localpath = localpath

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
        if not isinstance(other, TaskOutputForDisplay):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
