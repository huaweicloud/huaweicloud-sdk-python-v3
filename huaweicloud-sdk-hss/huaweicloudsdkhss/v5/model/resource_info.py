# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResourceInfo:

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
        'history_backup_status': 'str'
    }

    attribute_map = {
        'host_id': 'host_id',
        'history_backup_status': 'history_backup_status'
    }

    def __init__(self, host_id=None, history_backup_status=None):
        """ResourceInfo

        The model defined in huaweicloud sdk

        :param host_id: 主机id
        :type host_id: str
        :param history_backup_status: 历史开启备份状态，通过筛选可用服务器的error_message或者status判断，如果error_message为空，则没有开启备份，该字段为closed；若不为空，则为opened
        :type history_backup_status: str
        """
        
        

        self._host_id = None
        self._history_backup_status = None
        self.discriminator = None

        if host_id is not None:
            self.host_id = host_id
        if history_backup_status is not None:
            self.history_backup_status = history_backup_status

    @property
    def host_id(self):
        """Gets the host_id of this ResourceInfo.

        主机id

        :return: The host_id of this ResourceInfo.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        """Sets the host_id of this ResourceInfo.

        主机id

        :param host_id: The host_id of this ResourceInfo.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def history_backup_status(self):
        """Gets the history_backup_status of this ResourceInfo.

        历史开启备份状态，通过筛选可用服务器的error_message或者status判断，如果error_message为空，则没有开启备份，该字段为closed；若不为空，则为opened

        :return: The history_backup_status of this ResourceInfo.
        :rtype: str
        """
        return self._history_backup_status

    @history_backup_status.setter
    def history_backup_status(self, history_backup_status):
        """Sets the history_backup_status of this ResourceInfo.

        历史开启备份状态，通过筛选可用服务器的error_message或者status判断，如果error_message为空，则没有开启备份，该字段为closed；若不为空，则为opened

        :param history_backup_status: The history_backup_status of this ResourceInfo.
        :type history_backup_status: str
        """
        self._history_backup_status = history_backup_status

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
        if not isinstance(other, ResourceInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
