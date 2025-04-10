# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCsrResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'csr_list': 'list[CSRResponseBody]',
        'total': 'int'
    }

    attribute_map = {
        'csr_list': 'csr_list',
        'total': 'total'
    }

    def __init__(self, csr_list=None, total=None):
        r"""ListCsrResponse

        The model defined in huaweicloud sdk

        :param csr_list: CSR列表，详情请参见CSRResponseBody字段数据结构说明。
        :type csr_list: list[:class:`huaweicloudsdkscm.v3.CSRResponseBody`]
        :param total: CSR数量。
        :type total: int
        """
        
        super(ListCsrResponse, self).__init__()

        self._csr_list = None
        self._total = None
        self.discriminator = None

        if csr_list is not None:
            self.csr_list = csr_list
        if total is not None:
            self.total = total

    @property
    def csr_list(self):
        r"""Gets the csr_list of this ListCsrResponse.

        CSR列表，详情请参见CSRResponseBody字段数据结构说明。

        :return: The csr_list of this ListCsrResponse.
        :rtype: list[:class:`huaweicloudsdkscm.v3.CSRResponseBody`]
        """
        return self._csr_list

    @csr_list.setter
    def csr_list(self, csr_list):
        r"""Sets the csr_list of this ListCsrResponse.

        CSR列表，详情请参见CSRResponseBody字段数据结构说明。

        :param csr_list: The csr_list of this ListCsrResponse.
        :type csr_list: list[:class:`huaweicloudsdkscm.v3.CSRResponseBody`]
        """
        self._csr_list = csr_list

    @property
    def total(self):
        r"""Gets the total of this ListCsrResponse.

        CSR数量。

        :return: The total of this ListCsrResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListCsrResponse.

        CSR数量。

        :param total: The total of this ListCsrResponse.
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
        if not isinstance(other, ListCsrResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
