# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AssociatedResourceSetting:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'setting_name': 'str',
        'master_service': 'str',
        'master_resource_type': 'str',
        'associated_service': 'str',
        'associated_resource_type': 'str',
        'support_existing_resource': 'bool',
        'support_auto_delete': 'bool',
        'region_ids': 'list[str]'
    }

    attribute_map = {
        'setting_name': 'setting_name',
        'master_service': 'master_service',
        'master_resource_type': 'master_resource_type',
        'associated_service': 'associated_service',
        'associated_resource_type': 'associated_resource_type',
        'support_existing_resource': 'support_existing_resource',
        'support_auto_delete': 'support_auto_delete',
        'region_ids': 'region_ids'
    }

    def __init__(self, setting_name=None, master_service=None, master_resource_type=None, associated_service=None, associated_resource_type=None, support_existing_resource=None, support_auto_delete=None, region_ids=None):
        r"""AssociatedResourceSetting

        The model defined in huaweicloud sdk

        :param setting_name: 规则的配置名称
        :type setting_name: str
        :param master_service: 主资源
        :type master_service: str
        :param master_resource_type: 主资源类型
        :type master_resource_type: str
        :param associated_service: 关联资源
        :type associated_service: str
        :param associated_resource_type: 关联资源类型
        :type associated_resource_type: str
        :param support_existing_resource: 是否规则是对存量资源生效。
        :type support_existing_resource: bool
        :param support_auto_delete: 是否支持关系解除后自动删除标签。
        :type support_auto_delete: bool
        :param region_ids: 规则配置支持的区域Id。
        :type region_ids: list[str]
        """
        
        

        self._setting_name = None
        self._master_service = None
        self._master_resource_type = None
        self._associated_service = None
        self._associated_resource_type = None
        self._support_existing_resource = None
        self._support_auto_delete = None
        self._region_ids = None
        self.discriminator = None

        if setting_name is not None:
            self.setting_name = setting_name
        if master_service is not None:
            self.master_service = master_service
        if master_resource_type is not None:
            self.master_resource_type = master_resource_type
        if associated_service is not None:
            self.associated_service = associated_service
        if associated_resource_type is not None:
            self.associated_resource_type = associated_resource_type
        if support_existing_resource is not None:
            self.support_existing_resource = support_existing_resource
        if support_auto_delete is not None:
            self.support_auto_delete = support_auto_delete
        if region_ids is not None:
            self.region_ids = region_ids

    @property
    def setting_name(self):
        r"""Gets the setting_name of this AssociatedResourceSetting.

        规则的配置名称

        :return: The setting_name of this AssociatedResourceSetting.
        :rtype: str
        """
        return self._setting_name

    @setting_name.setter
    def setting_name(self, setting_name):
        r"""Sets the setting_name of this AssociatedResourceSetting.

        规则的配置名称

        :param setting_name: The setting_name of this AssociatedResourceSetting.
        :type setting_name: str
        """
        self._setting_name = setting_name

    @property
    def master_service(self):
        r"""Gets the master_service of this AssociatedResourceSetting.

        主资源

        :return: The master_service of this AssociatedResourceSetting.
        :rtype: str
        """
        return self._master_service

    @master_service.setter
    def master_service(self, master_service):
        r"""Sets the master_service of this AssociatedResourceSetting.

        主资源

        :param master_service: The master_service of this AssociatedResourceSetting.
        :type master_service: str
        """
        self._master_service = master_service

    @property
    def master_resource_type(self):
        r"""Gets the master_resource_type of this AssociatedResourceSetting.

        主资源类型

        :return: The master_resource_type of this AssociatedResourceSetting.
        :rtype: str
        """
        return self._master_resource_type

    @master_resource_type.setter
    def master_resource_type(self, master_resource_type):
        r"""Sets the master_resource_type of this AssociatedResourceSetting.

        主资源类型

        :param master_resource_type: The master_resource_type of this AssociatedResourceSetting.
        :type master_resource_type: str
        """
        self._master_resource_type = master_resource_type

    @property
    def associated_service(self):
        r"""Gets the associated_service of this AssociatedResourceSetting.

        关联资源

        :return: The associated_service of this AssociatedResourceSetting.
        :rtype: str
        """
        return self._associated_service

    @associated_service.setter
    def associated_service(self, associated_service):
        r"""Sets the associated_service of this AssociatedResourceSetting.

        关联资源

        :param associated_service: The associated_service of this AssociatedResourceSetting.
        :type associated_service: str
        """
        self._associated_service = associated_service

    @property
    def associated_resource_type(self):
        r"""Gets the associated_resource_type of this AssociatedResourceSetting.

        关联资源类型

        :return: The associated_resource_type of this AssociatedResourceSetting.
        :rtype: str
        """
        return self._associated_resource_type

    @associated_resource_type.setter
    def associated_resource_type(self, associated_resource_type):
        r"""Sets the associated_resource_type of this AssociatedResourceSetting.

        关联资源类型

        :param associated_resource_type: The associated_resource_type of this AssociatedResourceSetting.
        :type associated_resource_type: str
        """
        self._associated_resource_type = associated_resource_type

    @property
    def support_existing_resource(self):
        r"""Gets the support_existing_resource of this AssociatedResourceSetting.

        是否规则是对存量资源生效。

        :return: The support_existing_resource of this AssociatedResourceSetting.
        :rtype: bool
        """
        return self._support_existing_resource

    @support_existing_resource.setter
    def support_existing_resource(self, support_existing_resource):
        r"""Sets the support_existing_resource of this AssociatedResourceSetting.

        是否规则是对存量资源生效。

        :param support_existing_resource: The support_existing_resource of this AssociatedResourceSetting.
        :type support_existing_resource: bool
        """
        self._support_existing_resource = support_existing_resource

    @property
    def support_auto_delete(self):
        r"""Gets the support_auto_delete of this AssociatedResourceSetting.

        是否支持关系解除后自动删除标签。

        :return: The support_auto_delete of this AssociatedResourceSetting.
        :rtype: bool
        """
        return self._support_auto_delete

    @support_auto_delete.setter
    def support_auto_delete(self, support_auto_delete):
        r"""Sets the support_auto_delete of this AssociatedResourceSetting.

        是否支持关系解除后自动删除标签。

        :param support_auto_delete: The support_auto_delete of this AssociatedResourceSetting.
        :type support_auto_delete: bool
        """
        self._support_auto_delete = support_auto_delete

    @property
    def region_ids(self):
        r"""Gets the region_ids of this AssociatedResourceSetting.

        规则配置支持的区域Id。

        :return: The region_ids of this AssociatedResourceSetting.
        :rtype: list[str]
        """
        return self._region_ids

    @region_ids.setter
    def region_ids(self, region_ids):
        r"""Sets the region_ids of this AssociatedResourceSetting.

        规则配置支持的区域Id。

        :param region_ids: The region_ids of this AssociatedResourceSetting.
        :type region_ids: list[str]
        """
        self._region_ids = region_ids

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
        if not isinstance(other, AssociatedResourceSetting):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
