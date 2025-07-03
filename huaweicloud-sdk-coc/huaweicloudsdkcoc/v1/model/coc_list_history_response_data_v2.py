# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CocListHistoryResponseDataV2:

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
        'info': 'list[CocTicketHistoryBaseInfoV2]'
    }

    attribute_map = {
        'total': 'total',
        'info': 'info'
    }

    def __init__(self, total=None, info=None):
        r"""CocListHistoryResponseDataV2

        The model defined in huaweicloud sdk

        :param total: 总数
        :type total: int
        :param info: 历史详情
        :type info: list[:class:`huaweicloudsdkcoc.v1.CocTicketHistoryBaseInfoV2`]
        """
        
        

        self._total = None
        self._info = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if info is not None:
            self.info = info

    @property
    def total(self):
        r"""Gets the total of this CocListHistoryResponseDataV2.

        总数

        :return: The total of this CocListHistoryResponseDataV2.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this CocListHistoryResponseDataV2.

        总数

        :param total: The total of this CocListHistoryResponseDataV2.
        :type total: int
        """
        self._total = total

    @property
    def info(self):
        r"""Gets the info of this CocListHistoryResponseDataV2.

        历史详情

        :return: The info of this CocListHistoryResponseDataV2.
        :rtype: list[:class:`huaweicloudsdkcoc.v1.CocTicketHistoryBaseInfoV2`]
        """
        return self._info

    @info.setter
    def info(self, info):
        r"""Sets the info of this CocListHistoryResponseDataV2.

        历史详情

        :param info: The info of this CocListHistoryResponseDataV2.
        :type info: list[:class:`huaweicloudsdkcoc.v1.CocTicketHistoryBaseInfoV2`]
        """
        self._info = info

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
        if not isinstance(other, CocListHistoryResponseDataV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
