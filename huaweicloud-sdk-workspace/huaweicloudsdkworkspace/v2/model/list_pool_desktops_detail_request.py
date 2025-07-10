# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPoolDesktopsDetailRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'pool_id': 'str',
        'inconsistent_type': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'pool_id': 'pool_id',
        'inconsistent_type': 'inconsistent_type',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, pool_id=None, inconsistent_type=None, offset=None, limit=None):
        r"""ListPoolDesktopsDetailRequest

        The model defined in huaweicloud sdk

        :param pool_id: 桌面池ID。
        :type pool_id: str
        :param inconsistent_type: 通过该类型过滤出与桌面池规格类型不一致的桌面 - PRODUCT: 查找productID与桌面池套餐ID不一致的桌面 - IMAGE: 查找imageID与桌面池镜像ID不一致的桌面
        :type inconsistent_type: str
        :param offset: 用于分页查询，查询的起始记录序号，从0开始。
        :type offset: int
        :param limit: 用于分页查询，返回桌面数量限制。取值范围0-100，默认值是10。
        :type limit: int
        """
        
        

        self._pool_id = None
        self._inconsistent_type = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        self.pool_id = pool_id
        if inconsistent_type is not None:
            self.inconsistent_type = inconsistent_type
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def pool_id(self):
        r"""Gets the pool_id of this ListPoolDesktopsDetailRequest.

        桌面池ID。

        :return: The pool_id of this ListPoolDesktopsDetailRequest.
        :rtype: str
        """
        return self._pool_id

    @pool_id.setter
    def pool_id(self, pool_id):
        r"""Sets the pool_id of this ListPoolDesktopsDetailRequest.

        桌面池ID。

        :param pool_id: The pool_id of this ListPoolDesktopsDetailRequest.
        :type pool_id: str
        """
        self._pool_id = pool_id

    @property
    def inconsistent_type(self):
        r"""Gets the inconsistent_type of this ListPoolDesktopsDetailRequest.

        通过该类型过滤出与桌面池规格类型不一致的桌面 - PRODUCT: 查找productID与桌面池套餐ID不一致的桌面 - IMAGE: 查找imageID与桌面池镜像ID不一致的桌面

        :return: The inconsistent_type of this ListPoolDesktopsDetailRequest.
        :rtype: str
        """
        return self._inconsistent_type

    @inconsistent_type.setter
    def inconsistent_type(self, inconsistent_type):
        r"""Sets the inconsistent_type of this ListPoolDesktopsDetailRequest.

        通过该类型过滤出与桌面池规格类型不一致的桌面 - PRODUCT: 查找productID与桌面池套餐ID不一致的桌面 - IMAGE: 查找imageID与桌面池镜像ID不一致的桌面

        :param inconsistent_type: The inconsistent_type of this ListPoolDesktopsDetailRequest.
        :type inconsistent_type: str
        """
        self._inconsistent_type = inconsistent_type

    @property
    def offset(self):
        r"""Gets the offset of this ListPoolDesktopsDetailRequest.

        用于分页查询，查询的起始记录序号，从0开始。

        :return: The offset of this ListPoolDesktopsDetailRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListPoolDesktopsDetailRequest.

        用于分页查询，查询的起始记录序号，从0开始。

        :param offset: The offset of this ListPoolDesktopsDetailRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListPoolDesktopsDetailRequest.

        用于分页查询，返回桌面数量限制。取值范围0-100，默认值是10。

        :return: The limit of this ListPoolDesktopsDetailRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListPoolDesktopsDetailRequest.

        用于分页查询，返回桌面数量限制。取值范围0-100，默认值是10。

        :param limit: The limit of this ListPoolDesktopsDetailRequest.
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
        if not isinstance(other, ListPoolDesktopsDetailRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
