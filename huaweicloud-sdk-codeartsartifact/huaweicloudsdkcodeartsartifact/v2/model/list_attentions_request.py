# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAttentionsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'page_no': 'int',
        'page_size': 'int',
        'project_id': 'str'
    }

    attribute_map = {
        'page_no': 'page_no',
        'page_size': 'page_size',
        'project_id': 'project_id'
    }

    def __init__(self, page_no=None, page_size=None, project_id=None):
        r"""ListAttentionsRequest

        The model defined in huaweicloud sdk

        :param page_no: 页码
        :type page_no: int
        :param page_size: 每页大小
        :type page_size: int
        :param project_id: 项目id
        :type project_id: str
        """
        
        

        self._page_no = None
        self._page_size = None
        self._project_id = None
        self.discriminator = None

        if page_no is not None:
            self.page_no = page_no
        if page_size is not None:
            self.page_size = page_size
        if project_id is not None:
            self.project_id = project_id

    @property
    def page_no(self):
        r"""Gets the page_no of this ListAttentionsRequest.

        页码

        :return: The page_no of this ListAttentionsRequest.
        :rtype: int
        """
        return self._page_no

    @page_no.setter
    def page_no(self, page_no):
        r"""Sets the page_no of this ListAttentionsRequest.

        页码

        :param page_no: The page_no of this ListAttentionsRequest.
        :type page_no: int
        """
        self._page_no = page_no

    @property
    def page_size(self):
        r"""Gets the page_size of this ListAttentionsRequest.

        每页大小

        :return: The page_size of this ListAttentionsRequest.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        r"""Sets the page_size of this ListAttentionsRequest.

        每页大小

        :param page_size: The page_size of this ListAttentionsRequest.
        :type page_size: int
        """
        self._page_size = page_size

    @property
    def project_id(self):
        r"""Gets the project_id of this ListAttentionsRequest.

        项目id

        :return: The project_id of this ListAttentionsRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ListAttentionsRequest.

        项目id

        :param project_id: The project_id of this ListAttentionsRequest.
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
        if not isinstance(other, ListAttentionsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
