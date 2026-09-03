# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WiseEye:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enable': 'str',
        'level': 'str',
        'region_key': 'str',
        'scope_id': 'str',
        'scope_name': 'str'
    }

    attribute_map = {
        'enable': 'enable',
        'level': 'level',
        'region_key': 'region_key',
        'scope_id': 'scope_id',
        'scope_name': 'scope_name'
    }

    def __init__(self, enable=None, level=None, region_key=None, scope_id=None, scope_name=None):
        r"""WiseEye

        The model defined in huaweicloud sdk

        :param enable: 是否开启云眼告警配置
        :type enable: str
        :param level: 云眼告警级别
        :type level: str
        :param region_key: 云眼告警区域，目前取值有：china（中国区），asiaAfricaLatin（亚非拉），europe（欧洲）
        :type region_key: str
        :param scope_id: 云眼告警id，对应云眼信息中的name
        :type scope_id: str
        :param scope_name: 云眼告警范围，对应云眼信息中的label
        :type scope_name: str
        """
        
        

        self._enable = None
        self._level = None
        self._region_key = None
        self._scope_id = None
        self._scope_name = None
        self.discriminator = None

        if enable is not None:
            self.enable = enable
        if level is not None:
            self.level = level
        if region_key is not None:
            self.region_key = region_key
        if scope_id is not None:
            self.scope_id = scope_id
        if scope_name is not None:
            self.scope_name = scope_name

    @property
    def enable(self):
        r"""Gets the enable of this WiseEye.

        是否开启云眼告警配置

        :return: The enable of this WiseEye.
        :rtype: str
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        r"""Sets the enable of this WiseEye.

        是否开启云眼告警配置

        :param enable: The enable of this WiseEye.
        :type enable: str
        """
        self._enable = enable

    @property
    def level(self):
        r"""Gets the level of this WiseEye.

        云眼告警级别

        :return: The level of this WiseEye.
        :rtype: str
        """
        return self._level

    @level.setter
    def level(self, level):
        r"""Sets the level of this WiseEye.

        云眼告警级别

        :param level: The level of this WiseEye.
        :type level: str
        """
        self._level = level

    @property
    def region_key(self):
        r"""Gets the region_key of this WiseEye.

        云眼告警区域，目前取值有：china（中国区），asiaAfricaLatin（亚非拉），europe（欧洲）

        :return: The region_key of this WiseEye.
        :rtype: str
        """
        return self._region_key

    @region_key.setter
    def region_key(self, region_key):
        r"""Sets the region_key of this WiseEye.

        云眼告警区域，目前取值有：china（中国区），asiaAfricaLatin（亚非拉），europe（欧洲）

        :param region_key: The region_key of this WiseEye.
        :type region_key: str
        """
        self._region_key = region_key

    @property
    def scope_id(self):
        r"""Gets the scope_id of this WiseEye.

        云眼告警id，对应云眼信息中的name

        :return: The scope_id of this WiseEye.
        :rtype: str
        """
        return self._scope_id

    @scope_id.setter
    def scope_id(self, scope_id):
        r"""Sets the scope_id of this WiseEye.

        云眼告警id，对应云眼信息中的name

        :param scope_id: The scope_id of this WiseEye.
        :type scope_id: str
        """
        self._scope_id = scope_id

    @property
    def scope_name(self):
        r"""Gets the scope_name of this WiseEye.

        云眼告警范围，对应云眼信息中的label

        :return: The scope_name of this WiseEye.
        :rtype: str
        """
        return self._scope_name

    @scope_name.setter
    def scope_name(self, scope_name):
        r"""Sets the scope_name of this WiseEye.

        云眼告警范围，对应云眼信息中的label

        :param scope_name: The scope_name of this WiseEye.
        :type scope_name: str
        """
        self._scope_name = scope_name

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, WiseEye):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
