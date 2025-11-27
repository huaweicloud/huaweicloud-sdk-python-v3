# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GroupCreateResponseData:

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
        'path': 'str',
        'sync_mode': 'str',
        'create_time': 'str',
        'update_time': 'str',
        'sync_rules': 'list[GroupUpdateRequestSyncRules]',
        'related_domain_id': 'str',
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
        'path': 'path',
        'sync_mode': 'sync_mode',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'sync_rules': 'sync_rules',
        'related_domain_id': 'related_domain_id',
        'relation_configurations': 'relation_configurations'
    }

    def __init__(self, id=None, name=None, vendor=None, code=None, domain_id=None, region_id=None, component_id=None, application_id=None, path=None, sync_mode=None, create_time=None, update_time=None, sync_rules=None, related_domain_id=None, relation_configurations=None):
        r"""GroupCreateResponseData

        The model defined in huaweicloud sdk

        :param id: CloudCMDB分配的uuid。
        :type id: str
        :param name: 名称。
        :type name: str
        :param vendor: 厂商（默认RMS，可填RMS/ALI/OTHER）。
        :type vendor: str
        :param code: 分组code。
        :type code: str
        :param domain_id: 租户id。
        :type domain_id: str
        :param region_id: region id。
        :type region_id: str
        :param component_id: 组件id。
        :type component_id: str
        :param application_id: 应用id。
        :type application_id: str
        :param path: 分组路径。
        :type path: str
        :param sync_mode: 资源关联模式，MANUAL表示手动关联，AUTO表示智能关联。
        :type sync_mode: str
        :param create_time: 创建时间。
        :type create_time: str
        :param update_time: 更新时间。
        :type update_time: str
        :param sync_rules: 智能关联规则。
        :type sync_rules: list[:class:`huaweicloudsdkcoc.v1.GroupUpdateRequestSyncRules`]
        :param related_domain_id: 跨帐号资源所属的domainId。
        :type related_domain_id: str
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
        self._path = None
        self._sync_mode = None
        self._create_time = None
        self._update_time = None
        self._sync_rules = None
        self._related_domain_id = None
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
        if path is not None:
            self.path = path
        if sync_mode is not None:
            self.sync_mode = sync_mode
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if sync_rules is not None:
            self.sync_rules = sync_rules
        if related_domain_id is not None:
            self.related_domain_id = related_domain_id
        if relation_configurations is not None:
            self.relation_configurations = relation_configurations

    @property
    def id(self):
        r"""Gets the id of this GroupCreateResponseData.

        CloudCMDB分配的uuid。

        :return: The id of this GroupCreateResponseData.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this GroupCreateResponseData.

        CloudCMDB分配的uuid。

        :param id: The id of this GroupCreateResponseData.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this GroupCreateResponseData.

        名称。

        :return: The name of this GroupCreateResponseData.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this GroupCreateResponseData.

        名称。

        :param name: The name of this GroupCreateResponseData.
        :type name: str
        """
        self._name = name

    @property
    def vendor(self):
        r"""Gets the vendor of this GroupCreateResponseData.

        厂商（默认RMS，可填RMS/ALI/OTHER）。

        :return: The vendor of this GroupCreateResponseData.
        :rtype: str
        """
        return self._vendor

    @vendor.setter
    def vendor(self, vendor):
        r"""Sets the vendor of this GroupCreateResponseData.

        厂商（默认RMS，可填RMS/ALI/OTHER）。

        :param vendor: The vendor of this GroupCreateResponseData.
        :type vendor: str
        """
        self._vendor = vendor

    @property
    def code(self):
        r"""Gets the code of this GroupCreateResponseData.

        分组code。

        :return: The code of this GroupCreateResponseData.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        r"""Sets the code of this GroupCreateResponseData.

        分组code。

        :param code: The code of this GroupCreateResponseData.
        :type code: str
        """
        self._code = code

    @property
    def domain_id(self):
        r"""Gets the domain_id of this GroupCreateResponseData.

        租户id。

        :return: The domain_id of this GroupCreateResponseData.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this GroupCreateResponseData.

        租户id。

        :param domain_id: The domain_id of this GroupCreateResponseData.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def region_id(self):
        r"""Gets the region_id of this GroupCreateResponseData.

        region id。

        :return: The region_id of this GroupCreateResponseData.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        r"""Sets the region_id of this GroupCreateResponseData.

        region id。

        :param region_id: The region_id of this GroupCreateResponseData.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def component_id(self):
        r"""Gets the component_id of this GroupCreateResponseData.

        组件id。

        :return: The component_id of this GroupCreateResponseData.
        :rtype: str
        """
        return self._component_id

    @component_id.setter
    def component_id(self, component_id):
        r"""Sets the component_id of this GroupCreateResponseData.

        组件id。

        :param component_id: The component_id of this GroupCreateResponseData.
        :type component_id: str
        """
        self._component_id = component_id

    @property
    def application_id(self):
        r"""Gets the application_id of this GroupCreateResponseData.

        应用id。

        :return: The application_id of this GroupCreateResponseData.
        :rtype: str
        """
        return self._application_id

    @application_id.setter
    def application_id(self, application_id):
        r"""Sets the application_id of this GroupCreateResponseData.

        应用id。

        :param application_id: The application_id of this GroupCreateResponseData.
        :type application_id: str
        """
        self._application_id = application_id

    @property
    def path(self):
        r"""Gets the path of this GroupCreateResponseData.

        分组路径。

        :return: The path of this GroupCreateResponseData.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        r"""Sets the path of this GroupCreateResponseData.

        分组路径。

        :param path: The path of this GroupCreateResponseData.
        :type path: str
        """
        self._path = path

    @property
    def sync_mode(self):
        r"""Gets the sync_mode of this GroupCreateResponseData.

        资源关联模式，MANUAL表示手动关联，AUTO表示智能关联。

        :return: The sync_mode of this GroupCreateResponseData.
        :rtype: str
        """
        return self._sync_mode

    @sync_mode.setter
    def sync_mode(self, sync_mode):
        r"""Sets the sync_mode of this GroupCreateResponseData.

        资源关联模式，MANUAL表示手动关联，AUTO表示智能关联。

        :param sync_mode: The sync_mode of this GroupCreateResponseData.
        :type sync_mode: str
        """
        self._sync_mode = sync_mode

    @property
    def create_time(self):
        r"""Gets the create_time of this GroupCreateResponseData.

        创建时间。

        :return: The create_time of this GroupCreateResponseData.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this GroupCreateResponseData.

        创建时间。

        :param create_time: The create_time of this GroupCreateResponseData.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this GroupCreateResponseData.

        更新时间。

        :return: The update_time of this GroupCreateResponseData.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this GroupCreateResponseData.

        更新时间。

        :param update_time: The update_time of this GroupCreateResponseData.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def sync_rules(self):
        r"""Gets the sync_rules of this GroupCreateResponseData.

        智能关联规则。

        :return: The sync_rules of this GroupCreateResponseData.
        :rtype: list[:class:`huaweicloudsdkcoc.v1.GroupUpdateRequestSyncRules`]
        """
        return self._sync_rules

    @sync_rules.setter
    def sync_rules(self, sync_rules):
        r"""Sets the sync_rules of this GroupCreateResponseData.

        智能关联规则。

        :param sync_rules: The sync_rules of this GroupCreateResponseData.
        :type sync_rules: list[:class:`huaweicloudsdkcoc.v1.GroupUpdateRequestSyncRules`]
        """
        self._sync_rules = sync_rules

    @property
    def related_domain_id(self):
        r"""Gets the related_domain_id of this GroupCreateResponseData.

        跨帐号资源所属的domainId。

        :return: The related_domain_id of this GroupCreateResponseData.
        :rtype: str
        """
        return self._related_domain_id

    @related_domain_id.setter
    def related_domain_id(self, related_domain_id):
        r"""Sets the related_domain_id of this GroupCreateResponseData.

        跨帐号资源所属的domainId。

        :param related_domain_id: The related_domain_id of this GroupCreateResponseData.
        :type related_domain_id: str
        """
        self._related_domain_id = related_domain_id

    @property
    def relation_configurations(self):
        r"""Gets the relation_configurations of this GroupCreateResponseData.

        分组配置信息。

        :return: The relation_configurations of this GroupCreateResponseData.
        :rtype: list[:class:`huaweicloudsdkcoc.v1.GroupRelationConfiguration`]
        """
        return self._relation_configurations

    @relation_configurations.setter
    def relation_configurations(self, relation_configurations):
        r"""Sets the relation_configurations of this GroupCreateResponseData.

        分组配置信息。

        :param relation_configurations: The relation_configurations of this GroupCreateResponseData.
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
        if not isinstance(other, GroupCreateResponseData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
