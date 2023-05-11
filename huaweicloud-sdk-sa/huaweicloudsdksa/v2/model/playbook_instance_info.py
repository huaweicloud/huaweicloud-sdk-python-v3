# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PlaybookInstanceInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'project_id': 'str',
        'playbook': 'PlaybookInfoRef',
        'dataclass': 'DataclassInfoRef',
        'dataobject': 'DataclassInfoRef',
        'status': 'str',
        'trigger_type': 'str',
        'start_time': 'str',
        'end_time': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'project_id': 'project_id',
        'playbook': 'playbook',
        'dataclass': 'dataclass',
        'dataobject': 'dataobject',
        'status': 'status',
        'trigger_type': 'trigger_type',
        'start_time': 'start_time',
        'end_time': 'end_time'
    }

    def __init__(self, id=None, name=None, project_id=None, playbook=None, dataclass=None, dataobject=None, status=None, trigger_type=None, start_time=None, end_time=None):
        """PlaybookInstanceInfo

        The model defined in huaweicloud sdk

        :param id: Id value
        :type id: str
        :param name: The name, display only
        :type name: str
        :param project_id: Project id value
        :type project_id: str
        :param playbook: 
        :type playbook: :class:`huaweicloudsdksa.v2.PlaybookInfoRef`
        :param dataclass: 
        :type dataclass: :class:`huaweicloudsdksa.v2.DataclassInfoRef`
        :param dataobject: 
        :type dataobject: :class:`huaweicloudsdksa.v2.DataclassInfoRef`
        :param status: Playbook instance status. RUNNING、FINISHED、FAILED、RETRYING、 TERMINATING、TERMINATED
        :type status: str
        :param trigger_type: trigger type. DEBUG, TIMER, EVENT, MANUAL
        :type trigger_type: str
        :param start_time: Create time
        :type start_time: str
        :param end_time: Update time
        :type end_time: str
        """
        
        

        self._id = None
        self._name = None
        self._project_id = None
        self._playbook = None
        self._dataclass = None
        self._dataobject = None
        self._status = None
        self._trigger_type = None
        self._start_time = None
        self._end_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if project_id is not None:
            self.project_id = project_id
        if playbook is not None:
            self.playbook = playbook
        if dataclass is not None:
            self.dataclass = dataclass
        if dataobject is not None:
            self.dataobject = dataobject
        if status is not None:
            self.status = status
        if trigger_type is not None:
            self.trigger_type = trigger_type
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time

    @property
    def id(self):
        """Gets the id of this PlaybookInstanceInfo.

        Id value

        :return: The id of this PlaybookInstanceInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PlaybookInstanceInfo.

        Id value

        :param id: The id of this PlaybookInstanceInfo.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this PlaybookInstanceInfo.

        The name, display only

        :return: The name of this PlaybookInstanceInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PlaybookInstanceInfo.

        The name, display only

        :param name: The name of this PlaybookInstanceInfo.
        :type name: str
        """
        self._name = name

    @property
    def project_id(self):
        """Gets the project_id of this PlaybookInstanceInfo.

        Project id value

        :return: The project_id of this PlaybookInstanceInfo.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this PlaybookInstanceInfo.

        Project id value

        :param project_id: The project_id of this PlaybookInstanceInfo.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def playbook(self):
        """Gets the playbook of this PlaybookInstanceInfo.

        :return: The playbook of this PlaybookInstanceInfo.
        :rtype: :class:`huaweicloudsdksa.v2.PlaybookInfoRef`
        """
        return self._playbook

    @playbook.setter
    def playbook(self, playbook):
        """Sets the playbook of this PlaybookInstanceInfo.

        :param playbook: The playbook of this PlaybookInstanceInfo.
        :type playbook: :class:`huaweicloudsdksa.v2.PlaybookInfoRef`
        """
        self._playbook = playbook

    @property
    def dataclass(self):
        """Gets the dataclass of this PlaybookInstanceInfo.

        :return: The dataclass of this PlaybookInstanceInfo.
        :rtype: :class:`huaweicloudsdksa.v2.DataclassInfoRef`
        """
        return self._dataclass

    @dataclass.setter
    def dataclass(self, dataclass):
        """Sets the dataclass of this PlaybookInstanceInfo.

        :param dataclass: The dataclass of this PlaybookInstanceInfo.
        :type dataclass: :class:`huaweicloudsdksa.v2.DataclassInfoRef`
        """
        self._dataclass = dataclass

    @property
    def dataobject(self):
        """Gets the dataobject of this PlaybookInstanceInfo.

        :return: The dataobject of this PlaybookInstanceInfo.
        :rtype: :class:`huaweicloudsdksa.v2.DataclassInfoRef`
        """
        return self._dataobject

    @dataobject.setter
    def dataobject(self, dataobject):
        """Sets the dataobject of this PlaybookInstanceInfo.

        :param dataobject: The dataobject of this PlaybookInstanceInfo.
        :type dataobject: :class:`huaweicloudsdksa.v2.DataclassInfoRef`
        """
        self._dataobject = dataobject

    @property
    def status(self):
        """Gets the status of this PlaybookInstanceInfo.

        Playbook instance status. RUNNING、FINISHED、FAILED、RETRYING、 TERMINATING、TERMINATED

        :return: The status of this PlaybookInstanceInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this PlaybookInstanceInfo.

        Playbook instance status. RUNNING、FINISHED、FAILED、RETRYING、 TERMINATING、TERMINATED

        :param status: The status of this PlaybookInstanceInfo.
        :type status: str
        """
        self._status = status

    @property
    def trigger_type(self):
        """Gets the trigger_type of this PlaybookInstanceInfo.

        trigger type. DEBUG, TIMER, EVENT, MANUAL

        :return: The trigger_type of this PlaybookInstanceInfo.
        :rtype: str
        """
        return self._trigger_type

    @trigger_type.setter
    def trigger_type(self, trigger_type):
        """Sets the trigger_type of this PlaybookInstanceInfo.

        trigger type. DEBUG, TIMER, EVENT, MANUAL

        :param trigger_type: The trigger_type of this PlaybookInstanceInfo.
        :type trigger_type: str
        """
        self._trigger_type = trigger_type

    @property
    def start_time(self):
        """Gets the start_time of this PlaybookInstanceInfo.

        Create time

        :return: The start_time of this PlaybookInstanceInfo.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this PlaybookInstanceInfo.

        Create time

        :param start_time: The start_time of this PlaybookInstanceInfo.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this PlaybookInstanceInfo.

        Update time

        :return: The end_time of this PlaybookInstanceInfo.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this PlaybookInstanceInfo.

        Update time

        :param end_time: The end_time of this PlaybookInstanceInfo.
        :type end_time: str
        """
        self._end_time = end_time

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
        if not isinstance(other, PlaybookInstanceInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
