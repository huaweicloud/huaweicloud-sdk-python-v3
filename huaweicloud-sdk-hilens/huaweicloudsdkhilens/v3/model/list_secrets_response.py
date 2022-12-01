# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSecretsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'count': 'str',
        'secrets': 'list[SecretDetail]'
    }

    attribute_map = {
        'count': 'count',
        'secrets': 'secrets'
    }

    def __init__(self, count=None, secrets=None):
        """ListSecretsResponse

        The model defined in huaweicloud sdk

        :param count: 数量
        :type count: str
        :param secrets: 缪瑶详情列表
        :type secrets: list[:class:`huaweicloudsdkhilens.v3.SecretDetail`]
        """
        
        super(ListSecretsResponse, self).__init__()

        self._count = None
        self._secrets = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if secrets is not None:
            self.secrets = secrets

    @property
    def count(self):
        """Gets the count of this ListSecretsResponse.

        数量

        :return: The count of this ListSecretsResponse.
        :rtype: str
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ListSecretsResponse.

        数量

        :param count: The count of this ListSecretsResponse.
        :type count: str
        """
        self._count = count

    @property
    def secrets(self):
        """Gets the secrets of this ListSecretsResponse.

        缪瑶详情列表

        :return: The secrets of this ListSecretsResponse.
        :rtype: list[:class:`huaweicloudsdkhilens.v3.SecretDetail`]
        """
        return self._secrets

    @secrets.setter
    def secrets(self, secrets):
        """Sets the secrets of this ListSecretsResponse.

        缪瑶详情列表

        :param secrets: The secrets of this ListSecretsResponse.
        :type secrets: list[:class:`huaweicloudsdkhilens.v3.SecretDetail`]
        """
        self._secrets = secrets

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
        if not isinstance(other, ListSecretsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
