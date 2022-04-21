# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class JobEntities:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'sub_jobs': 'list[SubJob]',
        'sub_jobs_total': 'int'
    }

    attribute_map = {
        'sub_jobs': 'sub_jobs',
        'sub_jobs_total': 'sub_jobs_total'
    }

    def __init__(self, sub_jobs=None, sub_jobs_total=None):
        """JobEntities

        The model defined in huaweicloud sdk

        :param sub_jobs: 每个子任务的执行信息。
        :type sub_jobs: list[:class:`huaweicloudsdkecs.v2.SubJob`]
        :param sub_jobs_total: 子任务数量。
        :type sub_jobs_total: int
        """
        
        

        self._sub_jobs = None
        self._sub_jobs_total = None
        self.discriminator = None

        if sub_jobs is not None:
            self.sub_jobs = sub_jobs
        if sub_jobs_total is not None:
            self.sub_jobs_total = sub_jobs_total

    @property
    def sub_jobs(self):
        """Gets the sub_jobs of this JobEntities.

        每个子任务的执行信息。

        :return: The sub_jobs of this JobEntities.
        :rtype: list[:class:`huaweicloudsdkecs.v2.SubJob`]
        """
        return self._sub_jobs

    @sub_jobs.setter
    def sub_jobs(self, sub_jobs):
        """Sets the sub_jobs of this JobEntities.

        每个子任务的执行信息。

        :param sub_jobs: The sub_jobs of this JobEntities.
        :type sub_jobs: list[:class:`huaweicloudsdkecs.v2.SubJob`]
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
        :type sub_jobs_total: int
        """
        self._sub_jobs_total = sub_jobs_total

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
        if not isinstance(other, JobEntities):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
