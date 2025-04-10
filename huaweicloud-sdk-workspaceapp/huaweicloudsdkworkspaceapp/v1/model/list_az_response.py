# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAzResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'azs': 'dict(str, list[AvailabilityZoneInfo])',
        'default_type': 'str',
        'support_type': 'list[str]'
    }

    attribute_map = {
        'azs': 'azs',
        'default_type': 'default_type',
        'support_type': 'support_type'
    }

    def __init__(self, azs=None, default_type=None, support_type=None):
        r"""ListAzResponse

        The model defined in huaweicloud sdk

        :param azs: 云应用支持的可用分区表格，按站点分类。
        :type azs: dict(str, list[AvailabilityZoneInfo])
        :param default_type: 默认站点类型。
        :type default_type: str
        :param support_type: 云应用支持的站点类型。
        :type support_type: list[str]
        """
        
        super(ListAzResponse, self).__init__()

        self._azs = None
        self._default_type = None
        self._support_type = None
        self.discriminator = None

        if azs is not None:
            self.azs = azs
        if default_type is not None:
            self.default_type = default_type
        if support_type is not None:
            self.support_type = support_type

    @property
    def azs(self):
        r"""Gets the azs of this ListAzResponse.

        云应用支持的可用分区表格，按站点分类。

        :return: The azs of this ListAzResponse.
        :rtype: dict(str, list[AvailabilityZoneInfo])
        """
        return self._azs

    @azs.setter
    def azs(self, azs):
        r"""Sets the azs of this ListAzResponse.

        云应用支持的可用分区表格，按站点分类。

        :param azs: The azs of this ListAzResponse.
        :type azs: dict(str, list[AvailabilityZoneInfo])
        """
        self._azs = azs

    @property
    def default_type(self):
        r"""Gets the default_type of this ListAzResponse.

        默认站点类型。

        :return: The default_type of this ListAzResponse.
        :rtype: str
        """
        return self._default_type

    @default_type.setter
    def default_type(self, default_type):
        r"""Sets the default_type of this ListAzResponse.

        默认站点类型。

        :param default_type: The default_type of this ListAzResponse.
        :type default_type: str
        """
        self._default_type = default_type

    @property
    def support_type(self):
        r"""Gets the support_type of this ListAzResponse.

        云应用支持的站点类型。

        :return: The support_type of this ListAzResponse.
        :rtype: list[str]
        """
        return self._support_type

    @support_type.setter
    def support_type(self, support_type):
        r"""Sets the support_type of this ListAzResponse.

        云应用支持的站点类型。

        :param support_type: The support_type of this ListAzResponse.
        :type support_type: list[str]
        """
        self._support_type = support_type

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
        if not isinstance(other, ListAzResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
