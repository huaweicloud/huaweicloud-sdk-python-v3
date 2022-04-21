# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAvailableRdsListResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'instances': 'list[QueryAvailableRdsList]',
        'offset': 'int',
        'limit': 'int',
        'total': 'int'
    }

    attribute_map = {
        'instances': 'instances',
        'offset': 'offset',
        'limit': 'limit',
        'total': 'total'
    }

    def __init__(self, instances=None, offset=None, limit=None, total=None):
        """ListAvailableRdsListResponse

        The model defined in huaweicloud sdk

        :param instances: 获取创建逻辑库可用数据库实例信息列表的集合。
        :type instances: list[:class:`huaweicloudsdkddm.v1.QueryAvailableRdsList`]
        :param offset: 分页参数: 起始值。
        :type offset: int
        :param limit: 分页参数：每页多少条。
        :type limit: int
        :param total: 集合总数
        :type total: int
        """
        
        super(ListAvailableRdsListResponse, self).__init__()

        self._instances = None
        self._offset = None
        self._limit = None
        self._total = None
        self.discriminator = None

        if instances is not None:
            self.instances = instances
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if total is not None:
            self.total = total

    @property
    def instances(self):
        """Gets the instances of this ListAvailableRdsListResponse.

        获取创建逻辑库可用数据库实例信息列表的集合。

        :return: The instances of this ListAvailableRdsListResponse.
        :rtype: list[:class:`huaweicloudsdkddm.v1.QueryAvailableRdsList`]
        """
        return self._instances

    @instances.setter
    def instances(self, instances):
        """Sets the instances of this ListAvailableRdsListResponse.

        获取创建逻辑库可用数据库实例信息列表的集合。

        :param instances: The instances of this ListAvailableRdsListResponse.
        :type instances: list[:class:`huaweicloudsdkddm.v1.QueryAvailableRdsList`]
        """
        self._instances = instances

    @property
    def offset(self):
        """Gets the offset of this ListAvailableRdsListResponse.

        分页参数: 起始值。

        :return: The offset of this ListAvailableRdsListResponse.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListAvailableRdsListResponse.

        分页参数: 起始值。

        :param offset: The offset of this ListAvailableRdsListResponse.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListAvailableRdsListResponse.

        分页参数：每页多少条。

        :return: The limit of this ListAvailableRdsListResponse.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListAvailableRdsListResponse.

        分页参数：每页多少条。

        :param limit: The limit of this ListAvailableRdsListResponse.
        :type limit: int
        """
        self._limit = limit

    @property
    def total(self):
        """Gets the total of this ListAvailableRdsListResponse.

        集合总数

        :return: The total of this ListAvailableRdsListResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ListAvailableRdsListResponse.

        集合总数

        :param total: The total of this ListAvailableRdsListResponse.
        :type total: int
        """
        self._total = total

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
        if not isinstance(other, ListAvailableRdsListResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
