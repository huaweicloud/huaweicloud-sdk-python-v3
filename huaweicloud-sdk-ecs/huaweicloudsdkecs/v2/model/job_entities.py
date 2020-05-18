# coding: utf-8

import pprint
import re

import six


class JobEntities(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        'sub_jobs': 'list[SubJob]',
        'sub_jobs_total': 'int',
        'server_id': 'str',
        'nic_id': 'str'
    }

    attribute_map = {
        'sub_jobs': 'sub_jobs',
        'sub_jobs_total': 'sub_jobs_total',
        'server_id': 'server_id',
        'nic_id': 'nic_id'
    }

    def __init__(self, sub_jobs=None, sub_jobs_total=None, server_id=None, nic_id=None):  # noqa: E501
        """JobEntities - a model defined in huaweicloud sdk"""

        self._sub_jobs = None
        self._sub_jobs_total = None
        self._server_id = None
        self._nic_id = None
        self.discriminator = None

        if sub_jobs is not None:
            self.sub_jobs = sub_jobs
        if sub_jobs_total is not None:
            self.sub_jobs_total = sub_jobs_total
        if server_id is not None:
            self.server_id = server_id
        if nic_id is not None:
            self.nic_id = nic_id

    @property
    def sub_jobs(self):
        """Gets the sub_jobs of this JobEntities.

        每个子任务的执行信息。

        :return: The sub_jobs of this JobEntities.
        :rtype: list[SubJob]
        """
        return self._sub_jobs

    @sub_jobs.setter
    def sub_jobs(self, sub_jobs):
        """Sets the sub_jobs of this JobEntities.

        每个子任务的执行信息。

        :param sub_jobs: The sub_jobs of this JobEntities.
        :type: list[SubJob]
        """
        self._sub_jobs = sub_jobs

    @property
    def sub_jobs_total(self):
        """Gets the sub_jobs_total of this JobEntities.

        子任务数量。

        :return: The sub_jobs_total of this JobEntities.
        :rtype: int
        """
        return self._sub_jobs_total

    @sub_jobs_total.setter
    def sub_jobs_total(self, sub_jobs_total):
        """Sets the sub_jobs_total of this JobEntities.

        子任务数量。

        :param sub_jobs_total: The sub_jobs_total of this JobEntities.
        :type: int
        """
        self._sub_jobs_total = sub_jobs_total

    @property
    def server_id(self):
        """Gets the server_id of this JobEntities.

        云服务器相关操作显示server_id。

        :return: The server_id of this JobEntities.
        :rtype: str
        """
        return self._server_id

    @server_id.setter
    def server_id(self, server_id):
        """Sets the server_id of this JobEntities.

        云服务器相关操作显示server_id。

        :param server_id: The server_id of this JobEntities.
        :type: str
        """
        self._server_id = server_id

    @property
    def nic_id(self):
        """Gets the nic_id of this JobEntities.

        网卡相关操作显示nic_id。

        :return: The nic_id of this JobEntities.
        :rtype: str
        """
        return self._nic_id

    @nic_id.setter
    def nic_id(self, nic_id):
        """Sets the nic_id of this JobEntities.

        网卡相关操作显示nic_id。

        :param nic_id: The nic_id of this JobEntities.
        :type: str
        """
        self._nic_id = nic_id

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
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, JobEntities):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
