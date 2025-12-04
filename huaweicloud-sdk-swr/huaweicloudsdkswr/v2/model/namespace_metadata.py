# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NamespaceMetadata:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'public': 'str',
        'auto_scan': 'str',
        'prevent_vul': 'str',
        'severity': 'str'
    }

    attribute_map = {
        'public': 'public',
        'auto_scan': 'auto_scan',
        'prevent_vul': 'prevent_vul',
        'severity': 'severity'
    }

    def __init__(self, public=None, auto_scan=None, prevent_vul=None, severity=None):
        r"""NamespaceMetadata

        The model defined in huaweicloud sdk

        :param public: 是否公开，可选true、false
        :type public: str
        :param auto_scan: 上传制品时，是否自动触发制品扫描，可选true、false
        :type auto_scan: str
        :param prevent_vul: 是否开启制品阻断，可选true、false
        :type prevent_vul: str
        :param severity: 阻断开启的场景下，如果存在漏洞，并且存在的漏洞严重程度高于此处定义的级别，则无法拉取镜像。可选值为\&quot;none\&quot;, \&quot;low\&quot;, \&quot;medium\&quot;, \&quot;high\&quot;, \&quot;critical\&quot;。
        :type severity: str
        """
        
        

        self._public = None
        self._auto_scan = None
        self._prevent_vul = None
        self._severity = None
        self.discriminator = None

        self.public = public
        if auto_scan is not None:
            self.auto_scan = auto_scan
        if prevent_vul is not None:
            self.prevent_vul = prevent_vul
        if severity is not None:
            self.severity = severity

    @property
    def public(self):
        r"""Gets the public of this NamespaceMetadata.

        是否公开，可选true、false

        :return: The public of this NamespaceMetadata.
        :rtype: str
        """
        return self._public

    @public.setter
    def public(self, public):
        r"""Sets the public of this NamespaceMetadata.

        是否公开，可选true、false

        :param public: The public of this NamespaceMetadata.
        :type public: str
        """
        self._public = public

    @property
    def auto_scan(self):
        r"""Gets the auto_scan of this NamespaceMetadata.

        上传制品时，是否自动触发制品扫描，可选true、false

        :return: The auto_scan of this NamespaceMetadata.
        :rtype: str
        """
        return self._auto_scan

    @auto_scan.setter
    def auto_scan(self, auto_scan):
        r"""Sets the auto_scan of this NamespaceMetadata.

        上传制品时，是否自动触发制品扫描，可选true、false

        :param auto_scan: The auto_scan of this NamespaceMetadata.
        :type auto_scan: str
        """
        self._auto_scan = auto_scan

    @property
    def prevent_vul(self):
        r"""Gets the prevent_vul of this NamespaceMetadata.

        是否开启制品阻断，可选true、false

        :return: The prevent_vul of this NamespaceMetadata.
        :rtype: str
        """
        return self._prevent_vul

    @prevent_vul.setter
    def prevent_vul(self, prevent_vul):
        r"""Sets the prevent_vul of this NamespaceMetadata.

        是否开启制品阻断，可选true、false

        :param prevent_vul: The prevent_vul of this NamespaceMetadata.
        :type prevent_vul: str
        """
        self._prevent_vul = prevent_vul

    @property
    def severity(self):
        r"""Gets the severity of this NamespaceMetadata.

        阻断开启的场景下，如果存在漏洞，并且存在的漏洞严重程度高于此处定义的级别，则无法拉取镜像。可选值为\"none\", \"low\", \"medium\", \"high\", \"critical\"。

        :return: The severity of this NamespaceMetadata.
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        r"""Sets the severity of this NamespaceMetadata.

        阻断开启的场景下，如果存在漏洞，并且存在的漏洞严重程度高于此处定义的级别，则无法拉取镜像。可选值为\"none\", \"low\", \"medium\", \"high\", \"critical\"。

        :param severity: The severity of this NamespaceMetadata.
        :type severity: str
        """
        self._severity = severity

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
        if not isinstance(other, NamespaceMetadata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
