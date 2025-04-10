# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpgradeInfoStatus:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'phase': 'str',
        'progress': 'str',
        'completion_time': 'str'
    }

    attribute_map = {
        'phase': 'phase',
        'progress': 'progress',
        'completion_time': 'completionTime'
    }

    def __init__(self, phase=None, progress=None, completion_time=None):
        r"""UpgradeInfoStatus

        The model defined in huaweicloud sdk

        :param phase: 升级任务状态. &gt; Init：初始化 &gt; Running：运行中 &gt; Pause：暂停 &gt; Success：成功 &gt; Failed：失败 
        :type phase: str
        :param progress: 升级任务进度
        :type progress: str
        :param completion_time: 升级任务结束时间
        :type completion_time: str
        """
        
        

        self._phase = None
        self._progress = None
        self._completion_time = None
        self.discriminator = None

        if phase is not None:
            self.phase = phase
        if progress is not None:
            self.progress = progress
        if completion_time is not None:
            self.completion_time = completion_time

    @property
    def phase(self):
        r"""Gets the phase of this UpgradeInfoStatus.

        升级任务状态. > Init：初始化 > Running：运行中 > Pause：暂停 > Success：成功 > Failed：失败 

        :return: The phase of this UpgradeInfoStatus.
        :rtype: str
        """
        return self._phase

    @phase.setter
    def phase(self, phase):
        r"""Sets the phase of this UpgradeInfoStatus.

        升级任务状态. > Init：初始化 > Running：运行中 > Pause：暂停 > Success：成功 > Failed：失败 

        :param phase: The phase of this UpgradeInfoStatus.
        :type phase: str
        """
        self._phase = phase

    @property
    def progress(self):
        r"""Gets the progress of this UpgradeInfoStatus.

        升级任务进度

        :return: The progress of this UpgradeInfoStatus.
        :rtype: str
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        r"""Sets the progress of this UpgradeInfoStatus.

        升级任务进度

        :param progress: The progress of this UpgradeInfoStatus.
        :type progress: str
        """
        self._progress = progress

    @property
    def completion_time(self):
        r"""Gets the completion_time of this UpgradeInfoStatus.

        升级任务结束时间

        :return: The completion_time of this UpgradeInfoStatus.
        :rtype: str
        """
        return self._completion_time

    @completion_time.setter
    def completion_time(self, completion_time):
        r"""Sets the completion_time of this UpgradeInfoStatus.

        升级任务结束时间

        :param completion_time: The completion_time of this UpgradeInfoStatus.
        :type completion_time: str
        """
        self._completion_time = completion_time

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
        if not isinstance(other, UpgradeInfoStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
