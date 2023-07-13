# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SetRaspSwitchRequestInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'host_id_list': 'list[str]',
        'status': 'bool'
    }

    attribute_map = {
        'host_id_list': 'host_id_list',
        'status': 'status'
    }

    def __init__(self, host_id_list=None, status=None):
        """SetRaspSwitchRequestInfo

        The model defined in huaweicloud sdk

        :param host_id_list: HostId list
        :type host_id_list: list[str]
        :param status: 动态网页防篡改状态
        :type status: bool
        """
        
        

        self._host_id_list = None
        self._status = None
        self.discriminator = None

        if host_id_list is not None:
            self.host_id_list = host_id_list
        if status is not None:
            self.status = status

    @property
    def host_id_list(self):
        """Gets the host_id_list of this SetRaspSwitchRequestInfo.

        HostId list

        :return: The host_id_list of this SetRaspSwitchRequestInfo.
        :rtype: list[str]
        """
        return self._host_id_list

    @host_id_list.setter
    def host_id_list(self, host_id_list):
        """Sets the host_id_list of this SetRaspSwitchRequestInfo.

        HostId list

        :param host_id_list: The host_id_list of this SetRaspSwitchRequestInfo.
        :type host_id_list: list[str]
        """
        self._host_id_list = host_id_list

    @property
    def status(self):
        """Gets the status of this SetRaspSwitchRequestInfo.

        动态网页防篡改状态

        :return: The status of this SetRaspSwitchRequestInfo.
        :rtype: bool
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this SetRaspSwitchRequestInfo.

        动态网页防篡改状态

        :param status: The status of this SetRaspSwitchRequestInfo.
        :type status: bool
        """
        self._status = status

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
        if not isinstance(other, SetRaspSwitchRequestInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
