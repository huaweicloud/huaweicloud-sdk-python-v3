# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateAgentStatusResponseDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'int',
        'status': 'str',
        'update_time': 'int',
        'result': 'AgentConfig'
    }

    attribute_map = {
        'id': 'id',
        'status': 'status',
        'update_time': 'update_time',
        'result': 'result'
    }

    def __init__(self, id=None, status=None, update_time=None, result=None):
        r"""UpdateAgentStatusResponseDetail

        The model defined in huaweicloud sdk

        :param id: 全链路应用id
        :type id: int
        :param status: 全链路应用状态，枚举值：CREATING，FAILED，NORMAL，DELETE
        :type status: str
        :param update_time: 全链路应用更新时间
        :type update_time: int
        :param result: 
        :type result: :class:`huaweicloudsdkcpts.v1.AgentConfig`
        """
        
        

        self._id = None
        self._status = None
        self._update_time = None
        self._result = None
        self.discriminator = None

        self.id = id
        self.status = status
        self.update_time = update_time
        if result is not None:
            self.result = result

    @property
    def id(self):
        r"""Gets the id of this UpdateAgentStatusResponseDetail.

        全链路应用id

        :return: The id of this UpdateAgentStatusResponseDetail.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this UpdateAgentStatusResponseDetail.

        全链路应用id

        :param id: The id of this UpdateAgentStatusResponseDetail.
        :type id: int
        """
        self._id = id

    @property
    def status(self):
        r"""Gets the status of this UpdateAgentStatusResponseDetail.

        全链路应用状态，枚举值：CREATING，FAILED，NORMAL，DELETE

        :return: The status of this UpdateAgentStatusResponseDetail.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this UpdateAgentStatusResponseDetail.

        全链路应用状态，枚举值：CREATING，FAILED，NORMAL，DELETE

        :param status: The status of this UpdateAgentStatusResponseDetail.
        :type status: str
        """
        self._status = status

    @property
    def update_time(self):
        r"""Gets the update_time of this UpdateAgentStatusResponseDetail.

        全链路应用更新时间

        :return: The update_time of this UpdateAgentStatusResponseDetail.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this UpdateAgentStatusResponseDetail.

        全链路应用更新时间

        :param update_time: The update_time of this UpdateAgentStatusResponseDetail.
        :type update_time: int
        """
        self._update_time = update_time

    @property
    def result(self):
        r"""Gets the result of this UpdateAgentStatusResponseDetail.

        :return: The result of this UpdateAgentStatusResponseDetail.
        :rtype: :class:`huaweicloudsdkcpts.v1.AgentConfig`
        """
        return self._result

    @result.setter
    def result(self, result):
        r"""Sets the result of this UpdateAgentStatusResponseDetail.

        :param result: The result of this UpdateAgentStatusResponseDetail.
        :type result: :class:`huaweicloudsdkcpts.v1.AgentConfig`
        """
        self._result = result

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
        if not isinstance(other, UpdateAgentStatusResponseDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
