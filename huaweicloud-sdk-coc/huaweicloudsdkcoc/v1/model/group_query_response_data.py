# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GroupQueryResponseData:

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
        'vendor': 'str',
        'code': 'str',
        'domain_id': 'str',
        'region_id': 'str',
        'component_id': 'str',
        'application_id': 'str',
        'ep_id': 'str',
        'sync_mode': 'str',
        'rule_tags': 'str',
        'relation_configurations': 'list[GroupRelationConfiguration]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'vendor': 'vendor',
        'code': 'code',
        'domain_id': 'domain_id',
        'region_id': 'region_id',
        'component_id': 'component_id',
        'application_id': 'application_id',
        'ep_id': 'ep_id',
        'sync_mode': 'sync_mode',
        'rule_tags': 'rule_tags',
        'relation_configurations': 'relation_configurations'
    }

    def __init__(self, id=None, name=None, vendor=None, code=None, domain_id=None, region_id=None, component_id=None, application_id=None, ep_id=None, sync_mode=None, rule_tags=None, relation_configurations=None):
        r"""GroupQueryResponseData

        The model defined in huaweicloud sdk

        :param id: CloudCMDB分配的uuid。
        :type id: str
        :param name: 名称。
        :type name: str
        :param vendor: 厂商（默认RMS，可填RMS/ALI/OTHER）。
        :type vendor: str
        :param code: code。
        :type code: str
        :param domain_id: 租户id。
        :type domain_id: str
        :param region_id: region id。
        :type region_id: str
        :param component_id: component id。
        :type component_id: str
        :param application_id: application id。
        :type application_id: str
        :param ep_id: 企业项目id。
        :type ep_id: str
        :param sync_mode: 资源关联模式，MANUAL表示手动关联，AUTO表示智能关联。
        :type sync_mode: str
        :param rule_tags: 关联标签。
        :type rule_tags: str
        :param relation_configurations: 分组配置信息。
        :type relation_configurations: list[:class:`huaweicloudsdkcoc.v1.GroupRelationConfiguration`]
        """
        
        

        self._id = None
        self._name = None
        self._vendor = None
        self._code = None
        self._domain_id = None
        self._region_id = None
        self._component_id = None
        self._application_id = None
        self._ep_id = None
        self._sync_mode = None
        self._rule_tags = None
        self._relation_configurations = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if vendor is not None:
            self.vendor = vendor
        if code is not None:
            self.code = code
        if domain_id is not None:
            self.domain_id = domain_id
        if region_id is not None:
            self.region_id = region_id
        if component_id is not None:
            self.component_id = component_id
        if application_id is not None:
            self.application_id = application_id
        self.ep_id = ep_id
        if sync_mode is not None:
            self.sync_mode = sync_mode
        if rule_tags is not None:
            self.rule_tags = rule_tags
        if relation_configurations is not None:
            self.relation_configurations = relation_configurations

    @property
    def id(self):
        r"""Gets the id of this GroupQueryResponseData.

        CloudCMDB分配的uuid。

        :return: The id of this GroupQueryResponseData.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this GroupQueryResponseData.

        CloudCMDB分配的uuid。

        :param id: The id of this GroupQueryResponseData.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this GroupQueryResponseData.

        名称。

        :return: The name of this GroupQueryResponseData.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this GroupQueryResponseData.

        名称。

        :param name: The name of this GroupQueryResponseData.
        :type name: str
        """
        self._name = name

    @property
    def vendor(self):
        r"""Gets the vendor of this GroupQueryResponseData.

        厂商（默认RMS，可填RMS/ALI/OTHER）。

        :return: The vendor of this GroupQueryResponseData.
        :rtype: str
        """
        return self._vendor

    @vendor.setter
    def vendor(self, vendor):
        r"""Sets the vendor of this GroupQueryResponseData.

        厂商（默认RMS，可填RMS/ALI/OTHER）。

        :param vendor: The vendor of this GroupQueryResponseData.
        :type vendor: str
        """
        self._vendor = vendor

    @property
    def code(self):
        r"""Gets the code of this GroupQueryResponseData.

        code。

        :return: The code of this GroupQueryResponseData.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        r"""Sets the code of this GroupQueryResponseData.

        code。

        :param code: The code of this GroupQueryResponseData.
        :type code: str
        """
        self._code = code

    @property
    def domain_id(self):
        r"""Gets the domain_id of this GroupQueryResponseData.

        租户id。

        :return: The domain_id of this GroupQueryResponseData.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this GroupQueryResponseData.

        租户id。

        :param domain_id: The domain_id of this GroupQueryResponseData.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def region_id(self):
        r"""Gets the region_id of this GroupQueryResponseData.

        region id。

        :return: The region_id of this GroupQueryResponseData.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        r"""Sets the region_id of this GroupQueryResponseData.

        region id。

        :param region_id: The region_id of this GroupQueryResponseData.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def component_id(self):
        r"""Gets the component_id of this GroupQueryResponseData.

        component id。

        :return: The component_id of this GroupQueryResponseData.
        :rtype: str
        """
        return self._component_id

    @component_id.setter
    def component_id(self, component_id):
        r"""Sets the component_id of this GroupQueryResponseData.

        component id。

        :param component_id: The component_id of this GroupQueryResponseData.
        :type component_id: str
        """
        self._component_id = component_id

    @property
    def application_id(self):
        r"""Gets the application_id of this GroupQueryResponseData.

        application id。

        :return: The application_id of this GroupQueryResponseData.
        :rtype: str
        """
        return self._application_id

    @application_id.setter
    def application_id(self, application_id):
        r"""Sets the application_id of this GroupQueryResponseData.

        application id。

        :param application_id: The application_id of this GroupQueryResponseData.
        :type application_id: str
        """
        self._application_id = application_id

    @property
    def ep_id(self):
        r"""Gets the ep_id of this GroupQueryResponseData.

        企业项目id。

        :return: The ep_id of this GroupQueryResponseData.
        :rtype: str
        """
        return self._ep_id

    @ep_id.setter
    def ep_id(self, ep_id):
        r"""Sets the ep_id of this GroupQueryResponseData.

        企业项目id。

        :param ep_id: The ep_id of this GroupQueryResponseData.
        :type ep_id: str
        """
        self._ep_id = ep_id

    @property
    def sync_mode(self):
        r"""Gets the sync_mode of this GroupQueryResponseData.

        资源关联模式，MANUAL表示手动关联，AUTO表示智能关联。

        :return: The sync_mode of this GroupQueryResponseData.
        :rtype: str
        """
        return self._sync_mode

    @sync_mode.setter
    def sync_mode(self, sync_mode):
        r"""Sets the sync_mode of this GroupQueryResponseData.

        资源关联模式，MANUAL表示手动关联，AUTO表示智能关联。

        :param sync_mode: The sync_mode of this GroupQueryResponseData.
        :type sync_mode: str
        """
        self._sync_mode = sync_mode

    @property
    def rule_tags(self):
        r"""Gets the rule_tags of this GroupQueryResponseData.

        关联标签。

        :return: The rule_tags of this GroupQueryResponseData.
        :rtype: str
        """
        return self._rule_tags

    @rule_tags.setter
    def rule_tags(self, rule_tags):
        r"""Sets the rule_tags of this GroupQueryResponseData.

        关联标签。

        :param rule_tags: The rule_tags of this GroupQueryResponseData.
        :type rule_tags: str
        """
        self._rule_tags = rule_tags

    @property
    def relation_configurations(self):
        r"""Gets the relation_configurations of this GroupQueryResponseData.

        分组配置信息。

        :return: The relation_configurations of this GroupQueryResponseData.
        :rtype: list[:class:`huaweicloudsdkcoc.v1.GroupRelationConfiguration`]
        """
        return self._relation_configurations

    @relation_configurations.setter
    def relation_configurations(self, relation_configurations):
        r"""Sets the relation_configurations of this GroupQueryResponseData.

        分组配置信息。

        :param relation_configurations: The relation_configurations of this GroupQueryResponseData.
        :type relation_configurations: list[:class:`huaweicloudsdkcoc.v1.GroupRelationConfiguration`]
        """
        self._relation_configurations = relation_configurations

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, GroupQueryResponseData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
