# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResourceInstanceProp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'host_name': 'str',
        'fixed_ip': 'str',
        'floating_ip': 'str',
        'region_id': 'str',
        'zone_id': 'str',
        'application': 'str',
        'group': 'str',
        'project_id': 'str'
    }

    attribute_map = {
        'host_name': 'host_name',
        'fixed_ip': 'fixed_ip',
        'floating_ip': 'floating_ip',
        'region_id': 'region_id',
        'zone_id': 'zone_id',
        'application': 'application',
        'group': 'group',
        'project_id': 'project_id'
    }

    def __init__(self, host_name=None, fixed_ip=None, floating_ip=None, region_id=None, zone_id=None, application=None, group=None, project_id=None):
        r"""ResourceInstanceProp

        The model defined in huaweicloud sdk

        :param host_name: 主机名 未校验：长度
        :type host_name: str
        :param fixed_ip: 内网ip 未校验： 格式，长度
        :type fixed_ip: str
        :param floating_ip: 弹性公网ip 未校验： 格式，长度
        :type floating_ip: str
        :param region_id: 区域 未校验： 长度
        :type region_id: str
        :param zone_id: 可用区
        :type zone_id: str
        :param application: CMDB应用，CMDB应用视图才有值。类似管理面的云服务
        :type application: str
        :param group: CMDB分组，CMDB应用视图才有值。类似管理面的schema
        :type group: str
        :param project_id: 实例的 project_id  需要消费，建议必填 未校验长度
        :type project_id: str
        """
        
        

        self._host_name = None
        self._fixed_ip = None
        self._floating_ip = None
        self._region_id = None
        self._zone_id = None
        self._application = None
        self._group = None
        self._project_id = None
        self.discriminator = None

        self.host_name = host_name
        self.fixed_ip = fixed_ip
        if floating_ip is not None:
            self.floating_ip = floating_ip
        self.region_id = region_id
        self.zone_id = zone_id
        if application is not None:
            self.application = application
        if group is not None:
            self.group = group
        if project_id is not None:
            self.project_id = project_id

    @property
    def host_name(self):
        r"""Gets the host_name of this ResourceInstanceProp.

        主机名 未校验：长度

        :return: The host_name of this ResourceInstanceProp.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        r"""Sets the host_name of this ResourceInstanceProp.

        主机名 未校验：长度

        :param host_name: The host_name of this ResourceInstanceProp.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def fixed_ip(self):
        r"""Gets the fixed_ip of this ResourceInstanceProp.

        内网ip 未校验： 格式，长度

        :return: The fixed_ip of this ResourceInstanceProp.
        :rtype: str
        """
        return self._fixed_ip

    @fixed_ip.setter
    def fixed_ip(self, fixed_ip):
        r"""Sets the fixed_ip of this ResourceInstanceProp.

        内网ip 未校验： 格式，长度

        :param fixed_ip: The fixed_ip of this ResourceInstanceProp.
        :type fixed_ip: str
        """
        self._fixed_ip = fixed_ip

    @property
    def floating_ip(self):
        r"""Gets the floating_ip of this ResourceInstanceProp.

        弹性公网ip 未校验： 格式，长度

        :return: The floating_ip of this ResourceInstanceProp.
        :rtype: str
        """
        return self._floating_ip

    @floating_ip.setter
    def floating_ip(self, floating_ip):
        r"""Sets the floating_ip of this ResourceInstanceProp.

        弹性公网ip 未校验： 格式，长度

        :param floating_ip: The floating_ip of this ResourceInstanceProp.
        :type floating_ip: str
        """
        self._floating_ip = floating_ip

    @property
    def region_id(self):
        r"""Gets the region_id of this ResourceInstanceProp.

        区域 未校验： 长度

        :return: The region_id of this ResourceInstanceProp.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        r"""Sets the region_id of this ResourceInstanceProp.

        区域 未校验： 长度

        :param region_id: The region_id of this ResourceInstanceProp.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def zone_id(self):
        r"""Gets the zone_id of this ResourceInstanceProp.

        可用区

        :return: The zone_id of this ResourceInstanceProp.
        :rtype: str
        """
        return self._zone_id

    @zone_id.setter
    def zone_id(self, zone_id):
        r"""Sets the zone_id of this ResourceInstanceProp.

        可用区

        :param zone_id: The zone_id of this ResourceInstanceProp.
        :type zone_id: str
        """
        self._zone_id = zone_id

    @property
    def application(self):
        r"""Gets the application of this ResourceInstanceProp.

        CMDB应用，CMDB应用视图才有值。类似管理面的云服务

        :return: The application of this ResourceInstanceProp.
        :rtype: str
        """
        return self._application

    @application.setter
    def application(self, application):
        r"""Sets the application of this ResourceInstanceProp.

        CMDB应用，CMDB应用视图才有值。类似管理面的云服务

        :param application: The application of this ResourceInstanceProp.
        :type application: str
        """
        self._application = application

    @property
    def group(self):
        r"""Gets the group of this ResourceInstanceProp.

        CMDB分组，CMDB应用视图才有值。类似管理面的schema

        :return: The group of this ResourceInstanceProp.
        :rtype: str
        """
        return self._group

    @group.setter
    def group(self, group):
        r"""Sets the group of this ResourceInstanceProp.

        CMDB分组，CMDB应用视图才有值。类似管理面的schema

        :param group: The group of this ResourceInstanceProp.
        :type group: str
        """
        self._group = group

    @property
    def project_id(self):
        r"""Gets the project_id of this ResourceInstanceProp.

        实例的 project_id  需要消费，建议必填 未校验长度

        :return: The project_id of this ResourceInstanceProp.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ResourceInstanceProp.

        实例的 project_id  需要消费，建议必填 未校验长度

        :param project_id: The project_id of this ResourceInstanceProp.
        :type project_id: str
        """
        self._project_id = project_id

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
        if not isinstance(other, ResourceInstanceProp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
