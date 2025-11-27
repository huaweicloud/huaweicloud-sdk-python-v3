# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListVendorAccountRequest:

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
        'offset': 'str',
        'marker': 'str',
        'vendor': 'str',
        'account_id': 'str',
        'account_name': 'str'
    }

    attribute_map = {
        'limit': 'limit',
        'offset': 'offset',
        'marker': 'marker',
        'vendor': 'vendor',
        'account_id': 'account_id',
        'account_name': 'account_name'
    }

    def __init__(self, limit=None, offset=None, marker=None, vendor=None, account_id=None, account_name=None):
        r"""ListVendorAccountRequest

        The model defined in huaweicloud sdk

        :param limit: **参数解释：** 分页查询每页显示的条目数量。 **约束限制：** 不涉及。 **取值范围：** 自定义，在1-500范围。 **默认取值：** 不涉及。
        :type limit: int
        :param offset: **参数解释：** 分页查询偏移量，表示从此偏移量开始查询。 **约束限制：** 不涉及。 **取值范围：** 0-2147483647。 **默认取值：** 0。
        :type offset: str
        :param marker: **参数解释：** 分页参数，上一页请求最后一个id。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type marker: str
        :param vendor: **参数解释：** 供应商。 **约束限制：** 不涉及。 **取值范围：** - RMS： 华为云。 - AWS：亚马逊。 - AZURE：微软。 - ALI：阿里云。 - VMWARE：VMware。 - OPENSTACK：openstack云平台。 - HCS：Huawei Cloud Stack。 - OTHER：其他云广商。 **默认取值：** 不涉及。
        :type vendor: str
        :param account_id: **参数解释：** 供应商的账户ID。 **约束限制：** 不涉及。 **取值范围：** 字符串，长度0到64个字符。 **默认取值：** 不涉及。
        :type account_id: str
        :param account_name: **参数解释：** 账户名。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type account_name: str
        """
        
        

        self._limit = None
        self._offset = None
        self._marker = None
        self._vendor = None
        self._account_id = None
        self._account_name = None
        self.discriminator = None

        self.limit = limit
        if offset is not None:
            self.offset = offset
        if marker is not None:
            self.marker = marker
        if vendor is not None:
            self.vendor = vendor
        if account_id is not None:
            self.account_id = account_id
        if account_name is not None:
            self.account_name = account_name

    @property
    def limit(self):
        r"""Gets the limit of this ListVendorAccountRequest.

        **参数解释：** 分页查询每页显示的条目数量。 **约束限制：** 不涉及。 **取值范围：** 自定义，在1-500范围。 **默认取值：** 不涉及。

        :return: The limit of this ListVendorAccountRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListVendorAccountRequest.

        **参数解释：** 分页查询每页显示的条目数量。 **约束限制：** 不涉及。 **取值范围：** 自定义，在1-500范围。 **默认取值：** 不涉及。

        :param limit: The limit of this ListVendorAccountRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListVendorAccountRequest.

        **参数解释：** 分页查询偏移量，表示从此偏移量开始查询。 **约束限制：** 不涉及。 **取值范围：** 0-2147483647。 **默认取值：** 0。

        :return: The offset of this ListVendorAccountRequest.
        :rtype: str
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListVendorAccountRequest.

        **参数解释：** 分页查询偏移量，表示从此偏移量开始查询。 **约束限制：** 不涉及。 **取值范围：** 0-2147483647。 **默认取值：** 0。

        :param offset: The offset of this ListVendorAccountRequest.
        :type offset: str
        """
        self._offset = offset

    @property
    def marker(self):
        r"""Gets the marker of this ListVendorAccountRequest.

        **参数解释：** 分页参数，上一页请求最后一个id。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The marker of this ListVendorAccountRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListVendorAccountRequest.

        **参数解释：** 分页参数，上一页请求最后一个id。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param marker: The marker of this ListVendorAccountRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def vendor(self):
        r"""Gets the vendor of this ListVendorAccountRequest.

        **参数解释：** 供应商。 **约束限制：** 不涉及。 **取值范围：** - RMS： 华为云。 - AWS：亚马逊。 - AZURE：微软。 - ALI：阿里云。 - VMWARE：VMware。 - OPENSTACK：openstack云平台。 - HCS：Huawei Cloud Stack。 - OTHER：其他云广商。 **默认取值：** 不涉及。

        :return: The vendor of this ListVendorAccountRequest.
        :rtype: str
        """
        return self._vendor

    @vendor.setter
    def vendor(self, vendor):
        r"""Sets the vendor of this ListVendorAccountRequest.

        **参数解释：** 供应商。 **约束限制：** 不涉及。 **取值范围：** - RMS： 华为云。 - AWS：亚马逊。 - AZURE：微软。 - ALI：阿里云。 - VMWARE：VMware。 - OPENSTACK：openstack云平台。 - HCS：Huawei Cloud Stack。 - OTHER：其他云广商。 **默认取值：** 不涉及。

        :param vendor: The vendor of this ListVendorAccountRequest.
        :type vendor: str
        """
        self._vendor = vendor

    @property
    def account_id(self):
        r"""Gets the account_id of this ListVendorAccountRequest.

        **参数解释：** 供应商的账户ID。 **约束限制：** 不涉及。 **取值范围：** 字符串，长度0到64个字符。 **默认取值：** 不涉及。

        :return: The account_id of this ListVendorAccountRequest.
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        r"""Sets the account_id of this ListVendorAccountRequest.

        **参数解释：** 供应商的账户ID。 **约束限制：** 不涉及。 **取值范围：** 字符串，长度0到64个字符。 **默认取值：** 不涉及。

        :param account_id: The account_id of this ListVendorAccountRequest.
        :type account_id: str
        """
        self._account_id = account_id

    @property
    def account_name(self):
        r"""Gets the account_name of this ListVendorAccountRequest.

        **参数解释：** 账户名。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The account_name of this ListVendorAccountRequest.
        :rtype: str
        """
        return self._account_name

    @account_name.setter
    def account_name(self, account_name):
        r"""Sets the account_name of this ListVendorAccountRequest.

        **参数解释：** 账户名。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param account_name: The account_name of this ListVendorAccountRequest.
        :type account_name: str
        """
        self._account_name = account_name

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
        if not isinstance(other, ListVendorAccountRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
