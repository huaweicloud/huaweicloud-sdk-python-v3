# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SwitchRaspRequestInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'host_id_list': 'list[str]',
        'app_status': 'bool',
        'app_type': 'str',
        'policy_id': 'str',
        'auto_attach': 'bool',
        'rasp_port_list': 'list[int]'
    }

    attribute_map = {
        'host_id_list': 'host_id_list',
        'app_status': 'app_status',
        'app_type': 'app_type',
        'policy_id': 'policy_id',
        'auto_attach': 'auto_attach',
        'rasp_port_list': 'rasp_port_list'
    }

    def __init__(self, host_id_list=None, app_status=None, app_type=None, policy_id=None, auto_attach=None, rasp_port_list=None):
        r"""SwitchRaspRequestInfo

        The model defined in huaweicloud sdk

        :param host_id_list: HostId list
        :type host_id_list: list[str]
        :param app_status: 应用防护开关状态
        :type app_status: bool
        :param app_type: 应用防护类型
        :type app_type: str
        :param policy_id: 防护策略ID
        :type policy_id: str
        :param auto_attach: 动态防护开关状态
        :type auto_attach: bool
        :param rasp_port_list: RASP端口列表，列表元素与host_id_list对应，app_status为true时支持生效
        :type rasp_port_list: list[int]
        """
        
        

        self._host_id_list = None
        self._app_status = None
        self._app_type = None
        self._policy_id = None
        self._auto_attach = None
        self._rasp_port_list = None
        self.discriminator = None

        self.host_id_list = host_id_list
        self.app_status = app_status
        if app_type is not None:
            self.app_type = app_type
        if policy_id is not None:
            self.policy_id = policy_id
        if auto_attach is not None:
            self.auto_attach = auto_attach
        if rasp_port_list is not None:
            self.rasp_port_list = rasp_port_list

    @property
    def host_id_list(self):
        r"""Gets the host_id_list of this SwitchRaspRequestInfo.

        HostId list

        :return: The host_id_list of this SwitchRaspRequestInfo.
        :rtype: list[str]
        """
        return self._host_id_list

    @host_id_list.setter
    def host_id_list(self, host_id_list):
        r"""Sets the host_id_list of this SwitchRaspRequestInfo.

        HostId list

        :param host_id_list: The host_id_list of this SwitchRaspRequestInfo.
        :type host_id_list: list[str]
        """
        self._host_id_list = host_id_list

    @property
    def app_status(self):
        r"""Gets the app_status of this SwitchRaspRequestInfo.

        应用防护开关状态

        :return: The app_status of this SwitchRaspRequestInfo.
        :rtype: bool
        """
        return self._app_status

    @app_status.setter
    def app_status(self, app_status):
        r"""Sets the app_status of this SwitchRaspRequestInfo.

        应用防护开关状态

        :param app_status: The app_status of this SwitchRaspRequestInfo.
        :type app_status: bool
        """
        self._app_status = app_status

    @property
    def app_type(self):
        r"""Gets the app_type of this SwitchRaspRequestInfo.

        应用防护类型

        :return: The app_type of this SwitchRaspRequestInfo.
        :rtype: str
        """
        return self._app_type

    @app_type.setter
    def app_type(self, app_type):
        r"""Sets the app_type of this SwitchRaspRequestInfo.

        应用防护类型

        :param app_type: The app_type of this SwitchRaspRequestInfo.
        :type app_type: str
        """
        self._app_type = app_type

    @property
    def policy_id(self):
        r"""Gets the policy_id of this SwitchRaspRequestInfo.

        防护策略ID

        :return: The policy_id of this SwitchRaspRequestInfo.
        :rtype: str
        """
        return self._policy_id

    @policy_id.setter
    def policy_id(self, policy_id):
        r"""Sets the policy_id of this SwitchRaspRequestInfo.

        防护策略ID

        :param policy_id: The policy_id of this SwitchRaspRequestInfo.
        :type policy_id: str
        """
        self._policy_id = policy_id

    @property
    def auto_attach(self):
        r"""Gets the auto_attach of this SwitchRaspRequestInfo.

        动态防护开关状态

        :return: The auto_attach of this SwitchRaspRequestInfo.
        :rtype: bool
        """
        return self._auto_attach

    @auto_attach.setter
    def auto_attach(self, auto_attach):
        r"""Sets the auto_attach of this SwitchRaspRequestInfo.

        动态防护开关状态

        :param auto_attach: The auto_attach of this SwitchRaspRequestInfo.
        :type auto_attach: bool
        """
        self._auto_attach = auto_attach

    @property
    def rasp_port_list(self):
        r"""Gets the rasp_port_list of this SwitchRaspRequestInfo.

        RASP端口列表，列表元素与host_id_list对应，app_status为true时支持生效

        :return: The rasp_port_list of this SwitchRaspRequestInfo.
        :rtype: list[int]
        """
        return self._rasp_port_list

    @rasp_port_list.setter
    def rasp_port_list(self, rasp_port_list):
        r"""Sets the rasp_port_list of this SwitchRaspRequestInfo.

        RASP端口列表，列表元素与host_id_list对应，app_status为true时支持生效

        :param rasp_port_list: The rasp_port_list of this SwitchRaspRequestInfo.
        :type rasp_port_list: list[int]
        """
        self._rasp_port_list = rasp_port_list

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
        if not isinstance(other, SwitchRaspRequestInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
