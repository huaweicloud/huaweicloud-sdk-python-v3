# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OperItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'put_kv': 'PutKv',
        'delete_kv': 'DeleteKv',
        'update_kv': 'UpdateKv'
    }

    attribute_map = {
        'put_kv': 'put_kv',
        'delete_kv': 'delete_kv',
        'update_kv': 'update_kv'
    }

    def __init__(self, put_kv=None, delete_kv=None, update_kv=None):
        r"""OperItem

        The model defined in huaweicloud sdk

        :param put_kv: 
        :type put_kv: :class:`huaweicloudsdkkvs.v1.PutKv`
        :param delete_kv: 
        :type delete_kv: :class:`huaweicloudsdkkvs.v1.DeleteKv`
        :param update_kv: 
        :type update_kv: :class:`huaweicloudsdkkvs.v1.UpdateKv`
        """
        
        

        self._put_kv = None
        self._delete_kv = None
        self._update_kv = None
        self.discriminator = None

        if put_kv is not None:
            self.put_kv = put_kv
        if delete_kv is not None:
            self.delete_kv = delete_kv
        if update_kv is not None:
            self.update_kv = update_kv

    @property
    def put_kv(self):
        r"""Gets the put_kv of this OperItem.

        :return: The put_kv of this OperItem.
        :rtype: :class:`huaweicloudsdkkvs.v1.PutKv`
        """
        return self._put_kv

    @put_kv.setter
    def put_kv(self, put_kv):
        r"""Sets the put_kv of this OperItem.

        :param put_kv: The put_kv of this OperItem.
        :type put_kv: :class:`huaweicloudsdkkvs.v1.PutKv`
        """
        self._put_kv = put_kv

    @property
    def delete_kv(self):
        r"""Gets the delete_kv of this OperItem.

        :return: The delete_kv of this OperItem.
        :rtype: :class:`huaweicloudsdkkvs.v1.DeleteKv`
        """
        return self._delete_kv

    @delete_kv.setter
    def delete_kv(self, delete_kv):
        r"""Sets the delete_kv of this OperItem.

        :param delete_kv: The delete_kv of this OperItem.
        :type delete_kv: :class:`huaweicloudsdkkvs.v1.DeleteKv`
        """
        self._delete_kv = delete_kv

    @property
    def update_kv(self):
        r"""Gets the update_kv of this OperItem.

        :return: The update_kv of this OperItem.
        :rtype: :class:`huaweicloudsdkkvs.v1.UpdateKv`
        """
        return self._update_kv

    @update_kv.setter
    def update_kv(self, update_kv):
        r"""Sets the update_kv of this OperItem.

        :param update_kv: The update_kv of this OperItem.
        :type update_kv: :class:`huaweicloudsdkkvs.v1.UpdateKv`
        """
        self._update_kv = update_kv

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
        if not isinstance(other, OperItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
