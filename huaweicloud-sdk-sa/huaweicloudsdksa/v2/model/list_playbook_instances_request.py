# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPlaybookInstancesRequest:

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
        'workspace_id': 'str',
        'status': 'str',
        'date_type': 'str',
        'name': 'str',
        'playbook_name': 'str',
        'dataclass_name': 'str',
        'dataobject_name': 'str',
        'trigger_type': 'str',
        'from_date': 'str',
        'to_date': 'str',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'project_id': 'project_id',
        'workspace_id': 'workspace_id',
        'status': 'status',
        'date_type': 'date_type',
        'name': 'name',
        'playbook_name': 'playbook_name',
        'dataclass_name': 'dataclass_name',
        'dataobject_name': 'dataobject_name',
        'trigger_type': 'trigger_type',
        'from_date': 'from_date',
        'to_date': 'to_date',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, project_id=None, workspace_id=None, status=None, date_type=None, name=None, playbook_name=None, dataclass_name=None, dataobject_name=None, trigger_type=None, from_date=None, to_date=None, limit=None, offset=None):
        """ListPlaybookInstancesRequest

        The model defined in huaweicloud sdk

        :param project_id: ID of project
        :type project_id: str
        :param workspace_id: ID of workspace
        :type workspace_id: str
        :param status: Playbook instance status. RUNNING、FINISHED、FAILED、RETRYING、 TERMINATING、TERMINATED
        :type status: str
        :param date_type: date type, START END
        :type date_type: str
        :param name: name
        :type name: str
        :param playbook_name: Playbook name.
        :type playbook_name: str
        :param dataclass_name: Dataclass name.
        :type dataclass_name: str
        :param dataobject_name: Dataobject name.
        :type dataobject_name: str
        :param trigger_type: trigger type. DEBUG, TIMER, EVENT, MANUAL
        :type trigger_type: str
        :param from_date: 起始时间
        :type from_date: str
        :param to_date: 结束时间
        :type to_date: str
        :param limit: request limit size
        :type limit: int
        :param offset: request offset, from 0
        :type offset: int
        """
        
        

        self._project_id = None
        self._workspace_id = None
        self._status = None
        self._date_type = None
        self._name = None
        self._playbook_name = None
        self._dataclass_name = None
        self._dataobject_name = None
        self._trigger_type = None
        self._from_date = None
        self._to_date = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        self.project_id = project_id
        self.workspace_id = workspace_id
        if status is not None:
            self.status = status
        if date_type is not None:
            self.date_type = date_type
        if name is not None:
            self.name = name
        if playbook_name is not None:
            self.playbook_name = playbook_name
        if dataclass_name is not None:
            self.dataclass_name = dataclass_name
        if dataobject_name is not None:
            self.dataobject_name = dataobject_name
        if trigger_type is not None:
            self.trigger_type = trigger_type
        if from_date is not None:
            self.from_date = from_date
        if to_date is not None:
            self.to_date = to_date
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def project_id(self):
        """Gets the project_id of this ListPlaybookInstancesRequest.

        ID of project

        :return: The project_id of this ListPlaybookInstancesRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this ListPlaybookInstancesRequest.

        ID of project

        :param project_id: The project_id of this ListPlaybookInstancesRequest.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def workspace_id(self):
        """Gets the workspace_id of this ListPlaybookInstancesRequest.

        ID of workspace

        :return: The workspace_id of this ListPlaybookInstancesRequest.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        """Sets the workspace_id of this ListPlaybookInstancesRequest.

        ID of workspace

        :param workspace_id: The workspace_id of this ListPlaybookInstancesRequest.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def status(self):
        """Gets the status of this ListPlaybookInstancesRequest.

        Playbook instance status. RUNNING、FINISHED、FAILED、RETRYING、 TERMINATING、TERMINATED

        :return: The status of this ListPlaybookInstancesRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListPlaybookInstancesRequest.

        Playbook instance status. RUNNING、FINISHED、FAILED、RETRYING、 TERMINATING、TERMINATED

        :param status: The status of this ListPlaybookInstancesRequest.
        :type status: str
        """
        self._status = status

    @property
    def date_type(self):
        """Gets the date_type of this ListPlaybookInstancesRequest.

        date type, START END

        :return: The date_type of this ListPlaybookInstancesRequest.
        :rtype: str
        """
        return self._date_type

    @date_type.setter
    def date_type(self, date_type):
        """Sets the date_type of this ListPlaybookInstancesRequest.

        date type, START END

        :param date_type: The date_type of this ListPlaybookInstancesRequest.
        :type date_type: str
        """
        self._date_type = date_type

    @property
    def name(self):
        """Gets the name of this ListPlaybookInstancesRequest.

        name

        :return: The name of this ListPlaybookInstancesRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListPlaybookInstancesRequest.

        name

        :param name: The name of this ListPlaybookInstancesRequest.
        :type name: str
        """
        self._name = name

    @property
    def playbook_name(self):
        """Gets the playbook_name of this ListPlaybookInstancesRequest.

        Playbook name.

        :return: The playbook_name of this ListPlaybookInstancesRequest.
        :rtype: str
        """
        return self._playbook_name

    @playbook_name.setter
    def playbook_name(self, playbook_name):
        """Sets the playbook_name of this ListPlaybookInstancesRequest.

        Playbook name.

        :param playbook_name: The playbook_name of this ListPlaybookInstancesRequest.
        :type playbook_name: str
        """
        self._playbook_name = playbook_name

    @property
    def dataclass_name(self):
        """Gets the dataclass_name of this ListPlaybookInstancesRequest.

        Dataclass name.

        :return: The dataclass_name of this ListPlaybookInstancesRequest.
        :rtype: str
        """
        return self._dataclass_name

    @dataclass_name.setter
    def dataclass_name(self, dataclass_name):
        """Sets the dataclass_name of this ListPlaybookInstancesRequest.

        Dataclass name.

        :param dataclass_name: The dataclass_name of this ListPlaybookInstancesRequest.
        :type dataclass_name: str
        """
        self._dataclass_name = dataclass_name

    @property
    def dataobject_name(self):
        """Gets the dataobject_name of this ListPlaybookInstancesRequest.

        Dataobject name.

        :return: The dataobject_name of this ListPlaybookInstancesRequest.
        :rtype: str
        """
        return self._dataobject_name

    @dataobject_name.setter
    def dataobject_name(self, dataobject_name):
        """Sets the dataobject_name of this ListPlaybookInstancesRequest.

        Dataobject name.

        :param dataobject_name: The dataobject_name of this ListPlaybookInstancesRequest.
        :type dataobject_name: str
        """
        self._dataobject_name = dataobject_name

    @property
    def trigger_type(self):
        """Gets the trigger_type of this ListPlaybookInstancesRequest.

        trigger type. DEBUG, TIMER, EVENT, MANUAL

        :return: The trigger_type of this ListPlaybookInstancesRequest.
        :rtype: str
        """
        return self._trigger_type

    @trigger_type.setter
    def trigger_type(self, trigger_type):
        """Sets the trigger_type of this ListPlaybookInstancesRequest.

        trigger type. DEBUG, TIMER, EVENT, MANUAL

        :param trigger_type: The trigger_type of this ListPlaybookInstancesRequest.
        :type trigger_type: str
        """
        self._trigger_type = trigger_type

    @property
    def from_date(self):
        """Gets the from_date of this ListPlaybookInstancesRequest.

        起始时间

        :return: The from_date of this ListPlaybookInstancesRequest.
        :rtype: str
        """
        return self._from_date

    @from_date.setter
    def from_date(self, from_date):
        """Sets the from_date of this ListPlaybookInstancesRequest.

        起始时间

        :param from_date: The from_date of this ListPlaybookInstancesRequest.
        :type from_date: str
        """
        self._from_date = from_date

    @property
    def to_date(self):
        """Gets the to_date of this ListPlaybookInstancesRequest.

        结束时间

        :return: The to_date of this ListPlaybookInstancesRequest.
        :rtype: str
        """
        return self._to_date

    @to_date.setter
    def to_date(self, to_date):
        """Sets the to_date of this ListPlaybookInstancesRequest.

        结束时间

        :param to_date: The to_date of this ListPlaybookInstancesRequest.
        :type to_date: str
        """
        self._to_date = to_date

    @property
    def limit(self):
        """Gets the limit of this ListPlaybookInstancesRequest.

        request limit size

        :return: The limit of this ListPlaybookInstancesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListPlaybookInstancesRequest.

        request limit size

        :param limit: The limit of this ListPlaybookInstancesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListPlaybookInstancesRequest.

        request offset, from 0

        :return: The offset of this ListPlaybookInstancesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListPlaybookInstancesRequest.

        request offset, from 0

        :param offset: The offset of this ListPlaybookInstancesRequest.
        :type offset: int
        """
        self._offset = offset

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
        if not isinstance(other, ListPlaybookInstancesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
