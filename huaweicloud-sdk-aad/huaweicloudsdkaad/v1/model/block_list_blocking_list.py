# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BlockListBlockingList:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ip': 'str',
        'blocking_time': 'int',
        'estimated_unblocking_time': 'int',
        'status': 'str'
    }

    attribute_map = {
        'ip': 'ip',
        'blocking_time': 'blocking_time',
        'estimated_unblocking_time': 'estimated_unblocking_time',
        'status': 'status'
    }

    def __init__(self, ip=None, blocking_time=None, estimated_unblocking_time=None, status=None):
        r"""BlockListBlockingList

        The model defined in huaweicloud sdk

        :param ip: ip地址
        :type ip: str
        :param blocking_time: 封堵时间
        :type blocking_time: int
        :param estimated_unblocking_time: 预计解封时间
        :type estimated_unblocking_time: int
        :param status: 状态。unblocking：解封中；success：成功；failed：失败
        :type status: str
        """
        
        

        self._ip = None
        self._blocking_time = None
        self._estimated_unblocking_time = None
        self._status = None
        self.discriminator = None

        self.ip = ip
        self.blocking_time = blocking_time
        self.estimated_unblocking_time = estimated_unblocking_time
        self.status = status

    @property
    def ip(self):
        r"""Gets the ip of this BlockListBlockingList.

        ip地址

        :return: The ip of this BlockListBlockingList.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        r"""Sets the ip of this BlockListBlockingList.

        ip地址

        :param ip: The ip of this BlockListBlockingList.
        :type ip: str
        """
        self._ip = ip

    @property
    def blocking_time(self):
        r"""Gets the blocking_time of this BlockListBlockingList.

        封堵时间

        :return: The blocking_time of this BlockListBlockingList.
        :rtype: int
        """
        return self._blocking_time

    @blocking_time.setter
    def blocking_time(self, blocking_time):
        r"""Sets the blocking_time of this BlockListBlockingList.

        封堵时间

        :param blocking_time: The blocking_time of this BlockListBlockingList.
        :type blocking_time: int
        """
        self._blocking_time = blocking_time

    @property
    def estimated_unblocking_time(self):
        r"""Gets the estimated_unblocking_time of this BlockListBlockingList.

        预计解封时间

        :return: The estimated_unblocking_time of this BlockListBlockingList.
        :rtype: int
        """
        return self._estimated_unblocking_time

    @estimated_unblocking_time.setter
    def estimated_unblocking_time(self, estimated_unblocking_time):
        r"""Sets the estimated_unblocking_time of this BlockListBlockingList.

        预计解封时间

        :param estimated_unblocking_time: The estimated_unblocking_time of this BlockListBlockingList.
        :type estimated_unblocking_time: int
        """
        self._estimated_unblocking_time = estimated_unblocking_time

    @property
    def status(self):
        r"""Gets the status of this BlockListBlockingList.

        状态。unblocking：解封中；success：成功；failed：失败

        :return: The status of this BlockListBlockingList.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this BlockListBlockingList.

        状态。unblocking：解封中；success：成功；failed：失败

        :param status: The status of this BlockListBlockingList.
        :type status: str
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
        if not isinstance(other, BlockListBlockingList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
