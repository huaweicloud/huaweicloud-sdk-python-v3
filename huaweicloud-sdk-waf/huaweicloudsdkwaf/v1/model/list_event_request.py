# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListEventRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'recent': 'str',
        'hosts': 'list[str]',
        'page': 'int',
        'pagesize': 'int'
    }

    attribute_map = {
        'recent': 'recent',
        'hosts': 'hosts',
        'page': 'page',
        'pagesize': 'pagesize'
    }

    def __init__(self, recent=None, hosts=None, page=None, pagesize=None):
        """ListEventRequest - a model defined in huaweicloud sdk"""
        
        

        self._recent = None
        self._hosts = None
        self._page = None
        self._pagesize = None
        self.discriminator = None

        self.recent = recent
        if hosts is not None:
            self.hosts = hosts
        if page is not None:
            self.page = page
        if pagesize is not None:
            self.pagesize = pagesize

    @property
    def recent(self):
        """Gets the recent of this ListEventRequest.

        查询日志的时间范围

        :return: The recent of this ListEventRequest.
        :rtype: str
        """
        return self._recent

    @recent.setter
    def recent(self, recent):
        """Sets the recent of this ListEventRequest.

        查询日志的时间范围

        :param recent: The recent of this ListEventRequest.
        :type: str
        """
        self._recent = recent

    @property
    def hosts(self):
        """Gets the hosts of this ListEventRequest.

        域名id9从获取防护网站列表获取域名id）

        :return: The hosts of this ListEventRequest.
        :rtype: list[str]
        """
        return self._hosts

    @hosts.setter
    def hosts(self, hosts):
        """Sets the hosts of this ListEventRequest.

        域名id9从获取防护网站列表获取域名id）

        :param hosts: The hosts of this ListEventRequest.
        :type: list[str]
        """
        self._hosts = hosts

    @property
    def page(self):
        """Gets the page of this ListEventRequest.

        页码

        :return: The page of this ListEventRequest.
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this ListEventRequest.

        页码

        :param page: The page of this ListEventRequest.
        :type: int
        """
        self._page = page

    @property
    def pagesize(self):
        """Gets the pagesize of this ListEventRequest.

        每页的条数

        :return: The pagesize of this ListEventRequest.
        :rtype: int
        """
        return self._pagesize

    @pagesize.setter
    def pagesize(self, pagesize):
        """Sets the pagesize of this ListEventRequest.

        每页的条数

        :param pagesize: The pagesize of this ListEventRequest.
        :type: int
        """
        self._pagesize = pagesize

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
        if not isinstance(other, ListEventRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
