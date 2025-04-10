# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSubnetBandwidthsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enterprise_project_id': 'str',
        'offset': 'int',
        'limit': 'int',
        'vpc_id': 'str',
        'subnet_id': 'str',
        'bandwidth_id': 'str',
        'bandwidth_name': 'str'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'offset': 'offset',
        'limit': 'limit',
        'vpc_id': 'vpc_id',
        'subnet_id': 'subnet_id',
        'bandwidth_id': 'bandwidth_id',
        'bandwidth_name': 'bandwidth_name'
    }

    def __init__(self, enterprise_project_id=None, offset=None, limit=None, vpc_id=None, subnet_id=None, bandwidth_id=None, bandwidth_name=None):
        r"""ListSubnetBandwidthsRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: 企业项目ID。
        :type enterprise_project_id: str
        :param offset: 用于分页查询，查询的起始记录序号，从0开始。
        :type offset: int
        :param limit: 用于分页查询，返回桌面数量限制。如果不指定，则返回所有符合条件的记录。
        :type limit: int
        :param vpc_id: vpc id。
        :type vpc_id: str
        :param subnet_id: 子网id。
        :type subnet_id: str
        :param bandwidth_id: 云办公带宽id。
        :type bandwidth_id: str
        :param bandwidth_name: 云办公带宽名称。
        :type bandwidth_name: str
        """
        
        

        self._enterprise_project_id = None
        self._offset = None
        self._limit = None
        self._vpc_id = None
        self._subnet_id = None
        self._bandwidth_id = None
        self._bandwidth_name = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if vpc_id is not None:
            self.vpc_id = vpc_id
        if subnet_id is not None:
            self.subnet_id = subnet_id
        if bandwidth_id is not None:
            self.bandwidth_id = bandwidth_id
        if bandwidth_name is not None:
            self.bandwidth_name = bandwidth_name

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListSubnetBandwidthsRequest.

        企业项目ID。

        :return: The enterprise_project_id of this ListSubnetBandwidthsRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListSubnetBandwidthsRequest.

        企业项目ID。

        :param enterprise_project_id: The enterprise_project_id of this ListSubnetBandwidthsRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def offset(self):
        r"""Gets the offset of this ListSubnetBandwidthsRequest.

        用于分页查询，查询的起始记录序号，从0开始。

        :return: The offset of this ListSubnetBandwidthsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListSubnetBandwidthsRequest.

        用于分页查询，查询的起始记录序号，从0开始。

        :param offset: The offset of this ListSubnetBandwidthsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListSubnetBandwidthsRequest.

        用于分页查询，返回桌面数量限制。如果不指定，则返回所有符合条件的记录。

        :return: The limit of this ListSubnetBandwidthsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListSubnetBandwidthsRequest.

        用于分页查询，返回桌面数量限制。如果不指定，则返回所有符合条件的记录。

        :param limit: The limit of this ListSubnetBandwidthsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this ListSubnetBandwidthsRequest.

        vpc id。

        :return: The vpc_id of this ListSubnetBandwidthsRequest.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this ListSubnetBandwidthsRequest.

        vpc id。

        :param vpc_id: The vpc_id of this ListSubnetBandwidthsRequest.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def subnet_id(self):
        r"""Gets the subnet_id of this ListSubnetBandwidthsRequest.

        子网id。

        :return: The subnet_id of this ListSubnetBandwidthsRequest.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        r"""Sets the subnet_id of this ListSubnetBandwidthsRequest.

        子网id。

        :param subnet_id: The subnet_id of this ListSubnetBandwidthsRequest.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def bandwidth_id(self):
        r"""Gets the bandwidth_id of this ListSubnetBandwidthsRequest.

        云办公带宽id。

        :return: The bandwidth_id of this ListSubnetBandwidthsRequest.
        :rtype: str
        """
        return self._bandwidth_id

    @bandwidth_id.setter
    def bandwidth_id(self, bandwidth_id):
        r"""Sets the bandwidth_id of this ListSubnetBandwidthsRequest.

        云办公带宽id。

        :param bandwidth_id: The bandwidth_id of this ListSubnetBandwidthsRequest.
        :type bandwidth_id: str
        """
        self._bandwidth_id = bandwidth_id

    @property
    def bandwidth_name(self):
        r"""Gets the bandwidth_name of this ListSubnetBandwidthsRequest.

        云办公带宽名称。

        :return: The bandwidth_name of this ListSubnetBandwidthsRequest.
        :rtype: str
        """
        return self._bandwidth_name

    @bandwidth_name.setter
    def bandwidth_name(self, bandwidth_name):
        r"""Sets the bandwidth_name of this ListSubnetBandwidthsRequest.

        云办公带宽名称。

        :param bandwidth_name: The bandwidth_name of this ListSubnetBandwidthsRequest.
        :type bandwidth_name: str
        """
        self._bandwidth_name = bandwidth_name

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
        if not isinstance(other, ListSubnetBandwidthsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
