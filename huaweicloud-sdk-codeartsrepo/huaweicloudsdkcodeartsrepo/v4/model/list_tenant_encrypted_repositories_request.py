# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTenantEncryptedRepositoriesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'tenant_id': 'str',
        'offset': 'int',
        'limit': 'int',
        'order_by': 'str',
        'sort': 'str'
    }

    attribute_map = {
        'tenant_id': 'tenant_id',
        'offset': 'offset',
        'limit': 'limit',
        'order_by': 'order_by',
        'sort': 'sort'
    }

    def __init__(self, tenant_id=None, offset=None, limit=None, order_by=None, sort=None):
        r"""ListTenantEncryptedRepositoriesRequest

        The model defined in huaweicloud sdk

        :param tenant_id: **参数解释：** 租户id
        :type tenant_id: str
        :param offset: **参数解释：** 偏移量，从0开始。
        :type offset: int
        :param limit: **参数解释：** 返回数量。
        :type limit: int
        :param order_by: **参数解释：** 排序字段 repoName 仓库名称  ownerName | 仓库所有者名称 ownerName, 不传该字段时不进行排序
        :type order_by: str
        :param sort: **参数解释：** 排序顺序 asc顺序 desc逆序
        :type sort: str
        """
        
        

        self._tenant_id = None
        self._offset = None
        self._limit = None
        self._order_by = None
        self._sort = None
        self.discriminator = None

        self.tenant_id = tenant_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if order_by is not None:
            self.order_by = order_by
        if sort is not None:
            self.sort = sort

    @property
    def tenant_id(self):
        r"""Gets the tenant_id of this ListTenantEncryptedRepositoriesRequest.

        **参数解释：** 租户id

        :return: The tenant_id of this ListTenantEncryptedRepositoriesRequest.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        r"""Sets the tenant_id of this ListTenantEncryptedRepositoriesRequest.

        **参数解释：** 租户id

        :param tenant_id: The tenant_id of this ListTenantEncryptedRepositoriesRequest.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

    @property
    def offset(self):
        r"""Gets the offset of this ListTenantEncryptedRepositoriesRequest.

        **参数解释：** 偏移量，从0开始。

        :return: The offset of this ListTenantEncryptedRepositoriesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListTenantEncryptedRepositoriesRequest.

        **参数解释：** 偏移量，从0开始。

        :param offset: The offset of this ListTenantEncryptedRepositoriesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListTenantEncryptedRepositoriesRequest.

        **参数解释：** 返回数量。

        :return: The limit of this ListTenantEncryptedRepositoriesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListTenantEncryptedRepositoriesRequest.

        **参数解释：** 返回数量。

        :param limit: The limit of this ListTenantEncryptedRepositoriesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def order_by(self):
        r"""Gets the order_by of this ListTenantEncryptedRepositoriesRequest.

        **参数解释：** 排序字段 repoName 仓库名称  ownerName | 仓库所有者名称 ownerName, 不传该字段时不进行排序

        :return: The order_by of this ListTenantEncryptedRepositoriesRequest.
        :rtype: str
        """
        return self._order_by

    @order_by.setter
    def order_by(self, order_by):
        r"""Sets the order_by of this ListTenantEncryptedRepositoriesRequest.

        **参数解释：** 排序字段 repoName 仓库名称  ownerName | 仓库所有者名称 ownerName, 不传该字段时不进行排序

        :param order_by: The order_by of this ListTenantEncryptedRepositoriesRequest.
        :type order_by: str
        """
        self._order_by = order_by

    @property
    def sort(self):
        r"""Gets the sort of this ListTenantEncryptedRepositoriesRequest.

        **参数解释：** 排序顺序 asc顺序 desc逆序

        :return: The sort of this ListTenantEncryptedRepositoriesRequest.
        :rtype: str
        """
        return self._sort

    @sort.setter
    def sort(self, sort):
        r"""Sets the sort of this ListTenantEncryptedRepositoriesRequest.

        **参数解释：** 排序顺序 asc顺序 desc逆序

        :param sort: The sort of this ListTenantEncryptedRepositoriesRequest.
        :type sort: str
        """
        self._sort = sort

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
        if not isinstance(other, ListTenantEncryptedRepositoriesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
