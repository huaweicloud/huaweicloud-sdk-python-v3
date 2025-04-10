# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SimCardFlowPerDayRsp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'date': 'str',
        'sim_flow': 'list[SimCardFlowItem]'
    }

    attribute_map = {
        'date': 'date',
        'sim_flow': 'sim_flow'
    }

    def __init__(self, date=None, sim_flow=None):
        r"""SimCardFlowPerDayRsp

        The model defined in huaweicloud sdk

        :param date: 日期
        :type date: str
        :param sim_flow: 
        :type sim_flow: list[:class:`huaweicloudsdkgsl.v3.SimCardFlowItem`]
        """
        
        

        self._date = None
        self._sim_flow = None
        self.discriminator = None

        if date is not None:
            self.date = date
        if sim_flow is not None:
            self.sim_flow = sim_flow

    @property
    def date(self):
        r"""Gets the date of this SimCardFlowPerDayRsp.

        日期

        :return: The date of this SimCardFlowPerDayRsp.
        :rtype: str
        """
        return self._date

    @date.setter
    def date(self, date):
        r"""Sets the date of this SimCardFlowPerDayRsp.

        日期

        :param date: The date of this SimCardFlowPerDayRsp.
        :type date: str
        """
        self._date = date

    @property
    def sim_flow(self):
        r"""Gets the sim_flow of this SimCardFlowPerDayRsp.

        :return: The sim_flow of this SimCardFlowPerDayRsp.
        :rtype: list[:class:`huaweicloudsdkgsl.v3.SimCardFlowItem`]
        """
        return self._sim_flow

    @sim_flow.setter
    def sim_flow(self, sim_flow):
        r"""Sets the sim_flow of this SimCardFlowPerDayRsp.

        :param sim_flow: The sim_flow of this SimCardFlowPerDayRsp.
        :type sim_flow: list[:class:`huaweicloudsdkgsl.v3.SimCardFlowItem`]
        """
        self._sim_flow = sim_flow

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
        if not isinstance(other, SimCardFlowPerDayRsp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
