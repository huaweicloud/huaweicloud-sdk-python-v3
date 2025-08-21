# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VpcReport:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'app': 'list[ItemVO]',
        'dst_ip': 'list[ItemVO]',
        'overview': 'Overview',
        'src_ip': 'list[ItemVO]',
        'traffic_trend': 'list[TrendVO]',
        'vpc': 'Vpc'
    }

    attribute_map = {
        'app': 'app',
        'dst_ip': 'dst_ip',
        'overview': 'overview',
        'src_ip': 'src_ip',
        'traffic_trend': 'traffic_trend',
        'vpc': 'vpc'
    }

    def __init__(self, app=None, dst_ip=None, overview=None, src_ip=None, traffic_trend=None, vpc=None):
        r"""VpcReport

        The model defined in huaweicloud sdk

        :param app: **参数解释**： TOP应用数量 **取值范围**： 不涉及
        :type app: list[:class:`huaweicloudsdkcfw.v1.ItemVO`]
        :param dst_ip: **参数解释**： TOP访问目的IP **取值范围**： 不涉及
        :type dst_ip: list[:class:`huaweicloudsdkcfw.v1.ItemVO`]
        :param overview: 
        :type overview: :class:`huaweicloudsdkcfw.v1.Overview`
        :param src_ip: **参数解释**： TOP访问源IP **取值范围**： 不涉及
        :type src_ip: list[:class:`huaweicloudsdkcfw.v1.ItemVO`]
        :param traffic_trend: **参数解释**： 流量趋势 **取值范围**： 不涉及
        :type traffic_trend: list[:class:`huaweicloudsdkcfw.v1.TrendVO`]
        :param vpc: 
        :type vpc: :class:`huaweicloudsdkcfw.v1.Vpc`
        """
        
        

        self._app = None
        self._dst_ip = None
        self._overview = None
        self._src_ip = None
        self._traffic_trend = None
        self._vpc = None
        self.discriminator = None

        if app is not None:
            self.app = app
        if dst_ip is not None:
            self.dst_ip = dst_ip
        if overview is not None:
            self.overview = overview
        if src_ip is not None:
            self.src_ip = src_ip
        if traffic_trend is not None:
            self.traffic_trend = traffic_trend
        if vpc is not None:
            self.vpc = vpc

    @property
    def app(self):
        r"""Gets the app of this VpcReport.

        **参数解释**： TOP应用数量 **取值范围**： 不涉及

        :return: The app of this VpcReport.
        :rtype: list[:class:`huaweicloudsdkcfw.v1.ItemVO`]
        """
        return self._app

    @app.setter
    def app(self, app):
        r"""Sets the app of this VpcReport.

        **参数解释**： TOP应用数量 **取值范围**： 不涉及

        :param app: The app of this VpcReport.
        :type app: list[:class:`huaweicloudsdkcfw.v1.ItemVO`]
        """
        self._app = app

    @property
    def dst_ip(self):
        r"""Gets the dst_ip of this VpcReport.

        **参数解释**： TOP访问目的IP **取值范围**： 不涉及

        :return: The dst_ip of this VpcReport.
        :rtype: list[:class:`huaweicloudsdkcfw.v1.ItemVO`]
        """
        return self._dst_ip

    @dst_ip.setter
    def dst_ip(self, dst_ip):
        r"""Sets the dst_ip of this VpcReport.

        **参数解释**： TOP访问目的IP **取值范围**： 不涉及

        :param dst_ip: The dst_ip of this VpcReport.
        :type dst_ip: list[:class:`huaweicloudsdkcfw.v1.ItemVO`]
        """
        self._dst_ip = dst_ip

    @property
    def overview(self):
        r"""Gets the overview of this VpcReport.

        :return: The overview of this VpcReport.
        :rtype: :class:`huaweicloudsdkcfw.v1.Overview`
        """
        return self._overview

    @overview.setter
    def overview(self, overview):
        r"""Sets the overview of this VpcReport.

        :param overview: The overview of this VpcReport.
        :type overview: :class:`huaweicloudsdkcfw.v1.Overview`
        """
        self._overview = overview

    @property
    def src_ip(self):
        r"""Gets the src_ip of this VpcReport.

        **参数解释**： TOP访问源IP **取值范围**： 不涉及

        :return: The src_ip of this VpcReport.
        :rtype: list[:class:`huaweicloudsdkcfw.v1.ItemVO`]
        """
        return self._src_ip

    @src_ip.setter
    def src_ip(self, src_ip):
        r"""Sets the src_ip of this VpcReport.

        **参数解释**： TOP访问源IP **取值范围**： 不涉及

        :param src_ip: The src_ip of this VpcReport.
        :type src_ip: list[:class:`huaweicloudsdkcfw.v1.ItemVO`]
        """
        self._src_ip = src_ip

    @property
    def traffic_trend(self):
        r"""Gets the traffic_trend of this VpcReport.

        **参数解释**： 流量趋势 **取值范围**： 不涉及

        :return: The traffic_trend of this VpcReport.
        :rtype: list[:class:`huaweicloudsdkcfw.v1.TrendVO`]
        """
        return self._traffic_trend

    @traffic_trend.setter
    def traffic_trend(self, traffic_trend):
        r"""Sets the traffic_trend of this VpcReport.

        **参数解释**： 流量趋势 **取值范围**： 不涉及

        :param traffic_trend: The traffic_trend of this VpcReport.
        :type traffic_trend: list[:class:`huaweicloudsdkcfw.v1.TrendVO`]
        """
        self._traffic_trend = traffic_trend

    @property
    def vpc(self):
        r"""Gets the vpc of this VpcReport.

        :return: The vpc of this VpcReport.
        :rtype: :class:`huaweicloudsdkcfw.v1.Vpc`
        """
        return self._vpc

    @vpc.setter
    def vpc(self, vpc):
        r"""Sets the vpc of this VpcReport.

        :param vpc: The vpc of this VpcReport.
        :type vpc: :class:`huaweicloudsdkcfw.v1.Vpc`
        """
        self._vpc = vpc

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
        if not isinstance(other, VpcReport):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
