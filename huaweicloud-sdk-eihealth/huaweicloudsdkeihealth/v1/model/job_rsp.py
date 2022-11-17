# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class JobRsp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'eihealth_project_name': 'str',
        'eihealth_project_id': 'str',
        'name': 'str',
        'id': 'str',
        'status': 'str',
        'finish_time': 'str',
        'failed_message': 'str',
        'failed_reason': 'str'
    }

    attribute_map = {
        'eihealth_project_name': 'eihealth_project_name',
        'eihealth_project_id': 'eihealth_project_id',
        'name': 'name',
        'id': 'id',
        'status': 'status',
        'finish_time': 'finish_time',
        'failed_message': 'failed_message',
        'failed_reason': 'failed_reason'
    }

    def __init__(self, eihealth_project_name=None, eihealth_project_id=None, name=None, id=None, status=None, finish_time=None, failed_message=None, failed_reason=None):
        """JobRsp

        The model defined in huaweicloud sdk

        :param eihealth_project_name: 项目名称
        :type eihealth_project_name: str
        :param eihealth_project_id: 项目id
        :type eihealth_project_id: str
        :param name: 作业名称
        :type name: str
        :param id: 作业id
        :type id: str
        :param status: 作业状态
        :type status: str
        :param finish_time: 作业结束时间
        :type finish_time: str
        :param failed_message: 作业失败提示
        :type failed_message: str
        :param failed_reason: 作业失败原因
        :type failed_reason: str
        """
        
        

        self._eihealth_project_name = None
        self._eihealth_project_id = None
        self._name = None
        self._id = None
        self._status = None
        self._finish_time = None
        self._failed_message = None
        self._failed_reason = None
        self.discriminator = None

        if eihealth_project_name is not None:
            self.eihealth_project_name = eihealth_project_name
        if eihealth_project_id is not None:
            self.eihealth_project_id = eihealth_project_id
        if name is not None:
            self.name = name
        if id is not None:
            self.id = id
        if status is not None:
            self.status = status
        if finish_time is not None:
            self.finish_time = finish_time
        if failed_message is not None:
            self.failed_message = failed_message
        if failed_reason is not None:
            self.failed_reason = failed_reason

    @property
    def eihealth_project_name(self):
        """Gets the eihealth_project_name of this JobRsp.

        项目名称

        :return: The eihealth_project_name of this JobRsp.
        :rtype: str
        """
        return self._eihealth_project_name

    @eihealth_project_name.setter
    def eihealth_project_name(self, eihealth_project_name):
        """Sets the eihealth_project_name of this JobRsp.

        项目名称

        :param eihealth_project_name: The eihealth_project_name of this JobRsp.
        :type eihealth_project_name: str
        """
        self._eihealth_project_name = eihealth_project_name

    @property
    def eihealth_project_id(self):
        """Gets the eihealth_project_id of this JobRsp.

        项目id

        :return: The eihealth_project_id of this JobRsp.
        :rtype: str
        """
        return self._eihealth_project_id

    @eihealth_project_id.setter
    def eihealth_project_id(self, eihealth_project_id):
        """Sets the eihealth_project_id of this JobRsp.

        项目id

        :param eihealth_project_id: The eihealth_project_id of this JobRsp.
        :type eihealth_project_id: str
        """
        self._eihealth_project_id = eihealth_project_id

    @property
    def name(self):
        """Gets the name of this JobRsp.

        作业名称

        :return: The name of this JobRsp.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this JobRsp.

        作业名称

        :param name: The name of this JobRsp.
        :type name: str
        """
        self._name = name

    @property
    def id(self):
        """Gets the id of this JobRsp.

        作业id

        :return: The id of this JobRsp.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this JobRsp.

        作业id

        :param id: The id of this JobRsp.
        :type id: str
        """
        self._id = id

    @property
    def status(self):
        """Gets the status of this JobRsp.

        作业状态

        :return: The status of this JobRsp.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this JobRsp.

        作业状态

        :param status: The status of this JobRsp.
        :type status: str
        """
        self._status = status

    @property
    def finish_time(self):
        """Gets the finish_time of this JobRsp.

        作业结束时间

        :return: The finish_time of this JobRsp.
        :rtype: str
        """
        return self._finish_time

    @finish_time.setter
    def finish_time(self, finish_time):
        """Sets the finish_time of this JobRsp.

        作业结束时间

        :param finish_time: The finish_time of this JobRsp.
        :type finish_time: str
        """
        self._finish_time = finish_time

    @property
    def failed_message(self):
        """Gets the failed_message of this JobRsp.

        作业失败提示

        :return: The failed_message of this JobRsp.
        :rtype: str
        """
        return self._failed_message

    @failed_message.setter
    def failed_message(self, failed_message):
        """Sets the failed_message of this JobRsp.

        作业失败提示

        :param failed_message: The failed_message of this JobRsp.
        :type failed_message: str
        """
        self._failed_message = failed_message

    @property
    def failed_reason(self):
        """Gets the failed_reason of this JobRsp.

        作业失败原因

        :return: The failed_reason of this JobRsp.
        :rtype: str
        """
        return self._failed_reason

    @failed_reason.setter
    def failed_reason(self, failed_reason):
        """Sets the failed_reason of this JobRsp.

        作业失败原因

        :param failed_reason: The failed_reason of this JobRsp.
        :type failed_reason: str
        """
        self._failed_reason = failed_reason

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
        if not isinstance(other, JobRsp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
