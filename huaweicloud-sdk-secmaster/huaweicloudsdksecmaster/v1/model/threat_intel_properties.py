# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ThreatIntelProperties:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'file_md5': 'str',
        'file_sha1': 'str',
        'file_sha256': 'str',
        'file_name': 'str',
        'create_time': 'datetime',
        'file_class': 'str',
        'file_family': 'str',
        'file_maltype': 'str',
        'ip_resolves_to_refs': 'str',
        'belongs_to_refs': 'str',
        'ip_location': 'str',
        'domain_family': 'str',
        'domain_resolves_to_refs': 'str',
        'domain_dns_type': 'str',
        'url_host': 'str',
        'url_resolves_to_refs': 'str',
        'display_name': 'str',
        'url_belongs_to_ref': 'str'
    }

    attribute_map = {
        'file_md5': 'file_md5',
        'file_sha1': 'file_sha1',
        'file_sha256': 'file_sha256',
        'file_name': 'file_name',
        'create_time': 'create_time',
        'file_class': 'file_class',
        'file_family': 'file_family',
        'file_maltype': 'file_maltype',
        'ip_resolves_to_refs': 'ip_resolves_to_refs',
        'belongs_to_refs': 'belongs_to_refs',
        'ip_location': 'ip_location',
        'domain_family': 'domain_family',
        'domain_resolves_to_refs': 'domain_resolves_to_refs',
        'domain_dns_type': 'domain_dns_type',
        'url_host': 'url_host',
        'url_resolves_to_refs': 'url_resolves_to_refs',
        'display_name': 'display_name',
        'url_belongs_to_ref': 'url_belongs_to_ref'
    }

    def __init__(self, file_md5=None, file_sha1=None, file_sha256=None, file_name=None, create_time=None, file_class=None, file_family=None, file_maltype=None, ip_resolves_to_refs=None, belongs_to_refs=None, ip_location=None, domain_family=None, domain_resolves_to_refs=None, domain_dns_type=None, url_host=None, url_resolves_to_refs=None, display_name=None, url_belongs_to_ref=None):
        """ThreatIntelProperties

        The model defined in huaweicloud sdk

        :param file_md5: 恶意软件Md5。
        :type file_md5: str
        :param file_sha1: 恶意软件Sha1。
        :type file_sha1: str
        :param file_sha256: 恶意软件Sha256值。
        :type file_sha256: str
        :param file_name: 文件名称。
        :type file_name: str
        :param create_time: 编译时间，格式ISO8601：YYYY-MM-DDTHH:mm:ss.ms+timezone。时区信息为事件发生时区，无法解析时区的时间，默认时区填东八区。
        :type create_time: datetime
        :param file_class: 文件类别，TEXT|XCODE。
        :type file_class: str
        :param file_family: 家族，例如：wannacry（勒索软件）。
        :type file_family: str
        :param file_maltype: 类别，例如：trojan（特洛伊）。
        :type file_maltype: str
        :param ip_resolves_to_refs: mac地址。
        :type ip_resolves_to_refs: str
        :param belongs_to_refs: IP AS 自治系统。
        :type belongs_to_refs: str
        :param ip_location: 地区 格式：country/provice/city/lngwgs/latwgs。
        :type ip_location: str
        :param domain_family: 例如：banjori|iodine。
        :type domain_family: str
        :param domain_resolves_to_refs: 解析的IP地址。
        :type domain_resolves_to_refs: str
        :param domain_dns_type: DNS类别。A|NS|CNAME|TXT。
        :type domain_dns_type: str
        :param url_host: 例：3ms.huawei.com。
        :type url_host: str
        :param url_resolves_to_refs: IP地址。
        :type url_resolves_to_refs: str
        :param display_name: 显示名称。
        :type display_name: str
        :param url_belongs_to_ref: 邮箱账户，@之前部分。
        :type url_belongs_to_ref: str
        """
        
        

        self._file_md5 = None
        self._file_sha1 = None
        self._file_sha256 = None
        self._file_name = None
        self._create_time = None
        self._file_class = None
        self._file_family = None
        self._file_maltype = None
        self._ip_resolves_to_refs = None
        self._belongs_to_refs = None
        self._ip_location = None
        self._domain_family = None
        self._domain_resolves_to_refs = None
        self._domain_dns_type = None
        self._url_host = None
        self._url_resolves_to_refs = None
        self._display_name = None
        self._url_belongs_to_ref = None
        self.discriminator = None

        if file_md5 is not None:
            self.file_md5 = file_md5
        if file_sha1 is not None:
            self.file_sha1 = file_sha1
        if file_sha256 is not None:
            self.file_sha256 = file_sha256
        if file_name is not None:
            self.file_name = file_name
        if create_time is not None:
            self.create_time = create_time
        if file_class is not None:
            self.file_class = file_class
        if file_family is not None:
            self.file_family = file_family
        if file_maltype is not None:
            self.file_maltype = file_maltype
        if ip_resolves_to_refs is not None:
            self.ip_resolves_to_refs = ip_resolves_to_refs
        if belongs_to_refs is not None:
            self.belongs_to_refs = belongs_to_refs
        if ip_location is not None:
            self.ip_location = ip_location
        if domain_family is not None:
            self.domain_family = domain_family
        if domain_resolves_to_refs is not None:
            self.domain_resolves_to_refs = domain_resolves_to_refs
        if domain_dns_type is not None:
            self.domain_dns_type = domain_dns_type
        if url_host is not None:
            self.url_host = url_host
        if url_resolves_to_refs is not None:
            self.url_resolves_to_refs = url_resolves_to_refs
        if display_name is not None:
            self.display_name = display_name
        if url_belongs_to_ref is not None:
            self.url_belongs_to_ref = url_belongs_to_ref

    @property
    def file_md5(self):
        """Gets the file_md5 of this ThreatIntelProperties.

        恶意软件Md5。

        :return: The file_md5 of this ThreatIntelProperties.
        :rtype: str
        """
        return self._file_md5

    @file_md5.setter
    def file_md5(self, file_md5):
        """Sets the file_md5 of this ThreatIntelProperties.

        恶意软件Md5。

        :param file_md5: The file_md5 of this ThreatIntelProperties.
        :type file_md5: str
        """
        self._file_md5 = file_md5

    @property
    def file_sha1(self):
        """Gets the file_sha1 of this ThreatIntelProperties.

        恶意软件Sha1。

        :return: The file_sha1 of this ThreatIntelProperties.
        :rtype: str
        """
        return self._file_sha1

    @file_sha1.setter
    def file_sha1(self, file_sha1):
        """Sets the file_sha1 of this ThreatIntelProperties.

        恶意软件Sha1。

        :param file_sha1: The file_sha1 of this ThreatIntelProperties.
        :type file_sha1: str
        """
        self._file_sha1 = file_sha1

    @property
    def file_sha256(self):
        """Gets the file_sha256 of this ThreatIntelProperties.

        恶意软件Sha256值。

        :return: The file_sha256 of this ThreatIntelProperties.
        :rtype: str
        """
        return self._file_sha256

    @file_sha256.setter
    def file_sha256(self, file_sha256):
        """Sets the file_sha256 of this ThreatIntelProperties.

        恶意软件Sha256值。

        :param file_sha256: The file_sha256 of this ThreatIntelProperties.
        :type file_sha256: str
        """
        self._file_sha256 = file_sha256

    @property
    def file_name(self):
        """Gets the file_name of this ThreatIntelProperties.

        文件名称。

        :return: The file_name of this ThreatIntelProperties.
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this ThreatIntelProperties.

        文件名称。

        :param file_name: The file_name of this ThreatIntelProperties.
        :type file_name: str
        """
        self._file_name = file_name

    @property
    def create_time(self):
        """Gets the create_time of this ThreatIntelProperties.

        编译时间，格式ISO8601：YYYY-MM-DDTHH:mm:ss.ms+timezone。时区信息为事件发生时区，无法解析时区的时间，默认时区填东八区。

        :return: The create_time of this ThreatIntelProperties.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this ThreatIntelProperties.

        编译时间，格式ISO8601：YYYY-MM-DDTHH:mm:ss.ms+timezone。时区信息为事件发生时区，无法解析时区的时间，默认时区填东八区。

        :param create_time: The create_time of this ThreatIntelProperties.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def file_class(self):
        """Gets the file_class of this ThreatIntelProperties.

        文件类别，TEXT|XCODE。

        :return: The file_class of this ThreatIntelProperties.
        :rtype: str
        """
        return self._file_class

    @file_class.setter
    def file_class(self, file_class):
        """Sets the file_class of this ThreatIntelProperties.

        文件类别，TEXT|XCODE。

        :param file_class: The file_class of this ThreatIntelProperties.
        :type file_class: str
        """
        self._file_class = file_class

    @property
    def file_family(self):
        """Gets the file_family of this ThreatIntelProperties.

        家族，例如：wannacry（勒索软件）。

        :return: The file_family of this ThreatIntelProperties.
        :rtype: str
        """
        return self._file_family

    @file_family.setter
    def file_family(self, file_family):
        """Sets the file_family of this ThreatIntelProperties.

        家族，例如：wannacry（勒索软件）。

        :param file_family: The file_family of this ThreatIntelProperties.
        :type file_family: str
        """
        self._file_family = file_family

    @property
    def file_maltype(self):
        """Gets the file_maltype of this ThreatIntelProperties.

        类别，例如：trojan（特洛伊）。

        :return: The file_maltype of this ThreatIntelProperties.
        :rtype: str
        """
        return self._file_maltype

    @file_maltype.setter
    def file_maltype(self, file_maltype):
        """Sets the file_maltype of this ThreatIntelProperties.

        类别，例如：trojan（特洛伊）。

        :param file_maltype: The file_maltype of this ThreatIntelProperties.
        :type file_maltype: str
        """
        self._file_maltype = file_maltype

    @property
    def ip_resolves_to_refs(self):
        """Gets the ip_resolves_to_refs of this ThreatIntelProperties.

        mac地址。

        :return: The ip_resolves_to_refs of this ThreatIntelProperties.
        :rtype: str
        """
        return self._ip_resolves_to_refs

    @ip_resolves_to_refs.setter
    def ip_resolves_to_refs(self, ip_resolves_to_refs):
        """Sets the ip_resolves_to_refs of this ThreatIntelProperties.

        mac地址。

        :param ip_resolves_to_refs: The ip_resolves_to_refs of this ThreatIntelProperties.
        :type ip_resolves_to_refs: str
        """
        self._ip_resolves_to_refs = ip_resolves_to_refs

    @property
    def belongs_to_refs(self):
        """Gets the belongs_to_refs of this ThreatIntelProperties.

        IP AS 自治系统。

        :return: The belongs_to_refs of this ThreatIntelProperties.
        :rtype: str
        """
        return self._belongs_to_refs

    @belongs_to_refs.setter
    def belongs_to_refs(self, belongs_to_refs):
        """Sets the belongs_to_refs of this ThreatIntelProperties.

        IP AS 自治系统。

        :param belongs_to_refs: The belongs_to_refs of this ThreatIntelProperties.
        :type belongs_to_refs: str
        """
        self._belongs_to_refs = belongs_to_refs

    @property
    def ip_location(self):
        """Gets the ip_location of this ThreatIntelProperties.

        地区 格式：country/provice/city/lngwgs/latwgs。

        :return: The ip_location of this ThreatIntelProperties.
        :rtype: str
        """
        return self._ip_location

    @ip_location.setter
    def ip_location(self, ip_location):
        """Sets the ip_location of this ThreatIntelProperties.

        地区 格式：country/provice/city/lngwgs/latwgs。

        :param ip_location: The ip_location of this ThreatIntelProperties.
        :type ip_location: str
        """
        self._ip_location = ip_location

    @property
    def domain_family(self):
        """Gets the domain_family of this ThreatIntelProperties.

        例如：banjori|iodine。

        :return: The domain_family of this ThreatIntelProperties.
        :rtype: str
        """
        return self._domain_family

    @domain_family.setter
    def domain_family(self, domain_family):
        """Sets the domain_family of this ThreatIntelProperties.

        例如：banjori|iodine。

        :param domain_family: The domain_family of this ThreatIntelProperties.
        :type domain_family: str
        """
        self._domain_family = domain_family

    @property
    def domain_resolves_to_refs(self):
        """Gets the domain_resolves_to_refs of this ThreatIntelProperties.

        解析的IP地址。

        :return: The domain_resolves_to_refs of this ThreatIntelProperties.
        :rtype: str
        """
        return self._domain_resolves_to_refs

    @domain_resolves_to_refs.setter
    def domain_resolves_to_refs(self, domain_resolves_to_refs):
        """Sets the domain_resolves_to_refs of this ThreatIntelProperties.

        解析的IP地址。

        :param domain_resolves_to_refs: The domain_resolves_to_refs of this ThreatIntelProperties.
        :type domain_resolves_to_refs: str
        """
        self._domain_resolves_to_refs = domain_resolves_to_refs

    @property
    def domain_dns_type(self):
        """Gets the domain_dns_type of this ThreatIntelProperties.

        DNS类别。A|NS|CNAME|TXT。

        :return: The domain_dns_type of this ThreatIntelProperties.
        :rtype: str
        """
        return self._domain_dns_type

    @domain_dns_type.setter
    def domain_dns_type(self, domain_dns_type):
        """Sets the domain_dns_type of this ThreatIntelProperties.

        DNS类别。A|NS|CNAME|TXT。

        :param domain_dns_type: The domain_dns_type of this ThreatIntelProperties.
        :type domain_dns_type: str
        """
        self._domain_dns_type = domain_dns_type

    @property
    def url_host(self):
        """Gets the url_host of this ThreatIntelProperties.

        例：3ms.huawei.com。

        :return: The url_host of this ThreatIntelProperties.
        :rtype: str
        """
        return self._url_host

    @url_host.setter
    def url_host(self, url_host):
        """Sets the url_host of this ThreatIntelProperties.

        例：3ms.huawei.com。

        :param url_host: The url_host of this ThreatIntelProperties.
        :type url_host: str
        """
        self._url_host = url_host

    @property
    def url_resolves_to_refs(self):
        """Gets the url_resolves_to_refs of this ThreatIntelProperties.

        IP地址。

        :return: The url_resolves_to_refs of this ThreatIntelProperties.
        :rtype: str
        """
        return self._url_resolves_to_refs

    @url_resolves_to_refs.setter
    def url_resolves_to_refs(self, url_resolves_to_refs):
        """Sets the url_resolves_to_refs of this ThreatIntelProperties.

        IP地址。

        :param url_resolves_to_refs: The url_resolves_to_refs of this ThreatIntelProperties.
        :type url_resolves_to_refs: str
        """
        self._url_resolves_to_refs = url_resolves_to_refs

    @property
    def display_name(self):
        """Gets the display_name of this ThreatIntelProperties.

        显示名称。

        :return: The display_name of this ThreatIntelProperties.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this ThreatIntelProperties.

        显示名称。

        :param display_name: The display_name of this ThreatIntelProperties.
        :type display_name: str
        """
        self._display_name = display_name

    @property
    def url_belongs_to_ref(self):
        """Gets the url_belongs_to_ref of this ThreatIntelProperties.

        邮箱账户，@之前部分。

        :return: The url_belongs_to_ref of this ThreatIntelProperties.
        :rtype: str
        """
        return self._url_belongs_to_ref

    @url_belongs_to_ref.setter
    def url_belongs_to_ref(self, url_belongs_to_ref):
        """Sets the url_belongs_to_ref of this ThreatIntelProperties.

        邮箱账户，@之前部分。

        :param url_belongs_to_ref: The url_belongs_to_ref of this ThreatIntelProperties.
        :type url_belongs_to_ref: str
        """
        self._url_belongs_to_ref = url_belongs_to_ref

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
        if not isinstance(other, ThreatIntelProperties):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
