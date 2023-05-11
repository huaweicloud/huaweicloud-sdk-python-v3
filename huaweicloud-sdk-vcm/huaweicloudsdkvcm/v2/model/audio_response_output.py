# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AudioResponseOutput:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'obs': 'AudioOutputObs',
        'hosting': 'AudioResponseOutputHosting'
    }

    attribute_map = {
        'obs': 'obs',
        'hosting': 'hosting'
    }

    def __init__(self, obs=None, hosting=None):
        """AudioResponseOutput

        The model defined in huaweicloud sdk

        :param obs: 
        :type obs: :class:`huaweicloudsdkvcm.v2.AudioOutputObs`
        :param hosting: 
        :type hosting: :class:`huaweicloudsdkvcm.v2.AudioResponseOutputHosting`
        """
        
        

        self._obs = None
        self._hosting = None
        self.discriminator = None

        if obs is not None:
            self.obs = obs
        if hosting is not None:
            self.hosting = hosting

    @property
    def obs(self):
        """Gets the obs of this AudioResponseOutput.

        :return: The obs of this AudioResponseOutput.
        :rtype: :class:`huaweicloudsdkvcm.v2.AudioOutputObs`
        """
        return self._obs

    @obs.setter
    def obs(self, obs):
        """Sets the obs of this AudioResponseOutput.

        :param obs: The obs of this AudioResponseOutput.
        :type obs: :class:`huaweicloudsdkvcm.v2.AudioOutputObs`
        """
        self._obs = obs

    @property
    def hosting(self):
        """Gets the hosting of this AudioResponseOutput.

        :return: The hosting of this AudioResponseOutput.
        :rtype: :class:`huaweicloudsdkvcm.v2.AudioResponseOutputHosting`
        """
        return self._hosting

    @hosting.setter
    def hosting(self, hosting):
        """Sets the hosting of this AudioResponseOutput.

        :param hosting: The hosting of this AudioResponseOutput.
        :type hosting: :class:`huaweicloudsdkvcm.v2.AudioResponseOutputHosting`
        """
        self._hosting = hosting

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
        if not isinstance(other, AudioResponseOutput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
