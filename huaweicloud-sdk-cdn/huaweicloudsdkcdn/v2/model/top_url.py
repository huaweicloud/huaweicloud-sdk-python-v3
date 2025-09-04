# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TopUrl:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enable': 'bool',
        'limit': 'int',
        'sort_by_code': 'bool'
    }

    attribute_map = {
        'enable': 'enable',
        'limit': 'limit',
        'sort_by_code': 'sort_by_code'
    }

    def __init__(self, enable=None, limit=None, sort_by_code=None):
        r"""TopUrl

        The model defined in huaweicloud sdk

        :param enable: 配置开关
        :type enable: bool
        :param limit: 热点统计配置指标的上报数量。如top_url 100、top_url 1000
        :type limit: int
        :param sort_by_code: 热点统计类指标是否支持按状态码上报
        :type sort_by_code: bool
        """
        
        

        self._enable = None
        self._limit = None
        self._sort_by_code = None
        self.discriminator = None

        if enable is not None:
            self.enable = enable
        if limit is not None:
            self.limit = limit
        if sort_by_code is not None:
            self.sort_by_code = sort_by_code

    @property
    def enable(self):
        r"""Gets the enable of this TopUrl.

        配置开关

        :return: The enable of this TopUrl.
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        r"""Sets the enable of this TopUrl.

        配置开关

        :param enable: The enable of this TopUrl.
        :type enable: bool
        """
        self._enable = enable

    @property
    def limit(self):
        r"""Gets the limit of this TopUrl.

        热点统计配置指标的上报数量。如top_url 100、top_url 1000

        :return: The limit of this TopUrl.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this TopUrl.

        热点统计配置指标的上报数量。如top_url 100、top_url 1000

        :param limit: The limit of this TopUrl.
        :type limit: int
        """
        self._limit = limit

    @property
    def sort_by_code(self):
        r"""Gets the sort_by_code of this TopUrl.

        热点统计类指标是否支持按状态码上报

        :return: The sort_by_code of this TopUrl.
        :rtype: bool
        """
        return self._sort_by_code

    @sort_by_code.setter
    def sort_by_code(self, sort_by_code):
        r"""Sets the sort_by_code of this TopUrl.

        热点统计类指标是否支持按状态码上报

        :param sort_by_code: The sort_by_code of this TopUrl.
        :type sort_by_code: bool
        """
        self._sort_by_code = sort_by_code

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
        if not isinstance(other, TopUrl):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
