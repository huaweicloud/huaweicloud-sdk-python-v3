# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OpenGaussHaResponse:

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
        """OpenGaussHaResponse

        The model defined in huaweicloud sdk

        :param mode: GaussDB 分布式模式，返回值为：Enterprise（企业版）；主备版，返回值为：Ha(主备版)。
        :type mode: str
        :param replication_mode: 备机同步参数。  取值：  GaussDB为“sync”。 说明： - “sync”为同步模式。
        :type replication_mode: str
        :param consistency: GaussDB的预留参数：指定实例一致性类型，取值范围：strong（强一致性） | eventual(最终一致性)。
        :type consistency: str
        """
        
        

        self._mode = None
        self._replication_mode = None
        self._consistency = None
        self.discriminator = None

        self.mode = mode
        self.replication_mode = replication_mode
        self.consistency = consistency

    @property
    def mode(self):
        """Gets the mode of this OpenGaussHaResponse.

        GaussDB 分布式模式，返回值为：Enterprise（企业版）；主备版，返回值为：Ha(主备版)。

        :return: The mode of this OpenGaussHaResponse.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this OpenGaussHaResponse.

        GaussDB 分布式模式，返回值为：Enterprise（企业版）；主备版，返回值为：Ha(主备版)。

        :param mode: The mode of this OpenGaussHaResponse.
        :type mode: str
        """
        self._mode = mode

    @property
    def replication_mode(self):
        """Gets the replication_mode of this OpenGaussHaResponse.

        备机同步参数。  取值：  GaussDB为“sync”。 说明： - “sync”为同步模式。

        :return: The replication_mode of this OpenGaussHaResponse.
        :rtype: str
        """
        return self._replication_mode

    @replication_mode.setter
    def replication_mode(self, replication_mode):
        """Sets the replication_mode of this OpenGaussHaResponse.

        备机同步参数。  取值：  GaussDB为“sync”。 说明： - “sync”为同步模式。

        :param replication_mode: The replication_mode of this OpenGaussHaResponse.
        :type replication_mode: str
        """
        self._replication_mode = replication_mode

    @property
    def consistency(self):
        """Gets the consistency of this OpenGaussHaResponse.

        GaussDB的预留参数：指定实例一致性类型，取值范围：strong（强一致性） | eventual(最终一致性)。

        :return: The consistency of this OpenGaussHaResponse.
        :rtype: str
        """
        return self._consistency

    @consistency.setter
    def consistency(self, consistency):
        """Sets the consistency of this OpenGaussHaResponse.

        GaussDB的预留参数：指定实例一致性类型，取值范围：strong（强一致性） | eventual(最终一致性)。

        :param consistency: The consistency of this OpenGaussHaResponse.
        :type consistency: str
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
        if not isinstance(other, OpenGaussHaResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
