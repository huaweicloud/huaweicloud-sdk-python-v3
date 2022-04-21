# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NovaListKeypairsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'limit': 'int',
        'marker': 'str',
        'open_stack_api_version': 'str'
    }

    attribute_map = {
        'limit': 'limit',
        'marker': 'marker',
        'open_stack_api_version': 'OpenStack-API-Version'
    }

    def __init__(self, limit=None, marker=None, open_stack_api_version=None):
        """NovaListKeypairsRequest

        The model defined in huaweicloud sdk

        :param limit: 查询返回秘钥数量限制。  在微版本2.35后支持
        :type limit: int
        :param marker: 从marker指定的keypair的名称的下一条数据开始查询。  在微版本2.35后支持。
        :type marker: str
        :param open_stack_api_version: 微版本头
        :type open_stack_api_version: str
        """
        
        

        self._limit = None
        self._marker = None
        self._open_stack_api_version = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if open_stack_api_version is not None:
            self.open_stack_api_version = open_stack_api_version

    @property
    def limit(self):
        """Gets the limit of this NovaListKeypairsRequest.

        查询返回秘钥数量限制。  在微版本2.35后支持

        :return: The limit of this NovaListKeypairsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this NovaListKeypairsRequest.

        查询返回秘钥数量限制。  在微版本2.35后支持

        :param limit: The limit of this NovaListKeypairsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        """Gets the marker of this NovaListKeypairsRequest.

        从marker指定的keypair的名称的下一条数据开始查询。  在微版本2.35后支持。

        :return: The marker of this NovaListKeypairsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this NovaListKeypairsRequest.

        从marker指定的keypair的名称的下一条数据开始查询。  在微版本2.35后支持。

        :param marker: The marker of this NovaListKeypairsRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def open_stack_api_version(self):
        """Gets the open_stack_api_version of this NovaListKeypairsRequest.

        微版本头

        :return: The open_stack_api_version of this NovaListKeypairsRequest.
        :rtype: str
        """
        return self._open_stack_api_version

    @open_stack_api_version.setter
    def open_stack_api_version(self, open_stack_api_version):
        """Sets the open_stack_api_version of this NovaListKeypairsRequest.

        微版本头

        :param open_stack_api_version: The open_stack_api_version of this NovaListKeypairsRequest.
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
        if not isinstance(other, NovaListKeypairsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
