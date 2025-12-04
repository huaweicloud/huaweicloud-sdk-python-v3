# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GroupCreateRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'component_id': 'str',
        'vendor': 'str',
        'region_id': 'str',
        'application_id': 'str',
        'sync_mode': 'str',
        'sync_rules': 'list[GroupUpdateRequestSyncRules]',
        'relation_configurations': 'list[GroupRelationConfiguration]',
        'related_domain_id': 'str'
    }

    attribute_map = {
        'name': 'name',
        'component_id': 'component_id',
        'vendor': 'vendor',
        'region_id': 'region_id',
        'application_id': 'application_id',
        'sync_mode': 'sync_mode',
        'sync_rules': 'sync_rules',
        'relation_configurations': 'relation_configurations',
        'related_domain_id': 'related_domain_id'
    }

    def __init__(self, name=None, component_id=None, vendor=None, region_id=None, application_id=None, sync_mode=None, sync_rules=None, relation_configurations=None, related_domain_id=None):
        r"""GroupCreateRequest

        The model defined in huaweicloud sdk

        :param name: 分组名称。
        :type name: str
        :param component_id: 组件id。
        :type component_id: str
        :param vendor: 厂商（默认RMS，可填RMS/ALI/OTHER）。
        :type vendor: str
        :param region_id: region id。
        :type region_id: str
        :param application_id: 应用id。
        :type application_id: str
        :param sync_mode: 资源同步方式，MANUAL表示手动，AUTO表示智能关联。
        :type sync_mode: str
        :param sync_rules: 智能关联规则。
        :type sync_rules: list[:class:`huaweicloudsdkcoc.v1.GroupUpdateRequestSyncRules`]
        :param relation_configurations: 分组配置信息。
        :type relation_configurations: list[:class:`huaweicloudsdkcoc.v1.GroupRelationConfiguration`]
        :param related_domain_id: 关联帐号id。
        :type related_domain_id: str
        """
        
        

        self._name = None
        self._component_id = None
        self._vendor = None
        self._region_id = None
        self._application_id = None
        self._sync_mode = None
        self._sync_rules = None
        self._relation_configurations = None
        self._related_domain_id = None
        self.discriminator = None

        self.name = name
        self.component_id = component_id
        if vendor is not None:
            self.vendor = vendor
        self.region_id = region_id
        if application_id is not None:
            self.application_id = application_id
        self.sync_mode = sync_mode
        if sync_rules is not None:
            self.sync_rules = sync_rules
        if relation_configurations is not None:
            self.relation_configurations = relation_configurations
        if related_domain_id is not None:
            self.related_domain_id = related_domain_id

    @property
    def name(self):
        r"""Gets the name of this GroupCreateRequest.

        分组名称。

        :return: The name of this GroupCreateRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this GroupCreateRequest.

        分组名称。

        :param name: The name of this GroupCreateRequest.
        :type name: str
        """
        self._name = name

    @property
    def component_id(self):
        r"""Gets the component_id of this GroupCreateRequest.

        组件id。

        :return: The component_id of this GroupCreateRequest.
        :rtype: str
        """
        return self._component_id

    @component_id.setter
    def component_id(self, component_id):
        r"""Sets the component_id of this GroupCreateRequest.

        组件id。

        :param component_id: The component_id of this GroupCreateRequest.
        :type component_id: str
        """
        self._component_id = component_id

    @property
    def vendor(self):
        r"""Gets the vendor of this GroupCreateRequest.

        厂商（默认RMS，可填RMS/ALI/OTHER）。

        :return: The vendor of this GroupCreateRequest.
        :rtype: str
        """
        return self._vendor

    @vendor.setter
    def vendor(self, vendor):
        r"""Sets the vendor of this GroupCreateRequest.

        厂商（默认RMS，可填RMS/ALI/OTHER）。

        :param vendor: The vendor of this GroupCreateRequest.
        :type vendor: str
        """
        self._vendor = vendor

    @property
    def region_id(self):
        r"""Gets the region_id of this GroupCreateRequest.

        region id。

        :return: The region_id of this GroupCreateRequest.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        r"""Sets the region_id of this GroupCreateRequest.

        region id。

        :param region_id: The region_id of this GroupCreateRequest.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def application_id(self):
        r"""Gets the application_id of this GroupCreateRequest.

        应用id。

        :return: The application_id of this GroupCreateRequest.
        :rtype: str
        """
        return self._application_id

    @application_id.setter
    def application_id(self, application_id):
        r"""Sets the application_id of this GroupCreateRequest.

        应用id。

        :param application_id: The application_id of this GroupCreateRequest.
        :type application_id: str
        """
        self._application_id = application_id

    @property
    def sync_mode(self):
        r"""Gets the sync_mode of this GroupCreateRequest.

        资源同步方式，MANUAL表示手动，AUTO表示智能关联。

        :return: The sync_mode of this GroupCreateRequest.
        :rtype: str
        """
        return self._sync_mode

    @sync_mode.setter
    def sync_mode(self, sync_mode):
        r"""Sets the sync_mode of this GroupCreateRequest.

        资源同步方式，MANUAL表示手动，AUTO表示智能关联。

        :param sync_mode: The sync_mode of this GroupCreateRequest.
        :type sync_mode: str
        """
        self._sync_mode = sync_mode

    @property
    def sync_rules(self):
        r"""Gets the sync_rules of this GroupCreateRequest.

        智能关联规则。

        :return: The sync_rules of this GroupCreateRequest.
        :rtype: list[:class:`huaweicloudsdkcoc.v1.GroupUpdateRequestSyncRules`]
        """
        return self._sync_rules

    @sync_rules.setter
    def sync_rules(self, sync_rules):
        r"""Sets the sync_rules of this GroupCreateRequest.

        智能关联规则。

        :param sync_rules: The sync_rules of this GroupCreateRequest.
        :type sync_rules: list[:class:`huaweicloudsdkcoc.v1.GroupUpdateRequestSyncRules`]
        """
        self._sync_rules = sync_rules

    @property
    def relation_configurations(self):
        r"""Gets the relation_configurations of this GroupCreateRequest.

        分组配置信息。

        :return: The relation_configurations of this GroupCreateRequest.
        :rtype: list[:class:`huaweicloudsdkcoc.v1.GroupRelationConfiguration`]
        """
        return self._relation_configurations

    @relation_configurations.setter
    def relation_configurations(self, relation_configurations):
        r"""Sets the relation_configurations of this GroupCreateRequest.

        分组配置信息。

        :param relation_configurations: The relation_configurations of this GroupCreateRequest.
        :type relation_configurations: list[:class:`huaweicloudsdkcoc.v1.GroupRelationConfiguration`]
        """
        self._relation_configurations = relation_configurations

    @property
    def related_domain_id(self):
        r"""Gets the related_domain_id of this GroupCreateRequest.

        关联帐号id。

        :return: The related_domain_id of this GroupCreateRequest.
        :rtype: str
        """
        return self._related_domain_id

    @related_domain_id.setter
    def related_domain_id(self, related_domain_id):
        r"""Sets the related_domain_id of this GroupCreateRequest.

        关联帐号id。

        :param related_domain_id: The related_domain_id of this GroupCreateRequest.
        :type related_domain_id: str
        """
        self._related_domain_id = related_domain_id

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
        if not isinstance(other, GroupCreateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
