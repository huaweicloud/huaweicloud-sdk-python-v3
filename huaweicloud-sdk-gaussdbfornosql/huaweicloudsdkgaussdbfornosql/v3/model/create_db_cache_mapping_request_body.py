# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateDbCacheMappingRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'source_instance_id': 'str',
        'target_instance_id': 'str'
    }

    attribute_map = {
        'source_instance_id': 'source_instance_id',
        'target_instance_id': 'target_instance_id'
    }

    def __init__(self, source_instance_id=None, target_instance_id=None):
        r"""CreateDbCacheMappingRequestBody

        The model defined in huaweicloud sdk

        :param source_instance_id: 内存加速源实例ID。当前支持云数据库RDS for MySQL和GaussDB(for MySQL)实例。
        :type source_instance_id: str
        :param target_instance_id: 内存加速目标实例ID。当前仅支持GeminiDB Redis主备类型实例。
        :type target_instance_id: str
        """
        
        

        self._source_instance_id = None
        self._target_instance_id = None
        self.discriminator = None

        self.source_instance_id = source_instance_id
        self.target_instance_id = target_instance_id

    @property
    def source_instance_id(self):
        r"""Gets the source_instance_id of this CreateDbCacheMappingRequestBody.

        内存加速源实例ID。当前支持云数据库RDS for MySQL和GaussDB(for MySQL)实例。

        :return: The source_instance_id of this CreateDbCacheMappingRequestBody.
        :rtype: str
        """
        return self._source_instance_id

    @source_instance_id.setter
    def source_instance_id(self, source_instance_id):
        r"""Sets the source_instance_id of this CreateDbCacheMappingRequestBody.

        内存加速源实例ID。当前支持云数据库RDS for MySQL和GaussDB(for MySQL)实例。

        :param source_instance_id: The source_instance_id of this CreateDbCacheMappingRequestBody.
        :type source_instance_id: str
        """
        self._source_instance_id = source_instance_id

    @property
    def target_instance_id(self):
        r"""Gets the target_instance_id of this CreateDbCacheMappingRequestBody.

        内存加速目标实例ID。当前仅支持GeminiDB Redis主备类型实例。

        :return: The target_instance_id of this CreateDbCacheMappingRequestBody.
        :rtype: str
        """
        return self._target_instance_id

    @target_instance_id.setter
    def target_instance_id(self, target_instance_id):
        r"""Sets the target_instance_id of this CreateDbCacheMappingRequestBody.

        内存加速目标实例ID。当前仅支持GeminiDB Redis主备类型实例。

        :param target_instance_id: The target_instance_id of this CreateDbCacheMappingRequestBody.
        :type target_instance_id: str
        """
        self._target_instance_id = target_instance_id

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
        if not isinstance(other, CreateDbCacheMappingRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
