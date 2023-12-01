# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LogConfigDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'fw_instance_id': 'str',
        'lts_enable': 'int',
        'lts_log_group_id': 'str',
        'lts_attack_log_stream_id': 'str',
        'lts_attack_log_stream_enable': 'int',
        'lts_access_log_stream_id': 'str',
        'lts_access_log_stream_enable': 'int',
        'lts_flow_log_stream_id': 'str',
        'lts_flow_log_stream_enable': 'int'
    }

    attribute_map = {
        'fw_instance_id': 'fw_instance_id',
        'lts_enable': 'lts_enable',
        'lts_log_group_id': 'lts_log_group_id',
        'lts_attack_log_stream_id': 'lts_attack_log_stream_id',
        'lts_attack_log_stream_enable': 'lts_attack_log_stream_enable',
        'lts_access_log_stream_id': 'lts_access_log_stream_id',
        'lts_access_log_stream_enable': 'lts_access_log_stream_enable',
        'lts_flow_log_stream_id': 'lts_flow_log_stream_id',
        'lts_flow_log_stream_enable': 'lts_flow_log_stream_enable'
    }

    def __init__(self, fw_instance_id=None, lts_enable=None, lts_log_group_id=None, lts_attack_log_stream_id=None, lts_attack_log_stream_enable=None, lts_access_log_stream_id=None, lts_access_log_stream_enable=None, lts_flow_log_stream_id=None, lts_flow_log_stream_enable=None):
        """LogConfigDto

        The model defined in huaweicloud sdk

        :param fw_instance_id: 防火墙id
        :type fw_instance_id: str
        :param lts_enable: 是否开启LTS
        :type lts_enable: int
        :param lts_log_group_id: LTS日志分组id
        :type lts_log_group_id: str
        :param lts_attack_log_stream_id: 攻击日志流id
        :type lts_attack_log_stream_id: str
        :param lts_attack_log_stream_enable: 是否开启攻击日志流
        :type lts_attack_log_stream_enable: int
        :param lts_access_log_stream_id: 访问控制日志流id
        :type lts_access_log_stream_id: str
        :param lts_access_log_stream_enable: 是否开启访问控制流
        :type lts_access_log_stream_enable: int
        :param lts_flow_log_stream_id: 流量日志id
        :type lts_flow_log_stream_id: str
        :param lts_flow_log_stream_enable: 是否开启流量日志
        :type lts_flow_log_stream_enable: int
        """
        
        

        self._fw_instance_id = None
        self._lts_enable = None
        self._lts_log_group_id = None
        self._lts_attack_log_stream_id = None
        self._lts_attack_log_stream_enable = None
        self._lts_access_log_stream_id = None
        self._lts_access_log_stream_enable = None
        self._lts_flow_log_stream_id = None
        self._lts_flow_log_stream_enable = None
        self.discriminator = None

        self.fw_instance_id = fw_instance_id
        self.lts_enable = lts_enable
        self.lts_log_group_id = lts_log_group_id
        if lts_attack_log_stream_id is not None:
            self.lts_attack_log_stream_id = lts_attack_log_stream_id
        self.lts_attack_log_stream_enable = lts_attack_log_stream_enable
        if lts_access_log_stream_id is not None:
            self.lts_access_log_stream_id = lts_access_log_stream_id
        self.lts_access_log_stream_enable = lts_access_log_stream_enable
        if lts_flow_log_stream_id is not None:
            self.lts_flow_log_stream_id = lts_flow_log_stream_id
        self.lts_flow_log_stream_enable = lts_flow_log_stream_enable

    @property
    def fw_instance_id(self):
        """Gets the fw_instance_id of this LogConfigDto.

        防火墙id

        :return: The fw_instance_id of this LogConfigDto.
        :rtype: str
        """
        return self._fw_instance_id

    @fw_instance_id.setter
    def fw_instance_id(self, fw_instance_id):
        """Sets the fw_instance_id of this LogConfigDto.

        防火墙id

        :param fw_instance_id: The fw_instance_id of this LogConfigDto.
        :type fw_instance_id: str
        """
        self._fw_instance_id = fw_instance_id

    @property
    def lts_enable(self):
        """Gets the lts_enable of this LogConfigDto.

        是否开启LTS

        :return: The lts_enable of this LogConfigDto.
        :rtype: int
        """
        return self._lts_enable

    @lts_enable.setter
    def lts_enable(self, lts_enable):
        """Sets the lts_enable of this LogConfigDto.

        是否开启LTS

        :param lts_enable: The lts_enable of this LogConfigDto.
        :type lts_enable: int
        """
        self._lts_enable = lts_enable

    @property
    def lts_log_group_id(self):
        """Gets the lts_log_group_id of this LogConfigDto.

        LTS日志分组id

        :return: The lts_log_group_id of this LogConfigDto.
        :rtype: str
        """
        return self._lts_log_group_id

    @lts_log_group_id.setter
    def lts_log_group_id(self, lts_log_group_id):
        """Sets the lts_log_group_id of this LogConfigDto.

        LTS日志分组id

        :param lts_log_group_id: The lts_log_group_id of this LogConfigDto.
        :type lts_log_group_id: str
        """
        self._lts_log_group_id = lts_log_group_id

    @property
    def lts_attack_log_stream_id(self):
        """Gets the lts_attack_log_stream_id of this LogConfigDto.

        攻击日志流id

        :return: The lts_attack_log_stream_id of this LogConfigDto.
        :rtype: str
        """
        return self._lts_attack_log_stream_id

    @lts_attack_log_stream_id.setter
    def lts_attack_log_stream_id(self, lts_attack_log_stream_id):
        """Sets the lts_attack_log_stream_id of this LogConfigDto.

        攻击日志流id

        :param lts_attack_log_stream_id: The lts_attack_log_stream_id of this LogConfigDto.
        :type lts_attack_log_stream_id: str
        """
        self._lts_attack_log_stream_id = lts_attack_log_stream_id

    @property
    def lts_attack_log_stream_enable(self):
        """Gets the lts_attack_log_stream_enable of this LogConfigDto.

        是否开启攻击日志流

        :return: The lts_attack_log_stream_enable of this LogConfigDto.
        :rtype: int
        """
        return self._lts_attack_log_stream_enable

    @lts_attack_log_stream_enable.setter
    def lts_attack_log_stream_enable(self, lts_attack_log_stream_enable):
        """Sets the lts_attack_log_stream_enable of this LogConfigDto.

        是否开启攻击日志流

        :param lts_attack_log_stream_enable: The lts_attack_log_stream_enable of this LogConfigDto.
        :type lts_attack_log_stream_enable: int
        """
        self._lts_attack_log_stream_enable = lts_attack_log_stream_enable

    @property
    def lts_access_log_stream_id(self):
        """Gets the lts_access_log_stream_id of this LogConfigDto.

        访问控制日志流id

        :return: The lts_access_log_stream_id of this LogConfigDto.
        :rtype: str
        """
        return self._lts_access_log_stream_id

    @lts_access_log_stream_id.setter
    def lts_access_log_stream_id(self, lts_access_log_stream_id):
        """Sets the lts_access_log_stream_id of this LogConfigDto.

        访问控制日志流id

        :param lts_access_log_stream_id: The lts_access_log_stream_id of this LogConfigDto.
        :type lts_access_log_stream_id: str
        """
        self._lts_access_log_stream_id = lts_access_log_stream_id

    @property
    def lts_access_log_stream_enable(self):
        """Gets the lts_access_log_stream_enable of this LogConfigDto.

        是否开启访问控制流

        :return: The lts_access_log_stream_enable of this LogConfigDto.
        :rtype: int
        """
        return self._lts_access_log_stream_enable

    @lts_access_log_stream_enable.setter
    def lts_access_log_stream_enable(self, lts_access_log_stream_enable):
        """Sets the lts_access_log_stream_enable of this LogConfigDto.

        是否开启访问控制流

        :param lts_access_log_stream_enable: The lts_access_log_stream_enable of this LogConfigDto.
        :type lts_access_log_stream_enable: int
        """
        self._lts_access_log_stream_enable = lts_access_log_stream_enable

    @property
    def lts_flow_log_stream_id(self):
        """Gets the lts_flow_log_stream_id of this LogConfigDto.

        流量日志id

        :return: The lts_flow_log_stream_id of this LogConfigDto.
        :rtype: str
        """
        return self._lts_flow_log_stream_id

    @lts_flow_log_stream_id.setter
    def lts_flow_log_stream_id(self, lts_flow_log_stream_id):
        """Sets the lts_flow_log_stream_id of this LogConfigDto.

        流量日志id

        :param lts_flow_log_stream_id: The lts_flow_log_stream_id of this LogConfigDto.
        :type lts_flow_log_stream_id: str
        """
        self._lts_flow_log_stream_id = lts_flow_log_stream_id

    @property
    def lts_flow_log_stream_enable(self):
        """Gets the lts_flow_log_stream_enable of this LogConfigDto.

        是否开启流量日志

        :return: The lts_flow_log_stream_enable of this LogConfigDto.
        :rtype: int
        """
        return self._lts_flow_log_stream_enable

    @lts_flow_log_stream_enable.setter
    def lts_flow_log_stream_enable(self, lts_flow_log_stream_enable):
        """Sets the lts_flow_log_stream_enable of this LogConfigDto.

        是否开启流量日志

        :param lts_flow_log_stream_enable: The lts_flow_log_stream_enable of this LogConfigDto.
        :type lts_flow_log_stream_enable: int
        """
        self._lts_flow_log_stream_enable = lts_flow_log_stream_enable

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
        if not isinstance(other, LogConfigDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
