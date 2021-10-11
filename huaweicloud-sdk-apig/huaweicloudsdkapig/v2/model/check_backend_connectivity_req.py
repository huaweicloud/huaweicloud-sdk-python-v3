# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CheckBackendConnectivityReq:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'backend_type': 'str',
        'backend_address': 'str',
        'vpc_channel_id': 'str'
    }

    attribute_map = {
        'backend_type': 'backend_type',
        'backend_address': 'backend_address',
        'vpc_channel_id': 'vpc_channel_id'
    }

    def __init__(self, backend_type=None, backend_address=None, vpc_channel_id=None):
        """CheckBackendConnectivityReq - a model defined in huaweicloud sdk"""
        
        

        self._backend_type = None
        self._backend_address = None
        self._vpc_channel_id = None
        self.discriminator = None

        self.backend_type = backend_type
        if backend_address is not None:
            self.backend_address = backend_address
        if vpc_channel_id is not None:
            self.vpc_channel_id = vpc_channel_id

    @property
    def backend_type(self):
        """Gets the backend_type of this CheckBackendConnectivityReq.

        后端服务配置方式 backend_address - 配置后端服务地址（不使用负载通道）  vpc_channel - 使用负载通道

        :return: The backend_type of this CheckBackendConnectivityReq.
        :rtype: str
        """
        return self._backend_type

    @backend_type.setter
    def backend_type(self, backend_type):
        """Sets the backend_type of this CheckBackendConnectivityReq.

        后端服务配置方式 backend_address - 配置后端服务地址（不使用负载通道）  vpc_channel - 使用负载通道

        :param backend_type: The backend_type of this CheckBackendConnectivityReq.
        :type: str
        """
        self._backend_type = backend_type

    @property
    def backend_address(self):
        """Gets the backend_address of this CheckBackendConnectivityReq.

        后端服务地址，当type为backend_address时必填

        :return: The backend_address of this CheckBackendConnectivityReq.
        :rtype: str
        """
        return self._backend_address

    @backend_address.setter
    def backend_address(self, backend_address):
        """Sets the backend_address of this CheckBackendConnectivityReq.

        后端服务地址，当type为backend_address时必填

        :param backend_address: The backend_address of this CheckBackendConnectivityReq.
        :type: str
        """
        self._backend_address = backend_address

    @property
    def vpc_channel_id(self):
        """Gets the vpc_channel_id of this CheckBackendConnectivityReq.

        负载通道编号，当type为vpc_channel时必填

        :return: The vpc_channel_id of this CheckBackendConnectivityReq.
        :rtype: str
        """
        return self._vpc_channel_id

    @vpc_channel_id.setter
    def vpc_channel_id(self, vpc_channel_id):
        """Sets the vpc_channel_id of this CheckBackendConnectivityReq.

        负载通道编号，当type为vpc_channel时必填

        :param vpc_channel_id: The vpc_channel_id of this CheckBackendConnectivityReq.
        :type: str
        """
        self._vpc_channel_id = vpc_channel_id

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
        if not isinstance(other, CheckBackendConnectivityReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
