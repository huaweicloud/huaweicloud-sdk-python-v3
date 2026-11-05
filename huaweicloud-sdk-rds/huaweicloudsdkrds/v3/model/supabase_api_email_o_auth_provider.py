# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SupabaseApiEmailOAuthProvider:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enable_email_sign_up': 'bool',
        'enable_email_auto_confirm': 'bool',
        'smtp_config': 'SupabaseApiSMTPServer'
    }

    attribute_map = {
        'enable_email_sign_up': 'enable_email_sign_up',
        'enable_email_auto_confirm': 'enable_email_auto_confirm',
        'smtp_config': 'smtp_config'
    }

    def __init__(self, enable_email_sign_up=None, enable_email_auto_confirm=None, smtp_config=None):
        r"""SupabaseApiEmailOAuthProvider

        The model defined in huaweicloud sdk

        :param enable_email_sign_up: 
        :type enable_email_sign_up: bool
        :param enable_email_auto_confirm: 
        :type enable_email_auto_confirm: bool
        :param smtp_config: 
        :type smtp_config: :class:`huaweicloudsdkrds.v3.SupabaseApiSMTPServer`
        """
        
        

        self._enable_email_sign_up = None
        self._enable_email_auto_confirm = None
        self._smtp_config = None
        self.discriminator = None

        if enable_email_sign_up is not None:
            self.enable_email_sign_up = enable_email_sign_up
        if enable_email_auto_confirm is not None:
            self.enable_email_auto_confirm = enable_email_auto_confirm
        if smtp_config is not None:
            self.smtp_config = smtp_config

    @property
    def enable_email_sign_up(self):
        r"""Gets the enable_email_sign_up of this SupabaseApiEmailOAuthProvider.

        :return: The enable_email_sign_up of this SupabaseApiEmailOAuthProvider.
        :rtype: bool
        """
        return self._enable_email_sign_up

    @enable_email_sign_up.setter
    def enable_email_sign_up(self, enable_email_sign_up):
        r"""Sets the enable_email_sign_up of this SupabaseApiEmailOAuthProvider.

        :param enable_email_sign_up: The enable_email_sign_up of this SupabaseApiEmailOAuthProvider.
        :type enable_email_sign_up: bool
        """
        self._enable_email_sign_up = enable_email_sign_up

    @property
    def enable_email_auto_confirm(self):
        r"""Gets the enable_email_auto_confirm of this SupabaseApiEmailOAuthProvider.

        :return: The enable_email_auto_confirm of this SupabaseApiEmailOAuthProvider.
        :rtype: bool
        """
        return self._enable_email_auto_confirm

    @enable_email_auto_confirm.setter
    def enable_email_auto_confirm(self, enable_email_auto_confirm):
        r"""Sets the enable_email_auto_confirm of this SupabaseApiEmailOAuthProvider.

        :param enable_email_auto_confirm: The enable_email_auto_confirm of this SupabaseApiEmailOAuthProvider.
        :type enable_email_auto_confirm: bool
        """
        self._enable_email_auto_confirm = enable_email_auto_confirm

    @property
    def smtp_config(self):
        r"""Gets the smtp_config of this SupabaseApiEmailOAuthProvider.

        :return: The smtp_config of this SupabaseApiEmailOAuthProvider.
        :rtype: :class:`huaweicloudsdkrds.v3.SupabaseApiSMTPServer`
        """
        return self._smtp_config

    @smtp_config.setter
    def smtp_config(self, smtp_config):
        r"""Sets the smtp_config of this SupabaseApiEmailOAuthProvider.

        :param smtp_config: The smtp_config of this SupabaseApiEmailOAuthProvider.
        :type smtp_config: :class:`huaweicloudsdkrds.v3.SupabaseApiSMTPServer`
        """
        self._smtp_config = smtp_config

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SupabaseApiEmailOAuthProvider):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
