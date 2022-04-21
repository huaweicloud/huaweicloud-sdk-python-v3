# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QosQualityData:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'uid': 'str',
        'peerid': 'str',
        'mid': 'str',
        'data': 'list[TimeFloatValueData]'
    }

    attribute_map = {
        'uid': 'uid',
        'peerid': 'peerid',
        'mid': 'mid',
        'data': 'data'
    }

    def __init__(self, uid=None, peerid=None, mid=None, data=None):
        """QosQualityData

        The model defined in huaweicloud sdk

        :param uid: 用户id
        :type uid: str
        :param peerid: 对端的用户ID，为0时表示本端上行数据
        :type peerid: str
        :param mid: 指标ID
        :type mid: str
        :param data: 时间戳及相应时间的指标数值列表
        :type data: list[:class:`huaweicloudsdkcloudrtc.v1.TimeFloatValueData`]
        """
        
        

        self._uid = None
        self._peerid = None
        self._mid = None
        self._data = None
        self.discriminator = None

        if uid is not None:
            self.uid = uid
        if peerid is not None:
            self.peerid = peerid
        if mid is not None:
            self.mid = mid
        if data is not None:
            self.data = data

    @property
    def uid(self):
        """Gets the uid of this QosQualityData.

        用户id

        :return: The uid of this QosQualityData.
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this QosQualityData.

        用户id

        :param uid: The uid of this QosQualityData.
        :type uid: str
        """
        self._uid = uid

    @property
    def peerid(self):
        """Gets the peerid of this QosQualityData.

        对端的用户ID，为0时表示本端上行数据

        :return: The peerid of this QosQualityData.
        :rtype: str
        """
        return self._peerid

    @peerid.setter
    def peerid(self, peerid):
        """Sets the peerid of this QosQualityData.

        对端的用户ID，为0时表示本端上行数据

        :param peerid: The peerid of this QosQualityData.
        :type peerid: str
        """
        self._peerid = peerid

    @property
    def mid(self):
        """Gets the mid of this QosQualityData.

        指标ID

        :return: The mid of this QosQualityData.
        :rtype: str
        """
        return self._mid

    @mid.setter
    def mid(self, mid):
        """Sets the mid of this QosQualityData.

        指标ID

        :param mid: The mid of this QosQualityData.
        :type mid: str
        """
        self._mid = mid

    @property
    def data(self):
        """Gets the data of this QosQualityData.

        时间戳及相应时间的指标数值列表

        :return: The data of this QosQualityData.
        :rtype: list[:class:`huaweicloudsdkcloudrtc.v1.TimeFloatValueData`]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this QosQualityData.

        时间戳及相应时间的指标数值列表

        :param data: The data of this QosQualityData.
        :type data: list[:class:`huaweicloudsdkcloudrtc.v1.TimeFloatValueData`]
        """
        self._data = data

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
        if not isinstance(other, QosQualityData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
