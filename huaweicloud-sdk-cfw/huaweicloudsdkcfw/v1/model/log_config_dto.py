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
        r"""LogConfigDto

        The model defined in huaweicloud sdk

        :param fw_instance_id: 防火墙id，可通过[防火墙ID获取方式](cfw_02_0028.xml)获取
        :type fw_instance_id: str
        :param lts_enable: 是否开启LTS，1表示是，0表示不是
        :type lts_enable: int
        :param lts_log_group_id: LTS日志分组id,可通过查询LTS（云日志服务）下查询账号下所有日志组接口获得，通过返回值中的log_groups.log_group_id（.表示各对象之间层级的区分）获得
        :type lts_log_group_id: str
        :param lts_attack_log_stream_id: 攻击日志流id,可通过查询LTS（云日志服务）下查询指定日志组下的所有日志流接口获得，通过返回值中的log_streams.log_stream_id（.表示各对象之间层级的区分）获得
        :type lts_attack_log_stream_id: str
        :param lts_attack_log_stream_enable: 是否开启攻击日志流，1表示是，0表示不是
        :type lts_attack_log_stream_enable: int
        :param lts_access_log_stream_id: 访问控制日志流id,可通过查询LTS（云日志服务）下查询指定日志组下的所有日志流接口获得，通过返回值中的log_streams.log_stream_id（.表示各对象之间层级的区分）获得
        :type lts_access_log_stream_id: str
        :param lts_access_log_stream_enable: 是否开启访问控制流，1表示是，0表示不是
        :type lts_access_log_stream_enable: int
        :param lts_flow_log_stream_id: 流量日志id,可通过查询LTS（云日志服务）下查询指定日志组下的所有日志流接口获得，通过返回值中的log_streams.log_stream_id（.表示各对象之间层级的区分）获得
        :type lts_flow_log_stream_id: str
        :param lts_flow_log_stream_enable: 是否开启流量日志，1表示是，0表示不是
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
        if lts_attack_log_stream_enable is not None:
            self.lts_attack_log_stream_enable = lts_attack_log_stream_enable
        if lts_access_log_stream_id is not None:
            self.lts_access_log_stream_id = lts_access_log_stream_id
        if lts_access_log_stream_enable is not None:
            self.lts_access_log_stream_enable = lts_access_log_stream_enable
        if lts_flow_log_stream_id is not None:
            self.lts_flow_log_stream_id = lts_flow_log_stream_id
        if lts_flow_log_stream_enable is not None:
            self.lts_flow_log_stream_enable = lts_flow_log_stream_enable

    @property
    def fw_instance_id(self):
        r"""Gets the fw_instance_id of this LogConfigDto.

        防火墙id，可通过[防火墙ID获取方式](cfw_02_0028.xml)获取

        :return: The fw_instance_id of this LogConfigDto.
        :rtype: str
        """
        return self._fw_instance_id

    @fw_instance_id.setter
    def fw_instance_id(self, fw_instance_id):
        r"""Sets the fw_instance_id of this LogConfigDto.

        防火墙id，可通过[防火墙ID获取方式](cfw_02_0028.xml)获取

        :param fw_instance_id: The fw_instance_id of this LogConfigDto.
        :type fw_instance_id: str
        """
        self._fw_instance_id = fw_instance_id

    @property
    def lts_enable(self):
        r"""Gets the lts_enable of this LogConfigDto.

        是否开启LTS，1表示是，0表示不是

        :return: The lts_enable of this LogConfigDto.
        :rtype: int
        """
        return self._lts_enable

    @lts_enable.setter
    def lts_enable(self, lts_enable):
        r"""Sets the lts_enable of this LogConfigDto.

        是否开启LTS，1表示是，0表示不是

        :param lts_enable: The lts_enable of this LogConfigDto.
        :type lts_enable: int
        """
        self._lts_enable = lts_enable

    @property
    def lts_log_group_id(self):
        r"""Gets the lts_log_group_id of this LogConfigDto.

        LTS日志分组id,可通过查询LTS（云日志服务）下查询账号下所有日志组接口获得，通过返回值中的log_groups.log_group_id（.表示各对象之间层级的区分）获得

        :return: The lts_log_group_id of this LogConfigDto.
        :rtype: str
        """
        return self._lts_log_group_id

    @lts_log_group_id.setter
    def lts_log_group_id(self, lts_log_group_id):
        r"""Sets the lts_log_group_id of this LogConfigDto.

        LTS日志分组id,可通过查询LTS（云日志服务）下查询账号下所有日志组接口获得，通过返回值中的log_groups.log_group_id（.表示各对象之间层级的区分）获得

        :param lts_log_group_id: The lts_log_group_id of this LogConfigDto.
        :type lts_log_group_id: str
        """
        self._lts_log_group_id = lts_log_group_id

    @property
    def lts_attack_log_stream_id(self):
        r"""Gets the lts_attack_log_stream_id of this LogConfigDto.

        攻击日志流id,可通过查询LTS（云日志服务）下查询指定日志组下的所有日志流接口获得，通过返回值中的log_streams.log_stream_id（.表示各对象之间层级的区分）获得

        :return: The lts_attack_log_stream_id of this LogConfigDto.
        :rtype: str
        """
        return self._lts_attack_log_stream_id

    @lts_attack_log_stream_id.setter
    def lts_attack_log_stream_id(self, lts_attack_log_stream_id):
        r"""Sets the lts_attack_log_stream_id of this LogConfigDto.

        攻击日志流id,可通过查询LTS（云日志服务）下查询指定日志组下的所有日志流接口获得，通过返回值中的log_streams.log_stream_id（.表示各对象之间层级的区分）获得

        :param lts_attack_log_stream_id: The lts_attack_log_stream_id of this LogConfigDto.
        :type lts_attack_log_stream_id: str
        """
        self._lts_attack_log_stream_id = lts_attack_log_stream_id

    @property
    def lts_attack_log_stream_enable(self):
        r"""Gets the lts_attack_log_stream_enable of this LogConfigDto.

        是否开启攻击日志流，1表示是，0表示不是

        :return: The lts_attack_log_stream_enable of this LogConfigDto.
        :rtype: int
        """
        return self._lts_attack_log_stream_enable

    @lts_attack_log_stream_enable.setter
    def lts_attack_log_stream_enable(self, lts_attack_log_stream_enable):
        r"""Sets the lts_attack_log_stream_enable of this LogConfigDto.

        是否开启攻击日志流，1表示是，0表示不是

        :param lts_attack_log_stream_enable: The lts_attack_log_stream_enable of this LogConfigDto.
        :type lts_attack_log_stream_enable: int
        """
        self._lts_attack_log_stream_enable = lts_attack_log_stream_enable

    @property
    def lts_access_log_stream_id(self):
        r"""Gets the lts_access_log_stream_id of this LogConfigDto.

        访问控制日志流id,可通过查询LTS（云日志服务）下查询指定日志组下的所有日志流接口获得，通过返回值中的log_streams.log_stream_id（.表示各对象之间层级的区分）获得

        :return: The lts_access_log_stream_id of this LogConfigDto.
        :rtype: str
        """
        return self._lts_access_log_stream_id

    @lts_access_log_stream_id.setter
    def lts_access_log_stream_id(self, lts_access_log_stream_id):
        r"""Sets the lts_access_log_stream_id of this LogConfigDto.

        访问控制日志流id,可通过查询LTS（云日志服务）下查询指定日志组下的所有日志流接口获得，通过返回值中的log_streams.log_stream_id（.表示各对象之间层级的区分）获得

        :param lts_access_log_stream_id: The lts_access_log_stream_id of this LogConfigDto.
        :type lts_access_log_stream_id: str
        """
        self._lts_access_log_stream_id = lts_access_log_stream_id

    @property
    def lts_access_log_stream_enable(self):
        r"""Gets the lts_access_log_stream_enable of this LogConfigDto.

        是否开启访问控制流，1表示是，0表示不是

        :return: The lts_access_log_stream_enable of this LogConfigDto.
        :rtype: int
        """
        return self._lts_access_log_stream_enable

    @lts_access_log_stream_enable.setter
    def lts_access_log_stream_enable(self, lts_access_log_stream_enable):
        r"""Sets the lts_access_log_stream_enable of this LogConfigDto.

        是否开启访问控制流，1表示是，0表示不是

        :param lts_access_log_stream_enable: The lts_access_log_stream_enable of this LogConfigDto.
        :type lts_access_log_stream_enable: int
        """
        self._lts_access_log_stream_enable = lts_access_log_stream_enable

    @property
    def lts_flow_log_stream_id(self):
        r"""Gets the lts_flow_log_stream_id of this LogConfigDto.

        流量日志id,可通过查询LTS（云日志服务）下查询指定日志组下的所有日志流接口获得，通过返回值中的log_streams.log_stream_id（.表示各对象之间层级的区分）获得

        :return: The lts_flow_log_stream_id of this LogConfigDto.
        :rtype: str
        """
        return self._lts_flow_log_stream_id

    @lts_flow_log_stream_id.setter
    def lts_flow_log_stream_id(self, lts_flow_log_stream_id):
        r"""Sets the lts_flow_log_stream_id of this LogConfigDto.

        流量日志id,可通过查询LTS（云日志服务）下查询指定日志组下的所有日志流接口获得，通过返回值中的log_streams.log_stream_id（.表示各对象之间层级的区分）获得

        :param lts_flow_log_stream_id: The lts_flow_log_stream_id of this LogConfigDto.
        :type lts_flow_log_stream_id: str
        """
        self._lts_flow_log_stream_id = lts_flow_log_stream_id

    @property
    def lts_flow_log_stream_enable(self):
        r"""Gets the lts_flow_log_stream_enable of this LogConfigDto.

        是否开启流量日志，1表示是，0表示不是

        :return: The lts_flow_log_stream_enable of this LogConfigDto.
        :rtype: int
        """
        return self._lts_flow_log_stream_enable

    @lts_flow_log_stream_enable.setter
    def lts_flow_log_stream_enable(self, lts_flow_log_stream_enable):
        r"""Sets the lts_flow_log_stream_enable of this LogConfigDto.

        是否开启流量日志，1表示是，0表示不是

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
