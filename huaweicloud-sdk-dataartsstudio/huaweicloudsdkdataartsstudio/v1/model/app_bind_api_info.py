# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AppBindApiInfo:

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
        'description': 'str',
        'approval_time': 'int',
        'manager': 'str',
        'deadline': 'int',
        'relationship_type': 'str',
        'static_params': 'list[StaticParam]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'approval_time': 'approval_time',
        'manager': 'manager',
        'deadline': 'deadline',
        'relationship_type': 'relationship_type',
        'static_params': 'static_params'
    }

    def __init__(self, id=None, name=None, description=None, approval_time=None, manager=None, deadline=None, relationship_type=None, static_params=None):
        r"""AppBindApiInfo

        The model defined in huaweicloud sdk

        :param id: API ID
        :type id: str
        :param name: API名称
        :type name: str
        :param description: API描述
        :type description: str
        :param approval_time: 审核时间
        :type approval_time: int
        :param manager: API 审核人名称
        :type manager: str
        :param deadline: 使用截止时间
        :type deadline: int
        :param relationship_type: 绑定关系
        :type relationship_type: str
        :param static_params: 静态参数列表
        :type static_params: list[:class:`huaweicloudsdkdataartsstudio.v1.StaticParam`]
        """
        
        

        self._id = None
        self._name = None
        self._description = None
        self._approval_time = None
        self._manager = None
        self._deadline = None
        self._relationship_type = None
        self._static_params = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if approval_time is not None:
            self.approval_time = approval_time
        if manager is not None:
            self.manager = manager
        if deadline is not None:
            self.deadline = deadline
        if relationship_type is not None:
            self.relationship_type = relationship_type
        if static_params is not None:
            self.static_params = static_params

    @property
    def id(self):
        r"""Gets the id of this AppBindApiInfo.

        API ID

        :return: The id of this AppBindApiInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this AppBindApiInfo.

        API ID

        :param id: The id of this AppBindApiInfo.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this AppBindApiInfo.

        API名称

        :return: The name of this AppBindApiInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this AppBindApiInfo.

        API名称

        :param name: The name of this AppBindApiInfo.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this AppBindApiInfo.

        API描述

        :return: The description of this AppBindApiInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this AppBindApiInfo.

        API描述

        :param description: The description of this AppBindApiInfo.
        :type description: str
        """
        self._description = description

    @property
    def approval_time(self):
        r"""Gets the approval_time of this AppBindApiInfo.

        审核时间

        :return: The approval_time of this AppBindApiInfo.
        :rtype: int
        """
        return self._approval_time

    @approval_time.setter
    def approval_time(self, approval_time):
        r"""Sets the approval_time of this AppBindApiInfo.

        审核时间

        :param approval_time: The approval_time of this AppBindApiInfo.
        :type approval_time: int
        """
        self._approval_time = approval_time

    @property
    def manager(self):
        r"""Gets the manager of this AppBindApiInfo.

        API 审核人名称

        :return: The manager of this AppBindApiInfo.
        :rtype: str
        """
        return self._manager

    @manager.setter
    def manager(self, manager):
        r"""Sets the manager of this AppBindApiInfo.

        API 审核人名称

        :param manager: The manager of this AppBindApiInfo.
        :type manager: str
        """
        self._manager = manager

    @property
    def deadline(self):
        r"""Gets the deadline of this AppBindApiInfo.

        使用截止时间

        :return: The deadline of this AppBindApiInfo.
        :rtype: int
        """
        return self._deadline

    @deadline.setter
    def deadline(self, deadline):
        r"""Sets the deadline of this AppBindApiInfo.

        使用截止时间

        :param deadline: The deadline of this AppBindApiInfo.
        :type deadline: int
        """
        self._deadline = deadline

    @property
    def relationship_type(self):
        r"""Gets the relationship_type of this AppBindApiInfo.

        绑定关系

        :return: The relationship_type of this AppBindApiInfo.
        :rtype: str
        """
        return self._relationship_type

    @relationship_type.setter
    def relationship_type(self, relationship_type):
        r"""Sets the relationship_type of this AppBindApiInfo.

        绑定关系

        :param relationship_type: The relationship_type of this AppBindApiInfo.
        :type relationship_type: str
        """
        self._relationship_type = relationship_type

    @property
    def static_params(self):
        r"""Gets the static_params of this AppBindApiInfo.

        静态参数列表

        :return: The static_params of this AppBindApiInfo.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.StaticParam`]
        """
        return self._static_params

    @static_params.setter
    def static_params(self, static_params):
        r"""Sets the static_params of this AppBindApiInfo.

        静态参数列表

        :param static_params: The static_params of this AppBindApiInfo.
        :type static_params: list[:class:`huaweicloudsdkdataartsstudio.v1.StaticParam`]
        """
        self._static_params = static_params

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
        if not isinstance(other, AppBindApiInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
