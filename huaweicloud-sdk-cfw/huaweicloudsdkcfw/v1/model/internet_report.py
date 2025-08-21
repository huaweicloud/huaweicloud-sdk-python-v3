# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InternetReport:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'eip': 'Eip',
        'in2out': 'In2Out',
        'out2in': 'Out2in',
        'overview': 'Overview',
        'traffic_trend': 'list[TrendVO]'
    }

    attribute_map = {
        'eip': 'eip',
        'in2out': 'in2out',
        'out2in': 'out2in',
        'overview': 'overview',
        'traffic_trend': 'traffic_trend'
    }

    def __init__(self, eip=None, in2out=None, out2in=None, overview=None, traffic_trend=None):
        r"""InternetReport

        The model defined in huaweicloud sdk

        :param eip: 
        :type eip: :class:`huaweicloudsdkcfw.v1.Eip`
        :param in2out: 
        :type in2out: :class:`huaweicloudsdkcfw.v1.In2Out`
        :param out2in: 
        :type out2in: :class:`huaweicloudsdkcfw.v1.Out2in`
        :param overview: 
        :type overview: :class:`huaweicloudsdkcfw.v1.Overview`
        :param traffic_trend: **参数解释**： 流量趋势 **取值范围**： 不涉及
        :type traffic_trend: list[:class:`huaweicloudsdkcfw.v1.TrendVO`]
        """
        
        

        self._eip = None
        self._in2out = None
        self._out2in = None
        self._overview = None
        self._traffic_trend = None
        self.discriminator = None

        if eip is not None:
            self.eip = eip
        if in2out is not None:
            self.in2out = in2out
        if out2in is not None:
            self.out2in = out2in
        if overview is not None:
            self.overview = overview
        if traffic_trend is not None:
            self.traffic_trend = traffic_trend

    @property
    def eip(self):
        r"""Gets the eip of this InternetReport.

        :return: The eip of this InternetReport.
        :rtype: :class:`huaweicloudsdkcfw.v1.Eip`
        """
        return self._eip

    @eip.setter
    def eip(self, eip):
        r"""Sets the eip of this InternetReport.

        :param eip: The eip of this InternetReport.
        :type eip: :class:`huaweicloudsdkcfw.v1.Eip`
        """
        self._eip = eip

    @property
    def in2out(self):
        r"""Gets the in2out of this InternetReport.

        :return: The in2out of this InternetReport.
        :rtype: :class:`huaweicloudsdkcfw.v1.In2Out`
        """
        return self._in2out

    @in2out.setter
    def in2out(self, in2out):
        r"""Sets the in2out of this InternetReport.

        :param in2out: The in2out of this InternetReport.
        :type in2out: :class:`huaweicloudsdkcfw.v1.In2Out`
        """
        self._in2out = in2out

    @property
    def out2in(self):
        r"""Gets the out2in of this InternetReport.

        :return: The out2in of this InternetReport.
        :rtype: :class:`huaweicloudsdkcfw.v1.Out2in`
        """
        return self._out2in

    @out2in.setter
    def out2in(self, out2in):
        r"""Sets the out2in of this InternetReport.

        :param out2in: The out2in of this InternetReport.
        :type out2in: :class:`huaweicloudsdkcfw.v1.Out2in`
        """
        self._out2in = out2in

    @property
    def overview(self):
        r"""Gets the overview of this InternetReport.

        :return: The overview of this InternetReport.
        :rtype: :class:`huaweicloudsdkcfw.v1.Overview`
        """
        return self._overview

    @overview.setter
    def overview(self, overview):
        r"""Sets the overview of this InternetReport.

        :param overview: The overview of this InternetReport.
        :type overview: :class:`huaweicloudsdkcfw.v1.Overview`
        """
        self._overview = overview

    @property
    def traffic_trend(self):
        r"""Gets the traffic_trend of this InternetReport.

        **参数解释**： 流量趋势 **取值范围**： 不涉及

        :return: The traffic_trend of this InternetReport.
        :rtype: list[:class:`huaweicloudsdkcfw.v1.TrendVO`]
        """
        return self._traffic_trend

    @traffic_trend.setter
    def traffic_trend(self, traffic_trend):
        r"""Sets the traffic_trend of this InternetReport.

        **参数解释**： 流量趋势 **取值范围**： 不涉及

        :param traffic_trend: The traffic_trend of this InternetReport.
        :type traffic_trend: list[:class:`huaweicloudsdkcfw.v1.TrendVO`]
        """
        self._traffic_trend = traffic_trend

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
        if not isinstance(other, InternetReport):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
