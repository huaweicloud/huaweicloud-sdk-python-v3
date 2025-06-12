# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SecurityOptions:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'secure_boot_enabled': 'bool',
        'tpm_enabled': 'bool'
    }

    attribute_map = {
        'secure_boot_enabled': 'secure_boot_enabled',
        'tpm_enabled': 'tpm_enabled'
    }

    def __init__(self, secure_boot_enabled=None, tpm_enabled=None):
        r"""SecurityOptions

        The model defined in huaweicloud sdk

        :param secure_boot_enabled: 是否支持安全启动 true:支持安全启动 false:不支持安全启动 默认值：false
        :type secure_boot_enabled: bool
        :param tpm_enabled: 是否支持vtpm启动 true:支持vtpm启动 false:不支持vtpm启动 默认值：false
        :type tpm_enabled: bool
        """
        
        

        self._secure_boot_enabled = None
        self._tpm_enabled = None
        self.discriminator = None

        if secure_boot_enabled is not None:
            self.secure_boot_enabled = secure_boot_enabled
        if tpm_enabled is not None:
            self.tpm_enabled = tpm_enabled

    @property
    def secure_boot_enabled(self):
        r"""Gets the secure_boot_enabled of this SecurityOptions.

        是否支持安全启动 true:支持安全启动 false:不支持安全启动 默认值：false

        :return: The secure_boot_enabled of this SecurityOptions.
        :rtype: bool
        """
        return self._secure_boot_enabled

    @secure_boot_enabled.setter
    def secure_boot_enabled(self, secure_boot_enabled):
        r"""Sets the secure_boot_enabled of this SecurityOptions.

        是否支持安全启动 true:支持安全启动 false:不支持安全启动 默认值：false

        :param secure_boot_enabled: The secure_boot_enabled of this SecurityOptions.
        :type secure_boot_enabled: bool
        """
        self._secure_boot_enabled = secure_boot_enabled

    @property
    def tpm_enabled(self):
        r"""Gets the tpm_enabled of this SecurityOptions.

        是否支持vtpm启动 true:支持vtpm启动 false:不支持vtpm启动 默认值：false

        :return: The tpm_enabled of this SecurityOptions.
        :rtype: bool
        """
        return self._tpm_enabled

    @tpm_enabled.setter
    def tpm_enabled(self, tpm_enabled):
        r"""Sets the tpm_enabled of this SecurityOptions.

        是否支持vtpm启动 true:支持vtpm启动 false:不支持vtpm启动 默认值：false

        :param tpm_enabled: The tpm_enabled of this SecurityOptions.
        :type tpm_enabled: bool
        """
        self._tpm_enabled = tpm_enabled

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
        if not isinstance(other, SecurityOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
