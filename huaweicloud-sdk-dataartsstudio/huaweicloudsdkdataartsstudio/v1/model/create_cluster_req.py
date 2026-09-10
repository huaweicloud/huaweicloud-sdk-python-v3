# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateClusterReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cluster_name': 'str',
        'description': 'str',
        'flavor_id': 'str',
        'charge_mode': 'int',
        'cidr_in_vpc': 'str',
        'workspaces': 'list[str]'
    }

    attribute_map = {
        'cluster_name': 'cluster_name',
        'description': 'description',
        'flavor_id': 'flavor_id',
        'charge_mode': 'charge_mode',
        'cidr_in_vpc': 'cidr_in_vpc',
        'workspaces': 'workspaces'
    }

    def __init__(self, cluster_name=None, description=None, flavor_id=None, charge_mode=None, cidr_in_vpc=None, workspaces=None):
        r"""CreateClusterReq

        The model defined in huaweicloud sdk

        :param cluster_name: 新建的集群名称，名称只能包含数字、英文字母和下划线，但不能是纯数字，且不能以下划线开头。长度限制：1~128个字符。 说明：集群名称不区分大小写，系统会自动转换为小写。
        :type cluster_name: str
        :param description: 集群的描述信息。
        :type description: str
        :param flavor_id: 集群规格。
        :type flavor_id: str
        :param charge_mode: 集群的收费模式。只能设置为“1”，表示按照CU时收费。
        :type charge_mode: int
        :param cidr_in_vpc: 队列的虚拟私有云（VPC）的网段。建议使用网段：10.0.0.0/8~28，172.16.0.0/12~28，192.168.0.0/16~28。
        :type cidr_in_vpc: str
        :param workspaces: 集群需要绑定的工作空间ID。
        :type workspaces: list[str]
        """
        
        

        self._cluster_name = None
        self._description = None
        self._flavor_id = None
        self._charge_mode = None
        self._cidr_in_vpc = None
        self._workspaces = None
        self.discriminator = None

        self.cluster_name = cluster_name
        if description is not None:
            self.description = description
        self.flavor_id = flavor_id
        self.charge_mode = charge_mode
        if cidr_in_vpc is not None:
            self.cidr_in_vpc = cidr_in_vpc
        if workspaces is not None:
            self.workspaces = workspaces

    @property
    def cluster_name(self):
        r"""Gets the cluster_name of this CreateClusterReq.

        新建的集群名称，名称只能包含数字、英文字母和下划线，但不能是纯数字，且不能以下划线开头。长度限制：1~128个字符。 说明：集群名称不区分大小写，系统会自动转换为小写。

        :return: The cluster_name of this CreateClusterReq.
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        r"""Sets the cluster_name of this CreateClusterReq.

        新建的集群名称，名称只能包含数字、英文字母和下划线，但不能是纯数字，且不能以下划线开头。长度限制：1~128个字符。 说明：集群名称不区分大小写，系统会自动转换为小写。

        :param cluster_name: The cluster_name of this CreateClusterReq.
        :type cluster_name: str
        """
        self._cluster_name = cluster_name

    @property
    def description(self):
        r"""Gets the description of this CreateClusterReq.

        集群的描述信息。

        :return: The description of this CreateClusterReq.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateClusterReq.

        集群的描述信息。

        :param description: The description of this CreateClusterReq.
        :type description: str
        """
        self._description = description

    @property
    def flavor_id(self):
        r"""Gets the flavor_id of this CreateClusterReq.

        集群规格。

        :return: The flavor_id of this CreateClusterReq.
        :rtype: str
        """
        return self._flavor_id

    @flavor_id.setter
    def flavor_id(self, flavor_id):
        r"""Sets the flavor_id of this CreateClusterReq.

        集群规格。

        :param flavor_id: The flavor_id of this CreateClusterReq.
        :type flavor_id: str
        """
        self._flavor_id = flavor_id

    @property
    def charge_mode(self):
        r"""Gets the charge_mode of this CreateClusterReq.

        集群的收费模式。只能设置为“1”，表示按照CU时收费。

        :return: The charge_mode of this CreateClusterReq.
        :rtype: int
        """
        return self._charge_mode

    @charge_mode.setter
    def charge_mode(self, charge_mode):
        r"""Sets the charge_mode of this CreateClusterReq.

        集群的收费模式。只能设置为“1”，表示按照CU时收费。

        :param charge_mode: The charge_mode of this CreateClusterReq.
        :type charge_mode: int
        """
        self._charge_mode = charge_mode

    @property
    def cidr_in_vpc(self):
        r"""Gets the cidr_in_vpc of this CreateClusterReq.

        队列的虚拟私有云（VPC）的网段。建议使用网段：10.0.0.0/8~28，172.16.0.0/12~28，192.168.0.0/16~28。

        :return: The cidr_in_vpc of this CreateClusterReq.
        :rtype: str
        """
        return self._cidr_in_vpc

    @cidr_in_vpc.setter
    def cidr_in_vpc(self, cidr_in_vpc):
        r"""Sets the cidr_in_vpc of this CreateClusterReq.

        队列的虚拟私有云（VPC）的网段。建议使用网段：10.0.0.0/8~28，172.16.0.0/12~28，192.168.0.0/16~28。

        :param cidr_in_vpc: The cidr_in_vpc of this CreateClusterReq.
        :type cidr_in_vpc: str
        """
        self._cidr_in_vpc = cidr_in_vpc

    @property
    def workspaces(self):
        r"""Gets the workspaces of this CreateClusterReq.

        集群需要绑定的工作空间ID。

        :return: The workspaces of this CreateClusterReq.
        :rtype: list[str]
        """
        return self._workspaces

    @workspaces.setter
    def workspaces(self, workspaces):
        r"""Sets the workspaces of this CreateClusterReq.

        集群需要绑定的工作空间ID。

        :param workspaces: The workspaces of this CreateClusterReq.
        :type workspaces: list[str]
        """
        self._workspaces = workspaces

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
        if not isinstance(other, CreateClusterReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
