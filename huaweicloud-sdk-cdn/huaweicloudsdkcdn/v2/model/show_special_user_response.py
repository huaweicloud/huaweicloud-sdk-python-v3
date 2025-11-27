# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowSpecialUserResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status': 'int',
        'metric': 'int',
        'flux_metric': 'int',
        'cy': 'int',
        'h6': 'int',
        'c': 'int',
        'sc': 'int',
        'bhc': 'int',
        'pi': 'int',
        'exp5': 'int',
        'm1': 'int',
        'is_month_m5': 'int',
        'exp_agy': 'int',
        'ces_report_site': 'int',
        'float': 'int',
        'is_show_up_bw': 'int'
    }

    attribute_map = {
        'status': 'status',
        'metric': 'metric',
        'flux_metric': 'flux_metric',
        'cy': 'cy',
        'h6': 'h6',
        'c': 'c',
        'sc': 'sc',
        'bhc': 'bhc',
        'pi': 'pi',
        'exp5': 'exp5',
        'm1': 'm1',
        'is_month_m5': 'is_month_m5',
        'exp_agy': 'exp_agy',
        'ces_report_site': 'ces_report_site',
        'float': 'float',
        'is_show_up_bw': 'is_show_up_bw'
    }

    def __init__(self, status=None, metric=None, flux_metric=None, cy=None, h6=None, c=None, sc=None, bhc=None, pi=None, exp5=None, m1=None, is_month_m5=None, exp_agy=None, ces_report_site=None, float=None, is_show_up_bw=None):
        r"""ShowSpecialUserResponse

        The model defined in huaweicloud sdk

        :param status: 1表示用户可以查询总请求时长枚举，0表示用户不可以查询总请求时长枚举
        :type status: int
        :param metric: 进制
        :type metric: int
        :param flux_metric: 流量进制
        :type flux_metric: int
        :param cy: 1表示用户可以，0表示用户不可以。是否是开放国家及地区界面用户
        :type cy: int
        :param h6: 1表示用户可以查询ipv6流量,https流量，0表示用户不可以
        :type h6: int
        :param c: 1表示用户可以查询具体的状态码详情，0表示用户不可以
        :type c: int
        :param sc: 1表示用户查询 top url 时要返回http状态码，0表示用户不返回
        :type sc: int
        :param bhc: 1表示该用户可以查询回源状态码，0表示不可以
        :type bhc: int
        :param pi: 1表示该用户可以查询protocol和IPVersion，0表示用户不可以
        :type pi: int
        :param exp5: 1表示该用户可以查询租户界面5分钟粒度数据导出白名单，0表示用户不可以
        :type exp5: int
        :param m1: 1表示该用户可以查询1分钟粒度统计数据，0表示用户不可以
        :type m1: int
        :param is_month_m5: 1表示该用户可以查询1个月5分钟粒度统计数据，0表示用户不可以
        :type is_month_m5: int
        :param exp_agy: 1表示该用户可以在租户界面指定下载链接可用范围，0表示用户不可以
        :type exp_agy: int
        :param ces_report_site: 1表示该用户可以是否上报到国际站CES，0表示用户不可以
        :type ces_report_site: int
        :param float: 1表示该用户按上浮系数展示数据，0表示用户不可以
        :type float: int
        :param is_show_up_bw: 1表示该用户允许查询入网带宽，0表示用户不可以
        :type is_show_up_bw: int
        """
        
        super().__init__()

        self._status = None
        self._metric = None
        self._flux_metric = None
        self._cy = None
        self._h6 = None
        self._c = None
        self._sc = None
        self._bhc = None
        self._pi = None
        self._exp5 = None
        self._m1 = None
        self._is_month_m5 = None
        self._exp_agy = None
        self._ces_report_site = None
        self._float = None
        self._is_show_up_bw = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if metric is not None:
            self.metric = metric
        if flux_metric is not None:
            self.flux_metric = flux_metric
        if cy is not None:
            self.cy = cy
        if h6 is not None:
            self.h6 = h6
        if c is not None:
            self.c = c
        if sc is not None:
            self.sc = sc
        if bhc is not None:
            self.bhc = bhc
        if pi is not None:
            self.pi = pi
        if exp5 is not None:
            self.exp5 = exp5
        if m1 is not None:
            self.m1 = m1
        if is_month_m5 is not None:
            self.is_month_m5 = is_month_m5
        if exp_agy is not None:
            self.exp_agy = exp_agy
        if ces_report_site is not None:
            self.ces_report_site = ces_report_site
        if float is not None:
            self.float = float
        if is_show_up_bw is not None:
            self.is_show_up_bw = is_show_up_bw

    @property
    def status(self):
        r"""Gets the status of this ShowSpecialUserResponse.

        1表示用户可以查询总请求时长枚举，0表示用户不可以查询总请求时长枚举

        :return: The status of this ShowSpecialUserResponse.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ShowSpecialUserResponse.

        1表示用户可以查询总请求时长枚举，0表示用户不可以查询总请求时长枚举

        :param status: The status of this ShowSpecialUserResponse.
        :type status: int
        """
        self._status = status

    @property
    def metric(self):
        r"""Gets the metric of this ShowSpecialUserResponse.

        进制

        :return: The metric of this ShowSpecialUserResponse.
        :rtype: int
        """
        return self._metric

    @metric.setter
    def metric(self, metric):
        r"""Sets the metric of this ShowSpecialUserResponse.

        进制

        :param metric: The metric of this ShowSpecialUserResponse.
        :type metric: int
        """
        self._metric = metric

    @property
    def flux_metric(self):
        r"""Gets the flux_metric of this ShowSpecialUserResponse.

        流量进制

        :return: The flux_metric of this ShowSpecialUserResponse.
        :rtype: int
        """
        return self._flux_metric

    @flux_metric.setter
    def flux_metric(self, flux_metric):
        r"""Sets the flux_metric of this ShowSpecialUserResponse.

        流量进制

        :param flux_metric: The flux_metric of this ShowSpecialUserResponse.
        :type flux_metric: int
        """
        self._flux_metric = flux_metric

    @property
    def cy(self):
        r"""Gets the cy of this ShowSpecialUserResponse.

        1表示用户可以，0表示用户不可以。是否是开放国家及地区界面用户

        :return: The cy of this ShowSpecialUserResponse.
        :rtype: int
        """
        return self._cy

    @cy.setter
    def cy(self, cy):
        r"""Sets the cy of this ShowSpecialUserResponse.

        1表示用户可以，0表示用户不可以。是否是开放国家及地区界面用户

        :param cy: The cy of this ShowSpecialUserResponse.
        :type cy: int
        """
        self._cy = cy

    @property
    def h6(self):
        r"""Gets the h6 of this ShowSpecialUserResponse.

        1表示用户可以查询ipv6流量,https流量，0表示用户不可以

        :return: The h6 of this ShowSpecialUserResponse.
        :rtype: int
        """
        return self._h6

    @h6.setter
    def h6(self, h6):
        r"""Sets the h6 of this ShowSpecialUserResponse.

        1表示用户可以查询ipv6流量,https流量，0表示用户不可以

        :param h6: The h6 of this ShowSpecialUserResponse.
        :type h6: int
        """
        self._h6 = h6

    @property
    def c(self):
        r"""Gets the c of this ShowSpecialUserResponse.

        1表示用户可以查询具体的状态码详情，0表示用户不可以

        :return: The c of this ShowSpecialUserResponse.
        :rtype: int
        """
        return self._c

    @c.setter
    def c(self, c):
        r"""Sets the c of this ShowSpecialUserResponse.

        1表示用户可以查询具体的状态码详情，0表示用户不可以

        :param c: The c of this ShowSpecialUserResponse.
        :type c: int
        """
        self._c = c

    @property
    def sc(self):
        r"""Gets the sc of this ShowSpecialUserResponse.

        1表示用户查询 top url 时要返回http状态码，0表示用户不返回

        :return: The sc of this ShowSpecialUserResponse.
        :rtype: int
        """
        return self._sc

    @sc.setter
    def sc(self, sc):
        r"""Sets the sc of this ShowSpecialUserResponse.

        1表示用户查询 top url 时要返回http状态码，0表示用户不返回

        :param sc: The sc of this ShowSpecialUserResponse.
        :type sc: int
        """
        self._sc = sc

    @property
    def bhc(self):
        r"""Gets the bhc of this ShowSpecialUserResponse.

        1表示该用户可以查询回源状态码，0表示不可以

        :return: The bhc of this ShowSpecialUserResponse.
        :rtype: int
        """
        return self._bhc

    @bhc.setter
    def bhc(self, bhc):
        r"""Sets the bhc of this ShowSpecialUserResponse.

        1表示该用户可以查询回源状态码，0表示不可以

        :param bhc: The bhc of this ShowSpecialUserResponse.
        :type bhc: int
        """
        self._bhc = bhc

    @property
    def pi(self):
        r"""Gets the pi of this ShowSpecialUserResponse.

        1表示该用户可以查询protocol和IPVersion，0表示用户不可以

        :return: The pi of this ShowSpecialUserResponse.
        :rtype: int
        """
        return self._pi

    @pi.setter
    def pi(self, pi):
        r"""Sets the pi of this ShowSpecialUserResponse.

        1表示该用户可以查询protocol和IPVersion，0表示用户不可以

        :param pi: The pi of this ShowSpecialUserResponse.
        :type pi: int
        """
        self._pi = pi

    @property
    def exp5(self):
        r"""Gets the exp5 of this ShowSpecialUserResponse.

        1表示该用户可以查询租户界面5分钟粒度数据导出白名单，0表示用户不可以

        :return: The exp5 of this ShowSpecialUserResponse.
        :rtype: int
        """
        return self._exp5

    @exp5.setter
    def exp5(self, exp5):
        r"""Sets the exp5 of this ShowSpecialUserResponse.

        1表示该用户可以查询租户界面5分钟粒度数据导出白名单，0表示用户不可以

        :param exp5: The exp5 of this ShowSpecialUserResponse.
        :type exp5: int
        """
        self._exp5 = exp5

    @property
    def m1(self):
        r"""Gets the m1 of this ShowSpecialUserResponse.

        1表示该用户可以查询1分钟粒度统计数据，0表示用户不可以

        :return: The m1 of this ShowSpecialUserResponse.
        :rtype: int
        """
        return self._m1

    @m1.setter
    def m1(self, m1):
        r"""Sets the m1 of this ShowSpecialUserResponse.

        1表示该用户可以查询1分钟粒度统计数据，0表示用户不可以

        :param m1: The m1 of this ShowSpecialUserResponse.
        :type m1: int
        """
        self._m1 = m1

    @property
    def is_month_m5(self):
        r"""Gets the is_month_m5 of this ShowSpecialUserResponse.

        1表示该用户可以查询1个月5分钟粒度统计数据，0表示用户不可以

        :return: The is_month_m5 of this ShowSpecialUserResponse.
        :rtype: int
        """
        return self._is_month_m5

    @is_month_m5.setter
    def is_month_m5(self, is_month_m5):
        r"""Sets the is_month_m5 of this ShowSpecialUserResponse.

        1表示该用户可以查询1个月5分钟粒度统计数据，0表示用户不可以

        :param is_month_m5: The is_month_m5 of this ShowSpecialUserResponse.
        :type is_month_m5: int
        """
        self._is_month_m5 = is_month_m5

    @property
    def exp_agy(self):
        r"""Gets the exp_agy of this ShowSpecialUserResponse.

        1表示该用户可以在租户界面指定下载链接可用范围，0表示用户不可以

        :return: The exp_agy of this ShowSpecialUserResponse.
        :rtype: int
        """
        return self._exp_agy

    @exp_agy.setter
    def exp_agy(self, exp_agy):
        r"""Sets the exp_agy of this ShowSpecialUserResponse.

        1表示该用户可以在租户界面指定下载链接可用范围，0表示用户不可以

        :param exp_agy: The exp_agy of this ShowSpecialUserResponse.
        :type exp_agy: int
        """
        self._exp_agy = exp_agy

    @property
    def ces_report_site(self):
        r"""Gets the ces_report_site of this ShowSpecialUserResponse.

        1表示该用户可以是否上报到国际站CES，0表示用户不可以

        :return: The ces_report_site of this ShowSpecialUserResponse.
        :rtype: int
        """
        return self._ces_report_site

    @ces_report_site.setter
    def ces_report_site(self, ces_report_site):
        r"""Sets the ces_report_site of this ShowSpecialUserResponse.

        1表示该用户可以是否上报到国际站CES，0表示用户不可以

        :param ces_report_site: The ces_report_site of this ShowSpecialUserResponse.
        :type ces_report_site: int
        """
        self._ces_report_site = ces_report_site

    @property
    def float(self):
        r"""Gets the float of this ShowSpecialUserResponse.

        1表示该用户按上浮系数展示数据，0表示用户不可以

        :return: The float of this ShowSpecialUserResponse.
        :rtype: int
        """
        return self._float

    @float.setter
    def float(self, float):
        r"""Sets the float of this ShowSpecialUserResponse.

        1表示该用户按上浮系数展示数据，0表示用户不可以

        :param float: The float of this ShowSpecialUserResponse.
        :type float: int
        """
        self._float = float

    @property
    def is_show_up_bw(self):
        r"""Gets the is_show_up_bw of this ShowSpecialUserResponse.

        1表示该用户允许查询入网带宽，0表示用户不可以

        :return: The is_show_up_bw of this ShowSpecialUserResponse.
        :rtype: int
        """
        return self._is_show_up_bw

    @is_show_up_bw.setter
    def is_show_up_bw(self, is_show_up_bw):
        r"""Sets the is_show_up_bw of this ShowSpecialUserResponse.

        1表示该用户允许查询入网带宽，0表示用户不可以

        :param is_show_up_bw: The is_show_up_bw of this ShowSpecialUserResponse.
        :type is_show_up_bw: int
        """
        self._is_show_up_bw = is_show_up_bw

    def to_dict(self):
        import warnings
        warnings.warn("ShowSpecialUserResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ShowSpecialUserResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
