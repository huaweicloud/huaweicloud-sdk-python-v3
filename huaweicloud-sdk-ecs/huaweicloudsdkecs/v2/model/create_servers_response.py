# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class CreateServersResponse(SdkResponse):


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
        'order_id': 'str',
        'server_ids': 'list[str]'
    }

    attribute_map = {
        'job_id': 'job_id',
        'order_id': 'order_id',
        'server_ids': 'serverIds'
    }

    def __init__(self, job_id=None, order_id=None, server_ids=None):
        """CreateServersResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._job_id = None
        self._order_id = None
        self._server_ids = None
        self.discriminator = None

        if job_id is not None:
            self.job_id = job_id
        if order_id is not None:
            self.order_id = order_id
        if server_ids is not None:
            self.server_ids = server_ids

    @property
    def job_id(self):
        """Gets the job_id of this CreateServersResponse.

        提交任务成功后返回的任务ID，用户可以使用该ID对任务执行情况进行查询。

        :return: The job_id of this CreateServersResponse.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this CreateServersResponse.

        提交任务成功后返回的任务ID，用户可以使用该ID对任务执行情况进行查询。

        :param job_id: The job_id of this CreateServersResponse.
        :type: str
        """
        self._job_id = job_id

    @property
    def order_id(self):
        """Gets the order_id of this CreateServersResponse.

        订单号，创建包年包月的弹性云服务器时返回该参数。

        :return: The order_id of this CreateServersResponse.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this CreateServersResponse.

        订单号，创建包年包月的弹性云服务器时返回该参数。

        :param order_id: The order_id of this CreateServersResponse.
        :type: str
        """
        self._order_id = order_id

    @property
    def server_ids(self):
        """Gets the server_ids of this CreateServersResponse.

        云服务器ID列表。  通过云服务器ID查询云服务器详情 ，若返回404 可能云服务器还在创建或者已经创建失败。

        :return: The server_ids of this CreateServersResponse.
        :rtype: list[str]
        """
        return self._server_ids

    @server_ids.setter
    def server_ids(self, server_ids):
        """Sets the server_ids of this CreateServersResponse.

        云服务器ID列表。  通过云服务器ID查询云服务器详情 ，若返回404 可能云服务器还在创建或者已经创建失败。

        :param server_ids: The server_ids of this CreateServersResponse.
        :type: list[str]
        """
        self._server_ids = server_ids

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CreateServersResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
