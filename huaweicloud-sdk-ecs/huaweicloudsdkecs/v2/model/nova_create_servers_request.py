# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NovaCreateServersRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'open_stack_api_version': 'str',
        'body': 'NovaCreateServersRequestBody'
    }

    attribute_map = {
        'open_stack_api_version': 'OpenStack-API-Version',
        'body': 'body'
    }

    def __init__(self, open_stack_api_version=None, body=None):
        """NovaCreateServersRequest

        The model defined in huaweicloud sdk

        :param open_stack_api_version: 微版本头
        :type open_stack_api_version: str
        :param body: Body of the NovaCreateServersRequest
        :type body: :class:`huaweicloudsdkecs.v2.NovaCreateServersRequestBody`
        """
        
        

        self._open_stack_api_version = None
        self._body = None
        self.discriminator = None

        if open_stack_api_version is not None:
            self.open_stack_api_version = open_stack_api_version
        if body is not None:
            self.body = body

    @property
    def open_stack_api_version(self):
        """Gets the open_stack_api_version of this NovaCreateServersRequest.

        微版本头

        :return: The open_stack_api_version of this NovaCreateServersRequest.
        :rtype: str
        """
        return self._open_stack_api_version

    @open_stack_api_version.setter
    def open_stack_api_version(self, open_stack_api_version):
        """Sets the open_stack_api_version of this NovaCreateServersRequest.

        微版本头

        :param open_stack_api_version: The open_stack_api_version of this NovaCreateServersRequest.
        :type open_stack_api_version: str
        """
        self._open_stack_api_version = open_stack_api_version

    @property
    def body(self):
        """Gets the body of this NovaCreateServersRequest.

        :return: The body of this NovaCreateServersRequest.
        :rtype: :class:`huaweicloudsdkecs.v2.NovaCreateServersRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this NovaCreateServersRequest.

        :param body: The body of this NovaCreateServersRequest.
        :type body: :class:`huaweicloudsdkecs.v2.NovaCreateServersRequestBody`
        """
        self._body = body

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
        if not isinstance(other, NovaCreateServersRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
