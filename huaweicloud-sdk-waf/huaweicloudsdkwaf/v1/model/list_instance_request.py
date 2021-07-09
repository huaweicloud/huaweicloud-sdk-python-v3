# coding: utf-8

import re
import six





class ListInstanceRequest:


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
        'instancename': 'str'
    }

    attribute_map = {
        'page': 'page',
        'pagesize': 'pagesize',
        'instancename': 'instancename'
    }

    def __init__(self, page=None, pagesize=None, instancename=None):
        """ListInstanceRequest - a model defined in huaweicloud sdk"""
        
        

        self._page = None
        self._pagesize = None
        self._instancename = None
        self.discriminator = None

        if page is not None:
            self.page = page
        if pagesize is not None:
            self.pagesize = pagesize
        if instancename is not None:
            self.instancename = instancename

    @property
    def page(self):
        """Gets the page of this ListInstanceRequest.

        页数

        :return: The page of this ListInstanceRequest.
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this ListInstanceRequest.

        页数

        :param page: The page of this ListInstanceRequest.
        :type: int
        """
        self._page = page

    @property
    def pagesize(self):
        """Gets the pagesize of this ListInstanceRequest.

        每页数量

        :return: The pagesize of this ListInstanceRequest.
        :rtype: int
        """
        return self._pagesize

    @pagesize.setter
    def pagesize(self, pagesize):
        """Sets the pagesize of this ListInstanceRequest.

        每页数量

        :param pagesize: The pagesize of this ListInstanceRequest.
        :type: int
        """
        self._pagesize = pagesize

    @property
    def instancename(self):
        """Gets the instancename of this ListInstanceRequest.

        独享引擎名称

        :return: The instancename of this ListInstanceRequest.
        :rtype: str
        """
        return self._instancename

    @instancename.setter
    def instancename(self, instancename):
        """Sets the instancename of this ListInstanceRequest.

        独享引擎名称

        :param instancename: The instancename of this ListInstanceRequest.
        :type: str
        """
        self._instancename = instancename

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
        if not isinstance(other, ListInstanceRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
