# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TrafficMirrorFilter:

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
        'project_id': 'str',
        'description': 'str',
        'name': 'str',
        'ingress_rules': 'list[TrafficMirrorFilterRule]',
        'egress_rules': 'list[TrafficMirrorFilterRule]',
        'created_at': 'datetime',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'project_id': 'project_id',
        'description': 'description',
        'name': 'name',
        'ingress_rules': 'ingress_rules',
        'egress_rules': 'egress_rules',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, id=None, project_id=None, description=None, name=None, ingress_rules=None, egress_rules=None, created_at=None, updated_at=None):
        """TrafficMirrorFilter

        The model defined in huaweicloud sdk

        :param id: 功能说明：流量镜像筛选条件ID
        :type id: str
        :param project_id: 功能说明：项目ID
        :type project_id: str
        :param description: 功能说明：流量镜像筛选条件的描述信息 取值范围：0-255个字符，不能包含“&lt;”和“&gt;”
        :type description: str
        :param name: 功能说明：流量镜像筛选条件的名称 取值范围：1-64个字符，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）
        :type name: str
        :param ingress_rules: 功能说明：入方向筛选规则列表
        :type ingress_rules: list[:class:`huaweicloudsdkvpc.v3.TrafficMirrorFilterRule`]
        :param egress_rules: 功能说明：出方向筛选规则列表
        :type egress_rules: list[:class:`huaweicloudsdkvpc.v3.TrafficMirrorFilterRule`]
        :param created_at: 创建时间戳
        :type created_at: datetime
        :param updated_at: 更新时间戳
        :type updated_at: datetime
        """
        
        

        self._id = None
        self._project_id = None
        self._description = None
        self._name = None
        self._ingress_rules = None
        self._egress_rules = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        self.id = id
        self.project_id = project_id
        self.description = description
        self.name = name
        self.ingress_rules = ingress_rules
        self.egress_rules = egress_rules
        self.created_at = created_at
        self.updated_at = updated_at

    @property
    def id(self):
        """Gets the id of this TrafficMirrorFilter.

        功能说明：流量镜像筛选条件ID

        :return: The id of this TrafficMirrorFilter.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TrafficMirrorFilter.

        功能说明：流量镜像筛选条件ID

        :param id: The id of this TrafficMirrorFilter.
        :type id: str
        """
        self._id = id

    @property
    def project_id(self):
        """Gets the project_id of this TrafficMirrorFilter.

        功能说明：项目ID

        :return: The project_id of this TrafficMirrorFilter.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this TrafficMirrorFilter.

        功能说明：项目ID

        :param project_id: The project_id of this TrafficMirrorFilter.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def description(self):
        """Gets the description of this TrafficMirrorFilter.

        功能说明：流量镜像筛选条件的描述信息 取值范围：0-255个字符，不能包含“<”和“>”

        :return: The description of this TrafficMirrorFilter.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this TrafficMirrorFilter.

        功能说明：流量镜像筛选条件的描述信息 取值范围：0-255个字符，不能包含“<”和“>”

        :param description: The description of this TrafficMirrorFilter.
        :type description: str
        """
        self._description = description

    @property
    def name(self):
        """Gets the name of this TrafficMirrorFilter.

        功能说明：流量镜像筛选条件的名称 取值范围：1-64个字符，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）

        :return: The name of this TrafficMirrorFilter.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TrafficMirrorFilter.

        功能说明：流量镜像筛选条件的名称 取值范围：1-64个字符，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）

        :param name: The name of this TrafficMirrorFilter.
        :type name: str
        """
        self._name = name

    @property
    def ingress_rules(self):
        """Gets the ingress_rules of this TrafficMirrorFilter.

        功能说明：入方向筛选规则列表

        :return: The ingress_rules of this TrafficMirrorFilter.
        :rtype: list[:class:`huaweicloudsdkvpc.v3.TrafficMirrorFilterRule`]
        """
        return self._ingress_rules

    @ingress_rules.setter
    def ingress_rules(self, ingress_rules):
        """Sets the ingress_rules of this TrafficMirrorFilter.

        功能说明：入方向筛选规则列表

        :param ingress_rules: The ingress_rules of this TrafficMirrorFilter.
        :type ingress_rules: list[:class:`huaweicloudsdkvpc.v3.TrafficMirrorFilterRule`]
        """
        self._ingress_rules = ingress_rules

    @property
    def egress_rules(self):
        """Gets the egress_rules of this TrafficMirrorFilter.

        功能说明：出方向筛选规则列表

        :return: The egress_rules of this TrafficMirrorFilter.
        :rtype: list[:class:`huaweicloudsdkvpc.v3.TrafficMirrorFilterRule`]
        """
        return self._egress_rules

    @egress_rules.setter
    def egress_rules(self, egress_rules):
        """Sets the egress_rules of this TrafficMirrorFilter.

        功能说明：出方向筛选规则列表

        :param egress_rules: The egress_rules of this TrafficMirrorFilter.
        :type egress_rules: list[:class:`huaweicloudsdkvpc.v3.TrafficMirrorFilterRule`]
        """
        self._egress_rules = egress_rules

    @property
    def created_at(self):
        """Gets the created_at of this TrafficMirrorFilter.

        创建时间戳

        :return: The created_at of this TrafficMirrorFilter.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this TrafficMirrorFilter.

        创建时间戳

        :param created_at: The created_at of this TrafficMirrorFilter.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this TrafficMirrorFilter.

        更新时间戳

        :return: The updated_at of this TrafficMirrorFilter.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this TrafficMirrorFilter.

        更新时间戳

        :param updated_at: The updated_at of this TrafficMirrorFilter.
        :type updated_at: datetime
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
        if not isinstance(other, TrafficMirrorFilter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
