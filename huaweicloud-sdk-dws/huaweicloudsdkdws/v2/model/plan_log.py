# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PlanLog:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'exec_time': 'str',
        'stage_info': 'str',
        'exec_result': 'int',
        'exec_log': 'str'
    }

    attribute_map = {
        'exec_time': 'exec_time',
        'stage_info': 'stage_info',
        'exec_result': 'exec_result',
        'exec_log': 'exec_log'
    }

    def __init__(self, exec_time=None, stage_info=None, exec_result=None, exec_log=None):
        r"""PlanLog

        The model defined in huaweicloud sdk

        :param exec_time: **参数解释**： 执行时间。 **取值范围**： 不涉及。
        :type exec_time: str
        :param stage_info: **参数解释**： 执行计划阶段。 **取值范围**： 不涉及。
        :type stage_info: str
        :param exec_result: **参数解释**： 执行结果。 **取值范围**： 不涉及。
        :type exec_result: int
        :param exec_log: **参数解释**： 执行日志。 **取值范围**： 不涉及。
        :type exec_log: str
        """
        
        

        self._exec_time = None
        self._stage_info = None
        self._exec_result = None
        self._exec_log = None
        self.discriminator = None

        self.exec_time = exec_time
        self.stage_info = stage_info
        self.exec_result = exec_result
        self.exec_log = exec_log

    @property
    def exec_time(self):
        r"""Gets the exec_time of this PlanLog.

        **参数解释**： 执行时间。 **取值范围**： 不涉及。

        :return: The exec_time of this PlanLog.
        :rtype: str
        """
        return self._exec_time

    @exec_time.setter
    def exec_time(self, exec_time):
        r"""Sets the exec_time of this PlanLog.

        **参数解释**： 执行时间。 **取值范围**： 不涉及。

        :param exec_time: The exec_time of this PlanLog.
        :type exec_time: str
        """
        self._exec_time = exec_time

    @property
    def stage_info(self):
        r"""Gets the stage_info of this PlanLog.

        **参数解释**： 执行计划阶段。 **取值范围**： 不涉及。

        :return: The stage_info of this PlanLog.
        :rtype: str
        """
        return self._stage_info

    @stage_info.setter
    def stage_info(self, stage_info):
        r"""Sets the stage_info of this PlanLog.

        **参数解释**： 执行计划阶段。 **取值范围**： 不涉及。

        :param stage_info: The stage_info of this PlanLog.
        :type stage_info: str
        """
        self._stage_info = stage_info

    @property
    def exec_result(self):
        r"""Gets the exec_result of this PlanLog.

        **参数解释**： 执行结果。 **取值范围**： 不涉及。

        :return: The exec_result of this PlanLog.
        :rtype: int
        """
        return self._exec_result

    @exec_result.setter
    def exec_result(self, exec_result):
        r"""Sets the exec_result of this PlanLog.

        **参数解释**： 执行结果。 **取值范围**： 不涉及。

        :param exec_result: The exec_result of this PlanLog.
        :type exec_result: int
        """
        self._exec_result = exec_result

    @property
    def exec_log(self):
        r"""Gets the exec_log of this PlanLog.

        **参数解释**： 执行日志。 **取值范围**： 不涉及。

        :return: The exec_log of this PlanLog.
        :rtype: str
        """
        return self._exec_log

    @exec_log.setter
    def exec_log(self, exec_log):
        r"""Sets the exec_log of this PlanLog.

        **参数解释**： 执行日志。 **取值范围**： 不涉及。

        :param exec_log: The exec_log of this PlanLog.
        :type exec_log: str
        """
        self._exec_log = exec_log

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
        if not isinstance(other, PlanLog):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
