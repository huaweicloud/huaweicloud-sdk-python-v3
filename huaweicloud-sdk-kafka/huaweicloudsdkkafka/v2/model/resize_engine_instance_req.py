# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResizeEngineInstanceReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'oper_type': 'str',
        'new_storage_space': 'int',
        'new_broker_num': 'int',
        'new_product_id': 'str'
    }

    attribute_map = {
        'oper_type': 'oper_type',
        'new_storage_space': 'new_storage_space',
        'new_broker_num': 'new_broker_num',
        'new_product_id': 'new_product_id'
    }

    def __init__(self, oper_type=None, new_storage_space=None, new_broker_num=None, new_product_id=None):
        """ResizeEngineInstanceReq

        The model defined in huaweicloud sdk

        :param oper_type: 变更类型。  取值范围：   - storage：存储空间扩容，代理数量不变。    - horizontal：代理数量扩容，每个broker的存储空间不变。    - vertical：垂直扩容，broker的底层虚机规格变更，代理数量和存储空间不变。
        :type oper_type: str
        :param new_storage_space: 扩容后的存储空间。  当oper_type类型是storage或horizontal时，该参数有效且必填。  实例存储空间 &#x3D; 代理数量 * 每个broker的存储空间。  当oper_type类型是storage时，代理数量不变，每个broker存储空间最少扩容100GB。  当oper_type类型是horizontal时，每个broker的存储空间不变。
        :type new_storage_space: int
        :param new_broker_num: 当oper_type参数为horizontal时，该参数有效。  取值范围：最多支持30个broker。
        :type new_broker_num: int
        :param new_product_id: 垂直扩容时的新产品ID。  当oper_type类型是vertical时，该参数才有效且必填。
        :type new_product_id: str
        """
        
        

        self._oper_type = None
        self._new_storage_space = None
        self._new_broker_num = None
        self._new_product_id = None
        self.discriminator = None

        self.oper_type = oper_type
        if new_storage_space is not None:
            self.new_storage_space = new_storage_space
        if new_broker_num is not None:
            self.new_broker_num = new_broker_num
        if new_product_id is not None:
            self.new_product_id = new_product_id

    @property
    def oper_type(self):
        """Gets the oper_type of this ResizeEngineInstanceReq.

        变更类型。  取值范围：   - storage：存储空间扩容，代理数量不变。    - horizontal：代理数量扩容，每个broker的存储空间不变。    - vertical：垂直扩容，broker的底层虚机规格变更，代理数量和存储空间不变。

        :return: The oper_type of this ResizeEngineInstanceReq.
        :rtype: str
        """
        return self._oper_type

    @oper_type.setter
    def oper_type(self, oper_type):
        """Sets the oper_type of this ResizeEngineInstanceReq.

        变更类型。  取值范围：   - storage：存储空间扩容，代理数量不变。    - horizontal：代理数量扩容，每个broker的存储空间不变。    - vertical：垂直扩容，broker的底层虚机规格变更，代理数量和存储空间不变。

        :param oper_type: The oper_type of this ResizeEngineInstanceReq.
        :type oper_type: str
        """
        self._oper_type = oper_type

    @property
    def new_storage_space(self):
        """Gets the new_storage_space of this ResizeEngineInstanceReq.

        扩容后的存储空间。  当oper_type类型是storage或horizontal时，该参数有效且必填。  实例存储空间 = 代理数量 * 每个broker的存储空间。  当oper_type类型是storage时，代理数量不变，每个broker存储空间最少扩容100GB。  当oper_type类型是horizontal时，每个broker的存储空间不变。

        :return: The new_storage_space of this ResizeEngineInstanceReq.
        :rtype: int
        """
        return self._new_storage_space

    @new_storage_space.setter
    def new_storage_space(self, new_storage_space):
        """Sets the new_storage_space of this ResizeEngineInstanceReq.

        扩容后的存储空间。  当oper_type类型是storage或horizontal时，该参数有效且必填。  实例存储空间 = 代理数量 * 每个broker的存储空间。  当oper_type类型是storage时，代理数量不变，每个broker存储空间最少扩容100GB。  当oper_type类型是horizontal时，每个broker的存储空间不变。

        :param new_storage_space: The new_storage_space of this ResizeEngineInstanceReq.
        :type new_storage_space: int
        """
        self._new_storage_space = new_storage_space

    @property
    def new_broker_num(self):
        """Gets the new_broker_num of this ResizeEngineInstanceReq.

        当oper_type参数为horizontal时，该参数有效。  取值范围：最多支持30个broker。

        :return: The new_broker_num of this ResizeEngineInstanceReq.
        :rtype: int
        """
        return self._new_broker_num

    @new_broker_num.setter
    def new_broker_num(self, new_broker_num):
        """Sets the new_broker_num of this ResizeEngineInstanceReq.

        当oper_type参数为horizontal时，该参数有效。  取值范围：最多支持30个broker。

        :param new_broker_num: The new_broker_num of this ResizeEngineInstanceReq.
        :type new_broker_num: int
        """
        self._new_broker_num = new_broker_num

    @property
    def new_product_id(self):
        """Gets the new_product_id of this ResizeEngineInstanceReq.

        垂直扩容时的新产品ID。  当oper_type类型是vertical时，该参数才有效且必填。

        :return: The new_product_id of this ResizeEngineInstanceReq.
        :rtype: str
        """
        return self._new_product_id

    @new_product_id.setter
    def new_product_id(self, new_product_id):
        """Sets the new_product_id of this ResizeEngineInstanceReq.

        垂直扩容时的新产品ID。  当oper_type类型是vertical时，该参数才有效且必填。

        :param new_product_id: The new_product_id of this ResizeEngineInstanceReq.
        :type new_product_id: str
        """
        self._new_product_id = new_product_id

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
        if not isinstance(other, ResizeEngineInstanceReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
