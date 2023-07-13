# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ChannelConfigBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'smn': 'TrackerSMNChannelConfigBody',
        'obs': 'TrackerOBSChannelConfigBody'
    }

    attribute_map = {
        'smn': 'smn',
        'obs': 'obs'
    }

    def __init__(self, smn=None, obs=None):
        """ChannelConfigBody

        The model defined in huaweicloud sdk

        :param smn: 
        :type smn: :class:`huaweicloudsdkconfig.v1.TrackerSMNChannelConfigBody`
        :param obs: 
        :type obs: :class:`huaweicloudsdkconfig.v1.TrackerOBSChannelConfigBody`
        """
        
        

        self._smn = None
        self._obs = None
        self.discriminator = None

        if smn is not None:
            self.smn = smn
        if obs is not None:
            self.obs = obs

    @property
    def smn(self):
        """Gets the smn of this ChannelConfigBody.

        :return: The smn of this ChannelConfigBody.
        :rtype: :class:`huaweicloudsdkconfig.v1.TrackerSMNChannelConfigBody`
        """
        return self._smn

    @smn.setter
    def smn(self, smn):
        """Sets the smn of this ChannelConfigBody.

        :param smn: The smn of this ChannelConfigBody.
        :type smn: :class:`huaweicloudsdkconfig.v1.TrackerSMNChannelConfigBody`
        """
        self._smn = smn

    @property
    def obs(self):
        """Gets the obs of this ChannelConfigBody.

        :return: The obs of this ChannelConfigBody.
        :rtype: :class:`huaweicloudsdkconfig.v1.TrackerOBSChannelConfigBody`
        """
        return self._obs

    @obs.setter
    def obs(self, obs):
        """Sets the obs of this ChannelConfigBody.

        :param obs: The obs of this ChannelConfigBody.
        :type obs: :class:`huaweicloudsdkconfig.v1.TrackerOBSChannelConfigBody`
        """
        self._obs = obs

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
        if not isinstance(other, ChannelConfigBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
