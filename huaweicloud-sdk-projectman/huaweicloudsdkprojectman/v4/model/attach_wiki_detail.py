# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AttachWikiDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'issue_id': 'int',
        'wiki_title': 'str',
        'wiki_author': 'SimpleUser',
        'project': 'SimpleProject',
        'created_date': 'str',
        'wiki_id': 'str',
        'region': 'str'
    }

    attribute_map = {
        'issue_id': 'issue_id',
        'wiki_title': 'wiki_title',
        'wiki_author': 'wiki_author',
        'project': 'project',
        'created_date': 'created_date',
        'wiki_id': 'wiki_id',
        'region': 'region'
    }

    def __init__(self, issue_id=None, wiki_title=None, wiki_author=None, project=None, created_date=None, wiki_id=None, region=None):
        r"""AttachWikiDetail

        The model defined in huaweicloud sdk

        :param issue_id: 工作项ID
        :type issue_id: int
        :param wiki_title: Wiki标题
        :type wiki_title: str
        :param wiki_author: 
        :type wiki_author: :class:`huaweicloudsdkprojectman.v4.SimpleUser`
        :param project: 
        :type project: :class:`huaweicloudsdkprojectman.v4.SimpleProject`
        :param created_date: 创建时间
        :type created_date: str
        :param wiki_id: wiki ID
        :type wiki_id: str
        :param region: region值
        :type region: str
        """
        
        

        self._issue_id = None
        self._wiki_title = None
        self._wiki_author = None
        self._project = None
        self._created_date = None
        self._wiki_id = None
        self._region = None
        self.discriminator = None

        if issue_id is not None:
            self.issue_id = issue_id
        if wiki_title is not None:
            self.wiki_title = wiki_title
        if wiki_author is not None:
            self.wiki_author = wiki_author
        if project is not None:
            self.project = project
        if created_date is not None:
            self.created_date = created_date
        if wiki_id is not None:
            self.wiki_id = wiki_id
        if region is not None:
            self.region = region

    @property
    def issue_id(self):
        r"""Gets the issue_id of this AttachWikiDetail.

        工作项ID

        :return: The issue_id of this AttachWikiDetail.
        :rtype: int
        """
        return self._issue_id

    @issue_id.setter
    def issue_id(self, issue_id):
        r"""Sets the issue_id of this AttachWikiDetail.

        工作项ID

        :param issue_id: The issue_id of this AttachWikiDetail.
        :type issue_id: int
        """
        self._issue_id = issue_id

    @property
    def wiki_title(self):
        r"""Gets the wiki_title of this AttachWikiDetail.

        Wiki标题

        :return: The wiki_title of this AttachWikiDetail.
        :rtype: str
        """
        return self._wiki_title

    @wiki_title.setter
    def wiki_title(self, wiki_title):
        r"""Sets the wiki_title of this AttachWikiDetail.

        Wiki标题

        :param wiki_title: The wiki_title of this AttachWikiDetail.
        :type wiki_title: str
        """
        self._wiki_title = wiki_title

    @property
    def wiki_author(self):
        r"""Gets the wiki_author of this AttachWikiDetail.

        :return: The wiki_author of this AttachWikiDetail.
        :rtype: :class:`huaweicloudsdkprojectman.v4.SimpleUser`
        """
        return self._wiki_author

    @wiki_author.setter
    def wiki_author(self, wiki_author):
        r"""Sets the wiki_author of this AttachWikiDetail.

        :param wiki_author: The wiki_author of this AttachWikiDetail.
        :type wiki_author: :class:`huaweicloudsdkprojectman.v4.SimpleUser`
        """
        self._wiki_author = wiki_author

    @property
    def project(self):
        r"""Gets the project of this AttachWikiDetail.

        :return: The project of this AttachWikiDetail.
        :rtype: :class:`huaweicloudsdkprojectman.v4.SimpleProject`
        """
        return self._project

    @project.setter
    def project(self, project):
        r"""Sets the project of this AttachWikiDetail.

        :param project: The project of this AttachWikiDetail.
        :type project: :class:`huaweicloudsdkprojectman.v4.SimpleProject`
        """
        self._project = project

    @property
    def created_date(self):
        r"""Gets the created_date of this AttachWikiDetail.

        创建时间

        :return: The created_date of this AttachWikiDetail.
        :rtype: str
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        r"""Sets the created_date of this AttachWikiDetail.

        创建时间

        :param created_date: The created_date of this AttachWikiDetail.
        :type created_date: str
        """
        self._created_date = created_date

    @property
    def wiki_id(self):
        r"""Gets the wiki_id of this AttachWikiDetail.

        wiki ID

        :return: The wiki_id of this AttachWikiDetail.
        :rtype: str
        """
        return self._wiki_id

    @wiki_id.setter
    def wiki_id(self, wiki_id):
        r"""Sets the wiki_id of this AttachWikiDetail.

        wiki ID

        :param wiki_id: The wiki_id of this AttachWikiDetail.
        :type wiki_id: str
        """
        self._wiki_id = wiki_id

    @property
    def region(self):
        r"""Gets the region of this AttachWikiDetail.

        region值

        :return: The region of this AttachWikiDetail.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this AttachWikiDetail.

        region值

        :param region: The region of this AttachWikiDetail.
        :type region: str
        """
        self._region = region

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
        if not isinstance(other, AttachWikiDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
