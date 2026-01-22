# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateScheduleRequest:

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
        'body': 'ScheduleInfoDTO'
    }

    attribute_map = {
        'schedule_id': 'schedule_id',
        'body': 'body'
    }

    def __init__(self, schedule_id=None, body=None):
        r"""UpdateScheduleRequest

        The model defined in huaweicloud sdk

        :param schedule_id: **参数解释**： 时间表ID，可以通过调用[查询时间表列表接口]获得，通过返回值中的data.records.schedule_id获得 **约束限制**： 不涉及 **取值范围**： 32位UUID **默认取值**： 不涉及
        :type schedule_id: str
        :param body: Body of the UpdateScheduleRequest
        :type body: :class:`huaweicloudsdkcfw.v1.ScheduleInfoDTO`
        """
        
        

        self._schedule_id = None
        self._body = None
        self.discriminator = None

        self.schedule_id = schedule_id
        if body is not None:
            self.body = body

    @property
    def schedule_id(self):
        r"""Gets the schedule_id of this UpdateScheduleRequest.

        **参数解释**： 时间表ID，可以通过调用[查询时间表列表接口]获得，通过返回值中的data.records.schedule_id获得 **约束限制**： 不涉及 **取值范围**： 32位UUID **默认取值**： 不涉及

        :return: The schedule_id of this UpdateScheduleRequest.
        :rtype: str
        """
        return self._schedule_id

    @schedule_id.setter
    def schedule_id(self, schedule_id):
        r"""Sets the schedule_id of this UpdateScheduleRequest.

        **参数解释**： 时间表ID，可以通过调用[查询时间表列表接口]获得，通过返回值中的data.records.schedule_id获得 **约束限制**： 不涉及 **取值范围**： 32位UUID **默认取值**： 不涉及

        :param schedule_id: The schedule_id of this UpdateScheduleRequest.
        :type schedule_id: str
        """
        self._schedule_id = schedule_id

    @property
    def body(self):
        r"""Gets the body of this UpdateScheduleRequest.

        :return: The body of this UpdateScheduleRequest.
        :rtype: :class:`huaweicloudsdkcfw.v1.ScheduleInfoDTO`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this UpdateScheduleRequest.

        :param body: The body of this UpdateScheduleRequest.
        :type body: :class:`huaweicloudsdkcfw.v1.ScheduleInfoDTO`
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
        if not isinstance(other, UpdateScheduleRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
