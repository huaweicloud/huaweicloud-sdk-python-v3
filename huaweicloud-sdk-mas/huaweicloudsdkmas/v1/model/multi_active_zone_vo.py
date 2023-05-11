# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MultiActiveZoneVo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'available_zone': 'list[str]',
        'created_date': 'datetime',
        'description': 'str',
        'id': 'str',
        'is_master': 'bool',
        'name': 'str',
        'namespace_id': 'str',
        'region': 'str',
        'region_name': 'str',
        'spec': 'BaseMultiActiveZoneSpec',
        'type': 'int',
        'updated_date': 'datetime'
    }

    attribute_map = {
        'available_zone': 'available_zone',
        'created_date': 'created_date',
        'description': 'description',
        'id': 'id',
        'is_master': 'is_master',
        'name': 'name',
        'namespace_id': 'namespace_id',
        'region': 'region',
        'region_name': 'region_name',
        'spec': 'spec',
        'type': 'type',
        'updated_date': 'updated_date'
    }

    def __init__(self, available_zone=None, created_date=None, description=None, id=None, is_master=None, name=None, namespace_id=None, region=None, region_name=None, spec=None, type=None, updated_date=None):
        """MultiActiveZoneVo

        The model defined in huaweicloud sdk

        :param available_zone: 
        :type available_zone: list[str]
        :param created_date: 
        :type created_date: datetime
        :param description: 
        :type description: str
        :param id: 
        :type id: str
        :param is_master: 
        :type is_master: bool
        :param name: 
        :type name: str
        :param namespace_id: 
        :type namespace_id: str
        :param region: 
        :type region: str
        :param region_name: 
        :type region_name: str
        :param spec: 
        :type spec: :class:`huaweicloudsdkmas.v1.BaseMultiActiveZoneSpec`
        :param type: 
        :type type: int
        :param updated_date: 
        :type updated_date: datetime
        """
        
        

        self._available_zone = None
        self._created_date = None
        self._description = None
        self._id = None
        self._is_master = None
        self._name = None
        self._namespace_id = None
        self._region = None
        self._region_name = None
        self._spec = None
        self._type = None
        self._updated_date = None
        self.discriminator = None

        if available_zone is not None:
            self.available_zone = available_zone
        if created_date is not None:
            self.created_date = created_date
        if description is not None:
            self.description = description
        if id is not None:
            self.id = id
        if is_master is not None:
            self.is_master = is_master
        if name is not None:
            self.name = name
        if namespace_id is not None:
            self.namespace_id = namespace_id
        if region is not None:
            self.region = region
        if region_name is not None:
            self.region_name = region_name
        if spec is not None:
            self.spec = spec
        if type is not None:
            self.type = type
        if updated_date is not None:
            self.updated_date = updated_date

    @property
    def available_zone(self):
        """Gets the available_zone of this MultiActiveZoneVo.

        :return: The available_zone of this MultiActiveZoneVo.
        :rtype: list[str]
        """
        return self._available_zone

    @available_zone.setter
    def available_zone(self, available_zone):
        """Sets the available_zone of this MultiActiveZoneVo.

        :param available_zone: The available_zone of this MultiActiveZoneVo.
        :type available_zone: list[str]
        """
        self._available_zone = available_zone

    @property
    def created_date(self):
        """Gets the created_date of this MultiActiveZoneVo.

        :return: The created_date of this MultiActiveZoneVo.
        :rtype: datetime
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        """Sets the created_date of this MultiActiveZoneVo.

        :param created_date: The created_date of this MultiActiveZoneVo.
        :type created_date: datetime
        """
        self._created_date = created_date

    @property
    def description(self):
        """Gets the description of this MultiActiveZoneVo.

        :return: The description of this MultiActiveZoneVo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this MultiActiveZoneVo.

        :param description: The description of this MultiActiveZoneVo.
        :type description: str
        """
        self._description = description

    @property
    def id(self):
        """Gets the id of this MultiActiveZoneVo.

        :return: The id of this MultiActiveZoneVo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this MultiActiveZoneVo.

        :param id: The id of this MultiActiveZoneVo.
        :type id: str
        """
        self._id = id

    @property
    def is_master(self):
        """Gets the is_master of this MultiActiveZoneVo.

        :return: The is_master of this MultiActiveZoneVo.
        :rtype: bool
        """
        return self._is_master

    @is_master.setter
    def is_master(self, is_master):
        """Sets the is_master of this MultiActiveZoneVo.

        :param is_master: The is_master of this MultiActiveZoneVo.
        :type is_master: bool
        """
        self._is_master = is_master

    @property
    def name(self):
        """Gets the name of this MultiActiveZoneVo.

        :return: The name of this MultiActiveZoneVo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this MultiActiveZoneVo.

        :param name: The name of this MultiActiveZoneVo.
        :type name: str
        """
        self._name = name

    @property
    def namespace_id(self):
        """Gets the namespace_id of this MultiActiveZoneVo.

        :return: The namespace_id of this MultiActiveZoneVo.
        :rtype: str
        """
        return self._namespace_id

    @namespace_id.setter
    def namespace_id(self, namespace_id):
        """Sets the namespace_id of this MultiActiveZoneVo.

        :param namespace_id: The namespace_id of this MultiActiveZoneVo.
        :type namespace_id: str
        """
        self._namespace_id = namespace_id

    @property
    def region(self):
        """Gets the region of this MultiActiveZoneVo.

        :return: The region of this MultiActiveZoneVo.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this MultiActiveZoneVo.

        :param region: The region of this MultiActiveZoneVo.
        :type region: str
        """
        self._region = region

    @property
    def region_name(self):
        """Gets the region_name of this MultiActiveZoneVo.

        :return: The region_name of this MultiActiveZoneVo.
        :rtype: str
        """
        return self._region_name

    @region_name.setter
    def region_name(self, region_name):
        """Sets the region_name of this MultiActiveZoneVo.

        :param region_name: The region_name of this MultiActiveZoneVo.
        :type region_name: str
        """
        self._region_name = region_name

    @property
    def spec(self):
        """Gets the spec of this MultiActiveZoneVo.

        :return: The spec of this MultiActiveZoneVo.
        :rtype: :class:`huaweicloudsdkmas.v1.BaseMultiActiveZoneSpec`
        """
        return self._spec

    @spec.setter
    def spec(self, spec):
        """Sets the spec of this MultiActiveZoneVo.

        :param spec: The spec of this MultiActiveZoneVo.
        :type spec: :class:`huaweicloudsdkmas.v1.BaseMultiActiveZoneSpec`
        """
        self._spec = spec

    @property
    def type(self):
        """Gets the type of this MultiActiveZoneVo.

        :return: The type of this MultiActiveZoneVo.
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this MultiActiveZoneVo.

        :param type: The type of this MultiActiveZoneVo.
        :type type: int
        """
        self._type = type

    @property
    def updated_date(self):
        """Gets the updated_date of this MultiActiveZoneVo.

        :return: The updated_date of this MultiActiveZoneVo.
        :rtype: datetime
        """
        return self._updated_date

    @updated_date.setter
    def updated_date(self, updated_date):
        """Sets the updated_date of this MultiActiveZoneVo.

        :param updated_date: The updated_date of this MultiActiveZoneVo.
        :type updated_date: datetime
        """
        self._updated_date = updated_date

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
        if not isinstance(other, MultiActiveZoneVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
