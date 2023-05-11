# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RestBatchHandsUpReqBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'hands_state': 'int',
        'pids': 'list[str]'
    }

    attribute_map = {
        'hands_state': 'handsState',
        'pids': 'pids'
    }

    def __init__(self, hands_state=None, pids=None):
        """RestBatchHandsUpReqBody

        The model defined in huaweicloud sdk

        :param hands_state: - 0: 放下手 - 1: 举手
        :type hands_state: int
        :param pids: 与会者标识列表。
        :type pids: list[str]
        """
        
        

        self._hands_state = None
        self._pids = None
        self.discriminator = None

        self.hands_state = hands_state
        self.pids = pids

    @property
    def hands_state(self):
        """Gets the hands_state of this RestBatchHandsUpReqBody.

        - 0: 放下手 - 1: 举手

        :return: The hands_state of this RestBatchHandsUpReqBody.
        :rtype: int
        """
        return self._hands_state

    @hands_state.setter
    def hands_state(self, hands_state):
        """Sets the hands_state of this RestBatchHandsUpReqBody.

        - 0: 放下手 - 1: 举手

        :param hands_state: The hands_state of this RestBatchHandsUpReqBody.
        :type hands_state: int
        """
        self._hands_state = hands_state

    @property
    def pids(self):
        """Gets the pids of this RestBatchHandsUpReqBody.

        与会者标识列表。

        :return: The pids of this RestBatchHandsUpReqBody.
        :rtype: list[str]
        """
        return self._pids

    @pids.setter
    def pids(self, pids):
        """Sets the pids of this RestBatchHandsUpReqBody.

        与会者标识列表。

        :param pids: The pids of this RestBatchHandsUpReqBody.
        :type pids: list[str]
        """
        self._pids = pids

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
        if not isinstance(other, RestBatchHandsUpReqBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
