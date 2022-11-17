# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListBigkeyScanTasksResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'count': 'int',
        'records': 'list[RecordsResponse]'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'count': 'count',
        'records': 'records'
    }

    def __init__(self, instance_id=None, count=None, records=None):
        """ListBigkeyScanTasksResponse

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID
        :type instance_id: str
        :param count: 总数
        :type count: int
        :param records: 大key分析记录列表
        :type records: list[:class:`huaweicloudsdkdcs.v2.RecordsResponse`]
        """
        
        super(ListBigkeyScanTasksResponse, self).__init__()

        self._instance_id = None
        self._count = None
        self._records = None
        self.discriminator = None

        if instance_id is not None:
            self.instance_id = instance_id
        if count is not None:
            self.count = count
        if records is not None:
            self.records = records

    @property
    def instance_id(self):
        """Gets the instance_id of this ListBigkeyScanTasksResponse.

        实例ID

        :return: The instance_id of this ListBigkeyScanTasksResponse.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ListBigkeyScanTasksResponse.

        实例ID

        :param instance_id: The instance_id of this ListBigkeyScanTasksResponse.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def count(self):
        """Gets the count of this ListBigkeyScanTasksResponse.

        总数

        :return: The count of this ListBigkeyScanTasksResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ListBigkeyScanTasksResponse.

        总数

        :param count: The count of this ListBigkeyScanTasksResponse.
        :type count: int
        """
        self._count = count

    @property
    def records(self):
        """Gets the records of this ListBigkeyScanTasksResponse.

        大key分析记录列表

        :return: The records of this ListBigkeyScanTasksResponse.
        :rtype: list[:class:`huaweicloudsdkdcs.v2.RecordsResponse`]
        """
        return self._records

    @records.setter
    def records(self, records):
        """Sets the records of this ListBigkeyScanTasksResponse.

        大key分析记录列表

        :param records: The records of this ListBigkeyScanTasksResponse.
        :type records: list[:class:`huaweicloudsdkdcs.v2.RecordsResponse`]
        """
        self._records = records

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
        if not isinstance(other, ListBigkeyScanTasksResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
