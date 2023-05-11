# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAutoJobResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'auto_jobs': 'list[AutoJobListDto]',
        'count': 'int'
    }

    attribute_map = {
        'auto_jobs': 'auto_jobs',
        'count': 'count'
    }

    def __init__(self, auto_jobs=None, count=None):
        """ListAutoJobResponse

        The model defined in huaweicloud sdk

        :param auto_jobs: 自动作业列表
        :type auto_jobs: list[:class:`huaweicloudsdkeihealth.v1.AutoJobListDto`]
        :param count: 作业总数
        :type count: int
        """
        
        super(ListAutoJobResponse, self).__init__()

        self._auto_jobs = None
        self._count = None
        self.discriminator = None

        if auto_jobs is not None:
            self.auto_jobs = auto_jobs
        if count is not None:
            self.count = count

    @property
    def auto_jobs(self):
        """Gets the auto_jobs of this ListAutoJobResponse.

        自动作业列表

        :return: The auto_jobs of this ListAutoJobResponse.
        :rtype: list[:class:`huaweicloudsdkeihealth.v1.AutoJobListDto`]
        """
        return self._auto_jobs

    @auto_jobs.setter
    def auto_jobs(self, auto_jobs):
        """Sets the auto_jobs of this ListAutoJobResponse.

        自动作业列表

        :param auto_jobs: The auto_jobs of this ListAutoJobResponse.
        :type auto_jobs: list[:class:`huaweicloudsdkeihealth.v1.AutoJobListDto`]
        """
        self._auto_jobs = auto_jobs

    @property
    def count(self):
        """Gets the count of this ListAutoJobResponse.

        作业总数

        :return: The count of this ListAutoJobResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ListAutoJobResponse.

        作业总数

        :param count: The count of this ListAutoJobResponse.
        :type count: int
        """
        self._count = count

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
        if not isinstance(other, ListAutoJobResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
