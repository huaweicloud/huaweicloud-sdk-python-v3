# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AssociateInstanceGlobalEipRequestBodyGlobalEipGcBandwidthInfo:

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
        'type': 'str',
        'enterprise_project_id': 'str',
        'charge_mode': 'str',
        'bandwidth': 'int',
        'size': 'int',
        'local_area': 'str',
        'remote_area': 'str',
        'tags': 'list[AssociateInstanceGlobalEipRequestBodyGlobalEipGcBandwidthInfoTags]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'type': 'type',
        'enterprise_project_id': 'enterprise_project_id',
        'charge_mode': 'charge_mode',
        'bandwidth': 'bandwidth',
        'size': 'size',
        'local_area': 'local_area',
        'remote_area': 'remote_area',
        'tags': 'tags'
    }

    def __init__(self, id=None, name=None, description=None, type=None, enterprise_project_id=None, charge_mode=None, bandwidth=None, size=None, local_area=None, remote_area=None, tags=None):
        """AssociateInstanceGlobalEipRequestBodyGlobalEipGcBandwidthInfo

        The model defined in huaweicloud sdk

        :param id: ID
        :type id: str
        :param name: 资源名称
        :type name: str
        :param description: 
        :type description: str
        :param type: 
        :type type: str
        :param enterprise_project_id: 资源的企业项目id
        :type enterprise_project_id: str
        :param charge_mode: 计费模式
        :type charge_mode: str
        :param bandwidth: 
        :type bandwidth: int
        :param size: 大小
        :type size: int
        :param local_area: 骨干带宽的两端之一：A点
        :type local_area: str
        :param remote_area: 骨干带宽的两端之一：B点
        :type remote_area: str
        :param tags: 全域弹性公网IP标签
        :type tags: list[:class:`huaweicloudsdkgeip.v3.AssociateInstanceGlobalEipRequestBodyGlobalEipGcBandwidthInfoTags`]
        """
        
        

        self._id = None
        self._name = None
        self._description = None
        self._type = None
        self._enterprise_project_id = None
        self._charge_mode = None
        self._bandwidth = None
        self._size = None
        self._local_area = None
        self._remote_area = None
        self._tags = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if type is not None:
            self.type = type
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if charge_mode is not None:
            self.charge_mode = charge_mode
        if bandwidth is not None:
            self.bandwidth = bandwidth
        if size is not None:
            self.size = size
        if local_area is not None:
            self.local_area = local_area
        if remote_area is not None:
            self.remote_area = remote_area
        if tags is not None:
            self.tags = tags

    @property
    def id(self):
        """Gets the id of this AssociateInstanceGlobalEipRequestBodyGlobalEipGcBandwidthInfo.

        ID

        :return: The id of this AssociateInstanceGlobalEipRequestBodyGlobalEipGcBandwidthInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AssociateInstanceGlobalEipRequestBodyGlobalEipGcBandwidthInfo.

        ID

        :param id: The id of this AssociateInstanceGlobalEipRequestBodyGlobalEipGcBandwidthInfo.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this AssociateInstanceGlobalEipRequestBodyGlobalEipGcBandwidthInfo.

        资源名称

        :return: The name of this AssociateInstanceGlobalEipRequestBodyGlobalEipGcBandwidthInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AssociateInstanceGlobalEipRequestBodyGlobalEipGcBandwidthInfo.

        资源名称

        :param name: The name of this AssociateInstanceGlobalEipRequestBodyGlobalEipGcBandwidthInfo.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this AssociateInstanceGlobalEipRequestBodyGlobalEipGcBandwidthInfo.

        :return: The description of this AssociateInstanceGlobalEipRequestBodyGlobalEipGcBandwidthInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AssociateInstanceGlobalEipRequestBodyGlobalEipGcBandwidthInfo.

        :param description: The description of this AssociateInstanceGlobalEipRequestBodyGlobalEipGcBandwidthInfo.
        :type description: str
        """
        self._description = description

    @property
    def type(self):
        """Gets the type of this AssociateInstanceGlobalEipRequestBodyGlobalEipGcBandwidthInfo.

        :return: The type of this AssociateInstanceGlobalEipRequestBodyGlobalEipGcBandwidthInfo.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this AssociateInstanceGlobalEipRequestBodyGlobalEipGcBandwidthInfo.

        :param type: The type of this AssociateInstanceGlobalEipRequestBodyGlobalEipGcBandwidthInfo.
        :type type: str
        """
        self._type = type

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this AssociateInstanceGlobalEipRequestBodyGlobalEipGcBandwidthInfo.

        资源的企业项目id

        :return: The enterprise_project_id of this AssociateInstanceGlobalEipRequestBodyGlobalEipGcBandwidthInfo.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this AssociateInstanceGlobalEipRequestBodyGlobalEipGcBandwidthInfo.

        资源的企业项目id

        :param enterprise_project_id: The enterprise_project_id of this AssociateInstanceGlobalEipRequestBodyGlobalEipGcBandwidthInfo.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def charge_mode(self):
        """Gets the charge_mode of this AssociateInstanceGlobalEipRequestBodyGlobalEipGcBandwidthInfo.

        计费模式

        :return: The charge_mode of this AssociateInstanceGlobalEipRequestBodyGlobalEipGcBandwidthInfo.
        :rtype: str
        """
        return self._charge_mode

    @charge_mode.setter
    def charge_mode(self, charge_mode):
        """Sets the charge_mode of this AssociateInstanceGlobalEipRequestBodyGlobalEipGcBandwidthInfo.

        计费模式

        :param charge_mode: The charge_mode of this AssociateInstanceGlobalEipRequestBodyGlobalEipGcBandwidthInfo.
        :type charge_mode: str
        """
        self._charge_mode = charge_mode

    @property
    def bandwidth(self):
        """Gets the bandwidth of this AssociateInstanceGlobalEipRequestBodyGlobalEipGcBandwidthInfo.

        :return: The bandwidth of this AssociateInstanceGlobalEipRequestBodyGlobalEipGcBandwidthInfo.
        :rtype: int
        """
        return self._bandwidth

    @bandwidth.setter
    def bandwidth(self, bandwidth):
        """Sets the bandwidth of this AssociateInstanceGlobalEipRequestBodyGlobalEipGcBandwidthInfo.

        :param bandwidth: The bandwidth of this AssociateInstanceGlobalEipRequestBodyGlobalEipGcBandwidthInfo.
        :type bandwidth: int
        """
        self._bandwidth = bandwidth

    @property
    def size(self):
        """Gets the size of this AssociateInstanceGlobalEipRequestBodyGlobalEipGcBandwidthInfo.

        大小

        :return: The size of this AssociateInstanceGlobalEipRequestBodyGlobalEipGcBandwidthInfo.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this AssociateInstanceGlobalEipRequestBodyGlobalEipGcBandwidthInfo.

        大小

        :param size: The size of this AssociateInstanceGlobalEipRequestBodyGlobalEipGcBandwidthInfo.
        :type size: int
        """
        self._size = size

    @property
    def local_area(self):
        """Gets the local_area of this AssociateInstanceGlobalEipRequestBodyGlobalEipGcBandwidthInfo.

        骨干带宽的两端之一：A点

        :return: The local_area of this AssociateInstanceGlobalEipRequestBodyGlobalEipGcBandwidthInfo.
        :rtype: str
        """
        return self._local_area

    @local_area.setter
    def local_area(self, local_area):
        """Sets the local_area of this AssociateInstanceGlobalEipRequestBodyGlobalEipGcBandwidthInfo.

        骨干带宽的两端之一：A点

        :param local_area: The local_area of this AssociateInstanceGlobalEipRequestBodyGlobalEipGcBandwidthInfo.
        :type local_area: str
        """
        self._local_area = local_area

    @property
    def remote_area(self):
        """Gets the remote_area of this AssociateInstanceGlobalEipRequestBodyGlobalEipGcBandwidthInfo.

        骨干带宽的两端之一：B点

        :return: The remote_area of this AssociateInstanceGlobalEipRequestBodyGlobalEipGcBandwidthInfo.
        :rtype: str
        """
        return self._remote_area

    @remote_area.setter
    def remote_area(self, remote_area):
        """Sets the remote_area of this AssociateInstanceGlobalEipRequestBodyGlobalEipGcBandwidthInfo.

        骨干带宽的两端之一：B点

        :param remote_area: The remote_area of this AssociateInstanceGlobalEipRequestBodyGlobalEipGcBandwidthInfo.
        :type remote_area: str
        """
        self._remote_area = remote_area

    @property
    def tags(self):
        """Gets the tags of this AssociateInstanceGlobalEipRequestBodyGlobalEipGcBandwidthInfo.

        全域弹性公网IP标签

        :return: The tags of this AssociateInstanceGlobalEipRequestBodyGlobalEipGcBandwidthInfo.
        :rtype: list[:class:`huaweicloudsdkgeip.v3.AssociateInstanceGlobalEipRequestBodyGlobalEipGcBandwidthInfoTags`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this AssociateInstanceGlobalEipRequestBodyGlobalEipGcBandwidthInfo.

        全域弹性公网IP标签

        :param tags: The tags of this AssociateInstanceGlobalEipRequestBodyGlobalEipGcBandwidthInfo.
        :type tags: list[:class:`huaweicloudsdkgeip.v3.AssociateInstanceGlobalEipRequestBodyGlobalEipGcBandwidthInfoTags`]
        """
        self._tags = tags

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
        if not isinstance(other, AssociateInstanceGlobalEipRequestBodyGlobalEipGcBandwidthInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
