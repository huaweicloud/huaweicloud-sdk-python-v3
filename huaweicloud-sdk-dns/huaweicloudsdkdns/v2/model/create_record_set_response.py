# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateRecordSetResponse(SdkResponse):

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
        'zone_id': 'str',
        'zone_name': 'str',
        'type': 'str',
        'ttl': 'int',
        'records': 'list[str]',
        'create_at': 'str',
        'update_at': 'str',
        'status': 'str',
        'default': 'bool',
        'project_id': 'str',
        'links': 'PageLink'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'zone_id': 'zone_id',
        'zone_name': 'zone_name',
        'type': 'type',
        'ttl': 'ttl',
        'records': 'records',
        'create_at': 'create_at',
        'update_at': 'update_at',
        'status': 'status',
        'default': 'default',
        'project_id': 'project_id',
        'links': 'links'
    }

    def __init__(self, id=None, name=None, description=None, zone_id=None, zone_name=None, type=None, ttl=None, records=None, create_at=None, update_at=None, status=None, default=None, project_id=None, links=None):
        """CreateRecordSetResponse

        The model defined in huaweicloud sdk

        :param id: 
        :type id: str
        :param name: 
        :type name: str
        :param description: 
        :type description: str
        :param zone_id: 
        :type zone_id: str
        :param zone_name: 
        :type zone_name: str
        :param type: 
        :type type: str
        :param ttl: 
        :type ttl: int
        :param records: 
        :type records: list[str]
        :param create_at: 
        :type create_at: str
        :param update_at: 
        :type update_at: str
        :param status: 
        :type status: str
        :param default: 
        :type default: bool
        :param project_id: 
        :type project_id: str
        :param links: 
        :type links: :class:`huaweicloudsdkdns.v2.PageLink`
        """
        
        super(CreateRecordSetResponse, self).__init__()

        self._id = None
        self._name = None
        self._description = None
        self._zone_id = None
        self._zone_name = None
        self._type = None
        self._ttl = None
        self._records = None
        self._create_at = None
        self._update_at = None
        self._status = None
        self._default = None
        self._project_id = None
        self._links = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if zone_id is not None:
            self.zone_id = zone_id
        if zone_name is not None:
            self.zone_name = zone_name
        if type is not None:
            self.type = type
        if ttl is not None:
            self.ttl = ttl
        if records is not None:
            self.records = records
        if create_at is not None:
            self.create_at = create_at
        if update_at is not None:
            self.update_at = update_at
        if status is not None:
            self.status = status
        if default is not None:
            self.default = default
        if project_id is not None:
            self.project_id = project_id
        if links is not None:
            self.links = links

    @property
    def id(self):
        """Gets the id of this CreateRecordSetResponse.

        :return: The id of this CreateRecordSetResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CreateRecordSetResponse.

        :param id: The id of this CreateRecordSetResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this CreateRecordSetResponse.

        :return: The name of this CreateRecordSetResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateRecordSetResponse.

        :param name: The name of this CreateRecordSetResponse.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this CreateRecordSetResponse.

        :return: The description of this CreateRecordSetResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateRecordSetResponse.

        :param description: The description of this CreateRecordSetResponse.
        :type description: str
        """
        self._description = description

    @property
    def zone_id(self):
        """Gets the zone_id of this CreateRecordSetResponse.

        :return: The zone_id of this CreateRecordSetResponse.
        :rtype: str
        """
        return self._zone_id

    @zone_id.setter
    def zone_id(self, zone_id):
        """Sets the zone_id of this CreateRecordSetResponse.

        :param zone_id: The zone_id of this CreateRecordSetResponse.
        :type zone_id: str
        """
        self._zone_id = zone_id

    @property
    def zone_name(self):
        """Gets the zone_name of this CreateRecordSetResponse.

        :return: The zone_name of this CreateRecordSetResponse.
        :rtype: str
        """
        return self._zone_name

    @zone_name.setter
    def zone_name(self, zone_name):
        """Sets the zone_name of this CreateRecordSetResponse.

        :param zone_name: The zone_name of this CreateRecordSetResponse.
        :type zone_name: str
        """
        self._zone_name = zone_name

    @property
    def type(self):
        """Gets the type of this CreateRecordSetResponse.

        :return: The type of this CreateRecordSetResponse.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CreateRecordSetResponse.

        :param type: The type of this CreateRecordSetResponse.
        :type type: str
        """
        self._type = type

    @property
    def ttl(self):
        """Gets the ttl of this CreateRecordSetResponse.

        :return: The ttl of this CreateRecordSetResponse.
        :rtype: int
        """
        return self._ttl

    @ttl.setter
    def ttl(self, ttl):
        """Sets the ttl of this CreateRecordSetResponse.

        :param ttl: The ttl of this CreateRecordSetResponse.
        :type ttl: int
        """
        self._ttl = ttl

    @property
    def records(self):
        """Gets the records of this CreateRecordSetResponse.

        :return: The records of this CreateRecordSetResponse.
        :rtype: list[str]
        """
        return self._records

    @records.setter
    def records(self, records):
        """Sets the records of this CreateRecordSetResponse.

        :param records: The records of this CreateRecordSetResponse.
        :type records: list[str]
        """
        self._records = records

    @property
    def create_at(self):
        """Gets the create_at of this CreateRecordSetResponse.

        :return: The create_at of this CreateRecordSetResponse.
        :rtype: str
        """
        return self._create_at

    @create_at.setter
    def create_at(self, create_at):
        """Sets the create_at of this CreateRecordSetResponse.

        :param create_at: The create_at of this CreateRecordSetResponse.
        :type create_at: str
        """
        self._create_at = create_at

    @property
    def update_at(self):
        """Gets the update_at of this CreateRecordSetResponse.

        :return: The update_at of this CreateRecordSetResponse.
        :rtype: str
        """
        return self._update_at

    @update_at.setter
    def update_at(self, update_at):
        """Sets the update_at of this CreateRecordSetResponse.

        :param update_at: The update_at of this CreateRecordSetResponse.
        :type update_at: str
        """
        self._update_at = update_at

    @property
    def status(self):
        """Gets the status of this CreateRecordSetResponse.

        :return: The status of this CreateRecordSetResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CreateRecordSetResponse.

        :param status: The status of this CreateRecordSetResponse.
        :type status: str
        """
        self._status = status

    @property
    def default(self):
        """Gets the default of this CreateRecordSetResponse.

        :return: The default of this CreateRecordSetResponse.
        :rtype: bool
        """
        return self._default

    @default.setter
    def default(self, default):
        """Sets the default of this CreateRecordSetResponse.

        :param default: The default of this CreateRecordSetResponse.
        :type default: bool
        """
        self._default = default

    @property
    def project_id(self):
        """Gets the project_id of this CreateRecordSetResponse.

        :return: The project_id of this CreateRecordSetResponse.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this CreateRecordSetResponse.

        :param project_id: The project_id of this CreateRecordSetResponse.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def links(self):
        """Gets the links of this CreateRecordSetResponse.

        :return: The links of this CreateRecordSetResponse.
        :rtype: :class:`huaweicloudsdkdns.v2.PageLink`
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this CreateRecordSetResponse.

        :param links: The links of this CreateRecordSetResponse.
        :type links: :class:`huaweicloudsdkdns.v2.PageLink`
        """
        self._links = links

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
        if not isinstance(other, CreateRecordSetResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
