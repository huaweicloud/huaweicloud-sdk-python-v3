# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowTaskListResponse(SdkResponse):

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
        'total_records': 'int',
        'max_records': 'int',
        'resources': 'list[MetadataCollectionTask]'
    }

    attribute_map = {
        'count': 'count',
        'total_records': 'total_records',
        'max_records': 'max_records',
        'resources': 'resources'
    }

    def __init__(self, count=None, total_records=None, max_records=None, resources=None):
        """ShowTaskListResponse

        The model defined in huaweicloud sdk

        :param count: 查询采集任务数量
        :type count: int
        :param total_records: 同一projectId下已创建采集任务数量
        :type total_records: int
        :param max_records: 同一projectId下允许创建采集任务数量
        :type max_records: int
        :param resources: 采集任务列表
        :type resources: list[:class:`huaweicloudsdkdataartsstudio.v1.MetadataCollectionTask`]
        """
        
        super(ShowTaskListResponse, self).__init__()

        self._count = None
        self._total_records = None
        self._max_records = None
        self._resources = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if total_records is not None:
            self.total_records = total_records
        if max_records is not None:
            self.max_records = max_records
        if resources is not None:
            self.resources = resources

    @property
    def count(self):
        """Gets the count of this ShowTaskListResponse.

        查询采集任务数量

        :return: The count of this ShowTaskListResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ShowTaskListResponse.

        查询采集任务数量

        :param count: The count of this ShowTaskListResponse.
        :type count: int
        """
        self._count = count

    @property
    def total_records(self):
        """Gets the total_records of this ShowTaskListResponse.

        同一projectId下已创建采集任务数量

        :return: The total_records of this ShowTaskListResponse.
        :rtype: int
        """
        return self._total_records

    @total_records.setter
    def total_records(self, total_records):
        """Sets the total_records of this ShowTaskListResponse.

        同一projectId下已创建采集任务数量

        :param total_records: The total_records of this ShowTaskListResponse.
        :type total_records: int
        """
        self._total_records = total_records

    @property
    def max_records(self):
        """Gets the max_records of this ShowTaskListResponse.

        同一projectId下允许创建采集任务数量

        :return: The max_records of this ShowTaskListResponse.
        :rtype: int
        """
        return self._max_records

    @max_records.setter
    def max_records(self, max_records):
        """Sets the max_records of this ShowTaskListResponse.

        同一projectId下允许创建采集任务数量

        :param max_records: The max_records of this ShowTaskListResponse.
        :type max_records: int
        """
        self._max_records = max_records

    @property
    def resources(self):
        """Gets the resources of this ShowTaskListResponse.

        采集任务列表

        :return: The resources of this ShowTaskListResponse.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.MetadataCollectionTask`]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """Sets the resources of this ShowTaskListResponse.

        采集任务列表

        :param resources: The resources of this ShowTaskListResponse.
        :type resources: list[:class:`huaweicloudsdkdataartsstudio.v1.MetadataCollectionTask`]
        """
        self._resources = resources

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
        if not isinstance(other, ShowTaskListResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
