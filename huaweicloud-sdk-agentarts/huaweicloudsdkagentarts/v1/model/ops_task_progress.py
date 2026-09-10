# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OpsTaskProgress:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total': 'int',
        'progressed': 'int',
        'progress_rate': 'int'
    }

    attribute_map = {
        'total': 'total',
        'progressed': 'progressed',
        'progress_rate': 'progress_rate'
    }

    def __init__(self, total=None, progressed=None, progress_rate=None):
        r"""OpsTaskProgress

        The model defined in huaweicloud sdk

        :param total: **参数解释：**  对于周期任务，表示总计计划执行的次数。 对于运行中的单次任务，值为计划要分析的trace条数。 对还未开始运行的单次任务，值为null。 **取值范围：** null或0-5000
        :type total: int
        :param progressed: **参数解释：**  对于周期任务，表示已经处理的次数。 对于运行中的单次任务，值为计划要已分析的trace条数。 对还未开始运行的单次任务，值为0。 **取值范围：** 0-5000
        :type progressed: int
        :param progress_rate: **参数解释：**  进度百分比 **取值范围：**  0-100
        :type progress_rate: int
        """
        
        

        self._total = None
        self._progressed = None
        self._progress_rate = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if progressed is not None:
            self.progressed = progressed
        if progress_rate is not None:
            self.progress_rate = progress_rate

    @property
    def total(self):
        r"""Gets the total of this OpsTaskProgress.

        **参数解释：**  对于周期任务，表示总计计划执行的次数。 对于运行中的单次任务，值为计划要分析的trace条数。 对还未开始运行的单次任务，值为null。 **取值范围：** null或0-5000

        :return: The total of this OpsTaskProgress.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this OpsTaskProgress.

        **参数解释：**  对于周期任务，表示总计计划执行的次数。 对于运行中的单次任务，值为计划要分析的trace条数。 对还未开始运行的单次任务，值为null。 **取值范围：** null或0-5000

        :param total: The total of this OpsTaskProgress.
        :type total: int
        """
        self._total = total

    @property
    def progressed(self):
        r"""Gets the progressed of this OpsTaskProgress.

        **参数解释：**  对于周期任务，表示已经处理的次数。 对于运行中的单次任务，值为计划要已分析的trace条数。 对还未开始运行的单次任务，值为0。 **取值范围：** 0-5000

        :return: The progressed of this OpsTaskProgress.
        :rtype: int
        """
        return self._progressed

    @progressed.setter
    def progressed(self, progressed):
        r"""Sets the progressed of this OpsTaskProgress.

        **参数解释：**  对于周期任务，表示已经处理的次数。 对于运行中的单次任务，值为计划要已分析的trace条数。 对还未开始运行的单次任务，值为0。 **取值范围：** 0-5000

        :param progressed: The progressed of this OpsTaskProgress.
        :type progressed: int
        """
        self._progressed = progressed

    @property
    def progress_rate(self):
        r"""Gets the progress_rate of this OpsTaskProgress.

        **参数解释：**  进度百分比 **取值范围：**  0-100

        :return: The progress_rate of this OpsTaskProgress.
        :rtype: int
        """
        return self._progress_rate

    @progress_rate.setter
    def progress_rate(self, progress_rate):
        r"""Sets the progress_rate of this OpsTaskProgress.

        **参数解释：**  进度百分比 **取值范围：**  0-100

        :param progress_rate: The progress_rate of this OpsTaskProgress.
        :type progress_rate: int
        """
        self._progress_rate = progress_rate

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
        if not isinstance(other, OpsTaskProgress):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
