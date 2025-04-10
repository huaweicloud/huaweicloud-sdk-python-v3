# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteKafkaUserClientQuotaTaskReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'user': 'str',
        'client': 'str',
        'user_default': 'bool',
        'client_default': 'bool'
    }

    attribute_map = {
        'user': 'user',
        'client': 'client',
        'user_default': 'user-default',
        'client_default': 'client-default'
    }

    def __init__(self, user=None, client=None, user_default=None, client_default=None):
        r"""DeleteKafkaUserClientQuotaTaskReq

        The model defined in huaweicloud sdk

        :param user: 用户名。  不对全部用户/客户端限流时，用户名和客户端ID不能同时为空。
        :type user: str
        :param client: 客户端ID。  不对全部用户/客户端限流时，用户名和客户端ID不能同时为空。
        :type client: str
        :param user_default: 是否使用用户默认设置。   - 是，表示对全部用户限流。此时不能同时设置用户名。   - 否，表示对特定用户限流。此时需要设置用户名。
        :type user_default: bool
        :param client_default: 是否使用客户端默认设置。   - 是，表示对全部客户端限流。此时不能设置客户端ID。   - 否，表示对特定客户端限流。此时需要设置客户端ID。
        :type client_default: bool
        """
        
        

        self._user = None
        self._client = None
        self._user_default = None
        self._client_default = None
        self.discriminator = None

        if user is not None:
            self.user = user
        if client is not None:
            self.client = client
        if user_default is not None:
            self.user_default = user_default
        if client_default is not None:
            self.client_default = client_default

    @property
    def user(self):
        r"""Gets the user of this DeleteKafkaUserClientQuotaTaskReq.

        用户名。  不对全部用户/客户端限流时，用户名和客户端ID不能同时为空。

        :return: The user of this DeleteKafkaUserClientQuotaTaskReq.
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        r"""Sets the user of this DeleteKafkaUserClientQuotaTaskReq.

        用户名。  不对全部用户/客户端限流时，用户名和客户端ID不能同时为空。

        :param user: The user of this DeleteKafkaUserClientQuotaTaskReq.
        :type user: str
        """
        self._user = user

    @property
    def client(self):
        r"""Gets the client of this DeleteKafkaUserClientQuotaTaskReq.

        客户端ID。  不对全部用户/客户端限流时，用户名和客户端ID不能同时为空。

        :return: The client of this DeleteKafkaUserClientQuotaTaskReq.
        :rtype: str
        """
        return self._client

    @client.setter
    def client(self, client):
        r"""Sets the client of this DeleteKafkaUserClientQuotaTaskReq.

        客户端ID。  不对全部用户/客户端限流时，用户名和客户端ID不能同时为空。

        :param client: The client of this DeleteKafkaUserClientQuotaTaskReq.
        :type client: str
        """
        self._client = client

    @property
    def user_default(self):
        r"""Gets the user_default of this DeleteKafkaUserClientQuotaTaskReq.

        是否使用用户默认设置。   - 是，表示对全部用户限流。此时不能同时设置用户名。   - 否，表示对特定用户限流。此时需要设置用户名。

        :return: The user_default of this DeleteKafkaUserClientQuotaTaskReq.
        :rtype: bool
        """
        return self._user_default

    @user_default.setter
    def user_default(self, user_default):
        r"""Sets the user_default of this DeleteKafkaUserClientQuotaTaskReq.

        是否使用用户默认设置。   - 是，表示对全部用户限流。此时不能同时设置用户名。   - 否，表示对特定用户限流。此时需要设置用户名。

        :param user_default: The user_default of this DeleteKafkaUserClientQuotaTaskReq.
        :type user_default: bool
        """
        self._user_default = user_default

    @property
    def client_default(self):
        r"""Gets the client_default of this DeleteKafkaUserClientQuotaTaskReq.

        是否使用客户端默认设置。   - 是，表示对全部客户端限流。此时不能设置客户端ID。   - 否，表示对特定客户端限流。此时需要设置客户端ID。

        :return: The client_default of this DeleteKafkaUserClientQuotaTaskReq.
        :rtype: bool
        """
        return self._client_default

    @client_default.setter
    def client_default(self, client_default):
        r"""Sets the client_default of this DeleteKafkaUserClientQuotaTaskReq.

        是否使用客户端默认设置。   - 是，表示对全部客户端限流。此时不能设置客户端ID。   - 否，表示对特定客户端限流。此时需要设置客户端ID。

        :param client_default: The client_default of this DeleteKafkaUserClientQuotaTaskReq.
        :type client_default: bool
        """
        self._client_default = client_default

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
        if not isinstance(other, DeleteKafkaUserClientQuotaTaskReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
