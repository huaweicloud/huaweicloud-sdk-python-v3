# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RecyclingJob:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'job_id': 'str',
        'job_name': 'str',
        'project_id': 'str',
        'creator_name': 'str',
        'creator_id': 'str',
        'create_time': 'str',
        'delete_time': 'str',
        'create_time_stamp': 'str',
        'delete_time_stamp': 'str'
    }

    attribute_map = {
        'job_id': 'job_id',
        'job_name': 'job_name',
        'project_id': 'project_id',
        'creator_name': 'creator_name',
        'creator_id': 'creator_id',
        'create_time': 'create_time',
        'delete_time': 'delete_time',
        'create_time_stamp': 'create_time_stamp',
        'delete_time_stamp': 'delete_time_stamp'
    }

    def __init__(self, job_id=None, job_name=None, project_id=None, creator_name=None, creator_id=None, create_time=None, delete_time=None, create_time_stamp=None, delete_time_stamp=None):
        r"""RecyclingJob

        The model defined in huaweicloud sdk

        :param job_id: 任务ID
        :type job_id: str
        :param job_name: 任务名称
        :type job_name: str
        :param project_id: CodeArts项目ID
        :type project_id: str
        :param creator_name: 创建人
        :type creator_name: str
        :param creator_id: 创建人ID
        :type creator_id: str
        :param create_time: 创建时间
        :type create_time: str
        :param delete_time: 删除时间
        :type delete_time: str
        :param create_time_stamp: 创建时间戳
        :type create_time_stamp: str
        :param delete_time_stamp: 删除时间戳
        :type delete_time_stamp: str
        """
        
        

        self._job_id = None
        self._job_name = None
        self._project_id = None
        self._creator_name = None
        self._creator_id = None
        self._create_time = None
        self._delete_time = None
        self._create_time_stamp = None
        self._delete_time_stamp = None
        self.discriminator = None

        if job_id is not None:
            self.job_id = job_id
        if job_name is not None:
            self.job_name = job_name
        if project_id is not None:
            self.project_id = project_id
        if creator_name is not None:
            self.creator_name = creator_name
        if creator_id is not None:
            self.creator_id = creator_id
        if create_time is not None:
            self.create_time = create_time
        if delete_time is not None:
            self.delete_time = delete_time
        if create_time_stamp is not None:
            self.create_time_stamp = create_time_stamp
        if delete_time_stamp is not None:
            self.delete_time_stamp = delete_time_stamp

    @property
    def job_id(self):
        r"""Gets the job_id of this RecyclingJob.

        任务ID

        :return: The job_id of this RecyclingJob.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this RecyclingJob.

        任务ID

        :param job_id: The job_id of this RecyclingJob.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def job_name(self):
        r"""Gets the job_name of this RecyclingJob.

        任务名称

        :return: The job_name of this RecyclingJob.
        :rtype: str
        """
        return self._job_name

    @job_name.setter
    def job_name(self, job_name):
        r"""Sets the job_name of this RecyclingJob.

        任务名称

        :param job_name: The job_name of this RecyclingJob.
        :type job_name: str
        """
        self._job_name = job_name

    @property
    def project_id(self):
        r"""Gets the project_id of this RecyclingJob.

        CodeArts项目ID

        :return: The project_id of this RecyclingJob.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this RecyclingJob.

        CodeArts项目ID

        :param project_id: The project_id of this RecyclingJob.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def creator_name(self):
        r"""Gets the creator_name of this RecyclingJob.

        创建人

        :return: The creator_name of this RecyclingJob.
        :rtype: str
        """
        return self._creator_name

    @creator_name.setter
    def creator_name(self, creator_name):
        r"""Sets the creator_name of this RecyclingJob.

        创建人

        :param creator_name: The creator_name of this RecyclingJob.
        :type creator_name: str
        """
        self._creator_name = creator_name

    @property
    def creator_id(self):
        r"""Gets the creator_id of this RecyclingJob.

        创建人ID

        :return: The creator_id of this RecyclingJob.
        :rtype: str
        """
        return self._creator_id

    @creator_id.setter
    def creator_id(self, creator_id):
        r"""Sets the creator_id of this RecyclingJob.

        创建人ID

        :param creator_id: The creator_id of this RecyclingJob.
        :type creator_id: str
        """
        self._creator_id = creator_id

    @property
    def create_time(self):
        r"""Gets the create_time of this RecyclingJob.

        创建时间

        :return: The create_time of this RecyclingJob.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this RecyclingJob.

        创建时间

        :param create_time: The create_time of this RecyclingJob.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def delete_time(self):
        r"""Gets the delete_time of this RecyclingJob.

        删除时间

        :return: The delete_time of this RecyclingJob.
        :rtype: str
        """
        return self._delete_time

    @delete_time.setter
    def delete_time(self, delete_time):
        r"""Sets the delete_time of this RecyclingJob.

        删除时间

        :param delete_time: The delete_time of this RecyclingJob.
        :type delete_time: str
        """
        self._delete_time = delete_time

    @property
    def create_time_stamp(self):
        r"""Gets the create_time_stamp of this RecyclingJob.

        创建时间戳

        :return: The create_time_stamp of this RecyclingJob.
        :rtype: str
        """
        return self._create_time_stamp

    @create_time_stamp.setter
    def create_time_stamp(self, create_time_stamp):
        r"""Sets the create_time_stamp of this RecyclingJob.

        创建时间戳

        :param create_time_stamp: The create_time_stamp of this RecyclingJob.
        :type create_time_stamp: str
        """
        self._create_time_stamp = create_time_stamp

    @property
    def delete_time_stamp(self):
        r"""Gets the delete_time_stamp of this RecyclingJob.

        删除时间戳

        :return: The delete_time_stamp of this RecyclingJob.
        :rtype: str
        """
        return self._delete_time_stamp

    @delete_time_stamp.setter
    def delete_time_stamp(self, delete_time_stamp):
        r"""Sets the delete_time_stamp of this RecyclingJob.

        删除时间戳

        :param delete_time_stamp: The delete_time_stamp of this RecyclingJob.
        :type delete_time_stamp: str
        """
        self._delete_time_stamp = delete_time_stamp

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
        if not isinstance(other, RecyclingJob):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
