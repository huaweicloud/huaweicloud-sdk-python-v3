# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SearchByChecksumRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'checksum': 'str',
        'page_no': 'int',
        'page_size': 'int',
        'format': 'str',
        'in_project': 'str',
        'project_id': 'str'
    }

    attribute_map = {
        'checksum': 'checksum',
        'page_no': 'page_no',
        'page_size': 'page_size',
        'format': 'format',
        'in_project': 'in_project',
        'project_id': 'project_id'
    }

    def __init__(self, checksum=None, page_no=None, page_size=None, format=None, in_project=None, project_id=None):
        r"""SearchByChecksumRequest

        The model defined in huaweicloud sdk

        :param checksum: checksum
        :type checksum: str
        :param page_no: 页码
        :type page_no: int
        :param page_size: 每页条数
        :type page_size: int
        :param format: 仓库类型
        :type format: str
        :param in_project: 是否在项目中
        :type in_project: str
        :param project_id: 项目id
        :type project_id: str
        """
        
        

        self._checksum = None
        self._page_no = None
        self._page_size = None
        self._format = None
        self._in_project = None
        self._project_id = None
        self.discriminator = None

        self.checksum = checksum
        if page_no is not None:
            self.page_no = page_no
        if page_size is not None:
            self.page_size = page_size
        if format is not None:
            self.format = format
        if in_project is not None:
            self.in_project = in_project
        if project_id is not None:
            self.project_id = project_id

    @property
    def checksum(self):
        r"""Gets the checksum of this SearchByChecksumRequest.

        checksum

        :return: The checksum of this SearchByChecksumRequest.
        :rtype: str
        """
        return self._checksum

    @checksum.setter
    def checksum(self, checksum):
        r"""Sets the checksum of this SearchByChecksumRequest.

        checksum

        :param checksum: The checksum of this SearchByChecksumRequest.
        :type checksum: str
        """
        self._checksum = checksum

    @property
    def page_no(self):
        r"""Gets the page_no of this SearchByChecksumRequest.

        页码

        :return: The page_no of this SearchByChecksumRequest.
        :rtype: int
        """
        return self._page_no

    @page_no.setter
    def page_no(self, page_no):
        r"""Sets the page_no of this SearchByChecksumRequest.

        页码

        :param page_no: The page_no of this SearchByChecksumRequest.
        :type page_no: int
        """
        self._page_no = page_no

    @property
    def page_size(self):
        r"""Gets the page_size of this SearchByChecksumRequest.

        每页条数

        :return: The page_size of this SearchByChecksumRequest.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        r"""Sets the page_size of this SearchByChecksumRequest.

        每页条数

        :param page_size: The page_size of this SearchByChecksumRequest.
        :type page_size: int
        """
        self._page_size = page_size

    @property
    def format(self):
        r"""Gets the format of this SearchByChecksumRequest.

        仓库类型

        :return: The format of this SearchByChecksumRequest.
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        r"""Sets the format of this SearchByChecksumRequest.

        仓库类型

        :param format: The format of this SearchByChecksumRequest.
        :type format: str
        """
        self._format = format

    @property
    def in_project(self):
        r"""Gets the in_project of this SearchByChecksumRequest.

        是否在项目中

        :return: The in_project of this SearchByChecksumRequest.
        :rtype: str
        """
        return self._in_project

    @in_project.setter
    def in_project(self, in_project):
        r"""Sets the in_project of this SearchByChecksumRequest.

        是否在项目中

        :param in_project: The in_project of this SearchByChecksumRequest.
        :type in_project: str
        """
        self._in_project = in_project

    @property
    def project_id(self):
        r"""Gets the project_id of this SearchByChecksumRequest.

        项目id

        :return: The project_id of this SearchByChecksumRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this SearchByChecksumRequest.

        项目id

        :param project_id: The project_id of this SearchByChecksumRequest.
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
        if not isinstance(other, SearchByChecksumRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
