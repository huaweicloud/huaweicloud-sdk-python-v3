# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateEnterpriseRouter:

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
        'enable_default_propagation': 'bool',
        'enable_default_association': 'bool',
        'default_propagation_route_table_id': 'str',
        'default_association_route_table_id': 'str',
        'auto_accept_shared_attachments': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'enable_default_propagation': 'enable_default_propagation',
        'enable_default_association': 'enable_default_association',
        'default_propagation_route_table_id': 'default_propagation_route_table_id',
        'default_association_route_table_id': 'default_association_route_table_id',
        'auto_accept_shared_attachments': 'auto_accept_shared_attachments'
    }

    def __init__(self, name=None, description=None, enable_default_propagation=None, enable_default_association=None, default_propagation_route_table_id=None, default_association_route_table_id=None, auto_accept_shared_attachments=None):
        """UpdateEnterpriseRouter

        The model defined in huaweicloud sdk

        :param name: 企业路由器实例名称
        :type name: str
        :param description: 企业路由器实例描述信息
        :type description: str
        :param enable_default_propagation: 是否开启默认传播
        :type enable_default_propagation: bool
        :param enable_default_association: 是否开启默认关联
        :type enable_default_association: bool
        :param default_propagation_route_table_id: 默认传播路由表ID
        :type default_propagation_route_table_id: str
        :param default_association_route_table_id: 默认关联路由表ID
        :type default_association_route_table_id: str
        :param auto_accept_shared_attachments: 是否自动接受共享连接创建，默认false不开启
        :type auto_accept_shared_attachments: bool
        """
        
        

        self._name = None
        self._description = None
        self._enable_default_propagation = None
        self._enable_default_association = None
        self._default_propagation_route_table_id = None
        self._default_association_route_table_id = None
        self._auto_accept_shared_attachments = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if enable_default_propagation is not None:
            self.enable_default_propagation = enable_default_propagation
        if enable_default_association is not None:
            self.enable_default_association = enable_default_association
        if default_propagation_route_table_id is not None:
            self.default_propagation_route_table_id = default_propagation_route_table_id
        if default_association_route_table_id is not None:
            self.default_association_route_table_id = default_association_route_table_id
        if auto_accept_shared_attachments is not None:
            self.auto_accept_shared_attachments = auto_accept_shared_attachments

    @property
    def name(self):
        """Gets the name of this UpdateEnterpriseRouter.

        企业路由器实例名称

        :return: The name of this UpdateEnterpriseRouter.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateEnterpriseRouter.

        企业路由器实例名称

        :param name: The name of this UpdateEnterpriseRouter.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this UpdateEnterpriseRouter.

        企业路由器实例描述信息

        :return: The description of this UpdateEnterpriseRouter.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateEnterpriseRouter.

        企业路由器实例描述信息

        :param description: The description of this UpdateEnterpriseRouter.
        :type description: str
        """
        self._description = description

    @property
    def enable_default_propagation(self):
        """Gets the enable_default_propagation of this UpdateEnterpriseRouter.

        是否开启默认传播

        :return: The enable_default_propagation of this UpdateEnterpriseRouter.
        :rtype: bool
        """
        return self._enable_default_propagation

    @enable_default_propagation.setter
    def enable_default_propagation(self, enable_default_propagation):
        """Sets the enable_default_propagation of this UpdateEnterpriseRouter.

        是否开启默认传播

        :param enable_default_propagation: The enable_default_propagation of this UpdateEnterpriseRouter.
        :type enable_default_propagation: bool
        """
        self._enable_default_propagation = enable_default_propagation

    @property
    def enable_default_association(self):
        """Gets the enable_default_association of this UpdateEnterpriseRouter.

        是否开启默认关联

        :return: The enable_default_association of this UpdateEnterpriseRouter.
        :rtype: bool
        """
        return self._enable_default_association

    @enable_default_association.setter
    def enable_default_association(self, enable_default_association):
        """Sets the enable_default_association of this UpdateEnterpriseRouter.

        是否开启默认关联

        :param enable_default_association: The enable_default_association of this UpdateEnterpriseRouter.
        :type enable_default_association: bool
        """
        self._enable_default_association = enable_default_association

    @property
    def default_propagation_route_table_id(self):
        """Gets the default_propagation_route_table_id of this UpdateEnterpriseRouter.

        默认传播路由表ID

        :return: The default_propagation_route_table_id of this UpdateEnterpriseRouter.
        :rtype: str
        """
        return self._default_propagation_route_table_id

    @default_propagation_route_table_id.setter
    def default_propagation_route_table_id(self, default_propagation_route_table_id):
        """Sets the default_propagation_route_table_id of this UpdateEnterpriseRouter.

        默认传播路由表ID

        :param default_propagation_route_table_id: The default_propagation_route_table_id of this UpdateEnterpriseRouter.
        :type default_propagation_route_table_id: str
        """
        self._default_propagation_route_table_id = default_propagation_route_table_id

    @property
    def default_association_route_table_id(self):
        """Gets the default_association_route_table_id of this UpdateEnterpriseRouter.

        默认关联路由表ID

        :return: The default_association_route_table_id of this UpdateEnterpriseRouter.
        :rtype: str
        """
        return self._default_association_route_table_id

    @default_association_route_table_id.setter
    def default_association_route_table_id(self, default_association_route_table_id):
        """Sets the default_association_route_table_id of this UpdateEnterpriseRouter.

        默认关联路由表ID

        :param default_association_route_table_id: The default_association_route_table_id of this UpdateEnterpriseRouter.
        :type default_association_route_table_id: str
        """
        self._default_association_route_table_id = default_association_route_table_id

    @property
    def auto_accept_shared_attachments(self):
        """Gets the auto_accept_shared_attachments of this UpdateEnterpriseRouter.

        是否自动接受共享连接创建，默认false不开启

        :return: The auto_accept_shared_attachments of this UpdateEnterpriseRouter.
        :rtype: bool
        """
        return self._auto_accept_shared_attachments

    @auto_accept_shared_attachments.setter
    def auto_accept_shared_attachments(self, auto_accept_shared_attachments):
        """Sets the auto_accept_shared_attachments of this UpdateEnterpriseRouter.

        是否自动接受共享连接创建，默认false不开启

        :param auto_accept_shared_attachments: The auto_accept_shared_attachments of this UpdateEnterpriseRouter.
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
        if not isinstance(other, UpdateEnterpriseRouter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
