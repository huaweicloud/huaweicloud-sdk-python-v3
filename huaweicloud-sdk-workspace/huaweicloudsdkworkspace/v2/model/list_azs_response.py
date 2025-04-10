# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAzsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'support_type': 'list[str]',
        'default_type': 'str',
        'azs': 'dict(str, list[AzInfo])'
    }

    attribute_map = {
        'support_type': 'support_type',
        'default_type': 'default_type',
        'azs': 'azs'
    }

    def __init__(self, support_type=None, default_type=None, azs=None):
        r"""ListAzsResponse

        The model defined in huaweicloud sdk

        :param support_type: 支持类型。
        :type support_type: list[str]
        :param default_type: 默认类型。
        :type default_type: str
        :param azs: 可用区。
        :type azs: dict(str, list[AzInfo])
        """
        
        super(ListAzsResponse, self).__init__()

        self._support_type = None
        self._default_type = None
        self._azs = None
        self.discriminator = None

        if support_type is not None:
            self.support_type = support_type
        if default_type is not None:
            self.default_type = default_type
        if azs is not None:
            self.azs = azs

    @property
    def support_type(self):
        r"""Gets the support_type of this ListAzsResponse.

        支持类型。

        :return: The support_type of this ListAzsResponse.
        :rtype: list[str]
        """
        return self._support_type

    @support_type.setter
    def support_type(self, support_type):
        r"""Sets the support_type of this ListAzsResponse.

        支持类型。

        :param support_type: The support_type of this ListAzsResponse.
        :type support_type: list[str]
        """
        self._support_type = support_type

    @property
    def default_type(self):
        r"""Gets the default_type of this ListAzsResponse.

        默认类型。

        :return: The default_type of this ListAzsResponse.
        :rtype: str
        """
        return self._default_type

    @default_type.setter
    def default_type(self, default_type):
        r"""Sets the default_type of this ListAzsResponse.

        默认类型。

        :param default_type: The default_type of this ListAzsResponse.
        :type default_type: str
        """
        self._default_type = default_type

    @property
    def azs(self):
        r"""Gets the azs of this ListAzsResponse.

        可用区。

        :return: The azs of this ListAzsResponse.
        :rtype: dict(str, list[AzInfo])
        """
        return self._azs

    @azs.setter
    def azs(self, azs):
        r"""Sets the azs of this ListAzsResponse.

        可用区。

        :param azs: The azs of this ListAzsResponse.
        :type azs: dict(str, list[AzInfo])
        """
        self._azs = azs

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
        if not isinstance(other, ListAzsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
