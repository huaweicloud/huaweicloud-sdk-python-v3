# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MonthUsageVo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'sim_card_id': 'int',
        'iccid': 'str',
        'flow_usages': 'list[FlowUsageVo]'
    }

    attribute_map = {
        'sim_card_id': 'sim_card_id',
        'iccid': 'iccid',
        'flow_usages': 'flow_usages'
    }

    def __init__(self, sim_card_id=None, iccid=None, flow_usages=None):
        """MonthUsageVo

        The model defined in huaweicloud sdk

        :param sim_card_id: SIM卡ID
        :type sim_card_id: int
        :param iccid: iccid
        :type iccid: str
        :param flow_usages: 月用量
        :type flow_usages: list[:class:`huaweicloudsdkgsl.v3.FlowUsageVo`]
        """
        
        

        self._sim_card_id = None
        self._iccid = None
        self._flow_usages = None
        self.discriminator = None

        if sim_card_id is not None:
            self.sim_card_id = sim_card_id
        if iccid is not None:
            self.iccid = iccid
        if flow_usages is not None:
            self.flow_usages = flow_usages

    @property
    def sim_card_id(self):
        """Gets the sim_card_id of this MonthUsageVo.

        SIM卡ID

        :return: The sim_card_id of this MonthUsageVo.
        :rtype: int
        """
        return self._sim_card_id

    @sim_card_id.setter
    def sim_card_id(self, sim_card_id):
        """Sets the sim_card_id of this MonthUsageVo.

        SIM卡ID

        :param sim_card_id: The sim_card_id of this MonthUsageVo.
        :type sim_card_id: int
        """
        self._sim_card_id = sim_card_id

    @property
    def iccid(self):
        """Gets the iccid of this MonthUsageVo.

        iccid

        :return: The iccid of this MonthUsageVo.
        :rtype: str
        """
        return self._iccid

    @iccid.setter
    def iccid(self, iccid):
        """Sets the iccid of this MonthUsageVo.

        iccid

        :param iccid: The iccid of this MonthUsageVo.
        :type iccid: str
        """
        self._iccid = iccid

    @property
    def flow_usages(self):
        """Gets the flow_usages of this MonthUsageVo.

        月用量

        :return: The flow_usages of this MonthUsageVo.
        :rtype: list[:class:`huaweicloudsdkgsl.v3.FlowUsageVo`]
        """
        return self._flow_usages

    @flow_usages.setter
    def flow_usages(self, flow_usages):
        """Sets the flow_usages of this MonthUsageVo.

        月用量

        :param flow_usages: The flow_usages of this MonthUsageVo.
        :type flow_usages: list[:class:`huaweicloudsdkgsl.v3.FlowUsageVo`]
        """
        self._flow_usages = flow_usages

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
        if not isinstance(other, MonthUsageVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
