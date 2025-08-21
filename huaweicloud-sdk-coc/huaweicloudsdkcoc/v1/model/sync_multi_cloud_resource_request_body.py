# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SyncMultiCloudResourceRequestBody:

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
        'account_id': 'str'
    }

    attribute_map = {
        'vendor': 'vendor',
        'account_id': 'account_id'
    }

    def __init__(self, vendor=None, account_id=None):
        r"""SyncMultiCloudResourceRequestBody

        The model defined in huaweicloud sdk

        :param vendor: **参数解释：** 云广商信息。 **约束限制：** 不涉及。 **取值范围：** - RMS： 华为云。 - AWS：亚马逊。 - AZURE：微软。 - ALI：阿里云。 - VMWARE：VMware。 - OPENSTACK：openstack云平台。 - HCS：Huawei Cloud Stack。 - OTHER：其他云广商。 **默认取值：** 不涉及。
        :type vendor: str
        :param account_id: **参数解释：** 供应商的账户ID。 **约束限制：** 不涉及。 **取值范围：** 字符串，长度0到64个字符。 **默认取值：** 不涉及。
        :type account_id: str
        """
        
        

        self._vendor = None
        self._account_id = None
        self.discriminator = None

        self.vendor = vendor
        if account_id is not None:
            self.account_id = account_id

    @property
    def vendor(self):
        r"""Gets the vendor of this SyncMultiCloudResourceRequestBody.

        **参数解释：** 云广商信息。 **约束限制：** 不涉及。 **取值范围：** - RMS： 华为云。 - AWS：亚马逊。 - AZURE：微软。 - ALI：阿里云。 - VMWARE：VMware。 - OPENSTACK：openstack云平台。 - HCS：Huawei Cloud Stack。 - OTHER：其他云广商。 **默认取值：** 不涉及。

        :return: The vendor of this SyncMultiCloudResourceRequestBody.
        :rtype: str
        """
        return self._vendor

    @vendor.setter
    def vendor(self, vendor):
        r"""Sets the vendor of this SyncMultiCloudResourceRequestBody.

        **参数解释：** 云广商信息。 **约束限制：** 不涉及。 **取值范围：** - RMS： 华为云。 - AWS：亚马逊。 - AZURE：微软。 - ALI：阿里云。 - VMWARE：VMware。 - OPENSTACK：openstack云平台。 - HCS：Huawei Cloud Stack。 - OTHER：其他云广商。 **默认取值：** 不涉及。

        :param vendor: The vendor of this SyncMultiCloudResourceRequestBody.
        :type vendor: str
        """
        self._vendor = vendor

    @property
    def account_id(self):
        r"""Gets the account_id of this SyncMultiCloudResourceRequestBody.

        **参数解释：** 供应商的账户ID。 **约束限制：** 不涉及。 **取值范围：** 字符串，长度0到64个字符。 **默认取值：** 不涉及。

        :return: The account_id of this SyncMultiCloudResourceRequestBody.
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        r"""Sets the account_id of this SyncMultiCloudResourceRequestBody.

        **参数解释：** 供应商的账户ID。 **约束限制：** 不涉及。 **取值范围：** 字符串，长度0到64个字符。 **默认取值：** 不涉及。

        :param account_id: The account_id of this SyncMultiCloudResourceRequestBody.
        :type account_id: str
        """
        self._account_id = account_id

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
        if not isinstance(other, SyncMultiCloudResourceRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
