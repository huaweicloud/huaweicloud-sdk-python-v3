# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListVariablesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'group_id': 'str',
        'page_no': 'str',
        'page_size': 'str',
        'project_id': 'str'
    }

    attribute_map = {
        'group_id': 'group_id',
        'page_no': 'page_no',
        'page_size': 'page_size',
        'project_id': 'project_id'
    }

    def __init__(self, group_id=None, page_no=None, page_size=None, project_id=None):
        """ListVariablesRequest

        The model defined in huaweicloud sdk

        :param group_id: group_id
        :type group_id: str
        :param page_no: 当前页数
        :type page_no: str
        :param page_size: 每页多少记录
        :type page_size: str
        :param project_id: 工程id
        :type project_id: str
        """
        
        

        self._group_id = None
        self._page_no = None
        self._page_size = None
        self._project_id = None
        self.discriminator = None

        if group_id is not None:
            self.group_id = group_id
        if page_no is not None:
            self.page_no = page_no
        if page_size is not None:
            self.page_size = page_size
        self.project_id = project_id

    @property
    def group_id(self):
        """Gets the group_id of this ListVariablesRequest.

        group_id

        :return: The group_id of this ListVariablesRequest.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this ListVariablesRequest.

        group_id

        :param group_id: The group_id of this ListVariablesRequest.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def page_no(self):
        """Gets the page_no of this ListVariablesRequest.

        当前页数

        :return: The page_no of this ListVariablesRequest.
        :rtype: str
        """
        return self._page_no

    @page_no.setter
    def page_no(self, page_no):
        """Sets the page_no of this ListVariablesRequest.

        当前页数

        :param page_no: The page_no of this ListVariablesRequest.
        :type page_no: str
        """
        self._page_no = page_no

    @property
    def page_size(self):
        """Gets the page_size of this ListVariablesRequest.

        每页多少记录

        :return: The page_size of this ListVariablesRequest.
        :rtype: str
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this ListVariablesRequest.

        每页多少记录

        :param page_size: The page_size of this ListVariablesRequest.
        :type page_size: str
        """
        self._page_size = page_size

    @property
    def project_id(self):
        """Gets the project_id of this ListVariablesRequest.

        工程id

        :return: The project_id of this ListVariablesRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this ListVariablesRequest.

        工程id

        :param project_id: The project_id of this ListVariablesRequest.
        :type project_id: str
        """
        self._project_id = project_id

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
        if not isinstance(other, ListVariablesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
