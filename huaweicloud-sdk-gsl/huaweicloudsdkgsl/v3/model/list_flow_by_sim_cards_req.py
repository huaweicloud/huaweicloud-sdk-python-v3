# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListFlowBySimCardsReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'iccids': 'list[str]',
        'sim_card_ids': 'list[int]'
    }

    attribute_map = {
        'iccids': 'iccids',
        'sim_card_ids': 'sim_card_ids'
    }

    def __init__(self, iccids=None, sim_card_ids=None):
        r"""ListFlowBySimCardsReq

        The model defined in huaweicloud sdk

        :param iccids: iccid列表（三网卡不支持），最大支持50，且iccid和sim_card_id列表二选一
        :type iccids: list[str]
        :param sim_card_ids: sim_card_id列表，最大支持50，且iccid和sim_card_id列表二选一
        :type sim_card_ids: list[int]
        """
        
        

        self._iccids = None
        self._sim_card_ids = None
        self.discriminator = None

        if iccids is not None:
            self.iccids = iccids
        if sim_card_ids is not None:
            self.sim_card_ids = sim_card_ids

    @property
    def iccids(self):
        r"""Gets the iccids of this ListFlowBySimCardsReq.

        iccid列表（三网卡不支持），最大支持50，且iccid和sim_card_id列表二选一

        :return: The iccids of this ListFlowBySimCardsReq.
        :rtype: list[str]
        """
        return self._iccids

    @iccids.setter
    def iccids(self, iccids):
        r"""Sets the iccids of this ListFlowBySimCardsReq.

        iccid列表（三网卡不支持），最大支持50，且iccid和sim_card_id列表二选一

        :param iccids: The iccids of this ListFlowBySimCardsReq.
        :type iccids: list[str]
        """
        self._iccids = iccids

    @property
    def sim_card_ids(self):
        r"""Gets the sim_card_ids of this ListFlowBySimCardsReq.

        sim_card_id列表，最大支持50，且iccid和sim_card_id列表二选一

        :return: The sim_card_ids of this ListFlowBySimCardsReq.
        :rtype: list[int]
        """
        return self._sim_card_ids

    @sim_card_ids.setter
    def sim_card_ids(self, sim_card_ids):
        r"""Sets the sim_card_ids of this ListFlowBySimCardsReq.

        sim_card_id列表，最大支持50，且iccid和sim_card_id列表二选一

        :param sim_card_ids: The sim_card_ids of this ListFlowBySimCardsReq.
        :type sim_card_ids: list[int]
        """
        self._sim_card_ids = sim_card_ids

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
        if not isinstance(other, ListFlowBySimCardsReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
