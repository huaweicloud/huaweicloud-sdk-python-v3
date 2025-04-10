# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListElasticResourcePoolsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'is_success': 'bool',
        'message': 'str',
        'count': 'int',
        'elastic_resource_pools': 'list[ElasticResourcePool]'
    }

    attribute_map = {
        'is_success': 'is_success',
        'message': 'message',
        'count': 'count',
        'elastic_resource_pools': 'elastic_resource_pools'
    }

    def __init__(self, is_success=None, message=None, count=None, elastic_resource_pools=None):
        r"""ListElasticResourcePoolsResponse

        The model defined in huaweicloud sdk

        :param is_success: 是否成功
        :type is_success: bool
        :param message: 消息
        :type message: str
        :param count: 数量
        :type count: int
        :param elastic_resource_pools: 弹性资源池列表
        :type elastic_resource_pools: list[:class:`huaweicloudsdkdli.v1.ElasticResourcePool`]
        """
        
        super(ListElasticResourcePoolsResponse, self).__init__()

        self._is_success = None
        self._message = None
        self._count = None
        self._elastic_resource_pools = None
        self.discriminator = None

        if is_success is not None:
            self.is_success = is_success
        if message is not None:
            self.message = message
        if count is not None:
            self.count = count
        if elastic_resource_pools is not None:
            self.elastic_resource_pools = elastic_resource_pools

    @property
    def is_success(self):
        r"""Gets the is_success of this ListElasticResourcePoolsResponse.

        是否成功

        :return: The is_success of this ListElasticResourcePoolsResponse.
        :rtype: bool
        """
        return self._is_success

    @is_success.setter
    def is_success(self, is_success):
        r"""Sets the is_success of this ListElasticResourcePoolsResponse.

        是否成功

        :param is_success: The is_success of this ListElasticResourcePoolsResponse.
        :type is_success: bool
        """
        self._is_success = is_success

    @property
    def message(self):
        r"""Gets the message of this ListElasticResourcePoolsResponse.

        消息

        :return: The message of this ListElasticResourcePoolsResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this ListElasticResourcePoolsResponse.

        消息

        :param message: The message of this ListElasticResourcePoolsResponse.
        :type message: str
        """
        self._message = message

    @property
    def count(self):
        r"""Gets the count of this ListElasticResourcePoolsResponse.

        数量

        :return: The count of this ListElasticResourcePoolsResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ListElasticResourcePoolsResponse.

        数量

        :param count: The count of this ListElasticResourcePoolsResponse.
        :type count: int
        """
        self._count = count

    @property
    def elastic_resource_pools(self):
        r"""Gets the elastic_resource_pools of this ListElasticResourcePoolsResponse.

        弹性资源池列表

        :return: The elastic_resource_pools of this ListElasticResourcePoolsResponse.
        :rtype: list[:class:`huaweicloudsdkdli.v1.ElasticResourcePool`]
        """
        return self._elastic_resource_pools

    @elastic_resource_pools.setter
    def elastic_resource_pools(self, elastic_resource_pools):
        r"""Sets the elastic_resource_pools of this ListElasticResourcePoolsResponse.

        弹性资源池列表

        :param elastic_resource_pools: The elastic_resource_pools of this ListElasticResourcePoolsResponse.
        :type elastic_resource_pools: list[:class:`huaweicloudsdkdli.v1.ElasticResourcePool`]
        """
        self._elastic_resource_pools = elastic_resource_pools

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
        if not isinstance(other, ListElasticResourcePoolsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
