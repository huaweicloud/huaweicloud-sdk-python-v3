# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListWorkloadQueueResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'workload_queue_name_list': 'list[str]',
        'workload_res_code': 'int',
        'workload_res_str': 'str'
    }

    attribute_map = {
        'workload_queue_name_list': 'workload_queue_name_list',
        'workload_res_code': 'workload_res_code',
        'workload_res_str': 'workload_res_str'
    }

    def __init__(self, workload_queue_name_list=None, workload_res_code=None, workload_res_str=None):
        """ListWorkloadQueueResponse

        The model defined in huaweicloud sdk

        :param workload_queue_name_list: 工作负载队列名称。
        :type workload_queue_name_list: list[str]
        :param workload_res_code: 结果状态码。
        :type workload_res_code: int
        :param workload_res_str: 结果描述。
        :type workload_res_str: str
        """
        
        super(ListWorkloadQueueResponse, self).__init__()

        self._workload_queue_name_list = None
        self._workload_res_code = None
        self._workload_res_str = None
        self.discriminator = None

        if workload_queue_name_list is not None:
            self.workload_queue_name_list = workload_queue_name_list
        if workload_res_code is not None:
            self.workload_res_code = workload_res_code
        if workload_res_str is not None:
            self.workload_res_str = workload_res_str

    @property
    def workload_queue_name_list(self):
        """Gets the workload_queue_name_list of this ListWorkloadQueueResponse.

        工作负载队列名称。

        :return: The workload_queue_name_list of this ListWorkloadQueueResponse.
        :rtype: list[str]
        """
        return self._workload_queue_name_list

    @workload_queue_name_list.setter
    def workload_queue_name_list(self, workload_queue_name_list):
        """Sets the workload_queue_name_list of this ListWorkloadQueueResponse.

        工作负载队列名称。

        :param workload_queue_name_list: The workload_queue_name_list of this ListWorkloadQueueResponse.
        :type workload_queue_name_list: list[str]
        """
        self._workload_queue_name_list = workload_queue_name_list

    @property
    def workload_res_code(self):
        """Gets the workload_res_code of this ListWorkloadQueueResponse.

        结果状态码。

        :return: The workload_res_code of this ListWorkloadQueueResponse.
        :rtype: int
        """
        return self._workload_res_code

    @workload_res_code.setter
    def workload_res_code(self, workload_res_code):
        """Sets the workload_res_code of this ListWorkloadQueueResponse.

        结果状态码。

        :param workload_res_code: The workload_res_code of this ListWorkloadQueueResponse.
        :type workload_res_code: int
        """
        self._workload_res_code = workload_res_code

    @property
    def workload_res_str(self):
        """Gets the workload_res_str of this ListWorkloadQueueResponse.

        结果描述。

        :return: The workload_res_str of this ListWorkloadQueueResponse.
        :rtype: str
        """
        return self._workload_res_str

    @workload_res_str.setter
    def workload_res_str(self, workload_res_str):
        """Sets the workload_res_str of this ListWorkloadQueueResponse.

        结果描述。

        :param workload_res_str: The workload_res_str of this ListWorkloadQueueResponse.
        :type workload_res_str: str
        """
        self._workload_res_str = workload_res_str

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
        if not isinstance(other, ListWorkloadQueueResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
