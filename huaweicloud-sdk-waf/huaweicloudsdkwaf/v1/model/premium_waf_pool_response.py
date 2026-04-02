# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PremiumWafPoolResponse:

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
        'region': 'str',
        'type': 'str',
        'vpc_id': 'str',
        'description': 'str',
        'hosts': 'list[IdNameEntry]',
        'instances': 'list[IdNameEntry]',
        'enterprise_project_id': 'str',
        'create_time': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'region': 'region',
        'type': 'type',
        'vpc_id': 'vpc_id',
        'description': 'description',
        'hosts': 'hosts',
        'instances': 'instances',
        'enterprise_project_id': 'enterprise_project_id',
        'create_time': 'create_time'
    }

    def __init__(self, id=None, name=None, region=None, type=None, vpc_id=None, description=None, hosts=None, instances=None, enterprise_project_id=None, create_time=None):
        r"""PremiumWafPoolResponse

        The model defined in huaweicloud sdk

        :param id: 实例组id
        :type id: str
        :param name: 实例组名称
        :type name: str
        :param region: 实例组所在region
        :type region: str
        :param type: 实例组类型
        :type type: str
        :param vpc_id: 实例组关联的vpc_id
        :type vpc_id: str
        :param description: 实例组描述
        :type description: str
        :param hosts: 实例组关联的防护域名
        :type hosts: list[:class:`huaweicloudsdkwaf.v1.IdNameEntry`]
        :param instances: 实例组关联的引擎实例
        :type instances: list[:class:`huaweicloudsdkwaf.v1.IdNameEntry`]
        :param enterprise_project_id: 实例组关联的企业计划id
        :type enterprise_project_id: str
        :param create_time: 实例组创建时间
        :type create_time: int
        """
        
        

        self._id = None
        self._name = None
        self._region = None
        self._type = None
        self._vpc_id = None
        self._description = None
        self._hosts = None
        self._instances = None
        self._enterprise_project_id = None
        self._create_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if region is not None:
            self.region = region
        if type is not None:
            self.type = type
        if vpc_id is not None:
            self.vpc_id = vpc_id
        if description is not None:
            self.description = description
        if hosts is not None:
            self.hosts = hosts
        if instances is not None:
            self.instances = instances
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if create_time is not None:
            self.create_time = create_time

    @property
    def id(self):
        r"""Gets the id of this PremiumWafPoolResponse.

        实例组id

        :return: The id of this PremiumWafPoolResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this PremiumWafPoolResponse.

        实例组id

        :param id: The id of this PremiumWafPoolResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this PremiumWafPoolResponse.

        实例组名称

        :return: The name of this PremiumWafPoolResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this PremiumWafPoolResponse.

        实例组名称

        :param name: The name of this PremiumWafPoolResponse.
        :type name: str
        """
        self._name = name

    @property
    def region(self):
        r"""Gets the region of this PremiumWafPoolResponse.

        实例组所在region

        :return: The region of this PremiumWafPoolResponse.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this PremiumWafPoolResponse.

        实例组所在region

        :param region: The region of this PremiumWafPoolResponse.
        :type region: str
        """
        self._region = region

    @property
    def type(self):
        r"""Gets the type of this PremiumWafPoolResponse.

        实例组类型

        :return: The type of this PremiumWafPoolResponse.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this PremiumWafPoolResponse.

        实例组类型

        :param type: The type of this PremiumWafPoolResponse.
        :type type: str
        """
        self._type = type

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this PremiumWafPoolResponse.

        实例组关联的vpc_id

        :return: The vpc_id of this PremiumWafPoolResponse.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this PremiumWafPoolResponse.

        实例组关联的vpc_id

        :param vpc_id: The vpc_id of this PremiumWafPoolResponse.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def description(self):
        r"""Gets the description of this PremiumWafPoolResponse.

        实例组描述

        :return: The description of this PremiumWafPoolResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this PremiumWafPoolResponse.

        实例组描述

        :param description: The description of this PremiumWafPoolResponse.
        :type description: str
        """
        self._description = description

    @property
    def hosts(self):
        r"""Gets the hosts of this PremiumWafPoolResponse.

        实例组关联的防护域名

        :return: The hosts of this PremiumWafPoolResponse.
        :rtype: list[:class:`huaweicloudsdkwaf.v1.IdNameEntry`]
        """
        return self._hosts

    @hosts.setter
    def hosts(self, hosts):
        r"""Sets the hosts of this PremiumWafPoolResponse.

        实例组关联的防护域名

        :param hosts: The hosts of this PremiumWafPoolResponse.
        :type hosts: list[:class:`huaweicloudsdkwaf.v1.IdNameEntry`]
        """
        self._hosts = hosts

    @property
    def instances(self):
        r"""Gets the instances of this PremiumWafPoolResponse.

        实例组关联的引擎实例

        :return: The instances of this PremiumWafPoolResponse.
        :rtype: list[:class:`huaweicloudsdkwaf.v1.IdNameEntry`]
        """
        return self._instances

    @instances.setter
    def instances(self, instances):
        r"""Sets the instances of this PremiumWafPoolResponse.

        实例组关联的引擎实例

        :param instances: The instances of this PremiumWafPoolResponse.
        :type instances: list[:class:`huaweicloudsdkwaf.v1.IdNameEntry`]
        """
        self._instances = instances

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this PremiumWafPoolResponse.

        实例组关联的企业计划id

        :return: The enterprise_project_id of this PremiumWafPoolResponse.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this PremiumWafPoolResponse.

        实例组关联的企业计划id

        :param enterprise_project_id: The enterprise_project_id of this PremiumWafPoolResponse.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def create_time(self):
        r"""Gets the create_time of this PremiumWafPoolResponse.

        实例组创建时间

        :return: The create_time of this PremiumWafPoolResponse.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this PremiumWafPoolResponse.

        实例组创建时间

        :param create_time: The create_time of this PremiumWafPoolResponse.
        :type create_time: int
        """
        self._create_time = create_time

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
        if not isinstance(other, PremiumWafPoolResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
