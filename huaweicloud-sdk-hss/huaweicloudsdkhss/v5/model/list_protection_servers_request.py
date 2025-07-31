# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListProtectionServersRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enterprise_project_id': 'str',
        'offset': 'int',
        'limit': 'int',
        'host_name': 'str',
        'os_type': 'str',
        'host_ip': 'str',
        'app_type': 'str',
        'app_status': 'str'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'offset': 'offset',
        'limit': 'limit',
        'host_name': 'host_name',
        'os_type': 'os_type',
        'host_ip': 'host_ip',
        'app_type': 'app_type',
        'app_status': 'app_status'
    }

    def __init__(self, enterprise_project_id=None, offset=None, limit=None, host_name=None, os_type=None, host_ip=None, app_type=None, app_status=None):
        r"""ListProtectionServersRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 
        :type enterprise_project_id: str
        :param offset: 查询起始点
        :type offset: int
        :param limit: 每页显示个数
        :type limit: int
        :param host_name: 云主机名称
        :type host_name: str
        :param os_type: 操作系统类型，包含如下2种。  - linux ：linux类型应用防护。  - windows ：windows类型应用防护。
        :type os_type: str
        :param host_ip: 云主机私有IP
        :type host_ip: str
        :param app_type: 应用类型，包含如下1种。   - java ：java类型应用防护。
        :type app_type: str
        :param app_status: 应用防护状态，包含如下2种。   - closed ：未开启。   - opened ：防护中。
        :type app_status: str
        """
        
        

        self._enterprise_project_id = None
        self._offset = None
        self._limit = None
        self._host_name = None
        self._os_type = None
        self._host_ip = None
        self._app_type = None
        self._app_status = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        self.offset = offset
        self.limit = limit
        if host_name is not None:
            self.host_name = host_name
        if os_type is not None:
            self.os_type = os_type
        if host_ip is not None:
            self.host_ip = host_ip
        if app_type is not None:
            self.app_type = app_type
        self.app_status = app_status

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListProtectionServersRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :return: The enterprise_project_id of this ListProtectionServersRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListProtectionServersRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :param enterprise_project_id: The enterprise_project_id of this ListProtectionServersRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def offset(self):
        r"""Gets the offset of this ListProtectionServersRequest.

        查询起始点

        :return: The offset of this ListProtectionServersRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListProtectionServersRequest.

        查询起始点

        :param offset: The offset of this ListProtectionServersRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListProtectionServersRequest.

        每页显示个数

        :return: The limit of this ListProtectionServersRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListProtectionServersRequest.

        每页显示个数

        :param limit: The limit of this ListProtectionServersRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def host_name(self):
        r"""Gets the host_name of this ListProtectionServersRequest.

        云主机名称

        :return: The host_name of this ListProtectionServersRequest.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        r"""Sets the host_name of this ListProtectionServersRequest.

        云主机名称

        :param host_name: The host_name of this ListProtectionServersRequest.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def os_type(self):
        r"""Gets the os_type of this ListProtectionServersRequest.

        操作系统类型，包含如下2种。  - linux ：linux类型应用防护。  - windows ：windows类型应用防护。

        :return: The os_type of this ListProtectionServersRequest.
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        r"""Sets the os_type of this ListProtectionServersRequest.

        操作系统类型，包含如下2种。  - linux ：linux类型应用防护。  - windows ：windows类型应用防护。

        :param os_type: The os_type of this ListProtectionServersRequest.
        :type os_type: str
        """
        self._os_type = os_type

    @property
    def host_ip(self):
        r"""Gets the host_ip of this ListProtectionServersRequest.

        云主机私有IP

        :return: The host_ip of this ListProtectionServersRequest.
        :rtype: str
        """
        return self._host_ip

    @host_ip.setter
    def host_ip(self, host_ip):
        r"""Sets the host_ip of this ListProtectionServersRequest.

        云主机私有IP

        :param host_ip: The host_ip of this ListProtectionServersRequest.
        :type host_ip: str
        """
        self._host_ip = host_ip

    @property
    def app_type(self):
        r"""Gets the app_type of this ListProtectionServersRequest.

        应用类型，包含如下1种。   - java ：java类型应用防护。

        :return: The app_type of this ListProtectionServersRequest.
        :rtype: str
        """
        return self._app_type

    @app_type.setter
    def app_type(self, app_type):
        r"""Sets the app_type of this ListProtectionServersRequest.

        应用类型，包含如下1种。   - java ：java类型应用防护。

        :param app_type: The app_type of this ListProtectionServersRequest.
        :type app_type: str
        """
        self._app_type = app_type

    @property
    def app_status(self):
        r"""Gets the app_status of this ListProtectionServersRequest.

        应用防护状态，包含如下2种。   - closed ：未开启。   - opened ：防护中。

        :return: The app_status of this ListProtectionServersRequest.
        :rtype: str
        """
        return self._app_status

    @app_status.setter
    def app_status(self, app_status):
        r"""Sets the app_status of this ListProtectionServersRequest.

        应用防护状态，包含如下2种。   - closed ：未开启。   - opened ：防护中。

        :param app_status: The app_status of this ListProtectionServersRequest.
        :type app_status: str
        """
        self._app_status = app_status

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
        if not isinstance(other, ListProtectionServersRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
