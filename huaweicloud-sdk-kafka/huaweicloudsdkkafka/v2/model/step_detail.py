# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StepDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'status': 'str',
        'start_time': 'str',
        'end_time': 'str'
    }

    attribute_map = {
        'name': 'name',
        'status': 'status',
        'start_time': 'start_time',
        'end_time': 'end_time'
    }

    def __init__(self, name=None, status=None, start_time=None, end_time=None):
        r"""StepDetail

        The model defined in huaweicloud sdk

        :param name: **参数解释**： 任务名称。  **取值范围**： 不涉及。
        :type name: str
        :param status: **参数解释**： 任务状态。 **取值范围**： - COMPLETED：任务已完成。 - IN_PROGRESS：任务正在进行。 - FAILED：任务失败。 - WAITING：等待开始。
        :type status: str
        :param start_time: **参数解释**： 开始时间。     **取值范围**： 不涉及。
        :type start_time: str
        :param end_time: **参数解释**： 结束时间。 **取值范围**： 不涉及。
        :type end_time: str
        """
        
        

        self._name = None
        self._status = None
        self._start_time = None
        self._end_time = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if status is not None:
            self.status = status
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time

    @property
    def name(self):
        r"""Gets the name of this StepDetail.

        **参数解释**： 任务名称。  **取值范围**： 不涉及。

        :return: The name of this StepDetail.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this StepDetail.

        **参数解释**： 任务名称。  **取值范围**： 不涉及。

        :param name: The name of this StepDetail.
        :type name: str
        """
        self._name = name

    @property
    def status(self):
        r"""Gets the status of this StepDetail.

        **参数解释**： 任务状态。 **取值范围**： - COMPLETED：任务已完成。 - IN_PROGRESS：任务正在进行。 - FAILED：任务失败。 - WAITING：等待开始。

        :return: The status of this StepDetail.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this StepDetail.

        **参数解释**： 任务状态。 **取值范围**： - COMPLETED：任务已完成。 - IN_PROGRESS：任务正在进行。 - FAILED：任务失败。 - WAITING：等待开始。

        :param status: The status of this StepDetail.
        :type status: str
        """
        self._status = status

    @property
    def start_time(self):
        r"""Gets the start_time of this StepDetail.

        **参数解释**： 开始时间。     **取值范围**： 不涉及。

        :return: The start_time of this StepDetail.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this StepDetail.

        **参数解释**： 开始时间。     **取值范围**： 不涉及。

        :param start_time: The start_time of this StepDetail.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this StepDetail.

        **参数解释**： 结束时间。 **取值范围**： 不涉及。

        :return: The end_time of this StepDetail.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this StepDetail.

        **参数解释**： 结束时间。 **取值范围**： 不涉及。

        :param end_time: The end_time of this StepDetail.
        :type end_time: str
        """
        self._end_time = end_time

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
        if not isinstance(other, StepDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
