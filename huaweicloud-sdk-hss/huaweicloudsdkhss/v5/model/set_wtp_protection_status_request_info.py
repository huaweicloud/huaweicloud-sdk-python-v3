# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SetWtpProtectionStatusRequestInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status': 'bool',
        'host_id_list': 'list[str]',
        'resource_id': 'str',
        'charging_mode': 'str'
    }

    attribute_map = {
        'status': 'status',
        'host_id_list': 'host_id_list',
        'resource_id': 'resource_id',
        'charging_mode': 'charging_mode'
    }

    def __init__(self, status=None, host_id_list=None, resource_id=None, charging_mode=None):
        r"""SetWtpProtectionStatusRequestInfo

        The model defined in huaweicloud sdk

        :param status: 开启关闭状态，true表示enable， false表示disable
        :type status: bool
        :param host_id_list: 主机ID数组，不能为空
        :type host_id_list: list[str]
        :param resource_id: 资源ID
        :type resource_id: str
        :param charging_mode: 计费模式   - packet_cycle: 包周期
        :type charging_mode: str
        """
        
        

        self._status = None
        self._host_id_list = None
        self._resource_id = None
        self._charging_mode = None
        self.discriminator = None

        self.status = status
        self.host_id_list = host_id_list
        if resource_id is not None:
            self.resource_id = resource_id
        if charging_mode is not None:
            self.charging_mode = charging_mode

    @property
    def status(self):
        r"""Gets the status of this SetWtpProtectionStatusRequestInfo.

        开启关闭状态，true表示enable， false表示disable

        :return: The status of this SetWtpProtectionStatusRequestInfo.
        :rtype: bool
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this SetWtpProtectionStatusRequestInfo.

        开启关闭状态，true表示enable， false表示disable

        :param status: The status of this SetWtpProtectionStatusRequestInfo.
        :type status: bool
        """
        self._status = status

    @property
    def host_id_list(self):
        r"""Gets the host_id_list of this SetWtpProtectionStatusRequestInfo.

        主机ID数组，不能为空

        :return: The host_id_list of this SetWtpProtectionStatusRequestInfo.
        :rtype: list[str]
        """
        return self._host_id_list

    @host_id_list.setter
    def host_id_list(self, host_id_list):
        r"""Sets the host_id_list of this SetWtpProtectionStatusRequestInfo.

        主机ID数组，不能为空

        :param host_id_list: The host_id_list of this SetWtpProtectionStatusRequestInfo.
        :type host_id_list: list[str]
        """
        self._host_id_list = host_id_list

    @property
    def resource_id(self):
        r"""Gets the resource_id of this SetWtpProtectionStatusRequestInfo.

        资源ID

        :return: The resource_id of this SetWtpProtectionStatusRequestInfo.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this SetWtpProtectionStatusRequestInfo.

        资源ID

        :param resource_id: The resource_id of this SetWtpProtectionStatusRequestInfo.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def charging_mode(self):
        r"""Gets the charging_mode of this SetWtpProtectionStatusRequestInfo.

        计费模式   - packet_cycle: 包周期

        :return: The charging_mode of this SetWtpProtectionStatusRequestInfo.
        :rtype: str
        """
        return self._charging_mode

    @charging_mode.setter
    def charging_mode(self, charging_mode):
        r"""Sets the charging_mode of this SetWtpProtectionStatusRequestInfo.

        计费模式   - packet_cycle: 包周期

        :param charging_mode: The charging_mode of this SetWtpProtectionStatusRequestInfo.
        :type charging_mode: str
        """
        self._charging_mode = charging_mode

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
        if not isinstance(other, SetWtpProtectionStatusRequestInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
