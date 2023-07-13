# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowJobDetailResponse(SdkResponse):

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
        'job_status': 'object',
        'job_result': 'str',
        'show_type': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'job_status': 'job_status',
        'job_result': 'job_result',
        'show_type': 'show_type'
    }

    def __init__(self, id=None, name=None, job_status=None, job_result=None, show_type=None):
        """ShowJobDetailResponse

        The model defined in huaweicloud sdk

        :param id: 任务的id。
        :type id: str
        :param name: 任务的名称。
        :type name: str
        :param job_status: 任务的状态。
        :type job_status: object
        :param job_result: 任务结果信息。
        :type job_result: str
        :param show_type: 任务显示类型，页面显示使用字段
        :type show_type: str
        """
        
        super(ShowJobDetailResponse, self).__init__()

        self._id = None
        self._name = None
        self._job_status = None
        self._job_result = None
        self._show_type = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if job_status is not None:
            self.job_status = job_status
        if job_result is not None:
            self.job_result = job_result
        if show_type is not None:
            self.show_type = show_type

    @property
    def id(self):
        """Gets the id of this ShowJobDetailResponse.

        任务的id。

        :return: The id of this ShowJobDetailResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ShowJobDetailResponse.

        任务的id。

        :param id: The id of this ShowJobDetailResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ShowJobDetailResponse.

        任务的名称。

        :return: The name of this ShowJobDetailResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ShowJobDetailResponse.

        任务的名称。

        :param name: The name of this ShowJobDetailResponse.
        :type name: str
        """
        self._name = name

    @property
    def job_status(self):
        """Gets the job_status of this ShowJobDetailResponse.

        任务的状态。

        :return: The job_status of this ShowJobDetailResponse.
        :rtype: object
        """
        return self._job_status

    @job_status.setter
    def job_status(self, job_status):
        """Sets the job_status of this ShowJobDetailResponse.

        任务的状态。

        :param job_status: The job_status of this ShowJobDetailResponse.
        :type job_status: object
        """
        self._job_status = job_status

    @property
    def job_result(self):
        """Gets the job_result of this ShowJobDetailResponse.

        任务结果信息。

        :return: The job_result of this ShowJobDetailResponse.
        :rtype: str
        """
        return self._job_result

    @job_result.setter
    def job_result(self, job_result):
        """Sets the job_result of this ShowJobDetailResponse.

        任务结果信息。

        :param job_result: The job_result of this ShowJobDetailResponse.
        :type job_result: str
        """
        self._job_result = job_result

    @property
    def show_type(self):
        """Gets the show_type of this ShowJobDetailResponse.

        任务显示类型，页面显示使用字段

        :return: The show_type of this ShowJobDetailResponse.
        :rtype: str
        """
        return self._show_type

    @show_type.setter
    def show_type(self, show_type):
        """Sets the show_type of this ShowJobDetailResponse.

        任务显示类型，页面显示使用字段

        :param show_type: The show_type of this ShowJobDetailResponse.
        :type show_type: str
        """
        self._show_type = show_type

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
        if not isinstance(other, ShowJobDetailResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
