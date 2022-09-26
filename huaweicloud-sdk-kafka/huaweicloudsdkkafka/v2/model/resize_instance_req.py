# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResizeInstanceReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'new_spec_code': 'str',
        'new_storage_space': 'int',
        'oper_type': 'str',
        'new_broker_num': 'int',
        'new_product_id': 'str'
    }

    attribute_map = {
        'new_spec_code': 'new_spec_code',
        'new_storage_space': 'new_storage_space',
        'oper_type': 'oper_type',
        'new_broker_num': 'new_broker_num',
        'new_product_id': 'new_product_id'
    }

    def __init__(self, new_spec_code=None, new_storage_space=None, oper_type=None, new_broker_num=None, new_product_id=None):
        """ResizeInstanceReq

        The model defined in huaweicloud sdk

        :param new_spec_code: 规格变更后的规格ID。 若只扩展磁盘大小，则规格ID保持和原实例不变。
        :type new_spec_code: str
        :param new_storage_space: 规格变更后的消息存储空间，单位：GB。 若扩展实例基准带宽，则new_storage_space不能低于基准带宽规定的最小磁盘大小。
        :type new_storage_space: int
        :param oper_type: 扩容类型, 新规格支持扩容类型：\&quot;horizontal\&quot;、\&quot;vertical\&quot;、\&quot;node\&quot;、\&quot;storage\&quot;四种类型。
        :type oper_type: str
        :param new_broker_num: 扩容后集群节点数。
        :type new_broker_num: int
        :param new_product_id: 新规格变更后的产品ID。 涉及垂直扩容场景，需指定该项。
        :type new_product_id: str
        """
        
        

        self._new_spec_code = None
        self._new_storage_space = None
        self._oper_type = None
        self._new_broker_num = None
        self._new_product_id = None
        self.discriminator = None

        if new_spec_code is not None:
            self.new_spec_code = new_spec_code
        if new_storage_space is not None:
            self.new_storage_space = new_storage_space
        if oper_type is not None:
            self.oper_type = oper_type
        if new_broker_num is not None:
            self.new_broker_num = new_broker_num
        if new_product_id is not None:
            self.new_product_id = new_product_id

    @property
    def new_spec_code(self):
        """Gets the new_spec_code of this ResizeInstanceReq.

        规格变更后的规格ID。 若只扩展磁盘大小，则规格ID保持和原实例不变。

        :return: The new_spec_code of this ResizeInstanceReq.
        :rtype: str
        """
        return self._new_spec_code

    @new_spec_code.setter
    def new_spec_code(self, new_spec_code):
        """Sets the new_spec_code of this ResizeInstanceReq.

        规格变更后的规格ID。 若只扩展磁盘大小，则规格ID保持和原实例不变。

        :param new_spec_code: The new_spec_code of this ResizeInstanceReq.
        :type new_spec_code: str
        """
        self._new_spec_code = new_spec_code

    @property
    def new_storage_space(self):
        """Gets the new_storage_space of this ResizeInstanceReq.

        规格变更后的消息存储空间，单位：GB。 若扩展实例基准带宽，则new_storage_space不能低于基准带宽规定的最小磁盘大小。

        :return: The new_storage_space of this ResizeInstanceReq.
        :rtype: int
        """
        return self._new_storage_space

    @new_storage_space.setter
    def new_storage_space(self, new_storage_space):
        """Sets the new_storage_space of this ResizeInstanceReq.

        规格变更后的消息存储空间，单位：GB。 若扩展实例基准带宽，则new_storage_space不能低于基准带宽规定的最小磁盘大小。

        :param new_storage_space: The new_storage_space of this ResizeInstanceReq.
        :type new_storage_space: int
        """
        self._new_storage_space = new_storage_space

    @property
    def oper_type(self):
        """Gets the oper_type of this ResizeInstanceReq.

        扩容类型, 新规格支持扩容类型：\"horizontal\"、\"vertical\"、\"node\"、\"storage\"四种类型。

        :return: The oper_type of this ResizeInstanceReq.
        :rtype: str
        """
        return self._oper_type

    @oper_type.setter
    def oper_type(self, oper_type):
        """Sets the oper_type of this ResizeInstanceReq.

        扩容类型, 新规格支持扩容类型：\"horizontal\"、\"vertical\"、\"node\"、\"storage\"四种类型。

        :param oper_type: The oper_type of this ResizeInstanceReq.
        :type oper_type: str
        """
        self._oper_type = oper_type

    @property
    def new_broker_num(self):
        """Gets the new_broker_num of this ResizeInstanceReq.

        扩容后集群节点数。

        :return: The new_broker_num of this ResizeInstanceReq.
        :rtype: int
        """
        return self._new_broker_num

    @new_broker_num.setter
    def new_broker_num(self, new_broker_num):
        """Sets the new_broker_num of this ResizeInstanceReq.

        扩容后集群节点数。

        :param new_broker_num: The new_broker_num of this ResizeInstanceReq.
        :type new_broker_num: int
        """
        self._new_broker_num = new_broker_num

    @property
    def new_product_id(self):
        """Gets the new_product_id of this ResizeInstanceReq.

        新规格变更后的产品ID。 涉及垂直扩容场景，需指定该项。

        :return: The new_product_id of this ResizeInstanceReq.
        :rtype: str
        """
        return self._new_product_id

    @new_product_id.setter
    def new_product_id(self, new_product_id):
        """Sets the new_product_id of this ResizeInstanceReq.

        新规格变更后的产品ID。 涉及垂直扩容场景，需指定该项。

        :param new_product_id: The new_product_id of this ResizeInstanceReq.
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
        if not isinstance(other, ResizeInstanceReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
