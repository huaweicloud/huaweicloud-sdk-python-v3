# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateEcnAccessPointResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'region_id': 'str',
        'bandwidth_size': 'int',
        'bind_ieg_count': 'int',
        'attach_vpc_count': 'int',
        'created_at': 'datetime',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'region_id': 'region_id',
        'bandwidth_size': 'bandwidth_size',
        'bind_ieg_count': 'bind_ieg_count',
        'attach_vpc_count': 'attach_vpc_count',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, id=None, region_id=None, bandwidth_size=None, bind_ieg_count=None, attach_vpc_count=None, created_at=None, updated_at=None):
        """CreateEcnAccessPointResponse

        The model defined in huaweicloud sdk

        :param id: 企业连接网络接入点ID
        :type id: str
        :param region_id: 区域ID
        :type region_id: str
        :param bandwidth_size: 带宽
        :type bandwidth_size: int
        :param bind_ieg_count: 绑定智能企业网关数量
        :type bind_ieg_count: int
        :param attach_vpc_count: 关联VPC数量
        :type attach_vpc_count: int
        :param created_at: 创建时间
        :type created_at: datetime
        :param updated_at: 更新时间
        :type updated_at: datetime
        """
        
        super(CreateEcnAccessPointResponse, self).__init__()

        self._id = None
        self._region_id = None
        self._bandwidth_size = None
        self._bind_ieg_count = None
        self._attach_vpc_count = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if region_id is not None:
            self.region_id = region_id
        if bandwidth_size is not None:
            self.bandwidth_size = bandwidth_size
        if bind_ieg_count is not None:
            self.bind_ieg_count = bind_ieg_count
        if attach_vpc_count is not None:
            self.attach_vpc_count = attach_vpc_count
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def id(self):
        """Gets the id of this CreateEcnAccessPointResponse.

        企业连接网络接入点ID

        :return: The id of this CreateEcnAccessPointResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CreateEcnAccessPointResponse.

        企业连接网络接入点ID

        :param id: The id of this CreateEcnAccessPointResponse.
        :type id: str
        """
        self._id = id

    @property
    def region_id(self):
        """Gets the region_id of this CreateEcnAccessPointResponse.

        区域ID

        :return: The region_id of this CreateEcnAccessPointResponse.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """Sets the region_id of this CreateEcnAccessPointResponse.

        区域ID

        :param region_id: The region_id of this CreateEcnAccessPointResponse.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def bandwidth_size(self):
        """Gets the bandwidth_size of this CreateEcnAccessPointResponse.

        带宽

        :return: The bandwidth_size of this CreateEcnAccessPointResponse.
        :rtype: int
        """
        return self._bandwidth_size

    @bandwidth_size.setter
    def bandwidth_size(self, bandwidth_size):
        """Sets the bandwidth_size of this CreateEcnAccessPointResponse.

        带宽

        :param bandwidth_size: The bandwidth_size of this CreateEcnAccessPointResponse.
        :type bandwidth_size: int
        """
        self._bandwidth_size = bandwidth_size

    @property
    def bind_ieg_count(self):
        """Gets the bind_ieg_count of this CreateEcnAccessPointResponse.

        绑定智能企业网关数量

        :return: The bind_ieg_count of this CreateEcnAccessPointResponse.
        :rtype: int
        """
        return self._bind_ieg_count

    @bind_ieg_count.setter
    def bind_ieg_count(self, bind_ieg_count):
        """Sets the bind_ieg_count of this CreateEcnAccessPointResponse.

        绑定智能企业网关数量

        :param bind_ieg_count: The bind_ieg_count of this CreateEcnAccessPointResponse.
        :type bind_ieg_count: int
        """
        self._bind_ieg_count = bind_ieg_count

    @property
    def attach_vpc_count(self):
        """Gets the attach_vpc_count of this CreateEcnAccessPointResponse.

        关联VPC数量

        :return: The attach_vpc_count of this CreateEcnAccessPointResponse.
        :rtype: int
        """
        return self._attach_vpc_count

    @attach_vpc_count.setter
    def attach_vpc_count(self, attach_vpc_count):
        """Sets the attach_vpc_count of this CreateEcnAccessPointResponse.

        关联VPC数量

        :param attach_vpc_count: The attach_vpc_count of this CreateEcnAccessPointResponse.
        :type attach_vpc_count: int
        """
        self._attach_vpc_count = attach_vpc_count

    @property
    def created_at(self):
        """Gets the created_at of this CreateEcnAccessPointResponse.

        创建时间

        :return: The created_at of this CreateEcnAccessPointResponse.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this CreateEcnAccessPointResponse.

        创建时间

        :param created_at: The created_at of this CreateEcnAccessPointResponse.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this CreateEcnAccessPointResponse.

        更新时间

        :return: The updated_at of this CreateEcnAccessPointResponse.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this CreateEcnAccessPointResponse.

        更新时间

        :param updated_at: The updated_at of this CreateEcnAccessPointResponse.
        :type updated_at: datetime
        """
        self._updated_at = updated_at

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
        if not isinstance(other, CreateEcnAccessPointResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
