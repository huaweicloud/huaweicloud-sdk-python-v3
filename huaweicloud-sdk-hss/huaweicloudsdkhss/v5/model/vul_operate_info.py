# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VulOperateInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'vul_id': 'str',
        'host_id_list': 'list[str]'
    }

    attribute_map = {
        'vul_id': 'vul_id',
        'host_id_list': 'host_id_list'
    }

    def __init__(self, vul_id=None, host_id_list=None):
        """VulOperateInfo

        The model defined in huaweicloud sdk

        :param vul_id: 漏洞ID
        :type vul_id: str
        :param host_id_list: 主机列表
        :type host_id_list: list[str]
        """
        
        

        self._vul_id = None
        self._host_id_list = None
        self.discriminator = None

        self.vul_id = vul_id
        self.host_id_list = host_id_list

    @property
    def vul_id(self):
        """Gets the vul_id of this VulOperateInfo.

        漏洞ID

        :return: The vul_id of this VulOperateInfo.
        :rtype: str
        """
        return self._vul_id

    @vul_id.setter
    def vul_id(self, vul_id):
        """Sets the vul_id of this VulOperateInfo.

        漏洞ID

        :param vul_id: The vul_id of this VulOperateInfo.
        :type vul_id: str
        """
        self._vul_id = vul_id

    @property
    def host_id_list(self):
        """Gets the host_id_list of this VulOperateInfo.

        主机列表

        :return: The host_id_list of this VulOperateInfo.
        :rtype: list[str]
        """
        return self._host_id_list

    @host_id_list.setter
    def host_id_list(self, host_id_list):
        """Sets the host_id_list of this VulOperateInfo.

        主机列表

        :param host_id_list: The host_id_list of this VulOperateInfo.
        :type host_id_list: list[str]
        """
        self._host_id_list = host_id_list

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
        if not isinstance(other, VulOperateInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
