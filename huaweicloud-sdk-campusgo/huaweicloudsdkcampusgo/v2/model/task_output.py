# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TaskOutput:

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
        'localpath': 'TaskOutputLocalpath'
    }

    attribute_map = {
        'obs': 'obs',
        'dis': 'dis',
        'webhook': 'webhook',
        'localpath': 'localpath'
    }

    def __init__(self, obs=None, dis=None, webhook=None, localpath=None):
        """TaskOutput

        The model defined in huaweicloud sdk

        :param obs: 
        :type obs: :class:`huaweicloudsdkcampusgo.v2.TaskOutputObs`
        :param dis: 
        :type dis: :class:`huaweicloudsdkcampusgo.v2.TaskOutputDis`
        :param webhook: 
        :type webhook: :class:`huaweicloudsdkcampusgo.v2.TaskOutputWebhook`
        :param localpath: 
        :type localpath: :class:`huaweicloudsdkcampusgo.v2.TaskOutputLocalpath`
        """
        
        

        self._obs = None
        self._dis = None
        self._webhook = None
        self._localpath = None
        self.discriminator = None

        if obs is not None:
            self.obs = obs
        if dis is not None:
            self.dis = dis
        if webhook is not None:
            self.webhook = webhook
        if localpath is not None:
            self.localpath = localpath

    @property
    def obs(self):
        """Gets the obs of this TaskOutput.


        :return: The obs of this TaskOutput.
        :rtype: :class:`huaweicloudsdkcampusgo.v2.TaskOutputObs`
        """
        return self._obs

    @obs.setter
    def obs(self, obs):
        """Sets the obs of this TaskOutput.


        :param obs: The obs of this TaskOutput.
        :type obs: :class:`huaweicloudsdkcampusgo.v2.TaskOutputObs`
        """
        self._obs = obs

    @property
    def dis(self):
        """Gets the dis of this TaskOutput.


        :return: The dis of this TaskOutput.
        :rtype: :class:`huaweicloudsdkcampusgo.v2.TaskOutputDis`
        """
        return self._dis

    @dis.setter
    def dis(self, dis):
        """Sets the dis of this TaskOutput.


        :param dis: The dis of this TaskOutput.
        :type dis: :class:`huaweicloudsdkcampusgo.v2.TaskOutputDis`
        """
        self._dis = dis

    @property
    def webhook(self):
        """Gets the webhook of this TaskOutput.


        :return: The webhook of this TaskOutput.
        :rtype: :class:`huaweicloudsdkcampusgo.v2.TaskOutputWebhook`
        """
        return self._webhook

    @webhook.setter
    def webhook(self, webhook):
        """Sets the webhook of this TaskOutput.


        :param webhook: The webhook of this TaskOutput.
        :type webhook: :class:`huaweicloudsdkcampusgo.v2.TaskOutputWebhook`
        """
        self._webhook = webhook

    @property
    def localpath(self):
        """Gets the localpath of this TaskOutput.


        :return: The localpath of this TaskOutput.
        :rtype: :class:`huaweicloudsdkcampusgo.v2.TaskOutputLocalpath`
        """
        return self._localpath

    @localpath.setter
    def localpath(self, localpath):
        """Sets the localpath of this TaskOutput.


        :param localpath: The localpath of this TaskOutput.
        :type localpath: :class:`huaweicloudsdkcampusgo.v2.TaskOutputLocalpath`
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
        if not isinstance(other, TaskOutput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
