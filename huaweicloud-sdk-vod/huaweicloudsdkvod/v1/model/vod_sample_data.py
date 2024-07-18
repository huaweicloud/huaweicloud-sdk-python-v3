# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VodSampleData:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'storage': 'float',
        'storage_warm': 'float',
        'storage_cold': 'float',
        'transcode': 'int'
    }

    attribute_map = {
        'storage': 'storage',
        'storage_warm': 'storage_warm',
        'storage_cold': 'storage_cold',
        'transcode': 'transcode'
    }

    def __init__(self, storage=None, storage_warm=None, storage_cold=None, transcode=None):
        """VodSampleData

        The model defined in huaweicloud sdk

        :param storage: 存储空间。  单位：GB。
        :type storage: float
        :param storage_warm: 低频存储空间。  单位：GB。
        :type storage_warm: float
        :param storage_cold: 归档存储空间。  单位：GB。
        :type storage_cold: float
        :param transcode: 转码时长。  单位：分钟。
        :type transcode: int
        """
        
        

        self._storage = None
        self._storage_warm = None
        self._storage_cold = None
        self._transcode = None
        self.discriminator = None

        if storage is not None:
            self.storage = storage
        if storage_warm is not None:
            self.storage_warm = storage_warm
        if storage_cold is not None:
            self.storage_cold = storage_cold
        if transcode is not None:
            self.transcode = transcode

    @property
    def storage(self):
        """Gets the storage of this VodSampleData.

        存储空间。  单位：GB。

        :return: The storage of this VodSampleData.
        :rtype: float
        """
        return self._storage

    @storage.setter
    def storage(self, storage):
        """Sets the storage of this VodSampleData.

        存储空间。  单位：GB。

        :param storage: The storage of this VodSampleData.
        :type storage: float
        """
        self._storage = storage

    @property
    def storage_warm(self):
        """Gets the storage_warm of this VodSampleData.

        低频存储空间。  单位：GB。

        :return: The storage_warm of this VodSampleData.
        :rtype: float
        """
        return self._storage_warm

    @storage_warm.setter
    def storage_warm(self, storage_warm):
        """Sets the storage_warm of this VodSampleData.

        低频存储空间。  单位：GB。

        :param storage_warm: The storage_warm of this VodSampleData.
        :type storage_warm: float
        """
        self._storage_warm = storage_warm

    @property
    def storage_cold(self):
        """Gets the storage_cold of this VodSampleData.

        归档存储空间。  单位：GB。

        :return: The storage_cold of this VodSampleData.
        :rtype: float
        """
        return self._storage_cold

    @storage_cold.setter
    def storage_cold(self, storage_cold):
        """Sets the storage_cold of this VodSampleData.

        归档存储空间。  单位：GB。

        :param storage_cold: The storage_cold of this VodSampleData.
        :type storage_cold: float
        """
        self._storage_cold = storage_cold

    @property
    def transcode(self):
        """Gets the transcode of this VodSampleData.

        转码时长。  单位：分钟。

        :return: The transcode of this VodSampleData.
        :rtype: int
        """
        return self._transcode

    @transcode.setter
    def transcode(self, transcode):
        """Sets the transcode of this VodSampleData.

        转码时长。  单位：分钟。

        :param transcode: The transcode of this VodSampleData.
        :type transcode: int
        """
        self._transcode = transcode

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
        if not isinstance(other, VodSampleData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
