# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class KvOperIds:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'put_kv_ids': 'list[int]',
        'delete_kv_ids': 'list[int]',
        'update_kv_ids': 'list[int]'
    }

    attribute_map = {
        'put_kv_ids': 'put_kv_ids',
        'delete_kv_ids': 'delete_kv_ids',
        'update_kv_ids': 'update_kv_ids'
    }

    def __init__(self, put_kv_ids=None, delete_kv_ids=None, update_kv_ids=None):
        r"""KvOperIds

        The model defined in huaweicloud sdk

        :param put_kv_ids: 上传kv操作, \&quot;oper_id\&quot;数组。 - 数组元素：请求内的操作编码，未成功的操作返回该标识。
        :type put_kv_ids: list[int]
        :param delete_kv_ids: 请求内的操作编码，未成功的操作返回该标识。 - 数组元素：请求内的操作编码，未成功的操作返回该标识。
        :type delete_kv_ids: list[int]
        :param update_kv_ids: 请求内的操作编码，未成功的操作返回该标识。 - 数组元素：请求内的操作编码，未成功的操作返回该标识。
        :type update_kv_ids: list[int]
        """
        
        

        self._put_kv_ids = None
        self._delete_kv_ids = None
        self._update_kv_ids = None
        self.discriminator = None

        if put_kv_ids is not None:
            self.put_kv_ids = put_kv_ids
        if delete_kv_ids is not None:
            self.delete_kv_ids = delete_kv_ids
        if update_kv_ids is not None:
            self.update_kv_ids = update_kv_ids

    @property
    def put_kv_ids(self):
        r"""Gets the put_kv_ids of this KvOperIds.

        上传kv操作, \"oper_id\"数组。 - 数组元素：请求内的操作编码，未成功的操作返回该标识。

        :return: The put_kv_ids of this KvOperIds.
        :rtype: list[int]
        """
        return self._put_kv_ids

    @put_kv_ids.setter
    def put_kv_ids(self, put_kv_ids):
        r"""Sets the put_kv_ids of this KvOperIds.

        上传kv操作, \"oper_id\"数组。 - 数组元素：请求内的操作编码，未成功的操作返回该标识。

        :param put_kv_ids: The put_kv_ids of this KvOperIds.
        :type put_kv_ids: list[int]
        """
        self._put_kv_ids = put_kv_ids

    @property
    def delete_kv_ids(self):
        r"""Gets the delete_kv_ids of this KvOperIds.

        请求内的操作编码，未成功的操作返回该标识。 - 数组元素：请求内的操作编码，未成功的操作返回该标识。

        :return: The delete_kv_ids of this KvOperIds.
        :rtype: list[int]
        """
        return self._delete_kv_ids

    @delete_kv_ids.setter
    def delete_kv_ids(self, delete_kv_ids):
        r"""Sets the delete_kv_ids of this KvOperIds.

        请求内的操作编码，未成功的操作返回该标识。 - 数组元素：请求内的操作编码，未成功的操作返回该标识。

        :param delete_kv_ids: The delete_kv_ids of this KvOperIds.
        :type delete_kv_ids: list[int]
        """
        self._delete_kv_ids = delete_kv_ids

    @property
    def update_kv_ids(self):
        r"""Gets the update_kv_ids of this KvOperIds.

        请求内的操作编码，未成功的操作返回该标识。 - 数组元素：请求内的操作编码，未成功的操作返回该标识。

        :return: The update_kv_ids of this KvOperIds.
        :rtype: list[int]
        """
        return self._update_kv_ids

    @update_kv_ids.setter
    def update_kv_ids(self, update_kv_ids):
        r"""Sets the update_kv_ids of this KvOperIds.

        请求内的操作编码，未成功的操作返回该标识。 - 数组元素：请求内的操作编码，未成功的操作返回该标识。

        :param update_kv_ids: The update_kv_ids of this KvOperIds.
        :type update_kv_ids: list[int]
        """
        self._update_kv_ids = update_kv_ids

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
        if not isinstance(other, KvOperIds):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
