# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListKmsTdeKeyResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'key_details': 'list[ListKmsTdeKeyResponseBodyKeyDetails]',
        'authorized_id': 'str',
        'authorized_name': 'str'
    }

    attribute_map = {
        'key_details': 'key_details',
        'authorized_id': 'authorized_id',
        'authorized_name': 'authorized_name'
    }

    def __init__(self, key_details=None, authorized_id=None, authorized_name=None):
        r"""ListKmsTdeKeyResponse

        The model defined in huaweicloud sdk

        :param key_details: **参数解释**: kms秘钥列表。
        :type key_details: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.ListKmsTdeKeyResponseBodyKeyDetails`]
        :param authorized_id: **参数解释**: 授权用户ID，在开启透明加密能力时，必须对当前用户ID进行授权。 授权操作参考创建授权接口 https://support.huaweicloud.com/api-dew/CreateGrant.html。 **取值范围**: 不涉及。
        :type authorized_id: str
        :param authorized_name: **参数解释**: 授权用户名称。 **取值范围**: 不涉及。
        :type authorized_name: str
        """
        
        super(ListKmsTdeKeyResponse, self).__init__()

        self._key_details = None
        self._authorized_id = None
        self._authorized_name = None
        self.discriminator = None

        if key_details is not None:
            self.key_details = key_details
        if authorized_id is not None:
            self.authorized_id = authorized_id
        if authorized_name is not None:
            self.authorized_name = authorized_name

    @property
    def key_details(self):
        r"""Gets the key_details of this ListKmsTdeKeyResponse.

        **参数解释**: kms秘钥列表。

        :return: The key_details of this ListKmsTdeKeyResponse.
        :rtype: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.ListKmsTdeKeyResponseBodyKeyDetails`]
        """
        return self._key_details

    @key_details.setter
    def key_details(self, key_details):
        r"""Sets the key_details of this ListKmsTdeKeyResponse.

        **参数解释**: kms秘钥列表。

        :param key_details: The key_details of this ListKmsTdeKeyResponse.
        :type key_details: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.ListKmsTdeKeyResponseBodyKeyDetails`]
        """
        self._key_details = key_details

    @property
    def authorized_id(self):
        r"""Gets the authorized_id of this ListKmsTdeKeyResponse.

        **参数解释**: 授权用户ID，在开启透明加密能力时，必须对当前用户ID进行授权。 授权操作参考创建授权接口 https://support.huaweicloud.com/api-dew/CreateGrant.html。 **取值范围**: 不涉及。

        :return: The authorized_id of this ListKmsTdeKeyResponse.
        :rtype: str
        """
        return self._authorized_id

    @authorized_id.setter
    def authorized_id(self, authorized_id):
        r"""Sets the authorized_id of this ListKmsTdeKeyResponse.

        **参数解释**: 授权用户ID，在开启透明加密能力时，必须对当前用户ID进行授权。 授权操作参考创建授权接口 https://support.huaweicloud.com/api-dew/CreateGrant.html。 **取值范围**: 不涉及。

        :param authorized_id: The authorized_id of this ListKmsTdeKeyResponse.
        :type authorized_id: str
        """
        self._authorized_id = authorized_id

    @property
    def authorized_name(self):
        r"""Gets the authorized_name of this ListKmsTdeKeyResponse.

        **参数解释**: 授权用户名称。 **取值范围**: 不涉及。

        :return: The authorized_name of this ListKmsTdeKeyResponse.
        :rtype: str
        """
        return self._authorized_name

    @authorized_name.setter
    def authorized_name(self, authorized_name):
        r"""Sets the authorized_name of this ListKmsTdeKeyResponse.

        **参数解释**: 授权用户名称。 **取值范围**: 不涉及。

        :param authorized_name: The authorized_name of this ListKmsTdeKeyResponse.
        :type authorized_name: str
        """
        self._authorized_name = authorized_name

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
        if not isinstance(other, ListKmsTdeKeyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
