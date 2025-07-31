# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WebSiteStatisticsResponseInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'domain': 'str',
        'num': 'int'
    }

    attribute_map = {
        'domain': 'domain',
        'num': 'num'
    }

    def __init__(self, domain=None, num=None):
        r"""WebSiteStatisticsResponseInfo

        The model defined in huaweicloud sdk

        :param domain: Web站点域名
        :type domain: str
        :param num: Web站点统计信息总数
        :type num: int
        """
        
        

        self._domain = None
        self._num = None
        self.discriminator = None

        if domain is not None:
            self.domain = domain
        if num is not None:
            self.num = num

    @property
    def domain(self):
        r"""Gets the domain of this WebSiteStatisticsResponseInfo.

        Web站点域名

        :return: The domain of this WebSiteStatisticsResponseInfo.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        r"""Sets the domain of this WebSiteStatisticsResponseInfo.

        Web站点域名

        :param domain: The domain of this WebSiteStatisticsResponseInfo.
        :type domain: str
        """
        self._domain = domain

    @property
    def num(self):
        r"""Gets the num of this WebSiteStatisticsResponseInfo.

        Web站点统计信息总数

        :return: The num of this WebSiteStatisticsResponseInfo.
        :rtype: int
        """
        return self._num

    @num.setter
    def num(self, num):
        r"""Sets the num of this WebSiteStatisticsResponseInfo.

        Web站点统计信息总数

        :param num: The num of this WebSiteStatisticsResponseInfo.
        :type num: int
        """
        self._num = num

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
        if not isinstance(other, WebSiteStatisticsResponseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
