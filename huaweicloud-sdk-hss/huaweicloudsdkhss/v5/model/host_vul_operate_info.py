# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HostVulOperateInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'host_id': 'str',
        'vul_id_list': 'list[str]'
    }

    attribute_map = {
        'host_id': 'host_id',
        'vul_id_list': 'vul_id_list'
    }

    def __init__(self, host_id=None, vul_id_list=None):
        """HostVulOperateInfo

        The model defined in huaweicloud sdk

        :param host_id: 主机ID
        :type host_id: str
        :param vul_id_list: 漏洞列表
        :type vul_id_list: list[str]
        """
        
        

        self._host_id = None
        self._vul_id_list = None
        self.discriminator = None

        self.host_id = host_id
        self.vul_id_list = vul_id_list

    @property
    def host_id(self):
        """Gets the host_id of this HostVulOperateInfo.

        主机ID

        :return: The host_id of this HostVulOperateInfo.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        """Sets the host_id of this HostVulOperateInfo.

        主机ID

        :param host_id: The host_id of this HostVulOperateInfo.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def vul_id_list(self):
        """Gets the vul_id_list of this HostVulOperateInfo.

        漏洞列表

        :return: The vul_id_list of this HostVulOperateInfo.
        :rtype: list[str]
        """
        return self._vul_id_list

    @vul_id_list.setter
    def vul_id_list(self, vul_id_list):
        """Sets the vul_id_list of this HostVulOperateInfo.

        漏洞列表

        :param vul_id_list: The vul_id_list of this HostVulOperateInfo.
        :type vul_id_list: list[str]
        """
        self._vul_id_list = vul_id_list

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
        if not isinstance(other, HostVulOperateInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
