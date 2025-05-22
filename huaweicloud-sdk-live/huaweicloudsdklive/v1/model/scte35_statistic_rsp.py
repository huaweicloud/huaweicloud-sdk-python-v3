# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SCTE35StatisticRsp:

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
        'scte35_info': 'list[SCTE35InfoItem]'
    }

    attribute_map = {
        'total': 'total',
        'scte35_info': 'scte35_info'
    }

    def __init__(self, total=None, scte35_info=None):
        r"""SCTE35StatisticRsp

        The model defined in huaweicloud sdk

        :param total: 查询到scet35信息的总个数。
        :type total: int
        :param scte35_info: 详细的scte35信号的数组。
        :type scte35_info: list[:class:`huaweicloudsdklive.v1.SCTE35InfoItem`]
        """
        
        

        self._total = None
        self._scte35_info = None
        self.discriminator = None

        self.total = total
        if scte35_info is not None:
            self.scte35_info = scte35_info

    @property
    def total(self):
        r"""Gets the total of this SCTE35StatisticRsp.

        查询到scet35信息的总个数。

        :return: The total of this SCTE35StatisticRsp.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this SCTE35StatisticRsp.

        查询到scet35信息的总个数。

        :param total: The total of this SCTE35StatisticRsp.
        :type total: int
        """
        self._total = total

    @property
    def scte35_info(self):
        r"""Gets the scte35_info of this SCTE35StatisticRsp.

        详细的scte35信号的数组。

        :return: The scte35_info of this SCTE35StatisticRsp.
        :rtype: list[:class:`huaweicloudsdklive.v1.SCTE35InfoItem`]
        """
        return self._scte35_info

    @scte35_info.setter
    def scte35_info(self, scte35_info):
        r"""Sets the scte35_info of this SCTE35StatisticRsp.

        详细的scte35信号的数组。

        :param scte35_info: The scte35_info of this SCTE35StatisticRsp.
        :type scte35_info: list[:class:`huaweicloudsdklive.v1.SCTE35InfoItem`]
        """
        self._scte35_info = scte35_info

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
        if not isinstance(other, SCTE35StatisticRsp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
