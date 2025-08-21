# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListUserKeysResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'keys': 'list[SSHKeyDto]',
        'total': 'int'
    }

    attribute_map = {
        'keys': 'keys',
        'total': 'total'
    }

    def __init__(self, keys=None, total=None):
        r"""ListUserKeysResponse

        The model defined in huaweicloud sdk

        :param keys: **参数解释：** 密钥列表。 **取值范围：** 列表长度不少于0，不超过1000。
        :type keys: list[:class:`huaweicloudsdkcodehub.v4.SSHKeyDto`]
        :param total: **参数解释：** 结果条数。
        :type total: int
        """
        
        super(ListUserKeysResponse, self).__init__()

        self._keys = None
        self._total = None
        self.discriminator = None

        if keys is not None:
            self.keys = keys
        if total is not None:
            self.total = total

    @property
    def keys(self):
        r"""Gets the keys of this ListUserKeysResponse.

        **参数解释：** 密钥列表。 **取值范围：** 列表长度不少于0，不超过1000。

        :return: The keys of this ListUserKeysResponse.
        :rtype: list[:class:`huaweicloudsdkcodehub.v4.SSHKeyDto`]
        """
        return self._keys

    @keys.setter
    def keys(self, keys):
        r"""Sets the keys of this ListUserKeysResponse.

        **参数解释：** 密钥列表。 **取值范围：** 列表长度不少于0，不超过1000。

        :param keys: The keys of this ListUserKeysResponse.
        :type keys: list[:class:`huaweicloudsdkcodehub.v4.SSHKeyDto`]
        """
        self._keys = keys

    @property
    def total(self):
        r"""Gets the total of this ListUserKeysResponse.

        **参数解释：** 结果条数。

        :return: The total of this ListUserKeysResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListUserKeysResponse.

        **参数解释：** 结果条数。

        :param total: The total of this ListUserKeysResponse.
        :type total: int
        """
        self._total = total

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
        if not isinstance(other, ListUserKeysResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
