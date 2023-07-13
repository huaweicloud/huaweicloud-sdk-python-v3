# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SyncObjectReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'object_keys': 'list[str]'
    }

    attribute_map = {
        'object_keys': 'object_keys'
    }

    def __init__(self, object_keys=None):
        """SyncObjectReq

        The model defined in huaweicloud sdk

        :param object_keys: 待同步对象的列表,其中待同步对象最大数量为10,列表中object_key为URL编码处理后的结果
        :type object_keys: list[str]
        """
        
        

        self._object_keys = None
        self.discriminator = None

        self.object_keys = object_keys

    @property
    def object_keys(self):
        """Gets the object_keys of this SyncObjectReq.

        待同步对象的列表,其中待同步对象最大数量为10,列表中object_key为URL编码处理后的结果

        :return: The object_keys of this SyncObjectReq.
        :rtype: list[str]
        """
        return self._object_keys

    @object_keys.setter
    def object_keys(self, object_keys):
        """Sets the object_keys of this SyncObjectReq.

        待同步对象的列表,其中待同步对象最大数量为10,列表中object_key为URL编码处理后的结果

        :param object_keys: The object_keys of this SyncObjectReq.
        :type object_keys: list[str]
        """
        self._object_keys = object_keys

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
        if not isinstance(other, SyncObjectReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
