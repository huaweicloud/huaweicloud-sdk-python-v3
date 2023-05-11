# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RepoHook:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'build_events': 'bool',
        'created_at': 'datetime',
        'enable_ssl_verification': 'bool',
        'id': 'int',
        'issues_events': 'bool',
        'merge_requests_events': 'bool',
        'note_events': 'bool',
        'pipeline_events': 'bool',
        'project_id': 'int',
        'push_events': 'bool',
        'repository_update_events': 'bool',
        'tag_push_events': 'bool',
        'wiki_page_events': 'bool'
    }

    attribute_map = {
        'build_events': 'build_events',
        'created_at': 'created_at',
        'enable_ssl_verification': 'enable_ssl_verification',
        'id': 'id',
        'issues_events': 'issues_events',
        'merge_requests_events': 'merge_requests_events',
        'note_events': 'note_events',
        'pipeline_events': 'pipeline_events',
        'project_id': 'project_id',
        'push_events': 'push_events',
        'repository_update_events': 'repository_update_events',
        'tag_push_events': 'tag_push_events',
        'wiki_page_events': 'wiki_page_events'
    }

    def __init__(self, build_events=None, created_at=None, enable_ssl_verification=None, id=None, issues_events=None, merge_requests_events=None, note_events=None, pipeline_events=None, project_id=None, push_events=None, repository_update_events=None, tag_push_events=None, wiki_page_events=None):
        """RepoHook

        The model defined in huaweicloud sdk

        :param build_events: 是否触发build_events事件
        :type build_events: bool
        :param created_at: 仓库统计创建的时间
        :type created_at: datetime
        :param enable_ssl_verification: 是否使用ssl验证
        :type enable_ssl_verification: bool
        :param id: hook id
        :type id: int
        :param issues_events: 是否触发issues_events事件
        :type issues_events: bool
        :param merge_requests_events: 是否触发merge_requests_events事件
        :type merge_requests_events: bool
        :param note_events: 是否触发note_events事件
        :type note_events: bool
        :param pipeline_events: 是否触发pipeline_events事件
        :type pipeline_events: bool
        :param project_id: 仓库id
        :type project_id: int
        :param push_events: 是否触发push_events事件
        :type push_events: bool
        :param repository_update_events: 是否触发repository_update_events事件
        :type repository_update_events: bool
        :param tag_push_events: 是否触发tag_push_events事件
        :type tag_push_events: bool
        :param wiki_page_events: 是否触发wiki_page_events事件
        :type wiki_page_events: bool
        """
        
        

        self._build_events = None
        self._created_at = None
        self._enable_ssl_verification = None
        self._id = None
        self._issues_events = None
        self._merge_requests_events = None
        self._note_events = None
        self._pipeline_events = None
        self._project_id = None
        self._push_events = None
        self._repository_update_events = None
        self._tag_push_events = None
        self._wiki_page_events = None
        self.discriminator = None

        if build_events is not None:
            self.build_events = build_events
        if created_at is not None:
            self.created_at = created_at
        if enable_ssl_verification is not None:
            self.enable_ssl_verification = enable_ssl_verification
        if id is not None:
            self.id = id
        if issues_events is not None:
            self.issues_events = issues_events
        if merge_requests_events is not None:
            self.merge_requests_events = merge_requests_events
        if note_events is not None:
            self.note_events = note_events
        if pipeline_events is not None:
            self.pipeline_events = pipeline_events
        if project_id is not None:
            self.project_id = project_id
        if push_events is not None:
            self.push_events = push_events
        if repository_update_events is not None:
            self.repository_update_events = repository_update_events
        if tag_push_events is not None:
            self.tag_push_events = tag_push_events
        if wiki_page_events is not None:
            self.wiki_page_events = wiki_page_events

    @property
    def build_events(self):
        """Gets the build_events of this RepoHook.

        是否触发build_events事件

        :return: The build_events of this RepoHook.
        :rtype: bool
        """
        return self._build_events

    @build_events.setter
    def build_events(self, build_events):
        """Sets the build_events of this RepoHook.

        是否触发build_events事件

        :param build_events: The build_events of this RepoHook.
        :type build_events: bool
        """
        self._build_events = build_events

    @property
    def created_at(self):
        """Gets the created_at of this RepoHook.

        仓库统计创建的时间

        :return: The created_at of this RepoHook.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this RepoHook.

        仓库统计创建的时间

        :param created_at: The created_at of this RepoHook.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def enable_ssl_verification(self):
        """Gets the enable_ssl_verification of this RepoHook.

        是否使用ssl验证

        :return: The enable_ssl_verification of this RepoHook.
        :rtype: bool
        """
        return self._enable_ssl_verification

    @enable_ssl_verification.setter
    def enable_ssl_verification(self, enable_ssl_verification):
        """Sets the enable_ssl_verification of this RepoHook.

        是否使用ssl验证

        :param enable_ssl_verification: The enable_ssl_verification of this RepoHook.
        :type enable_ssl_verification: bool
        """
        self._enable_ssl_verification = enable_ssl_verification

    @property
    def id(self):
        """Gets the id of this RepoHook.

        hook id

        :return: The id of this RepoHook.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this RepoHook.

        hook id

        :param id: The id of this RepoHook.
        :type id: int
        """
        self._id = id

    @property
    def issues_events(self):
        """Gets the issues_events of this RepoHook.

        是否触发issues_events事件

        :return: The issues_events of this RepoHook.
        :rtype: bool
        """
        return self._issues_events

    @issues_events.setter
    def issues_events(self, issues_events):
        """Sets the issues_events of this RepoHook.

        是否触发issues_events事件

        :param issues_events: The issues_events of this RepoHook.
        :type issues_events: bool
        """
        self._issues_events = issues_events

    @property
    def merge_requests_events(self):
        """Gets the merge_requests_events of this RepoHook.

        是否触发merge_requests_events事件

        :return: The merge_requests_events of this RepoHook.
        :rtype: bool
        """
        return self._merge_requests_events

    @merge_requests_events.setter
    def merge_requests_events(self, merge_requests_events):
        """Sets the merge_requests_events of this RepoHook.

        是否触发merge_requests_events事件

        :param merge_requests_events: The merge_requests_events of this RepoHook.
        :type merge_requests_events: bool
        """
        self._merge_requests_events = merge_requests_events

    @property
    def note_events(self):
        """Gets the note_events of this RepoHook.

        是否触发note_events事件

        :return: The note_events of this RepoHook.
        :rtype: bool
        """
        return self._note_events

    @note_events.setter
    def note_events(self, note_events):
        """Sets the note_events of this RepoHook.

        是否触发note_events事件

        :param note_events: The note_events of this RepoHook.
        :type note_events: bool
        """
        self._note_events = note_events

    @property
    def pipeline_events(self):
        """Gets the pipeline_events of this RepoHook.

        是否触发pipeline_events事件

        :return: The pipeline_events of this RepoHook.
        :rtype: bool
        """
        return self._pipeline_events

    @pipeline_events.setter
    def pipeline_events(self, pipeline_events):
        """Sets the pipeline_events of this RepoHook.

        是否触发pipeline_events事件

        :param pipeline_events: The pipeline_events of this RepoHook.
        :type pipeline_events: bool
        """
        self._pipeline_events = pipeline_events

    @property
    def project_id(self):
        """Gets the project_id of this RepoHook.

        仓库id

        :return: The project_id of this RepoHook.
        :rtype: int
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this RepoHook.

        仓库id

        :param project_id: The project_id of this RepoHook.
        :type project_id: int
        """
        self._project_id = project_id

    @property
    def push_events(self):
        """Gets the push_events of this RepoHook.

        是否触发push_events事件

        :return: The push_events of this RepoHook.
        :rtype: bool
        """
        return self._push_events

    @push_events.setter
    def push_events(self, push_events):
        """Sets the push_events of this RepoHook.

        是否触发push_events事件

        :param push_events: The push_events of this RepoHook.
        :type push_events: bool
        """
        self._push_events = push_events

    @property
    def repository_update_events(self):
        """Gets the repository_update_events of this RepoHook.

        是否触发repository_update_events事件

        :return: The repository_update_events of this RepoHook.
        :rtype: bool
        """
        return self._repository_update_events

    @repository_update_events.setter
    def repository_update_events(self, repository_update_events):
        """Sets the repository_update_events of this RepoHook.

        是否触发repository_update_events事件

        :param repository_update_events: The repository_update_events of this RepoHook.
        :type repository_update_events: bool
        """
        self._repository_update_events = repository_update_events

    @property
    def tag_push_events(self):
        """Gets the tag_push_events of this RepoHook.

        是否触发tag_push_events事件

        :return: The tag_push_events of this RepoHook.
        :rtype: bool
        """
        return self._tag_push_events

    @tag_push_events.setter
    def tag_push_events(self, tag_push_events):
        """Sets the tag_push_events of this RepoHook.

        是否触发tag_push_events事件

        :param tag_push_events: The tag_push_events of this RepoHook.
        :type tag_push_events: bool
        """
        self._tag_push_events = tag_push_events

    @property
    def wiki_page_events(self):
        """Gets the wiki_page_events of this RepoHook.

        是否触发wiki_page_events事件

        :return: The wiki_page_events of this RepoHook.
        :rtype: bool
        """
        return self._wiki_page_events

    @wiki_page_events.setter
    def wiki_page_events(self, wiki_page_events):
        """Sets the wiki_page_events of this RepoHook.

        是否触发wiki_page_events事件

        :param wiki_page_events: The wiki_page_events of this RepoHook.
        :type wiki_page_events: bool
        """
        self._wiki_page_events = wiki_page_events

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
        if not isinstance(other, RepoHook):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
