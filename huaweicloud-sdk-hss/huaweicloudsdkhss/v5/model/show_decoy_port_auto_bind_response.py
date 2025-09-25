# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDecoyPortAutoBindResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'auto_bind': 'bool',
        'windows_policy': 'str',
        'linux_policy': 'str'
    }

    attribute_map = {
        'auto_bind': 'auto_bind',
        'windows_policy': 'windows_policy',
        'linux_policy': 'linux_policy'
    }

    def __init__(self, auto_bind=None, windows_policy=None, linux_policy=None):
        r"""ShowDecoyPortAutoBindResponse

        The model defined in huaweicloud sdk

        :param auto_bind: 是否自动绑定
        :type auto_bind: bool
        :param windows_policy: 默认绑定的策略id
        :type windows_policy: str
        :param linux_policy: 默认绑定的策略id
        :type linux_policy: str
        """
        
        super(ShowDecoyPortAutoBindResponse, self).__init__()

        self._auto_bind = None
        self._windows_policy = None
        self._linux_policy = None
        self.discriminator = None

        if auto_bind is not None:
            self.auto_bind = auto_bind
        if windows_policy is not None:
            self.windows_policy = windows_policy
        if linux_policy is not None:
            self.linux_policy = linux_policy

    @property
    def auto_bind(self):
        r"""Gets the auto_bind of this ShowDecoyPortAutoBindResponse.

        是否自动绑定

        :return: The auto_bind of this ShowDecoyPortAutoBindResponse.
        :rtype: bool
        """
        return self._auto_bind

    @auto_bind.setter
    def auto_bind(self, auto_bind):
        r"""Sets the auto_bind of this ShowDecoyPortAutoBindResponse.

        是否自动绑定

        :param auto_bind: The auto_bind of this ShowDecoyPortAutoBindResponse.
        :type auto_bind: bool
        """
        self._auto_bind = auto_bind

    @property
    def windows_policy(self):
        r"""Gets the windows_policy of this ShowDecoyPortAutoBindResponse.

        默认绑定的策略id

        :return: The windows_policy of this ShowDecoyPortAutoBindResponse.
        :rtype: str
        """
        return self._windows_policy

    @windows_policy.setter
    def windows_policy(self, windows_policy):
        r"""Sets the windows_policy of this ShowDecoyPortAutoBindResponse.

        默认绑定的策略id

        :param windows_policy: The windows_policy of this ShowDecoyPortAutoBindResponse.
        :type windows_policy: str
        """
        self._windows_policy = windows_policy

    @property
    def linux_policy(self):
        r"""Gets the linux_policy of this ShowDecoyPortAutoBindResponse.

        默认绑定的策略id

        :return: The linux_policy of this ShowDecoyPortAutoBindResponse.
        :rtype: str
        """
        return self._linux_policy

    @linux_policy.setter
    def linux_policy(self, linux_policy):
        r"""Sets the linux_policy of this ShowDecoyPortAutoBindResponse.

        默认绑定的策略id

        :param linux_policy: The linux_policy of this ShowDecoyPortAutoBindResponse.
        :type linux_policy: str
        """
        self._linux_policy = linux_policy

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
        if not isinstance(other, ShowDecoyPortAutoBindResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
