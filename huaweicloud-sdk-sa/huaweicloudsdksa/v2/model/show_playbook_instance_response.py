# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowPlaybookInstanceResponse(SdkResponse):

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
        'end_time': 'str',
        'x_request_id': 'str'
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
        'end_time': 'end_time',
        'x_request_id': 'X-request-id'
    }

    def __init__(self, id=None, name=None, project_id=None, playbook=None, dataclass=None, dataobject=None, status=None, trigger_type=None, start_time=None, end_time=None, x_request_id=None):
        r"""ShowPlaybookInstanceResponse

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
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(ShowPlaybookInstanceResponse, self).__init__()

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
        self._x_request_id = None
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
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def id(self):
        r"""Gets the id of this ShowPlaybookInstanceResponse.

        Id value

        :return: The id of this ShowPlaybookInstanceResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ShowPlaybookInstanceResponse.

        Id value

        :param id: The id of this ShowPlaybookInstanceResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ShowPlaybookInstanceResponse.

        The name, display only

        :return: The name of this ShowPlaybookInstanceResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ShowPlaybookInstanceResponse.

        The name, display only

        :param name: The name of this ShowPlaybookInstanceResponse.
        :type name: str
        """
        self._name = name

    @property
    def project_id(self):
        r"""Gets the project_id of this ShowPlaybookInstanceResponse.

        Project id value

        :return: The project_id of this ShowPlaybookInstanceResponse.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ShowPlaybookInstanceResponse.

        Project id value

        :param project_id: The project_id of this ShowPlaybookInstanceResponse.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def playbook(self):
        r"""Gets the playbook of this ShowPlaybookInstanceResponse.

        :return: The playbook of this ShowPlaybookInstanceResponse.
        :rtype: :class:`huaweicloudsdksa.v2.PlaybookInfoRef`
        """
        return self._playbook

    @playbook.setter
    def playbook(self, playbook):
        r"""Sets the playbook of this ShowPlaybookInstanceResponse.

        :param playbook: The playbook of this ShowPlaybookInstanceResponse.
        :type playbook: :class:`huaweicloudsdksa.v2.PlaybookInfoRef`
        """
        self._playbook = playbook

    @property
    def dataclass(self):
        r"""Gets the dataclass of this ShowPlaybookInstanceResponse.

        :return: The dataclass of this ShowPlaybookInstanceResponse.
        :rtype: :class:`huaweicloudsdksa.v2.DataclassInfoRef`
        """
        return self._dataclass

    @dataclass.setter
    def dataclass(self, dataclass):
        r"""Sets the dataclass of this ShowPlaybookInstanceResponse.

        :param dataclass: The dataclass of this ShowPlaybookInstanceResponse.
        :type dataclass: :class:`huaweicloudsdksa.v2.DataclassInfoRef`
        """
        self._dataclass = dataclass

    @property
    def dataobject(self):
        r"""Gets the dataobject of this ShowPlaybookInstanceResponse.

        :return: The dataobject of this ShowPlaybookInstanceResponse.
        :rtype: :class:`huaweicloudsdksa.v2.DataclassInfoRef`
        """
        return self._dataobject

    @dataobject.setter
    def dataobject(self, dataobject):
        r"""Sets the dataobject of this ShowPlaybookInstanceResponse.

        :param dataobject: The dataobject of this ShowPlaybookInstanceResponse.
        :type dataobject: :class:`huaweicloudsdksa.v2.DataclassInfoRef`
        """
        self._dataobject = dataobject

    @property
    def status(self):
        r"""Gets the status of this ShowPlaybookInstanceResponse.

        Playbook instance status. RUNNING、FINISHED、FAILED、RETRYING、 TERMINATING、TERMINATED

        :return: The status of this ShowPlaybookInstanceResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ShowPlaybookInstanceResponse.

        Playbook instance status. RUNNING、FINISHED、FAILED、RETRYING、 TERMINATING、TERMINATED

        :param status: The status of this ShowPlaybookInstanceResponse.
        :type status: str
        """
        self._status = status

    @property
    def trigger_type(self):
        r"""Gets the trigger_type of this ShowPlaybookInstanceResponse.

        trigger type. DEBUG, TIMER, EVENT, MANUAL

        :return: The trigger_type of this ShowPlaybookInstanceResponse.
        :rtype: str
        """
        return self._trigger_type

    @trigger_type.setter
    def trigger_type(self, trigger_type):
        r"""Sets the trigger_type of this ShowPlaybookInstanceResponse.

        trigger type. DEBUG, TIMER, EVENT, MANUAL

        :param trigger_type: The trigger_type of this ShowPlaybookInstanceResponse.
        :type trigger_type: str
        """
        self._trigger_type = trigger_type

    @property
    def start_time(self):
        r"""Gets the start_time of this ShowPlaybookInstanceResponse.

        Create time

        :return: The start_time of this ShowPlaybookInstanceResponse.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ShowPlaybookInstanceResponse.

        Create time

        :param start_time: The start_time of this ShowPlaybookInstanceResponse.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ShowPlaybookInstanceResponse.

        Update time

        :return: The end_time of this ShowPlaybookInstanceResponse.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ShowPlaybookInstanceResponse.

        Update time

        :param end_time: The end_time of this ShowPlaybookInstanceResponse.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this ShowPlaybookInstanceResponse.

        :return: The x_request_id of this ShowPlaybookInstanceResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this ShowPlaybookInstanceResponse.

        :param x_request_id: The x_request_id of this ShowPlaybookInstanceResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

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
        if not isinstance(other, ShowPlaybookInstanceResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
