# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Entities:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'server_id': 'str',
        'nic_id': 'str',
        'sub_jobs_total': 'int',
        'sub_jobs': 'list[SubJobs]'
    }

    attribute_map = {
        'server_id': 'server_id',
        'nic_id': 'nic_id',
        'sub_jobs_total': 'sub_jobs_total',
        'sub_jobs': 'sub_jobs'
    }

    def __init__(self, server_id=None, nic_id=None, sub_jobs_total=None, sub_jobs=None):
        r"""Entities

        The model defined in huaweicloud sdk

        :param server_id: 裸金属服务器相关操作显示server_id
        :type server_id: str
        :param nic_id: 网卡相关操作显示nic_id
        :type nic_id: str
        :param sub_jobs_total: 子任务数量。没有子任务时为0
        :type sub_jobs_total: int
        :param sub_jobs: 每个子任务的执行信息。没有子任务时为空列表
        :type sub_jobs: list[:class:`huaweicloudsdkbms.v1.SubJobs`]
        """
        
        

        self._server_id = None
        self._nic_id = None
        self._sub_jobs_total = None
        self._sub_jobs = None
        self.discriminator = None

        if server_id is not None:
            self.server_id = server_id
        if nic_id is not None:
            self.nic_id = nic_id
        if sub_jobs_total is not None:
            self.sub_jobs_total = sub_jobs_total
        if sub_jobs is not None:
            self.sub_jobs = sub_jobs

    @property
    def server_id(self):
        r"""Gets the server_id of this Entities.

        裸金属服务器相关操作显示server_id

        :return: The server_id of this Entities.
        :rtype: str
        """
        return self._server_id

    @server_id.setter
    def server_id(self, server_id):
        r"""Sets the server_id of this Entities.

        裸金属服务器相关操作显示server_id

        :param server_id: The server_id of this Entities.
        :type server_id: str
        """
        self._server_id = server_id

    @property
    def nic_id(self):
        r"""Gets the nic_id of this Entities.

        网卡相关操作显示nic_id

        :return: The nic_id of this Entities.
        :rtype: str
        """
        return self._nic_id

    @nic_id.setter
    def nic_id(self, nic_id):
        r"""Sets the nic_id of this Entities.

        网卡相关操作显示nic_id

        :param nic_id: The nic_id of this Entities.
        :type nic_id: str
        """
        self._nic_id = nic_id

    @property
    def sub_jobs_total(self):
        r"""Gets the sub_jobs_total of this Entities.

        子任务数量。没有子任务时为0

        :return: The sub_jobs_total of this Entities.
        :rtype: int
        """
        return self._sub_jobs_total

    @sub_jobs_total.setter
    def sub_jobs_total(self, sub_jobs_total):
        r"""Sets the sub_jobs_total of this Entities.

        子任务数量。没有子任务时为0

        :param sub_jobs_total: The sub_jobs_total of this Entities.
        :type sub_jobs_total: int
        """
        self._sub_jobs_total = sub_jobs_total

    @property
    def sub_jobs(self):
        r"""Gets the sub_jobs of this Entities.

        每个子任务的执行信息。没有子任务时为空列表

        :return: The sub_jobs of this Entities.
        :rtype: list[:class:`huaweicloudsdkbms.v1.SubJobs`]
        """
        return self._sub_jobs

    @sub_jobs.setter
    def sub_jobs(self, sub_jobs):
        r"""Sets the sub_jobs of this Entities.

        每个子任务的执行信息。没有子任务时为空列表

        :param sub_jobs: The sub_jobs of this Entities.
        :type sub_jobs: list[:class:`huaweicloudsdkbms.v1.SubJobs`]
        """
        self._sub_jobs = sub_jobs

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
        if not isinstance(other, Entities):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
