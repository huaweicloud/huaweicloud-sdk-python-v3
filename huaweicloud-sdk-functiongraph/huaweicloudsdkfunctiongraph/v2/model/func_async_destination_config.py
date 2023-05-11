# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FuncAsyncDestinationConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'on_success': 'FuncDestinationConfig',
        'on_failure': 'FuncDestinationConfig'
    }

    attribute_map = {
        'on_success': 'on_success',
        'on_failure': 'on_failure'
    }

    def __init__(self, on_success=None, on_failure=None):
        """FuncAsyncDestinationConfig

        The model defined in huaweicloud sdk

        :param on_success: 
        :type on_success: :class:`huaweicloudsdkfunctiongraph.v2.FuncDestinationConfig`
        :param on_failure: 
        :type on_failure: :class:`huaweicloudsdkfunctiongraph.v2.FuncDestinationConfig`
        """
        
        

        self._on_success = None
        self._on_failure = None
        self.discriminator = None

        if on_success is not None:
            self.on_success = on_success
        if on_failure is not None:
            self.on_failure = on_failure

    @property
    def on_success(self):
        """Gets the on_success of this FuncAsyncDestinationConfig.

        :return: The on_success of this FuncAsyncDestinationConfig.
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.FuncDestinationConfig`
        """
        return self._on_success

    @on_success.setter
    def on_success(self, on_success):
        """Sets the on_success of this FuncAsyncDestinationConfig.

        :param on_success: The on_success of this FuncAsyncDestinationConfig.
        :type on_success: :class:`huaweicloudsdkfunctiongraph.v2.FuncDestinationConfig`
        """
        self._on_success = on_success

    @property
    def on_failure(self):
        """Gets the on_failure of this FuncAsyncDestinationConfig.

        :return: The on_failure of this FuncAsyncDestinationConfig.
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.FuncDestinationConfig`
        """
        return self._on_failure

    @on_failure.setter
    def on_failure(self, on_failure):
        """Sets the on_failure of this FuncAsyncDestinationConfig.

        :param on_failure: The on_failure of this FuncAsyncDestinationConfig.
        :type on_failure: :class:`huaweicloudsdkfunctiongraph.v2.FuncDestinationConfig`
        """
        self._on_failure = on_failure

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
        if not isinstance(other, FuncAsyncDestinationConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
