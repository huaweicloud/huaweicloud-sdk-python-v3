# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DataConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'offline': 'Offline',
        'nearline': 'Nearline'
    }

    attribute_map = {
        'offline': 'offline',
        'nearline': 'nearline'
    }

    def __init__(self, offline=None, nearline=None):
        """DataConfig

        The model defined in huaweicloud sdk

        :param offline: 
        :type offline: :class:`huaweicloudsdkres.v1.Offline`
        :param nearline: 
        :type nearline: :class:`huaweicloudsdkres.v1.Nearline`
        """
        
        

        self._offline = None
        self._nearline = None
        self.discriminator = None

        self.offline = offline
        if nearline is not None:
            self.nearline = nearline

    @property
    def offline(self):
        """Gets the offline of this DataConfig.


        :return: The offline of this DataConfig.
        :rtype: :class:`huaweicloudsdkres.v1.Offline`
        """
        return self._offline

    @offline.setter
    def offline(self, offline):
        """Sets the offline of this DataConfig.


        :param offline: The offline of this DataConfig.
        :type offline: :class:`huaweicloudsdkres.v1.Offline`
        """
        self._offline = offline

    @property
    def nearline(self):
        """Gets the nearline of this DataConfig.


        :return: The nearline of this DataConfig.
        :rtype: :class:`huaweicloudsdkres.v1.Nearline`
        """
        return self._nearline

    @nearline.setter
    def nearline(self, nearline):
        """Sets the nearline of this DataConfig.


        :param nearline: The nearline of this DataConfig.
        :type nearline: :class:`huaweicloudsdkres.v1.Nearline`
        """
        self._nearline = nearline

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
        if not isinstance(other, DataConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
