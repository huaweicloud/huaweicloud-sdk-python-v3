# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NovaShowKeypairRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'keypair_name': 'str',
        'open_stack_api_version': 'str'
    }

    attribute_map = {
        'keypair_name': 'keypair_name',
        'open_stack_api_version': 'OpenStack-API-Version'
    }

    def __init__(self, keypair_name=None, open_stack_api_version=None):
        """NovaShowKeypairRequest

        The model defined in huaweicloud sdk

        :param keypair_name: 密钥名称信息。
        :type keypair_name: str
        :param open_stack_api_version: 微版本头
        :type open_stack_api_version: str
        """
        
        

        self._keypair_name = None
        self._open_stack_api_version = None
        self.discriminator = None

        self.keypair_name = keypair_name
        if open_stack_api_version is not None:
            self.open_stack_api_version = open_stack_api_version

    @property
    def keypair_name(self):
        """Gets the keypair_name of this NovaShowKeypairRequest.

        密钥名称信息。

        :return: The keypair_name of this NovaShowKeypairRequest.
        :rtype: str
        """
        return self._keypair_name

    @keypair_name.setter
    def keypair_name(self, keypair_name):
        """Sets the keypair_name of this NovaShowKeypairRequest.

        密钥名称信息。

        :param keypair_name: The keypair_name of this NovaShowKeypairRequest.
        :type keypair_name: str
        """
        self._keypair_name = keypair_name

    @property
    def open_stack_api_version(self):
        """Gets the open_stack_api_version of this NovaShowKeypairRequest.

        微版本头

        :return: The open_stack_api_version of this NovaShowKeypairRequest.
        :rtype: str
        """
        return self._open_stack_api_version

    @open_stack_api_version.setter
    def open_stack_api_version(self, open_stack_api_version):
        """Sets the open_stack_api_version of this NovaShowKeypairRequest.

        微版本头

        :param open_stack_api_version: The open_stack_api_version of this NovaShowKeypairRequest.
        :type open_stack_api_version: str
        """
        self._open_stack_api_version = open_stack_api_version

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
        if not isinstance(other, NovaShowKeypairRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
