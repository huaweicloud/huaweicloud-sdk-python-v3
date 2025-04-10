# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PoliciesClientClientType:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'client_type_limit': 'bool',
        'options': 'PoliciesClientClientTypeOptions'
    }

    attribute_map = {
        'client_type_limit': 'client_type_limit',
        'options': 'options'
    }

    def __init__(self, client_type_limit=None, options=None):
        r"""PoliciesClientClientType

        The model defined in huaweicloud sdk

        :param client_type_limit: 是否开启终端类型登录管控。 false：表示关闭。 true：表示开启。
        :type client_type_limit: bool
        :param options: 
        :type options: :class:`huaweicloudsdkworkspace.v2.PoliciesClientClientTypeOptions`
        """
        
        

        self._client_type_limit = None
        self._options = None
        self.discriminator = None

        if client_type_limit is not None:
            self.client_type_limit = client_type_limit
        if options is not None:
            self.options = options

    @property
    def client_type_limit(self):
        r"""Gets the client_type_limit of this PoliciesClientClientType.

        是否开启终端类型登录管控。 false：表示关闭。 true：表示开启。

        :return: The client_type_limit of this PoliciesClientClientType.
        :rtype: bool
        """
        return self._client_type_limit

    @client_type_limit.setter
    def client_type_limit(self, client_type_limit):
        r"""Sets the client_type_limit of this PoliciesClientClientType.

        是否开启终端类型登录管控。 false：表示关闭。 true：表示开启。

        :param client_type_limit: The client_type_limit of this PoliciesClientClientType.
        :type client_type_limit: bool
        """
        self._client_type_limit = client_type_limit

    @property
    def options(self):
        r"""Gets the options of this PoliciesClientClientType.

        :return: The options of this PoliciesClientClientType.
        :rtype: :class:`huaweicloudsdkworkspace.v2.PoliciesClientClientTypeOptions`
        """
        return self._options

    @options.setter
    def options(self, options):
        r"""Sets the options of this PoliciesClientClientType.

        :param options: The options of this PoliciesClientClientType.
        :type options: :class:`huaweicloudsdkworkspace.v2.PoliciesClientClientTypeOptions`
        """
        self._options = options

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
        if not isinstance(other, PoliciesClientClientType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
