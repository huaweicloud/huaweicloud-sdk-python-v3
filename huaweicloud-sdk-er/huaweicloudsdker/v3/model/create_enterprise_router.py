# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateEnterpriseRouter:

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
        'description': 'str',
        'asn': 'int',
        'enterprise_project_id': 'str',
        'charge_mode': 'str',
        'tags': 'list[Tag]',
        'enable_default_propagation': 'bool',
        'enable_default_association': 'bool',
        'availability_zone_ids': 'list[str]',
        'auto_accept_shared_attachments': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'asn': 'asn',
        'enterprise_project_id': 'enterprise_project_id',
        'charge_mode': 'charge_mode',
        'tags': 'tags',
        'enable_default_propagation': 'enable_default_propagation',
        'enable_default_association': 'enable_default_association',
        'availability_zone_ids': 'availability_zone_ids',
        'auto_accept_shared_attachments': 'auto_accept_shared_attachments'
    }

    def __init__(self, name=None, description=None, asn=None, enterprise_project_id=None, charge_mode=None, tags=None, enable_default_propagation=None, enable_default_association=None, availability_zone_ids=None, auto_accept_shared_attachments=None):
        """CreateEnterpriseRouter

        The model defined in huaweicloud sdk

        :param name: 企业路由器实例名称
        :type name: str
        :param description: 企业路由器实例描述信息
        :type description: str
        :param asn: 企业路由器实例的BGP AS号
        :type asn: int
        :param enterprise_project_id: 企业项目ID
        :type enterprise_project_id: str
        :param charge_mode: 计费模式 按需
        :type charge_mode: str
        :param tags: 标签信息
        :type tags: list[:class:`huaweicloudsdker.v3.Tag`]
        :param enable_default_propagation: 是否开启默认路由表传播，默认false不开启
        :type enable_default_propagation: bool
        :param enable_default_association: 是否开启默认路由表关联，默认false不开启
        :type enable_default_association: bool
        :param availability_zone_ids: 企业路由器所在的可用区列表
        :type availability_zone_ids: list[str]
        :param auto_accept_shared_attachments: 是否开启自动接受共享连接创建，默认false不开启
        :type auto_accept_shared_attachments: bool
        """
        
        

        self._name = None
        self._description = None
        self._asn = None
        self._enterprise_project_id = None
        self._charge_mode = None
        self._tags = None
        self._enable_default_propagation = None
        self._enable_default_association = None
        self._availability_zone_ids = None
        self._auto_accept_shared_attachments = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        self.asn = asn
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if charge_mode is not None:
            self.charge_mode = charge_mode
        if tags is not None:
            self.tags = tags
        if enable_default_propagation is not None:
            self.enable_default_propagation = enable_default_propagation
        if enable_default_association is not None:
            self.enable_default_association = enable_default_association
        self.availability_zone_ids = availability_zone_ids
        if auto_accept_shared_attachments is not None:
            self.auto_accept_shared_attachments = auto_accept_shared_attachments

    @property
    def name(self):
        """Gets the name of this CreateEnterpriseRouter.

        企业路由器实例名称

        :return: The name of this CreateEnterpriseRouter.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateEnterpriseRouter.

        企业路由器实例名称

        :param name: The name of this CreateEnterpriseRouter.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this CreateEnterpriseRouter.

        企业路由器实例描述信息

        :return: The description of this CreateEnterpriseRouter.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateEnterpriseRouter.

        企业路由器实例描述信息

        :param description: The description of this CreateEnterpriseRouter.
        :type description: str
        """
        self._description = description

    @property
    def asn(self):
        """Gets the asn of this CreateEnterpriseRouter.

        企业路由器实例的BGP AS号

        :return: The asn of this CreateEnterpriseRouter.
        :rtype: int
        """
        return self._asn

    @asn.setter
    def asn(self, asn):
        """Sets the asn of this CreateEnterpriseRouter.

        企业路由器实例的BGP AS号

        :param asn: The asn of this CreateEnterpriseRouter.
        :type asn: int
        """
        self._asn = asn

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this CreateEnterpriseRouter.

        企业项目ID

        :return: The enterprise_project_id of this CreateEnterpriseRouter.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this CreateEnterpriseRouter.

        企业项目ID

        :param enterprise_project_id: The enterprise_project_id of this CreateEnterpriseRouter.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def charge_mode(self):
        """Gets the charge_mode of this CreateEnterpriseRouter.

        计费模式 按需

        :return: The charge_mode of this CreateEnterpriseRouter.
        :rtype: str
        """
        return self._charge_mode

    @charge_mode.setter
    def charge_mode(self, charge_mode):
        """Sets the charge_mode of this CreateEnterpriseRouter.

        计费模式 按需

        :param charge_mode: The charge_mode of this CreateEnterpriseRouter.
        :type charge_mode: str
        """
        self._charge_mode = charge_mode

    @property
    def tags(self):
        """Gets the tags of this CreateEnterpriseRouter.

        标签信息

        :return: The tags of this CreateEnterpriseRouter.
        :rtype: list[:class:`huaweicloudsdker.v3.Tag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this CreateEnterpriseRouter.

        标签信息

        :param tags: The tags of this CreateEnterpriseRouter.
        :type tags: list[:class:`huaweicloudsdker.v3.Tag`]
        """
        self._tags = tags

    @property
    def enable_default_propagation(self):
        """Gets the enable_default_propagation of this CreateEnterpriseRouter.

        是否开启默认路由表传播，默认false不开启

        :return: The enable_default_propagation of this CreateEnterpriseRouter.
        :rtype: bool
        """
        return self._enable_default_propagation

    @enable_default_propagation.setter
    def enable_default_propagation(self, enable_default_propagation):
        """Sets the enable_default_propagation of this CreateEnterpriseRouter.

        是否开启默认路由表传播，默认false不开启

        :param enable_default_propagation: The enable_default_propagation of this CreateEnterpriseRouter.
        :type enable_default_propagation: bool
        """
        self._enable_default_propagation = enable_default_propagation

    @property
    def enable_default_association(self):
        """Gets the enable_default_association of this CreateEnterpriseRouter.

        是否开启默认路由表关联，默认false不开启

        :return: The enable_default_association of this CreateEnterpriseRouter.
        :rtype: bool
        """
        return self._enable_default_association

    @enable_default_association.setter
    def enable_default_association(self, enable_default_association):
        """Sets the enable_default_association of this CreateEnterpriseRouter.

        是否开启默认路由表关联，默认false不开启

        :param enable_default_association: The enable_default_association of this CreateEnterpriseRouter.
        :type enable_default_association: bool
        """
        self._enable_default_association = enable_default_association

    @property
    def availability_zone_ids(self):
        """Gets the availability_zone_ids of this CreateEnterpriseRouter.

        企业路由器所在的可用区列表

        :return: The availability_zone_ids of this CreateEnterpriseRouter.
        :rtype: list[str]
        """
        return self._availability_zone_ids

    @availability_zone_ids.setter
    def availability_zone_ids(self, availability_zone_ids):
        """Sets the availability_zone_ids of this CreateEnterpriseRouter.

        企业路由器所在的可用区列表

        :param availability_zone_ids: The availability_zone_ids of this CreateEnterpriseRouter.
        :type availability_zone_ids: list[str]
        """
        self._availability_zone_ids = availability_zone_ids

    @property
    def auto_accept_shared_attachments(self):
        """Gets the auto_accept_shared_attachments of this CreateEnterpriseRouter.

        是否开启自动接受共享连接创建，默认false不开启

        :return: The auto_accept_shared_attachments of this CreateEnterpriseRouter.
        :rtype: bool
        """
        return self._auto_accept_shared_attachments

    @auto_accept_shared_attachments.setter
    def auto_accept_shared_attachments(self, auto_accept_shared_attachments):
        """Sets the auto_accept_shared_attachments of this CreateEnterpriseRouter.

        是否开启自动接受共享连接创建，默认false不开启

        :param auto_accept_shared_attachments: The auto_accept_shared_attachments of this CreateEnterpriseRouter.
        :type auto_accept_shared_attachments: bool
        """
        self._auto_accept_shared_attachments = auto_accept_shared_attachments

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
        if not isinstance(other, CreateEnterpriseRouter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
