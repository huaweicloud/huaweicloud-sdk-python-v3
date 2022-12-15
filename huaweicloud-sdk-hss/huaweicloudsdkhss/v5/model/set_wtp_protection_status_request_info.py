# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SetWtpProtectionStatusRequestInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status': 'bool',
        'host_id_list': 'list[str]',
        'resource_id': 'str',
        'payment_mode': 'int'
    }

    attribute_map = {
        'status': 'status',
        'host_id_list': 'host_id_list',
        'resource_id': 'resource_id',
        'payment_mode': 'payment_mode'
    }

    def __init__(self, status=None, host_id_list=None, resource_id=None, payment_mode=None):
        """SetWtpProtectionStatusRequestInfo

        The model defined in huaweicloud sdk

        :param status: 开启关闭状态
        :type status: bool
        :param host_id_list: HostId list
        :type host_id_list: list[str]
        :param resource_id: 资源ID
        :type resource_id: str
        :param payment_mode: 随机选择配额还是指定资源
        :type payment_mode: int
        """
        
        

        self._status = None
        self._host_id_list = None
        self._resource_id = None
        self._payment_mode = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if host_id_list is not None:
            self.host_id_list = host_id_list
        if resource_id is not None:
            self.resource_id = resource_id
        if payment_mode is not None:
            self.payment_mode = payment_mode

    @property
    def status(self):
        """Gets the status of this SetWtpProtectionStatusRequestInfo.

        开启关闭状态

        :return: The status of this SetWtpProtectionStatusRequestInfo.
        :rtype: bool
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this SetWtpProtectionStatusRequestInfo.

        开启关闭状态

        :param status: The status of this SetWtpProtectionStatusRequestInfo.
        :type status: bool
        """
        self._status = status

    @property
    def host_id_list(self):
        """Gets the host_id_list of this SetWtpProtectionStatusRequestInfo.

        HostId list

        :return: The host_id_list of this SetWtpProtectionStatusRequestInfo.
        :rtype: list[str]
        """
        return self._host_id_list

    @host_id_list.setter
    def host_id_list(self, host_id_list):
        """Sets the host_id_list of this SetWtpProtectionStatusRequestInfo.

        HostId list

        :param host_id_list: The host_id_list of this SetWtpProtectionStatusRequestInfo.
        :type host_id_list: list[str]
        """
        self._host_id_list = host_id_list

    @property
    def resource_id(self):
        """Gets the resource_id of this SetWtpProtectionStatusRequestInfo.

        资源ID

        :return: The resource_id of this SetWtpProtectionStatusRequestInfo.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this SetWtpProtectionStatusRequestInfo.

        资源ID

        :param resource_id: The resource_id of this SetWtpProtectionStatusRequestInfo.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def payment_mode(self):
        """Gets the payment_mode of this SetWtpProtectionStatusRequestInfo.

        随机选择配额还是指定资源

        :return: The payment_mode of this SetWtpProtectionStatusRequestInfo.
        :rtype: int
        """
        return self._payment_mode

    @payment_mode.setter
    def payment_mode(self, payment_mode):
        """Sets the payment_mode of this SetWtpProtectionStatusRequestInfo.

        随机选择配额还是指定资源

        :param payment_mode: The payment_mode of this SetWtpProtectionStatusRequestInfo.
        :type payment_mode: int
        """
        self._payment_mode = payment_mode

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
        if not isinstance(other, SetWtpProtectionStatusRequestInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
