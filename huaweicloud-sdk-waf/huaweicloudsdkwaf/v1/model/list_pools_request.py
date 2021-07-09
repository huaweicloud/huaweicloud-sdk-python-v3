# coding: utf-8

import re
import six





class ListPoolsRequest:


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
        'name': 'str',
        'vpc_id': 'str',
        'detail': 'bool'
    }

    attribute_map = {
        'page': 'page',
        'pagesize': 'pagesize',
        'name': 'name',
        'vpc_id': 'vpc_id',
        'detail': 'detail'
    }

    def __init__(self, page=None, pagesize=None, name=None, vpc_id=None, detail=None):
        """ListPoolsRequest - a model defined in huaweicloud sdk"""
        
        

        self._page = None
        self._pagesize = None
        self._name = None
        self._vpc_id = None
        self._detail = None
        self.discriminator = None

        if page is not None:
            self.page = page
        if pagesize is not None:
            self.pagesize = pagesize
        if name is not None:
            self.name = name
        if vpc_id is not None:
            self.vpc_id = vpc_id
        if detail is not None:
            self.detail = detail

    @property
    def page(self):
        """Gets the page of this ListPoolsRequest.

        当前页数

        :return: The page of this ListPoolsRequest.
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this ListPoolsRequest.

        当前页数

        :param page: The page of this ListPoolsRequest.
        :type: int
        """
        self._page = page

    @property
    def pagesize(self):
        """Gets the pagesize of this ListPoolsRequest.

        页内项目数

        :return: The pagesize of this ListPoolsRequest.
        :rtype: int
        """
        return self._pagesize

    @pagesize.setter
    def pagesize(self, pagesize):
        """Sets the pagesize of this ListPoolsRequest.

        页内项目数

        :param pagesize: The pagesize of this ListPoolsRequest.
        :type: int
        """
        self._pagesize = pagesize

    @property
    def name(self):
        """Gets the name of this ListPoolsRequest.

        WAF组名称

        :return: The name of this ListPoolsRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListPoolsRequest.

        WAF组名称

        :param name: The name of this ListPoolsRequest.
        :type: str
        """
        self._name = name

    @property
    def vpc_id(self):
        """Gets the vpc_id of this ListPoolsRequest.

        WAF组所在VPC ID

        :return: The vpc_id of this ListPoolsRequest.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this ListPoolsRequest.

        WAF组所在VPC ID

        :param vpc_id: The vpc_id of this ListPoolsRequest.
        :type: str
        """
        self._vpc_id = vpc_id

    @property
    def detail(self):
        """Gets the detail of this ListPoolsRequest.

        是否返回WAF组详情（例如组内域名/实例等）

        :return: The detail of this ListPoolsRequest.
        :rtype: bool
        """
        return self._detail

    @detail.setter
    def detail(self, detail):
        """Sets the detail of this ListPoolsRequest.

        是否返回WAF组详情（例如组内域名/实例等）

        :param detail: The detail of this ListPoolsRequest.
        :type: bool
        """
        self._detail = detail

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
        import simplejson as json
        return json.dumps(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListPoolsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
