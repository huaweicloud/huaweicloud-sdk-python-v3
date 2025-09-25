# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListWaitEventResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total': 'int',
        'rows': 'WaitEventResult'
    }

    attribute_map = {
        'total': 'total',
        'rows': 'rows'
    }

    def __init__(self, total=None, rows=None):
        r"""ListWaitEventResponse

        The model defined in huaweicloud sdk

        :param total: **参数解释**: 等待事件的总数量。 **取值范围**: 不涉及。
        :type total: int
        :param rows: 
        :type rows: :class:`huaweicloudsdkgaussdbforopengauss.v3.WaitEventResult`
        """
        
        super(ListWaitEventResponse, self).__init__()

        self._total = None
        self._rows = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if rows is not None:
            self.rows = rows

    @property
    def total(self):
        r"""Gets the total of this ListWaitEventResponse.

        **参数解释**: 等待事件的总数量。 **取值范围**: 不涉及。

        :return: The total of this ListWaitEventResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListWaitEventResponse.

        **参数解释**: 等待事件的总数量。 **取值范围**: 不涉及。

        :param total: The total of this ListWaitEventResponse.
        :type total: int
        """
        self._total = total

    @property
    def rows(self):
        r"""Gets the rows of this ListWaitEventResponse.

        :return: The rows of this ListWaitEventResponse.
        :rtype: :class:`huaweicloudsdkgaussdbforopengauss.v3.WaitEventResult`
        """
        return self._rows

    @rows.setter
    def rows(self, rows):
        r"""Sets the rows of this ListWaitEventResponse.

        :param rows: The rows of this ListWaitEventResponse.
        :type rows: :class:`huaweicloudsdkgaussdbforopengauss.v3.WaitEventResult`
        """
        self._rows = rows

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
        if not isinstance(other, ListWaitEventResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
