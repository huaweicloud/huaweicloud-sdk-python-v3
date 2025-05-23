# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Sbc:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'sbc_automatic_disconnection': 'str',
        'sbc_automatic_disconnection_options': 'SbcAutomaticDisconnectionOptions'
    }

    attribute_map = {
        'sbc_automatic_disconnection': 'sbc_automatic_disconnection',
        'sbc_automatic_disconnection_options': 'sbc_automatic_disconnection_options'
    }

    def __init__(self, sbc_automatic_disconnection=None, sbc_automatic_disconnection_options=None):
        r"""Sbc

        The model defined in huaweicloud sdk

        :param sbc_automatic_disconnection: 连接策略： - DISABLED：已禁用 - AUTO_DISCONNECT：自动断开 - AUTO_LOCK：自动锁屏
        :type sbc_automatic_disconnection: str
        :param sbc_automatic_disconnection_options: 
        :type sbc_automatic_disconnection_options: :class:`huaweicloudsdkworkspaceapp.v1.SbcAutomaticDisconnectionOptions`
        """
        
        

        self._sbc_automatic_disconnection = None
        self._sbc_automatic_disconnection_options = None
        self.discriminator = None

        if sbc_automatic_disconnection is not None:
            self.sbc_automatic_disconnection = sbc_automatic_disconnection
        if sbc_automatic_disconnection_options is not None:
            self.sbc_automatic_disconnection_options = sbc_automatic_disconnection_options

    @property
    def sbc_automatic_disconnection(self):
        r"""Gets the sbc_automatic_disconnection of this Sbc.

        连接策略： - DISABLED：已禁用 - AUTO_DISCONNECT：自动断开 - AUTO_LOCK：自动锁屏

        :return: The sbc_automatic_disconnection of this Sbc.
        :rtype: str
        """
        return self._sbc_automatic_disconnection

    @sbc_automatic_disconnection.setter
    def sbc_automatic_disconnection(self, sbc_automatic_disconnection):
        r"""Sets the sbc_automatic_disconnection of this Sbc.

        连接策略： - DISABLED：已禁用 - AUTO_DISCONNECT：自动断开 - AUTO_LOCK：自动锁屏

        :param sbc_automatic_disconnection: The sbc_automatic_disconnection of this Sbc.
        :type sbc_automatic_disconnection: str
        """
        self._sbc_automatic_disconnection = sbc_automatic_disconnection

    @property
    def sbc_automatic_disconnection_options(self):
        r"""Gets the sbc_automatic_disconnection_options of this Sbc.

        :return: The sbc_automatic_disconnection_options of this Sbc.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.SbcAutomaticDisconnectionOptions`
        """
        return self._sbc_automatic_disconnection_options

    @sbc_automatic_disconnection_options.setter
    def sbc_automatic_disconnection_options(self, sbc_automatic_disconnection_options):
        r"""Sets the sbc_automatic_disconnection_options of this Sbc.

        :param sbc_automatic_disconnection_options: The sbc_automatic_disconnection_options of this Sbc.
        :type sbc_automatic_disconnection_options: :class:`huaweicloudsdkworkspaceapp.v1.SbcAutomaticDisconnectionOptions`
        """
        self._sbc_automatic_disconnection_options = sbc_automatic_disconnection_options

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
        if not isinstance(other, Sbc):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
