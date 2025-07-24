# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RestBatchMoveToWaitingRoomReqBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'batch_participants': 'list[str]'
    }

    attribute_map = {
        'batch_participants': 'batchParticipants'
    }

    def __init__(self, batch_participants=None):
        r"""RestBatchMoveToWaitingRoomReqBody

        The model defined in huaweicloud sdk

        :param batch_participants: 需要移入等候室的全部与会者pid
        :type batch_participants: list[str]
        """
        
        

        self._batch_participants = None
        self.discriminator = None

        self.batch_participants = batch_participants

    @property
    def batch_participants(self):
        r"""Gets the batch_participants of this RestBatchMoveToWaitingRoomReqBody.

        需要移入等候室的全部与会者pid

        :return: The batch_participants of this RestBatchMoveToWaitingRoomReqBody.
        :rtype: list[str]
        """
        return self._batch_participants

    @batch_participants.setter
    def batch_participants(self, batch_participants):
        r"""Sets the batch_participants of this RestBatchMoveToWaitingRoomReqBody.

        需要移入等候室的全部与会者pid

        :param batch_participants: The batch_participants of this RestBatchMoveToWaitingRoomReqBody.
        :type batch_participants: list[str]
        """
        self._batch_participants = batch_participants

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
        if not isinstance(other, RestBatchMoveToWaitingRoomReqBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
