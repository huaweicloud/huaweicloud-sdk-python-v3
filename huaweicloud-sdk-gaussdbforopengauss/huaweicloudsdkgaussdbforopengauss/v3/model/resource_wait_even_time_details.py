# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResourceWaitEvenTimeDetails:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'data_io_time': 'DataIoTime',
        'lock_time': 'LockTime',
        'lwlock_time': 'LwlockTime'
    }

    attribute_map = {
        'data_io_time': 'data_io_time',
        'lock_time': 'lock_time',
        'lwlock_time': 'lwlock_time'
    }

    def __init__(self, data_io_time=None, lock_time=None, lwlock_time=None):
        r"""ResourceWaitEvenTimeDetails

        The model defined in huaweicloud sdk

        :param data_io_time: 
        :type data_io_time: :class:`huaweicloudsdkgaussdbforopengauss.v3.DataIoTime`
        :param lock_time: 
        :type lock_time: :class:`huaweicloudsdkgaussdbforopengauss.v3.LockTime`
        :param lwlock_time: 
        :type lwlock_time: :class:`huaweicloudsdkgaussdbforopengauss.v3.LwlockTime`
        """
        
        

        self._data_io_time = None
        self._lock_time = None
        self._lwlock_time = None
        self.discriminator = None

        self.data_io_time = data_io_time
        self.lock_time = lock_time
        self.lwlock_time = lwlock_time

    @property
    def data_io_time(self):
        r"""Gets the data_io_time of this ResourceWaitEvenTimeDetails.

        :return: The data_io_time of this ResourceWaitEvenTimeDetails.
        :rtype: :class:`huaweicloudsdkgaussdbforopengauss.v3.DataIoTime`
        """
        return self._data_io_time

    @data_io_time.setter
    def data_io_time(self, data_io_time):
        r"""Sets the data_io_time of this ResourceWaitEvenTimeDetails.

        :param data_io_time: The data_io_time of this ResourceWaitEvenTimeDetails.
        :type data_io_time: :class:`huaweicloudsdkgaussdbforopengauss.v3.DataIoTime`
        """
        self._data_io_time = data_io_time

    @property
    def lock_time(self):
        r"""Gets the lock_time of this ResourceWaitEvenTimeDetails.

        :return: The lock_time of this ResourceWaitEvenTimeDetails.
        :rtype: :class:`huaweicloudsdkgaussdbforopengauss.v3.LockTime`
        """
        return self._lock_time

    @lock_time.setter
    def lock_time(self, lock_time):
        r"""Sets the lock_time of this ResourceWaitEvenTimeDetails.

        :param lock_time: The lock_time of this ResourceWaitEvenTimeDetails.
        :type lock_time: :class:`huaweicloudsdkgaussdbforopengauss.v3.LockTime`
        """
        self._lock_time = lock_time

    @property
    def lwlock_time(self):
        r"""Gets the lwlock_time of this ResourceWaitEvenTimeDetails.

        :return: The lwlock_time of this ResourceWaitEvenTimeDetails.
        :rtype: :class:`huaweicloudsdkgaussdbforopengauss.v3.LwlockTime`
        """
        return self._lwlock_time

    @lwlock_time.setter
    def lwlock_time(self, lwlock_time):
        r"""Sets the lwlock_time of this ResourceWaitEvenTimeDetails.

        :param lwlock_time: The lwlock_time of this ResourceWaitEvenTimeDetails.
        :type lwlock_time: :class:`huaweicloudsdkgaussdbforopengauss.v3.LwlockTime`
        """
        self._lwlock_time = lwlock_time

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
        if not isinstance(other, ResourceWaitEvenTimeDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
