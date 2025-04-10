# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class JobScriptOrderStatisticsModel:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total_instance': 'int',
        'execute_statistics': 'list[ExectuionStatistic]'
    }

    attribute_map = {
        'total_instance': 'total_instance',
        'execute_statistics': 'execute_statistics'
    }

    def __init__(self, total_instance=None, execute_statistics=None):
        r"""JobScriptOrderStatisticsModel

        The model defined in huaweicloud sdk

        :param total_instance: 实例总量
        :type total_instance: int
        :param execute_statistics: 每个状态一个count，里面记录该状态的总数量，以及包含该状态的批次列表
        :type execute_statistics: list[:class:`huaweicloudsdkcoc.v1.ExectuionStatistic`]
        """
        
        

        self._total_instance = None
        self._execute_statistics = None
        self.discriminator = None

        if total_instance is not None:
            self.total_instance = total_instance
        if execute_statistics is not None:
            self.execute_statistics = execute_statistics

    @property
    def total_instance(self):
        r"""Gets the total_instance of this JobScriptOrderStatisticsModel.

        实例总量

        :return: The total_instance of this JobScriptOrderStatisticsModel.
        :rtype: int
        """
        return self._total_instance

    @total_instance.setter
    def total_instance(self, total_instance):
        r"""Sets the total_instance of this JobScriptOrderStatisticsModel.

        实例总量

        :param total_instance: The total_instance of this JobScriptOrderStatisticsModel.
        :type total_instance: int
        """
        self._total_instance = total_instance

    @property
    def execute_statistics(self):
        r"""Gets the execute_statistics of this JobScriptOrderStatisticsModel.

        每个状态一个count，里面记录该状态的总数量，以及包含该状态的批次列表

        :return: The execute_statistics of this JobScriptOrderStatisticsModel.
        :rtype: list[:class:`huaweicloudsdkcoc.v1.ExectuionStatistic`]
        """
        return self._execute_statistics

    @execute_statistics.setter
    def execute_statistics(self, execute_statistics):
        r"""Sets the execute_statistics of this JobScriptOrderStatisticsModel.

        每个状态一个count，里面记录该状态的总数量，以及包含该状态的批次列表

        :param execute_statistics: The execute_statistics of this JobScriptOrderStatisticsModel.
        :type execute_statistics: list[:class:`huaweicloudsdkcoc.v1.ExectuionStatistic`]
        """
        self._execute_statistics = execute_statistics

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
        if not isinstance(other, JobScriptOrderStatisticsModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
