# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AntiVirusRuleVO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'scan_protocol_configs': 'list[ScanProtocolConfig]',
        'total': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'scan_protocol_configs': 'scan_protocol_configs',
        'total': 'total'
    }

    def __init__(self, id=None, name=None, scan_protocol_configs=None, total=None):
        r"""AntiVirusRuleVO

        The model defined in huaweicloud sdk

        :param id: 
        :type id: str
        :param name: 
        :type name: str
        :param scan_protocol_configs: 
        :type scan_protocol_configs: list[:class:`huaweicloudsdkcfw.v1.ScanProtocolConfig`]
        :param total: 
        :type total: int
        """
        
        

        self._id = None
        self._name = None
        self._scan_protocol_configs = None
        self._total = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if scan_protocol_configs is not None:
            self.scan_protocol_configs = scan_protocol_configs
        if total is not None:
            self.total = total

    @property
    def id(self):
        r"""Gets the id of this AntiVirusRuleVO.

        :return: The id of this AntiVirusRuleVO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this AntiVirusRuleVO.

        :param id: The id of this AntiVirusRuleVO.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this AntiVirusRuleVO.

        :return: The name of this AntiVirusRuleVO.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this AntiVirusRuleVO.

        :param name: The name of this AntiVirusRuleVO.
        :type name: str
        """
        self._name = name

    @property
    def scan_protocol_configs(self):
        r"""Gets the scan_protocol_configs of this AntiVirusRuleVO.

        :return: The scan_protocol_configs of this AntiVirusRuleVO.
        :rtype: list[:class:`huaweicloudsdkcfw.v1.ScanProtocolConfig`]
        """
        return self._scan_protocol_configs

    @scan_protocol_configs.setter
    def scan_protocol_configs(self, scan_protocol_configs):
        r"""Sets the scan_protocol_configs of this AntiVirusRuleVO.

        :param scan_protocol_configs: The scan_protocol_configs of this AntiVirusRuleVO.
        :type scan_protocol_configs: list[:class:`huaweicloudsdkcfw.v1.ScanProtocolConfig`]
        """
        self._scan_protocol_configs = scan_protocol_configs

    @property
    def total(self):
        r"""Gets the total of this AntiVirusRuleVO.

        :return: The total of this AntiVirusRuleVO.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this AntiVirusRuleVO.

        :param total: The total of this AntiVirusRuleVO.
        :type total: int
        """
        self._total = total

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
        if not isinstance(other, AntiVirusRuleVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
