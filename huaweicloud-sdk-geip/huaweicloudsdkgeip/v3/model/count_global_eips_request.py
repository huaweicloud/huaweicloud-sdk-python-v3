# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CountGlobalEipsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'list[str]',
        'internet_bandwidth_id': 'list[str]',
        'name': 'list[str]',
        'name_like': 'str',
        'access_site': 'list[str]',
        'geip_pool_name': 'list[str]',
        'isp': 'list[str]',
        'ip_version': 'list[int]',
        'ip_address': 'list[str]',
        'ipv6_address': 'list[str]',
        'freezen': 'list[bool]',
        'polluted': 'list[bool]',
        'internet_bandwidth_is_null': 'list[bool]',
        'gcb_bandwidth_is_null': 'list[bool]',
        'status': 'list[str]',
        'associate_instance_info_region': 'list[str]',
        'associate_instance_info_public_border_group': 'list[str]',
        'associate_instance_info_instance_site': 'list[str]',
        'associate_instance_info_instance_type': 'list[str]',
        'associate_instance_info_instance_id': 'list[str]',
        'associate_instance_info_project_id': 'list[str]',
        'enterprise_project_id': 'list[str]',
        'tags': 'list[str]'
    }

    attribute_map = {
        'id': 'id',
        'internet_bandwidth_id': 'internet_bandwidth_id',
        'name': 'name',
        'name_like': 'name_like',
        'access_site': 'access_site',
        'geip_pool_name': 'geip_pool_name',
        'isp': 'isp',
        'ip_version': 'ip_version',
        'ip_address': 'ip_address',
        'ipv6_address': 'ipv6_address',
        'freezen': 'freezen',
        'polluted': 'polluted',
        'internet_bandwidth_is_null': 'internet_bandwidth_is_null',
        'gcb_bandwidth_is_null': 'gcb_bandwidth_is_null',
        'status': 'status',
        'associate_instance_info_region': 'associate_instance_info.region',
        'associate_instance_info_public_border_group': 'associate_instance_info.public_border_group',
        'associate_instance_info_instance_site': 'associate_instance_info.instance_site',
        'associate_instance_info_instance_type': 'associate_instance_info.instance_type',
        'associate_instance_info_instance_id': 'associate_instance_info.instance_id',
        'associate_instance_info_project_id': 'associate_instance_info.project_id',
        'enterprise_project_id': 'enterprise_project_id',
        'tags': 'tags'
    }

    def __init__(self, id=None, internet_bandwidth_id=None, name=None, name_like=None, access_site=None, geip_pool_name=None, isp=None, ip_version=None, ip_address=None, ipv6_address=None, freezen=None, polluted=None, internet_bandwidth_is_null=None, gcb_bandwidth_is_null=None, status=None, associate_instance_info_region=None, associate_instance_info_public_border_group=None, associate_instance_info_instance_site=None, associate_instance_info_instance_type=None, associate_instance_info_instance_id=None, associate_instance_info_project_id=None, enterprise_project_id=None, tags=None):
        r"""CountGlobalEipsRequest

        The model defined in huaweicloud sdk

        :param id: 
        :type id: list[str]
        :param internet_bandwidth_id: 
        :type internet_bandwidth_id: list[str]
        :param name: 
        :type name: list[str]
        :param name_like: 
        :type name_like: str
        :param access_site: 
        :type access_site: list[str]
        :param geip_pool_name: 
        :type geip_pool_name: list[str]
        :param isp: 
        :type isp: list[str]
        :param ip_version: 
        :type ip_version: list[int]
        :param ip_address: 
        :type ip_address: list[str]
        :param ipv6_address: 
        :type ipv6_address: list[str]
        :param freezen: 
        :type freezen: list[bool]
        :param polluted: 
        :type polluted: list[bool]
        :param internet_bandwidth_is_null: 
        :type internet_bandwidth_is_null: list[bool]
        :param gcb_bandwidth_is_null: 
        :type gcb_bandwidth_is_null: list[bool]
        :param status: 
        :type status: list[str]
        :param associate_instance_info_region: 
        :type associate_instance_info_region: list[str]
        :param associate_instance_info_public_border_group: 
        :type associate_instance_info_public_border_group: list[str]
        :param associate_instance_info_instance_site: 
        :type associate_instance_info_instance_site: list[str]
        :param associate_instance_info_instance_type: 
        :type associate_instance_info_instance_type: list[str]
        :param associate_instance_info_instance_id: 
        :type associate_instance_info_instance_id: list[str]
        :param associate_instance_info_project_id: 
        :type associate_instance_info_project_id: list[str]
        :param enterprise_project_id: 
        :type enterprise_project_id: list[str]
        :param tags: 
        :type tags: list[str]
        """
        
        

        self._id = None
        self._internet_bandwidth_id = None
        self._name = None
        self._name_like = None
        self._access_site = None
        self._geip_pool_name = None
        self._isp = None
        self._ip_version = None
        self._ip_address = None
        self._ipv6_address = None
        self._freezen = None
        self._polluted = None
        self._internet_bandwidth_is_null = None
        self._gcb_bandwidth_is_null = None
        self._status = None
        self._associate_instance_info_region = None
        self._associate_instance_info_public_border_group = None
        self._associate_instance_info_instance_site = None
        self._associate_instance_info_instance_type = None
        self._associate_instance_info_instance_id = None
        self._associate_instance_info_project_id = None
        self._enterprise_project_id = None
        self._tags = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if internet_bandwidth_id is not None:
            self.internet_bandwidth_id = internet_bandwidth_id
        if name is not None:
            self.name = name
        if name_like is not None:
            self.name_like = name_like
        if access_site is not None:
            self.access_site = access_site
        if geip_pool_name is not None:
            self.geip_pool_name = geip_pool_name
        if isp is not None:
            self.isp = isp
        if ip_version is not None:
            self.ip_version = ip_version
        if ip_address is not None:
            self.ip_address = ip_address
        if ipv6_address is not None:
            self.ipv6_address = ipv6_address
        if freezen is not None:
            self.freezen = freezen
        if polluted is not None:
            self.polluted = polluted
        if internet_bandwidth_is_null is not None:
            self.internet_bandwidth_is_null = internet_bandwidth_is_null
        if gcb_bandwidth_is_null is not None:
            self.gcb_bandwidth_is_null = gcb_bandwidth_is_null
        if status is not None:
            self.status = status
        if associate_instance_info_region is not None:
            self.associate_instance_info_region = associate_instance_info_region
        if associate_instance_info_public_border_group is not None:
            self.associate_instance_info_public_border_group = associate_instance_info_public_border_group
        if associate_instance_info_instance_site is not None:
            self.associate_instance_info_instance_site = associate_instance_info_instance_site
        if associate_instance_info_instance_type is not None:
            self.associate_instance_info_instance_type = associate_instance_info_instance_type
        if associate_instance_info_instance_id is not None:
            self.associate_instance_info_instance_id = associate_instance_info_instance_id
        if associate_instance_info_project_id is not None:
            self.associate_instance_info_project_id = associate_instance_info_project_id
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if tags is not None:
            self.tags = tags

    @property
    def id(self):
        r"""Gets the id of this CountGlobalEipsRequest.

        :return: The id of this CountGlobalEipsRequest.
        :rtype: list[str]
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this CountGlobalEipsRequest.

        :param id: The id of this CountGlobalEipsRequest.
        :type id: list[str]
        """
        self._id = id

    @property
    def internet_bandwidth_id(self):
        r"""Gets the internet_bandwidth_id of this CountGlobalEipsRequest.

        :return: The internet_bandwidth_id of this CountGlobalEipsRequest.
        :rtype: list[str]
        """
        return self._internet_bandwidth_id

    @internet_bandwidth_id.setter
    def internet_bandwidth_id(self, internet_bandwidth_id):
        r"""Sets the internet_bandwidth_id of this CountGlobalEipsRequest.

        :param internet_bandwidth_id: The internet_bandwidth_id of this CountGlobalEipsRequest.
        :type internet_bandwidth_id: list[str]
        """
        self._internet_bandwidth_id = internet_bandwidth_id

    @property
    def name(self):
        r"""Gets the name of this CountGlobalEipsRequest.

        :return: The name of this CountGlobalEipsRequest.
        :rtype: list[str]
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CountGlobalEipsRequest.

        :param name: The name of this CountGlobalEipsRequest.
        :type name: list[str]
        """
        self._name = name

    @property
    def name_like(self):
        r"""Gets the name_like of this CountGlobalEipsRequest.

        :return: The name_like of this CountGlobalEipsRequest.
        :rtype: str
        """
        return self._name_like

    @name_like.setter
    def name_like(self, name_like):
        r"""Sets the name_like of this CountGlobalEipsRequest.

        :param name_like: The name_like of this CountGlobalEipsRequest.
        :type name_like: str
        """
        self._name_like = name_like

    @property
    def access_site(self):
        r"""Gets the access_site of this CountGlobalEipsRequest.

        :return: The access_site of this CountGlobalEipsRequest.
        :rtype: list[str]
        """
        return self._access_site

    @access_site.setter
    def access_site(self, access_site):
        r"""Sets the access_site of this CountGlobalEipsRequest.

        :param access_site: The access_site of this CountGlobalEipsRequest.
        :type access_site: list[str]
        """
        self._access_site = access_site

    @property
    def geip_pool_name(self):
        r"""Gets the geip_pool_name of this CountGlobalEipsRequest.

        :return: The geip_pool_name of this CountGlobalEipsRequest.
        :rtype: list[str]
        """
        return self._geip_pool_name

    @geip_pool_name.setter
    def geip_pool_name(self, geip_pool_name):
        r"""Sets the geip_pool_name of this CountGlobalEipsRequest.

        :param geip_pool_name: The geip_pool_name of this CountGlobalEipsRequest.
        :type geip_pool_name: list[str]
        """
        self._geip_pool_name = geip_pool_name

    @property
    def isp(self):
        r"""Gets the isp of this CountGlobalEipsRequest.

        :return: The isp of this CountGlobalEipsRequest.
        :rtype: list[str]
        """
        return self._isp

    @isp.setter
    def isp(self, isp):
        r"""Sets the isp of this CountGlobalEipsRequest.

        :param isp: The isp of this CountGlobalEipsRequest.
        :type isp: list[str]
        """
        self._isp = isp

    @property
    def ip_version(self):
        r"""Gets the ip_version of this CountGlobalEipsRequest.

        :return: The ip_version of this CountGlobalEipsRequest.
        :rtype: list[int]
        """
        return self._ip_version

    @ip_version.setter
    def ip_version(self, ip_version):
        r"""Sets the ip_version of this CountGlobalEipsRequest.

        :param ip_version: The ip_version of this CountGlobalEipsRequest.
        :type ip_version: list[int]
        """
        self._ip_version = ip_version

    @property
    def ip_address(self):
        r"""Gets the ip_address of this CountGlobalEipsRequest.

        :return: The ip_address of this CountGlobalEipsRequest.
        :rtype: list[str]
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        r"""Sets the ip_address of this CountGlobalEipsRequest.

        :param ip_address: The ip_address of this CountGlobalEipsRequest.
        :type ip_address: list[str]
        """
        self._ip_address = ip_address

    @property
    def ipv6_address(self):
        r"""Gets the ipv6_address of this CountGlobalEipsRequest.

        :return: The ipv6_address of this CountGlobalEipsRequest.
        :rtype: list[str]
        """
        return self._ipv6_address

    @ipv6_address.setter
    def ipv6_address(self, ipv6_address):
        r"""Sets the ipv6_address of this CountGlobalEipsRequest.

        :param ipv6_address: The ipv6_address of this CountGlobalEipsRequest.
        :type ipv6_address: list[str]
        """
        self._ipv6_address = ipv6_address

    @property
    def freezen(self):
        r"""Gets the freezen of this CountGlobalEipsRequest.

        :return: The freezen of this CountGlobalEipsRequest.
        :rtype: list[bool]
        """
        return self._freezen

    @freezen.setter
    def freezen(self, freezen):
        r"""Sets the freezen of this CountGlobalEipsRequest.

        :param freezen: The freezen of this CountGlobalEipsRequest.
        :type freezen: list[bool]
        """
        self._freezen = freezen

    @property
    def polluted(self):
        r"""Gets the polluted of this CountGlobalEipsRequest.

        :return: The polluted of this CountGlobalEipsRequest.
        :rtype: list[bool]
        """
        return self._polluted

    @polluted.setter
    def polluted(self, polluted):
        r"""Sets the polluted of this CountGlobalEipsRequest.

        :param polluted: The polluted of this CountGlobalEipsRequest.
        :type polluted: list[bool]
        """
        self._polluted = polluted

    @property
    def internet_bandwidth_is_null(self):
        r"""Gets the internet_bandwidth_is_null of this CountGlobalEipsRequest.

        :return: The internet_bandwidth_is_null of this CountGlobalEipsRequest.
        :rtype: list[bool]
        """
        return self._internet_bandwidth_is_null

    @internet_bandwidth_is_null.setter
    def internet_bandwidth_is_null(self, internet_bandwidth_is_null):
        r"""Sets the internet_bandwidth_is_null of this CountGlobalEipsRequest.

        :param internet_bandwidth_is_null: The internet_bandwidth_is_null of this CountGlobalEipsRequest.
        :type internet_bandwidth_is_null: list[bool]
        """
        self._internet_bandwidth_is_null = internet_bandwidth_is_null

    @property
    def gcb_bandwidth_is_null(self):
        r"""Gets the gcb_bandwidth_is_null of this CountGlobalEipsRequest.

        :return: The gcb_bandwidth_is_null of this CountGlobalEipsRequest.
        :rtype: list[bool]
        """
        return self._gcb_bandwidth_is_null

    @gcb_bandwidth_is_null.setter
    def gcb_bandwidth_is_null(self, gcb_bandwidth_is_null):
        r"""Sets the gcb_bandwidth_is_null of this CountGlobalEipsRequest.

        :param gcb_bandwidth_is_null: The gcb_bandwidth_is_null of this CountGlobalEipsRequest.
        :type gcb_bandwidth_is_null: list[bool]
        """
        self._gcb_bandwidth_is_null = gcb_bandwidth_is_null

    @property
    def status(self):
        r"""Gets the status of this CountGlobalEipsRequest.

        :return: The status of this CountGlobalEipsRequest.
        :rtype: list[str]
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this CountGlobalEipsRequest.

        :param status: The status of this CountGlobalEipsRequest.
        :type status: list[str]
        """
        self._status = status

    @property
    def associate_instance_info_region(self):
        r"""Gets the associate_instance_info_region of this CountGlobalEipsRequest.

        :return: The associate_instance_info_region of this CountGlobalEipsRequest.
        :rtype: list[str]
        """
        return self._associate_instance_info_region

    @associate_instance_info_region.setter
    def associate_instance_info_region(self, associate_instance_info_region):
        r"""Sets the associate_instance_info_region of this CountGlobalEipsRequest.

        :param associate_instance_info_region: The associate_instance_info_region of this CountGlobalEipsRequest.
        :type associate_instance_info_region: list[str]
        """
        self._associate_instance_info_region = associate_instance_info_region

    @property
    def associate_instance_info_public_border_group(self):
        r"""Gets the associate_instance_info_public_border_group of this CountGlobalEipsRequest.

        :return: The associate_instance_info_public_border_group of this CountGlobalEipsRequest.
        :rtype: list[str]
        """
        return self._associate_instance_info_public_border_group

    @associate_instance_info_public_border_group.setter
    def associate_instance_info_public_border_group(self, associate_instance_info_public_border_group):
        r"""Sets the associate_instance_info_public_border_group of this CountGlobalEipsRequest.

        :param associate_instance_info_public_border_group: The associate_instance_info_public_border_group of this CountGlobalEipsRequest.
        :type associate_instance_info_public_border_group: list[str]
        """
        self._associate_instance_info_public_border_group = associate_instance_info_public_border_group

    @property
    def associate_instance_info_instance_site(self):
        r"""Gets the associate_instance_info_instance_site of this CountGlobalEipsRequest.

        :return: The associate_instance_info_instance_site of this CountGlobalEipsRequest.
        :rtype: list[str]
        """
        return self._associate_instance_info_instance_site

    @associate_instance_info_instance_site.setter
    def associate_instance_info_instance_site(self, associate_instance_info_instance_site):
        r"""Sets the associate_instance_info_instance_site of this CountGlobalEipsRequest.

        :param associate_instance_info_instance_site: The associate_instance_info_instance_site of this CountGlobalEipsRequest.
        :type associate_instance_info_instance_site: list[str]
        """
        self._associate_instance_info_instance_site = associate_instance_info_instance_site

    @property
    def associate_instance_info_instance_type(self):
        r"""Gets the associate_instance_info_instance_type of this CountGlobalEipsRequest.

        :return: The associate_instance_info_instance_type of this CountGlobalEipsRequest.
        :rtype: list[str]
        """
        return self._associate_instance_info_instance_type

    @associate_instance_info_instance_type.setter
    def associate_instance_info_instance_type(self, associate_instance_info_instance_type):
        r"""Sets the associate_instance_info_instance_type of this CountGlobalEipsRequest.

        :param associate_instance_info_instance_type: The associate_instance_info_instance_type of this CountGlobalEipsRequest.
        :type associate_instance_info_instance_type: list[str]
        """
        self._associate_instance_info_instance_type = associate_instance_info_instance_type

    @property
    def associate_instance_info_instance_id(self):
        r"""Gets the associate_instance_info_instance_id of this CountGlobalEipsRequest.

        :return: The associate_instance_info_instance_id of this CountGlobalEipsRequest.
        :rtype: list[str]
        """
        return self._associate_instance_info_instance_id

    @associate_instance_info_instance_id.setter
    def associate_instance_info_instance_id(self, associate_instance_info_instance_id):
        r"""Sets the associate_instance_info_instance_id of this CountGlobalEipsRequest.

        :param associate_instance_info_instance_id: The associate_instance_info_instance_id of this CountGlobalEipsRequest.
        :type associate_instance_info_instance_id: list[str]
        """
        self._associate_instance_info_instance_id = associate_instance_info_instance_id

    @property
    def associate_instance_info_project_id(self):
        r"""Gets the associate_instance_info_project_id of this CountGlobalEipsRequest.

        :return: The associate_instance_info_project_id of this CountGlobalEipsRequest.
        :rtype: list[str]
        """
        return self._associate_instance_info_project_id

    @associate_instance_info_project_id.setter
    def associate_instance_info_project_id(self, associate_instance_info_project_id):
        r"""Sets the associate_instance_info_project_id of this CountGlobalEipsRequest.

        :param associate_instance_info_project_id: The associate_instance_info_project_id of this CountGlobalEipsRequest.
        :type associate_instance_info_project_id: list[str]
        """
        self._associate_instance_info_project_id = associate_instance_info_project_id

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this CountGlobalEipsRequest.

        :return: The enterprise_project_id of this CountGlobalEipsRequest.
        :rtype: list[str]
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this CountGlobalEipsRequest.

        :param enterprise_project_id: The enterprise_project_id of this CountGlobalEipsRequest.
        :type enterprise_project_id: list[str]
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def tags(self):
        r"""Gets the tags of this CountGlobalEipsRequest.

        :return: The tags of this CountGlobalEipsRequest.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this CountGlobalEipsRequest.

        :param tags: The tags of this CountGlobalEipsRequest.
        :type tags: list[str]
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
        if not isinstance(other, CountGlobalEipsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
