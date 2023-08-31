# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CutNetReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'action': 'str',
        'iccid': 'str'
    }

    attribute_map = {
        'action': 'action',
        'iccid': 'iccid'
    }

    def __init__(self, action=None, iccid=None):
        """CutNetReq

        The model defined in huaweicloud sdk

        :param action: 操作类型(ADD：断网，DEL:取消断网)
        :type action: str
        :param iccid: iccid，传入的sim_card_id为0,则根据iccid进行处理
        :type iccid: str
        """
        
        

        self._action = None
        self._iccid = None
        self.discriminator = None

        self.action = action
        if iccid is not None:
            self.iccid = iccid

    @property
    def action(self):
        """Gets the action of this CutNetReq.

        操作类型(ADD：断网，DEL:取消断网)

        :return: The action of this CutNetReq.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this CutNetReq.

        操作类型(ADD：断网，DEL:取消断网)

        :param action: The action of this CutNetReq.
        :type action: str
        """
        self._action = action

    @property
    def iccid(self):
        """Gets the iccid of this CutNetReq.

        iccid，传入的sim_card_id为0,则根据iccid进行处理

        :return: The iccid of this CutNetReq.
        :rtype: str
        """
        return self._iccid

    @iccid.setter
    def iccid(self, iccid):
        """Sets the iccid of this CutNetReq.

        iccid，传入的sim_card_id为0,则根据iccid进行处理

        :param iccid: The iccid of this CutNetReq.
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
        if not isinstance(other, CutNetReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
