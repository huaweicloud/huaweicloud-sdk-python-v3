# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListExchangesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'vhost': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'vhost': 'vhost',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, instance_id=None, vhost=None, offset=None, limit=None):
        r"""ListExchangesRequest

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID
        :type instance_id: str
        :param vhost: 所属Vhost名称
        :type vhost: str
        :param offset: 分页查询偏移量，表示从此偏移量开始查询，offset大于等于0，默认从0开始查询。
        :type offset: int
        :param limit: 分页查询单页数量，取值范围0~50，默认查询10条。
        :type limit: int
        """
        
        

        self._instance_id = None
        self._vhost = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        self.instance_id = instance_id
        self.vhost = vhost
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ListExchangesRequest.

        实例ID

        :return: The instance_id of this ListExchangesRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ListExchangesRequest.

        实例ID

        :param instance_id: The instance_id of this ListExchangesRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def vhost(self):
        r"""Gets the vhost of this ListExchangesRequest.

        所属Vhost名称

        :return: The vhost of this ListExchangesRequest.
        :rtype: str
        """
        return self._vhost

    @vhost.setter
    def vhost(self, vhost):
        r"""Sets the vhost of this ListExchangesRequest.

        所属Vhost名称

        :param vhost: The vhost of this ListExchangesRequest.
        :type vhost: str
        """
        self._vhost = vhost

    @property
    def offset(self):
        r"""Gets the offset of this ListExchangesRequest.

        分页查询偏移量，表示从此偏移量开始查询，offset大于等于0，默认从0开始查询。

        :return: The offset of this ListExchangesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListExchangesRequest.

        分页查询偏移量，表示从此偏移量开始查询，offset大于等于0，默认从0开始查询。

        :param offset: The offset of this ListExchangesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListExchangesRequest.

        分页查询单页数量，取值范围0~50，默认查询10条。

        :return: The limit of this ListExchangesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListExchangesRequest.

        分页查询单页数量，取值范围0~50，默认查询10条。

        :param limit: The limit of this ListExchangesRequest.
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
        if not isinstance(other, ListExchangesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
