# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowRabbitMqProductCoresRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'engine': 'str',
        'product_id': 'str',
        'broker_num': 'int',
        'instance_id': 'str'
    }

    attribute_map = {
        'engine': 'engine',
        'product_id': 'product_id',
        'broker_num': 'broker_num',
        'instance_id': 'instance_id'
    }

    def __init__(self, engine=None, product_id=None, broker_num=None, instance_id=None):
        """ShowRabbitMqProductCoresRequest

        The model defined in huaweicloud sdk

        :param engine: 消息引擎的类型。
        :type engine: str
        :param product_id: 产品ID。
        :type product_id: str
        :param broker_num: 代理个数。  当产品为单机类型，代理个数只能为1；当产品为集群类型，可选3、5、7个代理个数。  产品类型为single时:   - 1  产品类型为cluster时:   - 3   - 5   - 7
        :type broker_num: int
        :param instance_id: 实例ID。
        :type instance_id: str
        """
        
        

        self._engine = None
        self._product_id = None
        self._broker_num = None
        self._instance_id = None
        self.discriminator = None

        self.engine = engine
        self.product_id = product_id
        self.broker_num = broker_num
        if instance_id is not None:
            self.instance_id = instance_id

    @property
    def engine(self):
        """Gets the engine of this ShowRabbitMqProductCoresRequest.

        消息引擎的类型。

        :return: The engine of this ShowRabbitMqProductCoresRequest.
        :rtype: str
        """
        return self._engine

    @engine.setter
    def engine(self, engine):
        """Sets the engine of this ShowRabbitMqProductCoresRequest.

        消息引擎的类型。

        :param engine: The engine of this ShowRabbitMqProductCoresRequest.
        :type engine: str
        """
        self._engine = engine

    @property
    def product_id(self):
        """Gets the product_id of this ShowRabbitMqProductCoresRequest.

        产品ID。

        :return: The product_id of this ShowRabbitMqProductCoresRequest.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """Sets the product_id of this ShowRabbitMqProductCoresRequest.

        产品ID。

        :param product_id: The product_id of this ShowRabbitMqProductCoresRequest.
        :type product_id: str
        """
        self._product_id = product_id

    @property
    def broker_num(self):
        """Gets the broker_num of this ShowRabbitMqProductCoresRequest.

        代理个数。  当产品为单机类型，代理个数只能为1；当产品为集群类型，可选3、5、7个代理个数。  产品类型为single时:   - 1  产品类型为cluster时:   - 3   - 5   - 7

        :return: The broker_num of this ShowRabbitMqProductCoresRequest.
        :rtype: int
        """
        return self._broker_num

    @broker_num.setter
    def broker_num(self, broker_num):
        """Sets the broker_num of this ShowRabbitMqProductCoresRequest.

        代理个数。  当产品为单机类型，代理个数只能为1；当产品为集群类型，可选3、5、7个代理个数。  产品类型为single时:   - 1  产品类型为cluster时:   - 3   - 5   - 7

        :param broker_num: The broker_num of this ShowRabbitMqProductCoresRequest.
        :type broker_num: int
        """
        self._broker_num = broker_num

    @property
    def instance_id(self):
        """Gets the instance_id of this ShowRabbitMqProductCoresRequest.

        实例ID。

        :return: The instance_id of this ShowRabbitMqProductCoresRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ShowRabbitMqProductCoresRequest.

        实例ID。

        :param instance_id: The instance_id of this ShowRabbitMqProductCoresRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

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
        if not isinstance(other, ShowRabbitMqProductCoresRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
