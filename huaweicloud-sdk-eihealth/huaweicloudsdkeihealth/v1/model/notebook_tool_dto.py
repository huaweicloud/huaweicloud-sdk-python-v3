# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NotebookToolDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'display_name': 'str',
        'profile': 'Profile'
    }

    attribute_map = {
        'display_name': 'display_name',
        'profile': 'profile'
    }

    def __init__(self, display_name=None, profile=None):
        """NotebookToolDto

        The model defined in huaweicloud sdk

        :param display_name: 显示名称
        :type display_name: str
        :param profile: 
        :type profile: :class:`huaweicloudsdkeihealth.v1.Profile`
        """
        
        

        self._display_name = None
        self._profile = None
        self.discriminator = None

        self.display_name = display_name
        self.profile = profile

    @property
    def display_name(self):
        """Gets the display_name of this NotebookToolDto.

        显示名称

        :return: The display_name of this NotebookToolDto.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this NotebookToolDto.

        显示名称

        :param display_name: The display_name of this NotebookToolDto.
        :type display_name: str
        """
        self._display_name = display_name

    @property
    def profile(self):
        """Gets the profile of this NotebookToolDto.

        :return: The profile of this NotebookToolDto.
        :rtype: :class:`huaweicloudsdkeihealth.v1.Profile`
        """
        return self._profile

    @profile.setter
    def profile(self, profile):
        """Sets the profile of this NotebookToolDto.

        :param profile: The profile of this NotebookToolDto.
        :type profile: :class:`huaweicloudsdkeihealth.v1.Profile`
        """
        self._profile = profile

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
        if not isinstance(other, NotebookToolDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
