# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowInstanceStatusResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'task_id': 'str',
        'task_status': 'str',
        'pipeline_id': 'str',
        'pipeline_name': 'str',
        'pipeline_url': 'str'
    }

    attribute_map = {
        'task_id': 'task_id',
        'task_status': 'task_status',
        'pipeline_id': 'pipeline_id',
        'pipeline_name': 'pipeline_name',
        'pipeline_url': 'pipeline_url'
    }

    def __init__(self, task_id=None, task_status=None, pipeline_id=None, pipeline_name=None, pipeline_url=None):
        """ShowInstanceStatusResponse

        The model defined in huaweicloud sdk

        :param task_id: 实例ID
        :type task_id: str
        :param task_status: 实例创建状态，取值和含义:initializing：初始化中；processing：处理中；finished：已完成；succeeded：成功
        :type task_status: str
        :param pipeline_id: 流水线ID
        :type pipeline_id: str
        :param pipeline_name: 流水线名字
        :type pipeline_name: str
        :param pipeline_url: 流水线详情页面url
        :type pipeline_url: str
        """
        
        super(ShowInstanceStatusResponse, self).__init__()

        self._task_id = None
        self._task_status = None
        self._pipeline_id = None
        self._pipeline_name = None
        self._pipeline_url = None
        self.discriminator = None

        if task_id is not None:
            self.task_id = task_id
        if task_status is not None:
            self.task_status = task_status
        if pipeline_id is not None:
            self.pipeline_id = pipeline_id
        if pipeline_name is not None:
            self.pipeline_name = pipeline_name
        if pipeline_url is not None:
            self.pipeline_url = pipeline_url

    @property
    def task_id(self):
        """Gets the task_id of this ShowInstanceStatusResponse.

        实例ID

        :return: The task_id of this ShowInstanceStatusResponse.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """Sets the task_id of this ShowInstanceStatusResponse.

        实例ID

        :param task_id: The task_id of this ShowInstanceStatusResponse.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def task_status(self):
        """Gets the task_status of this ShowInstanceStatusResponse.

        实例创建状态，取值和含义:initializing：初始化中；processing：处理中；finished：已完成；succeeded：成功

        :return: The task_status of this ShowInstanceStatusResponse.
        :rtype: str
        """
        return self._task_status

    @task_status.setter
    def task_status(self, task_status):
        """Sets the task_status of this ShowInstanceStatusResponse.

        实例创建状态，取值和含义:initializing：初始化中；processing：处理中；finished：已完成；succeeded：成功

        :param task_status: The task_status of this ShowInstanceStatusResponse.
        :type task_status: str
        """
        self._task_status = task_status

    @property
    def pipeline_id(self):
        """Gets the pipeline_id of this ShowInstanceStatusResponse.

        流水线ID

        :return: The pipeline_id of this ShowInstanceStatusResponse.
        :rtype: str
        """
        return self._pipeline_id

    @pipeline_id.setter
    def pipeline_id(self, pipeline_id):
        """Sets the pipeline_id of this ShowInstanceStatusResponse.

        流水线ID

        :param pipeline_id: The pipeline_id of this ShowInstanceStatusResponse.
        :type pipeline_id: str
        """
        self._pipeline_id = pipeline_id

    @property
    def pipeline_name(self):
        """Gets the pipeline_name of this ShowInstanceStatusResponse.

        流水线名字

        :return: The pipeline_name of this ShowInstanceStatusResponse.
        :rtype: str
        """
        return self._pipeline_name

    @pipeline_name.setter
    def pipeline_name(self, pipeline_name):
        """Sets the pipeline_name of this ShowInstanceStatusResponse.

        流水线名字

        :param pipeline_name: The pipeline_name of this ShowInstanceStatusResponse.
        :type pipeline_name: str
        """
        self._pipeline_name = pipeline_name

    @property
    def pipeline_url(self):
        """Gets the pipeline_url of this ShowInstanceStatusResponse.

        流水线详情页面url

        :return: The pipeline_url of this ShowInstanceStatusResponse.
        :rtype: str
        """
        return self._pipeline_url

    @pipeline_url.setter
    def pipeline_url(self, pipeline_url):
        """Sets the pipeline_url of this ShowInstanceStatusResponse.

        流水线详情页面url

        :param pipeline_url: The pipeline_url of this ShowInstanceStatusResponse.
        :type pipeline_url: str
        """
        self._pipeline_url = pipeline_url

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
        if not isinstance(other, ShowInstanceStatusResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
