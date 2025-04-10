# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateElasticResourcePoolResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'is_success': 'bool',
        'message': 'str',
        'elastic_resource_pool_name': 'str'
    }

    attribute_map = {
        'is_success': 'is_success',
        'message': 'message',
        'elastic_resource_pool_name': 'elastic_resource_pool_name'
    }

    def __init__(self, is_success=None, message=None, elastic_resource_pool_name=None):
        r"""CreateElasticResourcePoolResponse

        The model defined in huaweicloud sdk

        :param is_success: 是否成功
        :type is_success: bool
        :param message: 响应消息
        :type message: str
        :param elastic_resource_pool_name: 创建成功的弹性资源池名称
        :type elastic_resource_pool_name: str
        """
        
        super(CreateElasticResourcePoolResponse, self).__init__()

        self._is_success = None
        self._message = None
        self._elastic_resource_pool_name = None
        self.discriminator = None

        if is_success is not None:
            self.is_success = is_success
        if message is not None:
            self.message = message
        if elastic_resource_pool_name is not None:
            self.elastic_resource_pool_name = elastic_resource_pool_name

    @property
    def is_success(self):
        r"""Gets the is_success of this CreateElasticResourcePoolResponse.

        是否成功

        :return: The is_success of this CreateElasticResourcePoolResponse.
        :rtype: bool
        """
        return self._is_success

    @is_success.setter
    def is_success(self, is_success):
        r"""Sets the is_success of this CreateElasticResourcePoolResponse.

        是否成功

        :param is_success: The is_success of this CreateElasticResourcePoolResponse.
        :type is_success: bool
        """
        self._is_success = is_success

    @property
    def message(self):
        r"""Gets the message of this CreateElasticResourcePoolResponse.

        响应消息

        :return: The message of this CreateElasticResourcePoolResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this CreateElasticResourcePoolResponse.

        响应消息

        :param message: The message of this CreateElasticResourcePoolResponse.
        :type message: str
        """
        self._message = message

    @property
    def elastic_resource_pool_name(self):
        r"""Gets the elastic_resource_pool_name of this CreateElasticResourcePoolResponse.

        创建成功的弹性资源池名称

        :return: The elastic_resource_pool_name of this CreateElasticResourcePoolResponse.
        :rtype: str
        """
        return self._elastic_resource_pool_name

    @elastic_resource_pool_name.setter
    def elastic_resource_pool_name(self, elastic_resource_pool_name):
        r"""Sets the elastic_resource_pool_name of this CreateElasticResourcePoolResponse.

        创建成功的弹性资源池名称

        :param elastic_resource_pool_name: The elastic_resource_pool_name of this CreateElasticResourcePoolResponse.
        :type elastic_resource_pool_name: str
        """
        self._elastic_resource_pool_name = elastic_resource_pool_name

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
        if not isinstance(other, CreateElasticResourcePoolResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
