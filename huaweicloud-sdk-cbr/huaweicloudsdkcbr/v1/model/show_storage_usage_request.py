# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowStorageUsageRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'limit': 'int',
        'offset': 'int',
        'resource_id': 'str',
        'resource_type': 'str'
    }

    attribute_map = {
        'limit': 'limit',
        'offset': 'offset',
        'resource_id': 'resource_id',
        'resource_type': 'resource_type'
    }

    def __init__(self, limit=None, offset=None, resource_id=None, resource_type=None):
        r"""ShowStorageUsageRequest

        The model defined in huaweicloud sdk

        :param limit: 查询条数
        :type limit: int
        :param offset: 偏移值
        :type offset: int
        :param resource_id: 支持按照备份对象ID过滤
        :type resource_id: str
        :param resource_type: 支持按照备份对象类型过滤
        :type resource_type: str
        """
        
        

        self._limit = None
        self._offset = None
        self._resource_id = None
        self._resource_type = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if resource_id is not None:
            self.resource_id = resource_id
        if resource_type is not None:
            self.resource_type = resource_type

    @property
    def limit(self):
        r"""Gets the limit of this ShowStorageUsageRequest.

        查询条数

        :return: The limit of this ShowStorageUsageRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ShowStorageUsageRequest.

        查询条数

        :param limit: The limit of this ShowStorageUsageRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ShowStorageUsageRequest.

        偏移值

        :return: The offset of this ShowStorageUsageRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ShowStorageUsageRequest.

        偏移值

        :param offset: The offset of this ShowStorageUsageRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def resource_id(self):
        r"""Gets the resource_id of this ShowStorageUsageRequest.

        支持按照备份对象ID过滤

        :return: The resource_id of this ShowStorageUsageRequest.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this ShowStorageUsageRequest.

        支持按照备份对象ID过滤

        :param resource_id: The resource_id of this ShowStorageUsageRequest.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def resource_type(self):
        r"""Gets the resource_type of this ShowStorageUsageRequest.

        支持按照备份对象类型过滤

        :return: The resource_type of this ShowStorageUsageRequest.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        r"""Sets the resource_type of this ShowStorageUsageRequest.

        支持按照备份对象类型过滤

        :param resource_type: The resource_type of this ShowStorageUsageRequest.
        :type resource_type: str
        """
        self._resource_type = resource_type

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
        if not isinstance(other, ShowStorageUsageRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
