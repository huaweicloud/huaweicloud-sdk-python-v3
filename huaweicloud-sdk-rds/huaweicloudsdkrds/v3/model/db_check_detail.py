# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DBCheckDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'documentation_link': 'str',
        'description': 'str',
        'id': 'str',
        'title': 'str',
        'status': 'str',
        'detected_problems': 'list[DetectedProblem]'
    }

    attribute_map = {
        'documentation_link': 'documentation_link',
        'description': 'description',
        'id': 'id',
        'title': 'title',
        'status': 'status',
        'detected_problems': 'detected_problems'
    }

    def __init__(self, documentation_link=None, description=None, id=None, title=None, status=None, detected_problems=None):
        r"""DBCheckDetail

        The model defined in huaweicloud sdk

        :param documentation_link: 检查说明链接
        :type documentation_link: str
        :param description: 检查项描述
        :type description: str
        :param id: 检查项id
        :type id: str
        :param title: 检查项标题
        :type title: str
        :param status: 检查状态
        :type status: str
        :param detected_problems: 各项检查项检测到的问题
        :type detected_problems: list[:class:`huaweicloudsdkrds.v3.DetectedProblem`]
        """
        
        

        self._documentation_link = None
        self._description = None
        self._id = None
        self._title = None
        self._status = None
        self._detected_problems = None
        self.discriminator = None

        if documentation_link is not None:
            self.documentation_link = documentation_link
        if description is not None:
            self.description = description
        if id is not None:
            self.id = id
        if title is not None:
            self.title = title
        if status is not None:
            self.status = status
        if detected_problems is not None:
            self.detected_problems = detected_problems

    @property
    def documentation_link(self):
        r"""Gets the documentation_link of this DBCheckDetail.

        检查说明链接

        :return: The documentation_link of this DBCheckDetail.
        :rtype: str
        """
        return self._documentation_link

    @documentation_link.setter
    def documentation_link(self, documentation_link):
        r"""Sets the documentation_link of this DBCheckDetail.

        检查说明链接

        :param documentation_link: The documentation_link of this DBCheckDetail.
        :type documentation_link: str
        """
        self._documentation_link = documentation_link

    @property
    def description(self):
        r"""Gets the description of this DBCheckDetail.

        检查项描述

        :return: The description of this DBCheckDetail.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this DBCheckDetail.

        检查项描述

        :param description: The description of this DBCheckDetail.
        :type description: str
        """
        self._description = description

    @property
    def id(self):
        r"""Gets the id of this DBCheckDetail.

        检查项id

        :return: The id of this DBCheckDetail.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this DBCheckDetail.

        检查项id

        :param id: The id of this DBCheckDetail.
        :type id: str
        """
        self._id = id

    @property
    def title(self):
        r"""Gets the title of this DBCheckDetail.

        检查项标题

        :return: The title of this DBCheckDetail.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        r"""Sets the title of this DBCheckDetail.

        检查项标题

        :param title: The title of this DBCheckDetail.
        :type title: str
        """
        self._title = title

    @property
    def status(self):
        r"""Gets the status of this DBCheckDetail.

        检查状态

        :return: The status of this DBCheckDetail.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this DBCheckDetail.

        检查状态

        :param status: The status of this DBCheckDetail.
        :type status: str
        """
        self._status = status

    @property
    def detected_problems(self):
        r"""Gets the detected_problems of this DBCheckDetail.

        各项检查项检测到的问题

        :return: The detected_problems of this DBCheckDetail.
        :rtype: list[:class:`huaweicloudsdkrds.v3.DetectedProblem`]
        """
        return self._detected_problems

    @detected_problems.setter
    def detected_problems(self, detected_problems):
        r"""Sets the detected_problems of this DBCheckDetail.

        各项检查项检测到的问题

        :param detected_problems: The detected_problems of this DBCheckDetail.
        :type detected_problems: list[:class:`huaweicloudsdkrds.v3.DetectedProblem`]
        """
        self._detected_problems = detected_problems

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
        if not isinstance(other, DBCheckDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
