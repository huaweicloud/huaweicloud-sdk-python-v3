# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSupportRegions:

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
        'instance_type': 'str',
        'access_site': 'str',
        'region_id': 'str',
        'public_border_group': 'str',
        'remote_endpoint': 'str',
        'status': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'instance_type': 'instance_type',
        'access_site': 'access_site',
        'region_id': 'region_id',
        'public_border_group': 'public_border_group',
        'remote_endpoint': 'remote_endpoint',
        'status': 'status',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, id=None, instance_type=None, access_site=None, region_id=None, public_border_group=None, remote_endpoint=None, status=None, created_at=None, updated_at=None):
        r"""ListSupportRegions

        The model defined in huaweicloud sdk

        :param id: 域弹性公网IP支持绑定的Region限制的ID
        :type id: str
        :param instance_type: 支持绑定的实例类型
        :type instance_type: str
        :param access_site: 接入点信息
        :type access_site: str
        :param region_id: region_id
        :type region_id: str
        :param public_border_group: - 功能说明：表示中心站点资源或者边缘站点资源 - 取值范围：center、边缘站点名称
        :type public_border_group: str
        :param remote_endpoint: remote_endpoint
        :type remote_endpoint: str
        :param status: 状态
        :type status: str
        :param created_at: 创建时间
        :type created_at: datetime
        :param updated_at: 更新时间
        :type updated_at: datetime
        """
        
        

        self._id = None
        self._instance_type = None
        self._access_site = None
        self._region_id = None
        self._public_border_group = None
        self._remote_endpoint = None
        self._status = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if instance_type is not None:
            self.instance_type = instance_type
        if access_site is not None:
            self.access_site = access_site
        if region_id is not None:
            self.region_id = region_id
        if public_border_group is not None:
            self.public_border_group = public_border_group
        if remote_endpoint is not None:
            self.remote_endpoint = remote_endpoint
        if status is not None:
            self.status = status
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def id(self):
        r"""Gets the id of this ListSupportRegions.

        域弹性公网IP支持绑定的Region限制的ID

        :return: The id of this ListSupportRegions.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ListSupportRegions.

        域弹性公网IP支持绑定的Region限制的ID

        :param id: The id of this ListSupportRegions.
        :type id: str
        """
        self._id = id

    @property
    def instance_type(self):
        r"""Gets the instance_type of this ListSupportRegions.

        支持绑定的实例类型

        :return: The instance_type of this ListSupportRegions.
        :rtype: str
        """
        return self._instance_type

    @instance_type.setter
    def instance_type(self, instance_type):
        r"""Sets the instance_type of this ListSupportRegions.

        支持绑定的实例类型

        :param instance_type: The instance_type of this ListSupportRegions.
        :type instance_type: str
        """
        self._instance_type = instance_type

    @property
    def access_site(self):
        r"""Gets the access_site of this ListSupportRegions.

        接入点信息

        :return: The access_site of this ListSupportRegions.
        :rtype: str
        """
        return self._access_site

    @access_site.setter
    def access_site(self, access_site):
        r"""Sets the access_site of this ListSupportRegions.

        接入点信息

        :param access_site: The access_site of this ListSupportRegions.
        :type access_site: str
        """
        self._access_site = access_site

    @property
    def region_id(self):
        r"""Gets the region_id of this ListSupportRegions.

        region_id

        :return: The region_id of this ListSupportRegions.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        r"""Sets the region_id of this ListSupportRegions.

        region_id

        :param region_id: The region_id of this ListSupportRegions.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def public_border_group(self):
        r"""Gets the public_border_group of this ListSupportRegions.

        - 功能说明：表示中心站点资源或者边缘站点资源 - 取值范围：center、边缘站点名称

        :return: The public_border_group of this ListSupportRegions.
        :rtype: str
        """
        return self._public_border_group

    @public_border_group.setter
    def public_border_group(self, public_border_group):
        r"""Sets the public_border_group of this ListSupportRegions.

        - 功能说明：表示中心站点资源或者边缘站点资源 - 取值范围：center、边缘站点名称

        :param public_border_group: The public_border_group of this ListSupportRegions.
        :type public_border_group: str
        """
        self._public_border_group = public_border_group

    @property
    def remote_endpoint(self):
        r"""Gets the remote_endpoint of this ListSupportRegions.

        remote_endpoint

        :return: The remote_endpoint of this ListSupportRegions.
        :rtype: str
        """
        return self._remote_endpoint

    @remote_endpoint.setter
    def remote_endpoint(self, remote_endpoint):
        r"""Sets the remote_endpoint of this ListSupportRegions.

        remote_endpoint

        :param remote_endpoint: The remote_endpoint of this ListSupportRegions.
        :type remote_endpoint: str
        """
        self._remote_endpoint = remote_endpoint

    @property
    def status(self):
        r"""Gets the status of this ListSupportRegions.

        状态

        :return: The status of this ListSupportRegions.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListSupportRegions.

        状态

        :param status: The status of this ListSupportRegions.
        :type status: str
        """
        self._status = status

    @property
    def created_at(self):
        r"""Gets the created_at of this ListSupportRegions.

        创建时间

        :return: The created_at of this ListSupportRegions.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this ListSupportRegions.

        创建时间

        :param created_at: The created_at of this ListSupportRegions.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this ListSupportRegions.

        更新时间

        :return: The updated_at of this ListSupportRegions.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this ListSupportRegions.

        更新时间

        :param updated_at: The updated_at of this ListSupportRegions.
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
        if not isinstance(other, ListSupportRegions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
