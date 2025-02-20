# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GroupInfo:

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
        'code': 'str',
        'domain_id': 'str',
        'region_id': 'str',
        'application_id': 'str',
        'component_id': 'str',
        'sync_mode': 'str',
        'vendor': 'str',
        'sync_rules': 'str',
        'relation_configurations': 'list[str]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'code': 'code',
        'domain_id': 'domain_id',
        'region_id': 'region_id',
        'application_id': 'application_id',
        'component_id': 'component_id',
        'sync_mode': 'sync_mode',
        'vendor': 'vendor',
        'sync_rules': 'sync_rules',
        'relation_configurations': 'relation_configurations'
    }

    def __init__(self, id=None, name=None, code=None, domain_id=None, region_id=None, application_id=None, component_id=None, sync_mode=None, vendor=None, sync_rules=None, relation_configurations=None):
        """GroupInfo

        The model defined in huaweicloud sdk

        :param id: 
        :type id: str
        :param name: 
        :type name: str
        :param code: 
        :type code: str
        :param domain_id: 
        :type domain_id: str
        :param region_id: 
        :type region_id: str
        :param application_id: 
        :type application_id: str
        :param component_id: 
        :type component_id: str
        :param sync_mode: 
        :type sync_mode: str
        :param vendor: 
        :type vendor: str
        :param sync_rules: 
        :type sync_rules: str
        :param relation_configurations: 
        :type relation_configurations: list[str]
        """
        
        

        self._id = None
        self._name = None
        self._code = None
        self._domain_id = None
        self._region_id = None
        self._application_id = None
        self._component_id = None
        self._sync_mode = None
        self._vendor = None
        self._sync_rules = None
        self._relation_configurations = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if code is not None:
            self.code = code
        if domain_id is not None:
            self.domain_id = domain_id
        if region_id is not None:
            self.region_id = region_id
        if application_id is not None:
            self.application_id = application_id
        if component_id is not None:
            self.component_id = component_id
        if sync_mode is not None:
            self.sync_mode = sync_mode
        if vendor is not None:
            self.vendor = vendor
        if sync_rules is not None:
            self.sync_rules = sync_rules
        if relation_configurations is not None:
            self.relation_configurations = relation_configurations

    @property
    def id(self):
        """Gets the id of this GroupInfo.

        :return: The id of this GroupInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GroupInfo.

        :param id: The id of this GroupInfo.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this GroupInfo.

        :return: The name of this GroupInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GroupInfo.

        :param name: The name of this GroupInfo.
        :type name: str
        """
        self._name = name

    @property
    def code(self):
        """Gets the code of this GroupInfo.

        :return: The code of this GroupInfo.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this GroupInfo.

        :param code: The code of this GroupInfo.
        :type code: str
        """
        self._code = code

    @property
    def domain_id(self):
        """Gets the domain_id of this GroupInfo.

        :return: The domain_id of this GroupInfo.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this GroupInfo.

        :param domain_id: The domain_id of this GroupInfo.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def region_id(self):
        """Gets the region_id of this GroupInfo.

        :return: The region_id of this GroupInfo.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """Sets the region_id of this GroupInfo.

        :param region_id: The region_id of this GroupInfo.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def application_id(self):
        """Gets the application_id of this GroupInfo.

        :return: The application_id of this GroupInfo.
        :rtype: str
        """
        return self._application_id

    @application_id.setter
    def application_id(self, application_id):
        """Sets the application_id of this GroupInfo.

        :param application_id: The application_id of this GroupInfo.
        :type application_id: str
        """
        self._application_id = application_id

    @property
    def component_id(self):
        """Gets the component_id of this GroupInfo.

        :return: The component_id of this GroupInfo.
        :rtype: str
        """
        return self._component_id

    @component_id.setter
    def component_id(self, component_id):
        """Sets the component_id of this GroupInfo.

        :param component_id: The component_id of this GroupInfo.
        :type component_id: str
        """
        self._component_id = component_id

    @property
    def sync_mode(self):
        """Gets the sync_mode of this GroupInfo.

        :return: The sync_mode of this GroupInfo.
        :rtype: str
        """
        return self._sync_mode

    @sync_mode.setter
    def sync_mode(self, sync_mode):
        """Sets the sync_mode of this GroupInfo.

        :param sync_mode: The sync_mode of this GroupInfo.
        :type sync_mode: str
        """
        self._sync_mode = sync_mode

    @property
    def vendor(self):
        """Gets the vendor of this GroupInfo.

        :return: The vendor of this GroupInfo.
        :rtype: str
        """
        return self._vendor

    @vendor.setter
    def vendor(self, vendor):
        """Sets the vendor of this GroupInfo.

        :param vendor: The vendor of this GroupInfo.
        :type vendor: str
        """
        self._vendor = vendor

    @property
    def sync_rules(self):
        """Gets the sync_rules of this GroupInfo.

        :return: The sync_rules of this GroupInfo.
        :rtype: str
        """
        return self._sync_rules

    @sync_rules.setter
    def sync_rules(self, sync_rules):
        """Sets the sync_rules of this GroupInfo.

        :param sync_rules: The sync_rules of this GroupInfo.
        :type sync_rules: str
        """
        self._sync_rules = sync_rules

    @property
    def relation_configurations(self):
        """Gets the relation_configurations of this GroupInfo.

        :return: The relation_configurations of this GroupInfo.
        :rtype: list[str]
        """
        return self._relation_configurations

    @relation_configurations.setter
    def relation_configurations(self, relation_configurations):
        """Sets the relation_configurations of this GroupInfo.

        :param relation_configurations: The relation_configurations of this GroupInfo.
        :type relation_configurations: list[str]
        """
        self._relation_configurations = relation_configurations

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
        if not isinstance(other, GroupInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
