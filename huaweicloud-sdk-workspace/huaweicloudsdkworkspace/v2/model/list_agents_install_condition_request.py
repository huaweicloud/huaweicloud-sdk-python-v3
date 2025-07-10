# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAgentsInstallConditionRequest:

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
        'desktop_id': 'str',
        'desktop_name': 'str',
        'status': 'str',
        'ip_address': 'str',
        'is_installed': 'bool',
        'desktop_pool_id': 'str',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'desktop_id': 'desktop_id',
        'desktop_name': 'desktop_name',
        'status': 'status',
        'ip_address': 'ip_address',
        'is_installed': 'is_installed',
        'desktop_pool_id': 'desktop_pool_id',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, enterprise_project_id=None, desktop_id=None, desktop_name=None, status=None, ip_address=None, is_installed=None, desktop_pool_id=None, limit=None, offset=None):
        r"""ListAgentsInstallConditionRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: 企业项目ID。
        :type enterprise_project_id: str
        :param desktop_id: 桌面ID。
        :type desktop_id: str
        :param desktop_name: 桌面名称。
        :type desktop_name: str
        :param status: 桌面状态。
        :type status: str
        :param ip_address: ip地址。
        :type ip_address: str
        :param is_installed: 插件是否已安装。
        :type is_installed: bool
        :param desktop_pool_id: 桌面池id。
        :type desktop_pool_id: str
        :param limit: 每页显示的数量。
        :type limit: int
        :param offset: 用于分页查询，查询的起始记录序号，从0开始。
        :type offset: int
        """
        
        

        self._enterprise_project_id = None
        self._desktop_id = None
        self._desktop_name = None
        self._status = None
        self._ip_address = None
        self._is_installed = None
        self._desktop_pool_id = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if desktop_id is not None:
            self.desktop_id = desktop_id
        if desktop_name is not None:
            self.desktop_name = desktop_name
        if status is not None:
            self.status = status
        if ip_address is not None:
            self.ip_address = ip_address
        if is_installed is not None:
            self.is_installed = is_installed
        if desktop_pool_id is not None:
            self.desktop_pool_id = desktop_pool_id
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListAgentsInstallConditionRequest.

        企业项目ID。

        :return: The enterprise_project_id of this ListAgentsInstallConditionRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListAgentsInstallConditionRequest.

        企业项目ID。

        :param enterprise_project_id: The enterprise_project_id of this ListAgentsInstallConditionRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def desktop_id(self):
        r"""Gets the desktop_id of this ListAgentsInstallConditionRequest.

        桌面ID。

        :return: The desktop_id of this ListAgentsInstallConditionRequest.
        :rtype: str
        """
        return self._desktop_id

    @desktop_id.setter
    def desktop_id(self, desktop_id):
        r"""Sets the desktop_id of this ListAgentsInstallConditionRequest.

        桌面ID。

        :param desktop_id: The desktop_id of this ListAgentsInstallConditionRequest.
        :type desktop_id: str
        """
        self._desktop_id = desktop_id

    @property
    def desktop_name(self):
        r"""Gets the desktop_name of this ListAgentsInstallConditionRequest.

        桌面名称。

        :return: The desktop_name of this ListAgentsInstallConditionRequest.
        :rtype: str
        """
        return self._desktop_name

    @desktop_name.setter
    def desktop_name(self, desktop_name):
        r"""Sets the desktop_name of this ListAgentsInstallConditionRequest.

        桌面名称。

        :param desktop_name: The desktop_name of this ListAgentsInstallConditionRequest.
        :type desktop_name: str
        """
        self._desktop_name = desktop_name

    @property
    def status(self):
        r"""Gets the status of this ListAgentsInstallConditionRequest.

        桌面状态。

        :return: The status of this ListAgentsInstallConditionRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListAgentsInstallConditionRequest.

        桌面状态。

        :param status: The status of this ListAgentsInstallConditionRequest.
        :type status: str
        """
        self._status = status

    @property
    def ip_address(self):
        r"""Gets the ip_address of this ListAgentsInstallConditionRequest.

        ip地址。

        :return: The ip_address of this ListAgentsInstallConditionRequest.
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        r"""Sets the ip_address of this ListAgentsInstallConditionRequest.

        ip地址。

        :param ip_address: The ip_address of this ListAgentsInstallConditionRequest.
        :type ip_address: str
        """
        self._ip_address = ip_address

    @property
    def is_installed(self):
        r"""Gets the is_installed of this ListAgentsInstallConditionRequest.

        插件是否已安装。

        :return: The is_installed of this ListAgentsInstallConditionRequest.
        :rtype: bool
        """
        return self._is_installed

    @is_installed.setter
    def is_installed(self, is_installed):
        r"""Sets the is_installed of this ListAgentsInstallConditionRequest.

        插件是否已安装。

        :param is_installed: The is_installed of this ListAgentsInstallConditionRequest.
        :type is_installed: bool
        """
        self._is_installed = is_installed

    @property
    def desktop_pool_id(self):
        r"""Gets the desktop_pool_id of this ListAgentsInstallConditionRequest.

        桌面池id。

        :return: The desktop_pool_id of this ListAgentsInstallConditionRequest.
        :rtype: str
        """
        return self._desktop_pool_id

    @desktop_pool_id.setter
    def desktop_pool_id(self, desktop_pool_id):
        r"""Sets the desktop_pool_id of this ListAgentsInstallConditionRequest.

        桌面池id。

        :param desktop_pool_id: The desktop_pool_id of this ListAgentsInstallConditionRequest.
        :type desktop_pool_id: str
        """
        self._desktop_pool_id = desktop_pool_id

    @property
    def limit(self):
        r"""Gets the limit of this ListAgentsInstallConditionRequest.

        每页显示的数量。

        :return: The limit of this ListAgentsInstallConditionRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListAgentsInstallConditionRequest.

        每页显示的数量。

        :param limit: The limit of this ListAgentsInstallConditionRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListAgentsInstallConditionRequest.

        用于分页查询，查询的起始记录序号，从0开始。

        :return: The offset of this ListAgentsInstallConditionRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListAgentsInstallConditionRequest.

        用于分页查询，查询的起始记录序号，从0开始。

        :param offset: The offset of this ListAgentsInstallConditionRequest.
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
        if not isinstance(other, ListAgentsInstallConditionRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
