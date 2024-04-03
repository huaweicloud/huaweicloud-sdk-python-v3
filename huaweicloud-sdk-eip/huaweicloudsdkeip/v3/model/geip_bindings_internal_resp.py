# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GeipBindingsInternalResp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'geip_id': 'str',
        'geip_ip_address': 'str',
        'public_border_group': 'str',
        'created_at': 'str',
        'updated_at': 'str',
        'instance_type': 'str',
        'instance_id': 'str',
        'gcbandwidth': 'BackboneBandwidthResp',
        'vnic': 'InstanceVnicResp',
        'vn_list': 'list[InstancevirtualListResp]'
    }

    attribute_map = {
        'geip_id': 'geip_id',
        'geip_ip_address': 'geip_ip_address',
        'public_border_group': 'public_border_group',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'instance_type': 'instance_type',
        'instance_id': 'instance_id',
        'gcbandwidth': 'gcbandwidth',
        'vnic': 'vnic',
        'vn_list': 'vn_list'
    }

    def __init__(self, geip_id=None, geip_ip_address=None, public_border_group=None, created_at=None, updated_at=None, instance_type=None, instance_id=None, gcbandwidth=None, vnic=None, vn_list=None):
        """GeipBindingsInternalResp

        The model defined in huaweicloud sdk

        :param geip_id: GEIP的uuid
        :type geip_id: str
        :param geip_ip_address: GEIP的ip地址
        :type geip_ip_address: str
        :param public_border_group: 中心站点or边缘站点，默认展示
        :type public_border_group: str
        :param created_at: 创建时间
        :type created_at: str
        :param updated_at: 更新时间
        :type updated_at: str
        :param instance_type: 绑定实例的类型
        :type instance_type: str
        :param instance_id: 绑定实例的id
        :type instance_id: str
        :param gcbandwidth: 
        :type gcbandwidth: :class:`huaweicloudsdkeip.v3.BackboneBandwidthResp`
        :param vnic: 
        :type vnic: :class:`huaweicloudsdkeip.v3.InstanceVnicResp`
        :param vn_list: GEIP实例的vn信息
        :type vn_list: list[:class:`huaweicloudsdkeip.v3.InstancevirtualListResp`]
        """
        
        

        self._geip_id = None
        self._geip_ip_address = None
        self._public_border_group = None
        self._created_at = None
        self._updated_at = None
        self._instance_type = None
        self._instance_id = None
        self._gcbandwidth = None
        self._vnic = None
        self._vn_list = None
        self.discriminator = None

        if geip_id is not None:
            self.geip_id = geip_id
        if geip_ip_address is not None:
            self.geip_ip_address = geip_ip_address
        if public_border_group is not None:
            self.public_border_group = public_border_group
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if instance_type is not None:
            self.instance_type = instance_type
        if instance_id is not None:
            self.instance_id = instance_id
        if gcbandwidth is not None:
            self.gcbandwidth = gcbandwidth
        if vnic is not None:
            self.vnic = vnic
        if vn_list is not None:
            self.vn_list = vn_list

    @property
    def geip_id(self):
        """Gets the geip_id of this GeipBindingsInternalResp.

        GEIP的uuid

        :return: The geip_id of this GeipBindingsInternalResp.
        :rtype: str
        """
        return self._geip_id

    @geip_id.setter
    def geip_id(self, geip_id):
        """Sets the geip_id of this GeipBindingsInternalResp.

        GEIP的uuid

        :param geip_id: The geip_id of this GeipBindingsInternalResp.
        :type geip_id: str
        """
        self._geip_id = geip_id

    @property
    def geip_ip_address(self):
        """Gets the geip_ip_address of this GeipBindingsInternalResp.

        GEIP的ip地址

        :return: The geip_ip_address of this GeipBindingsInternalResp.
        :rtype: str
        """
        return self._geip_ip_address

    @geip_ip_address.setter
    def geip_ip_address(self, geip_ip_address):
        """Sets the geip_ip_address of this GeipBindingsInternalResp.

        GEIP的ip地址

        :param geip_ip_address: The geip_ip_address of this GeipBindingsInternalResp.
        :type geip_ip_address: str
        """
        self._geip_ip_address = geip_ip_address

    @property
    def public_border_group(self):
        """Gets the public_border_group of this GeipBindingsInternalResp.

        中心站点or边缘站点，默认展示

        :return: The public_border_group of this GeipBindingsInternalResp.
        :rtype: str
        """
        return self._public_border_group

    @public_border_group.setter
    def public_border_group(self, public_border_group):
        """Sets the public_border_group of this GeipBindingsInternalResp.

        中心站点or边缘站点，默认展示

        :param public_border_group: The public_border_group of this GeipBindingsInternalResp.
        :type public_border_group: str
        """
        self._public_border_group = public_border_group

    @property
    def created_at(self):
        """Gets the created_at of this GeipBindingsInternalResp.

        创建时间

        :return: The created_at of this GeipBindingsInternalResp.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this GeipBindingsInternalResp.

        创建时间

        :param created_at: The created_at of this GeipBindingsInternalResp.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this GeipBindingsInternalResp.

        更新时间

        :return: The updated_at of this GeipBindingsInternalResp.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this GeipBindingsInternalResp.

        更新时间

        :param updated_at: The updated_at of this GeipBindingsInternalResp.
        :type updated_at: str
        """
        self._updated_at = updated_at

    @property
    def instance_type(self):
        """Gets the instance_type of this GeipBindingsInternalResp.

        绑定实例的类型

        :return: The instance_type of this GeipBindingsInternalResp.
        :rtype: str
        """
        return self._instance_type

    @instance_type.setter
    def instance_type(self, instance_type):
        """Sets the instance_type of this GeipBindingsInternalResp.

        绑定实例的类型

        :param instance_type: The instance_type of this GeipBindingsInternalResp.
        :type instance_type: str
        """
        self._instance_type = instance_type

    @property
    def instance_id(self):
        """Gets the instance_id of this GeipBindingsInternalResp.

        绑定实例的id

        :return: The instance_id of this GeipBindingsInternalResp.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this GeipBindingsInternalResp.

        绑定实例的id

        :param instance_id: The instance_id of this GeipBindingsInternalResp.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def gcbandwidth(self):
        """Gets the gcbandwidth of this GeipBindingsInternalResp.

        :return: The gcbandwidth of this GeipBindingsInternalResp.
        :rtype: :class:`huaweicloudsdkeip.v3.BackboneBandwidthResp`
        """
        return self._gcbandwidth

    @gcbandwidth.setter
    def gcbandwidth(self, gcbandwidth):
        """Sets the gcbandwidth of this GeipBindingsInternalResp.

        :param gcbandwidth: The gcbandwidth of this GeipBindingsInternalResp.
        :type gcbandwidth: :class:`huaweicloudsdkeip.v3.BackboneBandwidthResp`
        """
        self._gcbandwidth = gcbandwidth

    @property
    def vnic(self):
        """Gets the vnic of this GeipBindingsInternalResp.

        :return: The vnic of this GeipBindingsInternalResp.
        :rtype: :class:`huaweicloudsdkeip.v3.InstanceVnicResp`
        """
        return self._vnic

    @vnic.setter
    def vnic(self, vnic):
        """Sets the vnic of this GeipBindingsInternalResp.

        :param vnic: The vnic of this GeipBindingsInternalResp.
        :type vnic: :class:`huaweicloudsdkeip.v3.InstanceVnicResp`
        """
        self._vnic = vnic

    @property
    def vn_list(self):
        """Gets the vn_list of this GeipBindingsInternalResp.

        GEIP实例的vn信息

        :return: The vn_list of this GeipBindingsInternalResp.
        :rtype: list[:class:`huaweicloudsdkeip.v3.InstancevirtualListResp`]
        """
        return self._vn_list

    @vn_list.setter
    def vn_list(self, vn_list):
        """Sets the vn_list of this GeipBindingsInternalResp.

        GEIP实例的vn信息

        :param vn_list: The vn_list of this GeipBindingsInternalResp.
        :type vn_list: list[:class:`huaweicloudsdkeip.v3.InstancevirtualListResp`]
        """
        self._vn_list = vn_list

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
        if not isinstance(other, GeipBindingsInternalResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
