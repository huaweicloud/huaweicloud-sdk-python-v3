# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CustomMetrics:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        '_exec': 'ModelExec',
        'http_get': 'HttpGet'
    }

    attribute_map = {
        '_exec': 'exec',
        'http_get': 'http_get'
    }

    def __init__(self, _exec=None, http_get=None):
        r"""CustomMetrics

        The model defined in huaweicloud sdk

        :param _exec: 
        :type _exec: :class:`huaweicloudsdkmodelarts.v1.ModelExec`
        :param http_get: 
        :type http_get: :class:`huaweicloudsdkmodelarts.v1.HttpGet`
        """
        
        

        self.__exec = None
        self._http_get = None
        self.discriminator = None

        if _exec is not None:
            self._exec = _exec
        if http_get is not None:
            self.http_get = http_get

    @property
    def _exec(self):
        r"""Gets the _exec of this CustomMetrics.

        :return: The _exec of this CustomMetrics.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ModelExec`
        """
        return self.__exec

    @_exec.setter
    def _exec(self, _exec):
        r"""Sets the _exec of this CustomMetrics.

        :param _exec: The _exec of this CustomMetrics.
        :type _exec: :class:`huaweicloudsdkmodelarts.v1.ModelExec`
        """
        self.__exec = _exec

    @property
    def http_get(self):
        r"""Gets the http_get of this CustomMetrics.

        :return: The http_get of this CustomMetrics.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.HttpGet`
        """
        return self._http_get

    @http_get.setter
    def http_get(self, http_get):
        r"""Sets the http_get of this CustomMetrics.

        :param http_get: The http_get of this CustomMetrics.
        :type http_get: :class:`huaweicloudsdkmodelarts.v1.HttpGet`
        """
        self._http_get = http_get

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CustomMetrics):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
