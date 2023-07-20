# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CopyJobResponse(SdkResponse):

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
        'status': 'str',
        'create_time': 'str',
        'is_clone_job': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'status': 'status',
        'create_time': 'create_time',
        'is_clone_job': 'is_clone_job'
    }

    def __init__(self, id=None, name=None, status=None, create_time=None, is_clone_job=None):
        """CopyJobResponse

        The model defined in huaweicloud sdk

        :param id: 任务ID。
        :type id: str
        :param name: 任务名称。
        :type name: str
        :param status: 任务状态。
        :type status: str
        :param create_time: 任务创建时间。
        :type create_time: str
        :param is_clone_job: 是否为克隆任务。
        :type is_clone_job: str
        """
        
        super(CopyJobResponse, self).__init__()

        self._id = None
        self._name = None
        self._status = None
        self._create_time = None
        self._is_clone_job = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if status is not None:
            self.status = status
        if create_time is not None:
            self.create_time = create_time
        if is_clone_job is not None:
            self.is_clone_job = is_clone_job

    @property
    def id(self):
        """Gets the id of this CopyJobResponse.

        任务ID。

        :return: The id of this CopyJobResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CopyJobResponse.

        任务ID。

        :param id: The id of this CopyJobResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this CopyJobResponse.

        任务名称。

        :return: The name of this CopyJobResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CopyJobResponse.

        任务名称。

        :param name: The name of this CopyJobResponse.
        :type name: str
        """
        self._name = name

    @property
    def status(self):
        """Gets the status of this CopyJobResponse.

        任务状态。

        :return: The status of this CopyJobResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CopyJobResponse.

        任务状态。

        :param status: The status of this CopyJobResponse.
        :type status: str
        """
        self._status = status

    @property
    def create_time(self):
        """Gets the create_time of this CopyJobResponse.

        任务创建时间。

        :return: The create_time of this CopyJobResponse.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this CopyJobResponse.

        任务创建时间。

        :param create_time: The create_time of this CopyJobResponse.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def is_clone_job(self):
        """Gets the is_clone_job of this CopyJobResponse.

        是否为克隆任务。

        :return: The is_clone_job of this CopyJobResponse.
        :rtype: str
        """
        return self._is_clone_job

    @is_clone_job.setter
    def is_clone_job(self, is_clone_job):
        """Sets the is_clone_job of this CopyJobResponse.

        是否为克隆任务。

        :param is_clone_job: The is_clone_job of this CopyJobResponse.
        :type is_clone_job: str
        """
        self._is_clone_job = is_clone_job

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
        if not isinstance(other, CopyJobResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
