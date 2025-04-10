# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SimCardFlowPerDayReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'sim_card_ids': 'list[int]',
        'iccids': 'list[str]',
        'month': 'str',
        'date': 'str'
    }

    attribute_map = {
        'sim_card_ids': 'sim_card_ids',
        'iccids': 'iccids',
        'month': 'month',
        'date': 'date'
    }

    def __init__(self, sim_card_ids=None, iccids=None, month=None, date=None):
        r"""SimCardFlowPerDayReq

        The model defined in huaweicloud sdk

        :param sim_card_ids: 
        :type sim_card_ids: list[int]
        :param iccids: 
        :type iccids: list[str]
        :param month: 月份
        :type month: str
        :param date: 日期
        :type date: str
        """
        
        

        self._sim_card_ids = None
        self._iccids = None
        self._month = None
        self._date = None
        self.discriminator = None

        if sim_card_ids is not None:
            self.sim_card_ids = sim_card_ids
        if iccids is not None:
            self.iccids = iccids
        if month is not None:
            self.month = month
        if date is not None:
            self.date = date

    @property
    def sim_card_ids(self):
        r"""Gets the sim_card_ids of this SimCardFlowPerDayReq.

        :return: The sim_card_ids of this SimCardFlowPerDayReq.
        :rtype: list[int]
        """
        return self._sim_card_ids

    @sim_card_ids.setter
    def sim_card_ids(self, sim_card_ids):
        r"""Sets the sim_card_ids of this SimCardFlowPerDayReq.

        :param sim_card_ids: The sim_card_ids of this SimCardFlowPerDayReq.
        :type sim_card_ids: list[int]
        """
        self._sim_card_ids = sim_card_ids

    @property
    def iccids(self):
        r"""Gets the iccids of this SimCardFlowPerDayReq.

        :return: The iccids of this SimCardFlowPerDayReq.
        :rtype: list[str]
        """
        return self._iccids

    @iccids.setter
    def iccids(self, iccids):
        r"""Sets the iccids of this SimCardFlowPerDayReq.

        :param iccids: The iccids of this SimCardFlowPerDayReq.
        :type iccids: list[str]
        """
        self._iccids = iccids

    @property
    def month(self):
        r"""Gets the month of this SimCardFlowPerDayReq.

        月份

        :return: The month of this SimCardFlowPerDayReq.
        :rtype: str
        """
        return self._month

    @month.setter
    def month(self, month):
        r"""Sets the month of this SimCardFlowPerDayReq.

        月份

        :param month: The month of this SimCardFlowPerDayReq.
        :type month: str
        """
        self._month = month

    @property
    def date(self):
        r"""Gets the date of this SimCardFlowPerDayReq.

        日期

        :return: The date of this SimCardFlowPerDayReq.
        :rtype: str
        """
        return self._date

    @date.setter
    def date(self, date):
        r"""Sets the date of this SimCardFlowPerDayReq.

        日期

        :param date: The date of this SimCardFlowPerDayReq.
        :type date: str
        """
        self._date = date

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
        if not isinstance(other, SimCardFlowPerDayReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
