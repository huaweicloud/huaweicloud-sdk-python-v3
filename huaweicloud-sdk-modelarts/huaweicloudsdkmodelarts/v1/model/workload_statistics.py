# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WorkloadStatistics:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'total': 'int',
        'status': 'WorkloadStatisticsStatus'
    }

    attribute_map = {
        'type': 'type',
        'total': 'total',
        'status': 'status'
    }

    def __init__(self, type=None, total=None, status=None):
        r"""WorkloadStatistics

        The model defined in huaweicloud sdk

        :param type: **参数描述**： 作业类型。 **取值范围**： 可选值如下： - train：训练作业 - infer：推理作业 - notebook：Notebook作业
        :type type: str
        :param total: **参数描述**： 作业个数。 **取值范围**： 不涉及。
        :type total: int
        :param status: 
        :type status: :class:`huaweicloudsdkmodelarts.v1.WorkloadStatisticsStatus`
        """
        
        

        self._type = None
        self._total = None
        self._status = None
        self.discriminator = None

        self.type = type
        self.total = total
        self.status = status

    @property
    def type(self):
        r"""Gets the type of this WorkloadStatistics.

        **参数描述**： 作业类型。 **取值范围**： 可选值如下： - train：训练作业 - infer：推理作业 - notebook：Notebook作业

        :return: The type of this WorkloadStatistics.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this WorkloadStatistics.

        **参数描述**： 作业类型。 **取值范围**： 可选值如下： - train：训练作业 - infer：推理作业 - notebook：Notebook作业

        :param type: The type of this WorkloadStatistics.
        :type type: str
        """
        self._type = type

    @property
    def total(self):
        r"""Gets the total of this WorkloadStatistics.

        **参数描述**： 作业个数。 **取值范围**： 不涉及。

        :return: The total of this WorkloadStatistics.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this WorkloadStatistics.

        **参数描述**： 作业个数。 **取值范围**： 不涉及。

        :param total: The total of this WorkloadStatistics.
        :type total: int
        """
        self._total = total

    @property
    def status(self):
        r"""Gets the status of this WorkloadStatistics.

        :return: The status of this WorkloadStatistics.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.WorkloadStatisticsStatus`
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this WorkloadStatistics.

        :param status: The status of this WorkloadStatistics.
        :type status: :class:`huaweicloudsdkmodelarts.v1.WorkloadStatisticsStatus`
        """
        self._status = status

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
        if not isinstance(other, WorkloadStatistics):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
