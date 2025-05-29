# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchGetKvRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'batch_get_kv_opers': 'list[BatchGetKvOfTable]'
    }

    attribute_map = {
        'batch_get_kv_opers': 'batch_get_kv_opers'
    }

    def __init__(self, batch_get_kv_opers=None):
        r"""BatchGetKvRequestBody

        The model defined in huaweicloud sdk

        :param batch_get_kv_opers: 按照table分类组织的get操作。
        :type batch_get_kv_opers: list[:class:`huaweicloudsdkkvs.v1.BatchGetKvOfTable`]
        """
        
        

        self._batch_get_kv_opers = None
        self.discriminator = None

        self.batch_get_kv_opers = batch_get_kv_opers

    @property
    def batch_get_kv_opers(self):
        r"""Gets the batch_get_kv_opers of this BatchGetKvRequestBody.

        按照table分类组织的get操作。

        :return: The batch_get_kv_opers of this BatchGetKvRequestBody.
        :rtype: list[:class:`huaweicloudsdkkvs.v1.BatchGetKvOfTable`]
        """
        return self._batch_get_kv_opers

    @batch_get_kv_opers.setter
    def batch_get_kv_opers(self, batch_get_kv_opers):
        r"""Sets the batch_get_kv_opers of this BatchGetKvRequestBody.

        按照table分类组织的get操作。

        :param batch_get_kv_opers: The batch_get_kv_opers of this BatchGetKvRequestBody.
        :type batch_get_kv_opers: list[:class:`huaweicloudsdkkvs.v1.BatchGetKvOfTable`]
        """
        self._batch_get_kv_opers = batch_get_kv_opers

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
        if not isinstance(other, BatchGetKvRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
