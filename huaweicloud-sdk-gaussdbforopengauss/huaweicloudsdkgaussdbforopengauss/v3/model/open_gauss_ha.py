# coding: utf-8

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
        'consistency': 'str',
        'replication_mode': 'str',
        'instance_mode': 'str'
    }

    attribute_map = {
        'mode': 'mode',
        'consistency': 'consistency',
        'replication_mode': 'replication_mode',
        'instance_mode': 'instance_mode'
    }

    def __init__(self, mode=None, consistency=None, replication_mode=None, instance_mode=None):
        r"""OpenGaussHa

        The model defined in huaweicloud sdk

        :param mode: GaussDB为分布式时，取值：enterprise；为集中式时，取值：centralization_standard。不区分大小写。
        :type mode: str
        :param consistency: 指定实例一致性类型，当创建分布式模式实例时，该字段值必传，当创建主备模式实例时，该字段值不传。取值范围：strong（强一致性） | eventual(最终一致性)，不分区大小写。
        :type consistency: str
        :param replication_mode: 备机同步参数。  取值：  GaussDB为“sync\&quot;  说明： - “sync”为同步模式。
        :type replication_mode: str
        :param instance_mode: 指定创建实例的产品类型，创建企业版实例时传空值或者enterprise，创建基础版实例时需要指定instance_mode的值为basic，创建生态版实例时需要指定instance_mode的值为ecology。
        :type instance_mode: str
        """
        
        

        self._mode = None
        self._consistency = None
        self._replication_mode = None
        self._instance_mode = None
        self.discriminator = None

        self.mode = mode
        self.consistency = consistency
        self.replication_mode = replication_mode
        if instance_mode is not None:
            self.instance_mode = instance_mode

    @property
    def mode(self):
        r"""Gets the mode of this OpenGaussHa.

        GaussDB为分布式时，取值：enterprise；为集中式时，取值：centralization_standard。不区分大小写。

        :return: The mode of this OpenGaussHa.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        r"""Sets the mode of this OpenGaussHa.

        GaussDB为分布式时，取值：enterprise；为集中式时，取值：centralization_standard。不区分大小写。

        :param mode: The mode of this OpenGaussHa.
        :type mode: str
        """
        self._mode = mode

    @property
    def consistency(self):
        r"""Gets the consistency of this OpenGaussHa.

        指定实例一致性类型，当创建分布式模式实例时，该字段值必传，当创建主备模式实例时，该字段值不传。取值范围：strong（强一致性） | eventual(最终一致性)，不分区大小写。

        :return: The consistency of this OpenGaussHa.
        :rtype: str
        """
        return self._consistency

    @consistency.setter
    def consistency(self, consistency):
        r"""Sets the consistency of this OpenGaussHa.

        指定实例一致性类型，当创建分布式模式实例时，该字段值必传，当创建主备模式实例时，该字段值不传。取值范围：strong（强一致性） | eventual(最终一致性)，不分区大小写。

        :param consistency: The consistency of this OpenGaussHa.
        :type consistency: str
        """
        self._consistency = consistency

    @property
    def replication_mode(self):
        r"""Gets the replication_mode of this OpenGaussHa.

        备机同步参数。  取值：  GaussDB为“sync\"  说明： - “sync”为同步模式。

        :return: The replication_mode of this OpenGaussHa.
        :rtype: str
        """
        return self._replication_mode

    @replication_mode.setter
    def replication_mode(self, replication_mode):
        r"""Sets the replication_mode of this OpenGaussHa.

        备机同步参数。  取值：  GaussDB为“sync\"  说明： - “sync”为同步模式。

        :param replication_mode: The replication_mode of this OpenGaussHa.
        :type replication_mode: str
        """
        self._replication_mode = replication_mode

    @property
    def instance_mode(self):
        r"""Gets the instance_mode of this OpenGaussHa.

        指定创建实例的产品类型，创建企业版实例时传空值或者enterprise，创建基础版实例时需要指定instance_mode的值为basic，创建生态版实例时需要指定instance_mode的值为ecology。

        :return: The instance_mode of this OpenGaussHa.
        :rtype: str
        """
        return self._instance_mode

    @instance_mode.setter
    def instance_mode(self, instance_mode):
        r"""Sets the instance_mode of this OpenGaussHa.

        指定创建实例的产品类型，创建企业版实例时传空值或者enterprise，创建基础版实例时需要指定instance_mode的值为basic，创建生态版实例时需要指定instance_mode的值为ecology。

        :param instance_mode: The instance_mode of this OpenGaussHa.
        :type instance_mode: str
        """
        self._instance_mode = instance_mode

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
