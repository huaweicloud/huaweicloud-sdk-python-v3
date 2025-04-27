# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IpaddressesData:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status': 'str',
        'id': 'str',
        'ip': 'str',
        'create_time': 'str',
        'update_time': 'str',
        'subnet_id': 'str',
        'error_info': 'str'
    }

    attribute_map = {
        'status': 'status',
        'id': 'id',
        'ip': 'ip',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'subnet_id': 'subnet_id',
        'error_info': 'error_info'
    }

    def __init__(self, status=None, id=None, ip=None, create_time=None, update_time=None, subnet_id=None, error_info=None):
        r"""IpaddressesData

        The model defined in huaweicloud sdk

        :param status: 资源状态。
        :type status: str
        :param id: 终端节点的ID，UUID形式的一个资源标识。
        :type id: str
        :param ip: IP地址信息。
        :type ip: str
        :param create_time: 创建时间。 格式：yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSS。
        :type create_time: str
        :param update_time: 更新时间。 格式：yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSS。
        :type update_time: str
        :param subnet_id: 子网ID。
        :type subnet_id: str
        :param error_info: 错误信息。
        :type error_info: str
        """
        
        

        self._status = None
        self._id = None
        self._ip = None
        self._create_time = None
        self._update_time = None
        self._subnet_id = None
        self._error_info = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if id is not None:
            self.id = id
        if ip is not None:
            self.ip = ip
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if subnet_id is not None:
            self.subnet_id = subnet_id
        if error_info is not None:
            self.error_info = error_info

    @property
    def status(self):
        r"""Gets the status of this IpaddressesData.

        资源状态。

        :return: The status of this IpaddressesData.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this IpaddressesData.

        资源状态。

        :param status: The status of this IpaddressesData.
        :type status: str
        """
        self._status = status

    @property
    def id(self):
        r"""Gets the id of this IpaddressesData.

        终端节点的ID，UUID形式的一个资源标识。

        :return: The id of this IpaddressesData.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this IpaddressesData.

        终端节点的ID，UUID形式的一个资源标识。

        :param id: The id of this IpaddressesData.
        :type id: str
        """
        self._id = id

    @property
    def ip(self):
        r"""Gets the ip of this IpaddressesData.

        IP地址信息。

        :return: The ip of this IpaddressesData.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        r"""Sets the ip of this IpaddressesData.

        IP地址信息。

        :param ip: The ip of this IpaddressesData.
        :type ip: str
        """
        self._ip = ip

    @property
    def create_time(self):
        r"""Gets the create_time of this IpaddressesData.

        创建时间。 格式：yyyy-MM-dd'T'HH:mm:ss.SSS。

        :return: The create_time of this IpaddressesData.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this IpaddressesData.

        创建时间。 格式：yyyy-MM-dd'T'HH:mm:ss.SSS。

        :param create_time: The create_time of this IpaddressesData.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this IpaddressesData.

        更新时间。 格式：yyyy-MM-dd'T'HH:mm:ss.SSS。

        :return: The update_time of this IpaddressesData.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this IpaddressesData.

        更新时间。 格式：yyyy-MM-dd'T'HH:mm:ss.SSS。

        :param update_time: The update_time of this IpaddressesData.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def subnet_id(self):
        r"""Gets the subnet_id of this IpaddressesData.

        子网ID。

        :return: The subnet_id of this IpaddressesData.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        r"""Sets the subnet_id of this IpaddressesData.

        子网ID。

        :param subnet_id: The subnet_id of this IpaddressesData.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def error_info(self):
        r"""Gets the error_info of this IpaddressesData.

        错误信息。

        :return: The error_info of this IpaddressesData.
        :rtype: str
        """
        return self._error_info

    @error_info.setter
    def error_info(self, error_info):
        r"""Sets the error_info of this IpaddressesData.

        错误信息。

        :param error_info: The error_info of this IpaddressesData.
        :type error_info: str
        """
        self._error_info = error_info

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
        if not isinstance(other, IpaddressesData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
