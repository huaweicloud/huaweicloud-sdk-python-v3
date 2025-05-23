# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListFlavorsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'flavors': 'list[Flavor]',
        'total': 'int'
    }

    attribute_map = {
        'flavors': 'flavors',
        'total': 'total'
    }

    def __init__(self, flavors=None, total=None):
        r"""ListFlavorsResponse

        The model defined in huaweicloud sdk

        :param flavors: 实例规格信息。
        :type flavors: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.Flavor`]
        :param total: 查询的记录总数
        :type total: int
        """
        
        super(ListFlavorsResponse, self).__init__()

        self._flavors = None
        self._total = None
        self.discriminator = None

        if flavors is not None:
            self.flavors = flavors
        if total is not None:
            self.total = total

    @property
    def flavors(self):
        r"""Gets the flavors of this ListFlavorsResponse.

        实例规格信息。

        :return: The flavors of this ListFlavorsResponse.
        :rtype: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.Flavor`]
        """
        return self._flavors

    @flavors.setter
    def flavors(self, flavors):
        r"""Sets the flavors of this ListFlavorsResponse.

        实例规格信息。

        :param flavors: The flavors of this ListFlavorsResponse.
        :type flavors: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.Flavor`]
        """
        self._flavors = flavors

    @property
    def total(self):
        r"""Gets the total of this ListFlavorsResponse.

        查询的记录总数

        :return: The total of this ListFlavorsResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListFlavorsResponse.

        查询的记录总数

        :param total: The total of this ListFlavorsResponse.
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
        if not isinstance(other, ListFlavorsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
