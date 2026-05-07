# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DomainStreamBackupInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'publish_domain': 'str',
        'stream_backup_enable': 'bool'
    }

    attribute_map = {
        'publish_domain': 'publish_domain',
        'stream_backup_enable': 'stream_backup_enable'
    }

    def __init__(self, publish_domain=None, stream_backup_enable=None):
        r"""DomainStreamBackupInfo

        The model defined in huaweicloud sdk

        :param publish_domain: **参数解释**： 直播推流域名 **约束限制**： 不涉及 **取值范围**： 字符长度为[1-255]位 **默认取值**： 不涉及 
        :type publish_domain: str
        :param stream_backup_enable: **参数解释**： 主备流开关 **约束限制**： 不涉及 **取值范围**： - true： 开启主备流功能 - false：关闭主备流功能 **默认取值**： false 
        :type stream_backup_enable: bool
        """
        
        

        self._publish_domain = None
        self._stream_backup_enable = None
        self.discriminator = None

        self.publish_domain = publish_domain
        self.stream_backup_enable = stream_backup_enable

    @property
    def publish_domain(self):
        r"""Gets the publish_domain of this DomainStreamBackupInfo.

        **参数解释**： 直播推流域名 **约束限制**： 不涉及 **取值范围**： 字符长度为[1-255]位 **默认取值**： 不涉及 

        :return: The publish_domain of this DomainStreamBackupInfo.
        :rtype: str
        """
        return self._publish_domain

    @publish_domain.setter
    def publish_domain(self, publish_domain):
        r"""Sets the publish_domain of this DomainStreamBackupInfo.

        **参数解释**： 直播推流域名 **约束限制**： 不涉及 **取值范围**： 字符长度为[1-255]位 **默认取值**： 不涉及 

        :param publish_domain: The publish_domain of this DomainStreamBackupInfo.
        :type publish_domain: str
        """
        self._publish_domain = publish_domain

    @property
    def stream_backup_enable(self):
        r"""Gets the stream_backup_enable of this DomainStreamBackupInfo.

        **参数解释**： 主备流开关 **约束限制**： 不涉及 **取值范围**： - true： 开启主备流功能 - false：关闭主备流功能 **默认取值**： false 

        :return: The stream_backup_enable of this DomainStreamBackupInfo.
        :rtype: bool
        """
        return self._stream_backup_enable

    @stream_backup_enable.setter
    def stream_backup_enable(self, stream_backup_enable):
        r"""Sets the stream_backup_enable of this DomainStreamBackupInfo.

        **参数解释**： 主备流开关 **约束限制**： 不涉及 **取值范围**： - true： 开启主备流功能 - false：关闭主备流功能 **默认取值**： false 

        :param stream_backup_enable: The stream_backup_enable of this DomainStreamBackupInfo.
        :type stream_backup_enable: bool
        """
        self._stream_backup_enable = stream_backup_enable

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
        if not isinstance(other, DomainStreamBackupInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
