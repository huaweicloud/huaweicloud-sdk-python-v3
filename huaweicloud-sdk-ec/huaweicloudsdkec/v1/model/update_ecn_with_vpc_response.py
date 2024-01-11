# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateEcnWithVpcResponse(SdkResponse):

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
        'vpc_id': 'str',
        'subnet_id': 'str',
        'local_subnet_list': 'list[str]',
        'remote_subnet_list': 'list[str]',
        'region_id': 'str',
        'status': 'str',
        'created_at': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'vpc_id': 'vpc_id',
        'subnet_id': 'subnet_id',
        'local_subnet_list': 'local_subnet_list',
        'remote_subnet_list': 'remote_subnet_list',
        'region_id': 'region_id',
        'status': 'status',
        'created_at': 'created_at'
    }

    def __init__(self, id=None, vpc_id=None, subnet_id=None, local_subnet_list=None, remote_subnet_list=None, region_id=None, status=None, created_at=None):
        """UpdateEcnWithVpcResponse

        The model defined in huaweicloud sdk

        :param id: 企业连接网络关联虚拟私有云ID
        :type id: str
        :param vpc_id: 虚拟私有云ID
        :type vpc_id: str
        :param subnet_id: 子网ID
        :type subnet_id: str
        :param local_subnet_list: 本端子网列表
        :type local_subnet_list: list[str]
        :param remote_subnet_list: 对端子网列表
        :type remote_subnet_list: list[str]
        :param region_id: 区域ID
        :type region_id: str
        :param status: 状态
        :type status: str
        :param created_at: 创建时间
        :type created_at: datetime
        """
        
        super(UpdateEcnWithVpcResponse, self).__init__()

        self._id = None
        self._vpc_id = None
        self._subnet_id = None
        self._local_subnet_list = None
        self._remote_subnet_list = None
        self._region_id = None
        self._status = None
        self._created_at = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if vpc_id is not None:
            self.vpc_id = vpc_id
        if subnet_id is not None:
            self.subnet_id = subnet_id
        if local_subnet_list is not None:
            self.local_subnet_list = local_subnet_list
        if remote_subnet_list is not None:
            self.remote_subnet_list = remote_subnet_list
        if region_id is not None:
            self.region_id = region_id
        if status is not None:
            self.status = status
        if created_at is not None:
            self.created_at = created_at

    @property
    def id(self):
        """Gets the id of this UpdateEcnWithVpcResponse.

        企业连接网络关联虚拟私有云ID

        :return: The id of this UpdateEcnWithVpcResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UpdateEcnWithVpcResponse.

        企业连接网络关联虚拟私有云ID

        :param id: The id of this UpdateEcnWithVpcResponse.
        :type id: str
        """
        self._id = id

    @property
    def vpc_id(self):
        """Gets the vpc_id of this UpdateEcnWithVpcResponse.

        虚拟私有云ID

        :return: The vpc_id of this UpdateEcnWithVpcResponse.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this UpdateEcnWithVpcResponse.

        虚拟私有云ID

        :param vpc_id: The vpc_id of this UpdateEcnWithVpcResponse.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def subnet_id(self):
        """Gets the subnet_id of this UpdateEcnWithVpcResponse.

        子网ID

        :return: The subnet_id of this UpdateEcnWithVpcResponse.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """Sets the subnet_id of this UpdateEcnWithVpcResponse.

        子网ID

        :param subnet_id: The subnet_id of this UpdateEcnWithVpcResponse.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def local_subnet_list(self):
        """Gets the local_subnet_list of this UpdateEcnWithVpcResponse.

        本端子网列表

        :return: The local_subnet_list of this UpdateEcnWithVpcResponse.
        :rtype: list[str]
        """
        return self._local_subnet_list

    @local_subnet_list.setter
    def local_subnet_list(self, local_subnet_list):
        """Sets the local_subnet_list of this UpdateEcnWithVpcResponse.

        本端子网列表

        :param local_subnet_list: The local_subnet_list of this UpdateEcnWithVpcResponse.
        :type local_subnet_list: list[str]
        """
        self._local_subnet_list = local_subnet_list

    @property
    def remote_subnet_list(self):
        """Gets the remote_subnet_list of this UpdateEcnWithVpcResponse.

        对端子网列表

        :return: The remote_subnet_list of this UpdateEcnWithVpcResponse.
        :rtype: list[str]
        """
        return self._remote_subnet_list

    @remote_subnet_list.setter
    def remote_subnet_list(self, remote_subnet_list):
        """Sets the remote_subnet_list of this UpdateEcnWithVpcResponse.

        对端子网列表

        :param remote_subnet_list: The remote_subnet_list of this UpdateEcnWithVpcResponse.
        :type remote_subnet_list: list[str]
        """
        self._remote_subnet_list = remote_subnet_list

    @property
    def region_id(self):
        """Gets the region_id of this UpdateEcnWithVpcResponse.

        区域ID

        :return: The region_id of this UpdateEcnWithVpcResponse.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """Sets the region_id of this UpdateEcnWithVpcResponse.

        区域ID

        :param region_id: The region_id of this UpdateEcnWithVpcResponse.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def status(self):
        """Gets the status of this UpdateEcnWithVpcResponse.

        状态

        :return: The status of this UpdateEcnWithVpcResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this UpdateEcnWithVpcResponse.

        状态

        :param status: The status of this UpdateEcnWithVpcResponse.
        :type status: str
        """
        self._status = status

    @property
    def created_at(self):
        """Gets the created_at of this UpdateEcnWithVpcResponse.

        创建时间

        :return: The created_at of this UpdateEcnWithVpcResponse.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this UpdateEcnWithVpcResponse.

        创建时间

        :param created_at: The created_at of this UpdateEcnWithVpcResponse.
        :type created_at: datetime
        """
        self._created_at = created_at

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
        if not isinstance(other, UpdateEcnWithVpcResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
