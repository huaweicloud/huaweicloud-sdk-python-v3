# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TaskSettingsTaskConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'scan_mode': 'str',
        'port_scan': 'bool',
        'weak_pwd_scan': 'bool',
        'cve_check': 'bool',
        'text_check': 'bool',
        'picture_check': 'bool',
        'malicious_code': 'bool',
        'malicious_link': 'bool'
    }

    attribute_map = {
        'scan_mode': 'scan_mode',
        'port_scan': 'port_scan',
        'weak_pwd_scan': 'weak_pwd_scan',
        'cve_check': 'cve_check',
        'text_check': 'text_check',
        'picture_check': 'picture_check',
        'malicious_code': 'malicious_code',
        'malicious_link': 'malicious_link'
    }

    def __init__(self, scan_mode=None, port_scan=None, weak_pwd_scan=None, cve_check=None, text_check=None, picture_check=None, malicious_code=None, malicious_link=None):
        """TaskSettingsTaskConfig

        The model defined in huaweicloud sdk

        :param scan_mode: 扫描模式:   * fast - 快速扫描   * normal - 标准扫描   * deep - 深度扫描 
        :type scan_mode: str
        :param port_scan: 是否进行端口扫描
        :type port_scan: bool
        :param weak_pwd_scan: 是否进行弱密码扫描
        :type weak_pwd_scan: bool
        :param cve_check: 是否进行CVE漏洞扫描
        :type cve_check: bool
        :param text_check: 是否进行网站内容合规文字检测
        :type text_check: bool
        :param picture_check: 是否进行网站内容合规图片检测
        :type picture_check: bool
        :param malicious_code: 是否进行网站挂马检测
        :type malicious_code: bool
        :param malicious_link: 是否进行链接健康检测（死链、暗链、恶意外链）
        :type malicious_link: bool
        """
        
        

        self._scan_mode = None
        self._port_scan = None
        self._weak_pwd_scan = None
        self._cve_check = None
        self._text_check = None
        self._picture_check = None
        self._malicious_code = None
        self._malicious_link = None
        self.discriminator = None

        if scan_mode is not None:
            self.scan_mode = scan_mode
        if port_scan is not None:
            self.port_scan = port_scan
        if weak_pwd_scan is not None:
            self.weak_pwd_scan = weak_pwd_scan
        if cve_check is not None:
            self.cve_check = cve_check
        if text_check is not None:
            self.text_check = text_check
        if picture_check is not None:
            self.picture_check = picture_check
        if malicious_code is not None:
            self.malicious_code = malicious_code
        if malicious_link is not None:
            self.malicious_link = malicious_link

    @property
    def scan_mode(self):
        """Gets the scan_mode of this TaskSettingsTaskConfig.

        扫描模式:   * fast - 快速扫描   * normal - 标准扫描   * deep - 深度扫描 

        :return: The scan_mode of this TaskSettingsTaskConfig.
        :rtype: str
        """
        return self._scan_mode

    @scan_mode.setter
    def scan_mode(self, scan_mode):
        """Sets the scan_mode of this TaskSettingsTaskConfig.

        扫描模式:   * fast - 快速扫描   * normal - 标准扫描   * deep - 深度扫描 

        :param scan_mode: The scan_mode of this TaskSettingsTaskConfig.
        :type scan_mode: str
        """
        self._scan_mode = scan_mode

    @property
    def port_scan(self):
        """Gets the port_scan of this TaskSettingsTaskConfig.

        是否进行端口扫描

        :return: The port_scan of this TaskSettingsTaskConfig.
        :rtype: bool
        """
        return self._port_scan

    @port_scan.setter
    def port_scan(self, port_scan):
        """Sets the port_scan of this TaskSettingsTaskConfig.

        是否进行端口扫描

        :param port_scan: The port_scan of this TaskSettingsTaskConfig.
        :type port_scan: bool
        """
        self._port_scan = port_scan

    @property
    def weak_pwd_scan(self):
        """Gets the weak_pwd_scan of this TaskSettingsTaskConfig.

        是否进行弱密码扫描

        :return: The weak_pwd_scan of this TaskSettingsTaskConfig.
        :rtype: bool
        """
        return self._weak_pwd_scan

    @weak_pwd_scan.setter
    def weak_pwd_scan(self, weak_pwd_scan):
        """Sets the weak_pwd_scan of this TaskSettingsTaskConfig.

        是否进行弱密码扫描

        :param weak_pwd_scan: The weak_pwd_scan of this TaskSettingsTaskConfig.
        :type weak_pwd_scan: bool
        """
        self._weak_pwd_scan = weak_pwd_scan

    @property
    def cve_check(self):
        """Gets the cve_check of this TaskSettingsTaskConfig.

        是否进行CVE漏洞扫描

        :return: The cve_check of this TaskSettingsTaskConfig.
        :rtype: bool
        """
        return self._cve_check

    @cve_check.setter
    def cve_check(self, cve_check):
        """Sets the cve_check of this TaskSettingsTaskConfig.

        是否进行CVE漏洞扫描

        :param cve_check: The cve_check of this TaskSettingsTaskConfig.
        :type cve_check: bool
        """
        self._cve_check = cve_check

    @property
    def text_check(self):
        """Gets the text_check of this TaskSettingsTaskConfig.

        是否进行网站内容合规文字检测

        :return: The text_check of this TaskSettingsTaskConfig.
        :rtype: bool
        """
        return self._text_check

    @text_check.setter
    def text_check(self, text_check):
        """Sets the text_check of this TaskSettingsTaskConfig.

        是否进行网站内容合规文字检测

        :param text_check: The text_check of this TaskSettingsTaskConfig.
        :type text_check: bool
        """
        self._text_check = text_check

    @property
    def picture_check(self):
        """Gets the picture_check of this TaskSettingsTaskConfig.

        是否进行网站内容合规图片检测

        :return: The picture_check of this TaskSettingsTaskConfig.
        :rtype: bool
        """
        return self._picture_check

    @picture_check.setter
    def picture_check(self, picture_check):
        """Sets the picture_check of this TaskSettingsTaskConfig.

        是否进行网站内容合规图片检测

        :param picture_check: The picture_check of this TaskSettingsTaskConfig.
        :type picture_check: bool
        """
        self._picture_check = picture_check

    @property
    def malicious_code(self):
        """Gets the malicious_code of this TaskSettingsTaskConfig.

        是否进行网站挂马检测

        :return: The malicious_code of this TaskSettingsTaskConfig.
        :rtype: bool
        """
        return self._malicious_code

    @malicious_code.setter
    def malicious_code(self, malicious_code):
        """Sets the malicious_code of this TaskSettingsTaskConfig.

        是否进行网站挂马检测

        :param malicious_code: The malicious_code of this TaskSettingsTaskConfig.
        :type malicious_code: bool
        """
        self._malicious_code = malicious_code

    @property
    def malicious_link(self):
        """Gets the malicious_link of this TaskSettingsTaskConfig.

        是否进行链接健康检测（死链、暗链、恶意外链）

        :return: The malicious_link of this TaskSettingsTaskConfig.
        :rtype: bool
        """
        return self._malicious_link

    @malicious_link.setter
    def malicious_link(self, malicious_link):
        """Sets the malicious_link of this TaskSettingsTaskConfig.

        是否进行链接健康检测（死链、暗链、恶意外链）

        :param malicious_link: The malicious_link of this TaskSettingsTaskConfig.
        :type malicious_link: bool
        """
        self._malicious_link = malicious_link

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
        if not isinstance(other, TaskSettingsTaskConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
