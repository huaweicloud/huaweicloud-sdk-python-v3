# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListWtpProtectHostRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'region': 'str',
        'enterprise_project_id': 'str',
        'host_name': 'str',
        'host_id': 'str',
        'public_ip': 'str',
        'private_ip': 'str',
        'group_name': 'str',
        'os_type': 'str',
        'protect_status': 'str',
        'wtp_status': 'str',
        'agent_status': 'str',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'region': 'region',
        'enterprise_project_id': 'enterprise_project_id',
        'host_name': 'host_name',
        'host_id': 'host_id',
        'public_ip': 'public_ip',
        'private_ip': 'private_ip',
        'group_name': 'group_name',
        'os_type': 'os_type',
        'protect_status': 'protect_status',
        'wtp_status': 'wtp_status',
        'agent_status': 'agent_status',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, region=None, enterprise_project_id=None, host_name=None, host_id=None, public_ip=None, private_ip=None, group_name=None, os_type=None, protect_status=None, wtp_status=None, agent_status=None, limit=None, offset=None):
        r"""ListWtpProtectHostRequest

        The model defined in huaweicloud sdk

        :param region: Region ID
        :type region: str
        :param enterprise_project_id: 主机所属的企业项目ID。 开通企业项目功能后才需要配置企业项目。 企业项目ID默认取值为“0”，表示默认企业项目。如果需要查询所有企业项目下的主机，请传参“all_granted_eps”。如果您只有某个企业项目的权限，则需要传递该企业项目ID，查询该企业项目下的主机，否则会因权限不足而报错。
        :type enterprise_project_id: str
        :param host_name: 服务器名称
        :type host_name: str
        :param host_id: 主机ID
        :type host_id: str
        :param public_ip: 弹性公网IP
        :type public_ip: str
        :param private_ip: 私有IP
        :type private_ip: str
        :param group_name: 服务器组名称
        :type group_name: str
        :param os_type: 操作系统类别（linux，windows）   - linux : linux操作系统   - windows : windows操作系统
        :type os_type: str
        :param protect_status: 配额状态   - opened : 已绑定网页防篡改配额
        :type protect_status: str
        :param wtp_status: 网页防篡改防护状态   - opened : 防护汇总   - opening : 正在开启   - open_failed : 防护失败   - partial_protection : 部分防护   - protection_interruption : 防护中断
        :type wtp_status: str
        :param agent_status: 客户端状态   - not_installed : agent未安装   - online : agent在线   - offline : agent不在线
        :type agent_status: str
        :param limit: 默认10
        :type limit: int
        :param offset: 偏移量：指定返回记录的开始位置
        :type offset: int
        """
        
        

        self._region = None
        self._enterprise_project_id = None
        self._host_name = None
        self._host_id = None
        self._public_ip = None
        self._private_ip = None
        self._group_name = None
        self._os_type = None
        self._protect_status = None
        self._wtp_status = None
        self._agent_status = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        if region is not None:
            self.region = region
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if host_name is not None:
            self.host_name = host_name
        if host_id is not None:
            self.host_id = host_id
        if public_ip is not None:
            self.public_ip = public_ip
        if private_ip is not None:
            self.private_ip = private_ip
        if group_name is not None:
            self.group_name = group_name
        if os_type is not None:
            self.os_type = os_type
        if protect_status is not None:
            self.protect_status = protect_status
        if wtp_status is not None:
            self.wtp_status = wtp_status
        if agent_status is not None:
            self.agent_status = agent_status
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def region(self):
        r"""Gets the region of this ListWtpProtectHostRequest.

        Region ID

        :return: The region of this ListWtpProtectHostRequest.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this ListWtpProtectHostRequest.

        Region ID

        :param region: The region of this ListWtpProtectHostRequest.
        :type region: str
        """
        self._region = region

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListWtpProtectHostRequest.

        主机所属的企业项目ID。 开通企业项目功能后才需要配置企业项目。 企业项目ID默认取值为“0”，表示默认企业项目。如果需要查询所有企业项目下的主机，请传参“all_granted_eps”。如果您只有某个企业项目的权限，则需要传递该企业项目ID，查询该企业项目下的主机，否则会因权限不足而报错。

        :return: The enterprise_project_id of this ListWtpProtectHostRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListWtpProtectHostRequest.

        主机所属的企业项目ID。 开通企业项目功能后才需要配置企业项目。 企业项目ID默认取值为“0”，表示默认企业项目。如果需要查询所有企业项目下的主机，请传参“all_granted_eps”。如果您只有某个企业项目的权限，则需要传递该企业项目ID，查询该企业项目下的主机，否则会因权限不足而报错。

        :param enterprise_project_id: The enterprise_project_id of this ListWtpProtectHostRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def host_name(self):
        r"""Gets the host_name of this ListWtpProtectHostRequest.

        服务器名称

        :return: The host_name of this ListWtpProtectHostRequest.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        r"""Sets the host_name of this ListWtpProtectHostRequest.

        服务器名称

        :param host_name: The host_name of this ListWtpProtectHostRequest.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def host_id(self):
        r"""Gets the host_id of this ListWtpProtectHostRequest.

        主机ID

        :return: The host_id of this ListWtpProtectHostRequest.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        r"""Sets the host_id of this ListWtpProtectHostRequest.

        主机ID

        :param host_id: The host_id of this ListWtpProtectHostRequest.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def public_ip(self):
        r"""Gets the public_ip of this ListWtpProtectHostRequest.

        弹性公网IP

        :return: The public_ip of this ListWtpProtectHostRequest.
        :rtype: str
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        r"""Sets the public_ip of this ListWtpProtectHostRequest.

        弹性公网IP

        :param public_ip: The public_ip of this ListWtpProtectHostRequest.
        :type public_ip: str
        """
        self._public_ip = public_ip

    @property
    def private_ip(self):
        r"""Gets the private_ip of this ListWtpProtectHostRequest.

        私有IP

        :return: The private_ip of this ListWtpProtectHostRequest.
        :rtype: str
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, private_ip):
        r"""Sets the private_ip of this ListWtpProtectHostRequest.

        私有IP

        :param private_ip: The private_ip of this ListWtpProtectHostRequest.
        :type private_ip: str
        """
        self._private_ip = private_ip

    @property
    def group_name(self):
        r"""Gets the group_name of this ListWtpProtectHostRequest.

        服务器组名称

        :return: The group_name of this ListWtpProtectHostRequest.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        r"""Sets the group_name of this ListWtpProtectHostRequest.

        服务器组名称

        :param group_name: The group_name of this ListWtpProtectHostRequest.
        :type group_name: str
        """
        self._group_name = group_name

    @property
    def os_type(self):
        r"""Gets the os_type of this ListWtpProtectHostRequest.

        操作系统类别（linux，windows）   - linux : linux操作系统   - windows : windows操作系统

        :return: The os_type of this ListWtpProtectHostRequest.
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        r"""Sets the os_type of this ListWtpProtectHostRequest.

        操作系统类别（linux，windows）   - linux : linux操作系统   - windows : windows操作系统

        :param os_type: The os_type of this ListWtpProtectHostRequest.
        :type os_type: str
        """
        self._os_type = os_type

    @property
    def protect_status(self):
        r"""Gets the protect_status of this ListWtpProtectHostRequest.

        配额状态   - opened : 已绑定网页防篡改配额

        :return: The protect_status of this ListWtpProtectHostRequest.
        :rtype: str
        """
        return self._protect_status

    @protect_status.setter
    def protect_status(self, protect_status):
        r"""Sets the protect_status of this ListWtpProtectHostRequest.

        配额状态   - opened : 已绑定网页防篡改配额

        :param protect_status: The protect_status of this ListWtpProtectHostRequest.
        :type protect_status: str
        """
        self._protect_status = protect_status

    @property
    def wtp_status(self):
        r"""Gets the wtp_status of this ListWtpProtectHostRequest.

        网页防篡改防护状态   - opened : 防护汇总   - opening : 正在开启   - open_failed : 防护失败   - partial_protection : 部分防护   - protection_interruption : 防护中断

        :return: The wtp_status of this ListWtpProtectHostRequest.
        :rtype: str
        """
        return self._wtp_status

    @wtp_status.setter
    def wtp_status(self, wtp_status):
        r"""Sets the wtp_status of this ListWtpProtectHostRequest.

        网页防篡改防护状态   - opened : 防护汇总   - opening : 正在开启   - open_failed : 防护失败   - partial_protection : 部分防护   - protection_interruption : 防护中断

        :param wtp_status: The wtp_status of this ListWtpProtectHostRequest.
        :type wtp_status: str
        """
        self._wtp_status = wtp_status

    @property
    def agent_status(self):
        r"""Gets the agent_status of this ListWtpProtectHostRequest.

        客户端状态   - not_installed : agent未安装   - online : agent在线   - offline : agent不在线

        :return: The agent_status of this ListWtpProtectHostRequest.
        :rtype: str
        """
        return self._agent_status

    @agent_status.setter
    def agent_status(self, agent_status):
        r"""Sets the agent_status of this ListWtpProtectHostRequest.

        客户端状态   - not_installed : agent未安装   - online : agent在线   - offline : agent不在线

        :param agent_status: The agent_status of this ListWtpProtectHostRequest.
        :type agent_status: str
        """
        self._agent_status = agent_status

    @property
    def limit(self):
        r"""Gets the limit of this ListWtpProtectHostRequest.

        默认10

        :return: The limit of this ListWtpProtectHostRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListWtpProtectHostRequest.

        默认10

        :param limit: The limit of this ListWtpProtectHostRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListWtpProtectHostRequest.

        偏移量：指定返回记录的开始位置

        :return: The offset of this ListWtpProtectHostRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListWtpProtectHostRequest.

        偏移量：指定返回记录的开始位置

        :param offset: The offset of this ListWtpProtectHostRequest.
        :type offset: int
        """
        self._offset = offset

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
        if not isinstance(other, ListWtpProtectHostRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
