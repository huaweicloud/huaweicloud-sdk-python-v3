# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MilestoneBasicDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'int',
        'iid': 'int',
        'repository_id': 'int',
        'title': 'str',
        'description': 'str',
        'state': 'str',
        'created_at': 'str',
        'updated_at': 'str',
        'due_date': 'str',
        'start_date': 'str',
        'repository_path': 'str',
        'web_url': 'str'
    }

    attribute_map = {
        'id': 'id',
        'iid': 'iid',
        'repository_id': 'repository_id',
        'title': 'title',
        'description': 'description',
        'state': 'state',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'due_date': 'due_date',
        'start_date': 'start_date',
        'repository_path': 'repository_path',
        'web_url': 'web_url'
    }

    def __init__(self, id=None, iid=None, repository_id=None, title=None, description=None, state=None, created_at=None, updated_at=None, due_date=None, start_date=None, repository_path=None, web_url=None):
        r"""MilestoneBasicDto

        The model defined in huaweicloud sdk

        :param id: 里程碑id
        :type id: int
        :param iid: 里程碑iid
        :type iid: int
        :param repository_id: 仓库id
        :type repository_id: int
        :param title: 里程碑标题
        :type title: str
        :param description: 里程碑描述
        :type description: str
        :param state: 状态
        :type state: str
        :param created_at: 创建时间
        :type created_at: str
        :param updated_at: 更新时间
        :type updated_at: str
        :param due_date: 到期时间
        :type due_date: str
        :param start_date: 开始时间
        :type start_date: str
        :param repository_path: 仓库路径
        :type repository_path: str
        :param web_url: 主页url
        :type web_url: str
        """
        
        

        self._id = None
        self._iid = None
        self._repository_id = None
        self._title = None
        self._description = None
        self._state = None
        self._created_at = None
        self._updated_at = None
        self._due_date = None
        self._start_date = None
        self._repository_path = None
        self._web_url = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if iid is not None:
            self.iid = iid
        if repository_id is not None:
            self.repository_id = repository_id
        if title is not None:
            self.title = title
        if description is not None:
            self.description = description
        if state is not None:
            self.state = state
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if due_date is not None:
            self.due_date = due_date
        if start_date is not None:
            self.start_date = start_date
        if repository_path is not None:
            self.repository_path = repository_path
        if web_url is not None:
            self.web_url = web_url

    @property
    def id(self):
        r"""Gets the id of this MilestoneBasicDto.

        里程碑id

        :return: The id of this MilestoneBasicDto.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this MilestoneBasicDto.

        里程碑id

        :param id: The id of this MilestoneBasicDto.
        :type id: int
        """
        self._id = id

    @property
    def iid(self):
        r"""Gets the iid of this MilestoneBasicDto.

        里程碑iid

        :return: The iid of this MilestoneBasicDto.
        :rtype: int
        """
        return self._iid

    @iid.setter
    def iid(self, iid):
        r"""Sets the iid of this MilestoneBasicDto.

        里程碑iid

        :param iid: The iid of this MilestoneBasicDto.
        :type iid: int
        """
        self._iid = iid

    @property
    def repository_id(self):
        r"""Gets the repository_id of this MilestoneBasicDto.

        仓库id

        :return: The repository_id of this MilestoneBasicDto.
        :rtype: int
        """
        return self._repository_id

    @repository_id.setter
    def repository_id(self, repository_id):
        r"""Sets the repository_id of this MilestoneBasicDto.

        仓库id

        :param repository_id: The repository_id of this MilestoneBasicDto.
        :type repository_id: int
        """
        self._repository_id = repository_id

    @property
    def title(self):
        r"""Gets the title of this MilestoneBasicDto.

        里程碑标题

        :return: The title of this MilestoneBasicDto.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        r"""Sets the title of this MilestoneBasicDto.

        里程碑标题

        :param title: The title of this MilestoneBasicDto.
        :type title: str
        """
        self._title = title

    @property
    def description(self):
        r"""Gets the description of this MilestoneBasicDto.

        里程碑描述

        :return: The description of this MilestoneBasicDto.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this MilestoneBasicDto.

        里程碑描述

        :param description: The description of this MilestoneBasicDto.
        :type description: str
        """
        self._description = description

    @property
    def state(self):
        r"""Gets the state of this MilestoneBasicDto.

        状态

        :return: The state of this MilestoneBasicDto.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this MilestoneBasicDto.

        状态

        :param state: The state of this MilestoneBasicDto.
        :type state: str
        """
        self._state = state

    @property
    def created_at(self):
        r"""Gets the created_at of this MilestoneBasicDto.

        创建时间

        :return: The created_at of this MilestoneBasicDto.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this MilestoneBasicDto.

        创建时间

        :param created_at: The created_at of this MilestoneBasicDto.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this MilestoneBasicDto.

        更新时间

        :return: The updated_at of this MilestoneBasicDto.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this MilestoneBasicDto.

        更新时间

        :param updated_at: The updated_at of this MilestoneBasicDto.
        :type updated_at: str
        """
        self._updated_at = updated_at

    @property
    def due_date(self):
        r"""Gets the due_date of this MilestoneBasicDto.

        到期时间

        :return: The due_date of this MilestoneBasicDto.
        :rtype: str
        """
        return self._due_date

    @due_date.setter
    def due_date(self, due_date):
        r"""Sets the due_date of this MilestoneBasicDto.

        到期时间

        :param due_date: The due_date of this MilestoneBasicDto.
        :type due_date: str
        """
        self._due_date = due_date

    @property
    def start_date(self):
        r"""Gets the start_date of this MilestoneBasicDto.

        开始时间

        :return: The start_date of this MilestoneBasicDto.
        :rtype: str
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        r"""Sets the start_date of this MilestoneBasicDto.

        开始时间

        :param start_date: The start_date of this MilestoneBasicDto.
        :type start_date: str
        """
        self._start_date = start_date

    @property
    def repository_path(self):
        r"""Gets the repository_path of this MilestoneBasicDto.

        仓库路径

        :return: The repository_path of this MilestoneBasicDto.
        :rtype: str
        """
        return self._repository_path

    @repository_path.setter
    def repository_path(self, repository_path):
        r"""Sets the repository_path of this MilestoneBasicDto.

        仓库路径

        :param repository_path: The repository_path of this MilestoneBasicDto.
        :type repository_path: str
        """
        self._repository_path = repository_path

    @property
    def web_url(self):
        r"""Gets the web_url of this MilestoneBasicDto.

        主页url

        :return: The web_url of this MilestoneBasicDto.
        :rtype: str
        """
        return self._web_url

    @web_url.setter
    def web_url(self, web_url):
        r"""Sets the web_url of this MilestoneBasicDto.

        主页url

        :param web_url: The web_url of this MilestoneBasicDto.
        :type web_url: str
        """
        self._web_url = web_url

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
        if not isinstance(other, MilestoneBasicDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
