# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ModifyJobScheduleRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'schedule_id': 'str',
        'body': 'ModifyJobScheduleRequestBody'
    }

    attribute_map = {
        'schedule_id': 'schedule_id',
        'body': 'body'
    }

    def __init__(self, schedule_id=None, body=None):
        r"""ModifyJobScheduleRequest

        The model defined in huaweicloud sdk

        :param schedule_id: 策略ID
        :type schedule_id: str
        :param body: Body of the ModifyJobScheduleRequest
        :type body: :class:`huaweicloudsdkrds.v3.ModifyJobScheduleRequestBody`
        """
        
        

        self._schedule_id = None
        self._body = None
        self.discriminator = None

        self.schedule_id = schedule_id
        if body is not None:
            self.body = body

    @property
    def schedule_id(self):
        r"""Gets the schedule_id of this ModifyJobScheduleRequest.

        策略ID

        :return: The schedule_id of this ModifyJobScheduleRequest.
        :rtype: str
        """
        return self._schedule_id

    @schedule_id.setter
    def schedule_id(self, schedule_id):
        r"""Sets the schedule_id of this ModifyJobScheduleRequest.

        策略ID

        :param schedule_id: The schedule_id of this ModifyJobScheduleRequest.
        :type schedule_id: str
        """
        self._schedule_id = schedule_id

    @property
    def body(self):
        r"""Gets the body of this ModifyJobScheduleRequest.

        :return: The body of this ModifyJobScheduleRequest.
        :rtype: :class:`huaweicloudsdkrds.v3.ModifyJobScheduleRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this ModifyJobScheduleRequest.

        :param body: The body of this ModifyJobScheduleRequest.
        :type body: :class:`huaweicloudsdkrds.v3.ModifyJobScheduleRequestBody`
        """
        self._body = body

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ModifyJobScheduleRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
