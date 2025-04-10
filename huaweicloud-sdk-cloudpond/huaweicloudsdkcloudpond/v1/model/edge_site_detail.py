# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EdgeSiteDetail:

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
        'domain_id': 'str',
        'name': 'str',
        'description': 'str',
        'region_id': 'str',
        'project_id': 'str',
        'availability_zone_id': 'str',
        'status': 'str',
        'location': 'LocationDetail',
        'enterprise_project_id': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'domain_id': 'domain_id',
        'name': 'name',
        'description': 'description',
        'region_id': 'region_id',
        'project_id': 'project_id',
        'availability_zone_id': 'availability_zone_id',
        'status': 'status',
        'location': 'location',
        'enterprise_project_id': 'enterprise_project_id',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, id=None, domain_id=None, name=None, description=None, region_id=None, project_id=None, availability_zone_id=None, status=None, location=None, enterprise_project_id=None, created_at=None, updated_at=None):
        r"""EdgeSiteDetail

        The model defined in huaweicloud sdk

        :param id: 边缘小站ID
        :type id: str
        :param domain_id: 边缘小站所属账号ID
        :type domain_id: str
        :param name: 边缘小站名称
        :type name: str
        :param description: 边缘小站描述
        :type description: str
        :param region_id: 边缘小站所属区域ID
        :type region_id: str
        :param project_id: 边缘小站所属项目ID
        :type project_id: str
        :param availability_zone_id: 边缘小站的可用区ID
        :type availability_zone_id: str
        :param status: 边缘小站的部署状态
        :type status: str
        :param location: 
        :type location: :class:`huaweicloudsdkcloudpond.v1.LocationDetail`
        :param enterprise_project_id: 边缘小站所属企业项目ID
        :type enterprise_project_id: str
        :param created_at: 边缘小站创建时间
        :type created_at: datetime
        :param updated_at: 边缘小站更新时间
        :type updated_at: datetime
        """
        
        

        self._id = None
        self._domain_id = None
        self._name = None
        self._description = None
        self._region_id = None
        self._project_id = None
        self._availability_zone_id = None
        self._status = None
        self._location = None
        self._enterprise_project_id = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if domain_id is not None:
            self.domain_id = domain_id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if region_id is not None:
            self.region_id = region_id
        if project_id is not None:
            self.project_id = project_id
        if availability_zone_id is not None:
            self.availability_zone_id = availability_zone_id
        if status is not None:
            self.status = status
        if location is not None:
            self.location = location
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def id(self):
        r"""Gets the id of this EdgeSiteDetail.

        边缘小站ID

        :return: The id of this EdgeSiteDetail.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this EdgeSiteDetail.

        边缘小站ID

        :param id: The id of this EdgeSiteDetail.
        :type id: str
        """
        self._id = id

    @property
    def domain_id(self):
        r"""Gets the domain_id of this EdgeSiteDetail.

        边缘小站所属账号ID

        :return: The domain_id of this EdgeSiteDetail.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this EdgeSiteDetail.

        边缘小站所属账号ID

        :param domain_id: The domain_id of this EdgeSiteDetail.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def name(self):
        r"""Gets the name of this EdgeSiteDetail.

        边缘小站名称

        :return: The name of this EdgeSiteDetail.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this EdgeSiteDetail.

        边缘小站名称

        :param name: The name of this EdgeSiteDetail.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this EdgeSiteDetail.

        边缘小站描述

        :return: The description of this EdgeSiteDetail.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this EdgeSiteDetail.

        边缘小站描述

        :param description: The description of this EdgeSiteDetail.
        :type description: str
        """
        self._description = description

    @property
    def region_id(self):
        r"""Gets the region_id of this EdgeSiteDetail.

        边缘小站所属区域ID

        :return: The region_id of this EdgeSiteDetail.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        r"""Sets the region_id of this EdgeSiteDetail.

        边缘小站所属区域ID

        :param region_id: The region_id of this EdgeSiteDetail.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def project_id(self):
        r"""Gets the project_id of this EdgeSiteDetail.

        边缘小站所属项目ID

        :return: The project_id of this EdgeSiteDetail.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this EdgeSiteDetail.

        边缘小站所属项目ID

        :param project_id: The project_id of this EdgeSiteDetail.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def availability_zone_id(self):
        r"""Gets the availability_zone_id of this EdgeSiteDetail.

        边缘小站的可用区ID

        :return: The availability_zone_id of this EdgeSiteDetail.
        :rtype: str
        """
        return self._availability_zone_id

    @availability_zone_id.setter
    def availability_zone_id(self, availability_zone_id):
        r"""Sets the availability_zone_id of this EdgeSiteDetail.

        边缘小站的可用区ID

        :param availability_zone_id: The availability_zone_id of this EdgeSiteDetail.
        :type availability_zone_id: str
        """
        self._availability_zone_id = availability_zone_id

    @property
    def status(self):
        r"""Gets the status of this EdgeSiteDetail.

        边缘小站的部署状态

        :return: The status of this EdgeSiteDetail.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this EdgeSiteDetail.

        边缘小站的部署状态

        :param status: The status of this EdgeSiteDetail.
        :type status: str
        """
        self._status = status

    @property
    def location(self):
        r"""Gets the location of this EdgeSiteDetail.

        :return: The location of this EdgeSiteDetail.
        :rtype: :class:`huaweicloudsdkcloudpond.v1.LocationDetail`
        """
        return self._location

    @location.setter
    def location(self, location):
        r"""Sets the location of this EdgeSiteDetail.

        :param location: The location of this EdgeSiteDetail.
        :type location: :class:`huaweicloudsdkcloudpond.v1.LocationDetail`
        """
        self._location = location

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this EdgeSiteDetail.

        边缘小站所属企业项目ID

        :return: The enterprise_project_id of this EdgeSiteDetail.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this EdgeSiteDetail.

        边缘小站所属企业项目ID

        :param enterprise_project_id: The enterprise_project_id of this EdgeSiteDetail.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def created_at(self):
        r"""Gets the created_at of this EdgeSiteDetail.

        边缘小站创建时间

        :return: The created_at of this EdgeSiteDetail.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this EdgeSiteDetail.

        边缘小站创建时间

        :param created_at: The created_at of this EdgeSiteDetail.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this EdgeSiteDetail.

        边缘小站更新时间

        :return: The updated_at of this EdgeSiteDetail.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this EdgeSiteDetail.

        边缘小站更新时间

        :param updated_at: The updated_at of this EdgeSiteDetail.
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
        if not isinstance(other, EdgeSiteDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
