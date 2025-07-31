# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PolicyListDataList:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'policy_name': 'str',
        'policy_id': 'str',
        'host_num': 'int',
        'is_default': 'bool',
        'port_list': 'list[int]',
        'os_type': 'str',
        'status': 'str'
    }

    attribute_map = {
        'policy_name': 'policy_name',
        'policy_id': 'policy_id',
        'host_num': 'host_num',
        'is_default': 'is_default',
        'port_list': 'port_list',
        'os_type': 'os_type',
        'status': 'status'
    }

    def __init__(self, policy_name=None, policy_id=None, host_num=None, is_default=None, port_list=None, os_type=None, status=None):
        r"""PolicyListDataList

        The model defined in huaweicloud sdk

        :param policy_name: 策略名称
        :type policy_name: str
        :param policy_id: 策略ID
        :type policy_id: str
        :param host_num: **参数解释**: 总数 **取值范围**: 最小值0，最大值2147483647 
        :type host_num: int
        :param is_default: 是否默认
        :type is_default: bool
        :param port_list: 端口列表
        :type port_list: list[int]
        :param os_type: 操作系统类型，包含如下2种。   - Linux ：Linux。   - Windows ：Winodws.
        :type os_type: str
        :param status: 防护状态，包含如下3种 - applying ：生效中 - success ：已生效 - disable ：未生效
        :type status: str
        """
        
        

        self._policy_name = None
        self._policy_id = None
        self._host_num = None
        self._is_default = None
        self._port_list = None
        self._os_type = None
        self._status = None
        self.discriminator = None

        if policy_name is not None:
            self.policy_name = policy_name
        if policy_id is not None:
            self.policy_id = policy_id
        if host_num is not None:
            self.host_num = host_num
        if is_default is not None:
            self.is_default = is_default
        if port_list is not None:
            self.port_list = port_list
        if os_type is not None:
            self.os_type = os_type
        if status is not None:
            self.status = status

    @property
    def policy_name(self):
        r"""Gets the policy_name of this PolicyListDataList.

        策略名称

        :return: The policy_name of this PolicyListDataList.
        :rtype: str
        """
        return self._policy_name

    @policy_name.setter
    def policy_name(self, policy_name):
        r"""Sets the policy_name of this PolicyListDataList.

        策略名称

        :param policy_name: The policy_name of this PolicyListDataList.
        :type policy_name: str
        """
        self._policy_name = policy_name

    @property
    def policy_id(self):
        r"""Gets the policy_id of this PolicyListDataList.

        策略ID

        :return: The policy_id of this PolicyListDataList.
        :rtype: str
        """
        return self._policy_id

    @policy_id.setter
    def policy_id(self, policy_id):
        r"""Sets the policy_id of this PolicyListDataList.

        策略ID

        :param policy_id: The policy_id of this PolicyListDataList.
        :type policy_id: str
        """
        self._policy_id = policy_id

    @property
    def host_num(self):
        r"""Gets the host_num of this PolicyListDataList.

        **参数解释**: 总数 **取值范围**: 最小值0，最大值2147483647 

        :return: The host_num of this PolicyListDataList.
        :rtype: int
        """
        return self._host_num

    @host_num.setter
    def host_num(self, host_num):
        r"""Sets the host_num of this PolicyListDataList.

        **参数解释**: 总数 **取值范围**: 最小值0，最大值2147483647 

        :param host_num: The host_num of this PolicyListDataList.
        :type host_num: int
        """
        self._host_num = host_num

    @property
    def is_default(self):
        r"""Gets the is_default of this PolicyListDataList.

        是否默认

        :return: The is_default of this PolicyListDataList.
        :rtype: bool
        """
        return self._is_default

    @is_default.setter
    def is_default(self, is_default):
        r"""Sets the is_default of this PolicyListDataList.

        是否默认

        :param is_default: The is_default of this PolicyListDataList.
        :type is_default: bool
        """
        self._is_default = is_default

    @property
    def port_list(self):
        r"""Gets the port_list of this PolicyListDataList.

        端口列表

        :return: The port_list of this PolicyListDataList.
        :rtype: list[int]
        """
        return self._port_list

    @port_list.setter
    def port_list(self, port_list):
        r"""Sets the port_list of this PolicyListDataList.

        端口列表

        :param port_list: The port_list of this PolicyListDataList.
        :type port_list: list[int]
        """
        self._port_list = port_list

    @property
    def os_type(self):
        r"""Gets the os_type of this PolicyListDataList.

        操作系统类型，包含如下2种。   - Linux ：Linux。   - Windows ：Winodws.

        :return: The os_type of this PolicyListDataList.
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        r"""Sets the os_type of this PolicyListDataList.

        操作系统类型，包含如下2种。   - Linux ：Linux。   - Windows ：Winodws.

        :param os_type: The os_type of this PolicyListDataList.
        :type os_type: str
        """
        self._os_type = os_type

    @property
    def status(self):
        r"""Gets the status of this PolicyListDataList.

        防护状态，包含如下3种 - applying ：生效中 - success ：已生效 - disable ：未生效

        :return: The status of this PolicyListDataList.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this PolicyListDataList.

        防护状态，包含如下3种 - applying ：生效中 - success ：已生效 - disable ：未生效

        :param status: The status of this PolicyListDataList.
        :type status: str
        """
        self._status = status

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
        if not isinstance(other, PolicyListDataList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
