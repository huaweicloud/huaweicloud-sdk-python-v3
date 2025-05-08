# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PutKv:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'oper_id': 'int',
        'kv_doc': 'dict',
        'kv_blob': 'KvBlob',
        'condition_expression': 'ConditionExpression'
    }

    attribute_map = {
        'oper_id': 'oper_id',
        'kv_doc': 'kv_doc',
        'kv_blob': 'kv_blob',
        'condition_expression': 'condition_expression'
    }

    def __init__(self, oper_id=None, kv_doc=None, kv_blob=None, condition_expression=None):
        r"""PutKv

        The model defined in huaweicloud sdk

        :param oper_id: 请求内的操作编码，未成功的操作返回该标识。
        :type oper_id: int
        :param kv_doc: 用户文档。
        :type kv_doc: dict
        :param kv_blob: 
        :type kv_blob: :class:`huaweicloudsdkkvs.v1.KvBlob`
        :param condition_expression: 
        :type condition_expression: :class:`huaweicloudsdkkvs.v1.ConditionExpression`
        """
        
        

        self._oper_id = None
        self._kv_doc = None
        self._kv_blob = None
        self._condition_expression = None
        self.discriminator = None

        self.oper_id = oper_id
        if kv_doc is not None:
            self.kv_doc = kv_doc
        if kv_blob is not None:
            self.kv_blob = kv_blob
        if condition_expression is not None:
            self.condition_expression = condition_expression

    @property
    def oper_id(self):
        r"""Gets the oper_id of this PutKv.

        请求内的操作编码，未成功的操作返回该标识。

        :return: The oper_id of this PutKv.
        :rtype: int
        """
        return self._oper_id

    @oper_id.setter
    def oper_id(self, oper_id):
        r"""Sets the oper_id of this PutKv.

        请求内的操作编码，未成功的操作返回该标识。

        :param oper_id: The oper_id of this PutKv.
        :type oper_id: int
        """
        self._oper_id = oper_id

    @property
    def kv_doc(self):
        r"""Gets the kv_doc of this PutKv.

        用户文档。

        :return: The kv_doc of this PutKv.
        :rtype: dict
        """
        return self._kv_doc

    @kv_doc.setter
    def kv_doc(self, kv_doc):
        r"""Sets the kv_doc of this PutKv.

        用户文档。

        :param kv_doc: The kv_doc of this PutKv.
        :type kv_doc: dict
        """
        self._kv_doc = kv_doc

    @property
    def kv_blob(self):
        r"""Gets the kv_blob of this PutKv.

        :return: The kv_blob of this PutKv.
        :rtype: :class:`huaweicloudsdkkvs.v1.KvBlob`
        """
        return self._kv_blob

    @kv_blob.setter
    def kv_blob(self, kv_blob):
        r"""Sets the kv_blob of this PutKv.

        :param kv_blob: The kv_blob of this PutKv.
        :type kv_blob: :class:`huaweicloudsdkkvs.v1.KvBlob`
        """
        self._kv_blob = kv_blob

    @property
    def condition_expression(self):
        r"""Gets the condition_expression of this PutKv.

        :return: The condition_expression of this PutKv.
        :rtype: :class:`huaweicloudsdkkvs.v1.ConditionExpression`
        """
        return self._condition_expression

    @condition_expression.setter
    def condition_expression(self, condition_expression):
        r"""Sets the condition_expression of this PutKv.

        :param condition_expression: The condition_expression of this PutKv.
        :type condition_expression: :class:`huaweicloudsdkkvs.v1.ConditionExpression`
        """
        self._condition_expression = condition_expression

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
        if not isinstance(other, PutKv):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
