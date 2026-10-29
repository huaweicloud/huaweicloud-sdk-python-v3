# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowTasksListResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'info': 'list[TaskBasicInfo]',
        'total': 'int'
    }

    attribute_map = {
        'info': 'info',
        'total': 'total'
    }

    def __init__(self, info=None, total=None):
        r"""ShowTasksListResult

        The model defined in huaweicloud sdk

        :param info: **参数解释：** 任务列表。
        :type info: list[:class:`huaweicloudsdkcodeartscheck.v2.TaskBasicInfo`]
        :param total: **参数解释：** 代码检查任务总数。 **取值范围：** 不涉及。
        :type total: int
        """
        
        

        self._info = None
        self._total = None
        self.discriminator = None

        if info is not None:
            self.info = info
        if total is not None:
            self.total = total

    @property
    def info(self):
        r"""Gets the info of this ShowTasksListResult.

        **参数解释：** 任务列表。

        :return: The info of this ShowTasksListResult.
        :rtype: list[:class:`huaweicloudsdkcodeartscheck.v2.TaskBasicInfo`]
        """
        return self._info

    @info.setter
    def info(self, info):
        r"""Sets the info of this ShowTasksListResult.

        **参数解释：** 任务列表。

        :param info: The info of this ShowTasksListResult.
        :type info: list[:class:`huaweicloudsdkcodeartscheck.v2.TaskBasicInfo`]
        """
        self._info = info

    @property
    def total(self):
        r"""Gets the total of this ShowTasksListResult.

        **参数解释：** 代码检查任务总数。 **取值范围：** 不涉及。

        :return: The total of this ShowTasksListResult.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ShowTasksListResult.

        **参数解释：** 代码检查任务总数。 **取值范围：** 不涉及。

        :param total: The total of this ShowTasksListResult.
        :type total: int
        """
        self._total = total

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
        if not isinstance(other, ShowTasksListResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
