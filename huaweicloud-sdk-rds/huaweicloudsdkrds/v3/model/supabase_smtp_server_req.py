# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SupabaseSMTPServerReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'smtp_host': 'str',
        'smtp_port': 'int',
        'smtp_user': 'str',
        'smtp_pwd': 'str',
        'smtp_admin_email': 'str',
        'smtp_sender_name': 'str',
        'smtp_max_frequency': 'int'
    }

    attribute_map = {
        'smtp_host': 'smtp_host',
        'smtp_port': 'smtp_port',
        'smtp_user': 'smtp_user',
        'smtp_pwd': 'smtp_pwd',
        'smtp_admin_email': 'smtp_admin_email',
        'smtp_sender_name': 'smtp_sender_name',
        'smtp_max_frequency': 'smtp_max_frequency'
    }

    def __init__(self, smtp_host=None, smtp_port=None, smtp_user=None, smtp_pwd=None, smtp_admin_email=None, smtp_sender_name=None, smtp_max_frequency=None):
        r"""SupabaseSMTPServerReq

        The model defined in huaweicloud sdk

        :param smtp_host: 
        :type smtp_host: str
        :param smtp_port: 
        :type smtp_port: int
        :param smtp_user: 
        :type smtp_user: str
        :param smtp_pwd: 秘密，受控输入，show不返回。
        :type smtp_pwd: str
        :param smtp_admin_email: 
        :type smtp_admin_email: str
        :param smtp_sender_name: 
        :type smtp_sender_name: str
        :param smtp_max_frequency: 
        :type smtp_max_frequency: int
        """
        
        

        self._smtp_host = None
        self._smtp_port = None
        self._smtp_user = None
        self._smtp_pwd = None
        self._smtp_admin_email = None
        self._smtp_sender_name = None
        self._smtp_max_frequency = None
        self.discriminator = None

        if smtp_host is not None:
            self.smtp_host = smtp_host
        if smtp_port is not None:
            self.smtp_port = smtp_port
        if smtp_user is not None:
            self.smtp_user = smtp_user
        if smtp_pwd is not None:
            self.smtp_pwd = smtp_pwd
        if smtp_admin_email is not None:
            self.smtp_admin_email = smtp_admin_email
        if smtp_sender_name is not None:
            self.smtp_sender_name = smtp_sender_name
        if smtp_max_frequency is not None:
            self.smtp_max_frequency = smtp_max_frequency

    @property
    def smtp_host(self):
        r"""Gets the smtp_host of this SupabaseSMTPServerReq.

        :return: The smtp_host of this SupabaseSMTPServerReq.
        :rtype: str
        """
        return self._smtp_host

    @smtp_host.setter
    def smtp_host(self, smtp_host):
        r"""Sets the smtp_host of this SupabaseSMTPServerReq.

        :param smtp_host: The smtp_host of this SupabaseSMTPServerReq.
        :type smtp_host: str
        """
        self._smtp_host = smtp_host

    @property
    def smtp_port(self):
        r"""Gets the smtp_port of this SupabaseSMTPServerReq.

        :return: The smtp_port of this SupabaseSMTPServerReq.
        :rtype: int
        """
        return self._smtp_port

    @smtp_port.setter
    def smtp_port(self, smtp_port):
        r"""Sets the smtp_port of this SupabaseSMTPServerReq.

        :param smtp_port: The smtp_port of this SupabaseSMTPServerReq.
        :type smtp_port: int
        """
        self._smtp_port = smtp_port

    @property
    def smtp_user(self):
        r"""Gets the smtp_user of this SupabaseSMTPServerReq.

        :return: The smtp_user of this SupabaseSMTPServerReq.
        :rtype: str
        """
        return self._smtp_user

    @smtp_user.setter
    def smtp_user(self, smtp_user):
        r"""Sets the smtp_user of this SupabaseSMTPServerReq.

        :param smtp_user: The smtp_user of this SupabaseSMTPServerReq.
        :type smtp_user: str
        """
        self._smtp_user = smtp_user

    @property
    def smtp_pwd(self):
        r"""Gets the smtp_pwd of this SupabaseSMTPServerReq.

        秘密，受控输入，show不返回。

        :return: The smtp_pwd of this SupabaseSMTPServerReq.
        :rtype: str
        """
        return self._smtp_pwd

    @smtp_pwd.setter
    def smtp_pwd(self, smtp_pwd):
        r"""Sets the smtp_pwd of this SupabaseSMTPServerReq.

        秘密，受控输入，show不返回。

        :param smtp_pwd: The smtp_pwd of this SupabaseSMTPServerReq.
        :type smtp_pwd: str
        """
        self._smtp_pwd = smtp_pwd

    @property
    def smtp_admin_email(self):
        r"""Gets the smtp_admin_email of this SupabaseSMTPServerReq.

        :return: The smtp_admin_email of this SupabaseSMTPServerReq.
        :rtype: str
        """
        return self._smtp_admin_email

    @smtp_admin_email.setter
    def smtp_admin_email(self, smtp_admin_email):
        r"""Sets the smtp_admin_email of this SupabaseSMTPServerReq.

        :param smtp_admin_email: The smtp_admin_email of this SupabaseSMTPServerReq.
        :type smtp_admin_email: str
        """
        self._smtp_admin_email = smtp_admin_email

    @property
    def smtp_sender_name(self):
        r"""Gets the smtp_sender_name of this SupabaseSMTPServerReq.

        :return: The smtp_sender_name of this SupabaseSMTPServerReq.
        :rtype: str
        """
        return self._smtp_sender_name

    @smtp_sender_name.setter
    def smtp_sender_name(self, smtp_sender_name):
        r"""Sets the smtp_sender_name of this SupabaseSMTPServerReq.

        :param smtp_sender_name: The smtp_sender_name of this SupabaseSMTPServerReq.
        :type smtp_sender_name: str
        """
        self._smtp_sender_name = smtp_sender_name

    @property
    def smtp_max_frequency(self):
        r"""Gets the smtp_max_frequency of this SupabaseSMTPServerReq.

        :return: The smtp_max_frequency of this SupabaseSMTPServerReq.
        :rtype: int
        """
        return self._smtp_max_frequency

    @smtp_max_frequency.setter
    def smtp_max_frequency(self, smtp_max_frequency):
        r"""Sets the smtp_max_frequency of this SupabaseSMTPServerReq.

        :param smtp_max_frequency: The smtp_max_frequency of this SupabaseSMTPServerReq.
        :type smtp_max_frequency: int
        """
        self._smtp_max_frequency = smtp_max_frequency

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
        if not isinstance(other, SupabaseSMTPServerReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
