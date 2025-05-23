# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AudioOutput:

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
        'hosting': 'AudioOutputHosting'
    }

    attribute_map = {
        'obs': 'obs',
        'hosting': 'hosting'
    }

    def __init__(self, obs=None, hosting=None):
        r"""AudioOutput

        The model defined in huaweicloud sdk

        :param obs: 
        :type obs: :class:`huaweicloudsdkvcm.v2.AudioOutputObs`
        :param hosting: 
        :type hosting: :class:`huaweicloudsdkvcm.v2.AudioOutputHosting`
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
        r"""Gets the obs of this AudioOutput.

        :return: The obs of this AudioOutput.
        :rtype: :class:`huaweicloudsdkvcm.v2.AudioOutputObs`
        """
        return self._obs

    @obs.setter
    def obs(self, obs):
        r"""Sets the obs of this AudioOutput.

        :param obs: The obs of this AudioOutput.
        :type obs: :class:`huaweicloudsdkvcm.v2.AudioOutputObs`
        """
        self._obs = obs

    @property
    def hosting(self):
        r"""Gets the hosting of this AudioOutput.

        :return: The hosting of this AudioOutput.
        :rtype: :class:`huaweicloudsdkvcm.v2.AudioOutputHosting`
        """
        return self._hosting

    @hosting.setter
    def hosting(self, hosting):
        r"""Sets the hosting of this AudioOutput.

        :param hosting: The hosting of this AudioOutput.
        :type hosting: :class:`huaweicloudsdkvcm.v2.AudioOutputHosting`
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
        if not isinstance(other, AudioOutput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
