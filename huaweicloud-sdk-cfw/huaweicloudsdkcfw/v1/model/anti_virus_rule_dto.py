# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AntiVirusRuleDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'object_id': 'str',
        'scan_protocol_configs': 'list[ScanProtocolConfig]'
    }

    attribute_map = {
        'object_id': 'object_id',
        'scan_protocol_configs': 'scan_protocol_configs'
    }

    def __init__(self, object_id=None, scan_protocol_configs=None):
        r"""AntiVirusRuleDto

        The model defined in huaweicloud sdk

        :param object_id: 防护对象ID
        :type object_id: str
        :param scan_protocol_configs: 扫描协议配置
        :type scan_protocol_configs: list[:class:`huaweicloudsdkcfw.v1.ScanProtocolConfig`]
        """
        
        

        self._object_id = None
        self._scan_protocol_configs = None
        self.discriminator = None

        if object_id is not None:
            self.object_id = object_id
        if scan_protocol_configs is not None:
            self.scan_protocol_configs = scan_protocol_configs

    @property
    def object_id(self):
        r"""Gets the object_id of this AntiVirusRuleDto.

        防护对象ID

        :return: The object_id of this AntiVirusRuleDto.
        :rtype: str
        """
        return self._object_id

    @object_id.setter
    def object_id(self, object_id):
        r"""Sets the object_id of this AntiVirusRuleDto.

        防护对象ID

        :param object_id: The object_id of this AntiVirusRuleDto.
        :type object_id: str
        """
        self._object_id = object_id

    @property
    def scan_protocol_configs(self):
        r"""Gets the scan_protocol_configs of this AntiVirusRuleDto.

        扫描协议配置

        :return: The scan_protocol_configs of this AntiVirusRuleDto.
        :rtype: list[:class:`huaweicloudsdkcfw.v1.ScanProtocolConfig`]
        """
        return self._scan_protocol_configs

    @scan_protocol_configs.setter
    def scan_protocol_configs(self, scan_protocol_configs):
        r"""Sets the scan_protocol_configs of this AntiVirusRuleDto.

        扫描协议配置

        :param scan_protocol_configs: The scan_protocol_configs of this AntiVirusRuleDto.
        :type scan_protocol_configs: list[:class:`huaweicloudsdkcfw.v1.ScanProtocolConfig`]
        """
        self._scan_protocol_configs = scan_protocol_configs

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
        if not isinstance(other, AntiVirusRuleDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
