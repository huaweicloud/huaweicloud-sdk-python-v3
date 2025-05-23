# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RejectVpcPeeringResponse(SdkResponse):

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
        'name': 'str',
        'status': 'str',
        'request_vpc_info': 'VpcInfo',
        'accept_vpc_info': 'VpcInfo',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'description': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'status': 'status',
        'request_vpc_info': 'request_vpc_info',
        'accept_vpc_info': 'accept_vpc_info',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'description': 'description'
    }

    def __init__(self, id=None, name=None, status=None, request_vpc_info=None, accept_vpc_info=None, created_at=None, updated_at=None, description=None):
        r"""RejectVpcPeeringResponse

        The model defined in huaweicloud sdk

        :param id: 对等连接ID
        :type id: str
        :param name: 功能说明：对等连接名称 取值范围：支持1~64个字符
        :type name: str
        :param status: 功能说明：对等连接状态 取值范围： - PENDING_ACCEPTANCE：等待接受 - REJECTED：已拒绝。 - EXPIRED：已过期。 - DELETED：已删除。 - ACTIVE：活动的。
        :type status: str
        :param request_vpc_info: 
        :type request_vpc_info: :class:`huaweicloudsdkvpc.v2.VpcInfo`
        :param accept_vpc_info: 
        :type accept_vpc_info: :class:`huaweicloudsdkvpc.v2.VpcInfo`
        :param created_at: 功能说明：资源创建UTC时间 格式：yyyy-MM-ddTHH:mm:ss
        :type created_at: datetime
        :param updated_at: 功能说明：资源更新UTC时间 格式：yyyy-MM-ddTHH:mm:ss
        :type updated_at: datetime
        :param description: 对等连接描述
        :type description: str
        """
        
        super(RejectVpcPeeringResponse, self).__init__()

        self._id = None
        self._name = None
        self._status = None
        self._request_vpc_info = None
        self._accept_vpc_info = None
        self._created_at = None
        self._updated_at = None
        self._description = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if status is not None:
            self.status = status
        if request_vpc_info is not None:
            self.request_vpc_info = request_vpc_info
        if accept_vpc_info is not None:
            self.accept_vpc_info = accept_vpc_info
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if description is not None:
            self.description = description

    @property
    def id(self):
        r"""Gets the id of this RejectVpcPeeringResponse.

        对等连接ID

        :return: The id of this RejectVpcPeeringResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this RejectVpcPeeringResponse.

        对等连接ID

        :param id: The id of this RejectVpcPeeringResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this RejectVpcPeeringResponse.

        功能说明：对等连接名称 取值范围：支持1~64个字符

        :return: The name of this RejectVpcPeeringResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this RejectVpcPeeringResponse.

        功能说明：对等连接名称 取值范围：支持1~64个字符

        :param name: The name of this RejectVpcPeeringResponse.
        :type name: str
        """
        self._name = name

    @property
    def status(self):
        r"""Gets the status of this RejectVpcPeeringResponse.

        功能说明：对等连接状态 取值范围： - PENDING_ACCEPTANCE：等待接受 - REJECTED：已拒绝。 - EXPIRED：已过期。 - DELETED：已删除。 - ACTIVE：活动的。

        :return: The status of this RejectVpcPeeringResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this RejectVpcPeeringResponse.

        功能说明：对等连接状态 取值范围： - PENDING_ACCEPTANCE：等待接受 - REJECTED：已拒绝。 - EXPIRED：已过期。 - DELETED：已删除。 - ACTIVE：活动的。

        :param status: The status of this RejectVpcPeeringResponse.
        :type status: str
        """
        self._status = status

    @property
    def request_vpc_info(self):
        r"""Gets the request_vpc_info of this RejectVpcPeeringResponse.

        :return: The request_vpc_info of this RejectVpcPeeringResponse.
        :rtype: :class:`huaweicloudsdkvpc.v2.VpcInfo`
        """
        return self._request_vpc_info

    @request_vpc_info.setter
    def request_vpc_info(self, request_vpc_info):
        r"""Sets the request_vpc_info of this RejectVpcPeeringResponse.

        :param request_vpc_info: The request_vpc_info of this RejectVpcPeeringResponse.
        :type request_vpc_info: :class:`huaweicloudsdkvpc.v2.VpcInfo`
        """
        self._request_vpc_info = request_vpc_info

    @property
    def accept_vpc_info(self):
        r"""Gets the accept_vpc_info of this RejectVpcPeeringResponse.

        :return: The accept_vpc_info of this RejectVpcPeeringResponse.
        :rtype: :class:`huaweicloudsdkvpc.v2.VpcInfo`
        """
        return self._accept_vpc_info

    @accept_vpc_info.setter
    def accept_vpc_info(self, accept_vpc_info):
        r"""Sets the accept_vpc_info of this RejectVpcPeeringResponse.

        :param accept_vpc_info: The accept_vpc_info of this RejectVpcPeeringResponse.
        :type accept_vpc_info: :class:`huaweicloudsdkvpc.v2.VpcInfo`
        """
        self._accept_vpc_info = accept_vpc_info

    @property
    def created_at(self):
        r"""Gets the created_at of this RejectVpcPeeringResponse.

        功能说明：资源创建UTC时间 格式：yyyy-MM-ddTHH:mm:ss

        :return: The created_at of this RejectVpcPeeringResponse.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this RejectVpcPeeringResponse.

        功能说明：资源创建UTC时间 格式：yyyy-MM-ddTHH:mm:ss

        :param created_at: The created_at of this RejectVpcPeeringResponse.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this RejectVpcPeeringResponse.

        功能说明：资源更新UTC时间 格式：yyyy-MM-ddTHH:mm:ss

        :return: The updated_at of this RejectVpcPeeringResponse.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this RejectVpcPeeringResponse.

        功能说明：资源更新UTC时间 格式：yyyy-MM-ddTHH:mm:ss

        :param updated_at: The updated_at of this RejectVpcPeeringResponse.
        :type updated_at: datetime
        """
        self._updated_at = updated_at

    @property
    def description(self):
        r"""Gets the description of this RejectVpcPeeringResponse.

        对等连接描述

        :return: The description of this RejectVpcPeeringResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this RejectVpcPeeringResponse.

        对等连接描述

        :param description: The description of this RejectVpcPeeringResponse.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, RejectVpcPeeringResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
