# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateTuningResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'message_id': 'list[str]',
        'status': 'bool',
        'quota_exceeded': 'bool'
    }

    attribute_map = {
        'message_id': 'message_id',
        'status': 'status',
        'quota_exceeded': 'quota_exceeded'
    }

    def __init__(self, message_id=None, status=None, quota_exceeded=None):
        """CreateTuningResponse

        The model defined in huaweicloud sdk

        :param message_id: 诊断信息id
        :type message_id: list[str]
        :param status: 状态
        :type status: bool
        :param quota_exceeded: 诊断配额状态
        :type quota_exceeded: bool
        """
        
        super(CreateTuningResponse, self).__init__()

        self._message_id = None
        self._status = None
        self._quota_exceeded = None
        self.discriminator = None

        if message_id is not None:
            self.message_id = message_id
        if status is not None:
            self.status = status
        if quota_exceeded is not None:
            self.quota_exceeded = quota_exceeded

    @property
    def message_id(self):
        """Gets the message_id of this CreateTuningResponse.

        诊断信息id

        :return: The message_id of this CreateTuningResponse.
        :rtype: list[str]
        """
        return self._message_id

    @message_id.setter
    def message_id(self, message_id):
        """Sets the message_id of this CreateTuningResponse.

        诊断信息id

        :param message_id: The message_id of this CreateTuningResponse.
        :type message_id: list[str]
        """
        self._message_id = message_id

    @property
    def status(self):
        """Gets the status of this CreateTuningResponse.

        状态

        :return: The status of this CreateTuningResponse.
        :rtype: bool
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CreateTuningResponse.

        状态

        :param status: The status of this CreateTuningResponse.
        :type status: bool
        """
        self._status = status

    @property
    def quota_exceeded(self):
        """Gets the quota_exceeded of this CreateTuningResponse.

        诊断配额状态

        :return: The quota_exceeded of this CreateTuningResponse.
        :rtype: bool
        """
        return self._quota_exceeded

    @quota_exceeded.setter
    def quota_exceeded(self, quota_exceeded):
        """Sets the quota_exceeded of this CreateTuningResponse.

        诊断配额状态

        :param quota_exceeded: The quota_exceeded of this CreateTuningResponse.
        :type quota_exceeded: bool
        """
        self._quota_exceeded = quota_exceeded

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
        if not isinstance(other, CreateTuningResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
