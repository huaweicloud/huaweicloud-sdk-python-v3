# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EndpointGroupDetail:

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
        'description': 'str',
        'status': 'ConfigStatus',
        'traffic_dial_percentage': 'int',
        'region_id': 'str',
        'listeners': 'list[Id]',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'domain_id': 'str',
        'frozen_info': 'FrozenInfo'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'status': 'status',
        'traffic_dial_percentage': 'traffic_dial_percentage',
        'region_id': 'region_id',
        'listeners': 'listeners',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'domain_id': 'domain_id',
        'frozen_info': 'frozen_info'
    }

    def __init__(self, id=None, name=None, description=None, status=None, traffic_dial_percentage=None, region_id=None, listeners=None, created_at=None, updated_at=None, domain_id=None, frozen_info=None):
        r"""EndpointGroupDetail

        The model defined in huaweicloud sdk

        :param id: 终端节点组ID。
        :type id: str
        :param name: 终端节点组名称，取值范围：1~64个字符之间，只能由数字、字母、中划线和中文组成。
        :type name: str
        :param description: 终端节点组描述信息，取值范围：0~255个字符之间，禁止输入字符：&lt;&gt;。
        :type description: str
        :param status: 
        :type status: :class:`huaweicloudsdkga.v1.ConfigStatus`
        :param traffic_dial_percentage: 流量拨分到此组的百分比。
        :type traffic_dial_percentage: int
        :param region_id: 终端节点组所属区域ID。
        :type region_id: str
        :param listeners: 关联监听器列表。
        :type listeners: list[:class:`huaweicloudsdkga.v1.Id`]
        :param created_at: 创建时间。
        :type created_at: datetime
        :param updated_at: 更新时间。
        :type updated_at: datetime
        :param domain_id: 租户ID。
        :type domain_id: str
        :param frozen_info: 
        :type frozen_info: :class:`huaweicloudsdkga.v1.FrozenInfo`
        """
        
        

        self._id = None
        self._name = None
        self._description = None
        self._status = None
        self._traffic_dial_percentage = None
        self._region_id = None
        self._listeners = None
        self._created_at = None
        self._updated_at = None
        self._domain_id = None
        self._frozen_info = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if status is not None:
            self.status = status
        if traffic_dial_percentage is not None:
            self.traffic_dial_percentage = traffic_dial_percentage
        if region_id is not None:
            self.region_id = region_id
        if listeners is not None:
            self.listeners = listeners
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if domain_id is not None:
            self.domain_id = domain_id
        if frozen_info is not None:
            self.frozen_info = frozen_info

    @property
    def id(self):
        r"""Gets the id of this EndpointGroupDetail.

        终端节点组ID。

        :return: The id of this EndpointGroupDetail.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this EndpointGroupDetail.

        终端节点组ID。

        :param id: The id of this EndpointGroupDetail.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this EndpointGroupDetail.

        终端节点组名称，取值范围：1~64个字符之间，只能由数字、字母、中划线和中文组成。

        :return: The name of this EndpointGroupDetail.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this EndpointGroupDetail.

        终端节点组名称，取值范围：1~64个字符之间，只能由数字、字母、中划线和中文组成。

        :param name: The name of this EndpointGroupDetail.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this EndpointGroupDetail.

        终端节点组描述信息，取值范围：0~255个字符之间，禁止输入字符：<>。

        :return: The description of this EndpointGroupDetail.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this EndpointGroupDetail.

        终端节点组描述信息，取值范围：0~255个字符之间，禁止输入字符：<>。

        :param description: The description of this EndpointGroupDetail.
        :type description: str
        """
        self._description = description

    @property
    def status(self):
        r"""Gets the status of this EndpointGroupDetail.

        :return: The status of this EndpointGroupDetail.
        :rtype: :class:`huaweicloudsdkga.v1.ConfigStatus`
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this EndpointGroupDetail.

        :param status: The status of this EndpointGroupDetail.
        :type status: :class:`huaweicloudsdkga.v1.ConfigStatus`
        """
        self._status = status

    @property
    def traffic_dial_percentage(self):
        r"""Gets the traffic_dial_percentage of this EndpointGroupDetail.

        流量拨分到此组的百分比。

        :return: The traffic_dial_percentage of this EndpointGroupDetail.
        :rtype: int
        """
        return self._traffic_dial_percentage

    @traffic_dial_percentage.setter
    def traffic_dial_percentage(self, traffic_dial_percentage):
        r"""Sets the traffic_dial_percentage of this EndpointGroupDetail.

        流量拨分到此组的百分比。

        :param traffic_dial_percentage: The traffic_dial_percentage of this EndpointGroupDetail.
        :type traffic_dial_percentage: int
        """
        self._traffic_dial_percentage = traffic_dial_percentage

    @property
    def region_id(self):
        r"""Gets the region_id of this EndpointGroupDetail.

        终端节点组所属区域ID。

        :return: The region_id of this EndpointGroupDetail.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        r"""Sets the region_id of this EndpointGroupDetail.

        终端节点组所属区域ID。

        :param region_id: The region_id of this EndpointGroupDetail.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def listeners(self):
        r"""Gets the listeners of this EndpointGroupDetail.

        关联监听器列表。

        :return: The listeners of this EndpointGroupDetail.
        :rtype: list[:class:`huaweicloudsdkga.v1.Id`]
        """
        return self._listeners

    @listeners.setter
    def listeners(self, listeners):
        r"""Sets the listeners of this EndpointGroupDetail.

        关联监听器列表。

        :param listeners: The listeners of this EndpointGroupDetail.
        :type listeners: list[:class:`huaweicloudsdkga.v1.Id`]
        """
        self._listeners = listeners

    @property
    def created_at(self):
        r"""Gets the created_at of this EndpointGroupDetail.

        创建时间。

        :return: The created_at of this EndpointGroupDetail.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this EndpointGroupDetail.

        创建时间。

        :param created_at: The created_at of this EndpointGroupDetail.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this EndpointGroupDetail.

        更新时间。

        :return: The updated_at of this EndpointGroupDetail.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this EndpointGroupDetail.

        更新时间。

        :param updated_at: The updated_at of this EndpointGroupDetail.
        :type updated_at: datetime
        """
        self._updated_at = updated_at

    @property
    def domain_id(self):
        r"""Gets the domain_id of this EndpointGroupDetail.

        租户ID。

        :return: The domain_id of this EndpointGroupDetail.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this EndpointGroupDetail.

        租户ID。

        :param domain_id: The domain_id of this EndpointGroupDetail.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def frozen_info(self):
        r"""Gets the frozen_info of this EndpointGroupDetail.

        :return: The frozen_info of this EndpointGroupDetail.
        :rtype: :class:`huaweicloudsdkga.v1.FrozenInfo`
        """
        return self._frozen_info

    @frozen_info.setter
    def frozen_info(self, frozen_info):
        r"""Sets the frozen_info of this EndpointGroupDetail.

        :param frozen_info: The frozen_info of this EndpointGroupDetail.
        :type frozen_info: :class:`huaweicloudsdkga.v1.FrozenInfo`
        """
        self._frozen_info = frozen_info

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
        if not isinstance(other, EndpointGroupDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
