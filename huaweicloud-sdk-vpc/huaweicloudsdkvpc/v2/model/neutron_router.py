# coding: utf-8

import pprint
import re

import six


class NeutronRouter(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        'admin_state_up': 'bool',
        'external_gateway_info': 'ExternalGatewayInfo',
        'id': 'str',
        'name': 'str',
        'routes': 'list[Route]',
        'status': 'str',
        'tenant_id': 'str',
        'project_id': 'str',
        'created_at': 'str',
        'updated_at': 'str'
    }

    attribute_map = {
        'admin_state_up': 'admin_state_up',
        'external_gateway_info': 'external_gateway_info',
        'id': 'id',
        'name': 'name',
        'routes': 'routes',
        'status': 'status',
        'tenant_id': 'tenant_id',
        'project_id': 'project_id',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, admin_state_up=None, external_gateway_info=None, id=None, name=None, routes=None, status=None, tenant_id=None, project_id=None, created_at=None, updated_at=None):  # noqa: E501
        """NeutronRouter - a model defined in huaweicloud sdk"""

        self._admin_state_up = None
        self._external_gateway_info = None
        self._id = None
        self._name = None
        self._routes = None
        self._status = None
        self._tenant_id = None
        self._project_id = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        self.admin_state_up = admin_state_up
        self.external_gateway_info = external_gateway_info
        self.id = id
        self.name = name
        self.routes = routes
        self.status = status
        self.tenant_id = tenant_id
        self.project_id = project_id
        self.created_at = created_at
        self.updated_at = updated_at

    @property
    def admin_state_up(self):
        """Gets the admin_state_up of this NeutronRouter.

        功能说明：资源的管理状态。只支持true。 取值范围：true、false 约束：只支持true

        :return: The admin_state_up of this NeutronRouter.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        """Sets the admin_state_up of this NeutronRouter.

        功能说明：资源的管理状态。只支持true。 取值范围：true、false 约束：只支持true

        :param admin_state_up: The admin_state_up of this NeutronRouter.
        :type: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def external_gateway_info(self):
        """Gets the external_gateway_info of this NeutronRouter.


        :return: The external_gateway_info of this NeutronRouter.
        :rtype: ExternalGatewayInfo
        """
        return self._external_gateway_info

    @external_gateway_info.setter
    def external_gateway_info(self, external_gateway_info):
        """Sets the external_gateway_info of this NeutronRouter.


        :param external_gateway_info: The external_gateway_info of this NeutronRouter.
        :type: ExternalGatewayInfo
        """
        self._external_gateway_info = external_gateway_info

    @property
    def id(self):
        """Gets the id of this NeutronRouter.

        路由器ID

        :return: The id of this NeutronRouter.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NeutronRouter.

        路由器ID

        :param id: The id of this NeutronRouter.
        :type: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this NeutronRouter.

        功能说明：路由器的名称 取值范围：0-64个字符，仅支持数字、字母、中文、_(下划线)、-（中划线）、.（点）。 约束：如果name非空，则name不能重复。

        :return: The name of this NeutronRouter.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NeutronRouter.

        功能说明：路由器的名称 取值范围：0-64个字符，仅支持数字、字母、中文、_(下划线)、-（中划线）、.（点）。 约束：如果name非空，则name不能重复。

        :param name: The name of this NeutronRouter.
        :type: str
        """
        self._name = name

    @property
    def routes(self):
        """Gets the routes of this NeutronRouter.

        功能说明：路由信息，见Route对象

        :return: The routes of this NeutronRouter.
        :rtype: list[Route]
        """
        return self._routes

    @routes.setter
    def routes(self, routes):
        """Sets the routes of this NeutronRouter.

        功能说明：路由信息，见Route对象

        :param routes: The routes of this NeutronRouter.
        :type: list[Route]
        """
        self._routes = routes

    @property
    def status(self):
        """Gets the status of this NeutronRouter.

        功能说明：路由器的状态 取值范围：ACTIVE， DOWN，ERROR

        :return: The status of this NeutronRouter.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this NeutronRouter.

        功能说明：路由器的状态 取值范围：ACTIVE， DOWN，ERROR

        :param status: The status of this NeutronRouter.
        :type: str
        """
        self._status = status

    @property
    def tenant_id(self):
        """Gets the tenant_id of this NeutronRouter.

        项目ID

        :return: The tenant_id of this NeutronRouter.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this NeutronRouter.

        项目ID

        :param tenant_id: The tenant_id of this NeutronRouter.
        :type: str
        """
        self._tenant_id = tenant_id

    @property
    def project_id(self):
        """Gets the project_id of this NeutronRouter.

        项目ID

        :return: The project_id of this NeutronRouter.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this NeutronRouter.

        项目ID

        :param project_id: The project_id of this NeutronRouter.
        :type: str
        """
        self._project_id = project_id

    @property
    def created_at(self):
        """Gets the created_at of this NeutronRouter.

        功能说明：资源创建UTC时间 格式：yyyy-MM-ddTHH:mm:ss

        :return: The created_at of this NeutronRouter.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this NeutronRouter.

        功能说明：资源创建UTC时间 格式：yyyy-MM-ddTHH:mm:ss

        :param created_at: The created_at of this NeutronRouter.
        :type: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this NeutronRouter.

        功能说明：资源更新UTC时间 格式：yyyy-MM-ddTHH:mm:ss

        :return: The updated_at of this NeutronRouter.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this NeutronRouter.

        功能说明：资源更新UTC时间 格式：yyyy-MM-ddTHH:mm:ss

        :param updated_at: The updated_at of this NeutronRouter.
        :type: str
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
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, NeutronRouter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
