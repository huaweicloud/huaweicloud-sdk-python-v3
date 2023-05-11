# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Output:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'obs': 'OutputObs',
        'hosting': 'OutputHosting',
        'dis': 'OutputDis',
        'webhook': 'OutputWebhook',
        'localpath': 'OutputLocalpath'
    }

    attribute_map = {
        'obs': 'obs',
        'hosting': 'hosting',
        'dis': 'dis',
        'webhook': 'webhook',
        'localpath': 'localpath'
    }

    def __init__(self, obs=None, hosting=None, dis=None, webhook=None, localpath=None):
        """Output

        The model defined in huaweicloud sdk

        :param obs: 
        :type obs: :class:`huaweicloudsdkvcm.v2.OutputObs`
        :param hosting: 
        :type hosting: :class:`huaweicloudsdkvcm.v2.OutputHosting`
        :param dis: 
        :type dis: :class:`huaweicloudsdkvcm.v2.OutputDis`
        :param webhook: 
        :type webhook: :class:`huaweicloudsdkvcm.v2.OutputWebhook`
        :param localpath: 
        :type localpath: :class:`huaweicloudsdkvcm.v2.OutputLocalpath`
        """
        
        

        self._obs = None
        self._hosting = None
        self._dis = None
        self._webhook = None
        self._localpath = None
        self.discriminator = None

        if obs is not None:
            self.obs = obs
        if hosting is not None:
            self.hosting = hosting
        if dis is not None:
            self.dis = dis
        if webhook is not None:
            self.webhook = webhook
        if localpath is not None:
            self.localpath = localpath

    @property
    def obs(self):
        """Gets the obs of this Output.

        :return: The obs of this Output.
        :rtype: :class:`huaweicloudsdkvcm.v2.OutputObs`
        """
        return self._obs

    @obs.setter
    def obs(self, obs):
        """Sets the obs of this Output.

        :param obs: The obs of this Output.
        :type obs: :class:`huaweicloudsdkvcm.v2.OutputObs`
        """
        self._obs = obs

    @property
    def hosting(self):
        """Gets the hosting of this Output.

        :return: The hosting of this Output.
        :rtype: :class:`huaweicloudsdkvcm.v2.OutputHosting`
        """
        return self._hosting

    @hosting.setter
    def hosting(self, hosting):
        """Sets the hosting of this Output.

        :param hosting: The hosting of this Output.
        :type hosting: :class:`huaweicloudsdkvcm.v2.OutputHosting`
        """
        self._hosting = hosting

    @property
    def dis(self):
        """Gets the dis of this Output.

        :return: The dis of this Output.
        :rtype: :class:`huaweicloudsdkvcm.v2.OutputDis`
        """
        return self._dis

    @dis.setter
    def dis(self, dis):
        """Sets the dis of this Output.

        :param dis: The dis of this Output.
        :type dis: :class:`huaweicloudsdkvcm.v2.OutputDis`
        """
        self._dis = dis

    @property
    def webhook(self):
        """Gets the webhook of this Output.

        :return: The webhook of this Output.
        :rtype: :class:`huaweicloudsdkvcm.v2.OutputWebhook`
        """
        return self._webhook

    @webhook.setter
    def webhook(self, webhook):
        """Sets the webhook of this Output.

        :param webhook: The webhook of this Output.
        :type webhook: :class:`huaweicloudsdkvcm.v2.OutputWebhook`
        """
        self._webhook = webhook

    @property
    def localpath(self):
        """Gets the localpath of this Output.

        :return: The localpath of this Output.
        :rtype: :class:`huaweicloudsdkvcm.v2.OutputLocalpath`
        """
        return self._localpath

    @localpath.setter
    def localpath(self, localpath):
        """Sets the localpath of this Output.

        :param localpath: The localpath of this Output.
        :type localpath: :class:`huaweicloudsdkvcm.v2.OutputLocalpath`
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
        if not isinstance(other, Output):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
