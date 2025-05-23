# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ClusterListInstances:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status': 'str',
        'type': 'str',
        'id': 'str',
        'name': 'str',
        'spec_code': 'str',
        'az_code': 'str',
        'ip': 'str',
        'volume': 'ClusterVolumeRsp',
        'resource_id': 'str'
    }

    attribute_map = {
        'status': 'status',
        'type': 'type',
        'id': 'id',
        'name': 'name',
        'spec_code': 'specCode',
        'az_code': 'azCode',
        'ip': 'ip',
        'volume': 'volume',
        'resource_id': 'resourceId'
    }

    def __init__(self, status=None, type=None, id=None, name=None, spec_code=None, az_code=None, ip=None, volume=None, resource_id=None):
        r"""ClusterListInstances

        The model defined in huaweicloud sdk

        :param status: 节点状态值。  - 100：创建中。 - 200：可用。 - 303：不可用，如创建失败。
        :type status: str
        :param type: 当前节点的类型。
        :type type: str
        :param id: 实例ID。
        :type id: str
        :param name: 实例名字。
        :type name: str
        :param spec_code: 节点规格名称。
        :type spec_code: str
        :param az_code: 节点所属AZ信息。
        :type az_code: str
        :param ip: 实例ip信息。
        :type ip: str
        :param volume: 
        :type volume: :class:`huaweicloudsdkcss.v1.ClusterVolumeRsp`
        :param resource_id: 该实例对应的资源Id。
        :type resource_id: str
        """
        
        

        self._status = None
        self._type = None
        self._id = None
        self._name = None
        self._spec_code = None
        self._az_code = None
        self._ip = None
        self._volume = None
        self._resource_id = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if type is not None:
            self.type = type
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if spec_code is not None:
            self.spec_code = spec_code
        if az_code is not None:
            self.az_code = az_code
        if ip is not None:
            self.ip = ip
        if volume is not None:
            self.volume = volume
        if resource_id is not None:
            self.resource_id = resource_id

    @property
    def status(self):
        r"""Gets the status of this ClusterListInstances.

        节点状态值。  - 100：创建中。 - 200：可用。 - 303：不可用，如创建失败。

        :return: The status of this ClusterListInstances.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ClusterListInstances.

        节点状态值。  - 100：创建中。 - 200：可用。 - 303：不可用，如创建失败。

        :param status: The status of this ClusterListInstances.
        :type status: str
        """
        self._status = status

    @property
    def type(self):
        r"""Gets the type of this ClusterListInstances.

        当前节点的类型。

        :return: The type of this ClusterListInstances.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ClusterListInstances.

        当前节点的类型。

        :param type: The type of this ClusterListInstances.
        :type type: str
        """
        self._type = type

    @property
    def id(self):
        r"""Gets the id of this ClusterListInstances.

        实例ID。

        :return: The id of this ClusterListInstances.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ClusterListInstances.

        实例ID。

        :param id: The id of this ClusterListInstances.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ClusterListInstances.

        实例名字。

        :return: The name of this ClusterListInstances.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ClusterListInstances.

        实例名字。

        :param name: The name of this ClusterListInstances.
        :type name: str
        """
        self._name = name

    @property
    def spec_code(self):
        r"""Gets the spec_code of this ClusterListInstances.

        节点规格名称。

        :return: The spec_code of this ClusterListInstances.
        :rtype: str
        """
        return self._spec_code

    @spec_code.setter
    def spec_code(self, spec_code):
        r"""Sets the spec_code of this ClusterListInstances.

        节点规格名称。

        :param spec_code: The spec_code of this ClusterListInstances.
        :type spec_code: str
        """
        self._spec_code = spec_code

    @property
    def az_code(self):
        r"""Gets the az_code of this ClusterListInstances.

        节点所属AZ信息。

        :return: The az_code of this ClusterListInstances.
        :rtype: str
        """
        return self._az_code

    @az_code.setter
    def az_code(self, az_code):
        r"""Sets the az_code of this ClusterListInstances.

        节点所属AZ信息。

        :param az_code: The az_code of this ClusterListInstances.
        :type az_code: str
        """
        self._az_code = az_code

    @property
    def ip(self):
        r"""Gets the ip of this ClusterListInstances.

        实例ip信息。

        :return: The ip of this ClusterListInstances.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        r"""Sets the ip of this ClusterListInstances.

        实例ip信息。

        :param ip: The ip of this ClusterListInstances.
        :type ip: str
        """
        self._ip = ip

    @property
    def volume(self):
        r"""Gets the volume of this ClusterListInstances.

        :return: The volume of this ClusterListInstances.
        :rtype: :class:`huaweicloudsdkcss.v1.ClusterVolumeRsp`
        """
        return self._volume

    @volume.setter
    def volume(self, volume):
        r"""Sets the volume of this ClusterListInstances.

        :param volume: The volume of this ClusterListInstances.
        :type volume: :class:`huaweicloudsdkcss.v1.ClusterVolumeRsp`
        """
        self._volume = volume

    @property
    def resource_id(self):
        r"""Gets the resource_id of this ClusterListInstances.

        该实例对应的资源Id。

        :return: The resource_id of this ClusterListInstances.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this ClusterListInstances.

        该实例对应的资源Id。

        :param resource_id: The resource_id of this ClusterListInstances.
        :type resource_id: str
        """
        self._resource_id = resource_id

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
        if not isinstance(other, ClusterListInstances):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
