# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AssociationInfo:

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
        'cluster_id': 'str',
        'cluster_name': 'str',
        'app_id': 'str',
        'app_name': 'str',
        'vpc_name': 'str',
        'subnet_name': 'str',
        'cluster_server_type': 'str',
        'vpcep_address': 'str',
        'update_time': 'int',
        'create_time': 'int'
    }

    attribute_map = {
        'id': 'id',
        'cluster_id': 'cluster_id',
        'cluster_name': 'cluster_name',
        'app_id': 'app_id',
        'app_name': 'app_name',
        'vpc_name': 'vpc_name',
        'subnet_name': 'subnet_name',
        'cluster_server_type': 'cluster_server_type',
        'vpcep_address': 'vpcep_address',
        'update_time': 'update_time',
        'create_time': 'create_time'
    }

    def __init__(self, id=None, cluster_id=None, cluster_name=None, app_id=None, app_name=None, vpc_name=None, subnet_name=None, cluster_server_type=None, vpcep_address=None, update_time=None, create_time=None):
        r"""AssociationInfo

        The model defined in huaweicloud sdk

        :param id: 绑定关系ID
        :type id: str
        :param cluster_id: 集群ID
        :type cluster_id: str
        :param cluster_name: 集群名称
        :type cluster_name: str
        :param app_id: 应用ID
        :type app_id: str
        :param app_name: 应用名称
        :type app_name: str
        :param vpc_name: 应用所属的VPC名称
        :type vpc_name: str
        :param subnet_name: 应用所属的VPC的子网
        :type subnet_name: str
        :param cluster_server_type: 集群所属的服务
        :type cluster_server_type: str
        :param vpcep_address: 访问地址
        :type vpcep_address: str
        :param update_time: 绑定关系的最新更改时间，UNIX时间戳，单位毫秒
        :type update_time: int
        :param create_time: 绑定关系的创建时间，UNIX时间戳，单位毫秒
        :type create_time: int
        """
        
        

        self._id = None
        self._cluster_id = None
        self._cluster_name = None
        self._app_id = None
        self._app_name = None
        self._vpc_name = None
        self._subnet_name = None
        self._cluster_server_type = None
        self._vpcep_address = None
        self._update_time = None
        self._create_time = None
        self.discriminator = None

        self.id = id
        self.cluster_id = cluster_id
        self.cluster_name = cluster_name
        self.app_id = app_id
        self.app_name = app_name
        self.vpc_name = vpc_name
        self.subnet_name = subnet_name
        self.cluster_server_type = cluster_server_type
        self.vpcep_address = vpcep_address
        self.update_time = update_time
        self.create_time = create_time

    @property
    def id(self):
        r"""Gets the id of this AssociationInfo.

        绑定关系ID

        :return: The id of this AssociationInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this AssociationInfo.

        绑定关系ID

        :param id: The id of this AssociationInfo.
        :type id: str
        """
        self._id = id

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this AssociationInfo.

        集群ID

        :return: The cluster_id of this AssociationInfo.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this AssociationInfo.

        集群ID

        :param cluster_id: The cluster_id of this AssociationInfo.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def cluster_name(self):
        r"""Gets the cluster_name of this AssociationInfo.

        集群名称

        :return: The cluster_name of this AssociationInfo.
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        r"""Sets the cluster_name of this AssociationInfo.

        集群名称

        :param cluster_name: The cluster_name of this AssociationInfo.
        :type cluster_name: str
        """
        self._cluster_name = cluster_name

    @property
    def app_id(self):
        r"""Gets the app_id of this AssociationInfo.

        应用ID

        :return: The app_id of this AssociationInfo.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        r"""Sets the app_id of this AssociationInfo.

        应用ID

        :param app_id: The app_id of this AssociationInfo.
        :type app_id: str
        """
        self._app_id = app_id

    @property
    def app_name(self):
        r"""Gets the app_name of this AssociationInfo.

        应用名称

        :return: The app_name of this AssociationInfo.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        r"""Sets the app_name of this AssociationInfo.

        应用名称

        :param app_name: The app_name of this AssociationInfo.
        :type app_name: str
        """
        self._app_name = app_name

    @property
    def vpc_name(self):
        r"""Gets the vpc_name of this AssociationInfo.

        应用所属的VPC名称

        :return: The vpc_name of this AssociationInfo.
        :rtype: str
        """
        return self._vpc_name

    @vpc_name.setter
    def vpc_name(self, vpc_name):
        r"""Sets the vpc_name of this AssociationInfo.

        应用所属的VPC名称

        :param vpc_name: The vpc_name of this AssociationInfo.
        :type vpc_name: str
        """
        self._vpc_name = vpc_name

    @property
    def subnet_name(self):
        r"""Gets the subnet_name of this AssociationInfo.

        应用所属的VPC的子网

        :return: The subnet_name of this AssociationInfo.
        :rtype: str
        """
        return self._subnet_name

    @subnet_name.setter
    def subnet_name(self, subnet_name):
        r"""Sets the subnet_name of this AssociationInfo.

        应用所属的VPC的子网

        :param subnet_name: The subnet_name of this AssociationInfo.
        :type subnet_name: str
        """
        self._subnet_name = subnet_name

    @property
    def cluster_server_type(self):
        r"""Gets the cluster_server_type of this AssociationInfo.

        集群所属的服务

        :return: The cluster_server_type of this AssociationInfo.
        :rtype: str
        """
        return self._cluster_server_type

    @cluster_server_type.setter
    def cluster_server_type(self, cluster_server_type):
        r"""Sets the cluster_server_type of this AssociationInfo.

        集群所属的服务

        :param cluster_server_type: The cluster_server_type of this AssociationInfo.
        :type cluster_server_type: str
        """
        self._cluster_server_type = cluster_server_type

    @property
    def vpcep_address(self):
        r"""Gets the vpcep_address of this AssociationInfo.

        访问地址

        :return: The vpcep_address of this AssociationInfo.
        :rtype: str
        """
        return self._vpcep_address

    @vpcep_address.setter
    def vpcep_address(self, vpcep_address):
        r"""Sets the vpcep_address of this AssociationInfo.

        访问地址

        :param vpcep_address: The vpcep_address of this AssociationInfo.
        :type vpcep_address: str
        """
        self._vpcep_address = vpcep_address

    @property
    def update_time(self):
        r"""Gets the update_time of this AssociationInfo.

        绑定关系的最新更改时间，UNIX时间戳，单位毫秒

        :return: The update_time of this AssociationInfo.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this AssociationInfo.

        绑定关系的最新更改时间，UNIX时间戳，单位毫秒

        :param update_time: The update_time of this AssociationInfo.
        :type update_time: int
        """
        self._update_time = update_time

    @property
    def create_time(self):
        r"""Gets the create_time of this AssociationInfo.

        绑定关系的创建时间，UNIX时间戳，单位毫秒

        :return: The create_time of this AssociationInfo.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this AssociationInfo.

        绑定关系的创建时间，UNIX时间戳，单位毫秒

        :param create_time: The create_time of this AssociationInfo.
        :type create_time: int
        """
        self._create_time = create_time

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
        if not isinstance(other, AssociationInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
