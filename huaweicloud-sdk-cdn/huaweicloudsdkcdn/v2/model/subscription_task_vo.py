# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SubscriptionTaskVo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'period_type': 'int',
        'emails': 'str',
        'domain_name': 'str',
        'report_type': 'str'
    }

    attribute_map = {
        'name': 'name',
        'period_type': 'period_type',
        'emails': 'emails',
        'domain_name': 'domain_name',
        'report_type': 'report_type'
    }

    def __init__(self, name=None, period_type=None, emails=None, domain_name=None, report_type=None):
        r"""SubscriptionTaskVo

        The model defined in huaweicloud sdk

        :param name: - 订阅任务的名称 - [单词字符] [减号] [中文字符] 长度不超过32
        :type name: str
        :param period_type: - 订阅任务类型，类型如下： - 0：日报 - 1：周报 - 2：月报
        :type period_type: int
        :param emails: 接收运营报表的邮箱地址。支持同时输入多个邮箱地址，多个邮箱地址用英文逗号（,）分隔。
        :type emails: str
        :param domain_name: 订阅的域名列表，支持同时输入多个域名，多个域名用半角逗号（,）分隔；说明：如果该参数为all，则为账号下的所有域名订阅运营报表。
        :type domain_name: str
        :param report_type: - 运营报表类型。支持同时输入多个报表类型，多个报表类型以英文逗号（,）分隔。 - 0：访问区域分布 - 1：国家分布 - 2：运营商分布 - 3：域名排行（按流量排序） - 4：热门URL（按流量排序） - 5：热门URL（按请求数排序） - 6：热门Referer（按流量排序） - 7：热门Referer（按请求数排序） - 10：回源热门URL（按流量排序） - 11：回源热门URL（按请求数排序） - 13：热门UA（按流量排序） - 14：热门UA（按请求数排序）
        :type report_type: str
        """
        
        

        self._name = None
        self._period_type = None
        self._emails = None
        self._domain_name = None
        self._report_type = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if period_type is not None:
            self.period_type = period_type
        if emails is not None:
            self.emails = emails
        if domain_name is not None:
            self.domain_name = domain_name
        if report_type is not None:
            self.report_type = report_type

    @property
    def name(self):
        r"""Gets the name of this SubscriptionTaskVo.

        - 订阅任务的名称 - [单词字符] [减号] [中文字符] 长度不超过32

        :return: The name of this SubscriptionTaskVo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this SubscriptionTaskVo.

        - 订阅任务的名称 - [单词字符] [减号] [中文字符] 长度不超过32

        :param name: The name of this SubscriptionTaskVo.
        :type name: str
        """
        self._name = name

    @property
    def period_type(self):
        r"""Gets the period_type of this SubscriptionTaskVo.

        - 订阅任务类型，类型如下： - 0：日报 - 1：周报 - 2：月报

        :return: The period_type of this SubscriptionTaskVo.
        :rtype: int
        """
        return self._period_type

    @period_type.setter
    def period_type(self, period_type):
        r"""Sets the period_type of this SubscriptionTaskVo.

        - 订阅任务类型，类型如下： - 0：日报 - 1：周报 - 2：月报

        :param period_type: The period_type of this SubscriptionTaskVo.
        :type period_type: int
        """
        self._period_type = period_type

    @property
    def emails(self):
        r"""Gets the emails of this SubscriptionTaskVo.

        接收运营报表的邮箱地址。支持同时输入多个邮箱地址，多个邮箱地址用英文逗号（,）分隔。

        :return: The emails of this SubscriptionTaskVo.
        :rtype: str
        """
        return self._emails

    @emails.setter
    def emails(self, emails):
        r"""Sets the emails of this SubscriptionTaskVo.

        接收运营报表的邮箱地址。支持同时输入多个邮箱地址，多个邮箱地址用英文逗号（,）分隔。

        :param emails: The emails of this SubscriptionTaskVo.
        :type emails: str
        """
        self._emails = emails

    @property
    def domain_name(self):
        r"""Gets the domain_name of this SubscriptionTaskVo.

        订阅的域名列表，支持同时输入多个域名，多个域名用半角逗号（,）分隔；说明：如果该参数为all，则为账号下的所有域名订阅运营报表。

        :return: The domain_name of this SubscriptionTaskVo.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        r"""Sets the domain_name of this SubscriptionTaskVo.

        订阅的域名列表，支持同时输入多个域名，多个域名用半角逗号（,）分隔；说明：如果该参数为all，则为账号下的所有域名订阅运营报表。

        :param domain_name: The domain_name of this SubscriptionTaskVo.
        :type domain_name: str
        """
        self._domain_name = domain_name

    @property
    def report_type(self):
        r"""Gets the report_type of this SubscriptionTaskVo.

        - 运营报表类型。支持同时输入多个报表类型，多个报表类型以英文逗号（,）分隔。 - 0：访问区域分布 - 1：国家分布 - 2：运营商分布 - 3：域名排行（按流量排序） - 4：热门URL（按流量排序） - 5：热门URL（按请求数排序） - 6：热门Referer（按流量排序） - 7：热门Referer（按请求数排序） - 10：回源热门URL（按流量排序） - 11：回源热门URL（按请求数排序） - 13：热门UA（按流量排序） - 14：热门UA（按请求数排序）

        :return: The report_type of this SubscriptionTaskVo.
        :rtype: str
        """
        return self._report_type

    @report_type.setter
    def report_type(self, report_type):
        r"""Sets the report_type of this SubscriptionTaskVo.

        - 运营报表类型。支持同时输入多个报表类型，多个报表类型以英文逗号（,）分隔。 - 0：访问区域分布 - 1：国家分布 - 2：运营商分布 - 3：域名排行（按流量排序） - 4：热门URL（按流量排序） - 5：热门URL（按请求数排序） - 6：热门Referer（按流量排序） - 7：热门Referer（按请求数排序） - 10：回源热门URL（按流量排序） - 11：回源热门URL（按请求数排序） - 13：热门UA（按流量排序） - 14：热门UA（按请求数排序）

        :param report_type: The report_type of this SubscriptionTaskVo.
        :type report_type: str
        """
        self._report_type = report_type

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
        if not isinstance(other, SubscriptionTaskVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
