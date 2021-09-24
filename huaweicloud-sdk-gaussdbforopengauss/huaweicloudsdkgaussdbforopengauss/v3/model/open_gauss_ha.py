# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OpenGaussHa:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'mode': 'str',
        'replication_mode': 'str',
        'consistency': 'str'
    }

    attribute_map = {
        'mode': 'mode',
        'replication_mode': 'replication_mode',
        'consistency': 'consistency'
    }

    def __init__(self, mode=None, replication_mode=None, consistency=None):
        """OpenGaussHa - a model defined in huaweicloud sdk"""
        
        

        self._mode = None
        self._replication_mode = None
        self._consistency = None
        self.discriminator = None

        self.mode = mode
        self.replication_mode = replication_mode
        self.consistency = consistency

    @property
    def mode(self):
        """Gets the mode of this OpenGaussHa.

        GaussDB(for openGauss)为分布式模式，取值：enterprise(企业版) ，不区分大小写。

        :return: The mode of this OpenGaussHa.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this OpenGaussHa.

        GaussDB(for openGauss)为分布式模式，取值：enterprise(企业版) ，不区分大小写。

        :param mode: The mode of this OpenGaussHa.
        :type: str
        """
        self._mode = mode

    @property
    def replication_mode(self):
        """Gets the replication_mode of this OpenGaussHa.

        备机同步参数。  取值：  GaussDB(for openGauss)为“sync\"  说明： - “sync”为同步模式。

        :return: The replication_mode of this OpenGaussHa.
        :rtype: str
        """
        return self._replication_mode

    @replication_mode.setter
    def replication_mode(self, replication_mode):
        """Sets the replication_mode of this OpenGaussHa.

        备机同步参数。  取值：  GaussDB(for openGauss)为“sync\"  说明： - “sync”为同步模式。

        :param replication_mode: The replication_mode of this OpenGaussHa.
        :type: str
        """
        self._replication_mode = replication_mode

    @property
    def consistency(self):
        """Gets the consistency of this OpenGaussHa.

        指定实例一致性类型，取值范围：strong（强一致性） | eventual(最终一致性)，不分区大小写。

        :return: The consistency of this OpenGaussHa.
        :rtype: str
        """
        return self._consistency

    @consistency.setter
    def consistency(self, consistency):
        """Sets the consistency of this OpenGaussHa.

        指定实例一致性类型，取值范围：strong（强一致性） | eventual(最终一致性)，不分区大小写。

        :param consistency: The consistency of this OpenGaussHa.
        :type: str
        """
        self._consistency = consistency

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
        if not isinstance(other, OpenGaussHa):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
