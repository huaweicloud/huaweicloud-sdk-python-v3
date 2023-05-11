# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FileLocation:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'obs_location': 'ObsLocation'
    }

    attribute_map = {
        'obs_location': 'obs_location'
    }

    def __init__(self, obs_location=None):
        """FileLocation

        The model defined in huaweicloud sdk

        :param obs_location: 
        :type obs_location: :class:`huaweicloudsdkiotda.v5.ObsLocation`
        """
        
        

        self._obs_location = None
        self.discriminator = None

        if obs_location is not None:
            self.obs_location = obs_location

    @property
    def obs_location(self):
        """Gets the obs_location of this FileLocation.

        :return: The obs_location of this FileLocation.
        :rtype: :class:`huaweicloudsdkiotda.v5.ObsLocation`
        """
        return self._obs_location

    @obs_location.setter
    def obs_location(self, obs_location):
        """Sets the obs_location of this FileLocation.

        :param obs_location: The obs_location of this FileLocation.
        :type obs_location: :class:`huaweicloudsdkiotda.v5.ObsLocation`
        """
        self._obs_location = obs_location

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
        if not isinstance(other, FileLocation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
