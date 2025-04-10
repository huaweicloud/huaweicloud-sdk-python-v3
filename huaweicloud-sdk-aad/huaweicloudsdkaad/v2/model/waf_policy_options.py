# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WafPolicyOptions:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cc': 'bool',
        'custom': 'bool',
        'geoip': 'bool',
        'whiteblackip': 'bool',
        'modulex_enabled': 'bool'
    }

    attribute_map = {
        'cc': 'cc',
        'custom': 'custom',
        'geoip': 'geoip',
        'whiteblackip': 'whiteblackip',
        'modulex_enabled': 'modulex_enabled'
    }

    def __init__(self, cc=None, custom=None, geoip=None, whiteblackip=None, modulex_enabled=None):
        r"""WafPolicyOptions

        The model defined in huaweicloud sdk

        :param cc: 是否开启CC（频率控制）
        :type cc: bool
        :param custom: 是否开启精准访问防护
        :type custom: bool
        :param geoip: 是否开启区域封禁防护
        :type geoip: bool
        :param whiteblackip: 是否开启黑白名单防护
        :type whiteblackip: bool
        :param modulex_enabled: 是否开启智能CC防护
        :type modulex_enabled: bool
        """
        
        

        self._cc = None
        self._custom = None
        self._geoip = None
        self._whiteblackip = None
        self._modulex_enabled = None
        self.discriminator = None

        if cc is not None:
            self.cc = cc
        if custom is not None:
            self.custom = custom
        if geoip is not None:
            self.geoip = geoip
        if whiteblackip is not None:
            self.whiteblackip = whiteblackip
        if modulex_enabled is not None:
            self.modulex_enabled = modulex_enabled

    @property
    def cc(self):
        r"""Gets the cc of this WafPolicyOptions.

        是否开启CC（频率控制）

        :return: The cc of this WafPolicyOptions.
        :rtype: bool
        """
        return self._cc

    @cc.setter
    def cc(self, cc):
        r"""Sets the cc of this WafPolicyOptions.

        是否开启CC（频率控制）

        :param cc: The cc of this WafPolicyOptions.
        :type cc: bool
        """
        self._cc = cc

    @property
    def custom(self):
        r"""Gets the custom of this WafPolicyOptions.

        是否开启精准访问防护

        :return: The custom of this WafPolicyOptions.
        :rtype: bool
        """
        return self._custom

    @custom.setter
    def custom(self, custom):
        r"""Sets the custom of this WafPolicyOptions.

        是否开启精准访问防护

        :param custom: The custom of this WafPolicyOptions.
        :type custom: bool
        """
        self._custom = custom

    @property
    def geoip(self):
        r"""Gets the geoip of this WafPolicyOptions.

        是否开启区域封禁防护

        :return: The geoip of this WafPolicyOptions.
        :rtype: bool
        """
        return self._geoip

    @geoip.setter
    def geoip(self, geoip):
        r"""Sets the geoip of this WafPolicyOptions.

        是否开启区域封禁防护

        :param geoip: The geoip of this WafPolicyOptions.
        :type geoip: bool
        """
        self._geoip = geoip

    @property
    def whiteblackip(self):
        r"""Gets the whiteblackip of this WafPolicyOptions.

        是否开启黑白名单防护

        :return: The whiteblackip of this WafPolicyOptions.
        :rtype: bool
        """
        return self._whiteblackip

    @whiteblackip.setter
    def whiteblackip(self, whiteblackip):
        r"""Sets the whiteblackip of this WafPolicyOptions.

        是否开启黑白名单防护

        :param whiteblackip: The whiteblackip of this WafPolicyOptions.
        :type whiteblackip: bool
        """
        self._whiteblackip = whiteblackip

    @property
    def modulex_enabled(self):
        r"""Gets the modulex_enabled of this WafPolicyOptions.

        是否开启智能CC防护

        :return: The modulex_enabled of this WafPolicyOptions.
        :rtype: bool
        """
        return self._modulex_enabled

    @modulex_enabled.setter
    def modulex_enabled(self, modulex_enabled):
        r"""Sets the modulex_enabled of this WafPolicyOptions.

        是否开启智能CC防护

        :param modulex_enabled: The modulex_enabled of this WafPolicyOptions.
        :type modulex_enabled: bool
        """
        self._modulex_enabled = modulex_enabled

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
        if not isinstance(other, WafPolicyOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
