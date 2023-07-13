# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDataJobResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'count': 'int',
        'data_jobs': 'list[DataJobRsp]'
    }

    attribute_map = {
        'count': 'count',
        'data_jobs': 'data_jobs'
    }

    def __init__(self, count=None, data_jobs=None):
        """ListDataJobResponse

        The model defined in huaweicloud sdk

        :param count: 总条数
        :type count: int
        :param data_jobs: 数据作业列表
        :type data_jobs: list[:class:`huaweicloudsdkeihealth.v1.DataJobRsp`]
        """
        
        super(ListDataJobResponse, self).__init__()

        self._count = None
        self._data_jobs = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if data_jobs is not None:
            self.data_jobs = data_jobs

    @property
    def count(self):
        """Gets the count of this ListDataJobResponse.

        总条数

        :return: The count of this ListDataJobResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ListDataJobResponse.

        总条数

        :param count: The count of this ListDataJobResponse.
        :type count: int
        """
        self._count = count

    @property
    def data_jobs(self):
        """Gets the data_jobs of this ListDataJobResponse.

        数据作业列表

        :return: The data_jobs of this ListDataJobResponse.
        :rtype: list[:class:`huaweicloudsdkeihealth.v1.DataJobRsp`]
        """
        return self._data_jobs

    @data_jobs.setter
    def data_jobs(self, data_jobs):
        """Sets the data_jobs of this ListDataJobResponse.

        数据作业列表

        :param data_jobs: The data_jobs of this ListDataJobResponse.
        :type data_jobs: list[:class:`huaweicloudsdkeihealth.v1.DataJobRsp`]
        """
        self._data_jobs = data_jobs

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
        if not isinstance(other, ListDataJobResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
