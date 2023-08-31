# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DownUpTimeForSimCardReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'down_up_switch': 'int',
        'iccid': 'str'
    }

    attribute_map = {
        'down_up_switch': 'down_up_switch',
        'iccid': 'iccid'
    }

    def __init__(self, down_up_switch=None, iccid=None):
        """DownUpTimeForSimCardReq

        The model defined in huaweicloud sdk

        :param down_up_switch: 启用停用开关
        :type down_up_switch: int
        :param iccid: iccid，传入的sim_card_id为0,则根据iccid进行处理
        :type iccid: str
        """
        
        

        self._down_up_switch = None
        self._iccid = None
        self.discriminator = None

        if down_up_switch is not None:
            self.down_up_switch = down_up_switch
        if iccid is not None:
            self.iccid = iccid

    @property
    def down_up_switch(self):
        """Gets the down_up_switch of this DownUpTimeForSimCardReq.

        启用停用开关

        :return: The down_up_switch of this DownUpTimeForSimCardReq.
        :rtype: int
        """
        return self._down_up_switch

    @down_up_switch.setter
    def down_up_switch(self, down_up_switch):
        """Sets the down_up_switch of this DownUpTimeForSimCardReq.

        启用停用开关

        :param down_up_switch: The down_up_switch of this DownUpTimeForSimCardReq.
        :type down_up_switch: int
        """
        self._down_up_switch = down_up_switch

    @property
    def iccid(self):
        """Gets the iccid of this DownUpTimeForSimCardReq.

        iccid，传入的sim_card_id为0,则根据iccid进行处理

        :return: The iccid of this DownUpTimeForSimCardReq.
        :rtype: str
        """
        return self._iccid

    @iccid.setter
    def iccid(self, iccid):
        """Sets the iccid of this DownUpTimeForSimCardReq.

        iccid，传入的sim_card_id为0,则根据iccid进行处理

        :param iccid: The iccid of this DownUpTimeForSimCardReq.
        :type iccid: str
        """
        self._iccid = iccid

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
        if not isinstance(other, DownUpTimeForSimCardReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
