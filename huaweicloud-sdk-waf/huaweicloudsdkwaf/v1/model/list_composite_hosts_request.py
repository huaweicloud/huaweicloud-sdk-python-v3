# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCompositeHostsRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'page': 'int',
        'pagesize': 'int',
        'hostname': 'str',
        'policyname': 'str',
        'protect_status': 'int',
        'waf_type': 'str',
        'is_https': 'bool'
    }

    attribute_map = {
        'page': 'page',
        'pagesize': 'pagesize',
        'hostname': 'hostname',
        'policyname': 'policyname',
        'protect_status': 'protect_status',
        'waf_type': 'waf_type',
        'is_https': 'is_https'
    }

    def __init__(self, page=None, pagesize=None, hostname=None, policyname=None, protect_status=None, waf_type=None, is_https=None):
        """ListCompositeHostsRequest - a model defined in huaweicloud sdk"""
        
        

        self._page = None
        self._pagesize = None
        self._hostname = None
        self._policyname = None
        self._protect_status = None
        self._waf_type = None
        self._is_https = None
        self.discriminator = None

        if page is not None:
            self.page = page
        if pagesize is not None:
            self.pagesize = pagesize
        if hostname is not None:
            self.hostname = hostname
        if policyname is not None:
            self.policyname = policyname
        if protect_status is not None:
            self.protect_status = protect_status
        if waf_type is not None:
            self.waf_type = waf_type
        if is_https is not None:
            self.is_https = is_https

    @property
    def page(self):
        """Gets the page of this ListCompositeHostsRequest.

        page

        :return: The page of this ListCompositeHostsRequest.
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this ListCompositeHostsRequest.

        page

        :param page: The page of this ListCompositeHostsRequest.
        :type: int
        """
        self._page = page

    @property
    def pagesize(self):
        """Gets the pagesize of this ListCompositeHostsRequest.

        每页条数

        :return: The pagesize of this ListCompositeHostsRequest.
        :rtype: int
        """
        return self._pagesize

    @pagesize.setter
    def pagesize(self, pagesize):
        """Sets the pagesize of this ListCompositeHostsRequest.

        每页条数

        :param pagesize: The pagesize of this ListCompositeHostsRequest.
        :type: int
        """
        self._pagesize = pagesize

    @property
    def hostname(self):
        """Gets the hostname of this ListCompositeHostsRequest.

        域名名称

        :return: The hostname of this ListCompositeHostsRequest.
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """Sets the hostname of this ListCompositeHostsRequest.

        域名名称

        :param hostname: The hostname of this ListCompositeHostsRequest.
        :type: str
        """
        self._hostname = hostname

    @property
    def policyname(self):
        """Gets the policyname of this ListCompositeHostsRequest.

        防护策略名称

        :return: The policyname of this ListCompositeHostsRequest.
        :rtype: str
        """
        return self._policyname

    @policyname.setter
    def policyname(self, policyname):
        """Sets the policyname of this ListCompositeHostsRequest.

        防护策略名称

        :param policyname: The policyname of this ListCompositeHostsRequest.
        :type: str
        """
        self._policyname = policyname

    @property
    def protect_status(self):
        """Gets the protect_status of this ListCompositeHostsRequest.

        域名防护状态

        :return: The protect_status of this ListCompositeHostsRequest.
        :rtype: int
        """
        return self._protect_status

    @protect_status.setter
    def protect_status(self, protect_status):
        """Sets the protect_status of this ListCompositeHostsRequest.

        域名防护状态

        :param protect_status: The protect_status of this ListCompositeHostsRequest.
        :type: int
        """
        self._protect_status = protect_status

    @property
    def waf_type(self):
        """Gets the waf_type of this ListCompositeHostsRequest.

        域名所属WAF模式

        :return: The waf_type of this ListCompositeHostsRequest.
        :rtype: str
        """
        return self._waf_type

    @waf_type.setter
    def waf_type(self, waf_type):
        """Sets the waf_type of this ListCompositeHostsRequest.

        域名所属WAF模式

        :param waf_type: The waf_type of this ListCompositeHostsRequest.
        :type: str
        """
        self._waf_type = waf_type

    @property
    def is_https(self):
        """Gets the is_https of this ListCompositeHostsRequest.

        域名是否使用HTTPS

        :return: The is_https of this ListCompositeHostsRequest.
        :rtype: bool
        """
        return self._is_https

    @is_https.setter
    def is_https(self, is_https):
        """Sets the is_https of this ListCompositeHostsRequest.

        域名是否使用HTTPS

        :param is_https: The is_https of this ListCompositeHostsRequest.
        :type: bool
        """
        self._is_https = is_https

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
        if not isinstance(other, ListCompositeHostsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
