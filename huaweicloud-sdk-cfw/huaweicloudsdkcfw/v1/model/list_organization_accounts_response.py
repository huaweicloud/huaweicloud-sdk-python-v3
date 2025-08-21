# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListOrganizationAccountsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'data': 'list[OrganizationAccountInfo]',
        'marker': 'str',
        'total': 'int'
    }

    attribute_map = {
        'data': 'data',
        'marker': 'marker',
        'total': 'total'
    }

    def __init__(self, data=None, marker=None, total=None):
        r"""ListOrganizationAccountsResponse

        The model defined in huaweicloud sdk

        :param data: **参数解释**： 查询组织账号响应 **取值范围**： 不涉及
        :type data: list[:class:`huaweicloudsdkcfw.v1.OrganizationAccountInfo`]
        :param marker: **参数解释**： 分页标记 **取值范围**： 不涉及
        :type marker: str
        :param total: **参数解释**： 总数 **取值范围**： 不涉及
        :type total: int
        """
        
        super(ListOrganizationAccountsResponse, self).__init__()

        self._data = None
        self._marker = None
        self._total = None
        self.discriminator = None

        if data is not None:
            self.data = data
        if marker is not None:
            self.marker = marker
        if total is not None:
            self.total = total

    @property
    def data(self):
        r"""Gets the data of this ListOrganizationAccountsResponse.

        **参数解释**： 查询组织账号响应 **取值范围**： 不涉及

        :return: The data of this ListOrganizationAccountsResponse.
        :rtype: list[:class:`huaweicloudsdkcfw.v1.OrganizationAccountInfo`]
        """
        return self._data

    @data.setter
    def data(self, data):
        r"""Sets the data of this ListOrganizationAccountsResponse.

        **参数解释**： 查询组织账号响应 **取值范围**： 不涉及

        :param data: The data of this ListOrganizationAccountsResponse.
        :type data: list[:class:`huaweicloudsdkcfw.v1.OrganizationAccountInfo`]
        """
        self._data = data

    @property
    def marker(self):
        r"""Gets the marker of this ListOrganizationAccountsResponse.

        **参数解释**： 分页标记 **取值范围**： 不涉及

        :return: The marker of this ListOrganizationAccountsResponse.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListOrganizationAccountsResponse.

        **参数解释**： 分页标记 **取值范围**： 不涉及

        :param marker: The marker of this ListOrganizationAccountsResponse.
        :type marker: str
        """
        self._marker = marker

    @property
    def total(self):
        r"""Gets the total of this ListOrganizationAccountsResponse.

        **参数解释**： 总数 **取值范围**： 不涉及

        :return: The total of this ListOrganizationAccountsResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListOrganizationAccountsResponse.

        **参数解释**： 总数 **取值范围**： 不涉及

        :param total: The total of this ListOrganizationAccountsResponse.
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
        if not isinstance(other, ListOrganizationAccountsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
