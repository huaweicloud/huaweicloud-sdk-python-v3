# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ComponentRecordView:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'begin_time': 'str',
        'end_time': 'str',
        'description': 'object',
        'instance_id': 'str',
        'version': 'str',
        'current_used': 'bool',
        'status': 'str',
        'deploy_type': 'str',
        'jobs': 'list[RecordJob]'
    }

    attribute_map = {
        'begin_time': 'begin_time',
        'end_time': 'end_time',
        'description': 'description',
        'instance_id': 'instance_id',
        'version': 'version',
        'current_used': 'current_used',
        'status': 'status',
        'deploy_type': 'deploy_type',
        'jobs': 'jobs'
    }

    def __init__(self, begin_time=None, end_time=None, description=None, instance_id=None, version=None, current_used=None, status=None, deploy_type=None, jobs=None):
        """ComponentRecordView

        The model defined in huaweicloud sdk

        :param begin_time: 
        :type begin_time: str
        :param end_time: 
        :type end_time: str
        :param description: 
        :type description: object
        :param instance_id: 
        :type instance_id: str
        :param version: 
        :type version: str
        :param current_used: 
        :type current_used: bool
        :param status: 
        :type status: str
        :param deploy_type: 
        :type deploy_type: str
        :param jobs: 
        :type jobs: list[:class:`huaweicloudsdkservicestage.v3.RecordJob`]
        """
        
        

        self._begin_time = None
        self._end_time = None
        self._description = None
        self._instance_id = None
        self._version = None
        self._current_used = None
        self._status = None
        self._deploy_type = None
        self._jobs = None
        self.discriminator = None

        if begin_time is not None:
            self.begin_time = begin_time
        if end_time is not None:
            self.end_time = end_time
        if description is not None:
            self.description = description
        if instance_id is not None:
            self.instance_id = instance_id
        if version is not None:
            self.version = version
        if current_used is not None:
            self.current_used = current_used
        if status is not None:
            self.status = status
        if deploy_type is not None:
            self.deploy_type = deploy_type
        if jobs is not None:
            self.jobs = jobs

    @property
    def begin_time(self):
        """Gets the begin_time of this ComponentRecordView.

        :return: The begin_time of this ComponentRecordView.
        :rtype: str
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        """Sets the begin_time of this ComponentRecordView.

        :param begin_time: The begin_time of this ComponentRecordView.
        :type begin_time: str
        """
        self._begin_time = begin_time

    @property
    def end_time(self):
        """Gets the end_time of this ComponentRecordView.

        :return: The end_time of this ComponentRecordView.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ComponentRecordView.

        :param end_time: The end_time of this ComponentRecordView.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def description(self):
        """Gets the description of this ComponentRecordView.

        :return: The description of this ComponentRecordView.
        :rtype: object
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ComponentRecordView.

        :param description: The description of this ComponentRecordView.
        :type description: object
        """
        self._description = description

    @property
    def instance_id(self):
        """Gets the instance_id of this ComponentRecordView.

        :return: The instance_id of this ComponentRecordView.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ComponentRecordView.

        :param instance_id: The instance_id of this ComponentRecordView.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def version(self):
        """Gets the version of this ComponentRecordView.

        :return: The version of this ComponentRecordView.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ComponentRecordView.

        :param version: The version of this ComponentRecordView.
        :type version: str
        """
        self._version = version

    @property
    def current_used(self):
        """Gets the current_used of this ComponentRecordView.

        :return: The current_used of this ComponentRecordView.
        :rtype: bool
        """
        return self._current_used

    @current_used.setter
    def current_used(self, current_used):
        """Sets the current_used of this ComponentRecordView.

        :param current_used: The current_used of this ComponentRecordView.
        :type current_used: bool
        """
        self._current_used = current_used

    @property
    def status(self):
        """Gets the status of this ComponentRecordView.

        :return: The status of this ComponentRecordView.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ComponentRecordView.

        :param status: The status of this ComponentRecordView.
        :type status: str
        """
        self._status = status

    @property
    def deploy_type(self):
        """Gets the deploy_type of this ComponentRecordView.

        :return: The deploy_type of this ComponentRecordView.
        :rtype: str
        """
        return self._deploy_type

    @deploy_type.setter
    def deploy_type(self, deploy_type):
        """Sets the deploy_type of this ComponentRecordView.

        :param deploy_type: The deploy_type of this ComponentRecordView.
        :type deploy_type: str
        """
        self._deploy_type = deploy_type

    @property
    def jobs(self):
        """Gets the jobs of this ComponentRecordView.

        :return: The jobs of this ComponentRecordView.
        :rtype: list[:class:`huaweicloudsdkservicestage.v3.RecordJob`]
        """
        return self._jobs

    @jobs.setter
    def jobs(self, jobs):
        """Sets the jobs of this ComponentRecordView.

        :param jobs: The jobs of this ComponentRecordView.
        :type jobs: list[:class:`huaweicloudsdkservicestage.v3.RecordJob`]
        """
        self._jobs = jobs

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
        if not isinstance(other, ComponentRecordView):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
