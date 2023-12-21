# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateCbhResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_key': 'int',
        'slave_instance_key': 'int',
        'request_info': 'int',
        'job_id': 'int'
    }

    attribute_map = {
        'instance_key': 'instance_key',
        'slave_instance_key': 'slave_instance_key',
        'request_info': 'request_info',
        'job_id': 'job_id'
    }

    def __init__(self, instance_key=None, slave_instance_key=None, request_info=None, job_id=None):
        """CreateCbhResponse

        The model defined in huaweicloud sdk

        :param instance_key: 云堡垒机实例key。
        :type instance_key: int
        :param slave_instance_key: 云堡垒机备机实例key。（当前字段未启用，返回默认值null）
        :type slave_instance_key: int
        :param request_info: 返回创建云堡垒机实例信息。
        :type request_info: int
        :param job_id: job任务ID。（当前字段未启用，返回默认值null）
        :type job_id: int
        """
        
        super(CreateCbhResponse, self).__init__()

        self._instance_key = None
        self._slave_instance_key = None
        self._request_info = None
        self._job_id = None
        self.discriminator = None

        if instance_key is not None:
            self.instance_key = instance_key
        if slave_instance_key is not None:
            self.slave_instance_key = slave_instance_key
        if request_info is not None:
            self.request_info = request_info
        if job_id is not None:
            self.job_id = job_id

    @property
    def instance_key(self):
        """Gets the instance_key of this CreateCbhResponse.

        云堡垒机实例key。

        :return: The instance_key of this CreateCbhResponse.
        :rtype: int
        """
        return self._instance_key

    @instance_key.setter
    def instance_key(self, instance_key):
        """Sets the instance_key of this CreateCbhResponse.

        云堡垒机实例key。

        :param instance_key: The instance_key of this CreateCbhResponse.
        :type instance_key: int
        """
        self._instance_key = instance_key

    @property
    def slave_instance_key(self):
        """Gets the slave_instance_key of this CreateCbhResponse.

        云堡垒机备机实例key。（当前字段未启用，返回默认值null）

        :return: The slave_instance_key of this CreateCbhResponse.
        :rtype: int
        """
        return self._slave_instance_key

    @slave_instance_key.setter
    def slave_instance_key(self, slave_instance_key):
        """Sets the slave_instance_key of this CreateCbhResponse.

        云堡垒机备机实例key。（当前字段未启用，返回默认值null）

        :param slave_instance_key: The slave_instance_key of this CreateCbhResponse.
        :type slave_instance_key: int
        """
        self._slave_instance_key = slave_instance_key

    @property
    def request_info(self):
        """Gets the request_info of this CreateCbhResponse.

        返回创建云堡垒机实例信息。

        :return: The request_info of this CreateCbhResponse.
        :rtype: int
        """
        return self._request_info

    @request_info.setter
    def request_info(self, request_info):
        """Sets the request_info of this CreateCbhResponse.

        返回创建云堡垒机实例信息。

        :param request_info: The request_info of this CreateCbhResponse.
        :type request_info: int
        """
        self._request_info = request_info

    @property
    def job_id(self):
        """Gets the job_id of this CreateCbhResponse.

        job任务ID。（当前字段未启用，返回默认值null）

        :return: The job_id of this CreateCbhResponse.
        :rtype: int
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this CreateCbhResponse.

        job任务ID。（当前字段未启用，返回默认值null）

        :param job_id: The job_id of this CreateCbhResponse.
        :type job_id: int
        """
        self._job_id = job_id

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
        if not isinstance(other, CreateCbhResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
