# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAspInfosResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'asp': 'list[ListAspResult]',
        'total_count': 'int'
    }

    attribute_map = {
        'asp': 'asp',
        'total_count': 'total_count'
    }

    def __init__(self, asp=None, total_count=None):
        r"""ListAspInfosResponse

        The model defined in huaweicloud sdk

        :param asp: **参数解释**: asp报告信息列表。
        :type asp: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.ListAspResult`]
        :param total_count: **参数解释**: 总记录数。 **取值范围**: 不涉及。
        :type total_count: int
        """
        
        super(ListAspInfosResponse, self).__init__()

        self._asp = None
        self._total_count = None
        self.discriminator = None

        if asp is not None:
            self.asp = asp
        if total_count is not None:
            self.total_count = total_count

    @property
    def asp(self):
        r"""Gets the asp of this ListAspInfosResponse.

        **参数解释**: asp报告信息列表。

        :return: The asp of this ListAspInfosResponse.
        :rtype: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.ListAspResult`]
        """
        return self._asp

    @asp.setter
    def asp(self, asp):
        r"""Sets the asp of this ListAspInfosResponse.

        **参数解释**: asp报告信息列表。

        :param asp: The asp of this ListAspInfosResponse.
        :type asp: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.ListAspResult`]
        """
        self._asp = asp

    @property
    def total_count(self):
        r"""Gets the total_count of this ListAspInfosResponse.

        **参数解释**: 总记录数。 **取值范围**: 不涉及。

        :return: The total_count of this ListAspInfosResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this ListAspInfosResponse.

        **参数解释**: 总记录数。 **取值范围**: 不涉及。

        :param total_count: The total_count of this ListAspInfosResponse.
        :type total_count: int
        """
        self._total_count = total_count

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
        if not isinstance(other, ListAspInfosResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
