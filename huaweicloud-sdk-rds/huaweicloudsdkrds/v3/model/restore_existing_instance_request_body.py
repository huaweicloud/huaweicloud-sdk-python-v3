# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RestoreExistingInstanceRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'source': 'RestoreExistingInstanceRequestBodySource',
        'target': 'TargetInstanceRequest'
    }

    attribute_map = {
        'source': 'source',
        'target': 'target'
    }

    def __init__(self, source=None, target=None):
        """RestoreExistingInstanceRequestBody

        The model defined in huaweicloud sdk

        :param source: 
        :type source: :class:`huaweicloudsdkrds.v3.RestoreExistingInstanceRequestBodySource`
        :param target: 
        :type target: :class:`huaweicloudsdkrds.v3.TargetInstanceRequest`
        """
        
        

        self._source = None
        self._target = None
        self.discriminator = None

        self.source = source
        self.target = target

    @property
    def source(self):
        """Gets the source of this RestoreExistingInstanceRequestBody.

        :return: The source of this RestoreExistingInstanceRequestBody.
        :rtype: :class:`huaweicloudsdkrds.v3.RestoreExistingInstanceRequestBodySource`
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this RestoreExistingInstanceRequestBody.

        :param source: The source of this RestoreExistingInstanceRequestBody.
        :type source: :class:`huaweicloudsdkrds.v3.RestoreExistingInstanceRequestBodySource`
        """
        self._source = source

    @property
    def target(self):
        """Gets the target of this RestoreExistingInstanceRequestBody.

        :return: The target of this RestoreExistingInstanceRequestBody.
        :rtype: :class:`huaweicloudsdkrds.v3.TargetInstanceRequest`
        """
        return self._target

    @target.setter
    def target(self, target):
        """Sets the target of this RestoreExistingInstanceRequestBody.

        :param target: The target of this RestoreExistingInstanceRequestBody.
        :type target: :class:`huaweicloudsdkrds.v3.TargetInstanceRequest`
        """
        self._target = target

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
        if not isinstance(other, RestoreExistingInstanceRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
