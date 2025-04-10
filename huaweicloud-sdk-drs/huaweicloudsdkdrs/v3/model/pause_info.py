# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PauseInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'job_id': 'str',
        'pause_mode': 'str'
    }

    attribute_map = {
        'job_id': 'job_id',
        'pause_mode': 'pause_mode'
    }

    def __init__(self, job_id=None, pause_mode=None):
        r"""PauseInfo

        The model defined in huaweicloud sdk

        :param job_id: 任务id
        :type job_id: str
        :param pause_mode: 暂停类型，target:停回放,all:停日志抓取和回放
        :type pause_mode: str
        """
        
        

        self._job_id = None
        self._pause_mode = None
        self.discriminator = None

        self.job_id = job_id
        self.pause_mode = pause_mode

    @property
    def job_id(self):
        r"""Gets the job_id of this PauseInfo.

        任务id

        :return: The job_id of this PauseInfo.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this PauseInfo.

        任务id

        :param job_id: The job_id of this PauseInfo.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def pause_mode(self):
        r"""Gets the pause_mode of this PauseInfo.

        暂停类型，target:停回放,all:停日志抓取和回放

        :return: The pause_mode of this PauseInfo.
        :rtype: str
        """
        return self._pause_mode

    @pause_mode.setter
    def pause_mode(self, pause_mode):
        r"""Sets the pause_mode of this PauseInfo.

        暂停类型，target:停回放,all:停日志抓取和回放

        :param pause_mode: The pause_mode of this PauseInfo.
        :type pause_mode: str
        """
        self._pause_mode = pause_mode

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
        if not isinstance(other, PauseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
