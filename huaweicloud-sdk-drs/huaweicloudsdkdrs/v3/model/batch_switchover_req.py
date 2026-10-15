# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchSwitchoverReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'jobs': 'list[str]',
        'is_pause_job': 'bool'
    }

    attribute_map = {
        'jobs': 'jobs',
        'is_pause_job': 'is_pause_job'
    }

    def __init__(self, jobs=None, is_pause_job=None):
        r"""BatchSwitchoverReq

        The model defined in huaweicloud sdk

        :param jobs: 批量主备调换的任务详情ID请求列表
        :type jobs: list[str]
        :param is_pause_job: 灾备倒换后是否暂停任务。默认值为false，不暂停灾备任务。
        :type is_pause_job: bool
        """
        
        

        self._jobs = None
        self._is_pause_job = None
        self.discriminator = None

        self.jobs = jobs
        if is_pause_job is not None:
            self.is_pause_job = is_pause_job

    @property
    def jobs(self):
        r"""Gets the jobs of this BatchSwitchoverReq.

        批量主备调换的任务详情ID请求列表

        :return: The jobs of this BatchSwitchoverReq.
        :rtype: list[str]
        """
        return self._jobs

    @jobs.setter
    def jobs(self, jobs):
        r"""Sets the jobs of this BatchSwitchoverReq.

        批量主备调换的任务详情ID请求列表

        :param jobs: The jobs of this BatchSwitchoverReq.
        :type jobs: list[str]
        """
        self._jobs = jobs

    @property
    def is_pause_job(self):
        r"""Gets the is_pause_job of this BatchSwitchoverReq.

        灾备倒换后是否暂停任务。默认值为false，不暂停灾备任务。

        :return: The is_pause_job of this BatchSwitchoverReq.
        :rtype: bool
        """
        return self._is_pause_job

    @is_pause_job.setter
    def is_pause_job(self, is_pause_job):
        r"""Sets the is_pause_job of this BatchSwitchoverReq.

        灾备倒换后是否暂停任务。默认值为false，不暂停灾备任务。

        :param is_pause_job: The is_pause_job of this BatchSwitchoverReq.
        :type is_pause_job: bool
        """
        self._is_pause_job = is_pause_job

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
        if not isinstance(other, BatchSwitchoverReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
