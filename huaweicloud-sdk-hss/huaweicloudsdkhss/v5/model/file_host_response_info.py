# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FileHostResponseInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'host_name': 'str',
        'host_id': 'str',
        'change_total_num': 'int',
        'change_file_num': 'int',
        'change_registry_num': 'int',
        'latest_time': 'int'
    }

    attribute_map = {
        'host_name': 'host_name',
        'host_id': 'host_id',
        'change_total_num': 'change_total_num',
        'change_file_num': 'change_file_num',
        'change_registry_num': 'change_registry_num',
        'latest_time': 'latest_time'
    }

    def __init__(self, host_name=None, host_id=None, change_total_num=None, change_file_num=None, change_registry_num=None, latest_time=None):
        r"""FileHostResponseInfo

        The model defined in huaweicloud sdk

        :param host_name: 服务器名称
        :type host_name: str
        :param host_id: 服务器ID
        :type host_id: str
        :param change_total_num: 变更总数
        :type change_total_num: int
        :param change_file_num: 变更文件
        :type change_file_num: int
        :param change_registry_num: 变更注册表
        :type change_registry_num: int
        :param latest_time: 最后变更时间
        :type latest_time: int
        """
        
        

        self._host_name = None
        self._host_id = None
        self._change_total_num = None
        self._change_file_num = None
        self._change_registry_num = None
        self._latest_time = None
        self.discriminator = None

        if host_name is not None:
            self.host_name = host_name
        if host_id is not None:
            self.host_id = host_id
        if change_total_num is not None:
            self.change_total_num = change_total_num
        if change_file_num is not None:
            self.change_file_num = change_file_num
        if change_registry_num is not None:
            self.change_registry_num = change_registry_num
        if latest_time is not None:
            self.latest_time = latest_time

    @property
    def host_name(self):
        r"""Gets the host_name of this FileHostResponseInfo.

        服务器名称

        :return: The host_name of this FileHostResponseInfo.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        r"""Sets the host_name of this FileHostResponseInfo.

        服务器名称

        :param host_name: The host_name of this FileHostResponseInfo.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def host_id(self):
        r"""Gets the host_id of this FileHostResponseInfo.

        服务器ID

        :return: The host_id of this FileHostResponseInfo.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        r"""Sets the host_id of this FileHostResponseInfo.

        服务器ID

        :param host_id: The host_id of this FileHostResponseInfo.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def change_total_num(self):
        r"""Gets the change_total_num of this FileHostResponseInfo.

        变更总数

        :return: The change_total_num of this FileHostResponseInfo.
        :rtype: int
        """
        return self._change_total_num

    @change_total_num.setter
    def change_total_num(self, change_total_num):
        r"""Sets the change_total_num of this FileHostResponseInfo.

        变更总数

        :param change_total_num: The change_total_num of this FileHostResponseInfo.
        :type change_total_num: int
        """
        self._change_total_num = change_total_num

    @property
    def change_file_num(self):
        r"""Gets the change_file_num of this FileHostResponseInfo.

        变更文件

        :return: The change_file_num of this FileHostResponseInfo.
        :rtype: int
        """
        return self._change_file_num

    @change_file_num.setter
    def change_file_num(self, change_file_num):
        r"""Sets the change_file_num of this FileHostResponseInfo.

        变更文件

        :param change_file_num: The change_file_num of this FileHostResponseInfo.
        :type change_file_num: int
        """
        self._change_file_num = change_file_num

    @property
    def change_registry_num(self):
        r"""Gets the change_registry_num of this FileHostResponseInfo.

        变更注册表

        :return: The change_registry_num of this FileHostResponseInfo.
        :rtype: int
        """
        return self._change_registry_num

    @change_registry_num.setter
    def change_registry_num(self, change_registry_num):
        r"""Sets the change_registry_num of this FileHostResponseInfo.

        变更注册表

        :param change_registry_num: The change_registry_num of this FileHostResponseInfo.
        :type change_registry_num: int
        """
        self._change_registry_num = change_registry_num

    @property
    def latest_time(self):
        r"""Gets the latest_time of this FileHostResponseInfo.

        最后变更时间

        :return: The latest_time of this FileHostResponseInfo.
        :rtype: int
        """
        return self._latest_time

    @latest_time.setter
    def latest_time(self, latest_time):
        r"""Sets the latest_time of this FileHostResponseInfo.

        最后变更时间

        :param latest_time: The latest_time of this FileHostResponseInfo.
        :type latest_time: int
        """
        self._latest_time = latest_time

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
        if not isinstance(other, FileHostResponseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
