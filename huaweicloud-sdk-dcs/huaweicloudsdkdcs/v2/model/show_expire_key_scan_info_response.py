# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowExpireKeyScanInfoResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'records': 'list[SimpleKeyScanRecord]',
        'instance_id': 'str',
        'total': 'int',
        'count': 'int'
    }

    attribute_map = {
        'records': 'records',
        'instance_id': 'instance_id',
        'total': 'total',
        'count': 'count'
    }

    def __init__(self, records=None, instance_id=None, total=None, count=None):
        """ShowExpireKeyScanInfoResponse

        The model defined in huaweicloud sdk

        :param records: 记录
        :type records: list[:class:`huaweicloudsdkdcs.v2.SimpleKeyScanRecord`]
        :param instance_id: 实例ID
        :type instance_id: str
        :param total: 总数
        :type total: int
        :param count: 统计
        :type count: int
        """
        
        super(ShowExpireKeyScanInfoResponse, self).__init__()

        self._records = None
        self._instance_id = None
        self._total = None
        self._count = None
        self.discriminator = None

        if records is not None:
            self.records = records
        if instance_id is not None:
            self.instance_id = instance_id
        if total is not None:
            self.total = total
        if count is not None:
            self.count = count

    @property
    def records(self):
        """Gets the records of this ShowExpireKeyScanInfoResponse.

        记录

        :return: The records of this ShowExpireKeyScanInfoResponse.
        :rtype: list[:class:`huaweicloudsdkdcs.v2.SimpleKeyScanRecord`]
        """
        return self._records

    @records.setter
    def records(self, records):
        """Sets the records of this ShowExpireKeyScanInfoResponse.

        记录

        :param records: The records of this ShowExpireKeyScanInfoResponse.
        :type records: list[:class:`huaweicloudsdkdcs.v2.SimpleKeyScanRecord`]
        """
        self._records = records

    @property
    def instance_id(self):
        """Gets the instance_id of this ShowExpireKeyScanInfoResponse.

        实例ID

        :return: The instance_id of this ShowExpireKeyScanInfoResponse.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ShowExpireKeyScanInfoResponse.

        实例ID

        :param instance_id: The instance_id of this ShowExpireKeyScanInfoResponse.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def total(self):
        """Gets the total of this ShowExpireKeyScanInfoResponse.

        总数

        :return: The total of this ShowExpireKeyScanInfoResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ShowExpireKeyScanInfoResponse.

        总数

        :param total: The total of this ShowExpireKeyScanInfoResponse.
        :type total: int
        """
        self._total = total

    @property
    def count(self):
        """Gets the count of this ShowExpireKeyScanInfoResponse.

        统计

        :return: The count of this ShowExpireKeyScanInfoResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ShowExpireKeyScanInfoResponse.

        统计

        :param count: The count of this ShowExpireKeyScanInfoResponse.
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
        if not isinstance(other, ShowExpireKeyScanInfoResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
