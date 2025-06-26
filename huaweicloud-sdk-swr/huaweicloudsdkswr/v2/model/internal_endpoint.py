# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InternalEndpoint:

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
        'vpcep_endpoint_id': 'str',
        'project_id': 'str',
        'project_name': 'str',
        'vpc_id': 'str',
        'vpc_name': 'str',
        'vpc_cidr': 'str',
        'subnet_id': 'str',
        'subnet_name': 'str',
        'subnet_cidr': 'str',
        'endpoint_ip': 'str',
        'description': 'str',
        'status': 'str',
        'status_text': 'str',
        'created_at': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'vpcep_endpoint_id': 'vpcep_endpoint_id',
        'project_id': 'project_id',
        'project_name': 'project_name',
        'vpc_id': 'vpc_id',
        'vpc_name': 'vpc_name',
        'vpc_cidr': 'vpc_cidr',
        'subnet_id': 'subnet_id',
        'subnet_name': 'subnet_name',
        'subnet_cidr': 'subnet_cidr',
        'endpoint_ip': 'endpoint_ip',
        'description': 'description',
        'status': 'status',
        'status_text': 'status_text',
        'created_at': 'created_at'
    }

    def __init__(self, id=None, vpcep_endpoint_id=None, project_id=None, project_name=None, vpc_id=None, vpc_name=None, vpc_cidr=None, subnet_id=None, subnet_name=None, subnet_cidr=None, endpoint_ip=None, description=None, status=None, status_text=None, created_at=None):
        r"""InternalEndpoint

        The model defined in huaweicloud sdk

        :param id: 内网访问ID
        :type id: str
        :param vpcep_endpoint_id: VPC端点的ID
        :type vpcep_endpoint_id: str
        :param project_id: 项目ID
        :type project_id: str
        :param project_name: 项目名称
        :type project_name: str
        :param vpc_id: VPC的ID
        :type vpc_id: str
        :param vpc_name: VPC的名称
        :type vpc_name: str
        :param vpc_cidr: VPC的CIDR范围
        :type vpc_cidr: str
        :param subnet_id: 子网的ID
        :type subnet_id: str
        :param subnet_name: 子网的名称
        :type subnet_name: str
        :param subnet_cidr: 子网的CIDR范围
        :type subnet_cidr: str
        :param endpoint_ip: 端点的IP地址
        :type endpoint_ip: str
        :param description: 访问控制的描述信息
        :type description: str
        :param status: 访问控制的状态
        :type status: str
        :param status_text: 访问控制的状态信息
        :type status_text: str
        :param created_at: 访问控制的创建时间
        :type created_at: datetime
        """
        
        

        self._id = None
        self._vpcep_endpoint_id = None
        self._project_id = None
        self._project_name = None
        self._vpc_id = None
        self._vpc_name = None
        self._vpc_cidr = None
        self._subnet_id = None
        self._subnet_name = None
        self._subnet_cidr = None
        self._endpoint_ip = None
        self._description = None
        self._status = None
        self._status_text = None
        self._created_at = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if vpcep_endpoint_id is not None:
            self.vpcep_endpoint_id = vpcep_endpoint_id
        if project_id is not None:
            self.project_id = project_id
        if project_name is not None:
            self.project_name = project_name
        if vpc_id is not None:
            self.vpc_id = vpc_id
        if vpc_name is not None:
            self.vpc_name = vpc_name
        if vpc_cidr is not None:
            self.vpc_cidr = vpc_cidr
        if subnet_id is not None:
            self.subnet_id = subnet_id
        if subnet_name is not None:
            self.subnet_name = subnet_name
        if subnet_cidr is not None:
            self.subnet_cidr = subnet_cidr
        if endpoint_ip is not None:
            self.endpoint_ip = endpoint_ip
        if description is not None:
            self.description = description
        if status is not None:
            self.status = status
        if status_text is not None:
            self.status_text = status_text
        if created_at is not None:
            self.created_at = created_at

    @property
    def id(self):
        r"""Gets the id of this InternalEndpoint.

        内网访问ID

        :return: The id of this InternalEndpoint.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this InternalEndpoint.

        内网访问ID

        :param id: The id of this InternalEndpoint.
        :type id: str
        """
        self._id = id

    @property
    def vpcep_endpoint_id(self):
        r"""Gets the vpcep_endpoint_id of this InternalEndpoint.

        VPC端点的ID

        :return: The vpcep_endpoint_id of this InternalEndpoint.
        :rtype: str
        """
        return self._vpcep_endpoint_id

    @vpcep_endpoint_id.setter
    def vpcep_endpoint_id(self, vpcep_endpoint_id):
        r"""Sets the vpcep_endpoint_id of this InternalEndpoint.

        VPC端点的ID

        :param vpcep_endpoint_id: The vpcep_endpoint_id of this InternalEndpoint.
        :type vpcep_endpoint_id: str
        """
        self._vpcep_endpoint_id = vpcep_endpoint_id

    @property
    def project_id(self):
        r"""Gets the project_id of this InternalEndpoint.

        项目ID

        :return: The project_id of this InternalEndpoint.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this InternalEndpoint.

        项目ID

        :param project_id: The project_id of this InternalEndpoint.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def project_name(self):
        r"""Gets the project_name of this InternalEndpoint.

        项目名称

        :return: The project_name of this InternalEndpoint.
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        r"""Sets the project_name of this InternalEndpoint.

        项目名称

        :param project_name: The project_name of this InternalEndpoint.
        :type project_name: str
        """
        self._project_name = project_name

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this InternalEndpoint.

        VPC的ID

        :return: The vpc_id of this InternalEndpoint.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this InternalEndpoint.

        VPC的ID

        :param vpc_id: The vpc_id of this InternalEndpoint.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def vpc_name(self):
        r"""Gets the vpc_name of this InternalEndpoint.

        VPC的名称

        :return: The vpc_name of this InternalEndpoint.
        :rtype: str
        """
        return self._vpc_name

    @vpc_name.setter
    def vpc_name(self, vpc_name):
        r"""Sets the vpc_name of this InternalEndpoint.

        VPC的名称

        :param vpc_name: The vpc_name of this InternalEndpoint.
        :type vpc_name: str
        """
        self._vpc_name = vpc_name

    @property
    def vpc_cidr(self):
        r"""Gets the vpc_cidr of this InternalEndpoint.

        VPC的CIDR范围

        :return: The vpc_cidr of this InternalEndpoint.
        :rtype: str
        """
        return self._vpc_cidr

    @vpc_cidr.setter
    def vpc_cidr(self, vpc_cidr):
        r"""Sets the vpc_cidr of this InternalEndpoint.

        VPC的CIDR范围

        :param vpc_cidr: The vpc_cidr of this InternalEndpoint.
        :type vpc_cidr: str
        """
        self._vpc_cidr = vpc_cidr

    @property
    def subnet_id(self):
        r"""Gets the subnet_id of this InternalEndpoint.

        子网的ID

        :return: The subnet_id of this InternalEndpoint.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        r"""Sets the subnet_id of this InternalEndpoint.

        子网的ID

        :param subnet_id: The subnet_id of this InternalEndpoint.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def subnet_name(self):
        r"""Gets the subnet_name of this InternalEndpoint.

        子网的名称

        :return: The subnet_name of this InternalEndpoint.
        :rtype: str
        """
        return self._subnet_name

    @subnet_name.setter
    def subnet_name(self, subnet_name):
        r"""Sets the subnet_name of this InternalEndpoint.

        子网的名称

        :param subnet_name: The subnet_name of this InternalEndpoint.
        :type subnet_name: str
        """
        self._subnet_name = subnet_name

    @property
    def subnet_cidr(self):
        r"""Gets the subnet_cidr of this InternalEndpoint.

        子网的CIDR范围

        :return: The subnet_cidr of this InternalEndpoint.
        :rtype: str
        """
        return self._subnet_cidr

    @subnet_cidr.setter
    def subnet_cidr(self, subnet_cidr):
        r"""Sets the subnet_cidr of this InternalEndpoint.

        子网的CIDR范围

        :param subnet_cidr: The subnet_cidr of this InternalEndpoint.
        :type subnet_cidr: str
        """
        self._subnet_cidr = subnet_cidr

    @property
    def endpoint_ip(self):
        r"""Gets the endpoint_ip of this InternalEndpoint.

        端点的IP地址

        :return: The endpoint_ip of this InternalEndpoint.
        :rtype: str
        """
        return self._endpoint_ip

    @endpoint_ip.setter
    def endpoint_ip(self, endpoint_ip):
        r"""Sets the endpoint_ip of this InternalEndpoint.

        端点的IP地址

        :param endpoint_ip: The endpoint_ip of this InternalEndpoint.
        :type endpoint_ip: str
        """
        self._endpoint_ip = endpoint_ip

    @property
    def description(self):
        r"""Gets the description of this InternalEndpoint.

        访问控制的描述信息

        :return: The description of this InternalEndpoint.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this InternalEndpoint.

        访问控制的描述信息

        :param description: The description of this InternalEndpoint.
        :type description: str
        """
        self._description = description

    @property
    def status(self):
        r"""Gets the status of this InternalEndpoint.

        访问控制的状态

        :return: The status of this InternalEndpoint.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this InternalEndpoint.

        访问控制的状态

        :param status: The status of this InternalEndpoint.
        :type status: str
        """
        self._status = status

    @property
    def status_text(self):
        r"""Gets the status_text of this InternalEndpoint.

        访问控制的状态信息

        :return: The status_text of this InternalEndpoint.
        :rtype: str
        """
        return self._status_text

    @status_text.setter
    def status_text(self, status_text):
        r"""Sets the status_text of this InternalEndpoint.

        访问控制的状态信息

        :param status_text: The status_text of this InternalEndpoint.
        :type status_text: str
        """
        self._status_text = status_text

    @property
    def created_at(self):
        r"""Gets the created_at of this InternalEndpoint.

        访问控制的创建时间

        :return: The created_at of this InternalEndpoint.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this InternalEndpoint.

        访问控制的创建时间

        :param created_at: The created_at of this InternalEndpoint.
        :type created_at: datetime
        """
        self._created_at = created_at

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
        if not isinstance(other, InternalEndpoint):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
