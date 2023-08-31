# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SupplementDataResp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'end_date': 'float',
        'job_list': 'list[str]',
        'name': 'str',
        'parallel': 'int',
        'start_date': 'float',
        'status': 'str',
        'submitted_date': 'float',
        'supplement_data_instance_time': 'object',
        'supplement_data_run_time': 'object',
        'type': 'int',
        'user_name': 'str'
    }

    attribute_map = {
        'end_date': 'endDate',
        'job_list': 'jobList',
        'name': 'name',
        'parallel': 'parallel',
        'start_date': 'startDate',
        'status': 'status',
        'submitted_date': 'submittedDate',
        'supplement_data_instance_time': 'supplement_data_instance_time',
        'supplement_data_run_time': 'supplement_data_run_time',
        'type': 'type',
        'user_name': 'userName'
    }

    def __init__(self, end_date=None, job_list=None, name=None, parallel=None, start_date=None, status=None, submitted_date=None, supplement_data_instance_time=None, supplement_data_run_time=None, type=None, user_name=None):
        """SupplementDataResp

        The model defined in huaweicloud sdk

        :param end_date: 
        :type end_date: float
        :param job_list: 
        :type job_list: list[str]
        :param name: 
        :type name: str
        :param parallel: 
        :type parallel: int
        :param start_date: 
        :type start_date: float
        :param status: 
        :type status: str
        :param submitted_date: 
        :type submitted_date: float
        :param supplement_data_instance_time: 
        :type supplement_data_instance_time: object
        :param supplement_data_run_time: 
        :type supplement_data_run_time: object
        :param type: 
        :type type: int
        :param user_name: 
        :type user_name: str
        """
        
        

        self._end_date = None
        self._job_list = None
        self._name = None
        self._parallel = None
        self._start_date = None
        self._status = None
        self._submitted_date = None
        self._supplement_data_instance_time = None
        self._supplement_data_run_time = None
        self._type = None
        self._user_name = None
        self.discriminator = None

        if end_date is not None:
            self.end_date = end_date
        if job_list is not None:
            self.job_list = job_list
        if name is not None:
            self.name = name
        if parallel is not None:
            self.parallel = parallel
        if start_date is not None:
            self.start_date = start_date
        if status is not None:
            self.status = status
        if submitted_date is not None:
            self.submitted_date = submitted_date
        if supplement_data_instance_time is not None:
            self.supplement_data_instance_time = supplement_data_instance_time
        if supplement_data_run_time is not None:
            self.supplement_data_run_time = supplement_data_run_time
        if type is not None:
            self.type = type
        if user_name is not None:
            self.user_name = user_name

    @property
    def end_date(self):
        """Gets the end_date of this SupplementDataResp.

        :return: The end_date of this SupplementDataResp.
        :rtype: float
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this SupplementDataResp.

        :param end_date: The end_date of this SupplementDataResp.
        :type end_date: float
        """
        self._end_date = end_date

    @property
    def job_list(self):
        """Gets the job_list of this SupplementDataResp.

        :return: The job_list of this SupplementDataResp.
        :rtype: list[str]
        """
        return self._job_list

    @job_list.setter
    def job_list(self, job_list):
        """Sets the job_list of this SupplementDataResp.

        :param job_list: The job_list of this SupplementDataResp.
        :type job_list: list[str]
        """
        self._job_list = job_list

    @property
    def name(self):
        """Gets the name of this SupplementDataResp.

        :return: The name of this SupplementDataResp.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SupplementDataResp.

        :param name: The name of this SupplementDataResp.
        :type name: str
        """
        self._name = name

    @property
    def parallel(self):
        """Gets the parallel of this SupplementDataResp.

        :return: The parallel of this SupplementDataResp.
        :rtype: int
        """
        return self._parallel

    @parallel.setter
    def parallel(self, parallel):
        """Sets the parallel of this SupplementDataResp.

        :param parallel: The parallel of this SupplementDataResp.
        :type parallel: int
        """
        self._parallel = parallel

    @property
    def start_date(self):
        """Gets the start_date of this SupplementDataResp.

        :return: The start_date of this SupplementDataResp.
        :rtype: float
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this SupplementDataResp.

        :param start_date: The start_date of this SupplementDataResp.
        :type start_date: float
        """
        self._start_date = start_date

    @property
    def status(self):
        """Gets the status of this SupplementDataResp.

        :return: The status of this SupplementDataResp.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this SupplementDataResp.

        :param status: The status of this SupplementDataResp.
        :type status: str
        """
        self._status = status

    @property
    def submitted_date(self):
        """Gets the submitted_date of this SupplementDataResp.

        :return: The submitted_date of this SupplementDataResp.
        :rtype: float
        """
        return self._submitted_date

    @submitted_date.setter
    def submitted_date(self, submitted_date):
        """Sets the submitted_date of this SupplementDataResp.

        :param submitted_date: The submitted_date of this SupplementDataResp.
        :type submitted_date: float
        """
        self._submitted_date = submitted_date

    @property
    def supplement_data_instance_time(self):
        """Gets the supplement_data_instance_time of this SupplementDataResp.

        :return: The supplement_data_instance_time of this SupplementDataResp.
        :rtype: object
        """
        return self._supplement_data_instance_time

    @supplement_data_instance_time.setter
    def supplement_data_instance_time(self, supplement_data_instance_time):
        """Sets the supplement_data_instance_time of this SupplementDataResp.

        :param supplement_data_instance_time: The supplement_data_instance_time of this SupplementDataResp.
        :type supplement_data_instance_time: object
        """
        self._supplement_data_instance_time = supplement_data_instance_time

    @property
    def supplement_data_run_time(self):
        """Gets the supplement_data_run_time of this SupplementDataResp.

        :return: The supplement_data_run_time of this SupplementDataResp.
        :rtype: object
        """
        return self._supplement_data_run_time

    @supplement_data_run_time.setter
    def supplement_data_run_time(self, supplement_data_run_time):
        """Sets the supplement_data_run_time of this SupplementDataResp.

        :param supplement_data_run_time: The supplement_data_run_time of this SupplementDataResp.
        :type supplement_data_run_time: object
        """
        self._supplement_data_run_time = supplement_data_run_time

    @property
    def type(self):
        """Gets the type of this SupplementDataResp.

        :return: The type of this SupplementDataResp.
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SupplementDataResp.

        :param type: The type of this SupplementDataResp.
        :type type: int
        """
        self._type = type

    @property
    def user_name(self):
        """Gets the user_name of this SupplementDataResp.

        :return: The user_name of this SupplementDataResp.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this SupplementDataResp.

        :param user_name: The user_name of this SupplementDataResp.
        :type user_name: str
        """
        self._user_name = user_name

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
        if not isinstance(other, SupplementDataResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other