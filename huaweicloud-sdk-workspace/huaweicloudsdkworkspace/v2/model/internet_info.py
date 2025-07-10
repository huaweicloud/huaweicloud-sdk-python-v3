# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InternetInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'vpc_name': 'str',
        'subnet_id': 'str',
        'subnet_name': 'str',
        'nat_id': 'str',
        'nat_name': 'str',
        'eip': 'str',
        'created_at': 'str',
        'status': 'str',
        'enterprise_project_id': 'str'
    }

    attribute_map = {
        'vpc_name': 'vpc_name',
        'subnet_id': 'subnet_id',
        'subnet_name': 'subnet_name',
        'nat_id': 'nat_id',
        'nat_name': 'nat_name',
        'eip': 'eip',
        'created_at': 'created_at',
        'status': 'status',
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, vpc_name=None, subnet_id=None, subnet_name=None, nat_id=None, nat_name=None, eip=None, created_at=None, status=None, enterprise_project_id=None):
        r"""InternetInfo

        The model defined in huaweicloud sdk

        :param vpc_name: VPC名称。
        :type vpc_name: str
        :param subnet_id: 子网id。
        :type subnet_id: str
        :param subnet_name: 子网名称。
        :type subnet_name: str
        :param nat_id: NAT id。
        :type nat_id: str
        :param nat_name: NAT名称。
        :type nat_name: str
        :param eip: 弹性公网IP。
        :type eip: str
        :param created_at: 创建时间。
        :type created_at: str
        :param status: 状态。
        :type status: str
        :param enterprise_project_id: 企业项目ID。
        :type enterprise_project_id: str
        """
        
        

        self._vpc_name = None
        self._subnet_id = None
        self._subnet_name = None
        self._nat_id = None
        self._nat_name = None
        self._eip = None
        self._created_at = None
        self._status = None
        self._enterprise_project_id = None
        self.discriminator = None

        if vpc_name is not None:
            self.vpc_name = vpc_name
        if subnet_id is not None:
            self.subnet_id = subnet_id
        if subnet_name is not None:
            self.subnet_name = subnet_name
        if nat_id is not None:
            self.nat_id = nat_id
        if nat_name is not None:
            self.nat_name = nat_name
        if eip is not None:
            self.eip = eip
        if created_at is not None:
            self.created_at = created_at
        if status is not None:
            self.status = status
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id

    @property
    def vpc_name(self):
        r"""Gets the vpc_name of this InternetInfo.

        VPC名称。

        :return: The vpc_name of this InternetInfo.
        :rtype: str
        """
        return self._vpc_name

    @vpc_name.setter
    def vpc_name(self, vpc_name):
        r"""Sets the vpc_name of this InternetInfo.

        VPC名称。

        :param vpc_name: The vpc_name of this InternetInfo.
        :type vpc_name: str
        """
        self._vpc_name = vpc_name

    @property
    def subnet_id(self):
        r"""Gets the subnet_id of this InternetInfo.

        子网id。

        :return: The subnet_id of this InternetInfo.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        r"""Sets the subnet_id of this InternetInfo.

        子网id。

        :param subnet_id: The subnet_id of this InternetInfo.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def subnet_name(self):
        r"""Gets the subnet_name of this InternetInfo.

        子网名称。

        :return: The subnet_name of this InternetInfo.
        :rtype: str
        """
        return self._subnet_name

    @subnet_name.setter
    def subnet_name(self, subnet_name):
        r"""Sets the subnet_name of this InternetInfo.

        子网名称。

        :param subnet_name: The subnet_name of this InternetInfo.
        :type subnet_name: str
        """
        self._subnet_name = subnet_name

    @property
    def nat_id(self):
        r"""Gets the nat_id of this InternetInfo.

        NAT id。

        :return: The nat_id of this InternetInfo.
        :rtype: str
        """
        return self._nat_id

    @nat_id.setter
    def nat_id(self, nat_id):
        r"""Sets the nat_id of this InternetInfo.

        NAT id。

        :param nat_id: The nat_id of this InternetInfo.
        :type nat_id: str
        """
        self._nat_id = nat_id

    @property
    def nat_name(self):
        r"""Gets the nat_name of this InternetInfo.

        NAT名称。

        :return: The nat_name of this InternetInfo.
        :rtype: str
        """
        return self._nat_name

    @nat_name.setter
    def nat_name(self, nat_name):
        r"""Sets the nat_name of this InternetInfo.

        NAT名称。

        :param nat_name: The nat_name of this InternetInfo.
        :type nat_name: str
        """
        self._nat_name = nat_name

    @property
    def eip(self):
        r"""Gets the eip of this InternetInfo.

        弹性公网IP。

        :return: The eip of this InternetInfo.
        :rtype: str
        """
        return self._eip

    @eip.setter
    def eip(self, eip):
        r"""Sets the eip of this InternetInfo.

        弹性公网IP。

        :param eip: The eip of this InternetInfo.
        :type eip: str
        """
        self._eip = eip

    @property
    def created_at(self):
        r"""Gets the created_at of this InternetInfo.

        创建时间。

        :return: The created_at of this InternetInfo.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this InternetInfo.

        创建时间。

        :param created_at: The created_at of this InternetInfo.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def status(self):
        r"""Gets the status of this InternetInfo.

        状态。

        :return: The status of this InternetInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this InternetInfo.

        状态。

        :param status: The status of this InternetInfo.
        :type status: str
        """
        self._status = status

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this InternetInfo.

        企业项目ID。

        :return: The enterprise_project_id of this InternetInfo.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this InternetInfo.

        企业项目ID。

        :param enterprise_project_id: The enterprise_project_id of this InternetInfo.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

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
        if not isinstance(other, InternetInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
