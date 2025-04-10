# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SubscribeCloudServiceResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'code': 'int',
        'message': 'str',
        'order_ids': 'list[str]',
        'job_ids': 'list[str]',
        'job_id': 'str',
        'product_name': 'str'
    }

    attribute_map = {
        'code': 'code',
        'message': 'message',
        'order_ids': 'order_ids',
        'job_ids': 'job_ids',
        'job_id': 'job_id',
        'product_name': 'product_name'
    }

    def __init__(self, code=None, message=None, order_ids=None, job_ids=None, job_id=None, product_name=None):
        r"""SubscribeCloudServiceResponse

        The model defined in huaweicloud sdk

        :param code: 响应状态码
        :type code: int
        :param message: 响应信息
        :type message: str
        :param order_ids: 包年/包月订单ID,按需场景为空。
        :type order_ids: list[str]
        :param job_ids: jobIds,包年/包月场景为空。
        :type job_ids: list[str]
        :param job_id: jobId,包年/包月场景为空。
        :type job_id: str
        :param product_name: 产品名称
        :type product_name: str
        """
        
        super(SubscribeCloudServiceResponse, self).__init__()

        self._code = None
        self._message = None
        self._order_ids = None
        self._job_ids = None
        self._job_id = None
        self._product_name = None
        self.discriminator = None

        if code is not None:
            self.code = code
        if message is not None:
            self.message = message
        if order_ids is not None:
            self.order_ids = order_ids
        if job_ids is not None:
            self.job_ids = job_ids
        if job_id is not None:
            self.job_id = job_id
        if product_name is not None:
            self.product_name = product_name

    @property
    def code(self):
        r"""Gets the code of this SubscribeCloudServiceResponse.

        响应状态码

        :return: The code of this SubscribeCloudServiceResponse.
        :rtype: int
        """
        return self._code

    @code.setter
    def code(self, code):
        r"""Sets the code of this SubscribeCloudServiceResponse.

        响应状态码

        :param code: The code of this SubscribeCloudServiceResponse.
        :type code: int
        """
        self._code = code

    @property
    def message(self):
        r"""Gets the message of this SubscribeCloudServiceResponse.

        响应信息

        :return: The message of this SubscribeCloudServiceResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this SubscribeCloudServiceResponse.

        响应信息

        :param message: The message of this SubscribeCloudServiceResponse.
        :type message: str
        """
        self._message = message

    @property
    def order_ids(self):
        r"""Gets the order_ids of this SubscribeCloudServiceResponse.

        包年/包月订单ID,按需场景为空。

        :return: The order_ids of this SubscribeCloudServiceResponse.
        :rtype: list[str]
        """
        return self._order_ids

    @order_ids.setter
    def order_ids(self, order_ids):
        r"""Sets the order_ids of this SubscribeCloudServiceResponse.

        包年/包月订单ID,按需场景为空。

        :param order_ids: The order_ids of this SubscribeCloudServiceResponse.
        :type order_ids: list[str]
        """
        self._order_ids = order_ids

    @property
    def job_ids(self):
        r"""Gets the job_ids of this SubscribeCloudServiceResponse.

        jobIds,包年/包月场景为空。

        :return: The job_ids of this SubscribeCloudServiceResponse.
        :rtype: list[str]
        """
        return self._job_ids

    @job_ids.setter
    def job_ids(self, job_ids):
        r"""Sets the job_ids of this SubscribeCloudServiceResponse.

        jobIds,包年/包月场景为空。

        :param job_ids: The job_ids of this SubscribeCloudServiceResponse.
        :type job_ids: list[str]
        """
        self._job_ids = job_ids

    @property
    def job_id(self):
        r"""Gets the job_id of this SubscribeCloudServiceResponse.

        jobId,包年/包月场景为空。

        :return: The job_id of this SubscribeCloudServiceResponse.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this SubscribeCloudServiceResponse.

        jobId,包年/包月场景为空。

        :param job_id: The job_id of this SubscribeCloudServiceResponse.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def product_name(self):
        r"""Gets the product_name of this SubscribeCloudServiceResponse.

        产品名称

        :return: The product_name of this SubscribeCloudServiceResponse.
        :rtype: str
        """
        return self._product_name

    @product_name.setter
    def product_name(self, product_name):
        r"""Sets the product_name of this SubscribeCloudServiceResponse.

        产品名称

        :param product_name: The product_name of this SubscribeCloudServiceResponse.
        :type product_name: str
        """
        self._product_name = product_name

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
        if not isinstance(other, SubscribeCloudServiceResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
