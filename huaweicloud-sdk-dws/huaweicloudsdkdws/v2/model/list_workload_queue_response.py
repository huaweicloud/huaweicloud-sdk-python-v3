# coding: utf-8

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
        'queue_list': 'list[PlanStageQueue]',
        'workload_queue_name_list': 'list[str]',
        'workload_res_code': 'int'
    }

    attribute_map = {
        'queue_list': 'queue_list',
        'workload_queue_name_list': 'workload_queue_name_list',
        'workload_res_code': 'workload_res_code'
    }

    def __init__(self, queue_list=None, workload_queue_name_list=None, workload_res_code=None):
        r"""ListWorkloadQueueResponse

        The model defined in huaweicloud sdk

        :param queue_list: 资源池队列详情
        :type queue_list: list[:class:`huaweicloudsdkdws.v2.PlanStageQueue`]
        :param workload_queue_name_list: 资源池名称队列
        :type workload_queue_name_list: list[str]
        :param workload_res_code: 资源池队列查询返回码
        :type workload_res_code: int
        """
        
        super().__init__()

        self._queue_list = None
        self._workload_queue_name_list = None
        self._workload_res_code = None
        self.discriminator = None

        if queue_list is not None:
            self.queue_list = queue_list
        if workload_queue_name_list is not None:
            self.workload_queue_name_list = workload_queue_name_list
        if workload_res_code is not None:
            self.workload_res_code = workload_res_code

    @property
    def queue_list(self):
        r"""Gets the queue_list of this ListWorkloadQueueResponse.

        资源池队列详情

        :return: The queue_list of this ListWorkloadQueueResponse.
        :rtype: list[:class:`huaweicloudsdkdws.v2.PlanStageQueue`]
        """
        return self._queue_list

    @queue_list.setter
    def queue_list(self, queue_list):
        r"""Sets the queue_list of this ListWorkloadQueueResponse.

        资源池队列详情

        :param queue_list: The queue_list of this ListWorkloadQueueResponse.
        :type queue_list: list[:class:`huaweicloudsdkdws.v2.PlanStageQueue`]
        """
        self._queue_list = queue_list

    @property
    def workload_queue_name_list(self):
        r"""Gets the workload_queue_name_list of this ListWorkloadQueueResponse.

        资源池名称队列

        :return: The workload_queue_name_list of this ListWorkloadQueueResponse.
        :rtype: list[str]
        """
        return self._workload_queue_name_list

    @workload_queue_name_list.setter
    def workload_queue_name_list(self, workload_queue_name_list):
        r"""Sets the workload_queue_name_list of this ListWorkloadQueueResponse.

        资源池名称队列

        :param workload_queue_name_list: The workload_queue_name_list of this ListWorkloadQueueResponse.
        :type workload_queue_name_list: list[str]
        """
        self._workload_queue_name_list = workload_queue_name_list

    @property
    def workload_res_code(self):
        r"""Gets the workload_res_code of this ListWorkloadQueueResponse.

        资源池队列查询返回码

        :return: The workload_res_code of this ListWorkloadQueueResponse.
        :rtype: int
        """
        return self._workload_res_code

    @workload_res_code.setter
    def workload_res_code(self, workload_res_code):
        r"""Sets the workload_res_code of this ListWorkloadQueueResponse.

        资源池队列查询返回码

        :param workload_res_code: The workload_res_code of this ListWorkloadQueueResponse.
        :type workload_res_code: int
        """
        self._workload_res_code = workload_res_code

    def to_dict(self):
        import warnings
        warnings.warn("ListWorkloadQueueResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
        result = {}

        for attr, _ in self.openapi_types.items():
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
