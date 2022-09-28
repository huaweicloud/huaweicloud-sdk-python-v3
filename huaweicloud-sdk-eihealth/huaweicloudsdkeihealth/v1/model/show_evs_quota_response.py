# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowEvsQuotaResponse(SdkResponse):

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
        'usage': 'int',
        'unit': 'str'
    }

    attribute_map = {
        'total': 'total',
        'usage': 'usage',
        'unit': 'unit'
    }

    def __init__(self, total=None, usage=None, unit=None):
        """ShowEvsQuotaResponse

        The model defined in huaweicloud sdk

        :param total: 总配额
        :type total: int
        :param usage: 已使用
        :type usage: int
        :param unit: 单位
        :type unit: str
        """
        
        super(ShowEvsQuotaResponse, self).__init__()

        self._total = None
        self._usage = None
        self._unit = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if usage is not None:
            self.usage = usage
        if unit is not None:
            self.unit = unit

    @property
    def total(self):
        """Gets the total of this ShowEvsQuotaResponse.

        总配额

        :return: The total of this ShowEvsQuotaResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ShowEvsQuotaResponse.

        总配额

        :param total: The total of this ShowEvsQuotaResponse.
        :type total: int
        """
        self._total = total

    @property
    def usage(self):
        """Gets the usage of this ShowEvsQuotaResponse.

        已使用

        :return: The usage of this ShowEvsQuotaResponse.
        :rtype: int
        """
        return self._usage

    @usage.setter
    def usage(self, usage):
        """Sets the usage of this ShowEvsQuotaResponse.

        已使用

        :param usage: The usage of this ShowEvsQuotaResponse.
        :type usage: int
        """
        self._usage = usage

    @property
    def unit(self):
        """Gets the unit of this ShowEvsQuotaResponse.

        单位

        :return: The unit of this ShowEvsQuotaResponse.
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this ShowEvsQuotaResponse.

        单位

        :param unit: The unit of this ShowEvsQuotaResponse.
        :type unit: str
        """
        self._unit = unit

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
        if not isinstance(other, ShowEvsQuotaResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
