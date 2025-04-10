# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListReportsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'project_id': 'str',
        'page_size': 'int',
        'offset': 'int',
        'version_id': 'str',
        'type': 'int'
    }

    attribute_map = {
        'project_id': 'project_id',
        'page_size': 'page_size',
        'offset': 'offset',
        'version_id': 'version_id',
        'type': 'type'
    }

    def __init__(self, project_id=None, page_size=None, offset=None, version_id=None, type=None):
        r"""ListReportsRequest

        The model defined in huaweicloud sdk

        :param project_id: 项目ID，固定长度32位字符（字母和数字）。
        :type project_id: str
        :param page_size: 每页显示的条目数量,最大支持200条
        :type page_size: int
        :param offset: 页数，page_no大于等于1
        :type offset: int
        :param version_id: 版本id
        :type version_id: str
        :param type: 报表类型 1：首页用例库， 2：质量报告
        :type type: int
        """
        
        

        self._project_id = None
        self._page_size = None
        self._offset = None
        self._version_id = None
        self._type = None
        self.discriminator = None

        self.project_id = project_id
        self.page_size = page_size
        self.offset = offset
        self.version_id = version_id
        self.type = type

    @property
    def project_id(self):
        r"""Gets the project_id of this ListReportsRequest.

        项目ID，固定长度32位字符（字母和数字）。

        :return: The project_id of this ListReportsRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ListReportsRequest.

        项目ID，固定长度32位字符（字母和数字）。

        :param project_id: The project_id of this ListReportsRequest.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def page_size(self):
        r"""Gets the page_size of this ListReportsRequest.

        每页显示的条目数量,最大支持200条

        :return: The page_size of this ListReportsRequest.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        r"""Sets the page_size of this ListReportsRequest.

        每页显示的条目数量,最大支持200条

        :param page_size: The page_size of this ListReportsRequest.
        :type page_size: int
        """
        self._page_size = page_size

    @property
    def offset(self):
        r"""Gets the offset of this ListReportsRequest.

        页数，page_no大于等于1

        :return: The offset of this ListReportsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListReportsRequest.

        页数，page_no大于等于1

        :param offset: The offset of this ListReportsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def version_id(self):
        r"""Gets the version_id of this ListReportsRequest.

        版本id

        :return: The version_id of this ListReportsRequest.
        :rtype: str
        """
        return self._version_id

    @version_id.setter
    def version_id(self, version_id):
        r"""Sets the version_id of this ListReportsRequest.

        版本id

        :param version_id: The version_id of this ListReportsRequest.
        :type version_id: str
        """
        self._version_id = version_id

    @property
    def type(self):
        r"""Gets the type of this ListReportsRequest.

        报表类型 1：首页用例库， 2：质量报告

        :return: The type of this ListReportsRequest.
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ListReportsRequest.

        报表类型 1：首页用例库， 2：质量报告

        :param type: The type of this ListReportsRequest.
        :type type: int
        """
        self._type = type

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
        if not isinstance(other, ListReportsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
