# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GetCreateFirewallJobResponseData:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'status': 'str',
        'begin_time': 'date',
        'end_time': 'date'
    }

    attribute_map = {
        'id': 'id',
        'status': 'status',
        'begin_time': 'begin_time',
        'end_time': 'end_time'
    }

    def __init__(self, id=None, status=None, begin_time=None, end_time=None):
        r"""GetCreateFirewallJobResponseData

        The model defined in huaweicloud sdk

        :param id: **参数解释**： 创建按需防火墙任务ID **取值范围**： 不涉及
        :type id: str
        :param status: **参数解释**： 任务执行状态，用于展示创建防火墙是否成功。 **取值范围**： - Running：表示任务正在执行。 - Success：表示任务执行成功。 - Failed：表示任务执行失败。
        :type status: str
        :param begin_time: **参数解释**： 创建时间 **取值范围**： 格式为“yyyy-mm-ddThh:mm:ssZ”，其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。 例如： - 2023-10-26T10:30:00Z 表示： 2023年10月26日10点30分00秒，UTC时间 - 2023-10-26T10:30:00+0800 表示： 2023年10月26日10点30分00秒，比UTC时间快8小时，也就是北京时间。
        :type begin_time: date
        :param end_time: **参数解释**： 结束时间 **取值范围**： 格式为“yyyy-mm-ddThh:mm:ssZ”，其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。 例如： - 2023-10-26T10:30:00Z 表示： 2023年10月26日10点30分00秒，UTC时间 - 2023-10-26T10:30:00+0800 表示： 2023年10月26日10点30分00秒，比UTC时间快8小时，也就是北京时间。
        :type end_time: date
        """
        
        

        self._id = None
        self._status = None
        self._begin_time = None
        self._end_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if status is not None:
            self.status = status
        if begin_time is not None:
            self.begin_time = begin_time
        if end_time is not None:
            self.end_time = end_time

    @property
    def id(self):
        r"""Gets the id of this GetCreateFirewallJobResponseData.

        **参数解释**： 创建按需防火墙任务ID **取值范围**： 不涉及

        :return: The id of this GetCreateFirewallJobResponseData.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this GetCreateFirewallJobResponseData.

        **参数解释**： 创建按需防火墙任务ID **取值范围**： 不涉及

        :param id: The id of this GetCreateFirewallJobResponseData.
        :type id: str
        """
        self._id = id

    @property
    def status(self):
        r"""Gets the status of this GetCreateFirewallJobResponseData.

        **参数解释**： 任务执行状态，用于展示创建防火墙是否成功。 **取值范围**： - Running：表示任务正在执行。 - Success：表示任务执行成功。 - Failed：表示任务执行失败。

        :return: The status of this GetCreateFirewallJobResponseData.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this GetCreateFirewallJobResponseData.

        **参数解释**： 任务执行状态，用于展示创建防火墙是否成功。 **取值范围**： - Running：表示任务正在执行。 - Success：表示任务执行成功。 - Failed：表示任务执行失败。

        :param status: The status of this GetCreateFirewallJobResponseData.
        :type status: str
        """
        self._status = status

    @property
    def begin_time(self):
        r"""Gets the begin_time of this GetCreateFirewallJobResponseData.

        **参数解释**： 创建时间 **取值范围**： 格式为“yyyy-mm-ddThh:mm:ssZ”，其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。 例如： - 2023-10-26T10:30:00Z 表示： 2023年10月26日10点30分00秒，UTC时间 - 2023-10-26T10:30:00+0800 表示： 2023年10月26日10点30分00秒，比UTC时间快8小时，也就是北京时间。

        :return: The begin_time of this GetCreateFirewallJobResponseData.
        :rtype: date
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        r"""Sets the begin_time of this GetCreateFirewallJobResponseData.

        **参数解释**： 创建时间 **取值范围**： 格式为“yyyy-mm-ddThh:mm:ssZ”，其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。 例如： - 2023-10-26T10:30:00Z 表示： 2023年10月26日10点30分00秒，UTC时间 - 2023-10-26T10:30:00+0800 表示： 2023年10月26日10点30分00秒，比UTC时间快8小时，也就是北京时间。

        :param begin_time: The begin_time of this GetCreateFirewallJobResponseData.
        :type begin_time: date
        """
        self._begin_time = begin_time

    @property
    def end_time(self):
        r"""Gets the end_time of this GetCreateFirewallJobResponseData.

        **参数解释**： 结束时间 **取值范围**： 格式为“yyyy-mm-ddThh:mm:ssZ”，其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。 例如： - 2023-10-26T10:30:00Z 表示： 2023年10月26日10点30分00秒，UTC时间 - 2023-10-26T10:30:00+0800 表示： 2023年10月26日10点30分00秒，比UTC时间快8小时，也就是北京时间。

        :return: The end_time of this GetCreateFirewallJobResponseData.
        :rtype: date
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this GetCreateFirewallJobResponseData.

        **参数解释**： 结束时间 **取值范围**： 格式为“yyyy-mm-ddThh:mm:ssZ”，其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。 例如： - 2023-10-26T10:30:00Z 表示： 2023年10月26日10点30分00秒，UTC时间 - 2023-10-26T10:30:00+0800 表示： 2023年10月26日10点30分00秒，比UTC时间快8小时，也就是北京时间。

        :param end_time: The end_time of this GetCreateFirewallJobResponseData.
        :type end_time: date
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
        if not isinstance(other, GetCreateFirewallJobResponseData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
