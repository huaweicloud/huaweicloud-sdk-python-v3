# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSecretVersionsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'secret_name': 'str',
        'marker': 'str',
        'limit': 'int'
    }

    attribute_map = {
        'secret_name': 'secret_name',
        'marker': 'marker',
        'limit': 'limit'
    }

    def __init__(self, secret_name=None, marker=None, limit=None):
        """ListSecretVersionsRequest

        The model defined in huaweicloud sdk

        :param secret_name: 凭据名称。
        :type secret_name: str
        :param marker: 分页参数，取值为上一页数据的最后一条记录的版本号。
        :type marker: str
        :param limit: 每页显示的条目数量。默认值50。
        :type limit: int
        """
        
        

        self._secret_name = None
        self._marker = None
        self._limit = None
        self.discriminator = None

        self.secret_name = secret_name
        if marker is not None:
            self.marker = marker
        if limit is not None:
            self.limit = limit

    @property
    def secret_name(self):
        """Gets the secret_name of this ListSecretVersionsRequest.

        凭据名称。

        :return: The secret_name of this ListSecretVersionsRequest.
        :rtype: str
        """
        return self._secret_name

    @secret_name.setter
    def secret_name(self, secret_name):
        """Sets the secret_name of this ListSecretVersionsRequest.

        凭据名称。

        :param secret_name: The secret_name of this ListSecretVersionsRequest.
        :type secret_name: str
        """
        self._secret_name = secret_name

    @property
    def marker(self):
        """Gets the marker of this ListSecretVersionsRequest.

        分页参数，取值为上一页数据的最后一条记录的版本号。

        :return: The marker of this ListSecretVersionsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListSecretVersionsRequest.

        分页参数，取值为上一页数据的最后一条记录的版本号。

        :param marker: The marker of this ListSecretVersionsRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def limit(self):
        """Gets the limit of this ListSecretVersionsRequest.

        每页显示的条目数量。默认值50。

        :return: The limit of this ListSecretVersionsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListSecretVersionsRequest.

        每页显示的条目数量。默认值50。

        :param limit: The limit of this ListSecretVersionsRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ListSecretVersionsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
