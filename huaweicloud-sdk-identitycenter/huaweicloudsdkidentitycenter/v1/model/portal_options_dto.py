# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PortalOptionsDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'visible': 'bool',
        'visibility': 'str',
        'sign_in_options': 'SignInOptionsDto'
    }

    attribute_map = {
        'visible': 'visible',
        'visibility': 'visibility',
        'sign_in_options': 'sign_in_options'
    }

    def __init__(self, visible=None, visibility=None, sign_in_options=None):
        r"""PortalOptionsDto

        The model defined in huaweicloud sdk

        :param visible: 应用程序在门户是否可见
        :type visible: bool
        :param visibility: 应用程序在门户可见性
        :type visibility: str
        :param sign_in_options: 
        :type sign_in_options: :class:`huaweicloudsdkidentitycenter.v1.SignInOptionsDto`
        """
        
        

        self._visible = None
        self._visibility = None
        self._sign_in_options = None
        self.discriminator = None

        if visible is not None:
            self.visible = visible
        if visibility is not None:
            self.visibility = visibility
        if sign_in_options is not None:
            self.sign_in_options = sign_in_options

    @property
    def visible(self):
        r"""Gets the visible of this PortalOptionsDto.

        应用程序在门户是否可见

        :return: The visible of this PortalOptionsDto.
        :rtype: bool
        """
        return self._visible

    @visible.setter
    def visible(self, visible):
        r"""Sets the visible of this PortalOptionsDto.

        应用程序在门户是否可见

        :param visible: The visible of this PortalOptionsDto.
        :type visible: bool
        """
        self._visible = visible

    @property
    def visibility(self):
        r"""Gets the visibility of this PortalOptionsDto.

        应用程序在门户可见性

        :return: The visibility of this PortalOptionsDto.
        :rtype: str
        """
        return self._visibility

    @visibility.setter
    def visibility(self, visibility):
        r"""Sets the visibility of this PortalOptionsDto.

        应用程序在门户可见性

        :param visibility: The visibility of this PortalOptionsDto.
        :type visibility: str
        """
        self._visibility = visibility

    @property
    def sign_in_options(self):
        r"""Gets the sign_in_options of this PortalOptionsDto.

        :return: The sign_in_options of this PortalOptionsDto.
        :rtype: :class:`huaweicloudsdkidentitycenter.v1.SignInOptionsDto`
        """
        return self._sign_in_options

    @sign_in_options.setter
    def sign_in_options(self, sign_in_options):
        r"""Sets the sign_in_options of this PortalOptionsDto.

        :param sign_in_options: The sign_in_options of this PortalOptionsDto.
        :type sign_in_options: :class:`huaweicloudsdkidentitycenter.v1.SignInOptionsDto`
        """
        self._sign_in_options = sign_in_options

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
        if not isinstance(other, PortalOptionsDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
