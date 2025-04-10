# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateConsumerGroupOrBatchDeleteConsumerGroupResponse(SdkResponse):

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
        'name': 'str'
    }

    attribute_map = {
        'job_id': 'job_id',
        'name': 'name'
    }

    def __init__(self, job_id=None, name=None):
        r"""CreateConsumerGroupOrBatchDeleteConsumerGroupResponse

        The model defined in huaweicloud sdk

        :param job_id: 删除消费组的任务ID
        :type job_id: str
        :param name: 创建成功的消费组名称。
        :type name: str
        """
        
        super(CreateConsumerGroupOrBatchDeleteConsumerGroupResponse, self).__init__()

        self._job_id = None
        self._name = None
        self.discriminator = None

        if job_id is not None:
            self.job_id = job_id
        if name is not None:
            self.name = name

    @property
    def job_id(self):
        r"""Gets the job_id of this CreateConsumerGroupOrBatchDeleteConsumerGroupResponse.

        删除消费组的任务ID

        :return: The job_id of this CreateConsumerGroupOrBatchDeleteConsumerGroupResponse.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this CreateConsumerGroupOrBatchDeleteConsumerGroupResponse.

        删除消费组的任务ID

        :param job_id: The job_id of this CreateConsumerGroupOrBatchDeleteConsumerGroupResponse.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def name(self):
        r"""Gets the name of this CreateConsumerGroupOrBatchDeleteConsumerGroupResponse.

        创建成功的消费组名称。

        :return: The name of this CreateConsumerGroupOrBatchDeleteConsumerGroupResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateConsumerGroupOrBatchDeleteConsumerGroupResponse.

        创建成功的消费组名称。

        :param name: The name of this CreateConsumerGroupOrBatchDeleteConsumerGroupResponse.
        :type name: str
        """
        self._name = name

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
        if not isinstance(other, CreateConsumerGroupOrBatchDeleteConsumerGroupResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
