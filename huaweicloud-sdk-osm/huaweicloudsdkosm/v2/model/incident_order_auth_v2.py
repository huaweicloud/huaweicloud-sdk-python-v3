# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IncidentOrderAuthV2:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'id': 'int',
        'status': 'int',
        'incident_id': 'str',
        'simple_description': 'str',
        'resource_type_name': 'str',
        'visit_type_name': 'str',
        'create_time': 'datetime',
        'auth_effective_time': 'datetime',
        'auth_expire_time': 'datetime',
        'reject_reason': 'str',
        'customer_id': 'str',
        'x_customer_id': 'str',
        'x_customer_name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'status': 'status',
        'incident_id': 'incident_id',
        'simple_description': 'simple_description',
        'resource_type_name': 'resource_type_name',
        'visit_type_name': 'visit_type_name',
        'create_time': 'create_time',
        'auth_effective_time': 'auth_effective_time',
        'auth_expire_time': 'auth_expire_time',
        'reject_reason': 'reject_reason',
        'customer_id': 'customer_id',
        'x_customer_id': 'x_customer_id',
        'x_customer_name': 'x_customer_name'
    }

    def __init__(self, id=None, status=None, incident_id=None, simple_description=None, resource_type_name=None, visit_type_name=None, create_time=None, auth_effective_time=None, auth_expire_time=None, reject_reason=None, customer_id=None, x_customer_id=None, x_customer_name=None):
        """IncidentOrderAuthV2 - a model defined in huaweicloud sdk"""
        
        

        self._id = None
        self._status = None
        self._incident_id = None
        self._simple_description = None
        self._resource_type_name = None
        self._visit_type_name = None
        self._create_time = None
        self._auth_effective_time = None
        self._auth_expire_time = None
        self._reject_reason = None
        self._customer_id = None
        self._x_customer_id = None
        self._x_customer_name = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if status is not None:
            self.status = status
        if incident_id is not None:
            self.incident_id = incident_id
        if simple_description is not None:
            self.simple_description = simple_description
        if resource_type_name is not None:
            self.resource_type_name = resource_type_name
        if visit_type_name is not None:
            self.visit_type_name = visit_type_name
        if create_time is not None:
            self.create_time = create_time
        if auth_effective_time is not None:
            self.auth_effective_time = auth_effective_time
        if auth_expire_time is not None:
            self.auth_expire_time = auth_expire_time
        if reject_reason is not None:
            self.reject_reason = reject_reason
        if customer_id is not None:
            self.customer_id = customer_id
        if x_customer_id is not None:
            self.x_customer_id = x_customer_id
        if x_customer_name is not None:
            self.x_customer_name = x_customer_name

    @property
    def id(self):
        """Gets the id of this IncidentOrderAuthV2.

        授权id

        :return: The id of this IncidentOrderAuthV2.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this IncidentOrderAuthV2.

        授权id

        :param id: The id of this IncidentOrderAuthV2.
        :type: int
        """
        self._id = id

    @property
    def status(self):
        """Gets the status of this IncidentOrderAuthV2.

        授权状态

        :return: The status of this IncidentOrderAuthV2.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this IncidentOrderAuthV2.

        授权状态

        :param status: The status of this IncidentOrderAuthV2.
        :type: int
        """
        self._status = status

    @property
    def incident_id(self):
        """Gets the incident_id of this IncidentOrderAuthV2.

        工单id

        :return: The incident_id of this IncidentOrderAuthV2.
        :rtype: str
        """
        return self._incident_id

    @incident_id.setter
    def incident_id(self, incident_id):
        """Sets the incident_id of this IncidentOrderAuthV2.

        工单id

        :param incident_id: The incident_id of this IncidentOrderAuthV2.
        :type: str
        """
        self._incident_id = incident_id

    @property
    def simple_description(self):
        """Gets the simple_description of this IncidentOrderAuthV2.

        简要描述

        :return: The simple_description of this IncidentOrderAuthV2.
        :rtype: str
        """
        return self._simple_description

    @simple_description.setter
    def simple_description(self, simple_description):
        """Sets the simple_description of this IncidentOrderAuthV2.

        简要描述

        :param simple_description: The simple_description of this IncidentOrderAuthV2.
        :type: str
        """
        self._simple_description = simple_description

    @property
    def resource_type_name(self):
        """Gets the resource_type_name of this IncidentOrderAuthV2.

        授权资源类型名称

        :return: The resource_type_name of this IncidentOrderAuthV2.
        :rtype: str
        """
        return self._resource_type_name

    @resource_type_name.setter
    def resource_type_name(self, resource_type_name):
        """Sets the resource_type_name of this IncidentOrderAuthV2.

        授权资源类型名称

        :param resource_type_name: The resource_type_name of this IncidentOrderAuthV2.
        :type: str
        """
        self._resource_type_name = resource_type_name

    @property
    def visit_type_name(self):
        """Gets the visit_type_name of this IncidentOrderAuthV2.

        授权访问类型名称

        :return: The visit_type_name of this IncidentOrderAuthV2.
        :rtype: str
        """
        return self._visit_type_name

    @visit_type_name.setter
    def visit_type_name(self, visit_type_name):
        """Sets the visit_type_name of this IncidentOrderAuthV2.

        授权访问类型名称

        :param visit_type_name: The visit_type_name of this IncidentOrderAuthV2.
        :type: str
        """
        self._visit_type_name = visit_type_name

    @property
    def create_time(self):
        """Gets the create_time of this IncidentOrderAuthV2.

        创建时间

        :return: The create_time of this IncidentOrderAuthV2.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this IncidentOrderAuthV2.

        创建时间

        :param create_time: The create_time of this IncidentOrderAuthV2.
        :type: datetime
        """
        self._create_time = create_time

    @property
    def auth_effective_time(self):
        """Gets the auth_effective_time of this IncidentOrderAuthV2.

        授权生效时间

        :return: The auth_effective_time of this IncidentOrderAuthV2.
        :rtype: datetime
        """
        return self._auth_effective_time

    @auth_effective_time.setter
    def auth_effective_time(self, auth_effective_time):
        """Sets the auth_effective_time of this IncidentOrderAuthV2.

        授权生效时间

        :param auth_effective_time: The auth_effective_time of this IncidentOrderAuthV2.
        :type: datetime
        """
        self._auth_effective_time = auth_effective_time

    @property
    def auth_expire_time(self):
        """Gets the auth_expire_time of this IncidentOrderAuthV2.

        授权到期时间

        :return: The auth_expire_time of this IncidentOrderAuthV2.
        :rtype: datetime
        """
        return self._auth_expire_time

    @auth_expire_time.setter
    def auth_expire_time(self, auth_expire_time):
        """Sets the auth_expire_time of this IncidentOrderAuthV2.

        授权到期时间

        :param auth_expire_time: The auth_expire_time of this IncidentOrderAuthV2.
        :type: datetime
        """
        self._auth_expire_time = auth_expire_time

    @property
    def reject_reason(self):
        """Gets the reject_reason of this IncidentOrderAuthV2.

        拒绝原因

        :return: The reject_reason of this IncidentOrderAuthV2.
        :rtype: str
        """
        return self._reject_reason

    @reject_reason.setter
    def reject_reason(self, reject_reason):
        """Sets the reject_reason of this IncidentOrderAuthV2.

        拒绝原因

        :param reject_reason: The reject_reason of this IncidentOrderAuthV2.
        :type: str
        """
        self._reject_reason = reject_reason

    @property
    def customer_id(self):
        """Gets the customer_id of this IncidentOrderAuthV2.

        主账号id

        :return: The customer_id of this IncidentOrderAuthV2.
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this IncidentOrderAuthV2.

        主账号id

        :param customer_id: The customer_id of this IncidentOrderAuthV2.
        :type: str
        """
        self._customer_id = customer_id

    @property
    def x_customer_id(self):
        """Gets the x_customer_id of this IncidentOrderAuthV2.

        子用户id

        :return: The x_customer_id of this IncidentOrderAuthV2.
        :rtype: str
        """
        return self._x_customer_id

    @x_customer_id.setter
    def x_customer_id(self, x_customer_id):
        """Sets the x_customer_id of this IncidentOrderAuthV2.

        子用户id

        :param x_customer_id: The x_customer_id of this IncidentOrderAuthV2.
        :type: str
        """
        self._x_customer_id = x_customer_id

    @property
    def x_customer_name(self):
        """Gets the x_customer_name of this IncidentOrderAuthV2.

        子用户名称

        :return: The x_customer_name of this IncidentOrderAuthV2.
        :rtype: str
        """
        return self._x_customer_name

    @x_customer_name.setter
    def x_customer_name(self, x_customer_name):
        """Sets the x_customer_name of this IncidentOrderAuthV2.

        子用户名称

        :param x_customer_name: The x_customer_name of this IncidentOrderAuthV2.
        :type: str
        """
        self._x_customer_name = x_customer_name

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
        if not isinstance(other, IncidentOrderAuthV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
