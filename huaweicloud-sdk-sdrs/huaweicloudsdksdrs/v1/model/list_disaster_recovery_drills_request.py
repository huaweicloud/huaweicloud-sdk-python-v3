# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDisasterRecoveryDrillsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'server_group_id': 'str',
        'name': 'str',
        'status': 'str',
        'drill_vpc_id': 'str',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'server_group_id': 'server_group_id',
        'name': 'name',
        'status': 'status',
        'drill_vpc_id': 'drill_vpc_id',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, server_group_id=None, name=None, status=None, drill_vpc_id=None, limit=None, offset=None):
        """ListDisasterRecoveryDrillsRequest

        The model defined in huaweicloud sdk

        :param server_group_id: 保护组的ID。
        :type server_group_id: str
        :param name: 容灾演练的名称。支持模糊查询。
        :type name: str
        :param status: 容灾演练的状态。
        :type status: str
        :param drill_vpc_id: 演练虚拟私有云ID。
        :type drill_vpc_id: str
        :param limit: 每次请求返回结果个数限制，取值范围为[0,1000]的正整数，默认值为1000。
        :type limit: int
        :param offset: 每次请求开始的下标，即偏移量，默认值为0。offset必须为数字，不能为负数。
        :type offset: int
        """
        
        

        self._server_group_id = None
        self._name = None
        self._status = None
        self._drill_vpc_id = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        if server_group_id is not None:
            self.server_group_id = server_group_id
        if name is not None:
            self.name = name
        if status is not None:
            self.status = status
        if drill_vpc_id is not None:
            self.drill_vpc_id = drill_vpc_id
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def server_group_id(self):
        """Gets the server_group_id of this ListDisasterRecoveryDrillsRequest.

        保护组的ID。

        :return: The server_group_id of this ListDisasterRecoveryDrillsRequest.
        :rtype: str
        """
        return self._server_group_id

    @server_group_id.setter
    def server_group_id(self, server_group_id):
        """Sets the server_group_id of this ListDisasterRecoveryDrillsRequest.

        保护组的ID。

        :param server_group_id: The server_group_id of this ListDisasterRecoveryDrillsRequest.
        :type server_group_id: str
        """
        self._server_group_id = server_group_id

    @property
    def name(self):
        """Gets the name of this ListDisasterRecoveryDrillsRequest.

        容灾演练的名称。支持模糊查询。

        :return: The name of this ListDisasterRecoveryDrillsRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListDisasterRecoveryDrillsRequest.

        容灾演练的名称。支持模糊查询。

        :param name: The name of this ListDisasterRecoveryDrillsRequest.
        :type name: str
        """
        self._name = name

    @property
    def status(self):
        """Gets the status of this ListDisasterRecoveryDrillsRequest.

        容灾演练的状态。

        :return: The status of this ListDisasterRecoveryDrillsRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListDisasterRecoveryDrillsRequest.

        容灾演练的状态。

        :param status: The status of this ListDisasterRecoveryDrillsRequest.
        :type status: str
        """
        self._status = status

    @property
    def drill_vpc_id(self):
        """Gets the drill_vpc_id of this ListDisasterRecoveryDrillsRequest.

        演练虚拟私有云ID。

        :return: The drill_vpc_id of this ListDisasterRecoveryDrillsRequest.
        :rtype: str
        """
        return self._drill_vpc_id

    @drill_vpc_id.setter
    def drill_vpc_id(self, drill_vpc_id):
        """Sets the drill_vpc_id of this ListDisasterRecoveryDrillsRequest.

        演练虚拟私有云ID。

        :param drill_vpc_id: The drill_vpc_id of this ListDisasterRecoveryDrillsRequest.
        :type drill_vpc_id: str
        """
        self._drill_vpc_id = drill_vpc_id

    @property
    def limit(self):
        """Gets the limit of this ListDisasterRecoveryDrillsRequest.

        每次请求返回结果个数限制，取值范围为[0,1000]的正整数，默认值为1000。

        :return: The limit of this ListDisasterRecoveryDrillsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListDisasterRecoveryDrillsRequest.

        每次请求返回结果个数限制，取值范围为[0,1000]的正整数，默认值为1000。

        :param limit: The limit of this ListDisasterRecoveryDrillsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListDisasterRecoveryDrillsRequest.

        每次请求开始的下标，即偏移量，默认值为0。offset必须为数字，不能为负数。

        :return: The offset of this ListDisasterRecoveryDrillsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListDisasterRecoveryDrillsRequest.

        每次请求开始的下标，即偏移量，默认值为0。offset必须为数字，不能为负数。

        :param offset: The offset of this ListDisasterRecoveryDrillsRequest.
        :type offset: int
        """
        self._offset = offset

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
        if not isinstance(other, ListDisasterRecoveryDrillsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
