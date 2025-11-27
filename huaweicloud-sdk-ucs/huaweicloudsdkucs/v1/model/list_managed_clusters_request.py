# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListManagedClustersRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'unimported': 'bool',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'unimported': 'unimported',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, unimported=None, limit=None, offset=None):
        r"""ListManagedClustersRequest

        The model defined in huaweicloud sdk

        :param unimported: 是否已导入到ucs
        :type unimported: bool
        :param limit: 分页获取列表时，页的大小，默认为-1
        :type limit: int
        :param offset: 分页获取列表时，起始偏移量，默认为0
        :type offset: int
        """
        
        

        self._unimported = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        if unimported is not None:
            self.unimported = unimported
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def unimported(self):
        r"""Gets the unimported of this ListManagedClustersRequest.

        是否已导入到ucs

        :return: The unimported of this ListManagedClustersRequest.
        :rtype: bool
        """
        return self._unimported

    @unimported.setter
    def unimported(self, unimported):
        r"""Sets the unimported of this ListManagedClustersRequest.

        是否已导入到ucs

        :param unimported: The unimported of this ListManagedClustersRequest.
        :type unimported: bool
        """
        self._unimported = unimported

    @property
    def limit(self):
        r"""Gets the limit of this ListManagedClustersRequest.

        分页获取列表时，页的大小，默认为-1

        :return: The limit of this ListManagedClustersRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListManagedClustersRequest.

        分页获取列表时，页的大小，默认为-1

        :param limit: The limit of this ListManagedClustersRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListManagedClustersRequest.

        分页获取列表时，起始偏移量，默认为0

        :return: The offset of this ListManagedClustersRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListManagedClustersRequest.

        分页获取列表时，起始偏移量，默认为0

        :param offset: The offset of this ListManagedClustersRequest.
        :type offset: int
        """
        self._offset = offset

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListManagedClustersRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
