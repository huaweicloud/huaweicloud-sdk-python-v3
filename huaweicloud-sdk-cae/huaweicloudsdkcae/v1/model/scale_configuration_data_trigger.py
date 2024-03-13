# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ScaleConfigurationDataTrigger:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'metadata': 'ScalingTriggerMeta'
    }

    attribute_map = {
        'type': 'type',
        'metadata': 'metadata'
    }

    def __init__(self, type=None, metadata=None):
        """ScaleConfigurationDataTrigger

        The model defined in huaweicloud sdk

        :param type: 指标类型。
        :type type: str
        :param metadata: 
        :type metadata: :class:`huaweicloudsdkcae.v1.ScalingTriggerMeta`
        """
        
        

        self._type = None
        self._metadata = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if metadata is not None:
            self.metadata = metadata

    @property
    def type(self):
        """Gets the type of this ScaleConfigurationDataTrigger.

        指标类型。

        :return: The type of this ScaleConfigurationDataTrigger.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ScaleConfigurationDataTrigger.

        指标类型。

        :param type: The type of this ScaleConfigurationDataTrigger.
        :type type: str
        """
        self._type = type

    @property
    def metadata(self):
        """Gets the metadata of this ScaleConfigurationDataTrigger.

        :return: The metadata of this ScaleConfigurationDataTrigger.
        :rtype: :class:`huaweicloudsdkcae.v1.ScalingTriggerMeta`
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this ScaleConfigurationDataTrigger.

        :param metadata: The metadata of this ScaleConfigurationDataTrigger.
        :type metadata: :class:`huaweicloudsdkcae.v1.ScalingTriggerMeta`
        """
        self._metadata = metadata

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
        if not isinstance(other, ScaleConfigurationDataTrigger):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
