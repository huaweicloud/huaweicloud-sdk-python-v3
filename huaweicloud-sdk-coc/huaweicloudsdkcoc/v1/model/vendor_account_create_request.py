# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VendorAccountCreateRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'vendor': 'str',
        'account_id': 'str',
        'account_name': 'str',
        'ak': 'str',
        'sk': 'str'
    }

    attribute_map = {
        'vendor': 'vendor',
        'account_id': 'account_id',
        'account_name': 'account_name',
        'ak': 'ak',
        'sk': 'sk'
    }

    def __init__(self, vendor=None, account_id=None, account_name=None, ak=None, sk=None):
        r"""VendorAccountCreateRequest

        The model defined in huaweicloud sdk

        :param vendor: **参数解释：** 云广商信息。 **约束限制：** 不涉及。 **取值范围：** - RMS： 华为云。 - AWS：亚马逊。 - AZURE：微软。 - ALI：阿里云。 - VMWARE：VMware。 - OPENSTACK：openstack云平台。 - HCS：Huawei Cloud Stack。 - OTHER：其他云广商。 **默认取值：** 不涉及。
        :type vendor: str
        :param account_id: **参数解释：** 供应商的账户ID。 **约束限制：** 不涉及。 **取值范围：** 字符串，长度0到64个字符。 **默认取值：** 不涉及。
        :type account_id: str
        :param account_name: **参数解释：** 账户名。 **约束限制：** 不涉及。 **取值范围：** 字符串，长度0到64个字符。 **默认取值：** 不涉及。
        :type account_name: str
        :param ak: **参数解释：** 访问密钥id。 **约束限制：** 不涉及。 **取值范围：** 字符串，长度0到64个字符。 **默认取值：** 不涉及。
        :type ak: str
        :param sk: **参数解释：** 访问密钥密码。 **约束限制：** 不涉及。 **取值范围：** 字符串，长度0到64个字符。 **默认取值：** 不涉及。
        :type sk: str
        """
        
        

        self._vendor = None
        self._account_id = None
        self._account_name = None
        self._ak = None
        self._sk = None
        self.discriminator = None

        self.vendor = vendor
        self.account_id = account_id
        self.account_name = account_name
        self.ak = ak
        self.sk = sk

    @property
    def vendor(self):
        r"""Gets the vendor of this VendorAccountCreateRequest.

        **参数解释：** 云广商信息。 **约束限制：** 不涉及。 **取值范围：** - RMS： 华为云。 - AWS：亚马逊。 - AZURE：微软。 - ALI：阿里云。 - VMWARE：VMware。 - OPENSTACK：openstack云平台。 - HCS：Huawei Cloud Stack。 - OTHER：其他云广商。 **默认取值：** 不涉及。

        :return: The vendor of this VendorAccountCreateRequest.
        :rtype: str
        """
        return self._vendor

    @vendor.setter
    def vendor(self, vendor):
        r"""Sets the vendor of this VendorAccountCreateRequest.

        **参数解释：** 云广商信息。 **约束限制：** 不涉及。 **取值范围：** - RMS： 华为云。 - AWS：亚马逊。 - AZURE：微软。 - ALI：阿里云。 - VMWARE：VMware。 - OPENSTACK：openstack云平台。 - HCS：Huawei Cloud Stack。 - OTHER：其他云广商。 **默认取值：** 不涉及。

        :param vendor: The vendor of this VendorAccountCreateRequest.
        :type vendor: str
        """
        self._vendor = vendor

    @property
    def account_id(self):
        r"""Gets the account_id of this VendorAccountCreateRequest.

        **参数解释：** 供应商的账户ID。 **约束限制：** 不涉及。 **取值范围：** 字符串，长度0到64个字符。 **默认取值：** 不涉及。

        :return: The account_id of this VendorAccountCreateRequest.
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        r"""Sets the account_id of this VendorAccountCreateRequest.

        **参数解释：** 供应商的账户ID。 **约束限制：** 不涉及。 **取值范围：** 字符串，长度0到64个字符。 **默认取值：** 不涉及。

        :param account_id: The account_id of this VendorAccountCreateRequest.
        :type account_id: str
        """
        self._account_id = account_id

    @property
    def account_name(self):
        r"""Gets the account_name of this VendorAccountCreateRequest.

        **参数解释：** 账户名。 **约束限制：** 不涉及。 **取值范围：** 字符串，长度0到64个字符。 **默认取值：** 不涉及。

        :return: The account_name of this VendorAccountCreateRequest.
        :rtype: str
        """
        return self._account_name

    @account_name.setter
    def account_name(self, account_name):
        r"""Sets the account_name of this VendorAccountCreateRequest.

        **参数解释：** 账户名。 **约束限制：** 不涉及。 **取值范围：** 字符串，长度0到64个字符。 **默认取值：** 不涉及。

        :param account_name: The account_name of this VendorAccountCreateRequest.
        :type account_name: str
        """
        self._account_name = account_name

    @property
    def ak(self):
        r"""Gets the ak of this VendorAccountCreateRequest.

        **参数解释：** 访问密钥id。 **约束限制：** 不涉及。 **取值范围：** 字符串，长度0到64个字符。 **默认取值：** 不涉及。

        :return: The ak of this VendorAccountCreateRequest.
        :rtype: str
        """
        return self._ak

    @ak.setter
    def ak(self, ak):
        r"""Sets the ak of this VendorAccountCreateRequest.

        **参数解释：** 访问密钥id。 **约束限制：** 不涉及。 **取值范围：** 字符串，长度0到64个字符。 **默认取值：** 不涉及。

        :param ak: The ak of this VendorAccountCreateRequest.
        :type ak: str
        """
        self._ak = ak

    @property
    def sk(self):
        r"""Gets the sk of this VendorAccountCreateRequest.

        **参数解释：** 访问密钥密码。 **约束限制：** 不涉及。 **取值范围：** 字符串，长度0到64个字符。 **默认取值：** 不涉及。

        :return: The sk of this VendorAccountCreateRequest.
        :rtype: str
        """
        return self._sk

    @sk.setter
    def sk(self, sk):
        r"""Sets the sk of this VendorAccountCreateRequest.

        **参数解释：** 访问密钥密码。 **约束限制：** 不涉及。 **取值范围：** 字符串，长度0到64个字符。 **默认取值：** 不涉及。

        :param sk: The sk of this VendorAccountCreateRequest.
        :type sk: str
        """
        self._sk = sk

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
        if not isinstance(other, VendorAccountCreateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
