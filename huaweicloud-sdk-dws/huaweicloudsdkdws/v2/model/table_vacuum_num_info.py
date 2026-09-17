# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TableVacuumNumInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'waiting_num': 'int',
        'running_num': 'int',
        'finished_num': 'int',
        'canceled_num': 'int',
        'total_num': 'int'
    }

    attribute_map = {
        'waiting_num': 'waiting_num',
        'running_num': 'running_num',
        'finished_num': 'finished_num',
        'canceled_num': 'canceled_num',
        'total_num': 'total_num'
    }

    def __init__(self, waiting_num=None, running_num=None, finished_num=None, canceled_num=None, total_num=None):
        r"""TableVacuumNumInfo

        The model defined in huaweicloud sdk

        :param waiting_num: **参数解释**： 等待的表数量。 **默认取值**： 不涉及。
        :type waiting_num: int
        :param running_num: **参数解释**： 运行中的表数量。 **默认取值**： 不涉及。
        :type running_num: int
        :param finished_num: **参数解释**： 已完成的表数量。 **默认取值**： 不涉及。
        :type finished_num: int
        :param canceled_num: **参数解释**： 取消的表数量。 **默认取值**： 不涉及。
        :type canceled_num: int
        :param total_num: **参数解释**： 总数。 **默认取值**： 不涉及。
        :type total_num: int
        """
        
        

        self._waiting_num = None
        self._running_num = None
        self._finished_num = None
        self._canceled_num = None
        self._total_num = None
        self.discriminator = None

        if waiting_num is not None:
            self.waiting_num = waiting_num
        if running_num is not None:
            self.running_num = running_num
        if finished_num is not None:
            self.finished_num = finished_num
        if canceled_num is not None:
            self.canceled_num = canceled_num
        if total_num is not None:
            self.total_num = total_num

    @property
    def waiting_num(self):
        r"""Gets the waiting_num of this TableVacuumNumInfo.

        **参数解释**： 等待的表数量。 **默认取值**： 不涉及。

        :return: The waiting_num of this TableVacuumNumInfo.
        :rtype: int
        """
        return self._waiting_num

    @waiting_num.setter
    def waiting_num(self, waiting_num):
        r"""Sets the waiting_num of this TableVacuumNumInfo.

        **参数解释**： 等待的表数量。 **默认取值**： 不涉及。

        :param waiting_num: The waiting_num of this TableVacuumNumInfo.
        :type waiting_num: int
        """
        self._waiting_num = waiting_num

    @property
    def running_num(self):
        r"""Gets the running_num of this TableVacuumNumInfo.

        **参数解释**： 运行中的表数量。 **默认取值**： 不涉及。

        :return: The running_num of this TableVacuumNumInfo.
        :rtype: int
        """
        return self._running_num

    @running_num.setter
    def running_num(self, running_num):
        r"""Sets the running_num of this TableVacuumNumInfo.

        **参数解释**： 运行中的表数量。 **默认取值**： 不涉及。

        :param running_num: The running_num of this TableVacuumNumInfo.
        :type running_num: int
        """
        self._running_num = running_num

    @property
    def finished_num(self):
        r"""Gets the finished_num of this TableVacuumNumInfo.

        **参数解释**： 已完成的表数量。 **默认取值**： 不涉及。

        :return: The finished_num of this TableVacuumNumInfo.
        :rtype: int
        """
        return self._finished_num

    @finished_num.setter
    def finished_num(self, finished_num):
        r"""Sets the finished_num of this TableVacuumNumInfo.

        **参数解释**： 已完成的表数量。 **默认取值**： 不涉及。

        :param finished_num: The finished_num of this TableVacuumNumInfo.
        :type finished_num: int
        """
        self._finished_num = finished_num

    @property
    def canceled_num(self):
        r"""Gets the canceled_num of this TableVacuumNumInfo.

        **参数解释**： 取消的表数量。 **默认取值**： 不涉及。

        :return: The canceled_num of this TableVacuumNumInfo.
        :rtype: int
        """
        return self._canceled_num

    @canceled_num.setter
    def canceled_num(self, canceled_num):
        r"""Sets the canceled_num of this TableVacuumNumInfo.

        **参数解释**： 取消的表数量。 **默认取值**： 不涉及。

        :param canceled_num: The canceled_num of this TableVacuumNumInfo.
        :type canceled_num: int
        """
        self._canceled_num = canceled_num

    @property
    def total_num(self):
        r"""Gets the total_num of this TableVacuumNumInfo.

        **参数解释**： 总数。 **默认取值**： 不涉及。

        :return: The total_num of this TableVacuumNumInfo.
        :rtype: int
        """
        return self._total_num

    @total_num.setter
    def total_num(self, total_num):
        r"""Sets the total_num of this TableVacuumNumInfo.

        **参数解释**： 总数。 **默认取值**： 不涉及。

        :param total_num: The total_num of this TableVacuumNumInfo.
        :type total_num: int
        """
        self._total_num = total_num

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
        if not isinstance(other, TableVacuumNumInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
